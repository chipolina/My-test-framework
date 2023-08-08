import allure

from tests.UI.page_objects.main_page import MainPage
from tests.UI.page_objects.register_page import RegisterPage


@allure.title('first')
def test_check_main_page_elements(browser, base_url):
    """
    Check number of Categories
    """
    browser.get(base_url)
    with allure.step('Check number of Categories'):
        MainPage(browser).check_len_elements(MainPage.CATEGORIES, 7)

@allure.title('second')
def test_register_new_user(browser, base_url):
    """
    Register new user
    """
    browser.get(base_url)
    with allure.step('Click register button'):
        MainPage(browser).find_register_btn().click()
    with allure.step('Fill required fields'):
        RegisterPage(browser).create_random_user()
    with allure.step('Click register button'):
        RegisterPage(browser).find_register_btn().click()
    with allure.step('Check success registration text'):
        RegisterPage(browser).check_success_registration()

