""" TRANSPORT_ADDRESS_MIB 


"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class TransportAddressType_Enum(Enum):
    """
    TransportAddressType_Enum

    """

    UNKNOWN = 0

    UDPIPV4 = 1

    UDPIPV6 = 2

    UDPIPV4Z = 3

    UDPIPV6Z = 4

    TCPIPV4 = 5

    TCPIPV6 = 6

    TCPIPV4Z = 7

    TCPIPV6Z = 8

    SCTPIPV4 = 9

    SCTPIPV6 = 10

    SCTPIPV4Z = 11

    SCTPIPV6Z = 12

    LOCAL = 13

    UDPDNS = 14

    TCPDNS = 15

    SCTPDNS = 16


    @staticmethod
    def _meta_info():
        from ydk.models.transport._meta import _TRANSPORT_ADDRESS_MIB as meta
        return meta._meta_table['TransportAddressType_Enum']



