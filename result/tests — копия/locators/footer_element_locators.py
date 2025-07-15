from selenium.webdriver.common.by import By


class FooterLocators:
    """Содержит локаторы для элементов footer."""

    # Контейнер футера
    FOOTER_CONTAINER = (By.XPATH, '//footer[@class="footer-module-scss-module__twNBtW__container"]')

    # Лого футера
    FOOTER_LOGO = (By.XPATH, '//div[@class="footer-module-scss-module__twNBtW__left"]//img[@alt="Cine Network"]')

    # Кнопка "Telegram" в футере
    FOOTER_TELEGRAM_SOCIAL_BUTTON = (By.XPATH, '//div[@class="footer-module-scss-module__twNBtW__right"]//img[@alt="Telegramlogo"]')

    # Кнопка "VK" в футере
    FOOTER_VK_SOCIAL_BUTTON = (By.XPATH, '//div[@class="footer-module-scss-module__twNBtW__right"]//img[@alt="VKlogo"]')

    # Кнопка "Contacts" в футере
    FOOTER_CONTACTS_BUTTON = (By.XPATH, "//div[@class='footer-module-scss-module__twNBtW__left-links']//a[text()='Contacts']")

    # Кнопка "Terms & Privacy" в футере
    FOOTER_TERMS_PRIVACY_BUTTON = (By.XPATH, "//div[@class='footer-module-scss-module__twNBtW__left-links']//a[text()='Terms & Privacy']")
