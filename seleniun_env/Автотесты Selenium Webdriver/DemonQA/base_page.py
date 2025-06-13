from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        # Инициализация драйвера из фикстуры
        self.driver = driver

    def open(self, url):
        # Открываем страницу
        self.driver.get(url)

    def click(self, locator):
        # Кликаем на элементы. Локатор в файле locators
        self.driver.find_element(locator).click()

    def send_keys(self, locator, text):
        # Отправляем данные в поле
        self.driver.find_element(locator).send_keys(text)

    def current_url(self):
        # Получить ссылку
         return self.driver.current_url

    

    

    