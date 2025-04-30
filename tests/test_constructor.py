import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import Constants
from locators import TestLocators
from test_data import TestData

class TestConstructorSauces:
    # переход к разделу Соусы по кнопке Соусы
    def test_transition_to_sauces_button(self, driver):
        driver.get(Constants.URL)
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        # кликнуть по кнопке Соусы
        driver.find_element(*TestLocators.BUTTON_SAUCES_LOCATOR).click()
        # проверяем что заголовок Соусы виден на странице
        element_visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_SAUCES_LOCATOR))
        assert element_visible

    # переход к разделу Соусы с помощью скролла
    def test_transition_to_sauces_scroll(self, driver):
        driver.get(Constants.URL)
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        # скроллим до заголовка Соусы
        element = driver.find_element(*TestLocators.TEXT_SAUCES_LOCATOR)
        driver.execute_script("arguments[0].scrollIntoView()",element)
        # проверяем что заголовок Соусы виден на странице
        element_visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_SAUCES_LOCATOR))
        assert element_visible

class TestConstructorFillings:
    # переход к разделу Начинки по кнопке Начинки
    def test_transition_to_fillings_button(self, driver):
        driver.get(Constants.URL)
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        # кликнуть по кнопке Начинки
        driver.find_element(*TestLocators.BUTTON_FILLINGS_LOCATOR).click()
        # проверяем что заголовок Начинки виден на странице
        element_visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_FILLINGS_LOCATOR))
        assert element_visible

    # переход к разделу Начинки с помощью скролла
    def test_transition_to_fillings_scroll(self, driver):
        driver.get(Constants.URL)
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        # скроллим до заголовка Начинки
        element = driver.find_element(*TestLocators.TEXT_FILLINGS_LOCATOR)
        driver.execute_script("arguments[0].scrollIntoView()",element)
        # проверяем что заголовок Начинки виден на странице
        element_visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_FILLINGS_LOCATOR))
        assert element_visible

class TestConstructorBuns:
    # переход к разделу Булки по кнопке Булки
    def test_transition_to_buns_button(self, driver):
        driver.get(Constants.URL)
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        # кликнуть по кнопке Соусы
        driver.find_element(*TestLocators.BUTTON_SAUCES_LOCATOR).click()
        # проверяем что заголовок Соусы виден на странице
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_SAUCES_LOCATOR))
        # кликнуть по кнопке Булки
        driver.find_element(*TestLocators.BUTTON_BUNS_LOCATOR).click()
        # проверяем что заголовок Булки виден на странице
        element_visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_BUNS_LOCATOR))
        assert element_visible

    # переход к разделу Булки с помощью скролла
    def test_transition_to_buns_scroll(self, driver):
        driver.get(Constants.URL)
        # ожидаем загрузки страницы до надписи Соберите бургер
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_ASSEMBLE_BURGER_LOCATOR))
        # кликнуть по кнопке Соусы
        driver.find_element(*TestLocators.BUTTON_SAUCES_LOCATOR).click()
        # проверяем что заголовок Соусы виден на странице
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_SAUCES_LOCATOR))
        # скроллим до заголовка Булки
        element = driver.find_element(*TestLocators.TEXT_BUNS_LOCATOR)
        driver.execute_script("arguments[0].scrollIntoView()",element)
        # проверяем что заголовок Булки виден на странице
        element_visible = WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_BUNS_LOCATOR))
        assert element_visible