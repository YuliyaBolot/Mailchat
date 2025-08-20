import allure
from pages.base_page import BasePage
from locators.email_page_locators import EmailPageLocators


class EmailPage(BasePage):

    @allure.step("Загрузка формы для ввода почты")
    def loading_email_form(self):
        return self.find_element_located(EmailPageLocators.EMAIL_FORM)

    @allure.step("Вводим почту")
    def set_email(self, email):
        self.find_element_located_click(EmailPageLocators.EMAIL_FIELD)
        self.find_element_located(EmailPageLocators.EMAIL_FIELD).clear()
        return self.find_element_located(EmailPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Нажимаем на кнопку 'Продолжить'")
    def click_on_active_continue_button(self):
        return self.find_element_located_click(EmailPageLocators.ACTIVE_CONTINUE_BUTTON)

    @allure.step("Ввод почты")
    def put_email(self, email):
        self.loading_email_form()
        self.set_email(email)

    @allure.step("Проверяем, что кнопка 'Продолжить' не активна")
    def check_inactive_continue_button(self):
        return self.find_element_located(EmailPageLocators.INACTIVE_CONTINUE_BUTTON)
