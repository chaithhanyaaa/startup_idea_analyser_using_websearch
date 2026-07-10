from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class StartupAnalysis(BaseModel):
    summary: str = Field(description="Short summary of the startup.")
    competitors: list[str] = Field(description="Major competitors.")
    market_opportunity: str = Field(description="Market opportunity.")
    strengths: list[str]
    weaknesses: list[str]
    risks: list[str]
    monetization: list[str]
    mvp_features: list[str]

parser = PydanticOutputParser(pydantic_object=StartupAnalysis)

startup_analysis_prompt = ChatPromptTemplate.from_template("""
You are an experienced Startup Consultant and Venture Capital analyst.

Analyze the following startup idea using the provided web research and return ONLY valid JSON matching the requested schema. Do not include markdown formatting, code fences, or extra commentary.

Startup Idea:
{idea}

Web Research:
{research}

{format_instructions}
""", partial_variables={"format_instructions": parser.get_format_instructions()})