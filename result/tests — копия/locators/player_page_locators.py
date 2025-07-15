from selenium.webdriver.common.by import By


class PlayerLocators:
    """Локаторы для страницы Player"""
   
    # Блок эпизоды v
    EPISODER_CONTAINER = (By.XPATH, '//div[@class="player-episode-module-scss-module__n-2UrW__container"]//div[@class="player-episode-module-scss-module__n-2UrW__body"]')
    EPISODES_H2 = (By.XPATH, '//div[@class="player-episode-module-scss-module__n-2UrW__body"]//h2[text()="Эпизоды:"]')
    EPIDODES_SERIES_ALL = (By.XPATH, '//div[@class="player-episode-module-scss-module__n-2UrW__episodes"]//div')

    # Блок с названием ---
    ARTICLE_CONTAINER = (By.XPATH, '//div[@class="player-module-scss-module__ecoPna__article"]')
    NAME_ANIME = (By.XPATH, '//h2[@class="player-module-scss-module__ecoPna__title"]')
    NUMBER_SERIES = (By.XPATH, '//h3[@class="player-module-scss-module__ecoPna__subtitle"]')
    LIKE_BUTTON_ANIME = (By.XPATH, '//div[@class="player-aside-module-scss-module__fAYBZa__span"]//button[@id="like"]//div')
    COUNT_LIKES_ANIME = (By.XPATH, '//div[@class="player-aside-module-scss-module__fAYBZa__span"][1]//p[@class="w-3"]')
    DISLIKE_BUTTON_ANIME = (By.XPATH, '//div[@class="player-aside-module-scss-module__fAYBZa__span"]//button[@id="dislike"]//div')
    COUNT_DISLIKES_ANIME = (By.XPATH, '//div[@class="player-aside-module-scss-module__fAYBZa__span"][2]//p[@class="w-3"]')
    SHARE_BUTTON_ANIME = (By.XPATH, '//div[@class="player-aside-module-scss-module__fAYBZa__buttons"]//button[text()="Поделиться"]')
    
    GETMORE_BUTTON_ANIME = (By.XPATH, '//div[@class="player-aside-module-scss-module__fAYBZa__getmore"]//button')
    GETMORE_POP_UP = (By.XPATH, '//div[@id="headlessui-popover-panel-«R5ekivf9nl7»"]')
    REPORT_BUTTON_ANIME = (By.XPATH, '//div[@id="headlessui-popover-panel-«R5ekivf9nl7»"]//button[text()="Пожаловаться"]')
    REPORT_WINDOW_ANIME_BUTTONS_ALL = (By.XPATH, '//div[@class="popup-module-scss-module__VIQHUW__panel"]//div[@class="complain-popup-module-scss-module__XG6Idq__complains"]//div[@class="complain-popup-module-scss-module__XG6Idq__complain"]')

    REPORT_WINDOW_CONTAINER = (By.XPATH, '//div[@class="popup-module-scss-module__VIQHUW__backdrop"]//div[@class="popup-module-scss-module__VIQHUW__panel"]')
    TEXTAREA_REPORT_WINDOW = (By.XPATH, '//div[@class="textarea-module-scss-module__WbmcLa__field"]//textarea')
    SEND_FORM_BUTTON_REPORT_WINDOW = (By.XPATH, '//button[text()="Отправить"]')
    CLOSE_FORM_REPORT_BUTTON = (By.XPATH, '//button[@class="popup-module-scss-module__VIQHUW__union"]')

    # Блок комментарий ---
    COMMENT_CONTAINER = (By.XPATH, '//div[@class="player-module-scss-module__ecoPna__comments-fullscreen"]//div[@class="comment-module-scss-module__NcIP4q__container"]')
    WRITE_COMMENT_BUTTON_ANIME = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//button[@style="line-height:23px;opacity:100%;font-size:18px;padding-left:24px;padding-right:24px;padding-bottom:14px;padding-top:14px;font-weight:400"]')
    
    # Модальное окно написания коммента ---
    MODAL_TABLE_COMMENT = (By.XPATH, '//div[@class="popup-module-scss-module__VIQHUW__panel"]')
    CLOSE_MODAL_BUTTON = (By.XPATH, '//div[@class="popup-module-scss-module__VIQHUW__header"]//button[@class="popup-module-scss-module__VIQHUW__union"]')
    STARS_ALL_SVG = (By.XPATH, '//*[local-name()="svg"][@viewBox="0 0 24 24"]')
    TEXTAREA_COMMENT = (By.XPATH, '//textarea[@placeholder="Напишите свой текст"]')
    CHECKBOX_COMMENT = (By.XPATH, '//span[@role="checkbox"]')
    CHECKBOX_OK_IMAGE_COMMENT = (By.CLASS_NAME, 'checkbox-module-scss-module__hSlm0a__checkIcon')
    SEND_COMMENT_BUTTON = (By.XPATH, '//button[text()="Отправить"]')
    TEXTAREA_VALUE = (By.CSS_SELECTOR, '[contenteditable="plaintext-only"]')
    
    # Комменты ---
    ALL_COMMENTS = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//div[@class="comment-module-scss-module__NcIP4q__wrapper"]')
    REPLY_COMMENT_BUTTON_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//div[@class="comment-module-scss-module__NcIP4q__wrapper"]//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//h1[text()="Ответить"]')
    COUNT_LIKES_COMMENT_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//div[@class="comment-module-scss-module__NcIP4q__wrapper"]//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//div[@class="comment-module-scss-module__NcIP4q__likes"]//h1[@class="comment-module-scss-module__NcIP4q__likes-text"]')
    LIKE_BUTTON_COMMENT_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//div[@class="comment-module-scss-module__NcIP4q__wrapper"]//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//div[@class="comment-module-scss-module__NcIP4q__likes"]//button[@id="like"]')
    DISLIKE_BUTTON_COMMENT_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//div[@class="comment-module-scss-module__NcIP4q__wrapper"]//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//div[@class="comment-module-scss-module__NcIP4q__likes"]//button[@id="dislike"]')
    GET_MORE_BUTTON_COMMENT_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__container"]//div[@class="comment-module-scss-module__NcIP4q__wrapper"]//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__under-title"]//div[@class="comment-module-scss-module__NcIP4q__tooltip-button"]//button')
    POP_UP_GET_MORE_COMMENT_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__tooltip"]')
    
    COMMENT_DELETE_BUTTON = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__tooltip"]//button[text()="Удалить"]')
    POP_UP_CONFIRM_WINDOW = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__dialog-content"]')
    CONFIRM_DELETE_BUTTON = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__dialog-content"]//button[text()="Да, я уверен"]')
    CLOSE_CONFIRM_DELETE_POP_UP = (By.XPATH, '//button[@class="comment-module-scss-module__NcIP4q__close"]')

    SHORT_COMMENT_MOBILE = (By.XPATH, '//div[@class="comments-compact-module-scss-module__y_SJKG__short-comment"]')
    COMMENT_PLAYER_MOBILE_CONTAINER = (By.XPATH, '//div[@class="comments-compact-module-scss-module__y_SJKG__content"]')

    # Подкомменты ---
    ANSWERS_COMMENT_ALL = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment comment-module-scss-module__NcIP4q__isAnswer"]')
    REPLY_COMMENT_BUTTON_IN_ANSWERS_ALL = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment comment-module-scss-module__NcIP4q__isAnswer"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//h1[text()="Ответить"]')
    COUNT_LIKES_ANWERS_ALL = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment comment-module-scss-module__NcIP4q__isAnswer"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//div[@class="comment-module-scss-module__NcIP4q__likes"]//h1[@class="comment-module-scss-module__NcIP4q__likes-text"]')
    LIKE_BUTTON_ANSWERS_ALL = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment comment-module-scss-module__NcIP4q__isAnswer"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//div[@class="comment-module-scss-module__NcIP4q__likes"]//button[@id="like"]')
    DISLIKE_BUTTON_ANSWERS_ALL = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment comment-module-scss-module__NcIP4q__isAnswer"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__footer"]//div[@class="comment-module-scss-module__NcIP4q__likes"]//button[@id="dislike"]')
    GET_MORE_BUTTON_IN_ANSWERS_ALL = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className comment-module-scss-module__NcIP4q__comment comment-module-scss-module__NcIP4q__isAnswer"]//div[@class="comment-module-scss-module__NcIP4q__content"]//div[@class="comment-module-scss-module__NcIP4q__under-title"]//div[@class="comment-module-scss-module__NcIP4q__tooltip-button"]//button')
   
    # Окошко после нажатия на кнопку get_more (универсальных для комментов и подкомментов) ---
    GET_MORE_TABLE_CONTAINER_IN_ANSWERS = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__tooltip"]')
    GET_MORE_TABLE_BUTTONS_ALL = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__tooltip"]//button[@class="comment-module-scss-module__NcIP4q__tooltip-el"]')
    GET_MORE_TABLE_ANSWERS_DELETE_BUTTON = (By.XPATH, '//div[@class="comment-module-scss-module__NcIP4q__tooltip"]//button[@class="comment-module-scss-module__NcIP4q__tooltip-del comment-module-scss-module__NcIP4q__tooltip-el"]')

    # Видеоплеер ---
    VIDEOPLAYER_CONTAINER = (By.XPATH, '//div[@aria-label="Video Player - Sprite Fight"]')
    PLAY_VIDEOPLAYER = (By.XPATH, '//button[@class="player-module-scss-module__kFWiqG__start"]')
    BOTTOM_PLAYER_CONTAINER = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__control"]')

    MINI_PLAY_BUTTON = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__side"]//button[@class="player-module-scss-module__kFWiqG__plays"]')
    MINI_SKIP_BUTTON = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__side"]//button[@class="player-module-scss-module__kFWiqG__skip"]')
    MINI_VOLUME_BUTTON = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__side"]//div[@class="player-module-scss-module__kFWiqG__volume-container"]//button[@class="player-module-scss-module__kFWiqG__volume"]')
    MINI_VOLUME_SLIDER = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__side"]//div[@class="player-module-scss-module__kFWiqG__volume-container"]//div[@class="player-module-scss-module__kFWiqG__volume-slider"]')

    PLAY_BUTTON_MOBILE = (By.XPATH, '//button[@class="player-module-scss-module__kFWiqG__mob-next-prev-play"]')
    NEXT_EPISODE_BUTTON_MOBILE = (By.XPATH, '//button[@class="player-module-scss-module__kFWiqG__mob-next-prev-btn"][1]')
    PREV_EPISODE_BUTTON_MOBILE = (By.XPATH, '//button[@class="player-module-scss-module__kFWiqG__mob-next-prev-btn"][2]')
    
    CURRENT_TIME_PLAYER = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__side"]//div[@class="player-module-scss-module__kFWiqG__time"]//div[@data-type="current"]')
    CURRENT_TIME_PLAYER = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__side"]//div[@class="player-module-scss-module__kFWiqG__time"]//div[@data-type="duration"]')
    SLIDER_TIME_PLAYING = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__control"]//div[@class="player-module-scss-module__kFWiqG__timeSlider"]')

    FULLSCREEN_BUTTON = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__buttons"]//div[@class="player-module-scss-module__kFWiqG__side flex-row-reverse"]//button[@class="player-module-scss-module__kFWiqG__fullscreen"]')
    PICTURE_IN_PICTURE_BUTONS = (By.XPATH, '//div[@class="player-module-scss-module__kFWiqG__buttons"]//div[@class="player-module-scss-module__kFWiqG__side flex-row-reverse"]//button[@class="player-module-scss-module__kFWiqG__pip"]')
    SETTINGS_BUTTON_PLAYER = (By.XPATH, '//button[@class="player-settings-module-scss-module__7PGxtW__button"]')
    SETTINGS_BUTTON_PLAYER_MOBILE = (By.XPATH, '//button[@class="player-settings-module-scss-module__UlFj6a__button"]')
    SETTINGS_WINDOW_CONTAINER = (By.XPATH, '//div[@class="display_88187f1d-module__s6es1G__className player-settings-module-scss-module__7PGxtW__panel-container animate-appear"]//div[@class="player-settings-module-scss-module__7PGxtW__panel"]')
    SETTINGS_WINDOW_CONTAINER_MOBILE = (By.XPATH, '//div[@class="player-settings-module-scss-module__UlFj6a__container"]')

    SETTINGS_BUTTONS_ALL = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]//div[@class="settings-content-module-scss-module__MUa3Yq__panel-el"]')
    AUTOPLAY_IN_SETTINGS_SWITCH_BUTTON = (By.XPATH, '//button[@id="headlessui-switch-«r1»"]')
    SETTINGS_LANGUAGE_BUTTON = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]//div[@class="settings-content-module-scss-module__MUa3Yq__panel-el"][2]')
    SETTINGS_AFTER_CLICK_WINDOW = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]')
    SETTINGS_AFTER_CLICK_H1 = (By.XPATH, '//h1[@class="settings-content-module-scss-module__MUa3Yq__backBtn-label"]')
    SETTINGS_SPEED_BUTTON = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]//div[@class="settings-content-module-scss-module__MUa3Yq__panel-el"][3]')
    SETTINGS_QUALITY_BUTTON = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]//div[@class="settings-content-module-scss-module__MUa3Yq__panel-el"][4]')
    SETTINGS_AUTO_SKIP_BUTTON = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]//div[@class="settings-content-module-scss-module__MUa3Yq__panel-el"][5]')
    
    SETTINGS_OTHER_BUTTON = (By.XPATH, '//div[@class="player-settings-module-scss-module__7PGxtW__panel"]//div[@class="settings-content-module-scss-module__MUa3Yq__panel-el"][6]')
    SETTINGS_SUBTITLE_BUTTON = (By.XPATH, '//div[@class="settings-content-module-scss-module__MUa3Yq__other"]//button[1]')
    SETTINGS_MORE_VOLUME_BUTTON = (By.XPATH, '//div[@class="settings-content-module-scss-module__MUa3Yq__other"]//button[2]')



