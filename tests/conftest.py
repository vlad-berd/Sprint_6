import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from curl import *
from data import DataOrderPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--windows-size=1600,900")
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get(BASE_URL)
    yield browser
    browser.quit()

USERS = DataOrderPage.users

@pytest.fixture(params=USERS.keys())
def user(request):
    yield USERS[request.param]
