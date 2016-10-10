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

    .. data:: TRUE = 1

    	IEEE Standard auto-negotiation

    .. data:: OVERRIDE = 2

    	Auto-negotiation with configuration override

    """

    TRUE = 1

    OVERRIDE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetAutoNegotiationEnum']


class EthernetDuplexEnum(Enum):
    """
    EthernetDuplexEnum

    Ethernet duplex

    .. data:: FULL = 0

    	Full duplex

    .. data:: HALF = 1

    	Half duplex

    """

    FULL = 0

    HALF = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetDuplexEnum']


class EthernetFecEnum(Enum):
    """
    EthernetFecEnum

    Ethernet fec

    .. data:: NONE = 0

    	Disable any FEC enabled on the interface

    .. data:: STANDARD = 1

    	Enable standard (Reed-Solomon) FEC

    """

    NONE = 0

    STANDARD = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetFecEnum']


class EthernetFlowCtrlEnum(Enum):
    """
    EthernetFlowCtrlEnum

    Ethernet flow ctrl

    .. data:: INGRESS = 0

    	Ingress flow control (sending pause frames)

    .. data:: EGRESS = 1

    	Egress flow control (received pause frames)

    .. data:: BIDIRECTIONAL = 2

    	Bi-direction flow control

    """

    INGRESS = 0

    EGRESS = 1

    BIDIRECTIONAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetFlowCtrlEnum']


class EthernetIpgEnum(Enum):
    """
    EthernetIpgEnum

    Ethernet ipg

    .. data:: NON_STANDARD = 16

    	Non standard IPG

    """

    NON_STANDARD = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetIpgEnum']


class EthernetLoopbackEnum(Enum):
    """
    EthernetLoopbackEnum

    Ethernet loopback

    .. data:: EXTERNAL = 0

    	External loopback (using loopback connector)

    .. data:: INTERNAL = 1

    	Internal loopback

    .. data:: LINE = 2

    	Line loopback

    """

    EXTERNAL = 0

    INTERNAL = 1

    LINE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetLoopbackEnum']


class EthernetPfcEnum(Enum):
    """
    EthernetPfcEnum

    Ethernet pfc

    .. data:: ON = 1

    	Enable priority flow control

    """

    ON = 1


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



