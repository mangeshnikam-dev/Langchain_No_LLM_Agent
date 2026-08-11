from app.agent.router import route_request
from app.agent.executor import execute_tool
from app.guardrails.input_guard import validate_input
from app.guardrails.output_guard import validate_output
from app.guardrails.tool_loop_guard import ToolCallLimiter

class NoLLMAgent:
    def __init__(self):
        self.limiter = ToolCallLimiter()

    def invoke(self, user_input: str) -> str:
        self.limiter.reset()

        valid, reason = validate_input(user_input)
        if not valid:
            return f"Request blocked: {reason}"

        decision = route_request(user_input)
        print("\n========== AGENT TRACE ==========")
        print("USER:", user_input)
        print("ROUTER:", decision)

        if decision["tool"] is None:
            return "I don't know which tool to use for this request."

        if not self.limiter.check():
            return "Execution stopped: maximum tool-call limit reached."

        result = execute_tool(
            decision["tool"],
            decision["arguments"],
            approval_callback=self._human_approval
        )

        valid, reason = validate_output(result)
        if not valid:
            return f"Response blocked: {reason}"

        print("TOOL:", decision["tool"])
        print("ARGUMENTS:", decision["arguments"])
        print("RESULT:", result)
        print("=================================")
        return result

    @staticmethod
    def _human_approval(tool_name: str) -> bool:
        answer = input(f"Approve execution of '{tool_name}'? (yes/no): ")
        return answer.lower().strip() == "yes"
