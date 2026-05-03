from __future__ import annotations

import argparse
from pathlib import Path

from .report import render_markdown, report_filename
from .research import build_research, parse_source_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Markdown research report.")
    parser.add_argument("topic", help="Research topic")
    parser.add_argument("--source", required=True, help="Path to a source notes text file")
    parser.add_argument("--out", default="reports", help="Output folder")
    args = parser.parse_args()

    source_path = Path(args.source)
    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    sources = parse_source_file(source_path.read_text(encoding="utf-8"))
    result = build_research(args.topic, sources)
    report = render_markdown(result)
    output_path = output_dir / report_filename(args.topic)
    output_path.write_text(report, encoding="utf-8")

    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    main()

