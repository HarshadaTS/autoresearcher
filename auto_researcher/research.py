from __future__ import annotations

from dataclasses import dataclass

from .text_utils import keywords, split_sentences


@dataclass(frozen=True)
class SourceNote:
    title: str
    content: str
    url: str | None = None


@dataclass(frozen=True)
class ResearchResult:
    topic: str
    summary: list[str]
    key_findings: list[str]
    keywords: list[str]
    sources: list[SourceNote]


def parse_source_file(text: str) -> list[SourceNote]:
    blocks = [block.strip() for block in text.split("\n---\n") if block.strip()]
    notes: list[SourceNote] = []

    for index, block in enumerate(blocks, start=1):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        title = lines[0].removeprefix("Title:").strip() if lines else f"Source {index}"
        url = None
        content_lines = []

        for line in lines[1:]:
            if line.lower().startswith("url:"):
                url = line.split(":", 1)[1].strip()
            else:
                content_lines.append(line.removeprefix("Content:").strip())

        content = " ".join(content_lines) if content_lines else block
        notes.append(SourceNote(title=title, content=content, url=url))

    return notes


def build_research(topic: str, sources: list[SourceNote]) -> ResearchResult:
    combined_text = " ".join(source.content for source in sources)
    topic_terms = set(keywords(topic, limit=6))
    common_terms = keywords(combined_text, limit=12)
    sentences = split_sentences(combined_text)

    ranked_sentences = sorted(
        sentences,
        key=lambda sentence: _score_sentence(sentence, topic_terms, common_terms),
        reverse=True,
    )

    summary = ranked_sentences[:3] or ["Not enough source text was provided to create a full summary."]
    key_findings = ranked_sentences[3:8] or summary

    return ResearchResult(
        topic=topic,
        summary=summary,
        key_findings=key_findings,
        keywords=common_terms,
        sources=sources,
    )


def _score_sentence(sentence: str, topic_terms: set[str], common_terms: list[str]) -> int:
    sentence_lower = sentence.lower()
    topic_score = sum(3 for term in topic_terms if term in sentence_lower)
    keyword_score = sum(1 for term in common_terms if term in sentence_lower)
    length_score = 1 if 60 <= len(sentence) <= 220 else 0
    return topic_score + keyword_score + length_score

