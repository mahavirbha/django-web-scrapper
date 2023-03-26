import requests
from bs4 import BeautifulSoup

def bsscript():
    page = requests.get("https://google.com/")
    soup = BeautifulSoup(page.text, 'html.parser')

    table_adr = []
    table_txt = []

    for link in soup.find_all('a'):
        link_address = link.get('href')
        link_text = link.string
        table_adr.append(link_address)
        table_txt.append(link_text)
    return table_adr, table_txt