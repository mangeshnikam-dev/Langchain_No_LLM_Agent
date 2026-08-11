SENSITIVE_TOOLS = {"send_email", "delete_file", "create_ticket", "make_payment"}

def requires_approval(tool_name: str) -> bool:
    return tool_name in SENSITIVE_TOOLS
