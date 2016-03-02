""" Cisco_IOS_XR_drivers_media_eth_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-media\-eth package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EthernetAutoNegotiation_Enum(Enum):
    """
    EthernetAutoNegotiation_Enum

    Ethernet auto negotiation

    """

    """

    IEEE Standard auto\-negotiation

    """
    TRUE = 1

    """

    Auto\-negotiation with configuration override

    """
    OVERRIDE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetAutoNegotiation_Enum']


class EthernetDuplex_Enum(Enum):
    """
    EthernetDuplex_Enum

    Ethernet duplex

    """

    """

    Full duplex

    """
    FULL = 0

    """

    Half duplex

    """
    HALF = 1


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetDuplex_Enum']


class EthernetFec_Enum(Enum):
    """
    EthernetFec_Enum

    Ethernet fec

    """

    """

    Disable any FEC enabled on the interface

    """
    NONE = 0

    """

    Enable standard (Reed\-Solomon) FEC

    """
    STANDARD = 1


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetFec_Enum']


class EthernetFlowCtrl_Enum(Enum):
    """
    EthernetFlowCtrl_Enum

    Ethernet flow ctrl

    """

    """

    Ingress flow control (sending pause frames)

    """
    INGRESS = 0

    """

    Egress flow control (received pause frames)

    """
    EGRESS = 1

    """

    Bi\-direction flow control

    """
    BIDIRECTIONAL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetFlowCtrl_Enum']


class EthernetIpg_Enum(Enum):
    """
    EthernetIpg_Enum

    Ethernet ipg

    """

    """

    Non standard IPG

    """
    NON_STANDARD = 16


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetIpg_Enum']


class EthernetLoopback_Enum(Enum):
    """
    EthernetLoopback_Enum

    Ethernet loopback

    """

    """

    External loopback (using loopback connector)

    """
    EXTERNAL = 0

    """

    Internal loopback

    """
    INTERNAL = 1

    """

    Line loopback

    """
    LINE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetLoopback_Enum']


class EthernetSpeed_Enum(Enum):
    """
    EthernetSpeed_Enum

    Ethernet speed

    """

    """

    10Mbits/s

    """
    Y_10 = 10

    """

    100Mbits/s

    """
    Y_100 = 100

    """

    1Gbits/s

    """
    Y_1000 = 1000


    @staticmethod
    def _meta_info():
        from ydk.models.drivers._meta import _Cisco_IOS_XR_drivers_media_eth_cfg as meta
        return meta._meta_table['EthernetSpeed_Enum']



