from typing import Any, Dict


def get_log_levels_as_dict(config: Dict[str, Any]) -> Dict[str, int]:
    try:
        return config["settings"]["verbosity_levels"]
    except KeyError:
        return {}


def privacy_file_redact_all_check(config: Dict[str, Any]) -> bool:
    try:
        file_privacy_dict: Dict[str, Any] = config["output"]["file"]
        return all(file_privacy_dict.values())
    except KeyError:
        return False


def privacy_console_redact_all_check(config: Dict[str, Any]) -> bool:
    try:
        console_privacy_dict: Dict[str, Any] = config["output"]["console"]
        return all(console_privacy_dict.values())
    except KeyError:
        return False
