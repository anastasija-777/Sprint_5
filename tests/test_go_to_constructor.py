import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import TestLocators


class TestConstructor:

    # проверяем переход по клику на «Конструктор»
    def test_go_to_constructor_button(self, driver,log_in):
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидаем загрузки страницы Профиль
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LOCATOR))
        # кликаем по кнопке Конструктор
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR_LOCATOR).click()
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        assert driver.current_url == Constants.URL

    # проверяем переход по клику на логотип Stellar Burgers
    def test_go_to_constructor_logo(self, driver,log_in):
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидаем загрузки страницы Профиль
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LOCATOR))
        # кликаем по логотипу Stellar Burgers
        driver.find_element(*TestLocators.LOGO_STELLAR_BURGER_LOCATOR).click()
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        assert driver.current_url == Constants.URL