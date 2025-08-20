import allure
from pages.base_page import BasePage
from locators.first_authorization_page_locatots import FirstAuthorizationPageLocators


class FirstAuthorizationPage(BasePage):

    @allure.step("Нажимаем на кнопку для выбора языка")
    def click_on_languages_button(self):
        return self.find_element_located_click(FirstAuthorizationPageLocators.LANGUAGES_BUTTON)

    @allure.step("Появление выпадающего списка для выбора языка")
    def appearance_languages_list(self):
        return self.find_element_located(FirstAuthorizationPageLocators.LANGUAGES_LST)

    @allure.step("Выбираем язык")
    def choose_language(self):
        return self.find_element_located_click(FirstAuthorizationPageLocators.LANGUAGE)

    @allure.step("Смена языков")
    def change_languages(self):
        self.click_on_languages_button()
        self.appearance_languages_list()
        self.choose_language()
        return self.find_element_located(FirstAuthorizationPageLocators.LANGUAGES_FIELD)

    @allure.step("Получение значения поля для ввода языка")
    def get_language(self):
        return self.find_element_located(FirstAuthorizationPageLocators.LANGUAGES_FIELD)

    @allure.step("Нажимаем на кнопку 'Начать'")
    def click_on_begin_button(self):
        return self.find_element_located_click(FirstAuthorizationPageLocators.BEGIN_BUTTON)
