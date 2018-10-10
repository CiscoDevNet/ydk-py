""" Cisco_IOS_XR_aaa_protocol_radius_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-protocol\-radius package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-locald\-cfg,
  Cisco\-IOS\-XR\-aaa\-lib\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AaaAction(Enum):
    """
    AaaAction (Enum Class)

    Aaa action

    .. data:: accept = 1

    	Accept

    .. data:: reject = 2

    	Reject

    """

    accept = Enum.YLeaf(1, "accept")

    reject = Enum.YLeaf(2, "reject")


class AaaAuthentication(Enum):
    """
    AaaAuthentication (Enum Class)

    Aaa authentication

    .. data:: all = 101

    	All

    .. data:: any = 102

    	Any

    .. data:: session_key = 103

    	Session key

    """

    all = Enum.YLeaf(101, "all")

    any = Enum.YLeaf(102, "any")

    session_key = Enum.YLeaf(103, "session-key")


class AaaConfig(Enum):
    """
    AaaConfig (Enum Class)

    Aaa config

    .. data:: false = 0

    	False

    .. data:: true = 1

    	True

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


class AaaDirection(Enum):
    """
    AaaDirection (Enum Class)

    Aaa direction

    .. data:: inbound = 0

    	Inbound

    .. data:: outbound = 1

    	Outbound

    """

    inbound = Enum.YLeaf(0, "inbound")

    outbound = Enum.YLeaf(1, "outbound")


class AaaDscpValue(Enum):
    """
    AaaDscpValue (Enum Class)

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

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    cs1 = Enum.YLeaf(8, "cs1")

    cs2 = Enum.YLeaf(16, "cs2")

    cs3 = Enum.YLeaf(24, "cs3")

    cs4 = Enum.YLeaf(32, "cs4")

    cs5 = Enum.YLeaf(40, "cs5")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")

    default = Enum.YLeaf(0, "default")

    ef = Enum.YLeaf(46, "ef")


class AaaSelectKey(Enum):
    """
    AaaSelectKey (Enum Class)

    Aaa select key

    .. data:: server_key = 1

    	Server key

    .. data:: session_key = 2

    	Session  key

    """

    server_key = Enum.YLeaf(1, "server-key")

    session_key = Enum.YLeaf(2, "session-key")



