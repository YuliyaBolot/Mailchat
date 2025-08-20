import allure
from pages.base_page import BasePage
from locators.birthday_page_locators import BirthdayPageLocators


class BirthdayPage(BasePage):

    @allure.step("Загрузка формы для ввода даты рождения")
    def loading_birthday_form(self):
        return self.find_element_located(BirthdayPageLocators.BIRTHDAY_FORM)
