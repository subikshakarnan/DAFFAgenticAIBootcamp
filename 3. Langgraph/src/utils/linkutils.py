import requests
import html2text


def links_parser(links:list) -> list:
    parsed_links = []
    for link in links: 
        link = link.split('//')[1].split('www.')
        link = link[1].split('/')[0] if len(link) > 1 else link[0].split('/')[0]
        parsed_links.append(link)  
    return parsed_links 

def url_to_markdown(url:str) -> str:
    out = requests.get(url) 
    converter = html2text.HTML2Text()
    converter.ignore_links = False 
    return converter.handle(out.text)


if __name__ == '__main__': 
    links= [
        "http://digital.gov.au",
        "https://architecture.digital.gov.au/",
        "https://www.dta.gov.au/digital-government-strategy" 
        ]
    print(links_parser(links)) 

