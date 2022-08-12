from bs4 import BeautifulSoup
import csv
f = open('zexprwire.txt', 'r', encoding='utf-8')
html_text = f.read()
soup = BeautifulSoup(html_text, 'lxml')

csv_data = [['Time Posted', 'title', 'link']]
all_news = soup.find_all('article')
for news in all_news:
    csv_data.append([news.find_next('time').text, news.h3.a['title'], news.h3.a['href']])


with open('data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
f.close()