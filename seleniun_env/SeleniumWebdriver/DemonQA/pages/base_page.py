from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        # Инициализация драйвера из фикстуры
        self.driver = driver

    def current_url(self):
        # Получить ссылку страницы
         return self.driver.current_url

    def open(self, url):
        # Открыть страницу по ссылке (url)
        self.driver.get(url)
        # Проверка, что ссылка открывается, прогружается через 15 сек
        try:
            self.wait(15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[src="/images/Toolsqa.jpg"]')))
        except TimeoutError:
            raise AssertionError(f"[Base_Page] - Страница не открылась. Шапка сайта не отобразилась")
        # Проверяем, что открылась правильная ссылка
        assert url == self.current_url() or url[8:] == self.current_url(), f'Ошибка в [BasePage] - Ожидаемая ссылка {url} не совпадает с фактической ссылкой {self.current_url()}'
        
    def current_url(self):
        # Получить ссылку страницы
         return self.driver.current_url
    
    def find(self, args):
        # Ищем элемент по локатору + проверка что элемент есть на странице
        assert self.driver.find_element(*args).is_displayed(), '[BasePage] - Элемент отсутствует на страницу! или неправильный локатор!'
        return self.driver.find_element(*args)
        
    def scroll_to_element(self, args):
        self.driver.execute_script('return arguments[0].ScrollIntoView(true);', *args)

    def wait(self, timeout):
        # Часть ф-ии явного ожидания WebDriverWait(driver, время)
        return WebDriverWait(self.driver, timeout)
        
     
    


    

    

    