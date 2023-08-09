import allure

from tests.UI.page_objects.login_page import LogInPage
from tests.UI.page_objects.main_page import MainPage
from tests.UI.page_objects.products_page import ProductsPage
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

    with allure.step('Go to register page'):
        main_page.find_register_btn().click()
    with allure.step('Fill required fields'):
        register_page.create_random_user()
    with allure.step('Click register button'):
        register_page.find_register_btn().click()
    with allure.step('Check success registration text'):
        register_page.check_success_registration()


@allure.title('Register new user required fields are empty')
def test_register_new_user_empty_fields(browser, base_url):
    """
    Register new user required fields are empty
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    register_page = RegisterPage(browser)

    with allure.step('Go to register page'):
        main_page.find_register_btn().click()
    with allure.step('Click register button'):
        register_page.find_register_btn().click()
    with allure.step('Check all required fields for error message'):
        register_page.find_first_name_error()
        register_page.find_last_name_error()
        register_page.find_email_error()
        register_page.find_password_error()
        register_page.find_password_confirm_error()


@allure.title('Add book to the cart')
def test_add_book_to_cart(browser, base_url):
    """
    Add book to the cart and check quantity
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    products_page = ProductsPage(browser)

    with allure.step('Go to books page'):
        main_page.find_books_btn().click()
    with allure.step('Number of products is 3'):
        products_page.check_products_number(3)
    with allure.step('Check the cart quantity'):
        main_page.check_element_text(main_page.SHOPPINGCART_QTY, '(0)')
    with allure.step('Check first book title is Fahrenheit 451 by Ray Bradbury'):
        products_page.check_first_book_title('Fahrenheit 451 by Ray Bradbury')
    with allure.step('Add the book to the cart'):
        products_page.find_first_book_add_to_cart_btn().click()
    with allure.step('Check and close notification bar'):
        products_page.check_notification_add_to_cart_success_text()
        products_page.find_notification_close_btn().click()
    with allure.step('Check new cart quantity'):
        main_page.check_element_text(main_page.SHOPPINGCART_QTY, '(1)')


@allure.title('Add book to wl')
def test_add_book_to_wl(browser, base_url):
    """
    Add book to wl and check quantity
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    products_page = ProductsPage(browser)

    with allure.step('Go to books page'):
        main_page.find_books_btn().click()
    with allure.step('Check the wl quantity'):
        main_page.check_element_text(main_page.WL_QTY, '(0)')
    with allure.step('Check first book title is Fahrenheit 451 by Ray Bradbury'):
        products_page.check_first_book_title('Fahrenheit 451 by Ray Bradbury')
    with allure.step('Add the book to wl'):
        products_page.find_first_book_add_to_wl_btn().click()
    with allure.step('Check and close notification bar'):
        products_page.check_notification_add_to_wl_success_text()
        products_page.find_notification_close_btn().click()
    with allure.step('Check new cart quantity'):
        main_page.check_element_text(main_page.WL_QTY, '(1)')


@allure.title('Search products')
def test_search_products(browser, base_url):
    """
    Search products
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    products_page = ProductsPage(browser)

    with allure.step('Input search request'):
        main_page.find_search_field().send_keys('APPLE')
    with allure.step('Click search button'):
        main_page.find_search_btn().click()
    with allure.step('Check that results are equal 2'):
        products_page.check_products_number(2)
    with allure.step('Check that results have APPLE in title'):
        products_page.check_search_results('APPLE')


@allure.title('Bad user Login')
def test_bad_user_login(browser, base_url):
    """
    Bad user login
    """
    browser.get(base_url)
    main_page = MainPage(browser)
    login_page = LogInPage(browser)

    with allure.step('Go to LoogIn page'):
        main_page.find_login_btn().click()
    with allure.step('Check main page texte'):
        login_page.check_page_text()
    with allure.step('Left empty fields and click login'):
        login_page.find_login_btn().click()
    with allure.step('Check email error message'):
        login_page.check_email_error_text()
