import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constants import Constants
from test_data import TestData

@pytest.fixture(scope='function')  # фикстура создающая отдельный экземпляр драйвера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')  # фикстура для перехода с главной страницы к форме регистрации
def go_to_registration_form(driver):
    # открываем в браузере главную страницу сайта
    driver.get(Constants.URL)
    # ожидание загрузки страницы когда кнопка Личный кабинет будет кликабельна
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_LOCATOR))
    # кликаем по кнопке Личный кабинет
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
    # ожидание загрузки страницы когда ссылка Зарегистрироваться будет кликабельна
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_REGISTER_LOCATOR))
    # кликаем по кликабельной ссылке Зарегистрироваться
    driver.find_element(*TestLocators.LINK_REGISTER_LOCATOR).click()
    # ожидание загрузки страницы когда поле Имя формы будет видно
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTER_NAME_LOCATOR))

@pytest.fixture(scope='function')  # фикстура для входа в аккаунт авторизированного пользователя
def log_in(driver):
    driver.get(Constants.URL)
    # ожидание загрузки страницы когда кнопка Войти в аккаунт будет кликабельна
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOG_IN_TO_YOAR_ACCOUNT_LOCATOR))
    # кликнуть по кнопке войти в аккаунт
    driver.find_element(*TestLocators.BUTTON_LOG_IN_TO_YOAR_ACCOUNT_LOCATOR).click()
    # ожидаем загрузки страницы с формой авторизации до появления надписи Вход
    WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTER_NAME_LOCATOR))
    # заполняем поле Email
    driver.find_element(*TestLocators.AUTHORIZATION_EMAIL_LOCATOR).click()
    driver.find_element(*TestLocators.AUTHORIZATION_EMAIL_LOCATOR).send_keys(TestData.email)
    # заполняем поле Пароль
    driver.find_element(*TestLocators.AUTHORIZATION_PASSWORD_LOCATOR).send_keys(TestData.password)
    # кликаем по кнопке Войти
    driver.find_element(*TestLocators.BUTTON_LOGIN_LOCATOR).click()
    # ожидание загрузки страницы когда кнопка Личный кабинет будет кликабельна
    WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_LOCATOR))

