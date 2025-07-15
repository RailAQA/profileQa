from selenium.webdriver.common.by import By


class HeaderElementLocators:
    """Содержит локаторы для элементов header."""

    # Контейнер шапки
    HEADER_CONTAINER = (By.XPATH, "//div[@class='header-module-scss-module__VETcYq__all']//header[@class='header-module-scss-module__VETcYq__container']")

    # Элементы поиска
    SEARCH_ICON = (By.XPATH, "//img[@alt='search ico']")
    SEARCH_INPUT = (By.XPATH, "//input[@data-testid='Search: input']")
    SEARCH_RESULTS_CONTAINER = (By.XPATH, "//div[@data-testid='Search: found']")
    SEARCH_FOUND_ANIME = (By.XPATH, "//div[class='header-module-scss-module__VETcYq__found-anime display_c329783a-module__gcoslG__className']")
    SEARCH_RESULTS_ANIME = (By.XPATH, '//div[@class="header-module-scss-module__VETcYq__found-anime display_88187f1d-module__s6es1G__className"]//a')

    # Лоадер
    LOADER = (By.XPATH, "//div[@class='header-module-scss-module__VETcYq__loader']")



    # Элементы профиля пользователя
    USER_PROFILE_LINK = (By.XPATH, "//a[@class='header-module-scss-module__VETcYq__user-container']")
    USER_ICON = (By.XPATH, "//img[@alt='user ico']")
    USER_NAME = (By.XPATH, "//h1[@class='header-module-scss-module__VETcYq__user-text']")

    YOUR_PREFERENCES_CONTAINER = (By.XPATH, '//div[@class="home-module-scss-module__jf9uCq__container"]//div[@class="recomendations-module-scss-module__Yj0dZa__container"]')
    NOW_IN_TREND_CONTAINER = (By.XPATH, '//div[@class="home-module-scss-module__jf9uCq__container"]//div[@class="w-full flex flex-col gap-4 text-2xl"][1]')


    # Для мобилки

    BURGER_MENU_BUTTON = (By.XPATH, '//button[@class="burger-menu-module-scss-module__-REZYq__btn"]')
    SEARCH_INPUT_MOB = (By.XPATH, '//input[@data-testid="Search: input"]')