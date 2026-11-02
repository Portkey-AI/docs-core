#!/usr/bin/env node
// Portkey <-> Prisma AIRS (aigw/) docs parity driver.
//
//   node driver.mjs drift  [--since <sha>] [--to <ref>] [-v]  root changes not yet mirrored into aigw/
//   node driver.mjs checks [--base <ref>]                 run aigw/scripts checks here and on <ref>, diff
//   node driver.mjs shots  <page> [<page>...] [--port N] [--top]  screenshot root page and its aigw twin
//                                                       (--top = first viewport only, not full page)
//
// Run from the repo root. Paths are root-tree page paths without .mdx,
// e.g. product/ai-gateway/decisions-api.

import { execFileSync, spawnSync } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const OUT = "/tmp/aigw-parity";
const PW_HOME = path.join(os.homedir(), ".cache", "aigw-parity-driver");
const SYNC_GREP = "docs(aigw): sync Portkey-side changes";
const EXCLUDE = [":!aigw", ":!changelog", ":!api-reference", ":!virtual_key_old", ":!mintlify"];

const git = (...a) => execFileSync("git", a, { encoding: "utf8", maxBuffer: 1 << 28 });
const gitOk = (...a) => spawnSync("git", a, { encoding: "utf8", maxBuffer: 1 << 28 });
const die = (m) => { console.error(m); process.exit(2); };

function opt(args, name, dflt) {
  const i = args.indexOf(name);
  if (i === -1) return dflt;
  const v = args[i + 1];
  args.splice(i, 2);
  return v;
}

// ---------- drift ----------

// Strip what legitimately differs between the trees so a mirrored line still matches.
function norm(s) {
  return s
    .toLowerCase()
    .replace(/\]\([^)]*\)/g, "]")          // link targets (/aigw/ prefix)
    .replace(/href="[^"]*"/g, "")
    .replace(/prisma airs ai gateway('s)?|the ai gateway('s)?|ai gateway('s)?|portkey('s)?( gateway)?/g, "")
    .replace(/organisation/g, "organization").replace(/behaviour/g, "behavior")
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

// Long lines may match anywhere in the twin (wrapping and rewording around them
// differ). Short ones like `"max_age": 300` or `## Azure OpenAI` would match by
// coincidence inside other sentences, so they must equal a whole twin line.
function twinMatcher(text) {
  const body = norm(text);
  const lines = new Set(text.split("\n").map(norm));
  return (l) => { const n = norm(l); return n.length >= 20 ? body.includes(n) : lines.has(n); };
}

function lastSyncPoint(ref) {
  const r = gitOk("log", ref, "-1", "--format=%H%n%B", `--grep=${SYNC_GREP}`, "--fixed-strings");
  const m = /up to ([0-9a-f]{7,40})/.exec(r.stdout || "");
  return m ? m[1] : null;
}

