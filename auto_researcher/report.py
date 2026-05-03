from __future__ import annotations

from datetime import date

from .research import ResearchResult
from .text_utils import slugify


def render_markdown(result: ResearchResult) -> str:
    lines = [
        f"# Research Report: {result.topic}",
        "",
        f"Generated on: {date.today().isoformat()}",
        "",
        "## Executive Summary",
        "",
    ]

    lines.extend(f"- {sentence}" for sentence in result.summary)
    lines.extend(["", "## Key Findings", ""])
    lines.extend(f"- {finding}" for finding in result.key_findings)
    lines.extend(["", "## Important Keywords", ""])
    lines.append(", ".join(result.keywords) if result.keywords else "No keywords found.")
    lines.extend(["", "## Sources", ""])

    for index, source in enumerate(result.sources, start=1):
        citation = f"{index}. {source.title}"
        if source.url:
            citation += f" - {source.url}"
        lines.append(citation)

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "This report uses a lightweight extractive summarization workflow. For academic or professional use, verify all facts against the original sources.",
            "",
        ]
    )
    return "\n".join(lines)


def report_filename(topic: str) -> str:
    return f"{slugify(topic)}.md"

