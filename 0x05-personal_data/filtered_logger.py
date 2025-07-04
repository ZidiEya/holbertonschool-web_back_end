#!/usr/bin/env python3
"""Module for filtering log messages with sensitive fields obfuscated."""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Returns log message with specified fields obfuscated."""
    return re.sub(
        rf'({"|".join(fields)})=[^{separator}]*',
        lambda m: f'{m.group(1)}={redaction}',
        message
    )
