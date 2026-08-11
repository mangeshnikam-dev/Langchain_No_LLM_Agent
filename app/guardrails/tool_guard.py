ALLOWED_TOOLS = {"weather", "calculator", "dictionary"}

def validate_tool(tool_name: str) -> tuple[bool, str]:
    if tool_name not in ALLOWED_TOOLS:
        return False, f"Tool '{tool_name}' is not allowed."
    return True, ""
