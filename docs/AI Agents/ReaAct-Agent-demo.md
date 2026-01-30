# React Agent Demo transcript

Hey there Eden here.

And in this video I'll be showing you what we're going to be building in this section.

And we'll be implementing a search agent, which is an agent which has searching capabilities.

So let's start with a quick demo.

So I'm in ChatGPT right now.

Let's now go and click the plus button.

And here we can go and select Web Search.

Now when we do this we provide ChatGPT with web search capabilities.

And if our query will require a web search it will go and use this tool, get the results, chew it

up and then return us the response grounded in the search results.

So let's try with this query.

Search for three job postings for an AI engineer using LinkedIn in the Bay area on LinkedIn and lists

their details.

Let's now send this query to ChatGPT and we'll follow along to see what it's going to do.

So you can see right now that now it's going to search the web.

And we can see we have some LinkedIn icons.

So this is some cool generative UI which we're going to discuss in the course.

So the application is reflecting what the agent is doing.

And it's now going to output the response.

And we can see that for each position we get we have here also a URL which is going to be where this

answer came from.

So we can see here this a engineering position for example which is hiring.

Now let's go and check out another position.

And here we can see we have a link chain index rag.

We have this description in the title.

Let's go and check the last one here.

And yeah here we can see generative AI Software Engineer.

Let's go and search here for link chain or.

Yeah.

So we can see we have here link chain.

And this looks like indeed like a solid job positioning.

Alrighty.

So again we can see we have now the summary.

And we have here the next steps.

And the important thing to note here is that for each response here we had the source.

Now this source, this grounding actually is very important to create the trust between the user and

the system.

Because if we only had the answers, then we couldn't decide as the users of this application whether

they're trustworthy or not.

And we know that Llms can hallucinate, they can generate a lot of garbage.

So when we have those sources URLs, we can go, we can check them, we can browse them, we can cross-check

what is returned from the LLM.

And that is indeed grounded in the source that it's used.

And we can even decide if we want to trust this source or not.

So this is a quick preview for something which is called generative UI, which we're going to discuss

in this course as well.

But the important thing to note here is the searching capabilities.

Large language models by themselves.

They are simply text in, text out.

Or if they're multimodal, they can accept also images and videos and audios and even produce them.

But the important thing to note is that they don't have real time information.

They're static in time because they're trained on a large corpus.

And if you're interested about that, feel free to check out the theory section where I discuss this.

But in general, they don't have access to the internet.

And if you want to give them this kind of access or access to external capabilities, we need to provide

them with tools.

And this is what we're going to do in this section.

So this section is going to be using learning agents for the first time.

And an interesting story is that when I created this course around 2022, ChatGPT and all the other

chat applications, they didn't have built in search.

And today all of those chat applications have built in search, and it's very useful and it's quite

a standard right now.

However, back in the day, this was not the case.

And it's interesting to see how those chat applications evolved.

So in this section we'll be implementing with Linkchain a search engine which is an LLM that's going

to have access to the exact same kind of search that we're seeing right now in this demo.
