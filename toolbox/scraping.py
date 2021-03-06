# html scraping

import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url, headers={"Accept-Language":"en-US"})
    soup = BeautifulSoup(response.content, "html.parser")
    return soup
