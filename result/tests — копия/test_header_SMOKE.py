from pages.header_element import HeaderElement
import pytest


@pytest.mark.smoke_desktop
def test_header_check(driver):
    """Инпут поиска есть на странице"""
    header = HeaderElement(driver)
    header.open('http://localhost:3001/home')
    header.search_check()

@pytest.mark.smoke_desktop
def test_search_input(driver):
    """Если ввести название аниме появится всплывающая выдача"""
    promt = 'Пожирая небеса'
    header = HeaderElement(driver)
    header.open('http://localhost:3001/home')
    header.search_click()
    header.search_anime(promt)

@pytest.mark.smoke_desktop
def test_search_correct_anime(driver):
    """Поиск существующего аниме и переход на его страницу"""
    promt = 'Пожирая небеса'
    header = HeaderElement(driver)
    header.open('http://localhost:3001/home')
    header.search_click()
    header.search_anime(promt)
    header.search_results_anime_click()

@pytest.mark.smoke_desktop
def test_search_popup_go_away(driver):
    """если на любое место, кроме инпута, то всплюывающая выдача пропадет"""
    promt = 'Пожирая небеса'
    header = HeaderElement(driver)
    header.open('http://localhost:3001/home')
    header.search_click()
    header.search_anime(promt)
    header.click_to_random()

# # # Мобильная версия смоки # # #
@pytest.mark.smoke_mobile
def test_header_module_check(driver):
    """Кнопка бургер меню и инпут поиска есть в хедере"""
    header = HeaderElement(driver)
    header.open_mobile('http://localhost:3001/home')
    header.burger_is_visible()
    header.search_input_is_visible()
