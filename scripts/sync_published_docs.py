#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPOSITORY_URL = "https://github.com/itdojp/ai-agent-collaboration-book"
BASEURL = "/ai-agent-collaboration-book"

LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]*)(\))")
CODE_FENCE_RE = re.compile(r"^\s*```")
IGNORE_SCHEMES = {"http", "https", "mailto", "tel"}

@dataclass(frozen=True)
class Mapping:
    source: str
    dest: str
    order: int
    section: str


def mappings() -> list[Mapping]:
    base: list[tuple[str, str, str]] = [
        ("index.md", "index.md", "home"),
        ("quickstart.md", "quickstart/index.md", "introduction"),
        ("concept-map.md", "concept-map/index.md", "introduction"),
        ("artifact-index.md", "artifact-index/index.md", "additional"),
        ("troubleshooting.md", "troubleshooting/index.md", "additional"),
        ("figure-index.md", "figure-index/index.md", "additional"),
        ("source-notes.md", "source-notes/index.md", "resources"),
        ("preface.md", "preface/index.md", "resources"),
        ("afterword.md", "afterword/index.md", "resources"),
        ("copyright.md", "copyright/index.md", "resources"),
        ("colophon.md", "colophon/index.md", "resources"),
        ("changelog.md", "changelog/index.md", "resources"),
        ("manuscript/00-reading-guide.md", "reading-guide/index.md", "introduction"),
    ]
    chapters = [
        ("manuscript/ch01-ai-agent-collaboration.md", "chapters/chapter-01/index.md"),
        ("manuscript/ch02-work-selection.md", "chapters/chapter-02/index.md"),
        ("manuscript/ch03-request-contract.md", "chapters/chapter-03/index.md"),
        ("manuscript/ch04-context-design.md", "chapters/chapter-04/index.md"),
        ("manuscript/ch05-task-delegation.md", "chapters/chapter-05/index.md"),
        ("manuscript/ch06-review-evaluation.md", "chapters/chapter-06/index.md"),
        ("manuscript/ch07-tool-permission-hitl.md", "chapters/chapter-07/index.md"),
        ("manuscript/ch08-logs-observability.md", "chapters/chapter-08/index.md"),
        ("manuscript/ch09-security-privacy.md", "chapters/chapter-09/index.md"),
        ("manuscript/ch10-governance.md", "chapters/chapter-10/index.md"),
        ("manuscript/ch11-discernment.md", "chapters/chapter-11/index.md"),
        ("manuscript/ch12-conflict-connection-debt.md", "chapters/chapter-12/index.md"),
        ("manuscript/ch13-experiment-culture.md", "chapters/chapter-13/index.md"),
        ("manuscript/ch14-self-talk.md", "chapters/chapter-14/index.md"),
        ("manuscript/ch15-skill-map.md", "chapters/chapter-15/index.md"),
        ("manuscript/ch16-org-rollout.md", "chapters/chapter-16/index.md"),
    ]
    appendices = [
        ("appendices/a-templates.md", "appendices/appendix-a/index.md"),
        ("appendices/b-checklists.md", "appendices/appendix-b/index.md"),
        ("appendices/c-rubric.md", "appendices/appendix-c/index.md"),
        ("appendices/d-use-cases.md", "appendices/appendix-d/index.md"),
        ("appendices/e-glossary.md", "appendices/appendix-e/index.md"),
        ("appendices/f-workshop-design.md", "appendices/appendix-f/index.md"),
        ("appendices/g-assessment-bank.md", "appendices/appendix-g/index.md"),
        ("appendices/h-governance-starter-pack.md", "appendices/appendix-h/index.md"),
    ]
    additional = [
        ("examples/recurring-case.md", "examples/recurring-case/index.md", "additional"),
        ("exercises/exercise-bank.md", "exercises/exercise-bank/index.md", "additional"),
    ]
    figure_files = sorted((ROOT / "figures").glob("*.md"))
    order = 0
    out: list[Mapping] = []
    for source, dest, section in base:
        out.append(Mapping(source, dest, order, section))
        order += 10
    for source, dest in chapters:
        out.append(Mapping(source, dest, order, "chapters"))
        order += 10
    for source, dest in appendices:
        out.append(Mapping(source, dest, order, "appendices"))
        order += 10
    for source, dest, section in additional:
        out.append(Mapping(source, dest, order, section))
        order += 10
    for fig in figure_files:
        rel = fig.relative_to(ROOT).as_posix()
        out.append(Mapping(rel, f"figures/{fig.stem}/index.md", order, "figures"))
        order += 10
    return out


