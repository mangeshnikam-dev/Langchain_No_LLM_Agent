from app.tools.calculator import calculate

def test_calculator():
    assert calculate.invoke({"expression": "25 * 4"}) == "100"
