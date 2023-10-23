"""Login page methods"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_button(self):
        assert self.is_element_present(
            *LoginPageLocators.CUSTOMER_USER_BTN), "Login button is not " \
                                                   "presented"

    def go_to_customer_page(self):
        login_button = self.browser.find_element(
            *LoginPageLocators.CUSTOMER_USER_BTN)
        login_button.click()
