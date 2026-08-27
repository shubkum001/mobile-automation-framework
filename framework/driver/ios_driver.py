from appium import webdriver
from appium.options.ios import XCUITestOptions
from framework.driver.base_driver import BaseMobileDriver


class IOSDriver(BaseMobileDriver):

    def create_driver(self):

        options = XCUITestOptions()

        options.platform_name = self.config.platform_name.value
        options.device_name = self.config.device_name
        options.automation_name = self.config.automation_name
        options.bundle_id = self.config.app_package
        options.new_command_timeout = self.config.new_command_timeout

        return webdriver.Remote(
            self.config.server_url,
            options=options
        )

#def create_driver(self):
# both class android_driver.py and ios_driver.py have create_driver() function but they behave differenlty
# same function will call android drsired caps and ios desired caps so one function is being used for two
#purpose that is call ploymorphism