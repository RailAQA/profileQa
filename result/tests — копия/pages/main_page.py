from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

locators = MainPageLocators()

class MainPage(BasePage):
    """Класс содержащий методы для страницы main_page."""
    random_carousel_1 = None


    def first_click_next_button(self):
        """Первый клик по кнопке NEXT."""
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        # Ожидания, чтобы анимация переключения карусели сработало
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_6, 10)
        # Проверка, что контент изменился
        self.elements_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL[0:3], 20)
        self.elements_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL[7:26], 20)
        assert '1' in self.find(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_1).get_attribute('data-testid'), f"ERROR [MainPage] Карусель 'По вашим предпочтениям' - отсутствует аттрибут - '1'. Фактический результат = {self.find(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_1).get_attribute('data-testid')}"
        # Проверяем, что кнопка "Back" видимая и кликабельная
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON, 20)
    
    def click_back_button_to_1(self):
        """Клик по кнопке BACK с переходом в 1-е состояние."""
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_1, 20)
        # Проверяем, что карусель переключилась в 1-е состояние
        self.carousel_back_button_is_not_visible()
        assert '0' in self.find(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_1).get_attribute('data-testid'), f"ERROR [MainPage] Карусель 'По вашим предпочтениям' - отсутствует аттрибут - '0'. Фактический результат = {self.find(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_1).get_attribute('data-testid')}"

    def carousel_back_button_is_not_visible(self):
        assert self.find(locators.YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON).get_attribute("class") == "carousel-module-scss-module__A4KUIq__hidden carousel-module-scss-module__A4KUIq__button", f'ERROR [MainPage] Карусель "По вашим предпочтениям" - у кнопки "Back" отсутствует аттрибут - "carousel-module-scss-module__A4KUIq__hidden carousel-module-scss-module__A4KUIq__button". Фактический результат = {self.find(locators.YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON).get_attribute("class")}'
        assert not self.find(locators.YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON).is_displayed(), 'ERROR [MainPage] Карусель "По вашим предпочтениям" - кнопка "Back" видимая'

    def click_to_anime_carousel_1(self):
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_5_click).click()
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_5_click, 5)
        self.element_is_clickable(self.locators_header.USER_ICON, 15)
        assert self.driver.current_url != "http://localhost:3001/home", f'ERROR [MainPage] Карусель "По вашим предпочтениям" - После нажатия на слайд аниме не произошел переход в аниме'

    def next_button_is_invisible_7(self):
        """Кликаем 7 раз на кнопку 'Next'."""
        # можно сделать через цикл
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_5, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_1, 5)
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_8, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_5, 5)
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_11, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_8, 5)
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_14, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_11, 5)
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_17, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_14, 5)
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_20, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_17, 5)
        self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_clickable(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_23, 5)
        self.element_is_not_visible(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_20, 5)
        # Проверяем что кнопка "Next" невидимая и "Back" активна
        assert self.find(locators.YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON).get_attribute('disabled') == 'true', f"ERROR [MainPage] Карусель 'По вашим предпочтениям' - кнопка 'NEXT' активная"
        assert self.find(locators.YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON).is_displayed(), f"ERROR [MainPage] Карусель 'По вашим предпочтениям' - кнопка 'BACK' неактивная"
        
        """Методы для карусели 'Сейчас в тренде'."""

    def scroll_to_carousel_2(self):
        """Подскролл к карусели"""
        element = self.find(locators.NOW_IN_TREND_CONTAINER)
        self.go_to_element(element)

    def nowintrend_back_button_is_invisible(self):
        """Проверяем, что кнопка 'Back' в карусели 'Сейчас в тренде' по дефолту невидимая."""
        assert self.find(locators.NOW_IN_TREND_BACK_BUTTON).get_attribute('disabled') == 'true', f'Error [MainPage] Карусель "Сейчас в тренде" - у кнопки отсутствует аттрибут - "disabled"'
        assert not self.find(locators.NOW_IN_TREND_BACK_BUTTON).is_displayed(), f'Error [MainPage] Карусель "Сейчас в тренде" - кнопка "Back" видимая'

    def first_click_next_button_nowintrend(self):
        """Первый клик по кнопке NEXT карусели 'Сейчас в тренде'."""
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        # Ожидания, чтобы анимация переключения карусели сработало
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_6, 10)
        # Проверка, что контент изменился
        self.elements_is_not_visible(locators.NOW_IN_TREND_ALL_SLIDES[0:3], 10)
        self.elements_is_not_visible(locators.NOW_IN_TREND_ALL_SLIDES[7:26], 10)
        assert '1' in self.find(locators.NOW_IN_TREND_CAROUSEL_SLIDE_1).get_attribute('data-testid'), f"Error [MainPage] Карусель 'Сейчас в тренде' - у элемента отсутствует аттрибут - '1'. Фактический результат - {self.find(locators.NOW_IN_TREND_CAROUSEL_SLIDE_1).get_attribute('data-testid')}"
        self.nowintrend_back_button_is_visible()

    def nowintrend_back_button_is_visible(self):
        """Провереяем, что кнопка 'Back' кликабельная и видимая"""
        #assert self.find(locators.NOW_IN_TREND_BACK_BUTTON).get_attribute('disabled') == 'false', f'Error [MainPage] - у кнопки есть аттрибут - "disabled"' Cережа сказал так должно быть
        
        # Можно через assert, но сделал через явное ожидание.
        #assert self.find(locators.NOW_IN_TREND_BACK_BUTTON).is_displayed(), f'Error [MainPage] - кнопка "Back" невидимая'
        self.element_is_clickable(locators.NOW_IN_TREND_BACK_BUTTON, 5)

    def click_back_button_to_1_nowintrend(self):
        """Клик по кнопке BACK с переходом в 1-е состояние."""
        self.find(locators.NOW_IN_TREND_BACK_BUTTON).click()
        # Явное ожидание переключения на 1 состояние
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_1, 5)
        assert '0' in self.find(locators.NOW_IN_TREND_CAROUSEL_SLIDE_1).get_attribute('data-testid'), f"Error [MainPage] Карусель 'Сейчас в тренде' - у элемента отсутствует аттрибут - '0'. Фактический результат - {self.find(locators.NOW_IN_TREND_CAROUSEL_SLIDE_1).get_attribute('data-testid')}"
        self.nowintrend_back_button_is_invisible()

    def click_to_anime_carousel_in_nowintrend(self):
        """В каруселе 'Сейчас в тренде' кликаем на на 5-е аниме"""
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_6, 15)
        self.find(locators.NOW_IN_TREND_CAROUSEL_SLIDE_6).click()
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_6, 20)
        self.element_is_clickable(self.locators_header.USER_ICON, 25)
        assert self.driver.current_url != "http://localhost:3001/home", f'ERROR [MainPage] Карусель "Сейчас в тренде" - После нажатия на слайд аниме не произошел переход в аниме'

    def next_button_is_invisible_7_nowintrend(self):
        """Кликаем 7 раз на кнопку 'Next' + проверка что кнопка некст невидимая."""
        # можно сделать через цикл
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_5, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_1, 10)
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_8, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_5, 10)
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_11, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_8, 10)
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_14, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_11, 10)
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_17, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_14, 10)
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_20, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_17, 10)
        self.find(locators.NOW_IN_TREND_NEXT_BUTTON).click()
        self.element_is_clickable(locators.NOW_IN_TREND_CAROUSEL_SLIDE_23, 10)
        self.element_is_not_visible(locators.NOW_IN_TREND_CAROUSEL_SLIDE_20, 10)
        # Проверяем что кнопка "Next" невидимая и "Back" активна
        assert self.find(locators.NOW_IN_TREND_NEXT_BUTTON).get_attribute('disabled') == 'true', f"ERROR [MainPage] Карусель 'Сейчас в тренде' - кнопка 'NEXT' активная"
        assert self.find(locators.NOW_IN_TREND_BACK_BUTTON).is_displayed(), f"ERROR [MainPage] Карусель 'Сейчас в тренде' - кнопка 'BACK' неактивная"

    """Рекламный блок"""
    def scroll_to_add_block(self):
        """Подскролл к рекламному блоку"""
        element = self.find(locators.BANNER_MAIN_SLIDE_CONTAINER)
        self.go_to_element(element)

    def add_block_check_in_page(self):
        """Проверяем, что рекламный блок есть на странице"""
        #self.elements_are_visible(locators.BANNER_MAIN_SLIDE_ALL, 5) Будет ошибка пока у баннеров не будет картинок
        self.elements_are_visible(locators.PAGINATION_BANNER_MAIN_BUTTON_ALL, 5)

    def add_block_pagination1_click(self):
        """Клик на 1-ю пагинаю рекламного блока"""
        self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_1).click()
        # Явное ожидание перелистывания
        self.element_is_visible(locators.BANNER_MAIN_SLIDE_1, 5)
        self.add_block_1slide_check()
            
    def add_block_1slide_check(self):
        """Проверяем, что мы находимся в 1-м слайде"""
        assert "transform: translateX(calc(0% + 0px));" in self.find(locators.BANNER_MAIN_SLIDE_1).get_attribute('style'), f'Error [MainPage] адд блок не переключился на 1-й слайд'
        assert self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_1).get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button', f'Error [MainPage] ошибка у пагинации'
        # Проверка пагниция 2-4. что они не активны
        for i in range(1,4):
            assert self.finds(locators.PAGINATION_BANNER_MAIN_BUTTON_ALL)[i].get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button banners-showing-module-scss-module__cgoiWq__button-unfocused', f'Error [MainPage] Ошибка в пагниации {i}'

    def add_block_pagination2_click(self):
        """Клик на 2-ю пагинаю рекламного блока"""
        self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_2).click()
        # Явное ожидание перелистывания
        self.element_is_visible(locators.BANNER_MAIN_SLIDE_2, 5)
        self.add_block_2slide_check()
     
    def add_block_2slide_check(self):
        """Проверяем, что мы находимся в 2-м слайде"""
        assert "transform: translateX(calc(-100% - 20px));" in self.find(locators.BANNER_MAIN_SLIDE_2).get_attribute('style'), f'Error [MainPage] адд блок не переключился на 2-й слайд'
        assert self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_2).get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button', f'Error [MainPage] ошибка у пагинации'
        # Проверка пагниция 1,3-4 что они не активны
        for i in range(0,4):
            if i == 1:
                continue
            assert self.finds(locators.PAGINATION_BANNER_MAIN_BUTTON_ALL)[i].get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button banners-showing-module-scss-module__cgoiWq__button-unfocused', f'Error [MainPage] Ошибка в пагниации {i}'

    def add_block_pagination3_click(self):
        """Клик на 3-ю пагинаю рекламного блока"""
        self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_3).click()
        # Явное ожидание перелистывания
        self.element_is_visible(locators.BANNER_MAIN_SLIDE_3, 5)
        self.add_block_3slide_check()
     
    def add_block_3slide_check(self):
        """Проверяем, что мы находимся в 3-м слайде"""
        assert "transform: translateX(calc(-200% - 40px));" in self.find(locators.BANNER_MAIN_SLIDE_3).get_attribute('style'), f'Error [MainPage] адд блок не переключился на 3-й слайд'
        assert self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_3).get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button', f'Error [MainPage] ошибка у пагинации'
        # Проверка пагниция 1-2,4 что они не активны
        for i in range(0,4):
            if i == 2:
                continue
            assert self.finds(locators.PAGINATION_BANNER_MAIN_BUTTON_ALL)[i].get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button banners-showing-module-scss-module__cgoiWq__button-unfocused', f'Error [MainPage] Ошибка в пагниации {i}'

    def add_block_pagination4_click(self):
        """Клик на 4-ю пагинаю рекламного блока"""
        self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_4).click()
        # Явное ожидание перелистывания
        self.element_is_visible(locators.BANNER_MAIN_SLIDE_4, 15)
        self.add_block_4slide_check()
     
    def add_block_4slide_check(self):
        """Проверяем, что мы находимся в 4-м слайде"""
        assert "transform: translateX(calc(-300% - 60px));" in self.find(locators.BANNER_MAIN_SLIDE_4).get_attribute('style'), f'Error [MainPage] адд блок не переключился на 4-й слайд'
        assert self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_4).get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button', f'Error [MainPage] ошибка у пагинации'
        # Проверка пагниция 1-3 что они не активны
        for i in range(0,3):
            assert self.finds(locators.PAGINATION_BANNER_MAIN_BUTTON_ALL)[i].get_attribute('class') == 'banners-showing-module-scss-module__cgoiWq__button banners-showing-module-scss-module__cgoiWq__button-unfocused', f'Error [MainPage] Ошибка в пагниации {i}'

    def add_block_pagination1_click_repeat(self):
         """Повторный клик на 1-ю пагинацию"""
         self.find(locators.PAGINATION_BANNER_MAIN_BUTTON_1).click()
         self.element_is_visible(locators.BANNER_MAIN_SLIDE_1, 15)
         self.add_block_1slide_check()

    def scroll_to_newanime_block(self):
        """Подскролл к блоку 'Новинки'"""
        element = self.find(locators.NEW_ANIME_CONTAINER)
        self.go_to_element(element)

    def newanime_block_check_in_page(self):
        """Проверяем, что "Новые аниме" блок есть на странице"""
        self.elements_are_visible(locators.NEW_ANIME_BLOCK_SLIDE_ALL, 5)

    def newanime_block_random_slide_click(self):
        """Кликаем на аниме в блоке 'Новинки'"""
        self.find(locators.NEW_ANIME_BLOCK_SLIDE_5).click()
        self.element_is_present(locators.NEW_ANIME_BLOCK_SLIDE_5, 5)
        self.element_is_clickable(self.locators_header.USER_ICON, 15)
        assert 'http://localhost:3001' + self.find(locators.NEW_ANIME_BLOCK_SLIDE_5).get_attribute('href') != 'http://localhost:3001/home', f'Error [MainPage] NEW_ANIME_BLOCK - Открывается главная страница после клика на аниме'

    def newanime_block_more_button_click(self):
        self.find(locators.NEW_ANIME_MORE_BUTTON).click()
        assert len(self.finds(locators.NEW_ANIME_BLOCK_SLIDE_ALL)) == 26, f'Error [MainPage] NEW_ANIME_BLOCK - Не работает кнопка "Показать все"'

    def stop_carousel(self):
        """Простое отключение анимации карусели"""
        self.driver.execute_script("""
    // 1. Отключаем все переходы у изображений
    document.querySelectorAll('.banners-showing-module-scss-module__cgoiWq__image').forEach(img => {
        img.style.transition = 'none';
    });
    
    // 2. Останавливаем все интервалы (самое важное!)
    for (let i = 1; i < 9999; i++) clearInterval(i);
    """)
    

    # # # Мобилка # # #

    def scroll_to_carousel_1(self):
        self.go_to_element_center(element=self.find(locators.YOUR_PREFERENCES_CONTAINER))
        assert self.finds(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL)[0-2].is_displayed(), f'[ERROR] MainPage после скрола к 1-й карусели не видны слайды 1 и 2.'

    def swipe_carousel_1(self):
        self.random_carousel_1 = self.random_number(4, 26)
        self.go_to_element(element=self.finds(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL)[self.random_carousel_1])
        assert self.finds(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL)[self.random_carousel_1].is_displayed(), f'[ERROR] MainPage карусель "По вашим предпочтениям" после скролла к слайду {self.random_carousel_1} не виден.'

    def scroll_to_carousel_2_mobile(self):
        self.go_to_element_center(element=self.find(locators.NOW_IN_TREND_CONTAINER))
        assert self.finds(locators.NOW_IN_TREND_ALL_SLIDES)[0-2].is_displayed(), f'[ERROR] MainPage после скрола к 2-й карусели не видны слайды 1 и 2.'

    def swipe_carousel_2(self):
        self.random_carousel_2 = self.random_number(4, 26)
        self.go_to_element(element=self.finds(locators.YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL)[self.random_carousel_2])
        assert self.finds(locators.NOW_IN_TREND_ALL_SLIDES)[self.random_carousel_2].is_displayed(), f'[ERROR] MainPage карусель "Сейчас в тренде" после скролла к слайду {self.random_carousel_2} не виден.'

    def scroll_to_more_button(self):
        self.go_to_element_center(element=self.find(locators.NEW_ANIME_MORE_BUTTON))
        self.element_is_clickable(locators.NEW_ANIME_MORE_BUTTON, 20)