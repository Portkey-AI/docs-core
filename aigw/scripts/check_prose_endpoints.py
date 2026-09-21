#!/usr/bin/env python3
"""Assert that every endpoint written in `aigw/` prose exists in the specification.

The gap this closes. On 2026-09-18 the spec repo dropped the scope segment from the
API key create path: `POST /api-keys/{type}/{sub-type}` became `POST /api-keys/{sub-type}`.
`sync_api_nav.py` caught the navigation and `mint validate` caught the stale navigation
entry, because both compare structure against structure. Neither could see that a
sentence still called the level a path parameter, or that a worked `curl` still posted
to `/api-keys/organisation/service`. Those were found by reading. This finds them by
running.

The failure mode is what makes it worth automating: a page describing an endpoint that
no longer exists still reads perfectly well. Nothing looks wrong until a reader copies
the request and gets a 404.

Source of truth is `docs-navigation.json` from the spec repo -- the same document
`sync_api_nav.py` reads, and the reason this script needs no YAML parser. It names every
operation as a `"METHOD /path"` string, which is exactly the set being checked against.

Matching is deliberately loose, because prose is not a specification:

  - Base prefixes are stripped. The spec's paths are relative to a server URL, so prose
    writes `POST /v1/chat/completions` and `POST /ai_gw/v2/api-keys/service` for what the
    spec calls `POST /chat/completions` and `POST /api-keys/{sub-type}`.
  - A `{placeholder}` segment in the spec matches any single segment, so a worked example
    using a real value -- `/api-keys/service`, `/configs/my-config` -- still matches.
  - Trailing slashes are ignored.

Anything genuinely outside the specification goes in ALLOWED below with a reason, never
by loosening the match. An endpoint absent from both is an error, and there are only
three honest resolutions: the prose is stale, the spec is missing something, or it
belongs in ALLOWED.

Usage:
    aigw/scripts/check_prose_endpoints.py             non-zero if any endpoint is unknown
    aigw/scripts/check_prose_endpoints.py --list      print every endpoint found, with its match
    aigw/scripts/check_prose_endpoints.py --from PATH read the fragment from a local checkout
"""

import argparse
import json
import os
import re
import sys
import urllib.request

FRAGMENT_URL = ("https://raw.githubusercontent.com/PaloAltoNetworks/openapi/"
                "refs/heads/main/docs-navigation.json")

AIGW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# Server prefixes the spec factors out into `servers`, so prose carries them and the
# operation paths do not. Longest first -- `/ai_gw/admin/v2` must win over `/ai_gw`.
BASE_PREFIXES = [
    "/ai_gw/admin/v2",
    "/ai_gw/v2",
    "/admin/v2",
    "/ai_gw",
    "/v2",
    "/v1",
]

