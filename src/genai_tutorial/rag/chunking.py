"""Document chunking.

Chunking is where most RAG systems quietly fail: chunks that split mid-sentence
or mid-table retrieve poorly no matter how good the embedding model is.
Lesson 04 has learners measure that effect rather than take it on faith.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    source: str
    index: int


def fixed_size(text: str, source: str, size: int = 1000, overlap: int = 150) -> list[Chunk]:
    """Naive character-window chunking — the baseline to beat."""
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")

    chunks: list[Chunk] = []
    start = 0
    while start < len(text):
        window = text[start : start + size]
        chunks.append(Chunk(text=window, source=source, index=len(chunks)))
        start += size - overlap
    return chunks


def by_paragraph(text: str, source: str, max_chars: int = 1200) -> list[Chunk]:
    """Split on blank lines, packing paragraphs up to max_chars.

    TODO (lesson 04 exercise): make this respect markdown headings so a section
    title travels with the text beneath it.
    """
    raise NotImplementedError("Exercise 04.2 — see solutions/ once you have tried it.")
