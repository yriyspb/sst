"""Transactions page methods"""
from .base_page import BasePage
from .locators import TransactionsPageLocators

data = []


class TransactionsPage(BasePage):

    def transactions_check(self):
        credit_string = self.browser.find_elements(
            *TransactionsPageLocators.CREDIT_STRING)
        assert len(credit_string) == 1, "Transaction record not found"
        debit_string = self.browser.find_elements(
            *TransactionsPageLocators.DEBIT_STRING)
        assert len(debit_string) == 1, "Transaction record not found"

    def parse_table(self):
        tbody = self.browser.find_element(
            *TransactionsPageLocators.TRANSACTIONS_TABLE)

        for tr in tbody.find_elements(
                *TransactionsPageLocators.TRANSACTIONS_TABLE_TR):
            row = [item.text for item in tr.find_elements(
                *TransactionsPageLocators.TRANSACTIONS_TABLE_TD)]
            data.append(row)
