# from pages.base_page import BasePage
#
#
# class ApiDemosPage(BasePage):
#
#     ACCESSIBILITY = (
#         "accessibility id",
#         "Accessibility"
#     )
#
#     def tap_accessibility(self):
#         self.click(self.ACCESSIBILITY)

from pages.base_page import BasePage

from locators.android.api_demos_locators import (
    ACCESSIBILITY_MENU,
    ACCESSIBILITY_NODE_PROVIDER,
    VIEWS_MENU,
    VIEWS_SCREEN_INDICATOR,
    WEBVIEW3_MENU,
)


class ApiDemosPage(BasePage):

    def open_accessibility(self):
        self.click(ACCESSIBILITY_MENU)

    def open_views(self):
        self.click(VIEWS_MENU)

    def is_accessibility_screen_displayed(self):
        return self.is_displayed(ACCESSIBILITY_NODE_PROVIDER)

    def is_views_screen_displayed(self):
        return self.is_displayed(VIEWS_SCREEN_INDICATOR)

    def scroll_views_to_bottom(self):
        self.scroll_to_bottom()

    def is_webview3_displayed(self):
        return self.is_displayed(WEBVIEW3_MENU)

    def scroll_until_webview3_visible(self):

        return self.scroll_until_visible(WEBVIEW3_MENU)



# class ApiDemosPage(BasePage)  -> example of inheritance inherting basepage and it's functionality