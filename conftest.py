import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://auth.lenzaos.com")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromiumService(), options=ChromeOptions())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(), options=FirefoxOptions())
    elif browser == "edge":
        driver = webdriver.Edge(options=EdgeOptions())
    else:
        raise ValueError("Unknown browser")
    driver.get(url)
    driver.url = url
    yield driver
    driver.quit()
