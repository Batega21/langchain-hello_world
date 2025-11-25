from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate   
from langchain_core.messages import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from datetime import datetime
import os

def set_api_keys():
    os.environ.get("NEW_API_KEY") = "your_new_api_key_here"

load_dotenv()  # take environment variables from .env.

def save_response_to_file(response: AIMessage, filename: str):
    """Saves the response to a file with a timestamp."""
    try:        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Create file in folder name Summaries
        full_filename = f"summaries/{filename}_{timestamp}.md"

        data = response.content
        markdown_content = f"""# Summary Response

        ## Details

        Created At: {timestamp}

        ## Response Content

        ```markdown
        {data}
        ```
        """
        with open(full_filename, "w") as file:
            file.write(markdown_content)
        print(f"Response saved to {full_filename}")

    except Exception as e:
        print(f"Failed to save response to file: {e}")

def main():
    # print("Hello from hello-world!")
    # print(os.environ.get("GOOGLE_API_KEY"))
    
    # 1. Define the information about the person
    information = """
    Michael Gerard Tyson (born June 30, 1966) is an American former professional boxer who competed between 1985 and 2024. Nicknamed "Iron Mike"[5] and "Kid Dynamite" in his early career, and later known as "the Baddest Man on the Planet",[6] Tyson is regarded as one of the greatest heavyweight boxers of all time.[7] He reigned as the undisputed world heavyweight champion from 1987 to 1990.
    Tyson won his first 19 professional fights by knockout, 12 of them in the first round. Claiming his first belt at 20 years, 4 months, and 22 days old, Tyson holds the record as the youngest boxer ever to win a heavyweight title.[8] He was the first heavyweight boxer to simultaneously hold the World Boxing Association (WBA), World Boxing Council (WBC), and International Boxing Federation (IBF) titles, as well as the only heavyweight to unify them in succession. The following year, Tyson became the lineal champion when he knocked out Michael Spinks in 91 seconds of the first round.[9] In 1990, Tyson lost the undisputed heavyweight championship when he was knocked out by underdog Buster Douglas, making it one of the biggest upsets in boxing history.[10]
    In 1992, he was convicted of rape and sentenced to six years in prison. He was released on parole after three years.[11] After his release in 1995, he engaged in a series of comeback fights, regaining the WBA and WBC titles in 1996 to join Floyd Patterson, Muhammad Ali, Tim Witherspoon, Evander Holyfield and George Foreman as the only men in boxing history to have regained a heavyweight championship after losing it. After being stripped of the WBC title in the same year, Tyson lost the WBA title to Evander Holyfield by an eleventh round stoppage. Their 1997 rematch ended when Tyson was disqualified for biting Holyfield's ears. In 2002, Tyson fought for the world heavyweight title, losing by knockout to Lennox Lewis. In November 2024, his bout against Jake Paul, which he lost via unanimous decision, became the biggest boxing gate in US history outside of Las Vegas.[12][13]
    Tyson was known for his ferocious and intimidating boxing style as well as his controversial behavior inside and outside the ring, which he explained was inspired by Sonny Liston, a boxer who is widely regarded as the most intimidating man in the history of boxing.[14][15] With a knockout-to-win percentage of 88%,[16] he was ranked 16th on The Ring magazine's list of 100 greatest punchers of all time,[17] and first on ESPN's list of "The Hardest Hitters in Heavyweight History".[18] Sky Sports described him as "perhaps the most ferocious fighter to step into a professional ring".[19] He has been inducted into the International Boxing Hall of Fame and the World Boxing Hall of Fame.
    Outside his boxing career, Tyson has appeared in various popular media. He appeared in the well-received movies Rocky Balboa (2006) and The Hangover (2009).
    """
    
    # 2. Create a prompt template to generate a summary and interesting facts
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    
    # 3. Create a PromptTemplate and use ChatGoogleGenerativeAI to generate the summary
    summary_prompt_template = PromptTemplate(
        template=summary_template,
        input_variables=["information"],
    )
    
    # 4. Create the model and chain
    # model = ChatGoogleGenerativeAI(
    #     model="gemini-2.5-flash-lite",
    #     temperature=0,
    # )
    model = ChatOllama(
        model="gemma3:1b",
        temperature=0,
    )
    # 5. Invoke the chain and print the response (LCEL)
    chain = summary_prompt_template | model
    # 6. Get the response
    response = chain.invoke({"information": information})
    print("Debug the Response:", response.content)
    save_response_to_file(response, "summary_response")

if __name__ == "__main__":
    main()