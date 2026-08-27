# from appium import webdriver
# from appium.options.android import UiAutomator2Options
#
#
# def test_launch_api_demos(driver):
#
#     print("Application launched successfully")
from framework.config.platform import Platform


def test_config(config):

    print(f"Environment: {config.environment}")
    print(f"Platform: {config.platform_name.value}")
    print(f"Device: {config.device_name}")

    assert config.environment in ["qa", "staging", "prod"]
    assert config.platform_name == Platform.ANDROID