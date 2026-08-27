from dataclasses import dataclass
from framework.config.platform import Platform


@dataclass(frozen=True)
class MobileConfig:
    environment: str
    platform_name: Platform
    device_name: str
    automation_name: str
    server_url: str
    app_package: str
    app_activity: str
    new_command_timeout: int


 # (About frozen - because configuration should generally be treated as read-only after loading.The frozen dataclass prevents accidental modification.)