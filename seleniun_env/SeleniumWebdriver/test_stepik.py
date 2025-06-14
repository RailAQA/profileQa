from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time
import pytest

@pytest.mark.smoke
def test_check(driver):
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    driver.find_element(By.ID, 'book').click()
    driver.find_element(By.ID, 'answer').send_keys(log(abs(12 * sin(int(driver.find_element(By.ID, 'input_value').text)))))
    driver.find_element(By.ID, 'solve').click()



# https://stepik.org/lesson/237240/step/4?unit=209628
@pytest.mark.lessons
class Test_To_DO:
###Тесты которые нужно доделать###
    def test_autorization_stepik(self, driver):
        driver.get("https://stepik.org/lesson/236895/step/1")
        WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="ember520"]/span/p'), 'test input'))
        login_button = driver.find_element(By.CLASS_NAME, 'navbar__auth').click()
        driver.find_element(By.NAME, 'login').send_keys("login")
        driver.find_element(By.NAME, 'password').send_keys('password')
        driver.find_element(By.CLASS_NAME, 'sign-form__btn').click()
        WebDriverWait(driver, 20).until(EC.element_attribute_to_include((By.CLASS_NAME, 'submit-submission'), 'disabled'))
        #assert driver.find_element(By.CSS_SELECTOR, '[data-ember-action-508="508"]').text == 'Оставить комментарий', "Логин не произошел"

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1', 'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
    def test_stepik(self, driver, link):
        driver.get(link)
        WebDriverWait(driver, 20).until(EC.element_attribute_to_include((By.CLASS_NAME, 'submit-submission'), 'disabled'))
        answer = log(int(time.time()))
        driver.find_element(By.CLASS_NAME, 'string-quiz__textarea').send_keys(answer)
        driver.find_element(By.CLASS_NAME, 'submit-submission').click()
        time.sleep(5)
        