# def test_open_accessibility(pages):
#
#     pages.api_demos.open_accessibility()
#
#     assert pages.api_demos.is_accessibility_screen_displayed(), (
#         "Accessibility screen was not displayed"
#     )

import pytest
import allure

@allure.feature("API Demos")
@allure.story("Views Navigation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_open_views(pages):

    with allure.step("Open Views menu"):
        pages.api_demos.open_views()

    with allure.step("Verify Views screen is displayed"):
        assert pages.api_demos.is_views_screen_displayed(), (
            "Views screen was not displayed"
        )

@pytest.mark.regression
def test_scroll_until_webview3_visible(pages):

    pages.api_demos.open_views()

    is_visible = pages.api_demos.scroll_until_webview3_visible()

    assert is_visible, (
        "WebView3 was not displayed after scrolling"
    )

