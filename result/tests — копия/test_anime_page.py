from pages.anime_page import AnimePage
import pytest
from time import sleep

# Проверяем логику кнопки 'Посмотреть'
@pytest.mark.smoke_desktop
def test_watch_button_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.click_watch_button()

# Проверяем логику кнопки "Трейлер"
@pytest.mark.smoke_desktop
def test_trailer_button_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.click_trailer_button()

# По нажатию на "Добавить коллекцию" появляется выпадающий список
@pytest.mark.smoke_desktop
def test_list_collection_check(driver):
    """Пока кликать нет смысла"""
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_list()
    anime_page.click_to_list()

# Про повторном нажатии на "Добавить коллекцию" пропадает список
@pytest.mark.smoke_desktop
def test_list_collection_back(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_list()
    anime_page.click_to_list_repeat()

# по дефолту активен модуль 'Обзор'
@pytest.mark.smoke_desktop
def test_review_button_default(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.review_button_is_default()

# По клик на 'Связанные' открывается соответствующий модуль
@pytest.mark.smoke_desktop
def test_related_button_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.related_button_click()

# По клик на 'Персонажи' открывается соответствующий модуль
@pytest.mark.smoke_desktop
def test_hero_button_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.hero_button_click()

# По клик на 'Создатели' открывается соответствующий модуль
@pytest.mark.smoke_desktop
def test_authors_button_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.authors_button_click()

# По клик на 'Отзывы' открывается соответствующий модуль
@pytest.mark.smoke_desktop
def test_feedback_button_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.feedback_button_click()

"""Модуль 'Отзывы'."""

# По нажатию на "Написать обзор" появляется pop-up
@pytest.mark.smoke_desktop
def test_click_to_write_feedback(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.feedback_button_click()
    anime_page.click_to_write_feedback_button()

# По дефолту активна 1-я звезда, остальные не активные
@pytest.mark.smoke_desktop
def test_stars_default(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.feedback_button_click()
    anime_page.click_to_write_feedback_button()
    anime_page.stars_default_check()

# Прокликиваем каждые звезды
@pytest.mark.smoke_desktop
def test_stars_click(driver):
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.feedback_button_click()
    anime_page.click_to_write_feedback_button()
    anime_page.click_to_2_star()
    anime_page.click_to_3_star()
    anime_page.click_to_4_star()
    anime_page.click_to_5_star()

@pytest.mark.smoke_desktop
def test_feedback_send(driver):
    """
    Заполняем отзыв и отправляем. Проверяем общую работоспособность
    """
    text = 'Проверка текста'
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.feedback_button_click()
    anime_page.click_to_write_feedback_button()
    anime_page.send_text(text)
    anime_page.checkbox_click()
    anime_page.send_feedback()

@pytest.mark.smoke_desktop
def test_close_pop_up(driver):
    """
    По нажатию на крестик закрывается поп-ап
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_section_buttons()
    anime_page.feedback_button_click()
    anime_page.click_to_write_feedback_button()
    anime_page.close_pop_up()

# Модуль Обзор (карусель)
@pytest.mark.smoke_desktop
def test_back_button_review_module_invisible_default(driver):
    """
    По дефолту у карусели кнопка "Back" невидимая и кнопка "Next" видимая
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.back_button_invisible_similar_carousel()

@pytest.mark.smoke_desktop
def test_next_button_review_module_invisible_default(driver):
    '''
    По дефолту кнопка "NEXT" видимая
    '''
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.next_button_visible_similar_carousel()

@pytest.mark.smoke_desktop
def test_click_next_button(driver):
    """
    При нажатии на кнопку 'Next' скроллится карусель +  кнопка 'Back' становится видимой
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.first_click_to_next_button()
    anime_page.back_button_visible()

@pytest.mark.smoke_desktop
def test_click_to_back_button(driver):
    """
    По нажатию на кнопку 'Back' карусель скроллится назад
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.first_click_to_next_button()
    anime_page.first_click_to_back_button()
    anime_page.back_button_invisible_similar_carousel()

@pytest.mark.smoke_desktop
def test_next_button_invisible(driver):
    """
    В последнем скролле карусели кнопка 'Next' невидимая
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.next_button_click_to_end()
    anime_page.next_button_invisible()
    anime_page.back_button_visible()

@pytest.mark.smoke_desktop
def test_click_random_anime(driver):
    """
    По клику на слайд открывается соответствующий аниме
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.click_to_3_slide()

# Модуль Связанные (слайды)
@pytest.mark.smoke_desktop
def test_all_button_click_related_module(driver):
    """
    По клику на кнопку 'Показать все' в модуле 'Связанные' появляются новые аниме
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.related_button_click()
    anime_page.click_to_all_button()

@pytest.mark.smoke_desktop
def test_click_to_anime_related_module(driver):
    """
    По клику на аниме в модуле 'Связанные' открывается соответствующий аниме
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.related_button_click()
    anime_page.click_to_all_button()
    anime_page.click_to_15_anime_related_module()

# Модуль Персонажи (слайды)
@pytest.mark.smoke_desktop
def test_all_button_click_heroes_module(driver):
    """
    По клику на кнопку 'Показать все' в модуле 'Персонажи' появляются новые аниме
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.hero_button_click()
    anime_page.go_to_all_button_heroes_module()
    anime_page.click_to_all_button_heroes_module()

# нужен тест на клик по слайду

# Модуль Создатели (слайды)
@pytest.mark.smoke_desktop
def test_all_button_click_authors_module(driver):
    """
    По клику на кнопку 'Показать все' в модуле 'Создатели' появляются новые карточки
    """
    anime_page = AnimePage(driver)
    anime_page.open('http://localhost:3001/anime/1')
    anime_page.authors_button_click()
    anime_page.go_to_all_button_authors_module()
    anime_page.click_to_all_button_authors_module()

    # нужен тест на клик по слайду


# # # Мобилка # # #

def test_carousel_similar_swipe(driver):
    """Проверяем свайп карусели 'Похожие' на странице AnimePage."""
    anime_page = AnimePage(driver)
    anime_page.open_mobile('http://localhost:3001/anime/1')
    anime_page.scroll_to_carousel()
    anime_page.swipe_similar_carousel()

# остальные проверки в регресс