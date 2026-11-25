"""PyTest browser fixture with a command-line language option."""

import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="Browser language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if os.environ.get("COURSE_BROWSER") == "edge":
        # Local verification on a computer without Chrome.
        options = webdriver.EdgeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        driver = webdriver.Edge(options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
