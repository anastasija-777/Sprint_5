import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import TestLocators


class TestButtonPersonalAccount:

    # проверяем переход по клику на «Личный кабинет»
    def test_go_to_personal_account(self, driver,log_in):
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидаем загрузки страницы Профиль
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_LOCATOR))
        assert driver.current_url == Constants.URL_PERSONAL_ACCOUNT