""" Cisco_IOS_XR_ethernet_link_oam_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ethernet\-link\-oam package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg,
  Cisco\-IOS\-XR\-l2\-eth\-infra\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EtherLinkOamEventActionEnum(Enum):
    """
    EtherLinkOamEventActionEnum (Enum Class)

    Ether link oam event action enum

    .. data:: disable = 1

    	Perform no action

    .. data:: error_disable = 2

    	Disable the interface

    .. data:: log = 3

    	Log the event

    """

    disable = Enum.YLeaf(1, "disable")

    error_disable = Enum.YLeaf(2, "error-disable")

    log = Enum.YLeaf(3, "log")


class EtherLinkOamEventActionEnumEfd(Enum):
    """
    EtherLinkOamEventActionEnumEfd (Enum Class)

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

    disable = Enum.YLeaf(1, "disable")

    error_disable = Enum.YLeaf(2, "error-disable")

    log = Enum.YLeaf(3, "log")

    efd = Enum.YLeaf(4, "efd")


class EtherLinkOamEventActionPrimEnum(Enum):
    """
    EtherLinkOamEventActionPrimEnum (Enum Class)

    Ether link oam event action prim enum

    .. data:: disable = 1

    	Perform no action

    .. data:: log = 3

    	Log the event

    """

    disable = Enum.YLeaf(1, "disable")

    log = Enum.YLeaf(3, "log")


class EtherLinkOamHelloIntervalEnum(Enum):
    """
    EtherLinkOamHelloIntervalEnum (Enum Class)

    Ether link oam hello interval enum

    .. data:: Y_1s = 0

    	1 s OAM hello interval

    .. data:: Y_100ms = 1

    	100 ms OAM hello interval

    """

    Y_1s = Enum.YLeaf(0, "1s")

    Y_100ms = Enum.YLeaf(1, "100ms")


class EtherLinkOamModeEnum(Enum):
    """
    EtherLinkOamModeEnum (Enum Class)

    Ether link oam mode enum

    .. data:: passive = 0

    	Ethernet Link OAM Passive mode

    .. data:: active = 1

    	Ethernet Link OAM Active mode

    """

    passive = Enum.YLeaf(0, "passive")

    active = Enum.YLeaf(1, "active")


class EtherLinkOamRequireModeEnum(Enum):
    """
    EtherLinkOamRequireModeEnum (Enum Class)

    Ether link oam require mode enum

    .. data:: passive = 0

    	Ethernet Link OAM Passive mode

    .. data:: active = 1

    	Ethernet Link OAM Active mode

    .. data:: dont_care = 2

    	Ethernet Link OAM mode not required

    """

    passive = Enum.YLeaf(0, "passive")

    active = Enum.YLeaf(1, "active")

    dont_care = Enum.YLeaf(2, "dont-care")


class EtherLinkOamThresholdUnitsFramesEnum(Enum):
    """
    EtherLinkOamThresholdUnitsFramesEnum (Enum Class)

    Ether link oam threshold units frames enum

    .. data:: frames = 3

    	Define threshold in frames

    .. data:: ppm = 4

    	Define threshold in parts per million

    """

    frames = Enum.YLeaf(3, "frames")

    ppm = Enum.YLeaf(4, "ppm")


class EtherLinkOamThresholdUnitsSymbolsEnum(Enum):
    """
    EtherLinkOamThresholdUnitsSymbolsEnum (Enum Class)

    Ether link oam threshold units symbols enum

    .. data:: symbols = 2

    	Define threshold in symbols

    .. data:: ppm = 4

    	Define threshold in parts per million

    """

    symbols = Enum.YLeaf(2, "symbols")

    ppm = Enum.YLeaf(4, "ppm")


class EtherLinkOamThresholdWindowMultiplierEnum(Enum):
    """
    EtherLinkOamThresholdWindowMultiplierEnum (Enum Class)

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

    none = Enum.YLeaf(0, "none")

    thousand = Enum.YLeaf(1, "thousand")

    million = Enum.YLeaf(2, "million")

    billion = Enum.YLeaf(3, "billion")


class EtherLinkOamWindowUnitsFramesEnum(Enum):
    """
    EtherLinkOamWindowUnitsFramesEnum (Enum Class)

    Ether link oam window units frames enum

    .. data:: milliseconds = 1

    	Define window in milliseconds

    .. data:: frames = 3

    	Define window in frames

    """

    milliseconds = Enum.YLeaf(1, "milliseconds")

    frames = Enum.YLeaf(3, "frames")


class EtherLinkOamWindowUnitsSymbolsEnum(Enum):
    """
    EtherLinkOamWindowUnitsSymbolsEnum (Enum Class)

    Ether link oam window units symbols enum

    .. data:: milliseconds = 1

    	Define window in milliseconds

    .. data:: symbols = 2

    	Define window in symbols

    """

    milliseconds = Enum.YLeaf(1, "milliseconds")

    symbols = Enum.YLeaf(2, "symbols")



