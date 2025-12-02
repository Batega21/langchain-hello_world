from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import GoogleGenerativeAI
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

# Tools
tools = [TavilySearch()]

# LLM
llm = GoogleGenerativeAI(model="gemini-2.0-flash-exp")

# Output Parser
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

# React Prompt
react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names"],
).partial(format_instructions=output_parser.get_format_instructions())

# Agent Executor
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_format_instructions,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Runnable function to extract output
extract_output = RunnableLambda(lambda x: x["output"])

# Runnable function to parse output
parse_output = RunnableLambda(lambda x: output_parser.parse(x))

#  LangChain Chain
chain = agent_executor | extract_output | parse_output

def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
        }
    )
    print(result)

    # Debug Console
      # type(result) <class 'dict'>
      # type(result["output"]) <class 'str'>
      # output_parser.parse(result["output"]) <class 'AgentResponse'>
      # type(output_parser.parse(result["output"])) <class 'schemas.AgentResponse'>
      # output_parser.parse(result["output"]).answer === AI answer
      # output_parser.parse(result["output"]).sources === job posting sources


if __name__ == "__main__":
    main()
