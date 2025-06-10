# Задание - https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

browser.find_element(By.NAME, 'firstname').send_keys('Раильчик')
browser.find_element(By.NAME, 'lastname').send_keys('Qa')
browser.find_element(By.NAME, 'email').send_keys('mailchik@mail.ru')

# Загружаем файл на сервер
bloknot = browser.find_element(By.ID, 'file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'files.txt')
bloknot.send_keys(file_path)

browser.find_element(By.CLASS_NAME, 'btn').click()
sleep(5)

browser.quit()
