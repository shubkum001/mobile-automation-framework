from pathlib import Path

import yaml

from framework.config.config import MobileConfig
from framework.config.platform import Platform
from utils.env_reader import get_env


def load_config(environment: str) -> MobileConfig:

    config_path = (
        Path(__file__).resolve().parents[2]
        / "config"
        / f"{environment}.yaml"
    )

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(config_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    try:
        data["platform_name"] = Platform(
            data["platform_name"].strip().lower()
        )

    except (KeyError, AttributeError, ValueError) as exc:
        raise ValueError(
            f"Invalid platform_name in configuration: "
            f"{data.get('platform_name')!r}. "
            f"Supported platforms: "
            f"{[platform.value for platform in Platform]}"
        ) from exc

    server_url = get_env("APPIUM_SERVER_URL")

    if server_url:
        data["server_url"] = server_url

    return MobileConfig(**data)

 # this is to go to the root that is "mobile automation framework then config then qa.yaml,prod.yaml,staging.yaml basesd on requiremnt"
 #If the file doesn't exist, Python throws: file not found error
 # This converts our YAML into a Python dictionary.
# reading file
# The ** operator expands the dictionary.


# this is to go to the root that is "mobile automation framework then config then qa.yaml"


# The ** operator expands the dictionary.

# we have used strip function to avoid unnecessary spaces someone writtten like " android " instead "android"