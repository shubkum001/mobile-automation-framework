from appium.webdriver.webdriver import WebDriver

from framework.exceptions.framework_exceptions import (
    ElementInteractionException,
)
from utils.logger import get_logger
from utils.wait_utils import WaitUtils


logger = get_logger(__name__)


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def click(self, locator: tuple):

        try:
            logger.info("Clicking element: %s", locator)

            element = self.wait.wait_for_clickable(locator)
            element.click()

        except Exception as exc:
            logger.exception(
                "Failed to click element: %s",
                locator
            )

            raise ElementInteractionException(
                f"Failed to click element: {locator}"
            ) from exc

    def enter_text(self, locator: tuple, text: str):

        try:
            logger.info(
                "Entering text into element: %s",
                locator
            )

            element = self.wait.wait_for_visible(locator)

            element.clear()
            element.send_keys(text)

        except Exception as exc:
            logger.exception(
                "Failed to enter text into element: %s",
                locator
            )

            raise ElementInteractionException(
                f"Failed to enter text into element: {locator}"
            ) from exc

    def get_text(self, locator: tuple) -> str:

        try:
            logger.info(
                "Getting text from element: %s",
                locator
            )

            element = self.wait.wait_for_visible(locator)

            return element.text

        except Exception as exc:
            logger.exception(
                "Failed to get text from element: %s",
                locator
            )

            raise ElementInteractionException(
                f"Failed to get text from element: {locator}"
            ) from exc

    def is_displayed(self, locator: tuple) -> bool:

        try:
            element = self.wait.wait_for_visible(locator)

            return element.is_displayed()

        except Exception:
            return False

    def wait_for_element(self, locator: tuple):

        try:
            logger.info(
                "Waiting for element: %s",
                locator
            )

            return self.wait.wait_for_visible(locator)

        except Exception as exc:
            logger.exception(
                "Failed to wait for element: %s",
                locator
            )

            raise ElementInteractionException(
                f"Element was not found: {locator}"
            ) from exc

    def hide_keyboard(self):

        try:
            logger.info("Hiding keyboard")

            self.driver.hide_keyboard()

        except Exception as exc:
            logger.exception(
                "Failed to hide keyboard"
            )

            raise ElementInteractionException(
                "Failed to hide keyboard"
            ) from exc

    def scroll_down(self):

        try:
            logger.info("Scrolling down")

            size = self.driver.get_window_size()

            width = size["width"]
            height = size["height"]

            start_x = width // 2
            start_y = int(height * 0.80)

            end_x = width // 2
            end_y = int(height * 0.20)

            self.driver.swipe(
                start_x,
                start_y,
                end_x,
                end_y,
                800
            )

        except Exception as exc:
            logger.exception("Failed to scroll down")

            raise ElementInteractionException(
                "Failed to scroll down"
            ) from exc

    def scroll_to_bottom(self, max_swipes: int = 10):

        try:

            logger.info(
                "Scrolling to bottom with maximum %s swipes",
                max_swipes
            )

            previous_page_source = None

            for swipe_count in range(1, max_swipes + 1):

                current_page_source = self.driver.page_source

                if current_page_source == previous_page_source:
                    logger.info(
                        "Bottom reached after %s swipes",
                        swipe_count - 1
                    )

                    return

                previous_page_source = current_page_source

                logger.info(
                    "Performing scroll %s/%s",
                    swipe_count,
                    max_swipes
                )

                self.scroll_down()

            logger.info(
                "Maximum scroll limit reached: %s swipes",
                max_swipes
            )

        except Exception as exc:

            logger.exception(
                "Failed to scroll to bottom"
            )

            raise ElementInteractionException(
                "Failed to scroll to bottom"
            ) from exc

    def scroll_until_visible(self, locator: tuple, max_swipes: int = 10) -> bool:

        try:

            logger.info(
                "Scrolling until element is visible: %s",
                locator
            )

            for swipe_count in range(1, max_swipes + 1):

                if self.is_displayed(locator):
                    logger.info(
                        "Element is visible after %s swipe(s): %s",
                        swipe_count - 1,
                        locator
                    )

                    return True

                logger.info(
                    "Element not visible. Performing scroll %s/%s",
                    swipe_count,
                    max_swipes
                )

                self.scroll_down()

            if self.is_displayed(locator):
                logger.info(
                    "Element became visible after maximum scroll attempt: %s",
                    locator
                )

                return True

            logger.warning(
                "Element was not visible after %s swipes: %s",
                max_swipes,
                locator
            )

            return False

        except Exception as exc:

            logger.exception(
                "Failed to scroll until element is visible: %s",
                locator
            )

            raise ElementInteractionException(
                f"Failed to scroll until element is visible: {locator}"
            ) from exc