def load_mapping() -> tuple[dict[str, Mapping], dict[str, str]]:
    items = mappings()
    by_source = {item.source: item for item in items}
    source_to_dest = {item.source: item.dest for item in items}
    return by_source, source_to_dest


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "AIエージェント協働の仕事術"


def make_excerpt(markdown: str, limit: int = 220) -> str:
    lines = []
    in_code = False
    for line in markdown.splitlines():
        if line.strip().startswith("---") and not lines:
            continue
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            continue
        if in_code or line.startswith("#") or line.strip().startswith("|"):
            continue
        clean = re.sub(r"[`*_>#-]", " ", line).strip()
        if clean:
            lines.append(clean)
        if sum(len(x) for x in lines) > limit:
            break
    return re.sub(r"\s+", " ", " ".join(lines))[:limit]


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def parse_link_target(raw: str) -> tuple[str, str, str, str] | None:
    stripped = raw.strip()
    if not stripped or stripped.startswith("#"):
        return None
    # Preserve optional link title by rewriting only the URL token.
    if stripped.startswith("<") and ">" in stripped:
        url = stripped[1:stripped.index(">")]
        suffix = stripped[stripped.index(">") + 1 :]
        prefix = "<"
        closing = ">"
    else:
        parts = stripped.split(maxsplit=1)
        url = parts[0]
        suffix = " " + parts[1] if len(parts) > 1 else ""
        prefix = ""
        closing = ""
    parsed = urlparse(url)
    if parsed.scheme in IGNORE_SCHEMES or parsed.scheme:
        return None
    if url.startswith("//"):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    fragment = f"#{parsed.fragment}" if parsed.fragment else ""
    query = f"?{parsed.query}" if parsed.query else ""
    return path, fragment, query, f"{prefix}{{url}}{closing}{suffix}"


def site_dir_for_dest(dest: str) -> str:
    if dest == "index.md":
        return "."
    if dest.endswith("/index.md"):
        return dest[: -len("/index.md")]
    return dest.rsplit("/", 1)[0]


def relative_site_link(current_dest: str, target_dest: str, fragment: str = "") -> str:
    current_dir = site_dir_for_dest(current_dest)
    target_dir = site_dir_for_dest(target_dest)
    rel = posixpath.relpath(target_dir, current_dir)
    if rel == ".":
        return fragment or "./"
    return rel.rstrip("/") + "/" + fragment


def relative_asset_link(current_dest: str, asset_dest: str, fragment: str = "") -> str:
    current_dir = site_dir_for_dest(current_dest)
    rel = posixpath.relpath(asset_dest, current_dir)
    return rel + fragment


def rewrite_links(markdown: str, source: str, dest: str, source_to_dest: dict[str, str]) -> str:
    source_path = (ROOT / source).resolve()
    out_lines: list[str] = []
    in_code = False
    for line in markdown.splitlines():
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            out_lines.append(line)
            continue
        if in_code:
            out_lines.append(line)
            continue

        def repl(match: re.Match[str]) -> str:
            before, raw, after = match.groups()
            parsed = parse_link_target(raw)
            if parsed is None:
                return match.group(0)
            path, fragment, query, formatter = parsed
            if query:
                return match.group(0)
            target = (source_path.parent / path).resolve()
            try:
                target_rel = target.relative_to(ROOT).as_posix()
            except ValueError:
                return match.group(0)
            if target_rel in source_to_dest:
                url = relative_site_link(dest, source_to_dest[target_rel], fragment)
                return before + formatter.format(url=url) + after
            if target_rel.startswith("figures/assets/") and target.exists():
                url = relative_asset_link(dest, target_rel, fragment)
                return before + formatter.format(url=url) + after
            if target.exists():
                url = f"{REPOSITORY_URL}/blob/main/{target_rel}{fragment}"
                return before + formatter.format(url=url) + after
            return match.group(0)

        out_lines.append(LINK_RE.sub(repl, line))
    return "\n".join(out_lines) + "\n"


