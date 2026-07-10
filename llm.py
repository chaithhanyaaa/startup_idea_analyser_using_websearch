from langchain_ollama import ChatOllama


def get_llm():
    """
    Returns the configured Ollama model.
    """

    return ChatOllama(
        model="qwen2.5:3b",
        temperature=0.3
    )