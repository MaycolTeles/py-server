"""
Module containing the "Logger" Interface.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from src.loggers.messages import MessageLevel


# MODULE IMPORTS
from abc import ABC, abstractmethod


class Logger(ABC):
    """
    Abstract Class containing all the methods that a Logger Class must implement.

    Those methods are:
    * set_message_level(self, message_level: MessageLevel) -> None
    * log_info(self, message: str, fields: Optional[dict[str, Any]]=None) -> None
    * log_warning(self, message: str, fields: Optional[dict[str, Any]]=None) -> None
    * log_error(self, message: str, fields: Optional[dict[str, Any]]=None) -> None
    """

    @abstractmethod
    def set_message_level(self, message_level: MessageLevel) -> None:
        """
        Method to set/define the logging level message.

        Any message above "message_level" will be logged;
        Any message below "message_level" will not be logged.

        For more information on the "message_level" order, check the "MessageLevel" class.

        Parameters
        -----------
        message_level : MessageLevel
            The message level that will be defined.
        """

    @abstractmethod
    def log_info(self, message: str, fields: Optional[dict[str, Any]]=None) -> None:
        """
        Method to log a message with INFO level.

        This method must be implemented in all classes that wants to be a Logger class.

        Parameters
        ----------
        message : str
            The message that will be logged.

        fields : Optional[dict[str, Any]]
            Some additional fields that are going to be logged.
            Default is None.
        """

    @abstractmethod
    def log_warning(self, message: str, fields: Optional[dict[str, Any]]=None) -> None:
        """
        Method to log a message with WARNING level.

        This method must be implemented in all classes that wants to be a Logger class.

        Parameters
        ----------
        message : str
            The message that will be logged.

        fields : Optional[dict[str, Any]]
            Some additional fields that are going to be logged.
            Default is None.
        """

    @abstractmethod
    def log_error(self, message: str, fields: Optional[dict[str, Any]]=None) -> None:
        """
        Method to log a message with ERROR level.

        This method must be implemented in all classes that wants to be a Logger class.

        Parameters
        ----------
        message : str
            The message that will be logged.

        fields : Optional[dict[str, Any]]
            Some additional fields that are going to be logged.
            Default is None.
        """
