from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_element_locators import HeaderElementLocators
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, TimeoutException)
import random
import allure


class BasePage:
    """Базовый класс для страниц, содержащий общие методы."""
    locators_header = HeaderElementLocators()
    locators_main_page = MainPageLocators()

    def __init__(self, driver):
        """Инициализирует страницу с драйвером Selenium"""
        self.driver = driver

    def open(self, url):
        """Открывает страницу с заданным URL."""
        with allure.step("Открыть страницу"):
            self.driver.get(url)

        # Проверка для главной страницы, что 1-я карусель загрузилась.
        if url == 'http://localhost:3001/home':
            try:
                self.element_is_clickable(self.locators_main_page.YOUR_PREFERENCES_CAROUSEL_SLIDE_2, 30)
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - карусель 'По вашим предпочтениям' не прогрузилась. Метод 'open()'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - карусель 'По вашим предпочтениям' не прогрузилась. Метод 'open()'.")
            
        try:
            self.element_is_clickable(self.locators_header.USER_ICON, 30)
        except TimeoutError:
            raise AssertionError(f"ERROR [Base_Page] - Страница не прогружена. Метод 'open()'.")
        except TimeoutException:
            raise AssertionError(f"ERROR [Base_Page] - Страница не прогружена или нету элемента {self.locators_header.USER_ICON}. Метод 'open()'.")    
            
    def open_mobile(self, url):
        """Открывает страницу с заданным URL (мобильная версия)"""
        with allure.step("Открыть страницу (мобильная версия)"):
            self.driver.get(url)

        if url == 'http://localhost:3001/home':
            try:
                self.element_is_clickable(self.locators_main_page.YOUR_PREFERENCES_CAROUSEL_SLIDE_1, 20)
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - карусель 'По вашим предпочтениям' не прогрузилась. Метод 'open_mobile()'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - карусель 'По вашим предпочтениям' не прогрузилась. Метод 'open_mobile()'.")
        

    def element_is_visible(self, args, timeout):
        """Ожидает, пока элемент станет видимым, и возвращает его."""
        with allure.step("Ожидание пока элемент будет виден"):
            try:
                return wait(self.driver, timeout).until(EC.visibility_of_element_located(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} невидим на странице. Метод 'element_is_visible'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} невидим на странице, либо его нет. Метод 'element_is_visible'.")


    def elements_are_visible(self, args, timeout):
        """Ожидает, пока все элементы станут видимыми, и возвращает их список."""
        with allure.step("Ожидание пока элементы будут видны"):
            try:
                wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} невидимый на странице. Метод 'elements_are_visible'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} невидимый на странице, либо его нет. Метод 'elements_are_visible'.")


    def element_is_present(self, args, timeout=5):
        """Ожидает, пока элемент появится в DOM, и возвращает его."""
        with allure.step("Ожидание пока элемент появится в DOM"):
            try:
                return wait(self.driver, timeout).until(EC.presence_of_element_located(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не появился в DOM. Метод 'element_is_present'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не появился в DOM. Метод 'element_is_present'.")


    def elements_are_present(self, args, timeout):
        """Ожидает, пока все элементы появятся в DOM, и возвращает их список."""
        with allure.step("Ожидание пока элементы появятся в DOM"):
            try:
                return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не появились в DOM. Метод 'elements_are_present'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не появились в DOM. Метод 'elements_are_present'.")


    def element_is_not_visible(self, args, timeout=5):
        """Ожидает, пока элемент станет невидимым."""
        with allure.step("Ожидание пока элемент станет невидимым"):
            try:
                return wait(self.driver, timeout).until(EC.invisibility_of_element_located(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не стал невидимым. Метод 'element_is_not_visible'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не стал невидимым. Метод 'element_is_not_visible'.")
    
    def elements_is_not_visible(self, args, timeout):
        """Ожидает, пока элемент станет невидимым."""
        with allure.step("Ожидание пока элементы станут невидимыми"):
            try:
                return wait(self.driver, timeout).until_not(EC.visibility_of_all_elements_located(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элементы {args} видны на странице. Метод 'elements_is_not_visible'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элементы {args} видны на странице. Метод 'elements_is_not_visible'.")


    def element_is_clickable(self, args, timeout):
        """Ожидает, пока элемент станет кликабельным, и возвращает его."""
        with allure.step("Ожидание пока элемент станет кликабельным"):
            try:
                return wait(self.driver, timeout).until(EC.element_to_be_clickable(args))
            except TimeoutError:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не кликабельный или его нет на странице. Метод 'element_is_clickable'.")
            except TimeoutException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не кликабельный или его нет на странице. Метод 'element_is_clickable'.")
            except NoSuchElementException:
                raise AssertionError(f"ERROR [Base_Page] - Элемент {args} не существует в DOM. Метод 'element_is_clickable'.")
            except ElementNotInteractableException:
                raise AssertionError(f"Элемент {args} есть, но с ним нельзя взаимодействовать")
        

    def go_to_element(self, element):
        """Прокручивает страницу к указанному элементу."""
        with allure.step("Скролл к элементу"):
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    def go_to_element_center(self, element):
        """Прокручивает страницу к указанному элементу, но чтобы элемент был посередине."""
        with allure.step("Скролл к элементу"):
            self.driver.execute_script("return arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", element)

    def find(self, args):
        try:
            return self.driver.find_element(*args)
        except NoSuchElementException:
            raise AssertionError(f"Элемент {args} не существует в DOM")
        except StaleElementReferenceException:
            raise AssertionError(f"Элемент {args} стал устаревшим (Stale)")
        except Exception as e:
            raise Exception(f"Неожиданная ошибка при поиске элемента {args}: {str(e)}") 

    def finds(self, args):
        try:
            return self.driver.find_elements(*args)
        except NoSuchElementException:
            raise AssertionError(f"Элемент {args} не существует в DOM")
        except StaleElementReferenceException:
            raise AssertionError(f"Элемент {args} стал устаревшим (Stale)")
        except Exception as e:
            raise Exception(f"Неожиданная ошибка при поиске элемента {args}: {str(e)}") 

    def random_number(self, a, b):
        return random.randrange(a, b)