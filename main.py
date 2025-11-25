from dotenv import load_dotenv

from typing import List
from pydantic import BaseModel, Field

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer: str = Field(description="Thr agent's answer to the query")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    result = agent.invoke({
        "messages": [
            HumanMessage(content="search for 3 job postings for a Digital Project Manager in the Argentina area on linkedin and list their details")
        ]
    })
    print("Agent Result:", result)
    

if __name__ == "__main__":
    main()