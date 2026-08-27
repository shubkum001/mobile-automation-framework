from pathlib import Path

from appium.webdriver.webdriver import WebDriver

from utils.logger import get_logger


logger = get_logger(__name__)


class ArtifactUtils:

    ARTIFACTS_DIR = Path("artifacts")
    SCREENSHOT_DIR = ARTIFACTS_DIR / "screenshots"
    PAGE_SOURCE_DIR = ARTIFACTS_DIR / "page_source"

    @classmethod
    def _create_directories(cls):

        cls.SCREENSHOT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        cls.PAGE_SOURCE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    @classmethod
    def save_screenshot(
        cls,
        driver: WebDriver,
        test_name: str
    ):

        cls._create_directories()

        screenshot_path = (
            cls.SCREENSHOT_DIR / f"{test_name}.png"
        )

        try:

            driver.save_screenshot(
                str(screenshot_path)
            )

            logger.info(
                "Screenshot saved: %s",
                screenshot_path
            )

            return screenshot_path

        except Exception:

            logger.exception(
                "Failed to save screenshot: %s",
                screenshot_path
            )

            return None

    @classmethod
    def save_page_source(
        cls,
        driver: WebDriver,
        test_name: str
    ):

        cls._create_directories()

        page_source_path = (
            cls.PAGE_SOURCE_DIR / f"{test_name}.xml"
        )

        try:

            page_source = driver.page_source

            page_source_path.write_text(
                page_source,
                encoding="utf-8"
            )

            logger.info(
                "Page source saved: %s",
                page_source_path
            )

            return page_source_path

        except Exception:

            logger.exception(
                "Failed to save page source: %s",
                page_source_path
            )

            return None