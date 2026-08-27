# from pages.base_page import BasePage
#
#
# class LoginPage(BasePage):
#
#     USERNAME = (
#         "id",
#         "com.example.app:id/username"
#     )
#
#     PASSWORD = (
#         "id",
#         "com.example.app:id/password"
#     )
#
#     LOGIN_BUTTON = (
#         "id",
#         "com.example.app:id/login"
#     )
#
#     def enter_username(self, username: str):
#         self.enter_text(
#             self.USERNAME,
#             username
#         )
#
#     def enter_password(self, password: str):
#         self.enter_text(
#             self.PASSWORD,
#             password
#         )
#
#     def click_login(self):
#         self.click(
#             self.LOGIN_BUTTON
#         )
#
#     def login(self, username: str, password: str):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()

from pages.base_page import BasePage

from locators.android.login_locators import (
    USERNAME_FIELD,
    PASSWORD_FIELD,
    LOGIN_BUTTON,
    LOGIN_ERROR_MESSAGE,
)


class LoginPage(BasePage):

    def enter_username(self, username: str):

        self.enter_text(
            USERNAME_FIELD,
            username
        )

    def enter_password(self, password: str):

        self.enter_text(
            PASSWORD_FIELD,
            password
        )

    def click_login(self):

        self.click(LOGIN_BUTTON)

    def login(self, username: str, password: str):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_error_displayed(self) -> bool:

        return self.is_displayed(
            LOGIN_ERROR_MESSAGE
        )