from pages.base_page import BasePage
from locators.player_page_locators import PlayerLocators
from locators.header_element_locators import HeaderElementLocators
import random
from faker import Faker
from selenium.webdriver.common.action_chains import ActionChains
locators = PlayerLocators()
locator_header = HeaderElementLocators()

class PlayerPage(BasePage):
    """Общий класс для страницы Player"""

    random_comment = None

    def scroll_to_like_anime(self):
        self.go_to_element_center(element=self.find(locators.LIKE_BUTTON_ANIME))
        self.element_is_clickable(locators.LIKE_BUTTON_ANIME, 20)

    def anime_likes_count_default(self):
        # Получаем стартовое число лайков
        assert int(self.find(locators.COUNT_LIKES_ANIME).text) >= 0, f'[Error] PlayerPage - По дефолту у аниме отрицательное количество лайков. Фактическое количество = {self.find(locators.COUNT_LIKES_ANIME).text}'
        return self.find(locators.COUNT_LIKES_ANIME).text

    def anime_like_button_click(self):
        start_count = self.anime_likes_count_default()
        self.find(locators.LIKE_BUTTON_ANIME).click()
        assert 'likes-module-scss-module__q3Yqyq__active' in self.find(locators.LIKE_BUTTON_ANIME).get_attribute('class'), f'[Error] PlayerPage После нажатия на лайк у аниме, у элемента Лайк отсутствует значение "likes-module-scss-module__q3Yqyq__active" у аттрибута "class". Фактическое значение = {self.find(locators.LIKE_BUTTON_ANIME).get_attribute("class")}'
        assert int(self.find(locators.COUNT_LIKES_ANIME).text) == int(start_count) + 1, f'[Error] PlayerPage После нажатия на лайк у аниме ошибка счетчика лайков.'

    def anime_like_button_repeat_click(self):
        start_count = self.anime_likes_count_default()
        self.find(locators.LIKE_BUTTON_ANIME).click()
        assert not 'likes-module-scss-module__q3Yqyq__active' in self.find(locators.LIKE_BUTTON_ANIME).get_attribute('class'), f'[Error] PlayerPage После нажатия на лайк у аниме, у элемента Лайк отсутствует значение "likes-module-scss-module__q3Yqyq__active" у аттрибута "class". Фактическое значение = {self.find(locators.LIKE_BUTTON_ANIME).get_attribute("class")}'
        assert int(self.find(locators.COUNT_LIKES_ANIME).text) == int(start_count) - 1, f'[Error] PlayerPage После нажатия на активный лайк у аниме ошибка счетчика лайков.'

    def scroll_to_dislike_anime(self):
        self.go_to_element_center(element=self.find(locators.DISLIKE_BUTTON_ANIME))
        self.element_is_clickable(locators.DISLIKE_BUTTON_ANIME, 20)

    def anime_dislikes_count_default(self):
        # Получаем стартовое число дизлайков
        assert int(self.find(locators.COUNT_DISLIKES_ANIME).text) >= 0, f'[Error] PlayerPage - По дефолту у аниме отрицательное количество дизлайков. Фактическое количество = {self.find(locators.COUNT_DISLIKES_ANIME).text}'
        return self.find(locators.COUNT_DISLIKES_ANIME).text
    
    def anime_dislike_button_click(self):
        start_count = self.anime_dislikes_count_default()
        self.find(locators.DISLIKE_BUTTON_ANIME).click()
        assert 'likes-module-scss-module__q3Yqyq__active' in self.find(locators.DISLIKE_BUTTON_ANIME).get_attribute('class'), f'[Error] PlayerPage После нажатия на дизлайк у аниме, у элемента ДизЛайк отсутствует значение "likes-module-scss-module__q3Yqyq__active" у аттрибута "class". Фактическое значение = {self.find(locators.DISLIKE_BUTTON_ANIME).get_attribute("class")}'
        assert int(self.find(locators.COUNT_DISLIKES_ANIME).text) == int(start_count) + 1, f'[Error] PlayerPage После нажатия на дизлайк у аниме ошибка счетчика дизлайков.'

    def like_and_dislike_click(self):
        # Клик на лайк после на дизлайк
        start_count_like = int(self.anime_likes_count_default())
        start_count_dislike = int(self.anime_dislikes_count_default())
        self.find(locators.LIKE_BUTTON_ANIME).click()
        self.find(locators.DISLIKE_BUTTON_ANIME).click()
        assert start_count_like == int(self.find(locators.COUNT_LIKES_ANIME).text), f'[Error] PlayerPage После нажатия на лайк и после на дизлайк, стартовое число лайков {start_count_like} неравно фактическому числу {int(self.find(locators.COUNT_LIKES_ANIME).text)}'
        assert start_count_dislike == int(self.find(locators.COUNT_DISLIKES_ANIME).text) - 1, f'[Error] PlayerPage После нажатия на лайк и после на дизлайк, число дизов не увеличилось на +1. Было {start_count_dislike}, а стало {int(self.find(locators.COUNT_DISLIKES_ANIME).text)}'

    def dislike_and_undislike_click(self):
        # Клик на дизлайк после еще раз на дизлайк
        start_count_dislike = int(self.anime_dislikes_count_default())
        self.find(locators.DISLIKE_BUTTON_ANIME).click()
        self.find(locators.DISLIKE_BUTTON_ANIME).click()
        assert start_count_dislike == int(self.find(locators.COUNT_DISLIKES_ANIME).text), f'[Error] PlayerPage После нажатия на дизлайк и после еще раз на дизлайк, число дизов неравно начальному кличеству. Было {start_count_dislike}, а стало {int(self.find(locators.COUNT_DISLIKES_ANIME).text)}'

    def dislike_and_like_click(self):
        # Клик на дизлайк после еще раз на дизлайк
        start_count_like = int(self.anime_likes_count_default())
        start_count_dislike = int(self.anime_dislikes_count_default())
        self.find(locators.DISLIKE_BUTTON_ANIME).click()
        self.find(locators.LIKE_BUTTON_ANIME).click()
        assert start_count_like == int(self.find(locators.COUNT_LIKES_ANIME).text) - 1, f'[Error] PlayerPage После нажатия на дизлайк и после на лайк, число лайков не увеличилось на +1. Было {start_count_like}, фактическое числоа = {int(self.find(locators.COUNT_LIKES_ANIME).text)}'
        assert start_count_dislike == int(self.find(locators.COUNT_DISLIKES_ANIME).text), f'[Error] PlayerPage После нажатия на дизлайк и после на лайк, число дизов неравно начальному количеству. Было {start_count_dislike}, а стало {int(self.find(locators.COUNT_DISLIKES_ANIME).text)}'

    def scroll_to_get_more_button(self):
        self.element_is_visible(locators.GETMORE_BUTTON_ANIME, 20)
        self.go_to_element_center(element=self.find(locators.GETMORE_BUTTON_ANIME))

    def click_to_report_anime(self):
        self.find(locators.GETMORE_BUTTON_ANIME).click()
        self.element_is_clickable(locators.REPORT_BUTTON_ANIME, 20)
        self.find(locators.REPORT_BUTTON_ANIME).click()
        map(lambda x: self.element_is_clickable(x), self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL))

    def not_like_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[0].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def abuse_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[1].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def contrafact_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[2].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def porn_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[3].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def personal_data_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[4].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def terror_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[5].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def spam_data_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[6].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def copyright_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[7].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def other_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[8].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)
    
    def must_delete_button_click(self):
        self.finds(locators.REPORT_WINDOW_ANIME_BUTTONS_ALL)[9].click()
        self.element_is_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def send_form_report(self):
        self.find(locators.TEXTAREA_REPORT_WINDOW).send_keys('Салам поплам')
        self.element_is_clickable(locators.SEND_FORM_BUTTON_REPORT_WINDOW, 20)
        self.find(locators.SEND_FORM_BUTTON_REPORT_WINDOW).click()
        self.element_is_not_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    def close_popup_report_click(self):
        self.element_is_clickable(locators.CLOSE_FORM_REPORT_BUTTON, 20)
        self.find(locators.CLOSE_FORM_REPORT_BUTTON).click()
        self.element_is_not_visible(locators.REPORT_WINDOW_CONTAINER, 20)

    # Блок 'Комментарий'

    def scroll_to_write_comment_button(self):
        self.go_to_element_center(element=self.find(locators.WRITE_COMMENT_BUTTON_ANIME))
        self.element_is_clickable(locators.WRITE_COMMENT_BUTTON_ANIME, 20)

    def write_comment_button_click(self):
        self.find(locators.WRITE_COMMENT_BUTTON_ANIME).click()
        self.element_is_visible(locators.MODAL_TABLE_COMMENT, 20)

    def click_to_random_stars(self):
        all_stars = self.finds(locators.STARS_ALL_SVG)
        clicked_star = random.choice(self.finds(locators.STARS_ALL_SVG))
        star_index = all_stars.index(clicked_star)
        clicked_star.click()

        if star_index == 0:
            assert 'fill-orange' in self.finds(locators.STARS_ALL_SVG)[0].get_attribute('class'), f'[Error] PlayerPage модальное окно комментария - отсутствует аттрибут "fill-orange" у 1-й звезды'
        elif star_index > 0:
            for i in range(0, star_index + 1):
                if not 'fill-orange' in self.finds(locators.STARS_ALL_SVG)[i].get_attribute('class'):
                    raise AssertionError(f'[Error] PlayerPage модальное окно комментария - отсутствует аттрибут "fill-orange" у элемента STARS_ALL_SVG[{i}]')
        
        if star_index < len(all_stars):
            for i in range(star_index + 1, 5):
                if 'fill-orange' in self.finds(locators.STARS_ALL_SVG)[i].get_attribute('class'):
                    raise AssertionError(f'[Error] PlayerPage модальное окно комментария - ЕСТЬ аттрибут "fill-orange" у элемента STARS_ALL_SVG[{i}]')
                
    def write_random_text(self):
        fake = Faker("ru_RU")
        fake_text = fake.text(max_nb_chars=80)
        self.element_is_clickable(locators.TEXTAREA_COMMENT, 20)
        self.find(locators.TEXTAREA_COMMENT).send_keys(fake_text)
        # НУЖНА ПРОВЕРКА НА ВВЕДЕННОЕ ЗНАЧЕНИЕ SHADOW_DOM
        
    def checkbox_random_active(self):
        self.element_is_clickable(locators.CHECKBOX_COMMENT, 20)
        random_checkbox_activity = random.randrange(0, 2)
        if random_checkbox_activity == 0:
            self.find(locators.CHECKBOX_COMMENT).click()
            self.element_is_visible(locators.CHECKBOX_OK_IMAGE_COMMENT, 15)
            self.find(locators.CHECKBOX_COMMENT).click()
            self.element_is_not_visible(locators.CHECKBOX_OK_IMAGE_COMMENT, 15)
        else:
            self.find(locators.CHECKBOX_COMMENT).click()
            self.element_is_visible(locators.CHECKBOX_OK_IMAGE_COMMENT, 15)
    
    def send_comment_anime(self):
        self.element_is_clickable(locators.SEND_COMMENT_BUTTON, 20)
        self.find(locators.SEND_COMMENT_BUTTON).click()
        self.element_is_not_visible(locators.MODAL_TABLE_COMMENT, 20)

    def click_to_get_more_button(self):
        # Далее клик на кнопку get_more
        assert self.finds(locators.GET_MORE_BUTTON_COMMENT_ALL)[self.random_comment].is_displayed()
        self.finds(locators.GET_MORE_BUTTON_COMMENT_ALL)[self.random_comment].click()
        #Добавлен доп скролл к попап для наджености
        self.go_to_element_center(element=self.finds(locators.GET_MORE_BUTTON_COMMENT_ALL)[self.random_comment])
        self.element_is_visible(locators.POP_UP_GET_MORE_COMMENT_ALL, 20)

    def click_to_delete_buton(self):
        self.find(locators.COMMENT_DELETE_BUTTON).click()
        self.element_is_visible(locators.POP_UP_CONFIRM_WINDOW, 20)
        #self.element_is_not_visible(locators.POP_UP_GET_MORE_COMMENT_ALL, 20)

    def click_to_confirm_delete_button(self):
        self.element_is_clickable(locators.CONFIRM_DELETE_BUTTON, 20)
        self.find(locators.CONFIRM_DELETE_BUTTON).click()
        self.element_is_not_visible(locators.POP_UP_CONFIRM_WINDOW, 20)
        self.element_is_not_visible(locators.POP_UP_GET_MORE_COMMENT_ALL, 20)

    def close_confirm_delete_pop_up(self):
        self.element_is_clickable(locators.CLOSE_CONFIRM_DELETE_POP_UP, 20)
        self.find(locators.CLOSE_CONFIRM_DELETE_POP_UP).click()
        self.element_is_not_visible(locators.CLOSE_CONFIRM_DELETE_POP_UP, 20)

    def scroll_to_random_comment(self):
        m = len(self.finds(locators.COMMENT_CONTAINER)) - 1
        self.random_comment = random.randrange(0, m + 1)
        self.go_to_element_center(element=self.finds(locators.COMMENT_CONTAINER)[self.random_comment])
        assert self.finds(locators.COMMENT_CONTAINER)[self.random_comment].is_displayed()

    def like_random_comment(self):
        # Подсчет числа лайков
        count_likes = int(self.finds(locators.COUNT_LIKES_COMMENT_ALL)[self.random_comment].text)
        #assert count_likes > 0, f'[Error] PlayerPage у комментария отрицательно количество лайков. Фактическое количество = {count_likes}'
        # Лайкаем коммент
        self.finds(locators.LIKE_BUTTON_COMMENT_ALL)[self.random_comment].click()
        assert count_likes == int(self.finds(locators.COUNT_LIKES_COMMENT_ALL)[self.random_comment].text) - 1, f'[Error] PlayerPage у комментария после нажатия на лайк не увеличилось количество лайков. Должно быть = {count_likes + 1}.Фактическое количество = {int(self.finds(locators.COUNT_LIKES_COMMENT_ALL)[self.random_comment].text)}'

    def dislike_random_comment(self):    
        # Подсчет числа лайков
        count_likes = int(self.finds(locators.COUNT_LIKES_COMMENT_ALL)[self.random_comment].text)
        #assert count_likes > 0, f'[Error] PlayerPage у комментария отрицательно количество лайков. Фактическое количество = {count_likes}'
        self.finds(locators.DISLIKE_BUTTON_COMMENT_ALL)[self.random_comment].click()
        assert count_likes == int(self.finds(locators.COUNT_LIKES_COMMENT_ALL)[self.random_comment].text) + 1, f'[Error] PlayerPage у комментария после нажатия на дизлайк не уменьшилось количество лайков. Должно быть = {count_likes - 1}.Фактическое количество = {int(self.finds(locators.COUNT_LIKES_COMMENT_ALL)[self.random_comment].text)}'

