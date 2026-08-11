BLOCKED_WORDS = ["password", "credit card", "secret key", "api key"]

def validate_input(user_input: str) -> tuple[bool, str]:
    if not user_input or not user_input.strip():
        return False, "Input cannot be empty."
    if len(user_input) > 500:
        return False, "Input is too long."
    lower = user_input.lower()
    for word in BLOCKED_WORDS:
        if word in lower:
            return False, "Request contains restricted information."
    return True, ""
