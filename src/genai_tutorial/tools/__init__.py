"""Tool definitions for lessons 03 and 06.

Tools are plain Python functions decorated with `@beta_tool`; the SDK derives
the JSON schema from the signature and docstring, which is why the docstrings
here are written for Claude to read, not just for humans.
"""

from genai_tutorial.tools.example_tools import get_weather, search_docs

__all__ = ["get_weather", "search_docs"]
