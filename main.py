from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_google_genai import GoogleGenerativeAI
from langchain_tavily import TavilySearch

from schemas import AgentResponse

# Tools
tools = [TavilySearch()]

# LLM
llm = GoogleGenerativeAI(model="gemini-2.0-flash-exp")

# Agent Executor
agent = create_agent(
    model=llm,
    tools=tools,
    response_format=AgentResponse,
)

def main():
    result = agent.invoke(
      {
        "messages": [
            {
                "role": "user",
                "content": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
            }
        ]
      }
    )

    structured = result.get("structured_response", None)
    print(structured if structured is not None else result)

    # Debug Console
      # type(result) <class 'dict'>s
      # type(result["output"]) <class 'str'>
      # output_parser.parse(result["output"]) <class 'AgentResponse'>
      # type(output_parser.parse(result["output"])) <class 'schemas.AgentResponse'>
      # output_parser.parse(result["output"]).answer === AI answer
      # output_parser.parse(result["output"]).sources === job posting sources


if __name__ == "__main__":
    main()
