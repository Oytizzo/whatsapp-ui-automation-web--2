from utils.locators import PageLocator
from pages.base_page import BasePage


class SearchNumber(BasePage):
    """"takes two paremeter
    driver
    url = https://web.whatsapp.com/send?phone={phone_number}"""
    def __init__(self, driver):
        self.locator = PageLocator
        super().__init__(driver)

    def click_search_button(self):
        self.find_element(*self.locator.SEARCH_BY_CLASS).click()

    def search_number(self, number=""):
        self.find_element(self.locator.SEARCH_BY_CLASS).send_keys(number)
