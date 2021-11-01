from selenium.webdriver.common.by import By


class PageLocator:
    SEARCH_BY_CLASS = (By.CLASS_NAME, '_3Qnsr')
    SEARCH_BY_XPATH = (By.XPATH, '//*[@id="side"]/div[1]/div/div')
    MESSAGE_BOX_BY_XPATH = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[1]')