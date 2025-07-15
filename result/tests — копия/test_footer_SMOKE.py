from pages.footer_element import FooterElement
import pytest

@pytest.mark.smoke_desktop
def test_logo_in_footer_visible(driver):
    """В футере есть логотип"""
    footer = FooterElement(driver)
    footer.open('http://localhost:3001/home')
    footer.scroll_to_footer()
    footer.logo_in_footer_check()

@pytest.mark.smoke_desktop
def test_contacts_button_check(driver):
    """Проверка кликабельности гиперссылки 'Контакты'."""
    footer = FooterElement(driver)
    footer.open('http://localhost:3001/home')
    footer.scroll_to_footer()
    footer.contacts_button_check()

@pytest.mark.smoke_desktop
def test_terms_privacy_button_check(driver):
    """Проверка кликабельности гиперссылки 'Terms&Privacy'."""
    footer = FooterElement(driver)
    footer.open('http://localhost:3001/home')
    footer.scroll_to_footer()
    footer.terms_privacy_button_check()

@pytest.mark.smoke_desktop
def test_vk_button_check(driver):
    """Проверка кликабельности кнопки 'ВК'."""
    footer = FooterElement(driver)
    footer.open('http://localhost:3001/home')
    footer.scroll_to_footer()
    footer.vk_button_check()

@pytest.mark.smoke_desktop
def test_tg_button_check(driver):
    """Проверка кликабельности кнопки 'ТГ'."""
    footer = FooterElement(driver)
    footer.open('http://localhost:3001/home')
    footer.scroll_to_footer()
    footer.tg_button_check()
