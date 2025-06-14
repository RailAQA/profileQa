#Задача https://stepik.org/lesson/165493/step/8?unit=140087

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

#Запуск Хрума и открытие нужной страницы
browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')

#Подсчет выражения
def otvet():
    num_1 = browser.find_element(By.ID, 'num1').text
    num_2 = browser.find_element(By.ID, "num2").text
    return str(int(num_1) + int(num_2))

#работа со с выпадающим списком
select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
select.select_by_value(otvet())

button = browser.find_element(By.CLASS_NAME, 'btn').click()
sleep(5)

browser.quit()
