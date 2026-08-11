import re

CITIES = ["pune", "mumbai", "delhi", "bangalore", "hyderabad"]

def route_request(user_input: str) -> dict:
    text = user_input.lower().strip()

    if "weather" in text or "temperature" in text:
        for city in CITIES:
            if city in text:
                return {"intent": "weather", "tool": "weather",
                        "arguments": {"city": city}}
        return {"intent": "weather", "tool": "weather",
                "arguments": {"city": "pune"}}

    calculation_match = re.search(
        r"(?:calculate|compute|what is)\s+([0-9+\-*/(). ]+)",
        text
    )
    if calculation_match:
        return {"intent": "calculation", "tool": "calculator",
                "arguments": {"expression": calculation_match.group(1).strip()}}

    if text.startswith("define ") or text.startswith("meaning of ") or "definition of" in text:
        word = text.split()[-1]
        return {"intent": "dictionary", "tool": "dictionary",
                "arguments": {"word": word}}

    return {"intent": "unknown", "tool": None, "arguments": {}}
