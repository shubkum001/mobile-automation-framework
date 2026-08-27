from pages.api_demos_page import ApiDemosPage
from pages.login_page import LoginPage


class PageObjects:

    def __init__(self, driver):

        self.driver = driver

        self.api_demos = ApiDemosPage(driver)
        self.login = LoginPage(driver)