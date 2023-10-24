"""Customer page methods"""
import allure
from selenium.webdriver.support.ui import Select

from .base_page import BasePage
from .locators import CustomerPageLocators


class CustomerPage(BasePage):

    @allure.feature('Select user')
    @allure.story('Выбор пользователя')
    @allure.severity('normal')
    def select_user(self):
        with allure.step("Проверим cуществование пользователя"):
            select = Select(
                self.browser.find_element(*CustomerPageLocators.USER_SELECT))
            select.select_by_visible_text(CustomerPageLocators.USER_NAME)

    def go_to_account_page(self):
        login_button = self.browser.find_element(
            *CustomerPageLocators.LOGIN_BTN)
        login_button.click()
