from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        # Инициализация драйвера из фикстуры
        self.driver = driver

    def current_url(self):
        # Получить ссылку страницы
         return self.driver.current_url
    
    def find(self, args):
        return self.driver.find_element(*args)
    
    def scroll_to_element(self, args):
        self.driver.execute_script('return arguments[0].ScrollIntoView(true);', *args)
     
    


    

    

    