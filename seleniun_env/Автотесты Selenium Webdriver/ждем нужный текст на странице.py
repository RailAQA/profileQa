# Задача: https://stepik.org/lesson/181384/step/8?unit=156009

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
from time import sleep

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
browser.find_element(By.ID, 'book').click()

def otvet():
    return log(abs(12 * sin(int(browser.find_element(By.ID, 'input_value').text))))

browser.find_element(By.ID, 'answer').send_keys(otvet())
browser.find_element(By.ID, 'solve').click()
sleep(5)