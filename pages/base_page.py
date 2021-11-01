from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base class for basic attributes for every other pages."""
    def __init__(self, driver, base_url="https://web.whatsapp.com/"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open(self):
        self.driver.get(self.base_url)

    def wait_element(self, *locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * Element not found within given time. --> %s" %(locator[1]))
        except Exception as e:
            print(e)
