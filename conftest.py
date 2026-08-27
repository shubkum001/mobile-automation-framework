from dataclasses import replace
from utils.artifact_utils import ArtifactUtils
from _pytest.nodes import Item
import allure
import pytest

from framework.config.config_reader import load_config
from framework.config.platform import Platform
from framework.driver.driver_factory import DriverFactory
from pages.page_objects import PageObjects
from utils.logger import get_logger

logger = get_logger(__name__)


def pytest_addoption(parser):

    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to execute tests against"
    )

    parser.addoption(
        "--platform",
        action="store",
        default=None,
        help="Platform to execute tests against: android or ios"
    )




@pytest.fixture(scope="session")
def environment(request):

    environment = request.config.getoption("--env")

    supported_environments = {"qa", "staging", "prod"}

    if environment not in supported_environments:
        raise ValueError(
            f"Unsupported environment: {environment}. "
            f"Supported environments: {sorted(supported_environments)}"
        )

    return environment


@pytest.fixture(scope="session")
def platform(request):

    platform = request.config.getoption("--platform")

    if platform is None:
        return None

    platform = platform.lower()

    supported_platforms = {"android", "ios"}

    if platform not in supported_platforms:
        raise ValueError(
            f"Unsupported platform: {platform}. "
            f"Supported platforms: {sorted(supported_platforms)}"
        )

    return platform


@pytest.fixture(scope="session")
def config(environment, platform):

    config = load_config(environment)

    if platform is not None:
        config = replace(
            config,
            platform_name=Platform(platform)
        )

    return config

@pytest.fixture(scope="session", autouse=True)
def report_metadata(config, request):

    plugin = request.config.pluginmanager.getplugin("html")

    if plugin is None:
        return

    metadata = getattr(request.config, "_metadata", None)

    if metadata is None:
        return

    metadata["Device"] = config.device_name
    metadata["Automation"] = config.automation_name


@pytest.fixture
def driver(config):

    driver = DriverFactory.create_driver(config)

    try:
        yield driver

    finally:
        driver.quit()


@pytest.fixture
def pages(driver):

    return PageObjects(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if not report.failed:
        return

    driver = item.funcargs.get("driver")

    if driver is None:
        return

    test_name = (
        item.nodeid
        .replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
    )

    screenshot_path = ArtifactUtils.save_screenshot(
        driver,
        test_name
    )

    page_source_path = ArtifactUtils.save_page_source(
        driver,
        test_name
    )

    if screenshot_path:
        allure.attach.file(
            str(screenshot_path),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

    if page_source_path:
        allure.attach.file(
            str(page_source_path),
            name="Page Source",
            attachment_type=allure.attachment_type.XML
        )

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata, config):

    environment = config.getoption("--env")
    platform = config.getoption("--platform")

    metadata["Environment"] = environment
    metadata["Platform"] = platform or "default"






#def environment(request): gets the value supplied from the command line.
# def pytest_addoption(parser):   it is a pytest hook , I want to add a custom command-line option.
# Default scope is function
# We don't want to read qa.yaml for every single test. the configuration is loaded once per Pytest execution.
# def pages(driver): this fixture we have created for object creation instead of creating object all the time
# all class we can create in one class and retrun it to fixture