# Блок "Эпизоды"

    def scroll_to_episodes_container(self):
        self.go_to_element(element=self.find(locators.EPISODES_H2))
        self.element_is_visible(locators.EPISODES_H2, 20)

    def scrolling_episodes_block(self):
        m = len(self.finds(locators.EPIDODES_SERIES_ALL)) - 1
        self.go_to_element_center(element=self.finds(locators.EPIDODES_SERIES_ALL)[m])
        assert self.finds(locators.EPIDODES_SERIES_ALL)[m].is_displayed(), f'[Error] PlayerPage Блок "Эпизоды" отсутствует серия {m + 1}'

# Плеер

    def check_player(self):
        self.element_is_clickable(locators.VIDEOPLAYER_CONTAINER, 20)

    def click_to_play_player(self):
        self.element_is_clickable(locators.PLAY_VIDEOPLAYER, 20)
        self.find(locators.PLAY_VIDEOPLAYER).click()
        self.element_is_not_visible(locators.PLAY_VIDEOPLAYER, 100)
        #self.element_is_visible(locators.BOTTOM_PLAYER_CONTAINER, 20) УТОЧНИТЬ
        assert self.find(locators.MINI_PLAY_BUTTON).get_attribute('aria-pressed') == "true", f'[Error] PlayerPage после нажатия на плеер не играет аниме. Стоит на паузе. Аттрибут aria_pressed = {self.find(locators.MINI_PLAY_BUTTON).get_attribute("aria-pressed")}'

    def mouse_hover_to_player(self):
        self.element_is_not_visible(locators.BOTTOM_PLAYER_CONTAINER, 20)
        player = self.find(locators.VIDEOPLAYER_CONTAINER)
        actions = ActionChains(self.driver)
        actions.move_to_element(player).perform()
        self.element_is_visible(locators.BOTTOM_PLAYER_CONTAINER, 20)
        assert self.find(locators.MINI_PLAY_BUTTON).get_attribute('aria-pressed') == "true", f'[Error] PlayerPage после нажатия на плеер не играет аниме. Стоит на паузе. Аттрибут aria_pressed = {self.find(locators.MINI_PLAY_BUTTON).get_attribute("aria-pressed")}'

    def click_to_setting_buttons(self):
        self.element_is_visible(locators.BOTTOM_PLAYER_CONTAINER, 20)
        self.element_is_clickable(locators.SETTINGS_BUTTON_PLAYER, 20)
        self.mouse_hover_to_player()
        self.find(locators.SETTINGS_BUTTON_PLAYER).click()
        self.element_is_visible(locators.SETTINGS_WINDOW_CONTAINER, 20)

    def click_to_language_button(self):
        self.element_is_clickable(locators.SETTINGS_LANGUAGE_BUTTON, 20)
        self.find(locators.SETTINGS_LANGUAGE_BUTTON).click()
        self.element_is_visible(locators.SETTINGS_AFTER_CLICK_WINDOW, 20)
        assert self.find(locators.SETTINGS_AFTER_CLICK_H1).text == "Озвучка", f'[Error] PlayerPage После нажатия на кнопку "Озвучка" открылся не тот поп ап, либо у него неверный H1. Фактический результа = {self.find(locators.SETTINGS_LANGUAGE_H1).text}'

    def click_to_speed_button(self):
        self.element_is_clickable(locators.SETTINGS_SPEED_BUTTON, 20)
        self.find(locators.SETTINGS_SPEED_BUTTON).click()
        self.element_is_visible(locators.SETTINGS_AFTER_CLICK_WINDOW, 20)
        assert self.find(locators.SETTINGS_AFTER_CLICK_H1).text == "Скорость", f'[Error] PlayerPage После нажатия на кнопку "Скорость" открылся не тот поп ап, либо у него неверный H1. Фактический результа = {self.find(locators.SETTINGS_LANGUAGE_H1).text}'

    def click_to_quality_button(self):
        self.element_is_clickable(locators.SETTINGS_QUALITY_BUTTON, 20)
        self.find(locators.SETTINGS_QUALITY_BUTTON).click()
        self.element_is_visible(locators.SETTINGS_AFTER_CLICK_WINDOW, 20)
        assert self.find(locators.SETTINGS_AFTER_CLICK_H1).text == "Качество", f'[Error] PlayerPage После нажатия на кнопку "Качество" открылся не тот поп ап, либо у него неверный H1. Фактический результа = {self.find(locators.SETTINGS_LANGUAGE_H1).text}' 

    def click_to_other_settings_button(self):
        self.element_is_clickable(locators.SETTINGS_OTHER_BUTTON, 20)
        self.find(locators.SETTINGS_OTHER_BUTTON).click()
        self.element_is_visible(locators.SETTINGS_AFTER_CLICK_WINDOW, 20)
        assert self.find(locators.SETTINGS_AFTER_CLICK_H1).text == "Другие настройки", f'[Error] PlayerPage После нажатия на кнопку "Качество" открылся не тот поп ап, либо у него неверный H1. Фактический результа = {self.find(locators.SETTINGS_LANGUAGE_H1).text}'

    def click_to_subtitle_settings_button(self):
        self.mouse_hover_to_player()
        self.element_is_clickable(locators.SETTINGS_SUBTITLE_BUTTON, 20)
        self.find(locators.SETTINGS_SUBTITLE_BUTTON).click()
        self.element_is_visible(locators.SETTINGS_AFTER_CLICK_WINDOW, 20)
        assert self.find(locators.SETTINGS_AFTER_CLICK_H1).text == "Субтитры", f'[Error] PlayerPage После нажатия на кнопку "Субтитры" открылся не тот поп ап, либо у него неверный H1. Фактический результа = {self.find(locators.SETTINGS_LANGUAGE_H1).text}'

    def click_to_more_volume_settings_button(self):
        self.mouse_hover_to_player()
        self.element_is_clickable(locators.SETTINGS_MORE_VOLUME_BUTTON, 20)
        self.find(locators.SETTINGS_MORE_VOLUME_BUTTON).click()
        self.element_is_visible(locators.SETTINGS_AFTER_CLICK_WINDOW, 20)
        assert self.find(locators.SETTINGS_AFTER_CLICK_H1).text == "Усиление громкости", f'[Error] PlayerPage После нажатия на кнопку "Усиление громкости" открылся не тот поп ап, либо у него неверный H1. Фактический результа = {self.find(locators.SETTINGS_LANGUAGE_H1).text}'  

    def change_timecode_player(self):
        time = self.find(locators.SLIDER_TIME_PLAYING)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(time, 30, 0).perform()
        assert self.find(locators.CURRENT_TIME_PLAYER).text > "0:30"

    def click_fullscreen(self):
        self.element_is_clickable(locators.FULLSCREEN_BUTTON, 20)
        self.find(locators.FULLSCREEN_BUTTON).click()
        assert self.find(locators.VIDEOPLAYER_CONTAINER).get_attribute('data-fullscreen') == "", f'[Error] PlayerPage после нажатия на фуллскрин button у плеер остутствует аттрибут data-fullscreen.'

    def activate_mobile_player(self):
        player = self.find(locators.VIDEOPLAYER_CONTAINER)
        actions = ActionChains(self.driver)
        actions.move_to_element(player).perform()

    def click_to_play_player_mobile(self):
        self.check_player()
        self.find(locators.PLAY_VIDEOPLAYER).click()
        self.activate_mobile_player()
        self.element_is_not_visible(locators.PLAY_VIDEOPLAYER, 20)
        self.element_is_clickable(locators.PLAY_BUTTON_MOBILE, 20)
        self.element_is_clickable(locators.PREV_EPISODE_BUTTON_MOBILE, 20)
        self.element_is_clickable(locators.NEXT_EPISODE_BUTTON_MOBILE, 20)

    def click_to_settings_button_mobile(self):
        self.element_is_clickable(locators.SETTINGS_BUTTON_PLAYER_MOBILE, 20)
        self.find(locators.SETTINGS_BUTTON_PLAYER_MOBILE).click()
        self.element_is_visible(locators.SETTINGS_WINDOW_CONTAINER_MOBILE, 20)

    def scroll_to_short_comment(self):
        self.go_to_element_center(element=self.find(locators.SHORT_COMMENT_MOBILE))
        self.element_is_clickable(locators.SHORT_COMMENT_MOBILE, 20)

    def click_to_short_comment(self):
        self.find(locators.SHORT_COMMENT_MOBILE).click()
        self.element_is_visible(locators.COMMENT_PLAYER_MOBILE_CONTAINER, 20)