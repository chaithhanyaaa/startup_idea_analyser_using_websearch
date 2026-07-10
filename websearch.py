from tavily import TavilyClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create the client once
client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def research_startup(idea: str) -> dict:
    """
    Fetch research related to a startup idea.

    Args:
        idea (str): Startup idea entered by the user.

    Returns:
        dict
    """

    try:

        response = client.search(
            query=idea,
            max_results=5
        )

        research = ""

        sources = []

        for result in response["results"]:

            research += (
                f"Title: {result['title']}\n"
                f"Content: {result['content']}\n\n"
            )

            sources.append(result["url"])

        return {
            "research": research,
            "sources": sources,
            "error": None
        }

    except Exception as e:

        return {
            "research": "",
            "sources": [],
            "error": str(e)
        }
    
if __name__ == "__main__":

    result = research_startup(
        "AI interview preparation platform for college students"
    )

    print(result)