import pytest

from utils.test_data_reader import load_login_test_data


login_data = load_login_test_data("android")


@pytest.mark.smoke
@pytest.mark.parametrize(
    "data",
    login_data,
    ids=[item.test_case for item in login_data]
)
def test_login_data_parameterization(data):

    print(f"Test Case: {data.test_case}")
    print(f"Username: {data.username}")
    print(f"Expected Result: {data.expected_result}")


# import pytest
#
# from utils.test_data_reader import load_login_test_data
#
#
# login_data = load_login_test_data("android")


# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "data",
#     login_data,
#     ids=[item.test_case for item in login_data]
# )
# def test_login_data_parameterization(pages, data):
#
#     pages.login.login(
#         data.username,
#         data.password
#     )
#
#     if data.expected_result == "success":
#
#         # We'll add the successful-login assertion
#         # after confirming the actual application screen.
#         pass
#
#     else:
#
#         assert pages.login.is_login_error_displayed(), (
#             f"Login error was not displayed for: {data.test_case}"
#         )