from pages.base_page import BasePage
from locators.footer_element_locators import FooterLocators
from selenium.webdriver.common.by import By
locators = FooterLocators()


class FooterElement(BasePage):

    def scroll_to_footer(self):
        self.go_to_element_center(element=self.find(locators.FOOTER_CONTAINER))
        self.element_is_visible(locators.FOOTER_CONTAINER, 20)

    def logo_in_footer_check(self):
        self.element_is_visible(locators.FOOTER_LOGO, 20)

    def contacts_button_check(self):
        self.element_is_clickable(locators.FOOTER_CONTACTS_BUTTON, 20)

    def terms_privacy_button_check(self):
        self.element_is_clickable(locators.FOOTER_TERMS_PRIVACY_BUTTON, 20)

    def vk_button_check(self):
        self.element_is_clickable(locators.FOOTER_VK_SOCIAL_BUTTON, 20)

    def tg_button_check(self):
        self.element_is_clickable(locators.FOOTER_TELEGRAM_SOCIAL_BUTTON, 20)