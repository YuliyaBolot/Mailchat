import allure
from pages.base_page import BasePage
from locators.specify_workspace_name_page_locators import SpecifyWorkspaceNamePageLocators


class SpecifyWorkspaceNamePage(BasePage):

    @allure.step("Загрузка формы для ввода имени рабочего пространства")
    def loading_workspace_name_form(self):
        return self.find_element_located(SpecifyWorkspaceNamePageLocators.WORKSPACE_NAME_FORM)

    @allure.step("Ввод имени воркспейса")
    def input_workspace_name(self, workspace_name):
        self.find_element_located_click(SpecifyWorkspaceNamePageLocators.WORKSPACE_NAME_FIELD)
        self.find_element_located(SpecifyWorkspaceNamePageLocators.WORKSPACE_NAME_FIELD).clear()
        return self.find_element_located(SpecifyWorkspaceNamePageLocators.WORKSPACE_NAME_FIELD).send_keys(
            workspace_name)

    @allure.step("Нажимаем на кнопку 'Продолжить'")
    def click_on_continue_button(self):
        return self.find_element_located_click(SpecifyWorkspaceNamePageLocators.CONTINUE_BUTTON)

    @allure.step("Получение сообщения о вводе некорректного имени")
    def get_message_about_incorrect_workspace_name(self):
        return self.find_element_located(SpecifyWorkspaceNamePageLocators.MESSAGE_ABOUT_INCORRECT_NAME).text

    @allure.step("Возврат на предыдущую страницу")
    def go_to_back_page(self):
        return self.find_element_located_click(SpecifyWorkspaceNamePageLocators.BACK_BUTTON)

    @allure.step("Ввод корректного имени воркспейса")
    def set_correct_workspace_name(self, workspace_name):
        self.loading_workspace_name_form()
        self.input_workspace_name(workspace_name)
        self.click_on_continue_button()
