import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from constants import Constants



class TestRegistration:
    # проверяем успешную регистрацию
    def test_successful_registration(self,driver,go_to_registration_form):
        email_address = f'HarryPotter{random.randint(10000, 99999)}@mail.com'
        random_password = f'{random.randint(100000, 999999)}'

        # заполняем поля Имя
        driver.find_element(*TestLocators.REGISTER_NAME_LOCATOR).send_keys('Гарри Поттер')
        # заполняем поле Email
        driver.find_element(*TestLocators.REGISTER_EMAIL_LOCATOR).send_keys(email_address)
        # заполняем поле Пароль
        driver.find_element(*TestLocators.REGISTER_PASSWORD_LOCATOR).send_keys(random_password)
        # кликаем по кнопке Зарегистрироваться
        driver.find_element(*TestLocators.BUTTON_REGISTER_LOCATOR).click()
        # ожидаем переход на url формы авторизации
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Constants.URL_LOGIN))
        # заполняем поле Email
        driver.find_element(*TestLocators.AUTHORIZATION_EMAIL_LOCATOR).click()
        driver.find_element(*TestLocators.AUTHORIZATION_EMAIL_LOCATOR).send_keys(email_address)
        # заполняем поле Пароль
        driver.find_element(*TestLocators.AUTHORIZATION_PASSWORD_LOCATOR).send_keys(random_password)
        driver.find_element(*TestLocators.BUTTON_LOGIN_LOCATOR).click()
        # ожидание загрузки страницы когда кнопка Личный кабинет будет кликабельна
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.PERSONAL_ACCOUNT_LOCATOR))
        # кликаем по кнопке Личный кабинет
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_LOCATOR).click()
        # ожидаем загрузки страницы Профиль
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Constants.URL_PERSONAL_ACCOUNT))
        # проверяем что имя в профиле соответствует имени указанном при регистрации
        name = driver.find_element(*TestLocators.NAME_PROFILE_LOCATOR).get_attribute('value')
        assert name == 'Гарри Поттер'

    # проверяем что выходит ошибка при попытке ввести невалидное значение в поле Пароль
    @pytest.mark.parametrize('password', [' ','1', '12345'])  # невалидные значения для пароля
    def test_password_in_registration_form_invalid_values(self, driver, go_to_registration_form, password):
        # заполняем поле Пароль
        driver.find_element(*TestLocators.AUTHORIZATION_PASSWORD_LOCATOR).send_keys(password)
        # кликаем по кнопке Зарегистрироваться
        driver.find_element(*TestLocators.BUTTON_REGISTER_LOCATOR).click()
        # проверяем, что выходит сообщение об ошибки при заполнении поля Пароль невалидным значением
        password_error_text = driver.find_element(*TestLocators.ERROR_PASSWORD_LOCATOR).text
        assert password_error_text == 'Некорректный пароль'

