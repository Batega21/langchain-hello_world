# LangChain

## LangChain Udemy Course

Welcome to the AI Agents with LangChain and LangGraph Udemy course - Unleashing the Power of Agentic AI!
This  course is designed to teach you how to QUICKLY harness the power the LangChain & LangGraph libraries for LLM applications and Agentic AI.
This course will equip you with the skills and knowledge necessary to develop cutting-edge LLM solutions for a diverse range of topics.

| Please note that this is not a course for beginners. This course assumes that you have a background in software engineering and are proficient in Python. I will be using Pycharm IDE but you can use any editor you'd like since we only use basic feature of the IDE like debugging and running scripts .

*What You’ll Build:*  No fluff. No toy examples. You’ll build:

- Search Agent
- Documentation Helper – A chatbot over Python package docs (and any data you choose), using advanced retrieval and RAG.
- Slim ChatGPT Code Interpreter – A lightweight code execution assistant.
- Prompt Engineering Theory Section
- Introduction to LangGraph
- Introduction to Model Context Protocol (MCP)
- Ice Breaker Agent – An AI agent that searches Google, finds LinkedIn and Twitter profiles, scrapes public info, and generates personalized icebreakers.


## Course Overview

### The topics covered in this course include

- AI Agents
- Agentic AI
- AI Engineering
- LangChain, LangGraph
- LLM + GenAI History
- Prompt Engineering: Few shots prompting, Chain of Thought, ReAct prompting
- Context Engineering
- Chat Models
- Open Source Models
- Prompts, PromptTemplates, langchainub
- Output Parsers, Pydantic Output Parsers
- Chains: create_retrieval_chain, create_stuff_documents_chain
- Agents, Custom Agents, Python Agents, CSV Agents, Agent Routers
- OpenAI Functions, Tool Calling
- Tools, Toolkits
- Memory
- Vectorstores (Pinecone, FAISS, Chroma)
- RAG (Retrieval Augmentation Generation)
- DocumentLoaders, TextSplitters
- Streamlit (for UI), Copilotkit
- LCEL
- LangSmith
- LangGraph
- GIST of Cursor IDE 
- Cursor Composter
- Curser Chat
- MCP - Model Context Protocol & LangChain Ecosystem
- Introduction To LangGraph

Throughout the course, you will work on hands-on exercises and real-world projects to reinforce your understanding of the concepts and techniques covered. By the end of the course, you will be proficient in using LangChain to create powerful, efficient, and versatile LLM applications for a wide array of usages.

## Why This Course?

- Up-to-date: Covers LangChain V.1+ and the latest LangGraph ecosystem.
- Practical: Real projects, real APIs, real-world skills.
- Career-boosting: Stay ahead in the LLM and GenAI job market.
- Step-by-step guidance: Clear, concise, no wasted time.
- Flexible: Use any Python IDE (Pycharm shown, but not required).

## React Agent

### Structured Output

1. What is the key difference between using `.with_structured_output()` and traditional output parsers?

**`.with_structured_output()` uses function calling when available, falling back to parsing when not
**The `.with_structured_output()` method intelligently uses function calling (tool calling) when the model supports it, which is more reliable than text parsing. When function calling isn't available, it falls back to using output parsers for text parsing.

2. What is the purpose of the partial_variables parameter in this prompt template?

```python
 prompt = PromptTemplate(
      template="Answer the user query.\n{format_instructions}\n{query}\n",
      input_variables=["query"],
      partial_variables={"format_instructions": parser.get_format_instructions()}
```

**To inject the parser's formatting instructions into every prompt**
The partial_variables parameter allows you to pre-populate certain template variables. Here, it automatically injects the format instructions from the parser into every prompt, ensuring the model knows how to format its output.

3. What does the `get_format_instructions()` method return?

**A string with instructions for how the model should format its output**
The `get_format_instructions()` method returns a string containing human-readable instructions that tell the language model how to format its output to be compatible with the parser.

4. What is the primary purpose of Output Parsers in LangChain?

**To transform raw text output from LLMs into structured, usable data formats**
Output parsers are specifically designed to transform the raw string output from language models into structured data formats like JSON objects, Pydantic models, or custom Python objects. This is their core functionality in LangChain.