def render_doc(item: Mapping, source_to_dest: dict[str, str]) -> str:
    source_path = ROOT / item.source
    if not source_path.exists():
        raise FileNotFoundError(f"missing source file: {item.source}")
    raw = source_path.read_text(encoding="utf-8")
    body = rewrite_links(raw, item.source, item.dest, source_to_dest).rstrip() + "\n"
    title = extract_title(raw)
    front_matter = [
        "---",
        f"title: {yaml_quote(title)}",
        f"source_path: {yaml_quote(item.source)}",
        f"order: {item.order}",
        f"book_section: {yaml_quote(item.section)}",
        "---",
        "",
    ]
    return "\n".join(front_matter) + body


def iter_generated_docs() -> list[Path]:
    _, source_to_dest = load_mapping()
    return [DOCS / dest for dest in source_to_dest.values()]


def site_url_for_doc(path: Path) -> str:
    rel = path.relative_to(DOCS)
    if rel.name == "index.md":
        if str(rel.parent) == ".":
            suffix = "/"
        else:
            suffix = "/" + rel.parent.as_posix().rstrip("/") + "/"
    else:
        suffix = "/" + rel.with_suffix("").as_posix().rstrip("/") + "/"
    return suffix


def generate_search_data(rendered: dict[Path, str]) -> str:
    items = []
    for path in sorted(rendered):
        if path.name != "index.md" and path.suffix != ".md":
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = rendered[path]
        body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
        title = extract_title(body)
        items.append(
            {
                "title": title,
                "url": f"{BASEURL}{site_url_for_doc(path)}",
                "source_path": rel,
                "excerpt": make_excerpt(body),
            }
        )
    return json.dumps({"baseurl": BASEURL, "items": items}, ensure_ascii=False, indent=2) + "\n"


def build_outputs() -> dict[Path, str]:
    _, source_to_dest = load_mapping()
    rendered: dict[Path, str] = {}
    for item in mappings():
        dest_path = DOCS / item.dest
        rendered[dest_path] = render_doc(item, source_to_dest)
    rendered[DOCS / "assets" / "search-data.json"] = generate_search_data(rendered)
    return rendered


def build_asset_outputs() -> dict[Path, bytes]:
    outputs: dict[Path, bytes] = {}
    asset_root = ROOT / "figures" / "assets"
    if not asset_root.exists():
        return outputs
    public_suffixes = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"}
    for source in sorted(asset_root.rglob("*")):
        if not source.is_file():
            continue
        if source.suffix.lower() not in public_suffixes:
            continue
        rel = source.relative_to(asset_root)
        outputs[DOCS / "figures" / "assets" / rel] = source.read_bytes()
    return outputs


def write_outputs(outputs: dict[Path, str], asset_outputs: dict[Path, bytes]) -> None:
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for path, content in asset_outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)


def check_outputs(outputs: dict[Path, str], asset_outputs: dict[Path, bytes]) -> list[str]:
    errors: list[str] = []
    for path, expected in outputs.items():
        if not path.exists():
            errors.append(f"missing generated file: {path.relative_to(ROOT)}")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected:
            errors.append(f"generated file is stale: {path.relative_to(ROOT)}")
    for path, expected in asset_outputs.items():
        if not path.exists():
            errors.append(f"missing generated asset: {path.relative_to(ROOT)}")
            continue
        actual = path.read_bytes()
        if actual != expected:
            errors.append(f"generated asset is stale: {path.relative_to(ROOT)}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the reader-facing Jekyll docs tree from manuscript files.")
    parser.add_argument("--check", action="store_true", help="verify generated files are up to date without writing")
    args = parser.parse_args(argv)

    outputs = build_outputs()
    asset_outputs = build_asset_outputs()
    if args.check:
        errors = check_outputs(outputs, asset_outputs)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            return 1
        print("published docs are in sync")
        return 0
    write_outputs(outputs, asset_outputs)
    print(f"wrote {len(outputs)} generated docs/search files and {len(asset_outputs)} assets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
