import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from curl import *
from pages.main_page import MainPage
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

@pytest.fixture
def order_page_driver(driver):
    main_page = MainPage(driver)
    main_page.click_on_cookie_confirm_button()
    main_page.click_on_top_order_button()

    return driver

USERS = DataOrderPage.users

@pytest.fixture(params=USERS.keys())
def user(request):
    yield USERS[request.param]
