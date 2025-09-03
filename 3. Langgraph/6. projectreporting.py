import requests
from langchain_ibm import ChatWatsonx 
from pydantic import BaseModel, Field
import pymupdf4llm
from dotenv import load_dotenv
from colorama import Fore 
import os 
import json
import sys 

load_dotenv()

class Review(BaseModel): 
    project_date: str = Field(description="The project commencement date")  
    use_case: str = Field(description="A brief summary of the project and use cases")  
    main_milestones: str = Field(description="Core milestones for the project including any dates.")  

def project_review_template(project_report:str) -> str: 
   return f"""You are an assistant designed to assist with project reporting.
    Review the pdf extract text provided and determine the project date, use case and main milestones.

    {project_report}
    """

llm = ChatWatsonx(
    model_id="meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
    project_id=os.environ['WATSONX_PROJECT_ID'],
    params={'max_tokens':5000, 'decoding_method':'greedy' }
)

reviewer_llm = llm.with_structured_output(Review)

if __name__ == '__main__': 
    while True: 
        prompt = input(Fore.LIGHTCYAN_EX + "⚡️ Enter the path to your project document here: " + Fore.RESET)
        if os.path.exists(prompt):  
            print(Fore.LIGHTYELLOW_EX + "🔍 File found" + Fore.RESET)
            print(Fore.LIGHTYELLOW_EX + "👨🏾‍💻 Loading document" + Fore.RESET)
            md_text = pymupdf4llm.to_markdown("project.pdf")
            print(Fore.LIGHTGREEN_EX + "🤖 Sending to LLM" + Fore.RESET)
            result = reviewer_llm.invoke(project_review_template(md_text)) 

            print(Fore.LIGHTMAGENTA_EX + str(dict(result)) + Fore.RESET) 
        else: 
            print(Fore.LIGHTRED_EX + f"File does not exist {prompt}" + Fore.RESET)





