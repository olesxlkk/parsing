import requests
from bs4 import BeautifulSoup

url = 'https://www.nstu.ru/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
news_in_div = soup.find_all('div', class_='bottomLine')

news = []
for div in news_in_div:
    url = div.select('a')[1]
    title = url.text
    link = url['href']
    id = int(link.split('=')[1])
    news.append({'id': id, 'url': link, 'title': title})
    
print(news)