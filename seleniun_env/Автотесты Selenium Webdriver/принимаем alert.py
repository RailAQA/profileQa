#Задача https://stepik.org/lesson/184253/step/4?unit=158843

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import *

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element(By.CLASS_NAME, 'btn').click()

# Принимаем алерт
alert = browser.switch_to.alert
alert.accept()

# Считаем выражение
def otvet():    
    x = browser.find_element(By.ID, 'input_value').text
    return log(abs(12 * sin(int(x))))

browser.find_element(By.ID, 'answer').send_keys(otvet())
browser.find_element(By.CLASS_NAME, 'btn').click()

sleep(5)
browser.quit()

