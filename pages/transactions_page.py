from .base_page import BasePage
from .locators import TransactionsPageLocators
import csv


class TransactionsPage(BasePage):

    def transactions_check(self):
        credit_string = self.browser.find_elements(*TransactionsPageLocators.CREDIT_STRING)
        assert len(credit_string) == 1, "Transaction record not found"
        debit_string = self.browser.find_elements(*TransactionsPageLocators.DEBIT_STRING)
        assert len(debit_string) == 1, "Transaction record not found"

    def create_csv(self):
        tbody = self.browser.find_element(*TransactionsPageLocators.TRANSACTIONS_TABLE)
        data = []

        for tr in tbody.find_elements(*TransactionsPageLocators.TRANSACTIONS_TABLE_TR):
            row = [item.text for item in tr.find_elements(*TransactionsPageLocators.TRANSACTIONS_TABLE_TD)]
            data.append(row)

        with open("transactions.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(
                data
            )
