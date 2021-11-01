import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# If you want to run it, you should type: python <module-name.py>


class BaseTest(unittest.TestCase):
    """BaseTest is the base class for every test class inheritence"""
    def setUp(self) -> None:
        options = Options()

        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://web.whatsapp.com/")

    def tearDown(self) -> None:
        self.driver.close()


# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
