import allure
import pytest
from pages.email_page import EmailPage
from pages.first_authorization_page import FirstAuthorizationPage
from pages.code_page import CodePage
from pages.workspace_page import WorkspacePage
from helper import Helper


@pytest.fixture()
def put_email(browser):
    """
    фикстура ввода корректной почты
    """
    first_page = FirstAuthorizationPage(driver=browser)
    first_page.click_on_begin_button()
    email_page = EmailPage(driver=browser)
    email_page.put_email(Helper.Correct_email[0])
    email_page.click_on_active_continue_button()


@pytest.fixture()
def put_email_and_code(browser):
    """
    фикстура ввода корректной почты и кода для проверки
    """
    first_page = FirstAuthorizationPage(driver=browser)
    first_page.click_on_begin_button()
    email_page = EmailPage(driver=browser)
    email_page.put_email(Helper.Correct_email[0])
    email_page.click_on_active_continue_button()
    code_page = CodePage(driver=browser)
    code_page.set_code_for_check_email(Helper.Correct_code)
