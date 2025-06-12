# Задача: https://stepik.org/lesson/181384/step/8?unit=156009

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
from time import sleep

def test_check(driver):
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    driver.find_element(By.ID, 'answer').send_keys(log(abs(12 * sin(int(driver.find_element(By.ID, 'input_value').text)))))
    driver.find_element(By.ID, 'solve').click()
    sleep(5)