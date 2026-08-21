"""Scorers, cheapest-first.

Reach for a deterministic scorer when one fits; an LLM judge costs money and
introduces its own variance, so it is the last resort, not the first.
"""

from __future__ import annotations


def exact_match(output: str, expected: str) -> float:
    return 1.0 if output.strip() == expected.strip() else 0.0


def contains_all(output: str, expected_terms: list[str]) -> float:
    lowered = output.lower()
    hits = sum(1 for term in expected_terms if term.lower() in lowered)
    return hits / len(expected_terms) if expected_terms else 0.0


def llm_judge(output: str, expected: str, rubric: str) -> float:
    """Score with Claude as judge.

    TODO (lesson 07 exercise): implement using structured outputs so the score
    comes back as a validated number rather than text you have to parse.
    """
    raise NotImplementedError("Exercise 07.3")
