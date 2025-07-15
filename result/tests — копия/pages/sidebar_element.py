from pages.base_page import BasePage
from locators.sidebar_element_locators import SideBarElementLocators
from locators.main_page_locators import MainPageLocators
from locators.header_element_locators import HeaderElementLocators
from time import sleep

locators = SideBarElementLocators()
locators_mainpage = MainPageLocators()
locators_header = HeaderElementLocators()

class SideBar(BasePage):
    """Класс содержащий методы для бокового меню"""

    def sidebar_elements_check(self):
        """Проверяем, что элементы сайдбара видны и кликабельны"""
        self.element_is_visible(locators.LOGO_SIDEBAR, 5)
        self.element_is_visible(locators.HOME_BUTTON, 5)
        self.element_is_clickable(locators.CATALOG_BUTTON, 5)
        self.element_is_clickable(locators.FAVOURITE_BUTTON, 5)
        self.element_is_clickable(locators.COLLECTIONS_BUTTON, 5)

    def sidebar_logo_click(self):
        """Кликакем на лого + ожидание, что страница загрузилась"""
        self.find(locators.LOGO_SIDEBAR).click()
        self.element_is_not_visible(locators.BANNER_FROM_ANIME_PAGE, 15)
        assert self.driver.current_url == 'http://localhost:3001/home', f'Error [SideBar] - После нажатия на лого открылась не главная страница, а - {self.driver.current_url}'

    def catalog_button_click(self):
        """Кликакем на гиперссылку 'Каталог'."""
        self.find(locators.CATALOG_BUTTON).click()
        self.element_is_not_visible(locators_mainpage.YOUR_PREFERENCES_CONTAINER, 30)
        assert self.driver.current_url == 'http://localhost:3001/catalog', f'Error [SideBar] - После нажатия на лого открылась не страница каталога, а - {self.driver.current_url}'

    def favourite_button_click(self):
        """Кликакем на гиперссылку 'Избранное'."""
        self.find(locators.FAVOURITE_BUTTON).click()
        self.element_is_not_visible(locators_mainpage.YOUR_PREFERENCES_CONTAINER, 30)
        assert self.driver.current_url == 'http://localhost:3001/favourite', f'Error [SideBar] - После нажатия на лого открылась не страница избранное, а - {self.driver.current_url}'

    def collection_button_click(self):
        """Кликакем на гиперссылку 'Коллекция'."""
        self.find(locators.COLLECTIONS_BUTTON).click()
        self.element_is_not_visible(locators_mainpage.YOUR_PREFERENCES_CONTAINER, 30)
        assert self.driver.current_url == 'http://localhost:3001/collections', f'Error [SideBar] - После нажатия на лого открылась не страница коллекция, а - {self.driver.current_url}'



                                    # # # Мобилка # # #

    def click_to_burger_menu(self):
        self.find(locators_header.BURGER_MENU_BUTTON).click()
        self.element_is_visible(locators.BURGER_MENU_CONTAINER, 20)

    def close_burger_menu(self):
        self.find(locators.CLOSE_BUTTON_BURGER_MENU).click()
        self.element_is_not_visible(locators.BURGER_MENU_CONTAINER, 20)
        self.element_is_visible(locators_mainpage.YOUR_PREFERENCES_CAROUSEL_SLIDE_1, 20)

    
