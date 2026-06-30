#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXPECTED = {
    "title": "AIエージェント協働の仕事術",
    "description": "AIエージェントを業務成果につなげるための依頼、コンテキスト、委任、検証、権限、判断、組織展開の実践フレームワーク",
    "version": "1.0.0",
    "repository": "itdojp/ai-agent-collaboration-book",
    "public_url": "https://itdojp.github.io/ai-agent-collaboration-book/",
    "baseurl": "/ai-agent-collaboration-book",
}


def load_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"PyYAML unavailable: {exc}") from exc
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> int:
    errors: list[str] = []
    book = json.loads((ROOT / "book-config.json").read_text(encoding="utf-8"))
    package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    cfg = load_yaml(DOCS / "_config.yml")

    if book.get("title") != EXPECTED["title"]:
        errors.append("book-config.json title mismatch")
    if package.get("version") != EXPECTED["version"] or book.get("version") != EXPECTED["version"] or cfg.get("version") != EXPECTED["version"]:
        errors.append("version must match 1.0.0 across book-config.json, package.json, docs/_config.yml")
    if book.get("description") != EXPECTED["description"]:
        errors.append("book-config.json description mismatch")
    if package.get("description") != EXPECTED["description"]:
        errors.append("package.json description mismatch")
    if cfg.get("description") != EXPECTED["description"]:
        errors.append("docs/_config.yml description mismatch")
    if book.get("publicUrl") != EXPECTED["public_url"]:
        errors.append("book-config.json publicUrl mismatch")
    if package.get("homepage") != EXPECTED["public_url"]:
        errors.append("package.json homepage mismatch")
    if cfg.get("baseurl") != EXPECTED["baseurl"]:
        errors.append("docs/_config.yml baseurl mismatch")
    repo_url = book.get("repository", {}).get("url")
    if repo_url != "https://github.com/itdojp/ai-agent-collaboration-book":
        errors.append("book-config.json repository.url mismatch")
    if package.get("repository", {}).get("url") != "git+https://github.com/itdojp/ai-agent-collaboration-book.git":
        errors.append("package.json repository.url mismatch")
    if cfg.get("repository") != EXPECTED["repository"]:
        errors.append("docs/_config.yml repository mismatch")
    if cfg.get("repository_path_prefix") != "docs":
        errors.append("docs/_config.yml repository_path_prefix must be docs")

    chapters = book.get("structure", {}).get("chapters", [])
    appendices = book.get("structure", {}).get("appendices", [])
    if len(chapters) != 17:
        errors.append(f"book-config.json must list 17 chapters including chapter 0, found {len(chapters)}")
    if len(appendices) != 8:
        errors.append(f"book-config.json must list 8 appendices, found {len(appendices)}")
    if not (DOCS / "chapters" / "chapter-16" / "index.md").exists():
        errors.append("docs chapter-16 page is missing")
    if not (DOCS / "appendices" / "appendix-h" / "index.md").exists():
        errors.append("docs appendix-h page is missing")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("metadata OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
