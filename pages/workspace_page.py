import allure
from pages.base_page import BasePage
from locators.workspace_page_locators import WorkspacePageLocators


class WorkspacePage(BasePage):

    @allure.step("Загрузка формы выбора рабочего пространства")
    def create_workspace(self):
        return self.find_element_located(WorkspacePageLocators.ADD_NEW_SPACE_BUTTON)

    @allure.step("Возврат на предыдущую страницу")
    def go_to_back_page(self):
        return self.find_element_located_click(WorkspacePageLocators.BACK_LINK)

    @allure.step("Нажимаем на кнопку добавления нового рабочего пространства")
    def click_on_add_new_workspace_button(self):
        return self.find_element_located_click(WorkspacePageLocators.ADD_NEW_SPACE_BUTTON)
