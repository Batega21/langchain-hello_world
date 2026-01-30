# Setup Search Agent

Branch: `ai/langChain/reAct-search-agent`

To set up the environment for a LangChain Search Agent, follow these steps:

Clone the Repository:
Open your terminal.

```sh
git clone <repository-link>
```

Replace <repository-link> with the URL of the relevant repository.

Navigate to the Directory:
Change into the cloned directory:

`cd <repository-name>`

Use the actual name of your cloned repository in place of <repository-name>.

Install the Necessary Packages:
Ensure you have Python and pip installed.
Install LangChain and other dependencies:

```sh
pip install langchain langchain-openai
```

Set Up Environment Variables:
Create a .env file to store API keys:

```sh
touch .env
```

Open the .env file and add your OpenAI API key as follows:


`OPENAI_API_KEY=your_api_key_here`

Download LangChain Documentation (if necessary):
To have the latest documentation for reference, you might want to run a scraping command:

`wget -r -np -k <documentation-url>`

Replace <documentation-url> with the current URL of LangChain documentation (you may need to check for the most recent URL).

Create Custom Search Agent:

Start coding your LangChain Search Agent using the template provided in the course.
Reference the LangChain documentation for specific configuration and methods relevant to building search agents.

Test Your Setup:

Run a simple script to verify if everything is working correctly.
Use the following command (replace script.py with your test script):

`python script.py`

By following these steps, you will have a functional environment set up for developing a LangChain Search Agent

## Transcript

Okay, so I checked out this branch which is called project slash react search agent.
And just a quick note if you want to check out the code for this section, check out this branch over here.
And for technical reasons, I committed the code to this branch over here and not the branch on the bottom left here.
Alright, let's start by initializing our Python project. Let's write UV init.
And now let's go install the dependencies. Let's add link chain.
We want to use link chain OpenAI. And we discussed those packages in previous videos.
So now we want to add a new package which is called link Chain.
And Tivoli is a third party which is going to help us connect our agent to the web and give the agent
searching capabilities so it will act as a search engine for our agent.
And it also has other very useful APIs like Tivoli Crawl, Tivoli Map, Tivoli Extract, which are very useful services for AI agents.
And we'll be using those capabilities in direct section of the course, so we'll cover them as well.
And by the way, today is actually the most popular choice for integrating a web search into an agent.
And they're even featured in the official documentation as the default service for a search engine when implementing agents.
So they really did go to example.
And I think the reason for that is that they first of all have an excellent API.
It scales very well.
It's very easy to use.
And I think they were actually the first ones to go and integrate this.
So to connect an agent A with searching capabilities.
Now it's also important to note that they have a very generous free tier.
And you can see it's 1000 API requests per month, which is going to be more than enough for this course.
All right.
Let me just show you a quick demo of the capabilities that we can integrate with it.
So in the API playground let me write a query like what are the latest anthropic models.
And we can see in the response we get here the URL of the source.
We also get the content you can see here.
It's talking about Cloud Outpost 4.1.
And in this search result it talks about Cloud Ops and site four.
And the search can be much more advanced.
We can have some special filtering and advanced capabilities.
However in this section we're only going to stick with the basics.
All right so that's enough about me.
And I'm going to link to in the videos resources.
Alrighty.
Let's go back to the code here.
And link chain Tavileh is the Tavileh link chain integration.
And here the provider is Tavileh in contrast to open AI in the previous example.
So a provider of link chain doesn't have to be a vendor which offers large language models.
It can also be a vendor which offer services that are exposed via API's and clients.
So in this case Tavileh is going to expose their services, their searching capabilities, their scraping
capabilities, and the link chain integration here is going to make our lives very, very easy when
we want to integrate those capabilities into our link chain link graph applications here, because the
team they wrote now, this integration, they connected to all the link chain objects, which we're
going to use.
And I'll give you a quick hint.
It's going to be link chain tools.
And this is another example of a link chain provider.
And I also forgot to add please also install Python.
And this is the original SDK which we are going to also be using in order to show you something very
very important.
All right let's go and also install Python dot env to load environment variables like we did before.
And let me also install black insert for some formatting
And uh yeah let's go and install everything.
So let me go and click enter.
We can check out the packages in the Pyproject.toml file over here.
And if you want the exact packages we can check out the UV dot log.
And let's go to our main.py file.
The boilerplate code.
Let's try it.
And let's run this code and make sure that it's working.
All right.
So we can see it's working.
And now let me show you what I have in my env file.
So like in the previous section I have my open API key I have Lang Smith.
Tracing equals true.
So we want to trace everything and we want to check out the traces I have here my link Smith API key.
Like previous sections I have my Lang Smith project which I changed in code search agent.
And I also have here a API key which I got from the UI.
All right, let me show you how you can get it.
You simply need to go to Tavileh to log in.
Let me now go and log with Google.
And right here I have my environment.
You can see all my API keys.
Let me go and generate an API key.
For example I'm using the free plan.
By the way.
Let me go and click here this plus button Now let's name the API key.
Let's call it API key.
I'm going to limit my monthly usage. And yeah let's hit create. And here you can simply go you can check out you can review the API key. You can copy it.

And this is the value that you should put in your um dot env file. So let me go back now to the env file. And it's also important to note that the name of the environment variable needs to be underscore API key, because that's where link chain is going to be looking for the credentials to authenticate to the services.

So it's working very similarly to the OpenAI API key here, where it's going to look for that API key in the environment variables.
Alrighty, let's go now to our main.py file.
And let's start with the imports.
And first let's go and let's load all the environment variables from the env file like we did in the previous video.
So let's import the load function.
And I want to call it in the beginning of the file here.
