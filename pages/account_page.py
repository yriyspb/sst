"""Account page methods"""
import allure
from .base_page import BasePage
from .locators import AccountPageLocators
from ..util import fibonacci_number, f


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
        with allure.step("Проверим сообщение об успехе пополенения счёта"):
            assert self.is_element_present(
                *AccountPageLocators.DEPOSIT_SUCCESS_MESSAGE), (
                "Deposit is not successful")
        withdrawl_tab = self.browser.find_element(
            *AccountPageLocators.WITHDRAWL_TAB)
        withdrawl_tab.click()
        assert self.is_element_present(
            *AccountPageLocators.AMOUNT_WITHDRAWL_INPUT), (
            "Amount withdrawal input is not presented")
        amount_input = self.browser.find_element(
            *AccountPageLocators.AMOUNT_INPUT)
        amount_input.send_keys(fibonacci_number(f))
        withdrawl_submit_button = self.browser.find_element(
            *AccountPageLocators.WITHDRAWL_SUBMIT_BTN)
        withdrawl_submit_button.click()
        with allure.step("Проверим сообщение об успехе списания со счёта"):
            assert self.is_element_present(
                *AccountPageLocators.WITHDRAWL_SUCCESS_MESSAGE), (
                "Withdraw is not successful")
        x = self.browser.find_element(*AccountPageLocators.BALANCE).text
        with allure.step("Проверим, что дебет и кредит сошелся)"):
            assert x == "0", "Balance is not null"

    def go_to_transactions_page(self):
        transactions_tab = self.browser.find_element(
            *AccountPageLocators.TRANSACTIONS_TAB)
        transactions_tab.click()
