#Задача https://stepik.org/lesson/165493/step/7?unit=140087

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import *

# Открываем Хрум и нужную страницу
browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/get_attribute.html')

#ищем нужный элемент
sunduk = browser.find_element(By.ID, 'treasure')
m = sunduk.get_attribute('valuex')
a = int(m)

#подсчет выражения
def otvet():
    return log(abs(12 * sin(a)))

# Ввод в поле ответа выражения и клики на чекбокс и радиокнопку
vvod = browser.find_element(By.ID, "answer").send_keys(otvet())
checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
radiobutton = browser.find_element(By.ID, 'robotsRule').click()
button = browser.find_element(By.CLASS_NAME, 'btn').click()

sleep(5)
browser.quit()
