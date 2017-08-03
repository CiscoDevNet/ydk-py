""" Cisco_IOS_XR_drivers_media_eth_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EthernetAutoNegotiation(Enum):
    """
    EthernetAutoNegotiation

    Ethernet auto negotiation

    .. data:: true = 1

    	IEEE Standard auto-negotiation

    .. data:: override = 2

    	Auto-negotiation with configuration override

    """

    true = Enum.YLeaf(1, "true")

    override = Enum.YLeaf(2, "override")


class EthernetDuplex(Enum):
    """
    EthernetDuplex

    Ethernet duplex

    .. data:: full = 0

    	Full duplex

    .. data:: half = 1

    	Half duplex

    """

    full = Enum.YLeaf(0, "full")

    half = Enum.YLeaf(1, "half")


class EthernetFec(Enum):
    """
    EthernetFec

    Ethernet fec

    .. data:: none = 0

    	Disable any FEC enabled on the interface

    .. data:: standard = 1

    	Enable standard (Reed-Solomon) FEC

    """

    none = Enum.YLeaf(0, "none")

    standard = Enum.YLeaf(1, "standard")


class EthernetFlowCtrl(Enum):
    """
    EthernetFlowCtrl

    Ethernet flow ctrl

    .. data:: ingress = 0

    	Ingress flow control (sending pause frames)

    .. data:: egress = 1

    	Egress flow control (received pause frames)

    .. data:: bidirectional = 2

    	Bi-direction flow control

    """

    ingress = Enum.YLeaf(0, "ingress")

    egress = Enum.YLeaf(1, "egress")

    bidirectional = Enum.YLeaf(2, "bidirectional")


class EthernetIpg(Enum):
    """
    EthernetIpg

    Ethernet ipg

    .. data:: non_standard = 16

    	Non standard IPG

    """

    non_standard = Enum.YLeaf(16, "non-standard")


class EthernetLoopback(Enum):
    """
    EthernetLoopback

    Ethernet loopback

    .. data:: external = 0

    	External loopback (using loopback connector)

    .. data:: internal = 1

    	Internal loopback

    .. data:: line = 2

    	Line loopback

    """

    external = Enum.YLeaf(0, "external")

    internal = Enum.YLeaf(1, "internal")

    line = Enum.YLeaf(2, "line")


class EthernetPfc(Enum):
    """
    EthernetPfc

    Ethernet pfc

    .. data:: on = 1

    	Enable priority flow control

    """

    on = Enum.YLeaf(1, "on")


class EthernetSpeed(Enum):
    """
    EthernetSpeed

    Ethernet speed

    .. data:: Y_10 = 10

    	10Mbits/s

    .. data:: Y_100 = 100

    	100Mbits/s

    .. data:: Y_1000 = 1000

    	1Gbits/s

    """

    Y_10 = Enum.YLeaf(10, "10")

    Y_100 = Enum.YLeaf(100, "100")

    Y_1000 = Enum.YLeaf(1000, "1000")



