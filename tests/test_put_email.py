import allure
import pytest
from pages.email_page import EmailPage
from pages.first_authorization_page import FirstAuthorizationPage
from pages.code_page import CodePage
from helper import Helper


class TestPutEmail(Helper):

    @allure.epic("Тестирование ввода адреса почты")
    @allure.title("Ввод корректного адреса почты")
    @pytest.mark.parametrize('correct_email', Helper.Correct_email)
    def test_put_correct_email(self, browser, correct_email):
        first_page = FirstAuthorizationPage(driver=browser)
        first_page.click_on_begin_button()
        email_page = EmailPage(driver=browser)
        email_page.put_email(correct_email)
        email_page.click_on_active_continue_button()
        code_page = CodePage(driver=browser)
        assert code_page.loading_code_form()

    @allure.epic("Тестирование ввода адреса почты")
    @allure.title("Ввод некорректного адреса почты")
    @pytest.mark.parametrize('incorrect_email', Helper.Incorrect_email)
    def test_put_incorrect_email(self, browser, incorrect_email):
        first_page = FirstAuthorizationPage(driver=browser)
        first_page.click_on_begin_button()
        email_page = EmailPage(driver=browser)
        email_page.put_email(incorrect_email)
        assert email_page.check_inactive_continue_button()
