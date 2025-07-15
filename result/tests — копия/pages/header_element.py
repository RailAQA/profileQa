from pages.base_page import BasePage
from locators.header_element_locators import HeaderElementLocators

locators = HeaderElementLocators()

class HeaderElement(BasePage):
    """Класс содержащий методы для хедера"""

    def search_check(self):
        """Проверяем, что поиск на месте"""
        self.element_is_clickable(locators.SEARCH_INPUT, 15)
        assert self.find(locators.SEARCH_INPUT).get_attribute('placeholder') == 'Найти...', f"Error [HEADER_ELEMENTS] Неверный плейсхолдер, фактический результат {self.find(locators.SEARCH_INPUT).get_attribute('placeholder')}" 
        
    def search_click(self):
        """Кликаем на поиск + проверки"""
        self.find(locators.SEARCH_INPUT).click()
        self.element_is_not_visible(locators.SEARCH_ICON, 20)
        assert self.find(locators.SEARCH_INPUT).get_attribute('placeholder') != 'Найти...', 'Error [HEADER_ELEMENTS] После клика на поиск не пропал плейсхолдер'

    def search_anime(self, promt):
        """Вводим поисковый запрос в поиск + проверки"""
        self.find(locators.SEARCH_INPUT).send_keys(promt)
        self.element_is_visible(locators.LOADER, 20)
        self.element_is_not_visible(locators.LOADER, 20)
        self.element_is_visible(locators.SEARCH_RESULTS_CONTAINER, 25)

    def search_results_anime_click(self):
        self.finds(locators.SEARCH_RESULTS_ANIME)[1].click()
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CONTAINER, 30)
        assert not self.find(locators.SEARCH_RESULTS_CONTAINER).is_displayed(), 'Error [HEADER_ELEMENTS] После перехода на страницу аниме не пропадает контейнер search results'
        assert self.driver.current_url != 'http://localhost:3001/home'
    
    def click_to_random(self):
        self.find(locators.NOW_IN_TREND_CONTAINER).click()
        self.element_is_not_visible(locators.SEARCH_RESULTS_CONTAINER, 25)
        assert not self.find(locators.SEARCH_RESULTS_CONTAINER).is_displayed(), 'Error [HEADER_ELEMENTS] После клика на любое метсо на странице не пропадает всплывающий результат'


                                # # # Мобильная версия смоки # # #

    def burger_is_visible(self):
        self.element_is_clickable(locators.BURGER_MENU_BUTTON, 20)

    def search_input_is_visible(self):
        self.element_is_clickable(locators.SEARCH_INPUT_MOB, 20)