from pages.player_page import PlayerPage
import pytest
from time import sleep
import allure

# Кнопки лайк и Дизлайк у Аниме

@pytest.mark.smoke_desktop
def test_click_to_like_in_anime(driver):
    """По нажатию на лайк у аниме в счетчик лайков +1."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_like_anime()
    playerpage.anime_like_button_click()

@pytest.mark.smoke_desktop
def test_click_to_dislike_in_anime(driver):
    """По нажатию на дизлайк у аниме в счетчик лайков -1."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_dislike_anime()
    playerpage.anime_dislike_button_click()

@pytest.mark.smoke_desktop
def test_repeat_click_to_like_in_anime(driver):
    """По нажатию на лайк у аниме в счетчик лайков +1 и после повторного нажатия на лайк -1."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_like_anime()
    playerpage.anime_like_button_click()
    playerpage.anime_like_button_repeat_click()

@pytest.mark.smoke_desktop
def test_like_and_unlike_anime(driver):
    """По нажатию на лайк у аниме в счетчик лайков +1 и после нажатия на дизлайк - у лайков -1 у дизлайков +1 ."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_like_anime()
    playerpage.like_and_dislike_click()

@pytest.mark.smoke_desktop
def test_dislike_and_undislike_anime(driver):
    """По нажатию на дизлайк у аниме в счетчик дизлайков +1 и после повторного нажатия на дизлайк - у счетчика дизлайков -1 ."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_dislike_anime()
    playerpage.dislike_and_undislike_click()

@pytest.mark.smoke_desktop
def test_dislike_and_like(driver):
    """По нажатию на дизлайк у аниме в счетчик дизлайков +1 и после нажатия на лайк - у лайков +1 у дизлайков -1 ."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_dislike_anime()
    playerpage.dislike_and_like_click()

# Поп-ап пожаловаться на аниме
@pytest.mark.smoke_desktop
def test_get_more_button_click(driver):
    """По нажатию на кнопку 'Больше' и пожаловаться появляется поп-ап"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()

@pytest.mark.smoke_desktop
def test_not_like_button_click_in_report(driver):
    """По нажатию на 'Не нравится' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.not_like_button_click()

@pytest.mark.smoke_desktop
def test_abuse_button_click_in_report(driver):
    """По нажатию на 'Насилие' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.abuse_button_click()

@pytest.mark.smoke_desktop
def test_contrafact_button_click_in_report(driver):
    """По нажатию на 'Незаконные товары' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.contrafact_button_click()

@pytest.mark.smoke_desktop
def test_porn_button_click_in_report(driver):
    """По нажатию на 'Порнография' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.porn_button_click()

@pytest.mark.smoke_desktop
def test_personal_data_button_click_in_report(driver):
    """По нажатию на 'Персональные данные' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.personal_data_button_click()

@pytest.mark.smoke_desktop
def test_terror_button_click_in_report(driver):
    """По нажатию на 'Терроризм' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.terror_button_click()

@pytest.mark.smoke_desktop
def test_spam_button_click_in_report(driver):
    """По нажатию на 'Мошеничество и спам' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.spam_data_button_click()

@pytest.mark.smoke_desktop
def test_copyright_button_click_in_report(driver):
    """По нажатию на 'Нарушение авторских прав' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.copyright_button_click()

@pytest.mark.smoke_desktop
def test_copyright_button_click_in_report(driver):
    """По нажатию на 'Другое' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.copyright_button_click()

@pytest.mark.smoke_desktop
def test_must_to_delete_button_click_in_report(driver):
    """По нажатию на 'Нарушаеn закон, но надо удалить' открывается соответствующий поп-ап'"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.must_delete_button_click()

#Кнопка отправить не кликабельная
@pytest.mark.smoke_desktop
def test_send_report_popup(driver):
    """Проверяем отправку поп-апа"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.must_delete_button_click()
    #playerpage.send_form_report()

@pytest.mark.smoke_desktop
def test_close_report_window(driver):
    """Проверяем что поп-ап закрывается"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_get_more_button()
    playerpage.click_to_report_anime()
    playerpage.must_delete_button_click()
    playerpage.close_popup_report_click()

# Блок 'Комментарии'

@pytest.mark.smoke_desktop
def test_open_comment_window(driver):
    """По нажатию на кнопку 'Написать комментарий' открывается соответствующее модальное окно"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_write_comment_button()
    playerpage.write_comment_button_click()

@pytest.mark.smoke_desktop
def test_send_comment_anime(driver):
    """Проверяем функцию отправки коммента"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_write_comment_button()
    playerpage.write_comment_button_click()
    playerpage.click_to_random_stars()
    playerpage.write_random_text()
    playerpage.checkbox_random_active()
    playerpage.send_comment_anime()
    
@pytest.mark.smoke_desktop
def test_get_more_popup(driver):
    """По нажатию на 3 точки у коммента появляется попап"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_random_comment()
    playerpage.click_to_get_more_button()
    
