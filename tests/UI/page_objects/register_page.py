import time

from selenium.webdriver.common.by import By

from src.helper import generate_email, generate_text
from tests.UI.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    GENDER_MALE = (By.CSS_SELECTOR, "#gender-male")
    FIRST_NAME = (By.CSS_SELECTOR, "#FirstName")
    FIRST_NAME_ERROR = (By.CSS_SELECTOR, "#FirstName-error")
    LAST_NAME = (By.CSS_SELECTOR, "#LastName")
    LAST_NAME_ERROR = (By.CSS_SELECTOR, "#LastName-error")
    DOB_DAY = (By.XPATH, "//select[@name='DateOfBirthDay']")
    DOB_CUR_DAY = (By.XPATH, "//select[@name='DateOfBirthDay']//option[@value='20']")
    DOB_MONTH = (By.XPATH, "//select[@name='DateOfBirthMonth']")
    DOB_CUR_MONTH = (By.XPATH, "//select[@name='DateOfBirthMonth']//option[@value='7']")
    DOB_YEAR = (By.XPATH, "//select[@name='DateOfBirthYear']")
    DOB_CUR_YEAR = (By.XPATH, "//select[@name='DateOfBirthYear']//option[@value='2012']")
    EMAIL = (By.CSS_SELECTOR, "#Email")
    EMAIL_ERROR = (By.CSS_SELECTOR, "#Email-error")
    PASSWORD = (By.CSS_SELECTOR, "#Password")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#Password-error")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#ConfirmPassword")
    PASSWORD_CONFIRM_ERROR = (By.CSS_SELECTOR, "#ConfirmPassword-error")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register-button")
    REGISTRATION_SUCCESS = (By.XPATH, "//*[@class='result']")

    def find_register_btn(self):
        return self.element(self.REGISTER_BTN)

    def find_register_succes(self):
        return self.element(self.REGISTRATION_SUCCESS)

    def create_random_user(self):
        password = generate_text(10)
        email = generate_email()
        # self.element(self.GENDER_MALE).click()
        self.element(self.FIRST_NAME).send_keys(generate_text(10))
        self.element(self.LAST_NAME).send_keys(generate_text(10))
        self.element(self.EMAIL).send_keys(email)
        self.element(self.PASSWORD).send_keys(password)
        self.element(self.PASSWORD_CONFIRM).send_keys(password)
        return email, password

    def check_success_registration(self):
        self.check_element_text(self.REGISTRATION_SUCCESS, 'Your registration completed')
