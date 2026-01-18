import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import DataOrderPage


class TestScooterOrderForm:
    @allure.title("Проверка успешного оформления заказа самоката для пользователя {user[name]} {user[surname]} ")
    @allure.description("Переходим по кнопке 'Заказать' на страницу оформления заказа самоката. Заполняем форму и проверяем сообщение об успешном создании заказа")
    def test_order_scooter_after_click_order_button_success(self, driver, user):
        main_page = MainPage(driver)
        main_page.click_on_cookie_confirm_button()
        main_page.click_on_top_order_button()
        order_page = OrderPage(driver)

        allure.dynamic.parameter("Полное имя", f"{user["name"]} {user["surname"]}", excluded=True)

        order_page.fill_field_name(user["name"])
        order_page.fill_field_surname(user["surname"])
        order_page.fill_field_address(user["address"])
        order_page.select_station(user["station"])
        order_page.fill_field_telephone(user["phone_number"])
        order_page.click_on_button_next()
        order_page.select_date_day()
        order_page.select_rental_period(user["rental_period"])
        order_page.select_scooter_color(user["color_scooter"])
        order_page.write_comment(user["comment"])
        order_page.click_on_button_order()
        order_page.click_on_button_confirm_order()

        message_success_order = order_page.get_message_success_order()

        assert DataOrderPage.expected_text_success_order in message_success_order
