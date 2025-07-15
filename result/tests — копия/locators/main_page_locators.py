from selenium.webdriver.common.by import By


class MainPageLocators:
    """Содержит локаторы для элементов страницы main_page."""

    # Блок с подборкой "По вашим предпочтениям"
    YOUR_PREFERENCES_CONTAINER = (By.XPATH, '//div[@class="home-module-scss-module__jf9uCq__container"]//div[@class="recomendations-module-scss-module__Yj0dZa__container"]')

    # Кнопки навигации в блоке с подборкой "По вашим предпочтениям"
    YOUR_PREFERENCES_CAROUSEL_BACK_BUTTON = (By.XPATH, '//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//button[1]')
    YOUR_PREFERENCES_CAROUSEL_NEXT_BUTTON = (By.XPATH, '//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//button[2]')

    # Слайды в блоке "По вашим предпочтениям"
    YOUR_PREFERENCES_CAROUSEL_SLIDE_ALL = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_1 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][1]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_2 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][2]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_3 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][3]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_4 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][4]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_5 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][5]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_6 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][6]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_7 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][7]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_8 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][8]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_9 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][9]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_10 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][10]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_11 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][11]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_12 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][12]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_13 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][13]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_14 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][14]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_15 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][15]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_16 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][16]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_17 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][17]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_18 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][18]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_19 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][19]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_20 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][20]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_21 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][21]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_22 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][22]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_23 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][23]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_24 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][24]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_25 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][25]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_26 = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][26]')
    YOUR_PREFERENCES_CAROUSEL_SLIDE_5_click = (By.XPATH, '//div[@class="recomendations-module-scss-module__Yj0dZa__container"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][5]//a[@class="anime-card-module-scss-module__z8WVqq__container"]//div[2]')



    # Блок с подборкой "Сейчас в тренде"
    NOW_IN_TREND_CONTAINER = (By.XPATH, '//div[@class="home-module-scss-module__jf9uCq__container"]//div[@class="w-full flex flex-col gap-4 text-2xl"][1]')
    NOW_IN_TREND_ALL_SLIDES = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"]')

    # Кнопки в блоке с подборкой "Сейчас в тренде"
    NOW_IN_TREND_BACK_BUTTON = (By.XPATH, '//div[@class="w-full flex flex-col gap-4 text-2xl"][1]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//button[1]')
    NOW_IN_TREND_NEXT_BUTTON = (By.XPATH, '//div[@class="w-full flex flex-col gap-4 text-2xl"][1]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//button[2]')

    # Слайды в блоке "Сейчас в тренде"
    NOW_IN_TREND_CAROUSEL_SLIDE_1 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][1]')
    NOW_IN_TREND_CAROUSEL_SLIDE_2 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][2]')
    NOW_IN_TREND_CAROUSEL_SLIDE_3 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][3]')
    NOW_IN_TREND_CAROUSEL_SLIDE_4 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][4]')
    NOW_IN_TREND_CAROUSEL_SLIDE_5 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][5]')
    NOW_IN_TREND_CAROUSEL_SLIDE_6 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][6]')
    NOW_IN_TREND_CAROUSEL_SLIDE_7 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][7]')
    NOW_IN_TREND_CAROUSEL_SLIDE_8 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][8]')
    NOW_IN_TREND_CAROUSEL_SLIDE_9 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][9]')
    NOW_IN_TREND_CAROUSEL_SLIDE_10 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][10]')
    NOW_IN_TREND_CAROUSEL_SLIDE_11 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][11]')
    NOW_IN_TREND_CAROUSEL_SLIDE_12 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][12]')
    NOW_IN_TREND_CAROUSEL_SLIDE_13 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][13]')
    NOW_IN_TREND_CAROUSEL_SLIDE_14 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][14]')
    NOW_IN_TREND_CAROUSEL_SLIDE_15 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][15]')
    NOW_IN_TREND_CAROUSEL_SLIDE_16 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][16]')
    NOW_IN_TREND_CAROUSEL_SLIDE_17 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][17]')
    NOW_IN_TREND_CAROUSEL_SLIDE_18 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][18]')
    NOW_IN_TREND_CAROUSEL_SLIDE_19 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][19]')
    NOW_IN_TREND_CAROUSEL_SLIDE_20 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][20]')
    NOW_IN_TREND_CAROUSEL_SLIDE_21 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][21]')
    NOW_IN_TREND_CAROUSEL_SLIDE_22 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][22]')
    NOW_IN_TREND_CAROUSEL_SLIDE_23 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][23]')
    NOW_IN_TREND_CAROUSEL_SLIDE_24 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][24]')
    NOW_IN_TREND_CAROUSEL_SLIDE_25 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][25]')
    NOW_IN_TREND_CAROUSEL_SLIDE_26 = (By.XPATH, '//div[text()="Сейчас в тренде"]//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@class="carousel-module-scss-module__A4KUIq__anime-slide"][26]')

    # Общий локатор для любого слайда (динамический) А нужно ли?)
    #NOW_IN_TREND_CAROUSEL_SLIDE_BY_INDEX = (By.XPATH, '//div[@class="carousel-module-scss-module__A4KUIq__anime-carousel"]//div[@data-testid="Carousel: card"][{}]')



    # Блок с банерами "Переходите к нам в тг"
    BANNER_MAIN_SLIDE_CONTAINER = (By.XPATH, '//div[@class="banners-showing-module-scss-module__cgoiWq__container"]')
    BANNER_MAIN_SLIDE_ALL = (By.XPATH, '//div[@class="banners-showing-module-scss-module__cgoiWq__container"]//img')
    BANNER_MAIN_SLIDE_1 = (By.XPATH, '//div[@class="banners-showing-module-scss-module__cgoiWq__container"]//img[@alt="banner 1"]')
    BANNER_MAIN_SLIDE_2 = (By.XPATH, '//div[@class="banners-showing-module-scss-module__cgoiWq__container"]//img[@alt="banner 2"]')
    BANNER_MAIN_SLIDE_3 = (By.XPATH, '//div[@class="banners-showing-module-scss-module__cgoiWq__container"]//img[@alt="banner 3"]')
    BANNER_MAIN_SLIDE_4 = (By.XPATH, '//div[@class="banners-showing-module-scss-module__cgoiWq__container"]//img[@alt="banner 4"]')

    # Пагинация(кнопки) в блоке с банерами "Переходите к нам в тг"
    PAGINATION_BANNER_MAIN_BUTTON_ALL = (By.XPATH, '//ul[@class="banners-showing-module-scss-module__cgoiWq__list"]//button')
    PAGINATION_BANNER_MAIN_BUTTON_1 = (By.XPATH, '//ul[@class="banners-showing-module-scss-module__cgoiWq__list"]//button[1]')
    PAGINATION_BANNER_MAIN_BUTTON_2 = (By.XPATH, '//ul[@class="banners-showing-module-scss-module__cgoiWq__list"]//button[2]')
    PAGINATION_BANNER_MAIN_BUTTON_3 = (By.XPATH, '//ul[@class="banners-showing-module-scss-module__cgoiWq__list"]//button[3]')
    PAGINATION_BANNER_MAIN_BUTTON_4 = (By.XPATH, '//ul[@class="banners-showing-module-scss-module__cgoiWq__list"]//button[4]')



    # Блок с подборкой "Новинки"
    NEW_ANIME_CONTAINER = (By.XPATH, '//div[@class="w-full flex flex-col gap-4 text-2xl"][2]')

    # Кнопки в блоке с подборкой "Новинки"
    NEW_ANIME_BACK_BUTTON = (By.XPATH, '')
    NEW_ANIME_NEXT_BUTTON = (By.XPATH, '')
    NEW_ANIME_MORE_BUTTON = (By.XPATH, "//button[text()='Показать всё']")

    # Слайды в блоке "Новинки"
    NEW_ANIME_BLOCK_SLIDE_ALL = (By.XPATH, '//div[@class="news-show-module-scss-module__0dpS2W__content"]//a')
    NEW_ANIME_BLOCK_SLIDE_5 = (By.XPATH, '//div[@class="news-show-module-scss-module__0dpS2W__content"]//a[5]')

    # Общий локатор для любого слайда (динамический)
    NEW_ANIME_CAROUSEL_SLIDE_BY_INDEX = (By.XPATH, '')



    # Кнопка "Показать все"
    SHOW_ALL_BUTTON = (By.XPATH, "//button[text()='Показать всё']")

