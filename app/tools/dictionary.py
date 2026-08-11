import requests
from langchain_core.tools import tool

@tool
def define_word(word: str) -> str:
    """Get an English word definition using the free Dictionary API."""
    response = requests.get(
        f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
        timeout=5
    )
    if response.status_code != 200:
        return f"Could not find definition for '{word}'."

    try:
        definition = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
        return f"{word}: {definition}"
    except (KeyError, IndexError, TypeError):
        return f"No definition found for '{word}'."
