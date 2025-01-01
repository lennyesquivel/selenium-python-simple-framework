import unittest
from selenium import webdriver


class WebDriverUtil(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
