import allure
from pages.first_authorization_page import FirstAuthorizationPage


class TestChangeLanguages:

    @allure.epic("Тестирование смены всех языков на первой странице авторизации")
    @allure.title("Смена языков")
    def test_change_languages(self, browser):
        first_page = FirstAuthorizationPage(driver=browser)
        new_language = first_page.change_languages().text
        language_in_field = first_page.get_language().text
        assert new_language == language_in_field
