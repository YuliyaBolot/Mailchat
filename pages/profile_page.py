import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators


class ProfilePage(BasePage):

    @allure.step("Загрузка формы настройки личного профиля")
    def loading_profile_form(self):
        return self.find_element_located(ProfilePageLocators.PROFILE_FORM)
