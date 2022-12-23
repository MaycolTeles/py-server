"""
Module containing the "LogMessage" Class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from src.loggers.messages import MessageLevel


# MODULE IMPORTS
from dataclasses import dataclass


@dataclass
class LogMessage:
    """
    Class to represent a message that will be logged.
    """
    message_level: MessageLevel
    message: str
    fields: Optional[dict[str, Any]] = None