# Endpoints correctly absent from the specification, because the specification was never
# the place for them. Each needs a reason; an entry without one is indistinguishable from
# a bug that someone silenced.
ALLOWED = {
    # Not the gateway. Strata Cloud Manager issues Admin API tokens from a Palo Alto
    # identity host, documented in admin-api/authentication.mdx.
    "POST /oauth2/access_token": "Palo Alto identity service, not the gateway",
    "GET /iam/v1/access_policies": "Palo Alto IAM API, not the gateway",
    "DELETE /iam/v1/access_policies/{id}": "Palo Alto IAM API, not the gateway",
    "GET /oauth/authorize": "generic OAuth authorisation endpoint, not a gateway route",

    # Prompt endpoints are excluded from the specification by design -- they sit in the
    # spec repo's _project/drops.yaml and its build fails if one reappears. That prose
    # still documents them is a separate question, tracked in TODO.md rather than here.
    "POST /prompts/{promptId}/completions": "prompt endpoints dropped upstream by design",

    # Other gateway planes. The MCP Gateway serves /m and the Agent Gateway /agent; this
    # specification covers the inference and admin planes only. Real routes, wrong
    # document -- see the note in TODO.md about whether they should have one.
    "GET /m/v0.1/servers": "MCP Gateway registry, served from /m, not in this spec",
    "POST /m/oauth/token": "MCP Gateway OAuth, served from /m, not in this spec",
    "POST /agent/{agent-slug}": "Agent Gateway, served from /agent, not in this spec",
    "POST /agent/{agent-slug}/.well-known/agent.json":
        "Agent Gateway discovery, served from /agent, not in this spec",

    # SCIM is RFC 7644, with its own schema and its own document.
    "DELETE /scim/Groups/{id}": "SCIM 2.0, governed by RFC 7644",

    # Provider-native routes the gateway proxies rather than implements. It forwards
    # these upstream unchanged, so they are the provider's contract, not ours.
    "POST /messages": "Anthropic-native route, proxied not implemented",
    "POST /messages/batches": "Anthropic-native route, proxied not implemented",
    "GET /messages/batches": "Anthropic-native route, proxied not implemented",
    "GET /messages/batches/{batch_id}": "Anthropic-native route, proxied not implemented",
    "POST /messages/batches/{batch_id}/cancel": "Anthropic-native route, proxied not implemented",
    "POST /messages/count_tokens": "Anthropic-native route, proxied not implemented",
    "POST /endpoints/{endpoint_name}/invocations": "SageMaker-native route, proxied",
    "PUT /knowledgebases": "Bedrock Knowledge Base route, proxied",
    "POST /knowledgebases/{knowledgeBaseId}/retrieve": "Bedrock Knowledge Base route, proxied",
    "POST /listen": "Deepgram-native route, proxied",
    "POST /predictions": "Replicate-native route, proxied",
    "POST /projects/{project}/locations/{location}/cachedContents": "Vertex-native route, proxied",
    "POST /v2/vectordb/collections/list": "Milvus-native route, proxied",
    "POST /v2/videos": "Together-native route, proxied",
}

# Endpoints that *should* be in the specification and are not. Unlike ALLOWED, every line
# here is a defect someone owns upstream -- the docs describe a real feature the spec does
# not admit exists, so nothing generates a reference page for it and nothing can verify
# the prose. Kept as a baseline that may only shrink: a new absence fails the check, and
# an entry that starts matching nothing also fails, so these get deleted when they land.
KNOWN_GAPS = {
    "POST /logs/exports": "Logs Export API absent from the spec",
    "GET /logs/exports/field-restrictions": "Logs Export API absent from the spec",
    "GET /logs/exports/{id}": "Logs Export API absent from the spec",
    "GET /logs/exports/{id}/download": "Logs Export API absent from the spec",
    "POST /logs/exports/{id}/start": "Logs Export API absent from the spec",
    "POST /logs/exports/{id}/cancel": "Logs Export API absent from the spec",
    "DELETE /logs/exports/{id}": "Logs Export API absent from the spec",

    # Only the input side is written as an endpoint. The output-guardrails path appears in
    # the same page as backticked prose, which this check does not read, so an entry for it
    # would match nothing and fail.
    "PUT /workspace-exclusions/input-guardrails": "raised by Phase 7, still absent",
}

# A path segment standing in for a value. The corpus uses all three syntaxes, sometimes
# on the same page: `{file_id}` from the spec, `:apiKeyId` from the older admin docs, and
# `<file_id>` in shell examples. Leaving any of them out truncates the path at the first
# placeholder -- `/v1/files/<file_id>` became `/files`, which then failed as a nonexistent
# endpoint. Every one of the first run's "findings" in this class was that bug.
# A `*` is a placeholder too: prose writes `GET /v1/responses/*` to mean the read routes
# as a set.
PLACEHOLDER = re.compile(r"^(?:\{[^}]*\}|:[A-Za-z_][A-Za-z0-9_]*|<[^>]*>|\*)$")

PATH_CHARS = r"[A-Za-z0-9_{}<>:./~*-]"

# `METHOD /path`, the way an endpoint is written in prose, a heading or a fence.
PROSE = re.compile(r"\b(GET|POST|PUT|DELETE|PATCH)\s+(/" + PATH_CHARS + r"*)")

