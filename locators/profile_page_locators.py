from selenium.webdriver.common.by import By


class ProfilePageLocators:

    PROFILE_FORM = (By.XPATH, "//div[@class='pr_profile']")

    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='Введите имя']")

    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='Введите фамилию']")

    ACTIVE_CONTINUE_BUTTON = (By.XPATH, "//div[@class='pr_profile__buttons']/button")

    INACTIVE_CONTINUE_BUTTON = (By.XPATH, "//button[@disabled]")

    ADD_PHOTO = (By.XPATH, "//p[@class='pr_profile__avatar_btn']")

    AVATAR = (By.XPATH, "//img[@class='avatar-thumb']")
