from selenium.webdriver.common.by import By

from tests.UI.page_objects.base_page import BasePage


class ProductsPage(BasePage):
    PRODUCTS_ITEMS = (By.CSS_SELECTOR, '.item-box')
    FIRST_BOOK_ADD_TO_CART_BTN = (
        By.XPATH, "//*[@data-productid=37]//button[contains(@class,'product-box-add-to-cart-button')]")
    FIRST_BOOK_ADD_TO_WL = (
        By.XPATH, "//*[@data-productid=37]//button[contains(@class,'add-to-wishlist-button')]")
    FIRST_BOOK_TITLE = (By.XPATH, "//*[@data-productid=37]//*[@class='product-title']/a")
    NOTIFICATION_CLOSE = (By.CSS_SELECTOR, '.close')
    NOTIFICATION_SUCCESS_TEXT = (By.XPATH, "//p[@class='content']")
    ACTUAL_PRICE = (
        By.XPATH, "//*[@data-productid=37]//span[contains(@class,'price actual-price')]")
    CURRENCY_SELECTOR = (By.CSS_SELECTOR, "#customerCurrency")
    CURRENCY_USD = (By.XPATH, "//option[text()='US Dollar']")
    CURRENCY_EURO = (By.XPATH, "//option[text()='Euro']")
    VIEW_GRID_BTN = (By.XPATH, "//a[@data-viewmode='grid']")
    VIEW_LIST_BTN = (By.XPATH, "//a[@data-viewmode='list']")
    GRID_VIEW = (By.XPATH, "//*[@class='product-grid']//*[@class='item-box']")
    LIST_VIEW = (By.XPATH, "//*[@class='product-list']//*[@class='item-box']")

    def find_first_book_title(self):
        return self.element(self.FIRST_BOOK_TITLE)

    def find_first_book_add_to_cart_btn(self):
        return self.element(self.FIRST_BOOK_ADD_TO_CART_BTN)

    def find_first_book_add_to_wl_btn(self):
        return self.element(self.FIRST_BOOK_ADD_TO_WL)

    def check_products_number(self, number):
        self.check_len_elements(self.PRODUCTS_ITEMS, number)

    def check_products_view_list_number(self, number):
        self.check_len_elements(self.LIST_VIEW, number)

    def check_products_view_grid_number(self, number):
        self.check_len_elements(self.GRID_VIEW, number)

    def check_first_book_title(self, title):
        self.check_element_text(self.FIRST_BOOK_TITLE, title)

    def check_notification_add_to_cart_success_text(self):
        self.check_element_text(self.NOTIFICATION_SUCCESS_TEXT, 'The product has been added to your shopping cart')

    def check_notification_add_to_wl_success_text(self):
        self.check_element_text(self.NOTIFICATION_SUCCESS_TEXT, 'The product has been added to your wishlist')

    def find_notification_close_btn(self):
        return self.element(self.NOTIFICATION_CLOSE)

    def check_search_results(self, search_text):
        result_items = self.elements(self.PRODUCTS_ITEMS)
        for item in result_items:
            words = item.text.split()
            lowercase_list = [word.lower() for word in words]

            assert search_text.lower() in lowercase_list, f"Search word {search_text} not in {item.text}"

    def check_actual_usd_price(self, price):
        self.check_element_text(self.ACTUAL_PRICE, price)

    def check_actual_euro_price(self, price):
        self.check_element_text(self.ACTUAL_PRICE, price)

    def find_currency_selector(self):
        return self.element(self.CURRENCY_SELECTOR)

    def find_currency_euro(self):
        return self.element(self.CURRENCY_EURO)

    def find_currency_usd(self):
        return self.element(self.CURRENCY_USD)

    def change_currency_to_euro(self):
        self.find_currency_selector().click()
        self.find_currency_euro().click()

    def change_currency_to_usd(self):
        self.find_currency_selector().click()
        self.find_currency_usd().click()

    def find_grid_view(self):
        return self.element(self.VIEW_GRID_BTN)

    def find_list_view(self):
        return self.element(self.VIEW_LIST_BTN)
