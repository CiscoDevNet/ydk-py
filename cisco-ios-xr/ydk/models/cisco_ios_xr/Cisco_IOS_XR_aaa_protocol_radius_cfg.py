""" Cisco_IOS_XR_aaa_protocol_radius_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-protocol\-radius package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-cfg,
  Cisco\-IOS\-XR\-aaa\-lib\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AaaActionEnum(Enum):
    """
    AaaActionEnum

    Aaa action

    .. data:: accept = 1

    	Accept

    .. data:: reject = 2

    	Reject

    """

    accept = 1

    reject = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_cfg as meta
        return meta._meta_table['AaaActionEnum']


class AaaAuthenticationEnum(Enum):
    """
    AaaAuthenticationEnum

    Aaa authentication

    .. data:: all = 101

    	All

    .. data:: any = 102

    	Any

    .. data:: session_key = 103

    	Session key

    """

    all = 101

    any = 102

    session_key = 103


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_cfg as meta
        return meta._meta_table['AaaAuthenticationEnum']


class AaaConfigEnum(Enum):
    """
    AaaConfigEnum

    Aaa config

    .. data:: false = 0

    	False

    .. data:: true = 1

    	True

    """

    false = 0

    true = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_cfg as meta
        return meta._meta_table['AaaConfigEnum']


class AaaDirectionEnum(Enum):
    """
    AaaDirectionEnum

    Aaa direction

    .. data:: inbound = 0

    	Inbound

    .. data:: outbound = 1

    	Outbound

    """

    inbound = 0

    outbound = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_cfg as meta
        return meta._meta_table['AaaDirectionEnum']


class AaaDscpValueEnum(Enum):
    """
    AaaDscpValueEnum

    Aaa dscp value

    .. data:: af11 = 10

    	Match packets with AF11 DSCP

    .. data:: af12 = 12

    	Match packets with AF12 DSCP

    .. data:: af13 = 14

    	Match packets with AF13 DSCP

    .. data:: af21 = 18

    	Match packets with AF21 DSCP

    .. data:: af22 = 20

    	Match packets with AF22 DSCP

    .. data:: af23 = 22

    	Match packets with AF23 DSCP

    .. data:: af31 = 26

    	Match packets with AF31 DSCP

    .. data:: af32 = 28

    	Match packets with AF32 DSCP

    .. data:: af33 = 30

    	Match packets with AF33 DSCP

    .. data:: af41 = 34

    	Match packets with AF41 DSCP

    .. data:: af42 = 36

    	Match packets with AF42 DSCP

    .. data:: af43 = 38

    	Match packets with AF43 DSCP

    .. data:: cs1 = 8

    	Match packets with CS1 DSCP

    .. data:: cs2 = 16

    	Match packets with CS2 DSCP

    .. data:: cs3 = 24

    	Match packets with CS3 DSCP

    .. data:: cs4 = 32

    	Match packets with CS4 DSCP

    .. data:: cs5 = 40

    	Match packets with CS5 DSCP

    .. data:: cs6 = 48

    	Match packets with CS6 DSCP

    .. data:: cs7 = 56

    	Match packets with CS7 DSCP

    .. data:: default = 0

    	Match packets with 0000 DSCP

    .. data:: ef = 46

    	Match packets with EF DSCP

    """

    af11 = 10

    af12 = 12

    af13 = 14

    af21 = 18

    af22 = 20

    af23 = 22

    af31 = 26

    af32 = 28

    af33 = 30

    af41 = 34

    af42 = 36

    af43 = 38

    cs1 = 8

    cs2 = 16

    cs3 = 24

    cs4 = 32

    cs5 = 40

    cs6 = 48

    cs7 = 56

    default = 0

    ef = 46


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_cfg as meta
        return meta._meta_table['AaaDscpValueEnum']


class AaaSelectKeyEnum(Enum):
    """
    AaaSelectKeyEnum

    Aaa select key

    .. data:: server_key = 1

    	Server key

    .. data:: session_key = 2

    	Session  key

    """

    server_key = 1

    session_key = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_protocol_radius_cfg as meta
        return meta._meta_table['AaaSelectKeyEnum']



