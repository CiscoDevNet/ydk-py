""" Cisco_IOS_XR_ethernet_link_oam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-link\-oam package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-l2\-eth\-infra\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EtherLinkOamEventActionEnumEfdEnum(Enum):
    """
    EtherLinkOamEventActionEnumEfdEnum

    Ether link oam event action enum efd

    .. data:: disable = 1

    	Perform no action

    .. data:: error_disable = 2

    	Disable the interface

    .. data:: log = 3

    	Log the event

    .. data:: efd = 4

    	EFD the interface

    """

    disable = 1

    error_disable = 2

    log = 3

    efd = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnumEfdEnum']


class EtherLinkOamEventActionEnumEnum(Enum):
    """
    EtherLinkOamEventActionEnumEnum

    Ether link oam event action enum

    .. data:: disable = 1

    	Perform no action

    .. data:: error_disable = 2

    	Disable the interface

    .. data:: log = 3

    	Log the event

    """

    disable = 1

    error_disable = 2

    log = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionEnumEnum']


class EtherLinkOamEventActionPrimEnumEnum(Enum):
    """
    EtherLinkOamEventActionPrimEnumEnum

    Ether link oam event action prim enum

    .. data:: disable = 1

    	Perform no action

    .. data:: log = 3

    	Log the event

    """

    disable = 1

    log = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamEventActionPrimEnumEnum']


class EtherLinkOamHelloIntervalEnumEnum(Enum):
    """
    EtherLinkOamHelloIntervalEnumEnum

    Ether link oam hello interval enum

    .. data:: Y_1s = 0

    	1 s OAM hello interval

    .. data:: Y_100ms = 1

    	100 ms OAM hello interval

    """

    Y_1s = 0

    Y_100ms = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamHelloIntervalEnumEnum']


class EtherLinkOamModeEnumEnum(Enum):
    """
    EtherLinkOamModeEnumEnum

    Ether link oam mode enum

    .. data:: passive = 0

    	Ethernet Link OAM Passive mode

    .. data:: active = 1

    	Ethernet Link OAM Active mode

    """

    passive = 0

    active = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamModeEnumEnum']


class EtherLinkOamRequireModeEnumEnum(Enum):
    """
    EtherLinkOamRequireModeEnumEnum

    Ether link oam require mode enum

    .. data:: passive = 0

    	Ethernet Link OAM Passive mode

    .. data:: active = 1

    	Ethernet Link OAM Active mode

    .. data:: dont_care = 2

    	Ethernet Link OAM mode not required

    """

    passive = 0

    active = 1

    dont_care = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamRequireModeEnumEnum']


class EtherLinkOamThresholdUnitsFramesEnumEnum(Enum):
    """
    EtherLinkOamThresholdUnitsFramesEnumEnum

    Ether link oam threshold units frames enum

    .. data:: frames = 3

    	Define threshold in frames

    .. data:: ppm = 4

    	Define threshold in parts per million

    """

    frames = 3

    ppm = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamThresholdUnitsFramesEnumEnum']


class EtherLinkOamThresholdUnitsSymbolsEnumEnum(Enum):
    """
    EtherLinkOamThresholdUnitsSymbolsEnumEnum

    Ether link oam threshold units symbols enum

    .. data:: symbols = 2

    	Define threshold in symbols

    .. data:: ppm = 4

    	Define threshold in parts per million

    """

    symbols = 2

    ppm = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamThresholdUnitsSymbolsEnumEnum']


class EtherLinkOamThresholdWindowMultiplierEnumEnum(Enum):
    """
    EtherLinkOamThresholdWindowMultiplierEnumEnum

    Ether link oam threshold window multiplier enum

    .. data:: none = 0

    	Do not use a multiplier

    .. data:: thousand = 1

    	Use multiplier of 1000

    .. data:: million = 2

    	Use multiplier of 1,000,000

    .. data:: billion = 3

    	Use multiplier of 1,000,000,000

    """

    none = 0

    thousand = 1

    million = 2

    billion = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamThresholdWindowMultiplierEnumEnum']


class EtherLinkOamWindowUnitsFramesEnumEnum(Enum):
    """
    EtherLinkOamWindowUnitsFramesEnumEnum

    Ether link oam window units frames enum

    .. data:: milliseconds = 1

    	Define window in milliseconds

    .. data:: frames = 3

    	Define window in frames

    """

    milliseconds = 1

    frames = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamWindowUnitsFramesEnumEnum']


class EtherLinkOamWindowUnitsSymbolsEnumEnum(Enum):
    """
    EtherLinkOamWindowUnitsSymbolsEnumEnum

    Ether link oam window units symbols enum

    .. data:: milliseconds = 1

    	Define window in milliseconds

    .. data:: symbols = 2

    	Define window in symbols

    """

    milliseconds = 1

    symbols = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_link_oam_cfg as meta
        return meta._meta_table['EtherLinkOamWindowUnitsSymbolsEnumEnum']



