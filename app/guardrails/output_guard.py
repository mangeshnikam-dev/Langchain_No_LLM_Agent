def validate_output(output: str) -> tuple[bool, str]:
    if not output:
        return False, "Empty response."
    if len(output) > 2000:
        return False, "Response is too long."
    return True, ""
