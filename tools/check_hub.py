#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Baran Bayran
"""Offline checks for this documentation hub; Python 3.12, standard library only.

Checks the current working tree, not Git history, external links, legal approval,
GitHub permissions or the running product. Findings never echo matched secrets.
"""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import tempfile
import unicodedata
import uuid
from contextlib import contextmanager
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED = frozenset({
    "README.md", "README.tr.md", "AGENTS.md", "CONTRIBUTING.md",
    "SECURITY.md", "CODE_OF_CONDUCT.md", "docs/product.md",
    "docs/architecture.md", "docs/status-and-roadmap.md",
    "docs/contribution-paths.md", "docs/partners.md",
    ".github/CODEOWNERS", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/docs.yml", "tools/check_hub.py",
    "LICENSE.md", "LICENSES/CC-BY-4.0.txt", "LICENSES/MIT.txt",
})
ENTRY_PATHS = frozenset({
    "docs/product.md", "docs/contribution-paths.md", "CONTRIBUTING.md",
    "docs/partners.md",
})
TEXT_SUFFIXES = frozenset({".md", ".yml", ".yaml", ".py", ".txt"})
EXTRA_TEXT_FILES = frozenset({".gitignore", ".env.example"})
PARITY = re.compile(r"<!--\s*section:\s*([a-z][a-z0-9-]*)\s*-->")
CONTENT_VERSION = re.compile(r"<!--\s*content-version:\s*([^\s]+)\s*-->")
FORBIDDEN = (
    ("private-repository-reference", re.compile(
        r"\b(?:baranbayran|skihubapp)/(?!skihub-hub(?:\b|/)|\.github(?:\b|/))[a-z0-9_.-]+", re.I)),
    ("internal-branch-reference", re.compile(
        r"\b[a-z]+-integration-\d{8}\b", re.I)),
    ("local-user-path", re.compile(
        r"(?:[a-z]:[\\/](?:users|home)[\\/]|/(?:home|Users)/[^/\s]+/)", re.I)),
    ("private-key", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")),
    ("github-token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("cloud-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("payment-key", re.compile(r"\bsk_(?:live|test)_[A-Za-z0-9]{20,}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("credential-in-url", re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s/@:]+:[^\s/@]+@", re.I)),
)
CREDENTIAL_ASSIGNMENT = re.compile(
    r"(?im)^\s*[\"']?(?:[a-z0-9_]*_)?(?:password|passwd|secret|api_key|access_token|auth_token|client_secret)"
    r"[\"']?\s*[:=]\s*[\"']?([^\s\"'`,;#]{8,})"
)
PLACEHOLDER = re.compile(
    r"^(?:<[^>]+>|\$\{[^}]+\}|YOUR_[A-Z_]+|CHANGE_ME|REPLACE_ME|"
    r"example|placeholder|not-used|synthetic-only)$", re.I
)


def without_code(markdown: str, *, mask_inline: bool = True) -> str:
    """Mask fenced/inline code while keeping line numbers stable for reports."""
    lines = markdown.splitlines(keepends=True)
    fence = None
    result = []
    for line in lines:
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match and fence is None:
            fence = (match[1][0], len(match[1]))
            result.append("\n" if line.endswith("\n") else "")
            continue
        if fence is not None:
            if match and match[1][0] == fence[0] and len(match[1]) >= fence[1]:
                fence = None
            result.append("\n" if line.endswith("\n") else "")
            continue
        result.append(re.sub(r"(`+).*?\1", "", line) if mask_inline else line)
    return "".join(result)


def heading_ids(markdown: str) -> set[str]:
    """GitHub-style Unicode heading slugs with collision/duplicate suffixes."""
    clean = without_code(markdown, mask_inline=False)
    used = set(re.findall(r'<a\s+[^>]*(?:id|name)=[\"\']([^\"\']+)', clean, re.I))
    lines = clean.splitlines()
    for index, line in enumerate(lines):
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        title = match[1] if match else None
        if title is None and index + 1 < len(lines) and line.strip():
            if re.match(r"^ {0,3}(?:=+|-+)\s*$", lines[index + 1]):
                title = line.strip()
        if title is None:
            continue
        title = re.sub(r"!?\[([^]]*)\]\([^)]*\)", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]*>", "", title)).lower()
        title = title.replace("*", "").replace("`", "")
        slug = "".join(
            c for c in title
            if c in "-_ " or not unicodedata.category(c).startswith(("P", "S", "C"))
        ).replace(" ", "-")
        candidate = slug
        suffix = 0
        while candidate in used:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        used.add(candidate)
    return used


def markdown_links(markdown: str) -> list[tuple[int, str]]:
    """Inline, reference and HTML href/src links; code examples are ignored."""
    clean = without_code(markdown)
    definitions = {}
    for match in re.finditer(r"(?m)^ {0,3}\[([^]]+)\]:\s*(?:<([^>]+)>|(\S+))", clean):
        definitions[match[1].strip().casefold()] = match[2] or match[3]
    links = []
    pattern = re.compile(
        r"!?\[[^]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+(?:\([^)]*\)[^\s)]*)?))"
        r"(?:\s+[\"'][^\n]*?[\"'])?\s*\)"
        r"|!?\[([^]\n]+)\]\[([^]\n]*)\]"
        r"|<(?:a|img)\b[^>]*?\b(?:href|src)=[\"']([^\"']+)[\"']",
        re.I,
    )
    for match in pattern.finditer(clean):
        target = match[1] or match[2] or match[5]
        if target is None:
            label = (match[4] or match[3]).strip().casefold()
            target = definitions.get(label)
            if target is None:
                target = "unresolved-reference:" + label
        links.append((clean.count("\n", 0, match.start()) + 1, html.unescape(target)))
    return links


def content_findings(text: str) -> list[tuple[str, int]]:
    findings = []
    for code, pattern in FORBIDDEN:
        for match in pattern.finditer(text):
            findings.append((code, text.count("\n", 0, match.start()) + 1))
    for match in CREDENTIAL_ASSIGNMENT.finditer(text):
        if not PLACEHOLDER.fullmatch(match[1]):
            findings.append(("assigned-secret", text.count("\n", 0, match.start()) + 1))
    return findings


def split_destination(destination: str):
    try:
        return urlsplit(destination)
    except ValueError:
        return None


def link_problem(root: Path, source: str, destination: str) -> str | None:
    parsed = split_destination(destination)
    if parsed is None:
        return "malformed-link"
    if parsed.scheme in {"https", "http", "mailto"}:
        return None
    if parsed.scheme or parsed.netloc or "\\" in destination or parsed.path.startswith("/"):
        return "unsafe-or-unsupported-link"
    path = unquote(parsed.path)
    normalized = posixpath.normpath(posixpath.join(posixpath.dirname(source), path)) if path else source
    if normalized == ".." or normalized.startswith("../"):
        return "link-outside-hub"
    target = root / normalized
    if not target.resolve().is_relative_to(root.resolve()):
        return "link-outside-hub"
    if not target.exists():
        return "missing-link-target"
    # Windows is case-insensitive; require the same filename case as Linux/GitHub.
    actual = root
    for component in normalized.split("/"):
        if component not in {item.name for item in actual.iterdir()}:
            return "link-target-case-mismatch"
        actual /= component
    if parsed.fragment and target.suffix.lower() == ".md":
        try:
            anchors = heading_ids(target.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError):
            return "unreadable-link-target"
        if unquote(parsed.fragment) not in anchors:
            return "missing-markdown-anchor"
    return None


def parity_problem(english: str, turkish: str) -> str | None:
    versions = CONTENT_VERSION.findall(english)
    if len(versions) != 1 or versions != CONTENT_VERSION.findall(turkish):
        return "readme-content-version-parity"
    first = PARITY.findall(english)
    second = PARITY.findall(turkish)
    if len(first) < 4 or len(first) != len(set(first)) or first != second:
        return "readme-parity-markers"
    def destinations(text: str) -> set[str]:
        result = set()
        for _, destination in markdown_links(text):
            parsed = split_destination(destination)
            if parsed is not None and not parsed.scheme and not parsed.netloc and parsed.path not in {"README.md", "README.tr.md", ""}:
                result.add(destination)
        return result
    if destinations(english) != destinations(turkish):
        return "readme-relative-target-parity"
    for document in (english, turkish):
        targets = {parsed.path for _, target in markdown_links(document) if (parsed := split_destination(target)) is not None}
        if not ENTRY_PATHS.issubset(targets):
            return "readme-four-entry-paths"
    if not any(target == "README.tr.md" for _, target in markdown_links(english[:700])):
        return "english-language-link"
    if not any(target == "README.md" for _, target in markdown_links(turkish[:700])):
        return "turkish-language-link"
    return None


def validate(root: Path) -> dict:
    errors = []
    files = {}
    markdown_count = 0
    links_checked = 0
    def add(code: str, path: str, line: int | None = None) -> None:
        finding = {"code": code, "file": path}
        if line is not None:
            finding["line"] = line
        if finding not in errors:
            errors.append(finding)
    for item in sorted(root.rglob("*")):
        relative = item.relative_to(root).as_posix()
        if ".git" in item.relative_to(root).parts:
            continue
        if item.is_symlink():
            add("symlink-not-allowed", relative)
            continue
        if not item.is_file():
            continue
        if item.name.startswith(".env") and item.name != ".env.example":
            add("environment-file-not-allowed", relative)
        allowed = (
            relative in REQUIRED or relative in EXTRA_TEXT_FILES
            or (relative.startswith("docs/") and item.suffix == ".md")
            or (relative.startswith(".github/ISSUE_TEMPLATE/") and item.suffix in {".md", ".yml", ".yaml"})
        )
        if not allowed:
            add("file-outside-reviewed-scope", relative)
        if item.suffix not in TEXT_SUFFIXES and relative not in REQUIRED | EXTRA_TEXT_FILES:
            add("binary-or-unapproved-asset", relative)
            continue
        try:
            content = item.read_text(encoding="utf-8-sig")
        except (UnicodeError, OSError):
            add("not-readable-utf8", relative)
            continue
        if "\x00" in content:
            add("binary-content", relative)
            continue
        files[relative] = content
        for code, line in content_findings(content):
            add(code, relative, line)
        if item.suffix == ".md":
            markdown_count += 1
            if not without_code(content).strip():
                add("empty-markdown", relative)
            for line, destination in markdown_links(content):
                links_checked += 1
                problem = link_problem(root, relative, destination)
                if problem:
                    add(problem, relative, line)
    for required in sorted(REQUIRED - files.keys()):
        add("missing-required-file", required)
    templates = {Path(name).stem for name in files if name.startswith(".github/ISSUE_TEMPLATE/")}
    if len(templates - {"config"}) < 3:
        add("three-issue-templates-required", ".github/ISSUE_TEMPLATE")
    if {"README.md", "README.tr.md"}.issubset(files):
        problem = parity_problem(files["README.md"], files["README.tr.md"])
        if problem:
            add(problem, "README.md + README.tr.md")
    return {
        "status": "FAIL" if errors else "PASS",
        "scope": "current-tree-offline-only",
        "files_checked": len(files),
        "markdown_files": markdown_count,
        "links_checked": links_checked,
        "external_link_network_check": "NOT_RUN",
        "history_and_hosted_settings": "NOT_RUN",
        "errors": errors,
    }


@contextmanager
def fixture_directory(scratch_dir: Path | None):
    # Inherit the parent ACL on Windows; mkdtemp's restrictive ACL can exclude a
    # sandboxed process. Fixtures contain generated documentation only.
    directory = (scratch_dir or Path(tempfile.gettempdir())) / ("hub-check-" + uuid.uuid4().hex)
    directory.mkdir()
    try:
        yield directory
    finally:
        for item in directory.iterdir():
            item.unlink()
        directory.rmdir()


def self_test(scratch_dir: Path | None = None) -> dict:
    """Adversarial examples test safeguards without storing sensitive fixtures."""
    results = {}
    with fixture_directory(scratch_dir) as root:
        (root / "README.md").write_text("# Intro\n# Intro\n# Intro-1\n", encoding="utf-8")
        results["duplicate-heading-anchors"] = heading_ids("# Intro\n# Intro\n# Intro-1\n") == {"intro", "intro-1", "intro-1-1"}
        results["inline-code-heading"] = heading_ids("# Use `Python` now\n") == {"use-python-now"}
        results["valid-duplicate-anchor"] = link_problem(root, "README.md", "#intro-1") is None
        results["broken-anchor-blocked"] = link_problem(root, "README.md", "#missing") == "missing-markdown-anchor"
        results["broken-link-blocked"] = link_problem(root, "README.md", "missing.md") == "missing-link-target"
        results["escape-blocked"] = link_problem(root, "README.md", "../outside.md") == "link-outside-hub"
        results["malformed-link-blocked"] = link_problem(root, "README.md", "https://[broken") == "malformed-link"
        results["local-path-blocked"] = bool(content_findings("C:" + chr(92) + "Users" + chr(92) + "Example" + chr(92) + "notes.md"))
        results["credential-blocked"] = bool(content_findings("gh" + "p_" + "A" * 36))
        results["private-reference-blocked"] = bool(content_findings("skihubapp/" + "private-source-example"))
        version = "<!-- content-version: test.1 -->\n"
        results["parity-drift-blocked"] = parity_problem(version + "<!-- section: first -->", version + "<!-- section: second -->") == "readme-parity-markers"
        results["fenced-links-ignored"] = markdown_links("```md\n[Example](missing.md)\n```\n") == []
    return {"status": "PASS" if all(results.values()) else "FAIL", "adversarial_checks": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--scratch-dir", type=Path, help="Existing writable directory for temporary self-test fixtures")
    args = parser.parse_args()
    result = self_test(args.scratch_dir) if args.self_test else validate(args.root.resolve())
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return int(result["status"] != "PASS")


if __name__ == "__main__":
    raise SystemExit(main())