@pytest.mark.smoke_desktop
def test_delete_comment(driver):
    """Проверка удаления коммента"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_random_comment()
    playerpage.click_to_get_more_button()
    playerpage.click_to_delete_buton()
    # Пока кнопка не работает
    #playerpage.click_to_confirm_delete_button()

@pytest.mark.smoke_desktop
def test_close_delete_pop_up(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_random_comment()
    playerpage.click_to_get_more_button()
    playerpage.click_to_delete_buton()
    playerpage.close_confirm_delete_pop_up()

# Функция оценки комментария

@pytest.mark.smoke_desktop
@allure.feature('Функция оценки комментария для разрешения декстопа')
def test_click_to_like_comment(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_random_comment()
    playerpage.like_random_comment()

@pytest.mark.smoke_desktop
@pytest.mark.xfail(reason='не работает дизлайк')
@allure.feature('Функция оценки комментария для разрешения декстопа')
def test_click_to_dislike_comment(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_random_comment()
    playerpage.dislike_random_comment()

# Блок эпизоды

@pytest.mark.smoke_desktop
@allure.feature('Блок эпизоды')
def test_scrolling_episode_block(driver):
    """Блок 'Эпизоды' скроллится."""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.scroll_to_episodes_container()
    playerpage.scrolling_episodes_block()

# Плеер

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_check_player(driver):
    """Плеер есть на странице"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.check_player()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_start_player(driver):
    """По нажатию на Play запускается аниме"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_check_bottom_module_player(driver):
    """При наведении на плеер появляется нижняя часть плеера"""
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_click_to_setting_button(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_language_popup(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()
    playerpage.click_to_language_button()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_speed_popup(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()
    playerpage.click_to_speed_button()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_quality_popup(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()
    playerpage.click_to_quality_button()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_other_settings_popup(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()
    playerpage.click_to_other_settings_button()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_subtitle_popup(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()
    playerpage.click_to_other_settings_button()
    playerpage.click_to_subtitle_settings_button()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_more_volume_popup(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_to_setting_buttons()
    playerpage.click_to_other_settings_button()
    playerpage.click_to_more_volume_settings_button()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_change_time_in_player(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.change_timecode_player()

@pytest.mark.smoke_desktop
@allure.feature('Плеер для разрешения декстопа')
def test_fullscreen_mode(driver):
    playerpage = PlayerPage(driver)
    playerpage.open('http://localhost:3001/player')
    playerpage.click_to_play_player()
    playerpage.mouse_hover_to_player()
    playerpage.click_fullscreen()

# # # Мобилка # # #


@pytest.mark.smoke_mobile
@allure.feature('Плеер для разрешения мобилок')
def test_start_mobile_player(driver):
    """По клику на плей запускается плеер на мобилке"""
    playerpage = PlayerPage(driver)
    playerpage.open_mobile('http://localhost:3001/player')
    playerpage.click_to_play_player_mobile()

@pytest.mark.smoke_mobile
@allure.feature('Плеер для разрешения мобилок')
def test_mobile_player_fullscreen(driver):
    """По клику на фуллскрин открывается фуллскрин плеер"""
    playerpage = PlayerPage(driver)
    playerpage.open_mobile('http://localhost:3001/player')
    playerpage.click_to_play_player_mobile()
    playerpage.click_fullscreen()

@pytest.mark.smoke_mobile
@allure.feature('Плеер для разрешения мобилок')
def test_change_time_in_player_mobile(driver):
    """При перемещении ползунка слайдбара тайминга происходит переход на соответствующий тайминг"""
    playerpage = PlayerPage(driver)
    playerpage.open_mobile('http://localhost:3001/player')
    playerpage.click_to_play_player_mobile()
    playerpage.change_timecode_player()

@pytest.mark.smoke_mobile
@allure.feature('Плеер для разрешения мобилок')
def test_check_settings_window_mobile(driver):
    """По клику на кнопку 'Настройки' открывается попап с настройками."""
    playerpage = PlayerPage(driver)
    playerpage.open_mobile('http://localhost:3001/player')
    playerpage.click_to_play_player_mobile()
    playerpage.click_to_settings_button_mobile()

# Комменты

@pytest.mark.smoke
def test_comment_click_check(driver):
    playerpage = PlayerPage(driver)
    playerpage.open_mobile('http://localhost:3001/player')
    playerpage.scroll_to_short_comment()
    playerpage.click_to_short_comment()
