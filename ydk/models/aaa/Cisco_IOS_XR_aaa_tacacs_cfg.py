""" Cisco_IOS_XR_aaa_tacacs_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-tacacs package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-lib\-cfg,
  Cisco\-IOS\-XR\-aaa\-locald\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class TacacsDscpValue_Enum(Enum):
    """
    TacacsDscpValue_Enum

    Tacacs dscp value

    """

    """

    Match packets with AF11 DSCP

    """
    AF11 = 10

    """

    Match packets with AF12 DSCP

    """
    AF12 = 12

    """

    Match packets with AF13 DSCP

    """
    AF13 = 14

    """

    Match packets with AF21 DSCP

    """
    AF21 = 18

    """

    Match packets with AF22 DSCP

    """
    AF22 = 20

    """

    Match packets with AF23 DSCP

    """
    AF23 = 22

    """

    Match packets with AF31 DSCP

    """
    AF31 = 26

    """

    Match packets with AF32 DSCP

    """
    AF32 = 28

    """

    Match packets with AF33 DSCP

    """
    AF33 = 30

    """

    Match packets with AF41 DSCP

    """
    AF41 = 34

    """

    Match packets with AF42 DSCP

    """
    AF42 = 36

    """

    Match packets with AF43 DSCP

    """
    AF43 = 38

    """

    Match packets with CS1 DSCP

    """
    CS1 = 8

    """

    Match packets with CS2 DSCP

    """
    CS2 = 16

    """

    Match packets with CS3 DSCP

    """
    CS3 = 24

    """

    Match packets with CS4 DSCP

    """
    CS4 = 32

    """

    Match packets with CS5 DSCP

    """
    CS5 = 40

    """

    Match packets with CS6 DSCP

    """
    CS6 = 48

    """

    Match packets with CS7 DSCP

    """
    CS7 = 56

    """

    Match packets with 0000 DSCP

    """
    DEFAULT = 0

    """

    Match packets with EF DSCP

    """
    EF = 46


    @staticmethod
    def _meta_info():
        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_tacacs_cfg as meta
        return meta._meta_table['TacacsDscpValue_Enum']



