import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language")
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language").lower()
    browser_name = request.config.getoption("browser_name").lower()

    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(10)
    yield browser

    browser.quit()
