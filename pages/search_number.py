from selenium.webdriver.common.keys import Keys

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

    def search_number_and_return(self, number=""):
        elem = self.find_element(self.locator.SEARCH_BY_CLASS)
        elem.send_keys(number)
        elem.send_keys(Keys.RETURN)

    def type_message(self, message=""):
        elem = self.find_element(self.locator.MESSAGE_BOX_BY_XPATH)
        elem.send_keys(message)

    def enter_message(self, message=""):
        self.type_message(message)
        elem = self.find_element(self.locator.SEND_BUTTON)
        elem.click()
