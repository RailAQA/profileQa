from pages.elements_page import ElementsPage
import pytest

# Проверяем кликабельность субменю у Elements
@pytest.mark.smoke_elements
def test_textbox_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open("https://demoqa.com/elements")
    elements_page.textbox_in_elements_menu_click()

@pytest.mark.smoke_elements
def test_checkbox_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open("https://demoqa.com/elements")
    elements_page.textbox_in_elements_menu_click()   
    
@pytest.mark.smoke_elements    
def test_radiobutton_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.radiobutton_in_elements_menu_click()

@pytest.mark.smoke_elements 
def test_webtables_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.webtables_in_elements_menu_click()

@pytest.mark.smoke_elements 
def test_buttons_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.buttons_in_elements_menu_click()

@pytest.mark.smoke_elements 
def test_links_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.links_in_elements_menu_click()

@pytest.mark.smoke_elements 
def test_brokenlinks_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.brokenlinks_in_elements_menu_click()

@pytest.mark.smoke_elements 
def test_uploaddownload_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.upload_in_elements_menu_click()

@pytest.mark.smoke_elements 
def test_dynamic_submenu_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open('https://demoqa.com/elements')
    elements_page.dynamic_in_elements_menu_click()
