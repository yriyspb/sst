"""Account page methods"""
import time
from .base_page import BasePage
from ..util import fibonacci_number, f
from .locators import AccountPageLocators


class AccountPage(BasePage):

    def deposit_withdrawal(self):
        deposit_tab = self.browser.find_element(
            *AccountPageLocators.DEPOSIT_TAB)
        deposit_tab.click()
        amount_input = self.browser.find_element(
            *AccountPageLocators.AMOUNT_INPUT)
        amount_input.send_keys(fibonacci_number(f))
        deposit_submit_button = self.browser.find_element(
            *AccountPageLocators.DEPOSIT_SUBMIT_BTN)
        deposit_submit_button.click()
        withdrawl_tab = self.browser.find_element(
            *AccountPageLocators.WITHDRAWL_TAB)
        withdrawl_tab.click()
        time.sleep(1)
        amount_input = self.browser.find_element(
            *AccountPageLocators.AMOUNT_INPUT)
        amount_input.send_keys(fibonacci_number(f))
        withdrawl_submit_button = self.browser.find_element(
            *AccountPageLocators.WITHDRAWL_SUBMIT_BTN)
        withdrawl_submit_button.click()
        x = self.browser.find_element(*AccountPageLocators.BALANCE).text
        assert x == "0", "Balance is not null"
        time.sleep(1)

    def go_to_transactions_page(self):
        transactions_tab = self.browser.find_element(
            *AccountPageLocators.TRANSACTIONS_TAB)
        transactions_tab.click()
