from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Src.PageObject.Pages.ResultsPageLocators import ResultsPageLocators


class ResultsPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.results = self.driver.find_elements(ResultsPageLocators.result_titles.get("type"),
                                                 ResultsPageLocators.result_titles.get("value"))

    def get_results(self):
        return self.results

    def wait_for_results(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(
            (ResultsPageLocators.result_titles.get("type"), ResultsPageLocators.result_titles.get("value"))))
