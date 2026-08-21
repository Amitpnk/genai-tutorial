"""Example tools used in the tool-use lesson."""

from __future__ import annotations

from anthropic import beta_tool


@beta_tool
def get_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather for a location.

    Args:
        location: City and region, e.g. "Pune, MH".
        unit: Temperature unit, either "celsius" or "fahrenheit".
    """
    # Stubbed so the lesson runs without a weather API key. Lesson 03 swaps in
    # a real HTTP call as its first exercise.
    return f"22 degrees {unit} and clear in {location}"


@beta_tool
def search_docs(query: str, limit: int = 3) -> str:
    """Search the tutorial's document corpus and return matching passages.

    Args:
        query: Natural-language search query.
        limit: Maximum number of passages to return.
    """
    raise NotImplementedError("Exercise 06.1 — wire this to the retriever from lesson 05.")
