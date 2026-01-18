import allure

from pages.main_page import MainPage
from data import title_dzen_home_page
from curl import *


class TestLogoNavigation:
    @allure.title("Проверка перехода по логотипу 'Самокат' на главную страницу")
    @allure.description("Нажимаем на логотип 'Самоката' и проверяем переход на главную страницу")
    def test_click_logo_scooter_redirect_to_main_page_success(self, driver):
        """Проверка перехода по логотипу 'Самокат' на главную страницу"""
        main_page = MainPage(driver)
        main_page.click_on_top_order_button()

        main_page.click_on_scooter_button()

        assert driver.current_url == BASE_URL

    @allure.title("Проверка перехода по логотипу 'Яндекс' на главную страницу Дзен")
    @allure.description("Нажимаем на логотип 'Яндекса' и проверяем переход на главную страницу Дзен")
    def test_click_logo_yandex_redirect_to_dzen_home_page_success(self, driver):
        """Проверка перехода по логотипу 'Яндекс' на главную страницу Дзен"""
        main_page = MainPage(driver)
        
        main_page.click_on_yandex_button()
        main_page.switching_to_dzen_home_page_tab(title_dzen_home_page)

        assert driver.current_url == DZEN_HOME_PAGE
