from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    max_retries=6,  # Crucial for handling temporary "exhaustion"
)

agent = create_agent(
    llm,
    tools,
    response_format=AgentResponse,
)


def main():
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Provide some examples regarding the practical applications of AI agents",
                }
            ]
        }
    )
    print(result)
    
    structured = result.get("structured_response", {})
    print(structured if structured is not None else result)


if __name__ == "__main__":
    main()
