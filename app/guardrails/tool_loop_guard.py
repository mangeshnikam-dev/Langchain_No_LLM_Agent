MAX_TOOL_CALLS = 3

class ToolCallLimiter:
    def __init__(self):
        self.count = 0

    def check(self) -> bool:
        if self.count >= MAX_TOOL_CALLS:
            return False
        self.count += 1
        return True

    def reset(self):
        self.count = 0
