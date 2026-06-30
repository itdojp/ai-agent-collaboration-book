#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "figures" / "assets"
MERMAID_DIR = ASSETS / "mermaid"
MERMAID_CLI_VERSION = "11.16.0"

MERMAID_SOURCES: dict[str, str] = {
    "concept-map.md": "concept-map.svg",
    "artifact-index.md": "artifact-index-flow.svg",
    "troubleshooting.md": "troubleshooting-flow.svg",
    "manuscript/ch01-ai-agent-collaboration.md": "chapter-01-collaboration-loop.svg",
    "figures/f-00-ai-agent-collaboration-loop.md": "f-00-ai-agent-collaboration-loop.svg",
    "figures/f-01-six-layer-model.md": "f-01-six-layer-model.svg",
    "figures/f-02-request-context-task-brief.md": "f-02-request-context-task-brief.svg",
    "figures/f-03-control-layer-flow.md": "f-03-control-layer-flow.svg",
    "figures/f-04-human-org-layer-flow.md": "f-04-human-org-layer-flow.svg",
    "figures/f-06-90-day-rollout-roadmap.md": "f-06-90-day-rollout-roadmap.svg",
    "figures/f-07-permission-ladder.md": "f-07-permission-ladder.svg",
    "figures/f-08-agent-run-log-flow.md": "f-08-agent-run-log-flow.svg",
    "figures/f-09-ai-security-risk-map.md": "f-09-ai-security-risk-map.svg",
    "figures/f-10-ai-governance-cycle.md": "f-10-ai-governance-cycle.svg",
    "figures/f-11-decision-responsibility-boundary.md": "f-11-decision-responsibility-boundary.svg",
    "figures/f-12-connection-debt-structure.md": "f-12-connection-debt-structure.svg",
    "figures/f-13-experiment-learning-loop.md": "f-13-experiment-learning-loop.svg",
    "figures/f-14-action-blocker-structure.md": "f-14-action-blocker-structure.svg",
    "figures/f-15-skill-level-map.md": "f-15-skill-level-map.svg",
}

LEVEL_PREFIX_ROWS = [
    ("AI適用段階", "A0〜A5", "2", "AIをどこまで業務へ組み込むか"),
    ("権限レベル", "P0〜P7", "7", "ツール操作権限の強さ"),
    ("観測性レベル", "O0〜O5", "8", "ログ、トレース、改善の成熟度"),
    ("セキュリティレベル", "S0〜S5", "9", "セキュリティ管理の重さ"),
    ("ガバナンスレベル", "G0〜G5", "10", "組織統制の成熟度"),
    ("判断レベル", "J0〜J5", "11", "人間判断の明示度"),
    ("Connection Debtレベル", "C0〜C5", "12", "未処理対立の重さ"),
    ("実験レベル", "X0〜X5", "13", "実験の影響範囲"),
    ("評価証拠レベル", "EV0〜EV5", "15", "認定に使う証拠の強さ"),
    ("スキルレベル", "Lv1〜Lv6", "15", "個人・チーム・全社能力"),
]

MERMAID_RE = re.compile(r"```mermaid\n(.*?)\n```", re.S)


def extract_mermaid(source: Path) -> str:
    text = source.read_text(encoding="utf-8")
    match = MERMAID_RE.search(text)
    if not match:
        raise ValueError(f"No Mermaid block found: {source.relative_to(ROOT)}")
    return match.group(1).rstrip() + "\n"


def expected_mermaid_outputs() -> list[tuple[Path, Path, str]]:
    outputs: list[tuple[Path, Path, str]] = []
    for rel, svg_name in MERMAID_SOURCES.items():
        source = ROOT / rel
        mmd = MERMAID_DIR / f"{Path(svg_name).stem}.mmd"
        outputs.append((mmd, ASSETS / svg_name, extract_mermaid(source)))
    return outputs


def write_mermaid_sources() -> list[tuple[Path, Path]]:
    MERMAID_DIR.mkdir(parents=True, exist_ok=True)
    pairs: list[tuple[Path, Path]] = []
    for mmd, svg, source_text in expected_mermaid_outputs():
        mmd.write_text(source_text, encoding="utf-8")
        pairs.append((mmd, svg))
    return pairs


def minify_svg(svg: Path) -> None:
    text = svg.read_text(encoding="utf-8")
    text = re.sub(r">\s+<", "><", text.strip())
    svg.write_text(text + "\n", encoding="utf-8")


def render_mermaid(pairs: list[tuple[Path, Path]]) -> None:
    local_tmp = ROOT / ".codex-local" / "tmp"
    env = os.environ.copy()
    env.setdefault("npm_config_cache", str(local_tmp / "npm-cache"))
    env.setdefault("PUPPETEER_CACHE_DIR", str(local_tmp / "puppeteer-cache"))
    env.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(local_tmp / "playwright-browsers"))
    for mmd, svg in pairs:
        svg.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            "npx",
            "-y",
            f"@mermaid-js/mermaid-cli@{MERMAID_CLI_VERSION}",
            "-i",
            str(mmd),
            "-o",
            str(svg),
            "--backgroundColor",
            "transparent",
        ]
        print("render:", " ".join(cmd), flush=True)
        subprocess.run(cmd, check=True, env=env)
        minify_svg(svg)


