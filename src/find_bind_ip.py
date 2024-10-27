import re
from typing import List


def extract_bind_addresses(config: str) -> List[str]:
    """
    Extracts all bind addresses from the given configuration string.

    :param config: A string containing the configuration.
    :return: A list of bind addresses found in the configuration.
    """
    pattern = r'bind\s+([^:\s]*[^:\s]*:\S*)'
    matches = re.findall(pattern, config)
    return matches
