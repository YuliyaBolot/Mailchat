import allure
from pages.email_page import EmailPage
from pages.code_page import CodePage
from pages.workspace_page import WorkspacePage
from helper import Code


class TestCodePage:

    @allure.epic("Тестирование ввода кода для проверки почты")
    @allure.title("Ввод корректного кода")
    def test_input_correct_code(self, browser, put_email):
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Correct_code)
        workspace = WorkspacePage(driver=browser)
        assert workspace.create_workspace()

    @allure.epic("Тестирование ввода кода для проверки почты")
    @allure.title("Возврат на предыдущую страницу")
    def test_go_to_back_page(self, browser, put_email):
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Correct_code)
        workspace = WorkspacePage(driver=browser)
        workspace.go_to_back_page()
        email_page = EmailPage(driver=browser)
        assert email_page.loading_email_form()

    @allure.epic("Тестирование ввода кода для проверки почты")
    @allure.title("Ввод некорректного кода")
    def test_input_incorrect_code(self, browser, put_email):
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Incorrect_code)
        error_message = code_page.get_error_message()
        assert error_message == Code.Error_code_message

    @allure.epic("Тестирование ввода кода для проверки почты")
    @allure.title("Ввод неполного кода")
    def test_input_short_code(self, browser, put_email):
        code_page = CodePage(driver=browser)
        code_page.input_short_code(Code.Short_code)
        assert code_page.check_inactive_continue_button()
