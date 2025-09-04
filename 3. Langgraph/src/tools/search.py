from langchain.tools import tool 
from src.utils.linkutils import links_parser 
import requests
from bs4 import BeautifulSoup
import html2text
import sys
import requests
from colorama import Fore 

@tool
def GovSearch(url:str, search_depth=2): 
    """This tool returns information from approved government websites.
    Approved domains are as follows:  
        http://digital.gov.au
        https://architecture.digital.gov.au/
        https://www.dta.gov.au/digital-government-strategy 
    """
    print(Fore.LIGHTYELLOW_EX + f"☎️ Tool called with url {url}" + Fore.RESET) 
    approved_links = links_parser(["http://digital.gov.au","https://architecture.digital.gov.au/","https://www.dta.gov.au/digital-government-strategy"])
    if links_parser([url])[0] not in approved_links: 
        return f"Invalid link provided, link must source from {approved_links}"
    out = requests.get(url) 
    converter = html2text.HTML2Text()
    converter.ignore_links = False 
    markdown_content = converter.handle(out.text)
    return markdown_content 

if __name__ == '__main__': 
    print(GovSearch({"url":"https://digital.gov.au"}))
