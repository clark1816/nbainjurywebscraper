import requests
import csv
from bs4 import BeautifulSoup
csv_file = open('nba_injury.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['basketballwiretap'])
def extract():
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'}
    url = 'https://basketball.realgm.com/news/wiretap/tags/24/NBA_Injury'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'article clearfix')
    for item in divs:
        playername = item.find('a').text
        print(playername)
        csv_writer.writerow(playername.split())
    return

c = extract()
print(transform(c))
