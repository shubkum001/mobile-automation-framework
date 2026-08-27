from appium.webdriver.webdriver import WebDriver

from framework.config.config import MobileConfig
from framework.config.platform import Platform
from framework.driver.android_driver import AndroidDriver
from framework.driver.ios_driver import IOSDriver
from framework.exceptions.framework_exceptions import (
    DriverInitializationException,
)
from utils.logger import get_logger


logger = get_logger(__name__)


class DriverFactory:

    @staticmethod
    def create_driver(config: MobileConfig) -> WebDriver:

        try:

            logger.info(
                "Creating driver for platform: %s",
                config.platform_name.value
            )

            if config.platform_name == Platform.ANDROID:
                return AndroidDriver(config).create_driver()

            if config.platform_name == Platform.IOS:
                return IOSDriver(config).create_driver()

            raise ValueError(
                f"Unsupported platform: {config.platform_name}"
            )

        except Exception as exc:

            logger.exception(
                "Failed to create driver for platform: %s",
                config.platform_name
            )

            raise DriverInitializationException(
                f"Failed to create driver for platform: "
                f"{config.platform_name}"
            ) from exc


 # static method because as now no need of instance because it doesnot have anything to initiate

 #(def create_driver(config: MobileConfig) -> WebDriver:) this is called hinitng -> Create a function called create_driver, which accepts a MobileConfig and returns a WebDriver.