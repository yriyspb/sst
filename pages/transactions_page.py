"""Transactions page methods"""
import allure
from .base_page import BasePage
from .locators import TransactionsPageLocators

data = []


class TransactionsPage(BasePage):

    def transactions_check(self):
        credit_string = self.browser.find_elements(
            *TransactionsPageLocators.CREDIT_STRING)
        with allure.step("Проверка: есть ли вообще транзакции в истории"):
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='Transactions',
                          attachment_type=allure.attachment_type.PNG)
            assert len(credit_string) == 1, "Transaction records not found"
        debit_string = self.browser.find_elements(
            *TransactionsPageLocators.DEBIT_STRING)
        with allure.step("Проверка: есть ли все транзакции в истории"):
            assert len(debit_string) == 1, "Transaction record not found"

    def parse_table(self):
        tbody = self.browser.find_element(
            *TransactionsPageLocators.TRANSACTIONS_TABLE)

        for tr in tbody.find_elements(
                *TransactionsPageLocators.TRANSACTIONS_TABLE_TR):
            row = [item.text for item in tr.find_elements(
                *TransactionsPageLocators.TRANSACTIONS_TABLE_TD)]
            data.append(row)
