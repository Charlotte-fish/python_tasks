from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 前提：安装selenium这个库，下载chromedriver驱动程序
# 选择一：将chromedriver.exe放在当前目录下，并将当前目录完整路径放在环境变量path中。
#        直接使用driver = webdriver.Chrome()
# 选择二：将chromedriver.exe放在其他目录下，并将那个目录绝对路径放在环境变量中。
#        使用webdriver.Chrome(executable_path='防止chromedriver的路径')
driver = webdriver.Chrome()

driver.get('http://127.0.0.1:5000')

student_li_list = driver.find_elements_by_css_selector('li')

students = []
for student_li in student_li_list:
  students.append(student_li.text.strip())

print('=================================')
print(students)

driver.close()