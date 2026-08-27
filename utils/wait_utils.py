from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait



class WaitUtils:

    def __init__(
        self,
        driver: WebDriver,
        timeout: int = 10,
    ):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element(self, locator: tuple):

        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            lambda driver: driver.find_element(*locator)
        )

    def wait_for_presence(self, locator: tuple):

        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(
            lambda driver: driver.find_element(*locator)
        )

    def wait_for_visible(self, locator: tuple):

        def element_is_visible(driver):

            element = driver.find_element(*locator)

            if element.is_displayed():
                return element

            return False

        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(element_is_visible)

    def wait_for_clickable(self, locator: tuple):

        def element_is_clickable(driver):

            element = driver.find_element(*locator)

            if element.is_displayed() and element.is_enabled():
                return element

            return False

        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(element_is_clickable)

    def wait_for_element_gone(self, locator: tuple):

        def element_is_gone(driver):

            try:
                element = driver.find_element(*locator)
                return not element.is_displayed()

            except Exception:
                return True

        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(element_is_gone)

    def wait_for_text(self, locator: tuple, expected_text: str):

        def text_is_present(driver):

            element = driver.find_element(*locator)

            return (
                expected_text in element.text
            )

        return WebDriverWait(
            self.driver,
            self.timeout
        ).until(text_is_present)