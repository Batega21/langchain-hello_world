# Agent setup - Tools and LLMs

## Environment

```sh
uv init
uv add langchain langchain-openai langchain-tavily tavily-python python-dotnev black isort
```

API Keys

```env
GOOGLE_API_KEY=****
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=****
LANGSMITH_PROJECT=hello-world
TAVILY_API_KEY=****
```
Branch: `ai/langChain/reAct-search-agent`

## Key points

In this chapter, the focus is on creating your first LangChain agent, highlighting the crucial components needed for its setup. Here are the key points:

Essential Components: The two main elements necessary for establishing an agent are tools and a language model (LM), which acts as the reasoning engine.

Importing Functions: The lecture begins by importing necessary functions from LinkedIn and OpenAI, setting up the functionality for the agent.

Definition of a Tool: A tool is defined as a function that the agent can execute. Tools can perform a variety of actions, such as calling APIs, searching databases, or running code.

Creating Tools: The process to create a tool is straightforward. It involves writing a standard Python function with type hints and docstrings. These elements help describe the function's purpose and parameters. The tool decorator from LangChain is then used to integrate the function into the agent.

Importance of Documentation: Clear and explicit documentation is emphasized, as the language model utilizes this information to decide when and how to invoke the tool.

Function Calling Concept: Modern language models can return special responses that prompt function calls, expanding their capabilities beyond just generating text.

Implementing a Search Agent: A practical example is provided where a simple search tool is created, returning a static response about the weather in Tokyo.

Creating the Agent: After defining the search tool, the lecture demonstrates how to create the agent by initializing the language model and providing it with a list of tools, which in this case includes only the search tool.

Running the Agent: Finally, the agent is invoked with a user query, showcasing its ability to process input and return results. The lecture concludes with a demonstration of running the agent and printing the output.

These points encapsulate the critical elements of this chapter and how they contribute to building a LangChain agent effectively.

## Transcription

And now we want to import the create agent function from LinkedIn.
Now, in order to create an agent, we need to give the agent two minimal things.
The first one is going to be tools, and the second is going to be an LM, which is going to be the reasoning engine.
So let's go and import the tool decorator from LinkedIn.
Let's go and import from LinkedIn core.
I want to import human message.
And we're going to be using human message to invoke the agent.
So this is going to be the input for the agent execution.
And lastly let's go and import from OpenAI chat OpenAI.
And this is going to supply for our agent our LM that we're going to be using.
All right so now is a good point to introduce blockchain tools and tools for the agent and tools for an LLM.

And let's go and clarify this topic.
All right.
So a tool is a function that an agent can execute.
It can be any function that we want.
So we can write the internal implementation of that function.
So this means we can give our agent endless possibilities of actions it can perform.
So we can make it call an API to search in a database to run and execute code.
We have total flexibility.
What this tool can do.
And once we write this tool, we can plug it into the agent and boom!
Like magic, the agent has the ability to go and execute this tool. And creating a tool is actually very, very simple.

All we need to do is to implement a function, a regular Python function with type hints and with some docstrings. So we'll have some description of what this function does, what arguments does it receive and what output does it output.

We then use the tool decorator by link chain.
This transforms this regular Python function into a tool which can be plugged in into an agent.
Now I want to emphasize a couple of things.

Now the type hinting the arguments, names and the docstrings of the function are very, very important because underneath the hood the large language model is going to use this description and the arguments type hints.

And it's going to be using that in order to choose whether to call this tool or not, and with which arguments and state of the art models these days support this functionality using something which is called function calling, which we will be elaborating a lot on this course.

Now, the gist of function calling is that instead of LMS just returning text or pictures or videos, they can also return a special response, which is a function that needs to be invoked in case it decides to.

And this is an extra capability that an LM can provide us.
And we are going to be treating this like a black box right now.
So we're not going to be diving deep into this.
We have plenty of time to do this in the course. All right. So back to the code.

We are going to implement a search agent.
So it's going to have a search tool.
And the search tool is going to receive a query.
It's going to search it in the internet.
And then it's going to output the response. Right.

So this is the Python signature of the tool we're going to be writing.
So this is a custom tool that we're going to be writing here.
And let me write here a very simple implementation.

Let's simply here print the query and let's return the string.
Tokyo weather is sunny right now.
This is a static function.
It doesn't really search over the internet, it simply returns the string. Tokyo weather is sunny.

This is what this function is doing. Of course, we'll be writing the real implementation in this video.

So let's go now and add to this function the doc strings. And here I have a description that this is a tool that searches over the internet.

The argument is query and it returns the search result.
So this is not the best description right now but it will suffice for this example.
In general, the rule of thumb is that we want to make this description as explicit and unambiguous as possible.

So the LLM would really have an easy time to decide whether to call this tool or not.
All right.

So this is now a regular Python function if we want to convert it into a tool.
Let's go and decorate it with the tool decorator of chain.
And this is going to convert this Python function into a link chain tool.
Now what is exactly a link chain tool.
This is still not clear at this point of time.
Trust me, we'll get into that later.

But what chain is going to do is going to take all this metadata of the tool, name the arguments that they take the description and it's going to format it nicely, and it's going to help us plug this metadata and this information to an LLM call.
This is what is going to be doing under the hood.
Don't worry.
We're going to soon see this.
All right.

So assume now we have now an object which we can inject to our agent.
And it can suddenly has a certain capability.
So let's go and create that agent.
And for that let's go and create an instance of the LLM.
And I'll initialize a chat OpenAI object.

And let me now create a list of tools.
So it's going to be a list containing the search tool here.
And let's go now and create the agent.
So let's define a variable.
We'll call this variable agent.
We're going to give it as an input our model.

So our LM and we're going to provide it with the list of tools which is a list with a single item which has the search tool.
Boom.
That's it.
We have now an agent ready to go, ready to run with a search capability.
Right.
So it has an LM.
It has a list of tools which contains only one tool, which is the search tool that is allegedly supposed to do some online search, but currently it's only going to return us.
Tokyo weather is sunny here, so let's go and try to run a certain query with the agent right now.

So this agent is actually a runnable. So let me write a result variable and let's go. Right agent dot invoke.
And in order to run the agent, we need to give it a dictionary with the messages field.
And the messages field should be a list of messages for the agent which is going to contain the input.
So this is the user's query.
So here under messages I'm going to be sending the human message alongside with the content of what's the weather in Tokyo.
Now notice here that the key here is messages.
But I did not provide here a list of messages.
I just provided one message, one human message, not inside the list.
And this is okay because link chain under the hood is going to cast this into a list containing a single element of a human message.
So this is why it should still be working.
If you want, you can put here this inside of a list.
So let me go now and print here the result.