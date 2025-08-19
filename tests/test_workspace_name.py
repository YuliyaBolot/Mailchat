import pytest
import allure
from pages.workspace_page import WorkspacePage
from pages.specify_workspace_name_page import SpecifyWorkspaceNamePage
from pages.profile_page import ProfilePage
from helper import Helper


class TestWorkspaceName:

    @allure.epic("Тестирование назначения имени воркспейса")
    @allure.title("Проверка успешного присвоения имени компании с корректным форматом")
    def test_set_correct_workspace_name(self, browser, put_email_and_code):
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.set_correct_workspace_name(Helper.Correct_workspace_name)
        profile = ProfilePage(driver=browser)
        assert profile.loading_profile_form()

    @allure.epic("Тестирование назначения имени воркспейса")
    @allure.title("Возврат на предыдущую страницу")
    def test_go_to_back_page(self, browser, put_email_and_code):
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.go_to_back_page()
        assert workspace.create_workspace()

    @allure.epic("Тестирование назначения имени воркспейса")
    @allure.title("Проверка ввода некорректного имени воркспейса")
    @pytest.mark.parametrize('name, message', [[Helper.Short_workspace_name, Helper.Message_about_short_workspace_name],
                                               [Helper.Incorrect_workspace_name,
                                                Helper.Message_about_incorrect_workspace_name],
                                               [Helper.Exist_domain, Helper.Message_about_domain_is_taken]])
    def test_set_incorrect_workspace_name(self, browser, put_email_and_code, name, message):
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.input_workspace_name(name)
        error_message = workspace_name.get_message_about_incorrect_workspace_name()
        assert error_message == message
