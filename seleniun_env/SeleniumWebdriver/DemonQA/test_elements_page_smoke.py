from pages.elements_page import ElementsPage
import pytest

@pytest.mark.smoke_elements
def test_textbox_elements_click(driver):
    elements_page = ElementsPage(driver)
    elements_page.open("https://demoqa.com/elements")
    elements_page.textbox_in_elements_menu_click()