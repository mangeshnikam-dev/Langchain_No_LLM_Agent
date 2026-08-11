from app.agent.agent import NoLLMAgent

def test_unknown_request():
    result = NoLLMAgent().invoke("hello")
    assert "don't know" in result.lower()
