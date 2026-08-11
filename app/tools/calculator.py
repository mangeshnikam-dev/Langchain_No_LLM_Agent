from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """Calculate a basic mathematical expression."""
    allowed_chars = "0123456789+-*/(). "
    if not expression or not all(c in allowed_chars for c in expression):
        raise ValueError("Expression contains unsupported characters.")

    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception:
        return "Unable to calculate the expression."
