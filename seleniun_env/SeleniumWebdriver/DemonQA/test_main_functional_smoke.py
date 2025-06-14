from pages.main_page import MainPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.smoke_main
def test_elements_click(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com")
    main_page.element_main.click()
    assert main_page.current_url() == 'https://demoqa.com/elements', 'Ссылка другая!'

@pytest.mark.smoke_main
def test_forms_click(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com")
    main_page.scroll_to_element_forms
    main_page.forms_main.click()
    assert main_page.current_url() == 'https://demoqa.com/forms', 'Ссылка другая!'

@pytest.mark.smoke_main
def test_alerts_click(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com")
    main_page.alerts_main.click()
    assert main_page.current_url() == 'https://demoqa.com/alertsWindows', 'Ссылка другая!'

@pytest.mark.smoke_main
def test_widgets_click(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com")
    main_page.widgets_main.click()
    assert main_page.current_url() == 'https://demoqa.com/widgets', 'Ссылка другая!'    

@pytest.mark.smoke_main
def test_interactions_click(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com")
    main_page.interactions_main.click()
    assert main_page.current_url() == 'https://demoqa.com/interaction', 'Ссылка другая!'   

@pytest.mark.smoke_main
def test_book_click(driver):
    main_page = MainPage(driver)
    main_page.open("https://demoqa.com")
    main_page.book_main.click()
    assert main_page.current_url() == 'https://demoqa.com/books', 'Ссылка другая!'   