# The same thing inside a curl invocation, where the method and the URL are separated by
# flags and the path is buried in a host.
#
# Only these hosts. An earlier version matched any URL and reported 494 failures, nearly
# all of them GitHub links, images and third-party documentation -- which is the shape of
# a check nobody runs twice. The gateway's own hosts are the only ones whose paths this
# repository is entitled to have an opinion about.
API_HOSTS = (
    "aigw.portkey.ai",
    "api.apps.paloaltonetworks.com",
    "api.portkey.ai",
)
CURL_URL = re.compile(
    r"https?://(?:" + "|".join(re.escape(h) for h in API_HOSTS) + r")(/" + PATH_CHARS + r"*)"
)
CURL_METHOD = re.compile(r"(?:-X|--request)\s+(GET|POST|PUT|DELETE|PATCH)\b")
# curl sends POST when given a body, with no -X at all. Most examples in this corpus are
# written that way, so inferring GET from the absence of -X reports every one of them as
# a nonexistent GET endpoint.
CURL_BODY = re.compile(r"(?:^|\s)(?:-d|--data|--data-raw|--data-binary|--json|-F|--form)\b")


def load_fragment(path):
    if path:
        with open(path) as fh:
            return json.load(fh)
    req = urllib.request.Request(FRAGMENT_URL, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def spec_operations(fragment):
    """Every `"METHOD /path"` string anywhere in the navigation fragment."""
    found = set()

    def walk(node):
        if isinstance(node, dict):
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
        elif isinstance(node, str) and PROSE.fullmatch(node):
            found.add(node)

    walk(fragment)
    return found


def normalise(path):
    """Strip a server prefix and any trailing slash, so prose and spec are comparable."""
    for prefix in BASE_PREFIXES:
        if path == prefix:
            return "/"
        if path.startswith(prefix + "/"):
            path = path[len(prefix):]
            break
    return path.rstrip("/") or "/"


def matches(written, declared):
    """True if a written path fits a declared one, with placeholders as wildcards.

    A placeholder on either side matches anything: `/api-keys/service` fits
    `/api-keys/{sub-type}` because the spec names the segment, and `/files/<file_id>`
    fits `/files/{file_id}` because the example fills it in. `/api-keys/a/b` fits
    neither -- segment counts must agree.
    """
    w = written.strip("/").split("/")
    d = declared.strip("/").split("/")
    if len(w) != len(d):
        return False
    return all(
        PLACEHOLDER.match(ds) or PLACEHOLDER.match(ws) or ds == ws
        for ws, ds in zip(w, d)
    )


def find_match(method, path, declared_by_method):
    for declared in declared_by_method.get(method, ()):
        if matches(path, declared):
            return f"{method} {declared}"
    return None


def curl_commands(lines):
    """Yield (start_line, command_text) for each curl invocation, joined across wrapping.

    A curl example spans many lines held together by trailing backslashes, and the method,
    the body flag and the URL are rarely on the same one. The method has to be decided
    from the whole command or not at all.
    """
    i = 0
    while i < len(lines):
        if re.match(r"\s*curl\b", lines[i]):
            start = i
            parts = [lines[i]]
            while parts[-1].rstrip().endswith("\\") and i + 1 < len(lines):
                i += 1
                parts.append(lines[i])
            yield start + 1, " ".join(parts)
        i += 1


def scan_file(path):
    """Yield (line_number, method, raw_path, method_is_certain) for each endpoint written.

    The method is certain when it is written down -- in prose, or as curl's -X. It is a
    guess when curl omits -X and the method has to come from whether a body is present.
    Documentation examples are routinely abridged to the header being discussed, so a
    POST example with its -d elided looks exactly like a GET. Callers should not fail a
    guess that lands on a real path under some other method.
    """
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    for i, line in enumerate(lines, 1):
        for method, raw in PROSE.findall(line):
            yield i, method, raw, True

    for lineno, command in curl_commands(lines):
        found = CURL_METHOD.search(command)
        if found:
            method, certain = found.group(1), True
        elif CURL_BODY.search(command):
            method, certain = "POST", False
        else:
            method, certain = "GET", False
        for raw in CURL_URL.findall(command):
            if raw and raw != "/":
                yield lineno, method, raw.split("?")[0], certain


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="src", help="read docs-navigation.json from a local path")
    ap.add_argument("--list", action="store_true", help="print every endpoint and its match")
    args = ap.parse_args()

    declared = spec_operations(load_fragment(args.src))
    by_method = {}
    for op in declared:
        method, path = op.split(" ", 1)
        by_method.setdefault(method, []).append(path)

    unknown = {}
    seen = 0
    allowed_hits = set()

    for root, _dirs, files in os.walk(AIGW):
        if "_project" in root:
            continue
        for name in sorted(files):
            if not name.endswith(".mdx"):
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, os.path.join(AIGW, ".."))
            for lineno, method, raw, certain in scan_file(full):
                path = normalise(raw)
                if path == "/":
                    continue
                seen += 1
                key = f"{method} {path}"

                hit = find_match(method, path, by_method)
                if not hit and not certain:
                    # The method was inferred. If the path is real under any method, the
                    # example is fine and the inference was simply wrong.
                    hit = next(
                        (find_match(m, path, by_method) for m in by_method
                         if find_match(m, path, by_method)),
                        None,
                    )
                if hit:
                    if args.list:
                        print(f"  ok       {key:58} -> {hit}")
                    continue

                # Placeholders are wildcards on both sides, so a written `/logs/exports/{id}`
                # matches a listed `/logs/exports/field-restrictions` as readily as the
                # entry meant for it. Prefer whichever candidate agrees on the most literal
                # segments, so the specific entry wins and the general one is not wrongly
                # reported as matching nothing.
                candidates = [
                    a for a in (*ALLOWED, *KNOWN_GAPS)
                    if a.split(" ", 1)[0] == method and matches(path, a.split(" ", 1)[1])
                ]
                listed = max(
                    candidates,
                    key=lambda a: sum(
                        1 for ws, ds in zip(path.strip("/").split("/"),
                                            a.split(" ", 1)[1].strip("/").split("/"))
                        if ws == ds
                    ),
                    default=None,
                )
                if listed:
                    allowed_hits.add(listed)
                    if args.list:
                        why = ALLOWED.get(listed) or KNOWN_GAPS[listed]
                        label = "allowed" if listed in ALLOWED else "gap"
                        print(f"  {label:8} {key:58} -- {why}")
                    continue

                unknown.setdefault(key, []).append(f"{rel}:{lineno}")

    print(f"{seen} endpoint mentions checked against {len(declared)} declared operations")
    allowed_n = len(allowed_hits & set(ALLOWED))
    gaps_n = len(allowed_hits & set(KNOWN_GAPS))
    if allowed_n:
        print(f"{allowed_n} outside the spec by nature (ALLOWED)")
    if gaps_n:
        print(f"{gaps_n} missing from the spec and tracked upstream (KNOWN_GAPS)")

    stale = sorted((set(ALLOWED) | set(KNOWN_GAPS)) - allowed_hits)
    if stale:
        print("\nListed endpoints that matched nothing. Either the prose that needed them")
        print("is gone or the spec now has them -- delete the entry either way:")
        for s in stale:
            print(f"  {s}")

    if not unknown:
        if not stale:
            print("\nEvery endpoint written in aigw/ is accounted for.")
        return 1 if stale else 0

    print(f"\n{len(unknown)} endpoint(s) written in aigw/ are not in the specification:\n")
    for key in sorted(unknown):
        where = unknown[key]
        print(f"  {key}")
        for w in where[:6]:
            print(f"      {w}")
        if len(where) > 6:
            print(f"      ... and {len(where) - 6} more")
    print("\nEither the prose is stale, the spec is missing an operation, or it belongs")
    print("in ALLOWED with a reason. Do not loosen the match to make this pass.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
