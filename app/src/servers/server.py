"""
Module containing the "Server" Class.
"""

import queue
import socket
import sys
import time
import threading

from src.constants import SERVER_ADDRESS, SERVER_TICK_FREQUENCY
from src.loggers import get_logger


logger = get_logger()


class Server:
    """
    Class to represent the Server.
    """

    def start(self) -> None:
        """
        Method to start the server.
        """
        logging_message = f"> SERVER RUNNING ON {SERVER_ADDRESS}"
        logger.log_info(
            message=logging_message,
        )

        print()
        print(logging_message, end="\n\n")

    def shut_down(self) -> None:
        """
        Method to shut down the server.
        """
        logging_message = "> SERVER OFF"
        logger.log_info(
            message=logging_message,
        )

        print()
        print(logging_message, end="\n\n")

        sys.exit()
