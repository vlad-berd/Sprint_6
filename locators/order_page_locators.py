from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Часть формы "Для кого самокат"
    FIELD_NAME = (By.CSS_SELECTOR, ".Input_Responsible__1jDKN[placeholder='* Имя']")
    FIELD_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    FIELD_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    FIELD_TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    FIELD_STATIONS = (By.CLASS_NAME, "select-search")

    @staticmethod
    def name_station(name):
        return By.XPATH, f"//div[@class='Order_Text__2broi' and text()='{name}']/.."
    
    NEXT_BUTTON = (By.CLASS_NAME, "Button_Middle__1CSJM")

    # Часть формы "Про Аренду"
    FIELD_DATE = (By.CLASS_NAME, "react-datepicker__input-container")
    TODAY_DAY = (By.CLASS_NAME, "react-datepicker__day--today")

    FIELD_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")

    @staticmethod
    def rental_period(period):
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"
    
    @staticmethod
    def scooter_color(color):
        return By.ID, f"{color}"

    FIELD_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[2]")

    # Окно с подтверждением заказа
    ORDER_CONFIRMATION_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Окно об успешном оформление заказа
    TEXT_SUCCESS_ORDER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
