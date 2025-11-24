# Setup environment

## Basic steps

Generate folder
Git init
UV Python's package manager
    `uv add langchain`
    `uv add langchain-openai`
    `uv add langchain-google-vertexai`
    `uv add langchain-google-genai`
    `uv add python-dotenv`
    `uv add black isort` format
Add .gitignore
Generate .env
    Set API keys
Generate API Key on LLM - What billing

*Prompt Template*: A template of a Prompt and add a parameters.

*LangChain* chain is a workflow that connects multiple components and chaining together in a sequence, where the output of a step becomes the input of the next step.
Each step can be an LM call, a prompt, a data transformation or tool call.

### Langchain Chain Workflow

User Query
    |
Prompt Template - Format query into structured prompt
    |
Language Model - Generate response
    |
Output Parser - Parse LLM output into structured data
    |
External API Tool Call - Call external service
    |
Final LLM Call - Process API response
    |
Final Output

## Basic flow

1. Define the information about the subject.
2. Create a prompt template to generate a summary and interesting facts
3. Create a PromptTemplate and use ChatGoogleGenerativeAI to generate the summary
4. Create the model and chain
5. Invoke the chain and print the response
6. Get the response

`main.py`

Lang Expression Language LCEL: What should happen instead of who it should happen, allowing LangChain to optimize the run-time execution of the chains.

## Troubleshooting

Verify if dependencies are installed
`uv pip list`
Other verification methods:
Check sync status:
`uv sync --check`
Show specific package:
`uv pip show langchain`
Check lock file:
`cat uv.lock`
