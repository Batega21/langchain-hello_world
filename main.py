from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()  # take environment variables from .env.


def main():
    print("Hello from hello-world!")
    
    information = """
    """
    
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(
        template=summary_template,
        input_variables=["information"],
    )
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


if __name__ == "__main__":
    main()
  