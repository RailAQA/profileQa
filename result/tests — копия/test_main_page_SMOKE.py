from pages.main_page import MainPage
import pytest
from time import sleep

# проверка на автоматическую работу карусели можно закинуть в регреcc. Для смока это не маст хев

#Проверяем карусель 'По вашим предпочтениям'

@pytest.mark.smoke_desktop
def test_back_button_invisible_default(driver):
    """В дефолтном состояние кнопка "Back" не активная"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.carousel_back_button_is_not_visible()

@pytest.mark.smoke_desktop
def test_carousel_1_next(driver):
    """По нажатию на кнопку "Next" - меняется контент, кнопка 'Back' становится активной"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.first_click_next_button()

@pytest.mark.smoke_desktop
def test_back_button_click(driver):
    """По нажатию на кнопку "Back" (состояние - 2) карусель перелистывается назад и кнопка 'Back' становится не активной"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.first_click_next_button()
    main_page.click_back_button_to_1()

@pytest.mark.smoke_desktop
def test_click_anime_carousel(driver):
    """По клику на любой рандомный аниме, просходите переход на странице просмотра (клика на рандомный, в нашем случай переходим в состоние 2 и кликаем на 7-й аниме)"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.first_click_next_button()
    main_page.click_to_anime_carousel_1()

@pytest.mark.smoke_desktop
def test_next_button_invisible(driver):
    """В состоянии 7 кнопка "Next" невидимая"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.next_button_is_invisible_7()

#Проверяем карусель 'Сейчас в тренде'

@pytest.mark.smoke_desktop
def test_back_button_invisible_nowintrend(driver):
    """В дефолтном состоянии кнопка "Back" не активная"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_carousel_2()
    main_page.nowintrend_back_button_is_invisible()

@pytest.mark.smoke_desktop
def test_carousel_2_next(driver):
    """По нажатию на кнопку "Next" - меняется контент, кнопка 'Back' становится активной"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_carousel_2()
    main_page.first_click_next_button_nowintrend()

@pytest.mark.smoke_desktop
def test_back_button_nowintrend_click(driver):
    """По нажатию на кнопку "Back" (состояние - 2) карусель перелистывается назад и кнопка 'Back' становится не активной"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_carousel_2()
    main_page.first_click_next_button_nowintrend()
    main_page.click_back_button_to_1_nowintrend()

@pytest.mark.smoke_desktop
def test_click_anime_carousel(driver):
    """По клику на любой рандомный аниме, просходите переход на странице просмотра (клика на рандомный, в нашем случай переходим в состоние 2 и кликаем на 7-й аниме)"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_carousel_2()
    main_page.first_click_next_button_nowintrend()
    main_page.click_to_anime_carousel_in_nowintrend()

@pytest.mark.smoke_desktop
def test_next_button_invisible_nowintrend(driver):
    """В состоянии 7 кнопка "Next" невидимая"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_carousel_2()
    main_page.next_button_is_invisible_7_nowintrend()

#Проверяем рекламный баннер

@pytest.mark.smoke_desktop
def test_add_banner(driver):
    """Рекламнный баннер присутствует на странице"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.stop_carousel()
    main_page.scroll_to_add_block()
    main_page.add_block_check_in_page()

@pytest.mark.smoke_desktop
def test_add_banner_pagination_click(driver):
    """Проверяем переключение слево направо баннеров через пагинацию"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.stop_carousel()
    main_page.scroll_to_add_block()
    main_page.add_block_pagination1_click()
    main_page.add_block_pagination2_click()
    main_page.add_block_pagination3_click()
    main_page.add_block_pagination4_click()

@pytest.mark.smoke_desktop
def test_reverse_add_banner_pagination_click(driver):
    """Проверяем переключение справо налево баннеров через пагинацию"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.stop_carousel()
    main_page.scroll_to_add_block()
    main_page.add_block_pagination4_click()
    main_page.add_block_pagination3_click()
    main_page.add_block_pagination2_click()
    main_page.add_block_pagination1_click()

@pytest.mark.smoke_desktop
def test_pagination_repeat_click(driver):
    """При повторном нажатии на пагинацию ничего не происходит"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.stop_carousel()
    main_page.scroll_to_add_block()
    main_page.add_block_pagination1_click()
    main_page.add_block_pagination1_click_repeat()

# Блок 'Новинки'

@pytest.mark.smoke_desktop
def test_new_anime_in_page(driver):
    '''Проверяем, что главное странице есть блок "Новинки"'''
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_newanime_block()
    main_page.newanime_block_check_in_page()

@pytest.mark.smoke_desktop
def test_new_anime_random_slide_click(driver):
    """Кликаем на любой аниме из блока 'Новинки'"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_newanime_block()
    main_page.newanime_block_random_slide_click()

@pytest.mark.smoke_desktop
def test_new_anime_more_button(driver):
    """Проверяем логику работы кнопки 'Показать все'"""
    main_page = MainPage(driver)
    main_page.open('http://localhost:3001/home')
    main_page.scroll_to_newanime_block()
    main_page.newanime_block_more_button_click()


    # # # Мобилка # # #

@pytest.mark.smoke_mobile
def test_carousel_1_swipe(driver):
    """Проверям свайп карусели 'По вашим предпочтениям'."""
    main_page = MainPage(driver)
    main_page.open_mobile('http://localhost:3001/home')
    main_page.scroll_to_carousel_1()
    main_page.swipe_carousel_1()

@pytest.mark.smoke_mobile
def test_carousel_2_swipe(driver):
    """Проверям свайп карусели 'Сейчас в тренде'."""
    main_page = MainPage(driver)
    main_page.open_mobile('http://localhost:3001/home')
    main_page.scroll_to_carousel_2_mobile()
    main_page.swipe_carousel_2()

@pytest.mark.smoke_mobile
def test_more_button_check(driver):
    """Кликаем на кнопку 'Показать больше'.'"""
    main_page = MainPage(driver)
    main_page.open_mobile('http://localhost:3001/home')
    main_page.scroll_to_more_button()
    main_page.newanime_block_more_button_click()