import allure
from pages.workspace_page import WorkspacePage
from pages.specify_workspace_name_page import SpecifyWorkspaceNamePage


class TestMoveToCreateNewWorkspace:

    @allure.epic("Тестирование перехода на этап создания нового пространства")
    @allure.title("Проверка перехода на этап создания нового пространства")
    def test_move_to_create_new_workspace(self, browser, put_email_and_code):
        workspace = WorkspacePage(driver=browser)
        workspace.click_on_add_new_workspace_button()
        workspace_name = SpecifyWorkspaceNamePage(driver=browser)
        assert workspace_name.loading_workspace_name_form()
