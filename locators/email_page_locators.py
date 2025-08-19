from selenium.webdriver.common.by import By


class EmailPageLocators:

    EMAIL_FORM = (By.XPATH, '//div[@class="log_login"]')

    EMAIL_FIELD = (By.XPATH, '//input[@id="email-input"]')

    ACTIVE_CONTINUE_BUTTON = (By.XPATH, '//button[@class="btn btn--full-width with-border btn--lg no-select"]')

    INACTIVE_CONTINUE_BUTTON = (By.XPATH, '//button[@disabled]')
