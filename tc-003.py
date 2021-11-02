import openpyxl
import time
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

print("=" * 50)
input("Scan the QR code than press enter ")
print("=" * 50)

number_sheet = XlsxSheet("number_for_whatsapp.xlsx", 'a1')
number = number_sheet.get_numbers_from_xlsx()

driver.implicitly_wait(5)
search_box = SearchNumber(driver)
search_box.open()

search_box.search_number_and_return(number)
msg = "Hello world"
search_box.enter_message(msg)
print("==============TC-002==============")

print("sleeping for 10 sec")
time.sleep(10)
msg_check_list = search_box.msg_check()
last_msg = msg_check_list[len(msg_check_list)-1]
aria_label = last_msg.get_attribute("aria-label").strip()

wb = openpyxl.load_workbook("number_for_whatsapp.xlsx")
sheet = wb['Sheet1']
cell = sheet['b1']
cell.value = aria_label
wb.save("update_whatsapp.xlsx")
print("=========================saved to xlsx===================")
print("======================TC-003 and TC-004===============")
