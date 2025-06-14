# Задание - https://stepik.org/lesson/228249/step/6?unit=200781

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import *

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

# Подсчет формулы
def otvet():
    x = browser.find_element(By.ID, 'input_value').text
    return str(log(abs(12 * sin(int(x)))))

# Чекбокс
browser.find_element(By.ID, 'answer').send_keys(otvet())
browser.find_element(By.ID, 'robotCheckbox').click()

#Скрипт на скролл
radio = browser.find_element(By.ID, 'robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
radio.click()
browser.find_element(By.CLASS_NAME, 'btn').click()

sleep(4)
browser.quit()