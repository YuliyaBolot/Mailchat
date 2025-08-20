import pytest
import allure
from pages.email_page import EmailPage
from pages.first_authorization_page import FirstAuthorizationPage
from pages.code_page import CodePage
from pages.profile_page import ProfilePage
from pages.birthday_page import BirthdayPage
from pages.workspace_page import WorkspacePage
from pages.specify_workspace_name_page import SpecifyWorkspaceNamePage
from helper import Profile, Workspace, Email, Code


class TestProfilePage:

    @allure.epic("Тестирование заполнения личных данных профиля")
    @allure.title("Проверка установки аватарки")
    @pytest.mark.xfail
    def test_upload_avatar(self, browser):
        first_page = FirstAuthorizationPage(driver=browser)
        first_page.click_on_begin_button()
        email_page = EmailPage(driver=browser)
        email_page.put_email(Email.New_email[0])
        email_page.click_on_active_continue_button()
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Correct_code)
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.set_correct_workspace_name(Workspace.New_workspace_name[0])
        profile = ProfilePage(driver=browser)
        profile.upload_profile_picture(Profile.Photo)
        assert profile.check_avatar_uploaded()

    @allure.epic("Тестирование заполнения личных данных профиля")
    @allure.title("Проверка установки данных пользователя")
    def test_input_user_first_name(self, browser):
        first_page = FirstAuthorizationPage(driver=browser)
        first_page.click_on_begin_button()
        email_page = EmailPage(driver=browser)
        email_page.put_email(Email.New_email[1])
        email_page.click_on_active_continue_button()
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Correct_code)
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.set_correct_workspace_name(Workspace.New_workspace_name[1])
        profile = ProfilePage(driver=browser)
        profile.input_user_data(Profile.Name, Profile.Last_name)
        birthday = BirthdayPage(driver=browser)
        assert birthday.loading_birthday_form()

    @allure.epic("Тестирование заполнения личных данных профиля")
    @allure.title("Проверка, что кнопка 'Продолжить' неактивна, если заполнено только имя пользоватедя")
    def test_check_continue_button_inactive_without_last_name(self, browser):
        first_page = FirstAuthorizationPage(driver=browser)
        first_page.click_on_begin_button()
        email_page = EmailPage(driver=browser)
        email_page.put_email(Email.New_email[2])
        email_page.click_on_active_continue_button()
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Correct_code)
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.set_correct_workspace_name(Workspace.New_workspace_name[2])
        profile = ProfilePage(driver=browser)
        profile.input_user_first_name(Profile.Name)
        assert profile.check_continue_button_inactive()

    @allure.epic("Тестирование заполнения личных данных профиля")
    @allure.title("Проверка, что кнопка 'Продолжить' неактивна, если заполнена только фамилия пользоватедя")
    def test_check_continue_button_inactive_without_first_name(self, browser):
        first_page = FirstAuthorizationPage(driver=browser)
        first_page.click_on_begin_button()
        email_page = EmailPage(driver=browser)
        email_page.put_email(Email.New_email[3])
        email_page.click_on_active_continue_button()
        code_page = CodePage(driver=browser)
        code_page.set_code_for_check_email(Code.Correct_code)
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        workspace_name.set_correct_workspace_name(Workspace.New_workspace_name[3])
        profile = ProfilePage(driver=browser)
        profile.input_user_last_name(Profile.Last_name)
        assert profile.check_continue_button_inactive()
