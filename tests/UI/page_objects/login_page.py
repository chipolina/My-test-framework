from selenium.webdriver.common.by import By

from tests.UI.page_objects.base_page import BasePage


class LogInPage(BasePage):
    PAGE_TEXT = (By.XPATH, "//*[@class='page-title']/h1")
    EMAIL = (By.CSS_SELECTOR, "#Email")
    EMAIL_ERROR = (By.CSS_SELECTOR, "#Email-error")
    PASSWORD = (By.CSS_SELECTOR, "#Password")
    LOGIN_BTN = (By.XPATH, "//button[@class='button-1 login-button']")

    def check_page_text(self):
        self.check_element_text(self.PAGE_TEXT, 'Welcome, Please Sign In!')

    def check_email_error_text(self):
        self.check_element_text(self.EMAIL_ERROR, 'Please enter your email')

    def find_login_btn(self):
        return self.element(self.LOGIN_BTN)
