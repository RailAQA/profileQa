from pages.base_page import BasePage
from locators.anime_page_locators import AnimePageLocators
from time import sleep
locators = AnimePageLocators()

class AnimePage(BasePage):
    random_carousel_similar = None

    def click_watch_button(self):
        """Клик на кнопку 'Посмотреть' + ожидания"""
        self.find(locators.WATCH_BUTTON).click()
        self.element_is_not_visible(locators.WATCH_BUTTON, 10)
        self.element_is_clickable(locators.LOGO_USER, 15)
        # нужен ассерт на ссылку

    def click_trailer_button(self):
        """Клик на кнопку 'Посмотреть' + ожидания"""
        self.find(locators.TRAILER_BUTTON).click()
        self.element_is_not_visible(locators.TRAILER_BUTTON, 10)
        self.element_is_clickable(locators.LOGO_USER, 15)
        # нужен ассерт на ссылку

    def click_to_list(self):
        """Клик на список + проверки всех кнопок"""
        self.find(locators.ADD_TO_COLLECTION_LIST_BUTTON).click()
        self.element_is_visible(locators.LIST_ALL_BUTTONS_CONTAINER, 20)
        self.scroll_to_list_container()
        buttons = self.elements_are_present(locators.LIST_ALL_BUTTONS_CONTAINER, 20)
        for _ in range(3):
            texts = {b.text.strip() for b in buttons}
        if all(texts):  # Проверяем, что нет пустых строк
            return texts
        sleep(0.3)
        
    def scroll_to_list(self):
        self.element_is_visible(locators.ADD_TO_COLLECTION_LIST_BUTTON, 15)
        element = self.find(locators.ADD_TO_COLLECTION_LIST_BUTTON)
        self.go_to_element(element)

    def scroll_to_list_container(self):
        container = self.find(locators.LIST_ALL_BUTTONS_CONTAINER)
        self.driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});",
        container)
        sleep(0.5)

    def click_to_list_repeat(self):
        self.find(locators.ADD_TO_COLLECTION_LIST_BUTTON).click()
        self.element_is_visible(locators.LIST_ALL_BUTTONS_CONTAINER, 10)
        self.scroll_to_list_container()
        self.find(locators.ADD_TO_COLLECTION_LIST_BUTTON).click()
        self.element_is_not_visible(locators.LIST_ALL_BUTTONS_CONTAINER, 15)

    def scroll_to_section_buttons(self):
        element = self.find(locators.SECTION_BUTTONS_ALL)
        self.go_to_element(element)

    def review_button_is_default(self):
        assert 'choose-data-module-scss-module__Zk0ViW__choose-el choose-data-module-scss-module__Zk0ViW__focused' in self.find(locators.REVIEW_SECTION_BUTTON).get_attribute('class'), 'Error [AnimePage] Кнопка Обзор не активная'

    def related_button_click(self):
        self.find(locators.RELATED_SECTION_BUTTON).click()
        self.element_is_not_visible(locators.REVIEW_MODULE_CONTAINER, 15)
        self.element_is_visible(locators.RELATED_MODULE_CONTAINER, 10)
        assert 'choose-data-module-scss-module__Zk0ViW__choose-el choose-data-module-scss-module__Zk0ViW__focused' in self.find(locators.RELATED_SECTION_BUTTON).get_attribute('class'), 'Error [AnimePage] Кнопка Связанные не активная'

    def hero_button_click(self):
        self.find(locators.HERO_SECTION_BUTTON).click()
        self.element_is_not_visible(locators.REVIEW_MODULE_CONTAINER, 15)
        # Пока нету постеров ненадежно
        self.element_is_visible(locators.HERO_MODULE_CONTAINER, 12)
        #assert len(self.finds(locators.HERO_MODULE_CONTAINER_ELEMENTS)) == 6, 'ERROR [ANIMEPAGE] не открылся модуль персонажи'
        assert 'choose-data-module-scss-module__Zk0ViW__choose-el choose-data-module-scss-module__Zk0ViW__focused' in self.find(locators.HERO_SECTION_BUTTON).get_attribute('class'), 'Error [AnimePage] Кнопка Персонажи не активная'

    def authors_button_click(self):
        self.find(locators.AUTHOR_SECTION_BUTTON).click()
        self.element_is_not_visible(locators.REVIEW_MODULE_CONTAINER, 15)
        self.element_is_visible(locators.AUTHORS_MODULE_CONTAINER, 10)
        assert 'choose-data-module-scss-module__Zk0ViW__choose-el choose-data-module-scss-module__Zk0ViW__focused' in self.find(locators.AUTHOR_SECTION_BUTTON).get_attribute('class'), 'Error [AnimePage] Кнопка Авторы не активная'

    def feedback_button_click(self):
        self.find(locators.FEEDBACK_SECTION_BUTTON).click()
        self.element_is_not_visible(locators.REVIEW_MODULE_CONTAINER, 15)
        self.element_is_visible(locators.FEEBACK_MODULE_CONTAINER, 10)
        assert 'choose-data-module-scss-module__Zk0ViW__choose-el choose-data-module-scss-module__Zk0ViW__focused' in self.find(locators.FEEDBACK_SECTION_BUTTON).get_attribute('class'), 'Error [AnimePage] Кнопка Отзывы не активная'

    def click_to_write_feedback_button(self):
        self.find(locators.WRITE_FEEDBACK_BUTTON).click()
        self.element_is_visible(locators.FEEDBACK_POP_UP, 10)

    def stars_default_check(self):
        #popup = self.element_is_visible(locators.FEEDBACK_POP_UP, 10)
        self.element_is_visible(locators.STAR_CONTAINER, 10)
        assert len(self.finds(locators.STARS_ALL)) == 5, f'Error [AnimePage] на странице аниме не 5 звезд. Фактическое количество - {len(self.finds(locators.STARS_ALL))}'
        # Далее проверяем, что активна только 1 звезда. Остальные четыре не активны
        assert self.finds(locators.ALL_STARS_SVG)[0].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 1-я звезда не активная по дефолту'
        assert self.finds(locators.ALL_STARS_SVG)[1].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 2-я звезда активная по дефолту'
        assert self.finds(locators.ALL_STARS_SVG)[2].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 3-я звезда активная по дефолту'
        assert self.finds(locators.ALL_STARS_SVG)[3].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 4-я звезда активная по дефолту'
        assert self.finds(locators.ALL_STARS_SVG)[4].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 5-я звезда активная по дефолту'
        
    def click_to_2_star(self):
        self.finds(locators.ALL_STARS_SVG)[1].click()
        assert self.finds(locators.ALL_STARS_SVG)[0].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 1-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[1].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 2-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[2].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 3-я звезда активная'
        assert self.finds(locators.ALL_STARS_SVG)[3].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 4-я звезда активная'
        assert self.finds(locators.ALL_STARS_SVG)[4].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 5-я звезда активная'

    def click_to_3_star(self):
        self.finds(locators.ALL_STARS_SVG)[2].click()
        assert self.finds(locators.ALL_STARS_SVG)[0].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 1-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[1].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 2-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[2].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 3-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[3].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 4-я звезда активная'
        assert self.finds(locators.ALL_STARS_SVG)[4].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 5-я звезда активная'
    
    def click_to_4_star(self):
        self.finds(locators.ALL_STARS_SVG)[3].click()
        assert self.finds(locators.ALL_STARS_SVG)[0].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 1-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[1].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 2-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[2].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 3-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[3].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 4-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[4].get_attribute('class') == "fill-none stroke-orange", 'Error [AnimePage] 5-я звезда активная'

    def click_to_5_star(self):
        self.finds(locators.ALL_STARS_SVG)[4].click()
        assert self.finds(locators.ALL_STARS_SVG)[0].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 1-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[1].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 2-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[2].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 3-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[3].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 4-я звезда не активная'
        assert self.finds(locators.ALL_STARS_SVG)[4].get_attribute('class') == "fill-orange stroke-orange", 'Error [AnimePage] 5-я звезда не активная'

    def send_text(self, text):
        self.find(locators.TEXT_AREA).send_keys(text)
        # нужны проверки

    def checkbox_click(self):
        self.find(locators.CHECK_BOX).click()
        self.element_is_visible(locators.CHECK_BOX_OK, 5)
        #assert self.find(locators.CHECK_BOX).get_attribute('data-headlessui-state') == 'checked', f'Error [AnimePage] После нажатия на чекбокс не стал активным'

    def send_feedback(self):
        self.find(locators.SEND_BUTTON).click()
        self.element_is_not_visible(locators.FEEDBACK_POP_UP, 15)

    def close_pop_up(self):
        self.find(locators.CLOSE_BUTTON).click()
        self.element_is_not_visible(locators.FEEDBACK_POP_UP, 10)

    """Модуль обзор"""
    def scroll_to_carousel(self):
        element = self.find(locators.SIMILAR_CAROUSEL_CONTAINER)
        self.go_to_element_center(element)
        self.element_is_visible(locators.SIMILAR_CAROUSEL_CONTAINER, 20)

    def back_button_invisible_similar_carousel(self):
        self.element_is_not_visible(locators.SIMILAR_CAROUSEL_BACK_BUTTON, 20)
        assert self.find(locators.SIMILAR_CAROUSEL_BACK_BUTTON).get_attribute('disabled') == 'true', 'Error [AnimePage] - у кнопки "Back" отсутствует аттрибут "disabled"'

    def next_button_visible_similar_carousel(self):
        self.element_is_clickable(locators.SIMILAR_CAROUSEL_NEXT_BUTTON, 20)
        assert not self.find(locators.SIMILAR_CAROUSEL_NEXT_BUTTON).get_attribute('disabled'), f"Error [AnimePage] - В кнопке 'Next' есть аттрибут 'disabled'."

    def first_click_to_next_button(self):
        self.find(locators.SIMILAR_CAROUSEL_NEXT_BUTTON).click()
        self.element_is_visible(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_6, 20)
        self.element_is_not_visible(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_1, 20)
        assert '1' in self.find(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_1).get_attribute('data-testid'), f"Error [AnimePage] - у слайдов отсутствует data-testid = '1'. Фактический результат - {self.find(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_1).get_attribute('data-testid')}"

    def back_button_visible(self):
        self.element_is_visible(locators.SIMILAR_CAROUSEL_BACK_BUTTON, 20)
        assert not self.find(locators.SIMILAR_CAROUSEL_BACK_BUTTON).get_attribute('disabled'), f"Error [AnimePage] - В кнопке 'Back' есть аттрибут 'disabled'."

    def first_click_to_back_button(self):
        self.find(locators.SIMILAR_CAROUSEL_BACK_BUTTON).click()
        self.element_is_visible(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_2, 20)
        self.element_is_not_visible(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_6, 20)
        assert '0' in self.find(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_1).get_attribute('data-testid'), f"Error [AnimePage] - у слайдов отсутствует data-testid = '0'. Фактический результат - {self.find(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_1).get_attribute('data-testid')}"

    def next_button_click_to_end(self):
        while not '5.5' in self.find(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_1).get_attribute('data-testid'):
            self.find(locators.SIMILAR_CAROUSEL_NEXT_BUTTON).click()

        self.element_is_clickable(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_25, 20)

    def next_button_invisible(self):
        self.element_is_not_visible(locators.SIMILAR_CAROUSEL_NEXT_BUTTON, 20)
        assert self.find(locators.SIMILAR_CAROUSEL_NEXT_BUTTON).get_attribute('disabled') == 'true', 'Error [AnimePage] - у кнопки "Next" отсутствует аттрибут "disabled"'

    def click_to_3_slide(self):
        self.first_click_to_next_button()
        self.element_is_clickable(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_6, 20)
        self.find(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_6).click()
        self.element_is_not_visible(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_6, 20)
        self.element_is_clickable(locators.LOGO_USER, 20)
        assert self.driver.current_url == 'http://localhost:3001/anime/6', f'[Error] AnimePage модуль "Обзор" после клика на 6-й слайд открылся не тот аниме'

    def go_to_all_button(self):
        element = self.find(locators.ALL_BUTTON)
        self.go_to_element_center(element)
        self.element_is_clickable(locators.ALL_BUTTON, 20)

    def click_to_all_button(self):
        precond = len(self.finds(locators.RELATED_ANIME_ALL))
        self.find(locators.ALL_BUTTON).click()
        self.element_is_not_visible(locators.ALL_BUTTON, 20)
        self.element_is_clickable(locators.RELATED_ANIME_9, 15)
        assert precond < len(self.finds(locators.RELATED_ANIME_ALL)), f"[Error] AnimePage модуль 'Связанные' после клика на 'Показать все' не появились новые слайды"

    def click_to_15_anime_related_module(self):
        element = self.find(locators.RELATED_ANIME_15)
        self.go_to_element_center(element)
        self.element_is_clickable(locators.RELATED_ANIME_15, 20)
        self.find(locators.RELATED_ANIME_15).click()
        self.element_is_not_visible(locators.RELATED_ANIME_15, 20)
        self.element_is_clickable(locators.LOGO_USER, 20)
        assert self.driver.current_url == 'http://localhost:3001/anime/15', f'[Error] AnimePage модуль "Связанные" после клика на 15-й слайд открылся не тот аниме'

    def go_to_all_button_heroes_module(self):
        element = self.find(locators.ALL_BUTTON_HEROES_MODULE)
        self.go_to_element_center(element)
        self.element_is_clickable(locators.ALL_BUTTON_HEROES_MODULE, 20)

    def click_to_all_button_heroes_module(self):
        precond = len(self.finds(locators.HEROES_SLIDE_ALL))
        self.find(locators.ALL_BUTTON_HEROES_MODULE).click()
        self.element_is_not_visible(locators.ALL_BUTTON_HEROES_MODULE, 20)
        self.element_is_clickable(locators.HEROES_SLIDE_9, 15)
        assert precond < len(self.finds(locators.HEROES_SLIDE_ALL)), f"[Error] AnimePage модуль 'Персонажи' после клика на 'Показать все' не появились новые слайды. Было - {precond} слайдов, после нажатия - {len(self.finds(locators.HEROES_SLIDE_ALL))}"

    def go_to_all_button_authors_module(self):
        element = self.find(locators.ALL_BUTTON_AUTHORS_MODULE)
        self.go_to_element_center(element)
        self.element_is_clickable(locators.ALL_BUTTON_AUTHORS_MODULE, 20)

    def click_to_all_button_authors_module(self):
        precond = len(self.finds(locators.AUTHORS_SLIDE_ALL))
        self.find(locators.ALL_BUTTON_AUTHORS_MODULE).click()
        self.element_is_not_visible(locators.ALL_BUTTON_AUTHORS_MODULE, 20)
        self.element_is_clickable(locators.AUTHORS_SLIDE_9, 15)
        assert precond < len(self.finds(locators.AUTHORS_SLIDE_ALL)), f"[Error] AnimePage модуль 'Создатели' после клика на 'Показать все' не появились новые слайды. Было - {precond} слайдов, после нажатия - {len(self.finds(locators.AUTHORS_SLIDE_ALL))}"

    def swipe_similar_carousel(self):
        self.random_carousel_similar = self.random_number(4, 26)
        self.go_to_element(element=self.finds(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_ALL)[self.random_carousel_similar])
        assert self.finds(locators.SIMILAR_CAROUSEL_ANIME_SLIDE_ALL)[self.random_carousel_similar].is_displayed(), f'[ERROR] AnimePage карусель "Похожие" после скролла к слайду {self.random_carousel_similar} не виден.'