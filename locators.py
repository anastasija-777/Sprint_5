import pytest
from selenium.webdriver.common.by import By

class TestLocators:
    PERSONAL_ACCOUNT_LOCATOR = By.XPATH,'.//p[text()="Личный Кабинет"]'  # кнопка Личный кабинет
    LINK_REGISTER_LOCATOR = By.XPATH,'.//a[text()="Зарегистрироваться"]'  # кликабельная ссылка Зарегистрироваться
    REGISTER_NAME_LOCATOR = By.XPATH,'.//fieldset[1]//input[@name="name"]'   # поле Имя в форме регистрации
    REGISTER_EMAIL_LOCATOR = By.XPATH,'.//fieldset[2]//input[@name="name"]'   # поле Email в форме регистрации
    REGISTER_PASSWORD_LOCATOR = By.XPATH,'.//fieldset[3]//input[@name="Пароль"]'   # поле Пароль в форме регистрации
    BUTTON_REGISTER_LOCATOR = By.XPATH,'.//button[text()="Зарегистрироваться"]'  # кнопка Зарегистрироваться в форме регистрации
    TEXT_LOGIN_LOCATOR = By.XPATH,'.//h2[text()="Вход"]'  # надпись Вход в форме авторизации

    AUTHORIZATION_EMAIL_LOCATOR = By.XPATH,'.//form//input[@name="name"]'  # поле Email в форме авторизации
    AUTHORIZATION_PASSWORD_LOCATOR = By.NAME, "Пароль"   # поле Пароль в форме авторизации
    BUTTON_LOGIN_LOCATOR = By.XPATH, ".//button[text()='Войти']"  # кнопка Войти в форме авторизации
    PROFILE_LOCATOR = By.XPATH, ".//a[text()='Профиль']" # раздел Профиль
    NAME_PROFILE_LOCATOR = By.NAME, "Name"  # поле с именем в Профиле
    ERROR_PASSWORD_LOCATOR = By.XPATH,'.//fieldset[3]//p[text()="Некорректный пароль"]'  # текст ошибки при вводе невалидного значения в поле Пароль
    BUTTON_LOG_IN_TO_YOAR_ACCOUNT_LOCATOR = By.XPATH,'.//button[text()="Войти в аккаунт"]'  # кнопка Войти в аккаунт на главной
    LINK_RECOVER_PASSWORD_LOCATOR = By.XPATH,'.//a[text()="Восстановить пароль"]'  # кликабельная ссылка Восстановить пароль
    LINK_LOGIN_LOCATOR = By.XPATH,'.//a[text()="Войти"]'   # кликабельная ссылка Войти пароль
    BUTTON_CONSTRUCTOR_LOCATOR = By.XPATH,'.//p[text()="Конструктор"]'   # кнопка Конструктор на странице Личного кабинета
    LOGO_STELLAR_BURGER_LOCATOR = By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]'  # логотип Stellar Burgers
    TEXT_ASSEMBLE_BURGER_LOCATOR = By.XPATH,'.//h1[text()="Соберите бургер"]'   # заголовок Соберите бургер
    BUTTON_LOGOUT_LOCATOR = By.XPATH,'.//button[text()="Выход"]'  # кнопка Выход
    BUTTON_SAUCES_LOCATOR = By.XPATH,'.//span[text()="Соусы"]'  # кнопка Соусы
    TEXT_SAUCES_LOCATOR = By.XPATH,'.//h2[text()="Соусы"]'  # заголовок Соусы
    BUTTON_FILLINGS_LOCATOR = By.XPATH, './/span[text()="Начинки"]'  # кнопка Начинки
    TEXT_FILLINGS_LOCATOR = By.XPATH, './/h2[text()="Начинки"]'  # заголовок Начинки
    BUTTON_BUNS_LOCATOR = By.XPATH, './/span[text()="Булки"]'  # кнопка Булки
    TEXT_BUNS_LOCATOR = By.XPATH, './/h2[text()="Булки"]'  # заголовок Булки
