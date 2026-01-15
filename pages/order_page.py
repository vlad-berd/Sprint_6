import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполнить поле 'Имя'")
    def fill_field_name(self, name):
        self.send_keys_to_input(OrderPageLocators.FIELD_NAME, name)

    @allure.step("Заполнить поле 'Фамилия'")
    def fill_field_surname(self, surname):
        self.send_keys_to_input(OrderPageLocators.FIELD_SURNAME, surname)

    @allure.step("Заполнить поле 'Адрес'")
    def fill_field_address(self, address):
        self.send_keys_to_input(OrderPageLocators.FIELD_ADDRESS, address)
    
    @allure.step("Выбрать станцию")
    def select_station(self, name):
        self.click_on_element(OrderPageLocators.FIELD_STATIONS)
        self.scroll_to_element(OrderPageLocators.name_station(name))
        self.click_on_element(OrderPageLocators.name_station(name))
    
    @allure.step("Заполнить поле 'Телефон'")
    def fill_field_telephone(self, telephone):
        self.send_keys_to_input(OrderPageLocators.FIELD_TELEPHONE, telephone)

    @allure.step("Кликнуть на кнопку 'Дальше'")
    def click_on_button_next(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать дату заказа")
    def select_date_day(self):
        self.click_on_element(OrderPageLocators.FIELD_DATE)
        self.click_on_element(OrderPageLocators.TODAY_DAY)
    
    @allure.step("Выбрать период аренды")
    def select_rental_period(self, period):
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.rental_period(period))

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color(self, color):
        self.click_on_element(OrderPageLocators.scooter_color(color))

    @allure.step("Написать комментарий")
    def write_comment(self, comment):
        self.send_keys_to_input(OrderPageLocators.FIELD_COMMENT, comment)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_on_button_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Кликнуть на кнопку 'Да' для подтверждения заказа")
    def click_on_button_confirm_order(self):
        self.click_on_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step("Получить сообщение об успешном оформление заказа")
    def get_message_success_order(self):
        return self.get_text_on_element(OrderPageLocators.TEXT_SUCCESS_ORDER)
