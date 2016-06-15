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

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EtherLinkOamEventActionEnum1Enum(Enum):
    """
    EtherLinkOamEventActionEnum1Enum

    Ether link oam event action enum1

    .. data:: ERROR_DISABLE = 2

    	Disable the interface

    .. data:: LOG = 3

    	Log the event

    """

    ERROR_DISABLE = 2

    LOG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum1Enum']


class EtherLinkOamEventActionEnum2Enum(Enum):
    """
    EtherLinkOamEventActionEnum2Enum

    Ether link oam event action enum2

    .. data:: DISABLE = 1

    	Perform no action

    .. data:: ERROR_DISABLE = 2

    	Disable the interface

    """

    DISABLE = 1

    ERROR_DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum2Enum']


class EtherLinkOamEventActionEnum4Enum(Enum):
    """
    EtherLinkOamEventActionEnum4Enum

    Ether link oam event action enum4

    .. data:: DISABLE = 1

    	Perform no action

    """

    DISABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum4Enum']


class EtherLinkOamEventActionEnum5Enum(Enum):
    """
    EtherLinkOamEventActionEnum5Enum

    Ether link oam event action enum5

    .. data:: DISABLE = 1

    	Perform no action

    .. data:: ERROR_DISABLE = 2

    	Disable the interface

    .. data:: EFD = 4

    	EFD the interface

    """

    DISABLE = 1

    ERROR_DISABLE = 2

    EFD = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum5Enum']


class EtherLinkOamEventActionEnum6Enum(Enum):
    """
    EtherLinkOamEventActionEnum6Enum

    Ether link oam event action enum6

    .. data:: DISABLE = 1

    	Perform no action

    .. data:: LOG = 3

    	Log the event

    .. data:: EFD = 4

    	EFD the interface

    """

    DISABLE = 1

    LOG = 3

    EFD = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnum6Enum']


class EtherLinkOamEventActionEnumEfdEnum(Enum):
    """
    EtherLinkOamEventActionEnumEfdEnum

    Ether link oam event action enum efd

    .. data:: DISABLE = 1

    	Perform no action

    .. data:: ERROR_DISABLE = 2

    	Disable the interface

    .. data:: LOG = 3

    	Log the event

    .. data:: EFD = 4

    	EFD the interface

    """

    DISABLE = 1

    ERROR_DISABLE = 2

    LOG = 3

    EFD = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnumEfdEnum']


class EtherLinkOamEventActionEnumEnum(Enum):
    """
    EtherLinkOamEventActionEnumEnum

    Ether link oam event action enum

    .. data:: DISABLE = 1

    	Perform no action

    .. data:: ERROR_DISABLE = 2

    	Disable the interface

    .. data:: LOG = 3

    	Log the event

    """

    DISABLE = 1

    ERROR_DISABLE = 2

    LOG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnumEnum']


class EtherLinkOamEventActionPrimEnumEnum(Enum):
    """
    EtherLinkOamEventActionPrimEnumEnum

    Ether link oam event action prim enum

    .. data:: DISABLE = 1

    	Perform no action

    .. data:: LOG = 3

    	Log the event

    """

    DISABLE = 1

    LOG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionPrimEnumEnum']


class EtherLinkOamInterfaceHelloIntervalEnumEnum(Enum):
    """
    EtherLinkOamInterfaceHelloIntervalEnumEnum

    Ether link oam interface hello interval enum

    .. data:: Y_1S = 0

    	1 s OAM hello interval

    .. data:: Y_100MS = 1

    	100 ms OAM hello interval

    """

    Y_1S = 0

    Y_100MS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamInterfaceHelloIntervalEnumEnum']


class EtherLinkOamInterfaceModeEnumEnum(Enum):
    """
    EtherLinkOamInterfaceModeEnumEnum

    Ether link oam interface mode enum

    .. data:: PASSIVE = 0

    	Ethernet Link OAM Passive mode

    .. data:: ACTIVE = 1

    	Ethernet Link OAM Active mode

    """

    PASSIVE = 0

    ACTIVE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamInterfaceModeEnumEnum']


class EtherLinkOamInterfaceRequireModeEnumEnum(Enum):
    """
    EtherLinkOamInterfaceRequireModeEnumEnum

    Ether link oam interface require mode enum

    .. data:: PASSIVE = 0

    	Ethernet Link OAM Passive mode

    .. data:: ACTIVE = 1

    	Ethernet Link OAM Active mode

    .. data:: DONT_CARE = 2

    	Ethernet Link OAM mode not required

    """

    PASSIVE = 0

    ACTIVE = 1

    DONT_CARE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamInterfaceRequireModeEnumEnum']


class EtherLinkOamProfileHelloIntervalEnumEnum(Enum):
    """
    EtherLinkOamProfileHelloIntervalEnumEnum

    Ether link oam profile hello interval enum

    .. data:: Y_100MS = 1

    	100 ms OAM hello interval

    """

    Y_100MS = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamProfileHelloIntervalEnumEnum']


class EtherLinkOamProfileModeEnumEnum(Enum):
    """
    EtherLinkOamProfileModeEnumEnum

    Ether link oam profile mode enum

    .. data:: PASSIVE = 0

    	Ethernet Link OAM Passive mode

    """

    PASSIVE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamProfileModeEnumEnum']


class EtherLinkOamProfileRequireModeEnumEnum(Enum):
    """
    EtherLinkOamProfileRequireModeEnumEnum

    Ether link oam profile require mode enum

    .. data:: PASSIVE = 0

    	Ethernet Link OAM Passive mode

    .. data:: ACTIVE = 1

    	Ethernet Link OAM Active mode

    """

    PASSIVE = 0

    ACTIVE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamProfileRequireModeEnumEnum']



