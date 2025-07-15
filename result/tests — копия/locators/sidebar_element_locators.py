from selenium.webdriver.common.by import By


class SideBarElementLocators:
    """Содержит локаторы для элементов sidebar."""

    # Главная, Каталог, Избранное, Коллекции
    LOGO_SIDEBAR = (By.XPATH, '//aside[@data-testid="Sidebar: block"]//a[@href="/home"]//img[@class="full:hidden"]')
    HOME_BUTTON = (By.XPATH, '//nav[@class="sidebar-module-scss-module__iYoO7W__navigation"]//a[1]')
    CATALOG_BUTTON = (By.XPATH, '//nav[@class="sidebar-module-scss-module__iYoO7W__navigation"]//a[2]')
    FAVOURITE_BUTTON = (By.XPATH, '//nav[@class="sidebar-module-scss-module__iYoO7W__navigation"]//a[3]')
    COLLECTIONS_BUTTON = (By.XPATH, '//nav[@class="sidebar-module-scss-module__iYoO7W__navigation"]//a[4]')



    # Контейнер раздела "Продолжить просмотр"
    CONTINUE_WATCHING_CONTAINER = (By.XPATH, "//div[contains(@class, 'continue-module-scss-module__gKXgja__container')]")

    # Универсальный локатор для всех кнопок на случай, если нужно работать со списком
    ALL_CONTINUE_BUTTONS = (By.XPATH, "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')]")

    # Кнопки "Продолжить просмотр" (индивидуальные, без чисел, основаны на структуре)
    FIRST_CONTINUE_BUTTON = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][.//h1[contains(@class, 'name')]][1]")
    SECOND_CONTINUE_BUTTON = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][.//h1[contains(@class, 'name')]][2]")
    THIRD_CONTINUE_BUTTON = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][.//h1[contains(@class, 'name')]][3]")

    # Элементы внутри первой кнопки
    FIRST_BUTTON_IMAGE_FULL = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][1]//img[contains(@class, 'full:block')]")
    FIRST_BUTTON_IMAGE_MOBILE = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][1]//img[contains(@class, 'full:hidden')]")
    FIRST_BUTTON_TITLE = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][1]//h1[contains(@class, 'name')]")
    FIRST_BUTTON_SERIES = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][1]//p[contains(@class, 'serias')]")

    # Элементы внутри второй кнопки
    SECOND_BUTTON_IMAGE_FULL = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][2]//img[contains(@class, 'full:block')]")
    SECOND_BUTTON_IMAGE_MOBILE = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][2]//img[contains(@class, 'full:hidden')]")
    SECOND_BUTTON_TITLE = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][2]//h1[contains(@class, 'name')]")
    SECOND_BUTTON_SERIES = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][2]//p[contains(@class, 'serias')]")

    # Элементы внутри третьей кнопки
    THIRD_BUTTON_IMAGE_FULL = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][3]//img[contains(@class, 'full:block')]")
    THIRD_BUTTON_IMAGE_MOBILE = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][3]//img[contains(@class, 'full:hidden')]")
    THIRD_BUTTON_TITLE = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][3]//h1[contains(@class, 'name')]")
    THIRD_BUTTON_SERIES = (By.XPATH,
    "//div[contains(text(), 'Продолжить просмотр')]//a[contains(@class, 'continue-link-module-scss-module')][3]//p[contains(@class, 'serias')]")

    LOGO_USER = (By.XPATH, '//a[@class="header-module-scss-module__VETcYq__user-container"]')
    BANNER_FROM_ANIME_PAGE = (By.XPATH, '//div[@class="anime-module-scss-module___fdGEa__banner"]')


                        # # # Мобилка # # # 
    
    BURGER_MENU_CONTAINER = (By.XPATH, '//div[@class="burger-menu-module-scss-module__-REZYq__content"]')
    CLOSE_BUTTON_BURGER_MENU = (By.XPATH, '//button[@class="burger-menu-module-scss-module__-REZYq__btn"]')

