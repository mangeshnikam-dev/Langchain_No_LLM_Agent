from app.tools.registry import TOOLS
from app.guardrails.tool_guard import validate_tool
from app.guardrails.approval_guard import requires_approval

def execute_tool(tool_name: str, arguments: dict, approval_callback=None) -> str:
    allowed, reason = validate_tool(tool_name)
    if not allowed:
        return f"Tool blocked: {reason}"

    tool = TOOLS.get(tool_name)
    if tool is None:
        return f"Tool '{tool_name}' does not exist."

    if requires_approval(tool_name):
        if approval_callback is None or not approval_callback(tool_name):
            return "Tool execution rejected by human approval guardrail."

    try:
        return str(tool.invoke(arguments))
    except Exception as exc:
        return f"Tool execution failed: {exc}"
