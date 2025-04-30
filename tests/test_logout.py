import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import TestLocators


class TestLogout:

    # проверяем что при клике по кнопке Выход происходит выход из личного кабинета
    def test_button_logout(self, driver,log_in):
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидаем загрузки страницы когда кнопка Выход станет кликабельной
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOGOUT_LOCATOR))
        # кликаем по кнопке Выход
        driver.find_element(*TestLocators.BUTTON_LOGOUT_LOCATOR).click()
        # ожидаем загрузки страницы с формой авторизации до появления надписи Вход
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_LOGIN_LOCATOR))
        assert driver.current_url == Constants.URL_LOGIN