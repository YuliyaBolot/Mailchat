from selenium.webdriver.common.by import By


class CodePageLocators:

    CODE_FORM = (By.XPATH, '//div[@class="cd_code"]')

    CODE_INPUT_1 = (By.XPATH, '//fieldset[@class="code-input"]/label[1]/input')

    CODE_INPUT_2 = (By.XPATH, '//fieldset[@class="code-input"]/label[2]/input')

    CODE_INPUT_3 = (By.XPATH, '//fieldset[@class="code-input"]/label[3]/input')

    CODE_INPUT_4 = (By.XPATH, '//fieldset[@class="code-input"]/label[4]/input')

    CODE_INPUT_5 = (By.XPATH, '//fieldset[@class="code-input"]/label[5]/input')

    CODE_INPUT_6 = (By.XPATH, '//fieldset[@class="code-input"]/label[6]/input')

    CONTINUE_BUTTON = (By.XPATH, '//button[@class="btn btn--full-width with-border btn--lg no-select"]/span')

    ERROR_CODE_MESSAGE = (By.XPATH, "//p[@class='cd_code__error']")

    INACTIVE_CONTINUE_BUTTON = (By.XPATH, '//button[@disabled]')
