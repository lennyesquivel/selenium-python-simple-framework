from Src.PageObject.Pages.HomePageLocators import HomePageLocators


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.search_input = driver.find_element(HomePageLocators.search_input.get("type"),
                                                HomePageLocators.search_input.get("value"))
        self.search_button = driver.find_element(HomePageLocators.search_button.get("type"),
                                                 HomePageLocators.search_button.get("value"))

    def get_search_input(self):
        return self.search_input

    def get_search_button(self):
        return self.search_button
