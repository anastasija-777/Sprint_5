import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import TestLocators
from test_data import TestData

class TestButtonsAuthorization:
    # проверяем вход по кнопке «Войти в аккаунт» на главной
    def test_button_log_in_to_your_account(self, driver):
        driver.get(Constants.URL)
        # ожидание загрузки страницы когда кнопка Войти в аккаунт будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOG_IN_TO_YOAR_ACCOUNT_LOCATOR))
        # кликнуть по кнопке войти в аккаунт
        driver.find_element(*TestLocators.BUTTON_LOG_IN_TO_YOAR_ACCOUNT_LOCATOR).click()
        assert driver.current_url == Constants.URL_LOGIN

    # проверяем вход через кнопку «Личный кабинет»
    def test_button_personal_account(self, driver):
        driver.get(Constants.URL)
        # ожидание загрузки страницы когда кнопка Личный кабинет будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_LOCATOR))
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        assert driver.current_url == Constants.URL_LOGIN

    # проверяем вход через кнопку в форме регистрации
    def test_button_registration_form(self, driver):
        driver.get(Constants.URL)
        # ожидание загрузки страницы когда кнопка Личный кабинет будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_LOCATOR))
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
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
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидаем загрузки страницы Профиль
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LOCATOR))
        # проверяем что имя в профиле соответствует имени указанном при регистрации
        name = driver.find_element(*TestLocators.NAME_PROFILE_LOCATOR).get_attribute('value')
        assert name == 'Гарри Поттер'

    # проверяем вход через кнопку в форме восстановления пароля
    def test_button_in_password_recovery_form(self, driver):
        driver.get(Constants.URL)
        # ожидание загрузки страницы когда кнопка Личный кабинет будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_LOCATOR))
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидание загрузки страницы когда ссылка Восстановить пароль будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_RECOVER_PASSWORD_LOCATOR))
        # кликаем по кликабельной ссылке Восстановить пароль
        driver.find_element(*TestLocators.LINK_RECOVER_PASSWORD_LOCATOR).click()
        # ожидание загрузки страницы когда ссылка Войти будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LINK_LOGIN_LOCATOR))
        # кликаем по кликабельной ссылке Войти пароль
        driver.find_element(*TestLocators.LINK_LOGIN_LOCATOR).click()
        assert driver.current_url == Constants.URL_LOGIN

