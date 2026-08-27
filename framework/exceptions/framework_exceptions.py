class FrameworkException(Exception):
    """Base exception for framework-specific failures."""


class ConfigurationException(FrameworkException):
    """Raised when framework configuration is invalid."""


class DriverInitializationException(FrameworkException):
    """Raised when Appium driver initialization fails."""


class ElementInteractionException(FrameworkException):
    """Raised when an element interaction fails."""


class TestDataException(FrameworkException):
    """Raised when test data cannot be loaded or is invalid."""