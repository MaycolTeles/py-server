"""
Module containing the "MessageLevel" Enum.
"""

from enum import Enum


class MessageLevel(Enum):
    """
    Enum containing all available message levels that are going to be logged.

    The level is like so:
    * ERROR = 0
    * WARNING = 1
    * INFO = 2
    """
    INFO = 0
    WARNING = 1
    ERROR = 2
