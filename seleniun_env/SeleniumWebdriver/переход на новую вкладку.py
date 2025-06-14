# Задание: https://stepik.org/lesson/184253/step/6?unit=158843

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import *

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

sleep(2) # Чтобы кнопка была в видимой часи
browser.find_element(By.CLASS_NAME, 'trollface').click()

# Переключаемся в новое окно
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def otvet():
    return log(abs(12 * sin(int(browser.find_element(By.ID, 'input_value').text))))

browser.find_element(By.ID, 'answer').send_keys(otvet())

browser.find_element(By.CLASS_NAME, 'btn').click()
sleep(5)

browser.quit()
