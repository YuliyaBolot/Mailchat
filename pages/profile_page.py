import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step("Загрузка формы настройки личного профиля")
    def loading_profile_form(self):
        return self.find_element_located(ProfilePageLocators.PROFILE_FORM)

    @allure.step("Вводим имя пользователя")
    def input_user_first_name(self, first_name):
        self.find_element_located_click(ProfilePageLocators.FIRST_NAME_FIELD)
        self.find_element_located(ProfilePageLocators.FIRST_NAME_FIELD).clear()
        return self.find_element_located(ProfilePageLocators.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step("Вводим фамилию пользователя")
    def input_user_last_name(self, last_name):
        self.find_element_located_click(ProfilePageLocators.LAST_NAME_FIELD)
        self.find_element_located(ProfilePageLocators.LAST_NAME_FIELD).clear()
        return self.find_element_located(ProfilePageLocators.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step("Загрузка аватарки")
    def upload_profile_picture(self, profile_picture):
        self.find_element_located_click(ProfilePageLocators.ADD_PHOTO)
        self.find_element_located(ProfilePageLocators.ADD_PHOTO).send_keys(profile_picture)

    @allure.step("Проверяем, что аватарка установлена")
    def check_avatar_uploaded(self):
        return self.find_element_located(ProfilePageLocators.AVATAR)

    @allure.step("Нажимаем на кнопку 'Продолжить'")
    def click_on_continue_button(self):
        return self.find_element_located_click(ProfilePageLocators.ACTIVE_CONTINUE_BUTTON)

    @allure.step("Ввод данных пользователя")
    def input_user_data(self, first_name, last_name):
        self.loading_profile_form()
        self.input_user_first_name(first_name)
        self.input_user_last_name(last_name)
        self.click_on_continue_button()

    @allure.step("Проверяем, что кнопка 'Продолжить' не доступна")
    def check_continue_button_inactive(self):
        return self.find_element_located(ProfilePageLocators.INACTIVE_CONTINUE_BUTTON)
