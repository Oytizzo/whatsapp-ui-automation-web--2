# =============================================================
# this code was used to get the phone number from xlsx

#
#

# ==============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from pages.search_number import SearchNumber
from utils.locators import PageLocator
from utils.helper import XlsxSheet

driver = webdriver.Chrome()
webpage = BasePage(driver)
webpage.open()

input("Scan the QR code than press enter ")

number_sheet = XlsxSheet("number_for_whatsapp.xlsx", 'a1')
number = number_sheet.get_numbers_from_xlsx()
print(len(number))
print(number)
print(type(number))

print("implicitly_wait 5 sec from now")
driver.implicitly_wait(5)
search_box = SearchNumber(driver)
search_box.open()
print("done opening search_box")

a = driver.find_element(By.CLASS_NAME, '_13NKt')
print(a)
a.get_attribute("innerHTML")
a.send_keys(number)

print("searched the number")
