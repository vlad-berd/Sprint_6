import allure
import pytest

from pages.main_page import MainPage
from data import DataMainPage
from curl import *


class TestImportantQuestions:
    @allure.title("Проверка ответа на вопрос - {question}")
    @allure.description("Проверка раздела 'Вопросы о важном' на соответствие ответов на вопросы")
    @pytest.mark.parametrize("question, answer", DataMainPage.questions_and_answers)
    def test_text_answer_on_question(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.click_on_question(question)

        text_answer = main_page.get_text_answer(answer)

        assert text_answer == answer
