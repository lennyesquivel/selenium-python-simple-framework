import unittest
from selenium.webdriver.common.keys import Keys

from time import sleep
from Src.Utils.WebDriverUtil import WebDriverUtil
from Src.PageObject.Pages.HomePage import HomePage
from Src.PageObject.Pages.ResultsPage import ResultsPage


class HomePageTest(WebDriverUtil):
    def test_home_page_search(self):
        search_term = "hannah montana linux"
        driver = self.driver
        driver.get("https://www.google.com")
        home_page = HomePage(driver)
        search_input = home_page.get_search_input()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)
        sleep(3)
        results_page = ResultsPage(driver)
        results = results_page.get_results()
        for result in results:
            if result.text:
                print("found: " + result.text)
                self.assertTrue(search_term in result.text.lower())


if __name__ == '__main__':
    unittest.main()
