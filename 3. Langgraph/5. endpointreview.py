import requests
from bs4 import BeautifulSoup
from src.utils.linkutils import url_to_markdown
from langchain_ibm import ChatWatsonx 
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os 
import json
import sys 
from colorama import Fore 

load_dotenv()

# Link extraction
class Url(BaseModel): 
    urls: list = Field(description="The list of urls") 

class Review(BaseModel): 
    trust_flag: bool = Field(description="Does the statement build trust")  
    trust_explanation: str = Field(description="Explain why or why not the statement builds trust")  
    sentiment: float = Field(description="Return a sentiment score between -1 to 1 with -1 being negative sentiment and 1 being positive sentiment")  
    polarity: float = Field(description="Return a polarity score between -1 to 1 with -1 being subjective and 1 being objective")  
    summary: str = Field(description="A 100 word summary about the page.")   

def link_extraction_template(urls:str) -> str: 
   return f"""You are an assistant designed to assist with policy compliance.
    Review the urls provided and return only those which are likely to contain information about AI transparency or policy.

    {urls}

    If you are unsure, play it safe and return the url. We are aiming for completeness over accuracy as each url will be deeply reviewed.
    """

def site_review_template(site_text:str) -> str: 
   return f"""You are an assistant designed to assist with policy compliance.
    Review the text provided and determine if the policy builds trust and why, compute it's sentiment and polarity and create a short summary of what the text talks about.

    {site_text}
    """

llm = ChatWatsonx(
    model_id="meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
    project_id=os.environ['WATSONX_PROJECT_ID'],
    params={'max_tokens':5000, 'decoding_method':'greedy' }
)

link_extractor_llm = llm.with_structured_output(Url)
reviewer_llm = llm.with_structured_output(Review)

def link_scraper(base_url:str): 
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser') 
    links = list(set([link['href'] for link in soup.find_all('a', href=True)]))
    links = list(filter(lambda x: "#" not in x.split(), links))
    links = list(filter(lambda x: base_url != x, links))
    return links

def ai_link_extractor(links_to_review, url_prefix=None):
    base_links = []
    for base_url in links_to_review: 
        links = link_scraper(base_url) 
        response = link_extractor_llm.invoke(link_extraction_template(links)) 
        filtered_links = list(filter(lambda x: x in links, response.urls))
        filtered_links = [f"{base_url if url_prefix==None else url_prefix}{x}" if x[:4] != 'http' else x for x in filtered_links]
        base_links = [*base_links, *filtered_links]

    return base_links

if __name__ == '__main__': 
    while True: 
        prompt = input(Fore.LIGHTCYAN_EX + "⚡️ Enter the site(s) you'd like to review: " + Fore.RESET)
        try: 
            links_to_review = [prompt]
            print(Fore.LIGHTYELLOW_EX + "🔗 Crawling Level 1 link tree" + Fore.RESET)
            lv1_links = ai_link_extractor(links_to_review)
            all_links = [*lv1_links]
            print(Fore.LIGHTGREEN_EX + f"{len(all_links)} links found" + Fore.RESET) 
            if len(all_links) > 0: 
                results = {}                
                for idx, link in enumerate(all_links): 
                    print(Fore.LIGHTYELLOW_EX + f"{idx+1}/{len(all_links)}: Evaluating: {link}" + Fore.RESET) 
                    site_data = url_to_markdown(link)
                    response = reviewer_llm.invoke(site_review_template(site_data)) 
                    print(Fore.LIGHTGREEN_EX + f"⚡️ {dict(response)}" + Fore.RESET) 
                    results[link] = dict(response)
                print(Fore.LIGHTGREEN_EX + f"💾 Consolidated results written to results.json" + Fore.RESET)              
                with open('result.json', 'w') as f: 
                    json.dump(results, f) 
            else: 
                print(Fore.LIGHTRED_EX + '🤷🏽‍♂️ Uh oh, no links found' + Fore.RESET) 
        except Exception as e: 
            print(Fore.LIGHTRED_EX + f"Something went wrong {e}" + Fore.RESET) 

   







