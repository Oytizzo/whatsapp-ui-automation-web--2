from selenium.webdriver.common.by import By


class PageLocator:
    SEARCH_BY_CLASS = (By.CLASS_NAME, '_13NKt')
    MESSAGE_BOX_BY_XPATH = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    SEND_BUTTON = (By.CLASS_NAME, '_4sWnG')
    # MSG_CHECK = (By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[2]/div[6]/div/div/div/div[2]/div/div/span')
    MSG_CHECK = (By.CSS_SELECTOR, 'div._2F01v > span')
    # MENU = (By.CLASS_NAME, '_2cNrC')
    MENU = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]')
    LOGOUT = (By.XPATH, '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]/div[1]')
