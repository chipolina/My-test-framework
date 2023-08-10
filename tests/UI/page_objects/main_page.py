from selenium.webdriver.common.by import By

from tests.UI.page_objects.base_page import BasePage


class MainPage(BasePage):
    REGISTER = (By.CSS_SELECTOR, ".ico-register")
    LOGIN = (By.CSS_SELECTOR, ".ico-login")
    SHOPPINGCART = (By.CSS_SELECTOR, ".ico-cart")
    SHOPPINGCART_QTY = (By.CSS_SELECTOR, ".cart-qty")
    WL_QTY = (By.CSS_SELECTOR, ".wishlist-qty")
    BOOKS = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(@href,'/books')]")
    CATEGORIES = (
        By.XPATH, "//ul[@class='top-menu notmobile']//a[not(ancestor::ul[contains(@class, 'sublist first-level')])]")
    SEARCH_FIELD = (By.CSS_SELECTOR, '#small-searchterms')
    SEARCH_BTN = (By.XPATH, "//button[contains(@class,'search-box-button')]")
    FACEBOOK = (By.XPATH, "//li[@class='facebook']/a")
    TWITTER = (By.XPATH, "//li[@class='twitter']/a")
    RSS = (By.XPATH, "//li[@class='rss']/a")
    YOUTUBE = (By.XPATH, "//li[@class='youtube']/a")

    def find_register_btn(self):
        return self.element(self.REGISTER)

    def find_login_btn(self):
        return self.element(self.LOGIN)

    def find_books_btn(self):
        return self.element(self.BOOKS)

    def find_search_field(self):
        return self.element(self.SEARCH_FIELD)

    def find_search_btn(self):
        return self.element(self.SEARCH_BTN)

    def check_elements_number(self, number):
        self.check_len_elements(self.CATEGORIES, number)

    def check_shopping_cart_qty(self, title):
        self.check_element_text(self.SHOPPINGCART_QTY, title)

    def check_wl_qty(self, title):
        self.check_element_text(self.WL_QTY, title)

    def find_fb(self):
        return self.element(self.FACEBOOK)

    def find_twitter(self):
        return self.element(self.TWITTER)

    def find_rss(self):
        return self.RSS

    def find_youtube(self):
        return self.element(self.YOUTUBE)

    def check_social_networks(self):
        self.find_fb()
        self.find_twitter()
        self.find_rss()
        self.find_youtube()
