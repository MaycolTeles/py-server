"""
Module containing the "Address" Class.
"""

from dataclasses import dataclass


@dataclass
class Address:
    """
    Class to represent a socket address.
    """
    _ip_address: str
    _port: int
