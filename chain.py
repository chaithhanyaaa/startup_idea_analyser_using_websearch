from websearch import research_startup
from prompt import startup_analysis_prompt, parser
from llm import get_llm

llm = get_llm()

chain = startup_analysis_prompt | llm | parser


def analyze_startup(idea: str):

    research = research_startup(idea)

    response = chain.invoke(
        {
            "idea": idea,
            "research": research["research"]
        }
    )

    return {
        "analysis": response.model_dump(),
        "sources": research["sources"],
        "error": research.get("error")
    }
