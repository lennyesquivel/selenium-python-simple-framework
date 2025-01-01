from selenium.webdriver.common.by import By


class ResultsPageLocators(object):
    result_titles = dict(type=By.XPATH, value="//div[contains(@class, 'g')]//h3")
