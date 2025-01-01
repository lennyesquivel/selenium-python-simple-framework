from selenium.webdriver.common.by import By


class HomePageLocators(object):
    search_input = dict(type=By.NAME, value="q")
    search_button = dict(type=By.NAME, value="btnK")
