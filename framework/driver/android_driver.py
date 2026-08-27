from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from framework.config.config import MobileConfig
# from framework.driver.base_driver import BaseMobileDriver
#
#
# class AndroidDriver(BaseMobileDriver):   # this is inheritance inherting BaseMobileDriver
#
#     def create_driver(self):
#
#         options = UiAutomator2Options()
#
#         options.platform_name = self.config.platform_name
#         options.device_name = self.config.device_name
#         options.automation_name = self.config.automation_name
#         options.app_package = self.config.app_package
#         options.app_activity = self.config.app_activity
#         options.new_command_timeout = self.config.new_command_timeout
#
#         return webdriver.Remote(
#             self.config.server_url,
#             options=options
#         )


from appium import webdriver
from appium.options.android import UiAutomator2Options

from framework.config.config import MobileConfig
from framework.driver.base_driver import BaseMobileDriver


class AndroidDriver(BaseMobileDriver):
    """
    Creates and returns an Appium driver for Android.
    """

    def create_driver(self):

        options = UiAutomator2Options()

        options.platform_name = self.config.platform_name.value
        options.device_name = self.config.device_name
        options.automation_name = self.config.automation_name
        options.app_package = self.config.app_package
        options.app_activity = self.config.app_activity
        options.new_command_timeout = self.config.new_command_timeout

        return webdriver.Remote(
            self.config.server_url,
            options=options
        )

#def create_driver(self):
# both class android_driver.py and ios_driver.py have create_driver() function but they behave differenlty
# same function will call android drsired caps and ios desired caps so one function is being used for two
#purpose that is call ploymorphism