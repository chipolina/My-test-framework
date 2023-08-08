import allure

from tests.UI.page_objects.main_page import MainPage
from tests.UI.page_objects.register_page import RegisterPage


@allure.title('Check the number of categories')
def test_check_main_page_elements(browser, base_url):
    """
    Check the number of Categories
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    with allure.step('Check the number of Categories'):
        main_page.check_len_elements(MainPage.CATEGORIES, 7)


@allure.title('Register new user')
def test_register_new_user(browser, base_url):
    """
    Register new user
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    register_page = RegisterPage(browser)

    with allure.step('Click register button'):
        main_page.find_register_btn().click()
    with allure.step('Fill required fields'):
        register_page.create_random_user()
    with allure.step('Click register button'):
        register_page.find_register_btn().click()
    with allure.step('Check success registration text'):
        register_page.check_success_registration()
