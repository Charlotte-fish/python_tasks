import requests
import json

students = []
for page in range(1, 5):
  url = f'http://127.0.0.1:5000/data?page={page}'
  
  print(f'Crawling {url}...')

  r = requests.get(url)
  r.encoding = 'utf8'

  data_dict = json.loads(r.text)
  
  for student in data_dict['data']:
    students.append(student.strip())

print('==================================')
print(students)