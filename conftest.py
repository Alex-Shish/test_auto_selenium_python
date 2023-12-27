import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose lang: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption("language")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart Chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart Firefox browser for test..")
        firefox_profile: FirefoxProfile = webdriver.FirefoxProfile()
        firefox_profile.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
