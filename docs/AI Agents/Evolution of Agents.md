# Evolution of Agents

## Summary

In this lecture, the focus is on the evolution of LangChain ReAct agents, starting from their inception at LinkedIn in November 2022. Here are the main points:

Initial Development: The original LangChain ReAct agent utilized a react prompting method to interpret actions and observations in text format.
Advancements in LMs: With the development of large language models, specifically native function calling capabilities, the architecture transitioned to tool calling agents. This enhancement enabled more reliable tool execution through structured function calls.
New ReAct Agent: A significant advancement introduced a new ReAct agent that incorporated function calling within a low-level orchestration framework, facilitating durable execution and fine-grained control, which are essential for production applications.
Create Agent Function: The introduction of the 'create agent' function in LangChain version 1.0 offers a high-level interface while utilizing the established LangGraph ReAct agent, allowing for easier agent creation.
Hands-on Exploration: Participants will engage in hands-on exploration of each iteration of these agents, starting with the latest features and moving backward, providing a thorough understanding of functionality and improvements.
Learning Goals: The lecture aims to equip participants with the knowledge necessary to navigate the complexities of agent development, focusing on the importance of understanding modern interfaces.

## Transcript


Lecture thumbnail
3:19 / 3:21
The react agent pattern has undergone significant evolution since it was introduced in LinkedIn back

in November of 2022, and initially, the Lang chain react agent relied purely on react prompting,

where the model would reason about the actions and observations in a text based format.

And as the LM landscape evolved with the native function calling feature capabilities of large language

models, this architecture transitioned into tool calling agents, which leveraged the structured function

calling instead of prompt based tool selection.

And this made tool execution more reliable and more efficient.

Now the next major leap came with the react agent, which maintained function calling but rebuilt the

agent on top of the graph's low level orchestration framework, providing with durable execution, persistence

ability and fine grained control needed for production grade applications.

Replications, and in the long chain version 1.0 linked Chain introduced the create agent function,

which provides a clean, high level interface while being powered with the battle tested Landgraf React

agent under the hood, and in this course, we'll walk through each one of these agent iterations.

Hands on.

Starting from the latest and greatest create agent function.

Moving back to the original OG react implementation in progressively build up towards the modern V1

agent architecture.

So you can understand not just how to use these agents, but how they actually work underneath the hood,

what each iteration improved and it will give you a very strong intuition when implementing production

grade agents.

Now, I know I mentioned tool calling and Landgraf and we haven't really discussed any of this.

We'll have plenty of time to do that.

And we'll be diving very, very deep into each one of those iterations and into each one of those agents

and each one of those topics like tool calling, like line graph.

And the only thing you need to remember from this video is that we're going to be iterating through

agent implementations until we get to a final agent implementation, which is robust and production

ready.

We're going to be starting with the latest create agent function.

And in this section we are going to learn how to use this function and how to create modern link chain

agents.

And now because learning about agents can be a bit overwhelming.

So what I decided to do is teach you in this section just the interface.

So how to create and how to get started really, really quick.

And in the sections afterward, we're going to be diving one layer deeper and understand how those agents

originated.

What is this magic of agents, how it's happening under the hood?

A lot of very cool and important things that every engineer must know.

And I promise you, it's going to be very cool.