from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search_tool(query: str) -> str:
    """
    Tool that searches the web
    Args:
        query (str): The search query
    Returns:
        str: The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0)
tools = [search_tool]
agent = create_agent(model=llm, tools=tools)

def main():
    result = agent.invoke({
        "messages": [
            HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the Argentina area on linkedin and list their details")
        ]
    })
    print("Agent Result:", result)
    

if __name__ == "__main__":
    main()