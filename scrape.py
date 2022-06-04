import requests
from bs4 import BeautifulSoup
import lxml

class Scraper:
    def __init__(self):
        pass

    def scrape_poems(self, url):
        first_lines = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
        for link in soup.find_all('a'):
            poem_url = link.get('href')
            if(poem_url == None):
                continue
            line = poem_url[1:len(poem_url)]
            line = list(line.split("_"))
            for word in line:
                if word == 'Series' or word =='One' or word == 'Two' or word == 'Three' or word == 'Index'\
                    or word == 'of' or word == 'First' or word == 'Lines':
                    continue
                word = str(word).lower()
                first_lines.append(word)
            #this way you can distinguish betweens poems and avoid connections across poems
            first_lines.append('END')

        return first_lines