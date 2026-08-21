import pytest

from genai_tutorial.rag.chunking import fixed_size

TEXT = "abcdefghij" * 30  # 300 chars


def test_fixed_size_covers_the_whole_document():
    chunks = fixed_size(TEXT, source="t.md", size=100, overlap=20)
    assert chunks[0].text == TEXT[:100]
    assert chunks[-1].text.endswith(TEXT[-10:])
    # Every character of the source must appear in at least one chunk.
    covered = set()
    start = 0
    for c in chunks:
        covered.update(range(start, start + len(c.text)))
        start += 80  # size - overlap
    assert covered >= set(range(len(TEXT)))


def test_fixed_size_overlaps_neighbours():
    chunks = fixed_size(TEXT, source="t.md", size=100, overlap=20)
    # The tail of one chunk must reappear at the head of the next, or a fact
    # straddling the boundary is retrievable from neither.
    assert chunks[0].text[-20:] == chunks[1].text[:20]


def test_fixed_size_indexes_sequentially():
    chunks = fixed_size(TEXT, source="t.md", size=100, overlap=20)
    assert [c.index for c in chunks] == list(range(len(chunks)))
    assert all(c.source == "t.md" for c in chunks)


def test_overlap_must_be_smaller_than_size():
    with pytest.raises(ValueError):
        fixed_size(TEXT, source="t.md", size=100, overlap=100)
