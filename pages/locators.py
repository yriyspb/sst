"""All pages locators"""
from selenium.webdriver.common.by import By


class LoginPageLocators():
    CUSTOMER_USER_BTN = (By.CSS_SELECTOR, "button[ng-click='customer()']")


class CustomerPageLocators():
    USER_SELECT = (By.ID, "userSelect")
    USER_NAME = "Harry Potter"
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")


class AccountPageLocators():
    TRANSACTIONS_TAB = (By.CSS_SELECTOR, "button[ng-class='btnClass1']")
    DEPOSIT_TAB = (By.CSS_SELECTOR, "button[ng-class='btnClass2']")
    WITHDRAWL_TAB = (By.CSS_SELECTOR, "button[ng-class='btnClass3']")
    AMOUNT_INPUT = (By.CSS_SELECTOR, "input[ng-model='amount']")
    DEPOSIT_SUBMIT_BTN = (
        By.XPATH, "//button[@type='submit' and normalize-space()='Deposit']")
    WITHDRAWL_SUBMIT_BTN = (
        By.XPATH, "//button[@type='submit' and normalize-space()='Withdraw']")
    BALANCE = (By.XPATH,
               "//div[contains(.,'Balance')]/strong/following-sibling::text()"
               "[contains(.,'Balance')]/following-sibling::node()")
    DEPOSIT_SUCCESS_MESSAGE = (
        By.XPATH, "//span[normalize-space()='Deposit Successful']")
    WITHDRAWL_SUCCESS_MESSAGE = (
        By.XPATH, "//span[normalize-space()='Transaction successful']")
    AMOUNT_WITHDRAWL_INPUT = (
        By.XPATH, "//label[normalize-space()='Amount to be Withdrawn :']")


class TransactionsPageLocators():
    DEBIT_STRING = (By.ID, "anchor0")
    CREDIT_STRING = (By.ID, "anchor1")
    TRANSACTIONS_TABLE = (By.TAG_NAME, "tbody")
    TRANSACTIONS_TABLE_TR = (By.XPATH, ".//tr")
    TRANSACTIONS_TABLE_TD = (By.XPATH, './/td')
