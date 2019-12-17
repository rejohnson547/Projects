from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/title/tt0944947/').text

soup = BeautifulSoup(source, 'html5lib')

artical = soup.find('artical')

title = soup.find('div', class_='title_wrapper')
summary = soup.find('div', class_='summary_text')

print(title.h1.text)
print('\n')
print(summary.text.strip())