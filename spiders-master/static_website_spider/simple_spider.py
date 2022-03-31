import requests
from bs4 import BeautifulSoup


def crawl_student_from_link(url):
  result = {}

  r = requests.get(url)

  r.encoding = 'utf8'

  html = BeautifulSoup(r.text, 'html.parser')

  student_li_list = html.find_all('li')

  students = []
  for student_li in student_li_list:
    students.append(student_li.text.strip())

  links = []
  other_page_link_list = html.find_all('a')
  for other_page_link in other_page_link_list:
    links.append('http://127.0.0.1:8000/' + other_page_link['href'])

  result['students'] = students
  result['links'] = links

  return result


def get_next_url(quene):
  for url in url_quene:
    if not url_quene[url]:
      return url
  # else:
  #   return None #不写else也可以，因为当函数没有返回值时，会自动返回none

# 爬取字典，false表示未被爬取，被爬取设置为true
url_quene = {'http://127.0.0.1:8000/': False}

url = get_next_url(url_quene)

students = []
while url is not None:
  print(f'Crawling {url}...')

  info = crawl_student_from_link(url)
  students.extend(info['students'])

  for link in info['links']:
    if link not in url_quene:
      url_quene[link] = False

  url_quene[url] = True

  print(f'{url} finished.')

  url = get_next_url(url_quene)

print('==================================')
print(students)