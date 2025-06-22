from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# Локаторы страницы elements_page:

ELEMENTS_MENU_BUTTON = (By.XPATH, "//div[text()='Elements']")
FORMS_MENU_BUTTON = (By.XPATH, "//div[text()='Forms']")
ALERTS_MENU_BUTTON = (By.XPATH, "//div[text()='Alerts, Frame & Windows']")
WIDGET_MENU_BUTTON = (By.XPATH, "//div[text()='Widgets']")
INTERACTIONS_MENU_BUTTON = (By.XPATH, "//div[text()='Interactions']")
BOOK_MENU_BUTTON = (By.XPATH, "//div[text()='Book Store Application']")

#Подменю у раздела Elements
TEXT_BOX_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-0"]//span[text()="Text Box"]')
CHECK_BOX_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-1"]//span[text()="Check Box"]')
RADIO_BUTTON_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-2"]//span[text()="Radio Button"]')
WEB_TABLES_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-3"]//span[text()="Web Tables"]')
BUTTONS_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-4"]//span[text()="Buttons"]')
LINKS_SUBMENU_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-5"]//span[text()="Links"]')
BROKEN_LINKS_SUBMENU_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-6"]//span[text()="Broken Links - Images"]')
UPLOAD_AN_DOWNLOAD_SUBMENU_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-7"]//span[text()="Upload and Download"]')
DYNAMIC_PROPERTIES_SUBMENU_IN_ELEMENTS_MENU = (By.XPATH, '//ul[@class="menu-list"]//li[@id="item-8"]//span[text()="Dynamic Properties"]')


class ElementsPage(BasePage):
    # Поиск элементов меню
    @property
    def elements_menu(self):
        return self.find(ELEMENTS_MENU_BUTTON)
    
    @property
    def forms_menu(self):
        return self.find(FORMS_MENU_BUTTON)
    
    @property
    def alerts_menu(self):
        return self.find(ALERTS_MENU_BUTTON)
    
    @property
    def widget_menu(self):
        return self.find(WIDGET_MENU_BUTTON)
    
    @property
    def interactions_menu(self):
        return self.find(INTERACTIONS_MENU_BUTTON)
    
    @property
    def book_menu(self):
        return self.find(BOOK_MENU_BUTTON)
    
    # Клик по элементам подменю раздела Elements
    def textbox_in_elements_menu_click(self):
        self.find(TEXT_BOX_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/text-box", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/text-box"'

    def checkbox_in_elements_menu_click(self):
        self.find(CHECK_BOX_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/checkbox", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/checkbox"'

    def radiobutton_in_elements_menu_click(self):
        self.find(RADIO_BUTTON_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/radio-button"'

    def webtables_in_elements_menu_click(self):
        self.find(WEB_TABLES_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/webtables"'

    def buttons_in_elements_menu_click(self):
        self.find(BUTTONS_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/buttons"'

    def links_in_elements_menu_click(self):
        self.find(LINKS_SUBMENU_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/links"'

    def brokenlinks_in_elements_menu_click(self):
        self.find(BROKEN_LINKS_SUBMENU_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/broken"'

    def upload_in_elements_menu_click(self):
        self.find(UPLOAD_AN_DOWNLOAD_SUBMENU_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/upload-download"'

    def dynamic_in_elements_menu_click(self):
        self.find(DYNAMIC_PROPERTIES_SUBMENU_IN_ELEMENTS_MENU).click()
        assert self.current_url() == "https://demoqa.com/radio-button", f'[elements_page] Открылась страница {self.current_url()}, а должна "https://demoqa.com/dynamic-properties"'

    

    