function drift(args) {
  const verbose = args.includes("-v"); if (verbose) args.splice(args.indexOf("-v"), 1);
  const to = opt(args, "--to", "origin/main");
  let since = opt(args, "--since");
  if (!since) {
    since = lastSyncPoint(to);
    if (!since) die(`No sync commit on ${to} says "up to <sha>". Pass --since <sha>.`);
    console.log(`sync point from last "${SYNC_GREP}" commit: ${since}`);
  }
  const log = git("log", "--no-merges", "--reverse", "--format=%h%x09%ad%x09%an%x09%s", "--date=short",
    `${since}..${to}`, "--", "*.mdx", ...EXCLUDE).trim();
  if (!log) { console.log(`No root .mdx changes in ${since}..${to}.`); return; }

  const rows = [];
  for (const line of log.split("\n")) {
    const [sha, date, author, subject] = line.split("\t");
    const files = git("show", "--format=", "--name-only", sha, "--", "*.mdx", ...EXCLUDE).trim().split("\n").filter(Boolean);
    console.log(`\n${sha} ${date} ${author}: ${subject}`);
    for (const f of files) {
      const twin = `aigw/${f}`;
      const has = gitOk("cat-file", "-e", `${to}:${twin}`).status === 0;
      const diff = git("show", "--format=", "-U0", sha, "--", f);
      const pick = (c) => diff.split("\n")
        .filter((l) => l.startsWith(c) && !l.startsWith(c + c + c))
        .map((l) => l.slice(1))
        // Drop only lines with no words left (braces, blank) and pure markup/imports.
        // Short settings such as `"max_age": 300` must stay: they are real edits.
        .filter((l) => norm(l).length > 0 && !/^\s*(```[\w-]*\s*$|<\/?[\w.]+\s*\/?>\s*$|import )/.test(l));
      const added = pick("+"), removed = pick("-");
      let status;
      const exists = (rev) => gitOk("cat-file", "-e", `${rev}:${f}`).status === 0;
      if (!exists(sha)) status = has ? "ROOT PAGE DELETED, aigw twin still exists" : "MIRRORED (page deleted in both)";
      else if (!has) status = exists(`${sha}^`) ? "NO aigw twin" : "NEW PAGE, no aigw twin";
      else {
        const inTwin = twinMatcher(git("show", `${to}:${twin}`));
        const inA = added.filter(inTwin).length;
        // A removed line that survives inside an added line was edited, not deleted.
        const stillR = removed.filter((l) => !added.some((a) => norm(a).includes(norm(l))) && inTwin(l)).length;
        if (!added.length && !removed.length) status = "trivial (formatting only)";
        else if (added.length && inA === added.length && !stillR) status = "MIRRORED";
        else if (!added.length) status = stillR ? `REMOVAL NOT MIRRORED (${stillR} line(s) still in aigw)` : "MIRRORED (removal)";
        else status = `${inA === 0 ? "MISSING" : "PARTIAL"} ${inA}/${added.length} added lines found` + (stillR ? `, ${stillR} removed line(s) still in aigw` : "");
      }
      rows.push({ sha, f, status });
      console.log(`  ${status.padEnd(44)} ${f}`);
      if (verbose && has && /PARTIAL|MISSING/.test(status)) {
        const inTwin = twinMatcher(git("show", `${to}:${twin}`));
        for (const l of added.filter((l) => !inTwin(l))) console.log(`      not in aigw: ${l.trim().slice(0, 140)}`);
      }
    }
  }
  const todo = rows.filter((r) => !/^MIRRORED|^trivial/.test(r.status));
  console.log(`\n${todo.length} file change(s) to review/port out of ${rows.length}.`);
  console.log("Heuristic: rewording on either side shows as PARTIAL. Read the diff before trusting a MIRRORED/MISSING verdict.");
}

// ---------- checks ----------

const CHECKS = ["check_nav_page_parity", "check_anchors", "check_prose_endpoints"];

function caBundle() {
  if (process.env.SSL_CERT_FILE || process.platform !== "darwin") return process.env.SSL_CERT_FILE;
  const pem = path.join(OUT, "cas.pem");
  if (!fs.existsSync(pem)) {
    const r = spawnSync("security", ["find-certificate", "-a", "-p",
      "/Library/Keychains/System.keychain", "/System/Library/Keychains/SystemRootCertificates.keychain"], { encoding: "utf8", maxBuffer: 1 << 26 });
    fs.writeFileSync(pem, r.stdout);
  }
  return pem;
}

function runChecks(dir, env) {
  const out = {};
  for (const c of CHECKS) {
    const r = spawnSync("python3", [path.join(dir, "aigw/scripts", `${c}.py`)], { cwd: dir, encoding: "utf8", env, maxBuffer: 1 << 26 });
    out[c] = { code: r.status, text: (r.stdout || "") + (r.stderr || "") };
  }
  return out;
}

function checks(args) {
  const base = opt(args, "--base", "origin/main");
  fs.mkdirSync(OUT, { recursive: true });
  const env = { ...process.env };
  const ca = caBundle(); if (ca) env.SSL_CERT_FILE = ca;
  const wt = path.join(OUT, "base-worktree");
  if (fs.existsSync(wt)) gitOk("worktree", "remove", "--force", wt);
  git("worktree", "add", "--detach", "--quiet", wt, base);
  try {
    const here = runChecks(process.cwd(), env), there = runChecks(wt, env);
    let regress = 0;
    for (const c of CHECKS) {
      const a = here[c], b = there[c];
      fs.writeFileSync(path.join(OUT, `${c}.branch.txt`), a.text);
      fs.writeFileSync(path.join(OUT, `${c}.base.txt`), b.text);
      const net = /URLError|CERTIFICATE_VERIFY_FAILED|Traceback/.test(a.text);
      const d = spawnSync("diff", [path.join(OUT, `${c}.base.txt`), path.join(OUT, `${c}.branch.txt`)], { encoding: "utf8" }).stdout;
      const worse = a.code !== 0 && b.code === 0;
      if (worse || net) regress++;
      console.log(`\n### ${c}: branch exit=${a.code}, ${base} exit=${b.code}${worse ? "  <-- NEW FAILURE" : ""}${net ? "  <-- DID NOT RUN (crash/network)" : ""}`);
      console.log(d.trim() ? d.trim() : "(identical output)");
    }
    console.log(`\nFull outputs: ${OUT}/<check>.{branch,base}.txt`);
    process.exitCode = regress ? 1 : 0;
  } finally {
    gitOk("worktree", "remove", "--force", wt);
  }
}

// ---------- shots ----------

function detectPort() {
  const log = path.join(OUT, "mint.log");
  if (fs.existsSync(log)) {
    const m = [...fs.readFileSync(log, "utf8").matchAll(/localhost:(\d+)/g)].pop();
    if (m) return m[1];
  }
  return "3000";
}

async function shots(args) {
  const port = opt(args, "--port", detectPort());
  const top = args.includes("--top"); if (top) args.splice(args.indexOf("--top"), 1);
  const pages = args.map((p) => p.replace(/^\/|\.mdx$/g, "").replace(/^aigw\//, ""));
  if (!pages.length) die("usage: shots <page> [<page>...] [--port N]");
  let pw;
  try { pw = createRequire(path.join(PW_HOME, "x.js"))("playwright-core"); }
  catch { die(`playwright-core missing. Run: mkdir -p ${PW_HOME} && cd ${PW_HOME} && npm init -y && npm i playwright-core@1.49.1`); }
  const dir = path.join(OUT, "shots"); fs.mkdirSync(dir, { recursive: true });
  let bad = 0;
  for (const p of pages) {
    for (const [tag, url] of [["root", `/${p}`], ["aigw", `/aigw/${p}`]]) {
      // Fresh browser per page: one long-lived Chrome dies after a few
      // multi-thousand-pixel full-page captures ("Target page ... has been closed").
      const browser = await pw.chromium.launch({ channel: "chrome", headless: true });
      try {
        const page = await (await browser.newContext({ viewport: { width: 1400, height: 1000 } })).newPage();
        const errs = [];
        page.on("pageerror", (e) => errs.push(e.message));
        const res = await page.goto(`http://localhost:${port}${url}`, { waitUntil: "domcontentloaded", timeout: 120000 });
        await page.waitForSelector("h1", { timeout: 120000 }).catch(() => {});
        await page.waitForTimeout(1500); // let mermaid / code blocks settle
        const title = (await page.locator("h1").first().textContent().catch(() => "")) || "";
        const notFound = res.status() >= 400 || /page not found|404/i.test(title);
        const file = path.join(dir, `${p.replace(/\//g, "__")}.${tag}.png`);
        await page.screenshot({ path: file, fullPage: !top });
        if (notFound || errs.length) bad++;
        console.log(`${notFound ? "404 " : "OK  "} ${tag.padEnd(4)} ${url}  h1="${title.trim()}"${errs.length ? `  pageerrors=${errs.length}: ${errs[0]}` : ""}\n     -> ${file}`);
      } catch (e) {
        bad++;
        console.log(`FAIL ${tag.padEnd(4)} ${url}  ${e.message.split("\n")[0]}`);
      } finally {
        await browser.close().catch(() => {});
      }
    }
  }
  process.exitCode = bad ? 1 : 0;
}

// ---------- main ----------

const [cmd, ...args] = process.argv.slice(2);
if (!fs.existsSync("docs.json") || !fs.existsSync("aigw")) die("Run from the docs-core repo root.");
fs.mkdirSync(OUT, { recursive: true });
if (cmd === "drift") drift(args);
else if (cmd === "checks") checks(args);
else if (cmd === "shots") await shots(args);
else die("usage: node driver.mjs drift|checks|shots ... (see header of this file)");
