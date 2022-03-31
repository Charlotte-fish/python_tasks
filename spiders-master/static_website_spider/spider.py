import requests
from bs4 import BeautifulSoup


url = 'http://localhost:8000'
r = requests.get(url)
r.encoding = 'utf8'
# print(r.text)

soup = BeautifulSoup(r.text,'html.parser')
li_list = soup.select('li')
# print(li_list)

for li in li_list:
    print(li.text)