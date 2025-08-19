import allure
from pages.base_page import BasePage
from locators.code_page_locators import CodePageLocators


class CodePage(BasePage):

    @allure.step("Загрузка формы для ввода кода")
    def loading_code_form(self):
        return self.find_element_located(CodePageLocators.CODE_FORM)

    @allure.step("Ввод кода")
    def input_code(self, code: list):
        self.find_element_located(CodePageLocators.CODE_INPUT_1).send_keys(code[0])
        self.find_element_located(CodePageLocators.CODE_INPUT_2).send_keys(code[1])
        self.find_element_located(CodePageLocators.CODE_INPUT_3).send_keys(code[2])
        self.find_element_located(CodePageLocators.CODE_INPUT_4).send_keys(code[3])
        self.find_element_located(CodePageLocators.CODE_INPUT_5).send_keys(code[4])
        self.find_element_located(CodePageLocators.CODE_INPUT_6).send_keys(code[5])

    @allure.step("Нажатие на кнопку 'Продолжить'")
    def click_on_continue_button(self):
        return self.find_element_located_click(CodePageLocators.CONTINUE_BUTTON)

    @allure.step("Ввод кода для проверки почты")
    def set_code_for_check_email(self, code: list):
        self.loading_code_form()
        self.input_code(code)
        self.click_on_continue_button()

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self):
        return self.find_element_located(CodePageLocators.ERROR_CODE_MESSAGE).text

    @allure.step("Ввод неполного кода")
    def input_short_code(self, code: list):
        self.find_element_located(CodePageLocators.CODE_INPUT_1).send_keys(code[0])
        self.find_element_located(CodePageLocators.CODE_INPUT_2).send_keys(code[1])
        self.find_element_located(CodePageLocators.CODE_INPUT_3).send_keys(code[2])
        self.find_element_located(CodePageLocators.CODE_INPUT_4).send_keys(code[3])
        self.find_element_located(CodePageLocators.CODE_INPUT_5).send_keys(code[4])

    @allure.step("Проверяем, что кнопка 'Продолжить' не активна")
    def check_inactive_continue_button(self):
        return self.find_element_located(CodePageLocators.INACTIVE_CONTINUE_BUTTON)