def level_prefix_svg_text() -> str:
    width = 1320
    row_h = 48
    header_h = 64
    title_h = 72
    height = title_h + header_h + row_h * len(LEVEL_PREFIX_ROWS) + 48
    cols = [40, 350, 520, 650]
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">F-05: レベル接頭辞一覧</title>',
        '<desc id="desc">AI適用段階、権限、観測性、セキュリティ、ガバナンス、判断、対立、実験、評価証拠、スキルの各接頭辞を整理した表</desc>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        '<style>text{font-family:-apple-system,BlinkMacSystemFont,&quot;Segoe UI&quot;,&quot;Noto Sans JP&quot;,sans-serif;fill:#172033}.title{font-size:30px;font-weight:700}.head{font-size:17px;font-weight:700;fill:#0f3b63}.cell{font-size:16px}.small{font-size:14px;fill:#46556b}.line{stroke:#c9d3e1;stroke-width:1}.headbg{fill:#eaf4ff}.rowbg{fill:#f8fbff}.tag{font-weight:700;fill:#0b5cad}</style>',
        '<text class="title" x="40" y="46">F-05: レベル接頭辞一覧</text>',
        f'<rect class="headbg" x="30" y="{title_h}" width="1260" height="{header_h}" rx="12"/>',
        f'<text class="head" x="{cols[0]}" y="{title_h + 39}">領域</text>',
        f'<text class="head" x="{cols[1]}" y="{title_h + 39}">表記</text>',
        f'<text class="head" x="{cols[2]}" y="{title_h + 39}">主な章</text>',
        f'<text class="head" x="{cols[3]}" y="{title_h + 39}">用途</text>',
    ]
    y0 = title_h + header_h
    for i, (domain, notation, chapter, usage) in enumerate(LEVEL_PREFIX_ROWS):
        y = y0 + row_h * i
        if i % 2 == 0:
            lines.append(f'<rect class="rowbg" x="30" y="{y}" width="1260" height="{row_h}"/>')
        lines.append(f'<line class="line" x1="30" x2="1290" y1="{y}" y2="{y}"/>')
        cy = y + 31
        lines.append(f'<text class="cell" x="{cols[0]}" y="{cy}">{html.escape(domain)}</text>')
        lines.append(f'<text class="cell tag" x="{cols[1]}" y="{cy}">{html.escape(notation)}</text>')
        lines.append(f'<text class="cell" x="{cols[2]}" y="{cy}">{html.escape(chapter)}</text>')
        lines.append(f'<text class="cell" x="{cols[3]}" y="{cy}">{html.escape(usage)}</text>')
    lines.append(f'<line class="line" x1="30" x2="1290" y1="{y0 + row_h * len(LEVEL_PREFIX_ROWS)}" y2="{y0 + row_h * len(LEVEL_PREFIX_ROWS)}"/>')
    lines.append(f'<text class="small" x="40" y="{height - 18}">注: E0〜E5は使わず、実験はX、評価証拠はEVを使う。</text>')
    lines.append('</svg>')
    return re.sub(r">\s+<", "><", "\n".join(lines).strip()) + "\n"


def write_level_prefix_svg() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ASSETS / "f-05-level-prefixes.svg").write_text(level_prefix_svg_text(), encoding="utf-8")


def check_outputs() -> int:
    errors: list[str] = []
    expected_svgs = [ASSETS / name for name in MERMAID_SOURCES.values()] + [ASSETS / "f-05-level-prefixes.svg"]
    for svg in expected_svgs:
        if not svg.exists():
            errors.append(f"missing figure asset: {svg.relative_to(ROOT)}")
        elif svg.stat().st_size == 0:
            errors.append(f"empty figure asset: {svg.relative_to(ROOT)}")
    for mmd, _svg, expected in expected_mermaid_outputs():
        if not mmd.exists():
            errors.append(f"missing Mermaid source: {mmd.relative_to(ROOT)}")
            continue
        actual = mmd.read_text(encoding="utf-8")
        if actual != expected:
            errors.append(f"stale Mermaid source: {mmd.relative_to(ROOT)}")
    level_svg = ASSETS / "f-05-level-prefixes.svg"
    if level_svg.exists() and level_svg.read_text(encoding="utf-8") != level_prefix_svg_text():
        errors.append(f"stale static figure asset: {level_svg.relative_to(ROOT)}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"figure assets OK ({len(expected_svgs)} SVG files)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract Mermaid sources and render committed SVG figure assets.")
    parser.add_argument("--extract-only", action="store_true", help="write .mmd sources and static SVG without running Mermaid CLI")
    parser.add_argument("--check", action="store_true", help="verify expected SVG and extracted Mermaid source files are current")
    args = parser.parse_args()
    if args.check:
        return check_outputs()
    pairs = write_mermaid_sources()
    write_level_prefix_svg()
    if not args.extract_only:
        render_mermaid(pairs)
    return check_outputs()


if __name__ == "__main__":
    raise SystemExit(main())
