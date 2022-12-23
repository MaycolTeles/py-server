"""
Module containing the "get_logger" function.
"""

from src.loggers.interfaces import Logger
from src.loggers.implementations import FileLogger


def get_logger() -> Logger:
    """
    Function to return a logger instance that will be used in the whole application.

    This function works as a factory.
    """
    return FileLogger()
