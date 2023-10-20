from .base_page import BasePage
from .locators import AccountPageLocators
import datetime
import time

current_time = datetime.datetime.now()
n = current_time.day + 1


def fibonacci_number(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)


class AccountPage(BasePage):

    def deposit_withdrawal(self):
        deposit_tab = self.browser.find_element(*AccountPageLocators.DEPOSIT_TAB)
        deposit_tab.click()
        input = self.browser.find_element(*AccountPageLocators.AMOUNT_INPUT)
        input.send_keys(fibonacci_number(n))
        deposit_submit_button = self.browser.find_element(*AccountPageLocators.DEPOSIT_SUBMIT_BTN)
        deposit_submit_button.click()
        withdrawl_tab = self.browser.find_element(*AccountPageLocators.WITHDRAWL_TAB)
        withdrawl_tab.click()
        time.sleep(1)
        input = self.browser.find_element(*AccountPageLocators.AMOUNT_INPUT)
        input.send_keys(fibonacci_number(n))
        withdrawl_submit_button = self.browser.find_element(*AccountPageLocators.WITHDRAWL_SUBMIT_BTN)
        withdrawl_submit_button.click()
        x = self.browser.find_element(*AccountPageLocators.BALANCE).text
        assert x == "0", "Balance is not null"
        time.sleep(1)

    def go_to_transactions_page(self):
        transactions_tab = self.browser.find_element(*AccountPageLocators.TRANSACTIONS_TAB)
        transactions_tab.click()
