from selenium.webdriver.common.by import By


class MainPageLocators:
    # Окно с куки
    COOKIE_CONFIRM_BUTTON = (By.ID, "rcc-confirm-button")

    # Логотипы
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Раздел "Вопросы о важном"
    @staticmethod
    def question_number(question):
        return By.XPATH, f"//div[@data-accordion-component='AccordionItemButton' and text()='{question}']"
    
    @staticmethod
    def answer_number(answer):
        return By.XPATH, f"//div[@data-accordion-component='AccordionItemPanel']/p[text()='{answer}']"
    
    # Кнопки перехода на страницу заказа
    ORDER_BUTTON_TOP_PAGE = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM_PAGE = (By.CLASS_NAME, "Button_Middle__1CSJM")
