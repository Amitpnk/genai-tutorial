import pytest


class _Block:
    def __init__(self, text):
        self.type = "text"
        self.text = text


class _Usage:
    input_tokens = 100
    output_tokens = 20
    cache_creation_input_tokens = 0
    cache_read_input_tokens = 80


class _Response:
    def __init__(self, text):
        self.content = [_Block(text)]
        self.usage = _Usage()
        self.stop_reason = "end_turn"


class FakeMessages:
    """Records the params it was called with so tests can assert on them."""

    def __init__(self):
        self.last_params = None

    def create(self, **params):
        self.last_params = params
        return _Response("stub response")


class FakeClient:
    def __init__(self):
        self.messages = FakeMessages()


@pytest.fixture
def fake_client(monkeypatch):
    """Replace the module-level client so no test touches the network.

    Deliberately a stub, not a skip: a test that quietly skips without an API
    key stops protecting the code the day CI loses its key.
    """
    from genai_tutorial import client as client_module

    fake = FakeClient()
    monkeypatch.setattr(client_module, "_client", fake)
    return fake
