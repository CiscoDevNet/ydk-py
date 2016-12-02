""" Cisco_IOS_XR_drivers_media_eth_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EthernetAutoNegotiationEnum(Enum):
    """
    EthernetAutoNegotiationEnum

    Ethernet auto negotiation

    .. data:: true = 1

    	IEEE Standard auto-negotiation

    .. data:: override = 2

    	Auto-negotiation with configuration override

    """

    true = 1

    override = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetAutoNegotiationEnum']


class EthernetDuplexEnum(Enum):
    """
    EthernetDuplexEnum

    Ethernet duplex

    .. data:: full = 0

    	Full duplex

    .. data:: half = 1

    	Half duplex

    """

    full = 0

    half = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetDuplexEnum']


class EthernetFecEnum(Enum):
    """
    EthernetFecEnum

    Ethernet fec

    .. data:: none = 0

    	Disable any FEC enabled on the interface

    .. data:: standard = 1

    	Enable standard (Reed-Solomon) FEC

    """

    none = 0

    standard = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetFecEnum']


class EthernetFlowCtrlEnum(Enum):
    """
    EthernetFlowCtrlEnum

    Ethernet flow ctrl

    .. data:: ingress = 0

    	Ingress flow control (sending pause frames)

    .. data:: egress = 1

    	Egress flow control (received pause frames)

    .. data:: bidirectional = 2

    	Bi-direction flow control

    """

    ingress = 0

    egress = 1

    bidirectional = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetFlowCtrlEnum']


class EthernetIpgEnum(Enum):
    """
    EthernetIpgEnum

    Ethernet ipg

    .. data:: non_standard = 16

    	Non standard IPG

    """

    non_standard = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetIpgEnum']


class EthernetLoopbackEnum(Enum):
    """
    EthernetLoopbackEnum

    Ethernet loopback

    .. data:: external = 0

    	External loopback (using loopback connector)

    .. data:: internal = 1

    	Internal loopback

    .. data:: line = 2

    	Line loopback

    """

    external = 0

    internal = 1

    line = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetLoopbackEnum']


class EthernetPfcEnum(Enum):
    """
    EthernetPfcEnum

    Ethernet pfc

    .. data:: on = 1

    	Enable priority flow control

    """

    on = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetPfcEnum']


class EthernetSpeedEnum(Enum):
    """
    EthernetSpeedEnum

    Ethernet speed

    .. data:: Y_10 = 10

    	10Mbits/s

    .. data:: Y_100 = 100

    	100Mbits/s

    .. data:: Y_1000 = 1000

    	1Gbits/s

    """

    Y_10 = 10

    Y_100 = 100

    Y_1000 = 1000


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetSpeedEnum']



