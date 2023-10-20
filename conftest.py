import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="function")
def browser():
    print("\nstart grid for test..")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("platformName", "Windows 10")
    browser = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=chrome_options
    )
    yield browser
    print("\nquit browser..")
    browser.quit()
