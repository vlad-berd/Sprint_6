import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Подождать появления нового окна или вкладки")
    def wait_for_new_window_or_tab(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
    
    @allure.step("Подождать соответсвие заголовка страницы и указанной строки")
    def wait_for_title_page_matches_specified_text(self, title_page, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.title_is(title_page))
    
    @allure.step("Подождать полной загрузки страницы нового окна или вкладки")
    def switching_to_new_tab(self, title_new_tab, timeout=10):
        original_window = self.driver.current_window_handle

        self.wait_for_new_window_or_tab(timeout)
    
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        
        self.wait_for_title_page_matches_specified_text(title_new_tab)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        self.wait_for_element(locator, timeout).click()

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)
