import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step("Инициализируем драйвер")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Находим элемент")
    def find_element_located(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Ожидаем возможности нажатия на элемент")
    def find_element_located_click(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()
