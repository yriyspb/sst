"""Login page methods"""
import allure
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.feature('Login page')
    @allure.story('Страница логина')
    @allure.severity('critical')
    def should_be_login_button(self):
        with allure.step("Проверим загрузку страницы теста"):
            assert self.is_element_present(
                *LoginPageLocators.CUSTOMER_USER_BTN), "Login button is not " \
                                                       "presented or Login " \
                                                       "page " \
                                                       "is not " \
                                                       "available"

    def go_to_customer_page(self):
        login_button = self.browser.find_element(
            *LoginPageLocators.CUSTOMER_USER_BTN)
        login_button.click()
