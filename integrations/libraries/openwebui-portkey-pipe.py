"""
title: Portkey Manifold Pipe
author: Portkey
version: 0.6.0
license: MIT
documentation: https://portkey.ai/docs/integrations/libraries/openwebui
"""

from pydantic import BaseModel, Field
from typing import Union, Generator, Iterator, List, Dict, Any
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class Pipe:
    class Valves(BaseModel):
        # Auth & endpoint
        PORTKEY_API_KEY: str = Field(
            default="",
            description="Your Portkey API key (required). Will be used as Bearer token."
        )
        PORTKEY_API_BASE_URL: str = Field(
            default="https://api.portkey.ai/v1",
            description="Base URL for the Portkey API (change only for self-hosted)."
        )

        # Models
        AUTO_DISCOVER_MODELS: bool = Field(
            default=True,
            description="If true, fetches models from GET {BASE}/models to fill dropdown."
        )
        PORTKEY_MODELS: str = Field(
            default="@openai-slug/gpt-4o, @anthropic-slug/claude-sonnet-latest",
            description="Comma-separated model IDs (used when auto-discovery is disabled or to augment)."
        )

        # Streaming format
        STREAM_FORMAT: str = Field(
            default="auto",
            description="How to return streamed lines: 'auto' | 'jsonl' | 'sse'. "
                        "'jsonl' strips 'data:' and yields pure JSON per line; "
                        "'sse' passes lines as-is; 'auto' tries to normalize sensibly."
        )

        # Headers / metadata
        FORWARD_USER_INFO_HEADERS: bool = Field(
            default=False,
            description="If true, forwards X-OpenWebUI-* user headers to Portkey."
        )
        SEND_METADATA_HEADER: bool = Field(
            default=True,
            description="If true, sends x-portkey-metadata with user info as JSON."
        )

        # Networking
        REQUEST_TIMEOUT_SECS: int = Field(
            default=600,
            description="HTTP timeout (seconds). Increase for long streams."
        )
        RETRIES_NON_STREAM: int = Field(
            default=3,
            description="Retry count for non-streaming requests (backoff included)."
        )
        RETRY_BACKOFF_FACTOR: float = Field(
            default=0.5,
            description="Seconds factor for exponential backoff (non-stream only)."
        )

    def __init__(self):
        self.type = "manifold"
        self.valves = self.Valves()
        self.name = "PORTKEY"
        self._session = None  # lazy init

    # ---------- utilities ----------

    def _clean_model_id(self, full_model_id: str) -> str:
        # OpenWebUI may prefix the pipe filename; strip it.
        # "portkey_manifold_pipe.@foo/bar" -> "@foo/bar"
        return full_model_id.split(".", 1)[-1] if "." in full_model_id else full_model_id

    def _user_to_metadata(self, __user__: Dict[str, Any]) -> Dict[str, Any]:
        # Harvest user info commonly available from OpenWebUI
        __user__ = __user__ or {}
        meta = {}
        # canonical set
        if "name" in __user__: meta["name"] = __user__["name"]
        if "id" in __user__: meta["id"] = __user__["id"]
        if "email" in __user__: meta["email"] = __user__["email"]
        if "role" in __user__: meta["role"] = __user__["role"]
        if "chat_id" in __user__: meta["chat_id"] = __user__["chat_id"]
        return meta

    def _build_headers(self, __user__: Dict[str, Any]) -> Dict[str, str]:
        if not self.valves.PORTKEY_API_KEY:
            raise Exception("PORTKEY_API_KEY is required. Paste your Portkey API key.")

        headers = {
            "Authorization": f"Bearer {self.valves.PORTKEY_API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "openwebui-portkey-pipe/0.6.0",
        }

        # Optional: forward OpenWebUI X- headers (mirrors ENABLE_FORWARD_USER_INFO_HEADERS behavior)
        if self.valves.FORWARD_USER_INFO_HEADERS and __user__:
            if "name" in __user__:   headers["X-OpenWebUI-User-Name"] = str(__user__["name"])
            if "id" in __user__:     headers["X-OpenWebUI-User-Id"] = str(__user__["id"])
            if "email" in __user__:  headers["X-OpenWebUI-User-Email"] = str(__user__["email"])
            if "role" in __user__:   headers["X-OpenWebUI-User-Role"] = str(__user__["role"])
            if "chat_id" in __user__:headers["X-OpenWebUI-Chat-Id"] = str(__user__["chat_id"])

        # Optional: structured metadata payload for Portkey observability
        if self.valves.SEND_METADATA_HEADER:
            meta = self._user_to_metadata(__user__)
            if meta:
                headers["x-portkey-metadata"] = json.dumps(meta)

        return headers

    def _session_non_stream(self) -> requests.Session:
        # Session with retries for non-stream requests
        if self._session is None:
            s = requests.Session()
            retry = Retry(
                total=self.valves.RETRIES_NON_STREAM,
                read=self.valves.RETRIES_NON_STREAM,
                connect=self.valves.RETRIES_NON_STREAM,
                backoff_factor=self.valves.RETRY_BACKOFF_FACTOR,
                status_forcelist=(429, 500, 502, 503, 504),
                allowed_methods=False,  # allow POST retries
                raise_on_status=False,
            )
            adapter = HTTPAdapter(max_retries=retry)
            s.mount("https://", adapter)
            s.mount("http://", adapter)
            self._session = s
        return self._session

    # ---------- models list for UI ----------

    def _models_from_auto_discovery(self) -> List[str]:
        url = f"{self.valves.PORTKEY_API_BASE_URL}/models"
        try:
            r = self._session_non_stream().get(url, timeout=30)
            r.raise_for_status()
            payload = r.json()
            # Robust extraction: prefer OpenAI-ish shape {"data":[{"id":...}]}
            data = payload.get("data") if isinstance(payload, dict) else None
            if isinstance(data, list):
                ids = [item.get("id") for item in data if isinstance(item, dict) and item.get("id")]
                return [i for i in ids if isinstance(i, str)]
            # Fallbacks
            if isinstance(payload, list):
                # maybe it's already a list of ids or objects
                maybe_ids = []
                for item in payload:
                    if isinstance(item, str):
                        maybe_ids.append(item)
                    elif isinstance(item, dict) and "id" in item and isinstance(item["id"], str):
                        maybe_ids.append(item["id"])
                return maybe_ids
            return []
        except Exception:
            return []

    def pipes(self) -> list:
        model_ids = []

        if self.valves.AUTO_DISCOVER_MODELS:
            model_ids.extend(self._models_from_auto_discovery())

        if self.valves.PORTKEY_MODELS:
            manual = [m.strip() for m in self.valves.PORTKEY_MODELS.split(",") if m.strip()]
            model_ids.extend(manual)

        # De-dup preserve order
        seen = set()
        uniq = []
        for m in model_ids:
            if m not in seen:
                seen.add(m)
                uniq.append(m)

        return [{"id": model_id, "name": model_id} for model_id in uniq]

    # ---------- streaming helpers ----------

    def _normalize_stream_line(self, line: str) -> str:
        """
        Return a single line based on STREAM_FORMAT:
          - 'jsonl': strip leading 'data:' if present; return the JSON payload only.
          - 'sse': return as-is.
          - 'auto': if startswith 'data:', drop the prefix; yield JSON if decodes, else original.
        Lines equal to '[DONE]' are skipped.
        """
        if not line or line.strip() == "[DONE]":
            return ""

        fmt = (self.valves.STREAM_FORMAT or "auto").lower()

        if fmt == "sse":
            return line

        # jsonl or auto
        if line.startswith("data:"):
            line = line[len("data:"):].lstrip()

        if fmt == "jsonl" or fmt == "auto":
            # try to confirm it is JSON; if yes, return compact JSON string
            try:
                obj = json.loads(line)
                return json.dumps(obj, separators=(",", ":"))
            except Exception:
                # not JSON, return as-is in 'auto'; in 'jsonl' still return raw line
                return line

        return line

    def _iter_stream(self, response: requests.Response) -> Iterator[str]:
        for raw in response.iter_lines(decode_unicode=True):
            if raw is None:
                continue
            line = raw.strip()
            if not line:
                continue  # skip keep-alives
            out = self._normalize_stream_line(line)
            if out:
                yield out

    # ---------- main entry ----------

    def pipe(self, body: dict, __user__: dict) -> Union[str, Generator, Iterator]:
        # validate & normalize model id
        full_model_id = body.get("model", "")
        if not full_model_id:
            raise Exception("A 'model' must be provided.")
        payload = {**body, "model": self._clean_model_id(full_model_id)}

        headers = self._build_headers(__user__)
        url = f"{self.valves.PORTKEY_API_BASE_URL}/chat/completions"
        stream = bool(body.get("stream", True))

        try:
            if stream:
                # streaming: do NOT use retrying session to avoid duplicate tokens
                r = requests.post(
                    url=url,
                    json=payload,
                    headers=headers,
                    stream=True,
                    timeout=self.valves.REQUEST_TIMEOUT_SECS,
                )
            else:
                r = self._session_non_stream().post(
                    url=url,
                    json=payload,
                    headers=headers,
                    stream=False,
                    timeout=self.valves.REQUEST_TIMEOUT_SECS,
                )

            r.raise_for_status()

            if stream:
                return self._iter_stream(r)
            else:
                return r.json()

        except requests.HTTPError as http_err:
            status = getattr(http_err.response, "status_code", "unknown")
            details = None
            try:
                details = http_err.response.json()
            except Exception:
                try:
                    details = {"raw": http_err.response.text}
                except Exception:
                    details = None

            msg = f"Portkey HTTP {status}"
            if isinstance(details, dict):
                err = details.get("error")
                if isinstance(err, dict):
                    parts = []
                    if "message" in err: parts.append(err["message"])
                    if "type" in err: parts.append(f"type={err['type']}")
                    if "request_id" in err: parts.append(f"request_id={err['request_id']}")
                    if parts: msg += " — " + " | ".join(parts)
                else:
                    # keep it concise, but helpful
                    snippet = json.dumps(details)[:800]
                    msg += f" — {snippet}"
            raise Exception(msg) from http_err

        except requests.RequestException as req_err:
            raise Exception(f"Network error talking to Portkey: {req_err}") from req_err

        except Exception as e:
            raise Exception(f"Unexpected error: {e}") from e
