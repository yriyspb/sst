"""Module providing main test function"""
import allure
from .pages.login_page import LoginPage
from .pages.customer_page import CustomerPage
from .pages.account_page import AccountPage
from .pages.transactions_page import TransactionsPage, data
from .util import create_csv


def test_e2e(browser):
    """e2e test steps"""
    link = "https://www.globalsqa.com/angularJs-protractor/" \
           "BankingProject/#/login"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_customer_page()
    customer_page = CustomerPage(browser, browser.current_url)
    customer_page.select_user()
    customer_page.go_to_account_page()
    account_page = AccountPage(browser, browser.current_url)
    account_page.deposit_withdrawal()
    account_page.go_to_transactions_page()
    transactions_page = TransactionsPage(browser, browser.current_url)
    transactions_page.transactions_check()
    transactions_page.parse_table()
    create_csv(data)
    with allure.step("Add file in report"):
        allure.attach.file("transactions.csv", name="transactions",
                           attachment_type=allure.attachment_type.CSV)
