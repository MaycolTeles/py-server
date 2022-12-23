"""
Module containing the "FileLogger" Class.
"""

from typing import Any, Optional
from datetime import datetime

from src.loggers.interfaces import Logger
from src.loggers.messages import LogMessage, MessageLevel


class FileLogger(Logger):
    """ 
    """
    _file_name: str
    _message_level: MessageLevel

    def __init__(self) -> None:
        """"""
        default_message_level = MessageLevel.INFO

        self._set_file_name()
        self.set_message_level(default_message_level)

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
        self._message_level = message_level

    def log_info(self, message: str, fields: Optional[dict[str, Any]]=None) -> None:
        """"""
        log_message = LogMessage(
            message_level=MessageLevel.INFO,
            message=message,
            fields=fields
        )

        self._log_message(log_message)

    def log_warning(self, message: str, fields: Optional[dict[str, Any]]=None) -> None:
        """"""
        log_message = LogMessage(
            message_level=MessageLevel.WARNING,
            message=message,
            fields=fields
        )

        self._log_message(log_message)

    def log_error(self, message: str, fields: Optional[dict[str, Any]]=None) -> None:
        """"""
        log_message = LogMessage(
            message_level=MessageLevel.ERROR,
            message=message,
            fields=fields
        )

        self._log_message(log_message)

    def _set_file_name(self) -> None:
        """"""
        current_time = datetime.now().replace(microsecond=0)
        self._file_name = f"logs/logging_{current_time}.txt"

    def _log_message(self, message: LogMessage) -> None:
        """"""
        message_should_be_logged = self._should_message_be_logged(message.message_level)

        if not message_should_be_logged:
            return

        str_message = self._format_message_to_str(message)

        self._log_message_on_file(str_message)

    def _log_message_on_file(self, message: str) -> None:
        """"""
        with open(self._file_name, "a") as write_file:
            write_file.write(message)

    def _format_message_to_str(self, log_message: LogMessage) -> str:
        """"""
        time = datetime.now().time().replace(microsecond=0)

        formatted_message = f"[{time}] -> [{log_message.message_level.name}] {log_message.message}\n"
        return formatted_message

    def _should_message_be_logged(self, message_level: MessageLevel) -> bool:
        """"""
        return message_level.value >= self._message_level.value
