from genai_tutorial import ask, usage_line


def test_ask_returns_text(fake_client):
    assert ask("hello") == "stub response"


def test_ask_sends_expected_params(fake_client):
    ask("hello", system="be terse", effort="low", max_tokens=500)
    params = fake_client.messages.last_params

    assert params["system"] == "be terse"
    assert params["max_tokens"] == 500
    assert params["output_config"] == {"effort": "low"}
    assert params["messages"] == [{"role": "user", "content": "hello"}]
    # No `thinking` key: adaptive is the default on Opus 5 and passing
    # budget_tokens would be rejected outright.
    assert "thinking" not in params


def test_ask_omits_system_when_absent(fake_client):
    ask("hello")
    assert "system" not in fake_client.messages.last_params


def test_usage_line_reports_cache_columns(fake_client):
    response = fake_client.messages.create(model="stub", max_tokens=1, messages=[])
    line = usage_line(response)
    assert "cache_read=80" in line
    assert "cache_write=0" in line
