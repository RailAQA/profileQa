from pages.sidebar_element import SideBar
import pytest
from time import sleep
# НУЖНА ПРОВЕРКА НА БЛОК ПРОДОЛЖИТЬ ПРОСМОТР ПОСЛЕ ТОГО КАК РЕАЛИЗУЮТ
# активная гиперссылка подсвечивается (ЛУЧШЕ В РЕГРЕСС)
# на странице аниме не подсвечивается гиперссылка (В регресс)


@pytest.mark.smoke_desktop
def test_sidebar_check(driver):
    """Есть логотип в сайдбаре, гиперссылка 4шт"""
    sidebar = SideBar(driver)
    sidebar.open('http://localhost:3001/home')
    sidebar.sidebar_elements_check()

@pytest.mark.smoke_desktop
def test_sidebar_logo_click(driver):
    """По нажатию на логотип перекидывает на главную страницу"""
    sidebar = SideBar(driver)
    sidebar.open('http://localhost:3001/anime/1')
    sidebar.sidebar_logo_click()

@pytest.mark.smoke_desktop
def test_sidebar_catalog_click(driver):
    """по нажатию на каталог перекидывает на страницу каталога"""
    sidebar = SideBar(driver)
    sidebar.open('http://localhost:3001/home')
    sidebar.catalog_button_click()

@pytest.mark.smoke_desktop
def test_sidebar_favourite_click(driver):
    """по нажатию на избранное перекидывает на страницу избранного"""
    sidebar = SideBar(driver)
    sidebar.open('http://localhost:3001/home')
    sidebar.favourite_button_click()

@pytest.mark.smoke_desktop
def test_sidebar_collection_click(driver):
    """по нажатию на коллекции перекидывает на страницу коллекции"""
    sidebar = SideBar(driver)
    sidebar.open('http://localhost:3001/home')
    sidebar.collection_button_click()

# # #  Мобилка  # # #
@pytest.mark.smoke_mobile
def test_open_burger_menu(driver):
    """По нажатию на кнопку бургер открывается бургер меню"""
    sidebar = SideBar(driver)
    sidebar.open_mobile('http://localhost:3001/home')
    sidebar.click_to_burger_menu()

@pytest.mark.smoke_mobile
def close_burger_menu(driver):
    """По нажатию на кнопку бургер открывается бургер меню"""
    sidebar = SideBar(driver)
    sidebar.open_mobile('http://localhost:3001/home')
    sidebar.click_to_burger_menu()
    sidebar.close_burger_menu()