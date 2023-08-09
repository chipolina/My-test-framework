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

    def find_first_book_title(self):
        return self.element(self.FIRST_BOOK_TITLE)

    def find_first_book_add_to_cart_btn(self):
        return self.element(self.FIRST_BOOK_ADD_TO_CART_BTN)

    def find_first_book_add_to_wl_btn(self):
        return self.element(self.FIRST_BOOK_ADD_TO_WL)

    def check_products_number(self, number):
        self.check_len_elements(self.PRODUCTS_ITEMS, number)

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

            assert search_text.lower() in lowercase_list
