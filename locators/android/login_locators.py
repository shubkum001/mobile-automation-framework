from appium.webdriver.common.appiumby import AppiumBy


USERNAME_FIELD = (
    AppiumBy.ACCESSIBILITY_ID,
    "Username"
)

PASSWORD_FIELD = (
    AppiumBy.ACCESSIBILITY_ID,
    "Password"
)

LOGIN_BUTTON = (
    AppiumBy.ACCESSIBILITY_ID,
    "Login"
)

LOGIN_ERROR_MESSAGE = (
    AppiumBy.ACCESSIBILITY_ID,
    "Login failed"
)