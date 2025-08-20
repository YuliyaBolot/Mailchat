from selenium.webdriver.common.by import By


class SpecifyWorkspaceNamePageLocators:

    WORKSPACE_NAME_FORM = (By.XPATH, "//div[@class='d_domain']")

    WORKSPACE_NAME_FIELD = (By.XPATH, "//input[@id='domain-company']")

    BACK_BUTTON = (By.XPATH, "//p[@class='d_domain__back-link']")

    MESSAGE_ABOUT_INCORRECT_NAME = (By.XPATH, "//p[@class='form-field__error no-select']")

    CONTINUE_BUTTON = (By.XPATH, "//button[@class='btn btn--full-width with-border btn--lg no-select']")
