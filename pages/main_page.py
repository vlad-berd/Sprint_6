import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Кликнуть по кнопке 'да все привыкли' (подтвердить куки)")
    def click_on_cookie_confirm_button(self):
        self.click_on_element(MainPageLocators.COOKIE_CONFIRM_BUTTON)

    @allure.step("Кликнуть на вопрос")
    def click_on_question(self, question):
        question_locator = MainPageLocators.question_number(question)
        self.scroll_to_element(question_locator)
        self.click_on_element(question_locator)
    
    @allure.step("Получить текст ответа")
    def get_text_answer(self, answer):
        answer_locator = MainPageLocators.answer_number(answer)
        return self.get_text_on_element(answer_locator)
    
    @allure.step("Кликнуть по верхней кнопке 'Заказать'")
    def click_on_top_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP_PAGE)
    
    @allure.step("Кликнуть по нижней кнопке 'Заказать'")
    def click_on_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM_PAGE)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM_PAGE)
    
    @allure.step("Кликнуть по логотипу 'Самоката'")
    def click_on_scooter_button(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть по логотипу 'Yandex'")
    def click_on_yandex_button(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Перейти вкладку главной страницы Дзена")
    def switching_to_dzen_home_page_tab(self, title_dzen_home_page):
        self.switching_to_new_tab(title_dzen_home_page)
