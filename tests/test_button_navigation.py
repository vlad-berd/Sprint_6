import allure

from pages.main_page import MainPage
from curl import *


class TestOrderButtonNavigation:
    @allure.title("Проверка перехода на страницу order по клику на верхнюю кнопку 'Заказать'")
    @allure.description("Нажимаем на верхнюю кнопку 'Заказать' и проверяем переход на страницу order")
    def test_click_on_top_button_order_redirect_to_order_page_success(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_top_order_button()

        assert driver.current_url == ORDER_URL

    @allure.title("Проверка перехода на страницу order по клику на нижнюю кнопку 'Заказать'")
    @allure.description("Нажимаем на нижнюю кнопку 'Заказать' и проверяем переход на страницу order")
    def test_click_on_bottom_button_order_redirect_to_order_page_success(self, driver):
        main_page = MainPage(driver)

        main_page.click_on_bottom_order_button()

        assert driver.current_url == ORDER_URL
