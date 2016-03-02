""" Cisco_IOS_XR_ethernet_link_oam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-link\-oam package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-l2\-eth\-infra\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class EtherLinkOamEventActionEnum1_Enum(Enum):
    """
    EtherLinkOamEventActionEnum1_Enum

    Ether link oam event action enum1

    """

    """

    Disable the interface

    """
    ERROR_DISABLE = 2

    """

    Log the event

    """
    LOG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum1_Enum']


class EtherLinkOamEventActionEnum2_Enum(Enum):
    """
    EtherLinkOamEventActionEnum2_Enum

    Ether link oam event action enum2

    """

    """

    Perform no action

    """
    DISABLE = 1

    """

    Disable the interface

    """
    ERROR_DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum2_Enum']


class EtherLinkOamEventActionEnum4_Enum(Enum):
    """
    EtherLinkOamEventActionEnum4_Enum

    Ether link oam event action enum4

    """

    """

    Perform no action

    """
    DISABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum4_Enum']


class EtherLinkOamEventActionEnum5_Enum(Enum):
    """
    EtherLinkOamEventActionEnum5_Enum

    Ether link oam event action enum5

    """

    """

    Perform no action

    """
    DISABLE = 1

    """

    Disable the interface

    """
    ERROR_DISABLE = 2

    """

    EFD the interface

    """
    EFD = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum5_Enum']


class EtherLinkOamEventActionEnum6_Enum(Enum):
    """
    EtherLinkOamEventActionEnum6_Enum

    Ether link oam event action enum6

    """

    """

    Perform no action

    """
    DISABLE = 1

    """

    Log the event

    """
    LOG = 3

    """

    EFD the interface

    """
    EFD = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum6_Enum']


class EtherLinkOamEventActionEnumEfd_Enum(Enum):
    """
    EtherLinkOamEventActionEnumEfd_Enum

    Ether link oam event action enum efd

    """

    """

    Perform no action

    """
    DISABLE = 1

    """

    Disable the interface

    """
    ERROR_DISABLE = 2

    """

    Log the event

    """
    LOG = 3

    """

    EFD the interface

    """
    EFD = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnumEfd_Enum']


class EtherLinkOamEventActionEnum_Enum(Enum):
    """
    EtherLinkOamEventActionEnum_Enum

    Ether link oam event action enum

    """

    """

    Perform no action

    """
    DISABLE = 1

    """

    Disable the interface

    """
    ERROR_DISABLE = 2

    """

    Log the event

    """
    LOG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum_Enum']


class EtherLinkOamEventActionPrimEnum_Enum(Enum):
    """
    EtherLinkOamEventActionPrimEnum_Enum

    Ether link oam event action prim enum

    """

    """

    Perform no action

    """
    DISABLE = 1

    """

    Log the event

    """
    LOG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionPrimEnum_Enum']


class EtherLinkOamInterfaceHelloIntervalEnum_Enum(Enum):
    """
    EtherLinkOamInterfaceHelloIntervalEnum_Enum

    Ether link oam interface hello interval enum

    """

    """

    1 s OAM hello interval

    """
    Y_1S = 0

    """

    100 ms OAM hello interval

    """
    Y_100MS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamInterfaceHelloIntervalEnum_Enum']


class EtherLinkOamInterfaceModeEnum_Enum(Enum):
    """
    EtherLinkOamInterfaceModeEnum_Enum

    Ether link oam interface mode enum

    """

    """

    Ethernet Link OAM Passive mode

    """
    PASSIVE = 0

    """

    Ethernet Link OAM Active mode

    """
    ACTIVE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamInterfaceModeEnum_Enum']


class EtherLinkOamInterfaceRequireModeEnum_Enum(Enum):
    """
    EtherLinkOamInterfaceRequireModeEnum_Enum

    Ether link oam interface require mode enum

    """

    """

    Ethernet Link OAM Passive mode

    """
    PASSIVE = 0

    """

    Ethernet Link OAM Active mode

    """
    ACTIVE = 1

    """

    Ethernet Link OAM mode not required

    """
    DONT_CARE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamInterfaceRequireModeEnum_Enum']


class EtherLinkOamProfileHelloIntervalEnum_Enum(Enum):
    """
    EtherLinkOamProfileHelloIntervalEnum_Enum

    Ether link oam profile hello interval enum

    """

    """

    100 ms OAM hello interval

    """
    Y_100MS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamProfileHelloIntervalEnum_Enum']


class EtherLinkOamProfileModeEnum_Enum(Enum):
    """
    EtherLinkOamProfileModeEnum_Enum

    Ether link oam profile mode enum

    """

    """

    Ethernet Link OAM Passive mode

    """
    PASSIVE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamProfileModeEnum_Enum']


class EtherLinkOamProfileRequireModeEnum_Enum(Enum):
    """
    EtherLinkOamProfileRequireModeEnum_Enum

    Ether link oam profile require mode enum

    """

    """

    Ethernet Link OAM Passive mode

    """
    PASSIVE = 0

    """

    Ethernet Link OAM Active mode

    """
    ACTIVE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamProfileRequireModeEnum_Enum']



