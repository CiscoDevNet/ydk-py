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



class TacacsDscpValueEnum(Enum):
    """
    TacacsDscpValueEnum

    Tacacs dscp value

    .. data:: AF11 = 10

    	Match packets with AF11 DSCP

    .. data:: AF12 = 12

    	Match packets with AF12 DSCP

    .. data:: AF13 = 14

    	Match packets with AF13 DSCP

    .. data:: AF21 = 18

    	Match packets with AF21 DSCP

    .. data:: AF22 = 20

    	Match packets with AF22 DSCP

    .. data:: AF23 = 22

    	Match packets with AF23 DSCP

    .. data:: AF31 = 26

    	Match packets with AF31 DSCP

    .. data:: AF32 = 28

    	Match packets with AF32 DSCP

    .. data:: AF33 = 30

    	Match packets with AF33 DSCP

    .. data:: AF41 = 34

    	Match packets with AF41 DSCP

    .. data:: AF42 = 36

    	Match packets with AF42 DSCP

    .. data:: AF43 = 38

    	Match packets with AF43 DSCP

    .. data:: CS1 = 8

    	Match packets with CS1 DSCP

    .. data:: CS2 = 16

    	Match packets with CS2 DSCP

    .. data:: CS3 = 24

    	Match packets with CS3 DSCP

    .. data:: CS4 = 32

    	Match packets with CS4 DSCP

    .. data:: CS5 = 40

    	Match packets with CS5 DSCP

    .. data:: CS6 = 48

    	Match packets with CS6 DSCP

    .. data:: CS7 = 56

    	Match packets with CS7 DSCP

    .. data:: DEFAULT = 0

    	Match packets with 0000 DSCP

    .. data:: EF = 46

    	Match packets with EF DSCP

    """

    AF11 = 10

    AF12 = 12

    AF13 = 14

    AF21 = 18

    AF22 = 20

    AF23 = 22

    AF31 = 26

    AF32 = 28

    AF33 = 30

    AF41 = 34

    AF42 = 36

    AF43 = 38

    CS1 = 8

    CS2 = 16

    CS3 = 24

    CS4 = 32

    CS5 = 40

    CS6 = 48

    CS7 = 56

    DEFAULT = 0

    EF = 46


    @staticmethod
    def _meta_info():
        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_tacacs_cfg as meta
        return meta._meta_table['TacacsDscpValueEnum']



