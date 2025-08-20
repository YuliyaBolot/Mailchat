from selenium.webdriver.common.by import By
from random import randint


class FirstAuthorizationPageLocators:

    LANGUAGES_BUTTON = (By.XPATH, '//span[@class="btn__title"]')

    LANGUAGES_LST = (By.XPATH, '//div[@class="context-menu__list"]')

    LANGUAGE = (By.XPATH, f'//div[@class="context-menu__list"]/div[{randint(1, 13)}]/div[2]//span')

    LANGUAGES_FIELD = (By.XPATH, '//p[@class="component-text text-type-primary align-left"]/span')

    BEGIN_BUTTON = (By.XPATH, '//button[@class="button-ui btn btn--full-width with-border btn--lg no-select"]')
