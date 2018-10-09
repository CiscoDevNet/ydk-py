""" Cisco_IOS_XR_controller_otu_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OtnExpTtiTypeDapi(Enum):
    """
    OtnExpTtiTypeDapi (Enum Class)

    Otn exp tti type dapi

    .. data:: exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 9

    	Expected TTI DAPI ASCII string

    """

    exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = Enum.YLeaf(9, "exp-tti-dapi-ascii/dapi-ascii")


class OtnExpTtiTypeFull(Enum):
    """
    OtnExpTtiTypeFull (Enum Class)

    Otn exp tti type full

    .. data:: exp_tti_full_ascii__FWD_SLASH__full_ascii = 5

    	Expected TTI Full ASCII string

    .. data:: exp_tti_hex__FWD_SLASH__hex = 7

    	Expected TTI hex string

    """

    exp_tti_full_ascii__FWD_SLASH__full_ascii = Enum.YLeaf(5, "exp-tti-full-ascii/full-ascii")

    exp_tti_hex__FWD_SLASH__hex = Enum.YLeaf(7, "exp-tti-hex/hex")


class OtnExpTtiTypeOs(Enum):
    """
    OtnExpTtiTypeOs (Enum Class)

    Otn exp tti type os

    .. data:: exp_tti_os_ascii__FWD_SLASH__os_ascii = 11

    	Expected TTI OS ASCII string

    .. data:: exp_tti_os_hex__FWD_SLASH__os_hex = 13

    	Expected TTI OS HEX string

    """

    exp_tti_os_ascii__FWD_SLASH__os_ascii = Enum.YLeaf(11, "exp-tti-os-ascii/os-ascii")

    exp_tti_os_hex__FWD_SLASH__os_hex = Enum.YLeaf(13, "exp-tti-os-hex/os-hex")


class OtnExpTtiTypeSapi(Enum):
    """
    OtnExpTtiTypeSapi (Enum Class)

    Otn exp tti type sapi

    .. data:: exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 15

    	Expected TTI SAPI ASCII string

    """

    exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = Enum.YLeaf(15, "exp-tti-sapi-ascii/sapi-ascii")


class OtnLoopback(Enum):
    """
    OtnLoopback (Enum Class)

    Otn loopback

    .. data:: line = 2

    	Line loopback

    .. data:: internal = 4

    	Internal loopback

    """

    line = Enum.YLeaf(2, "line")

    internal = Enum.YLeaf(4, "internal")


class OtnPerMon(Enum):
    """
    OtnPerMon (Enum Class)

    Otn per mon

    .. data:: disable = 0

    	Performance Monitoring Disabled

    .. data:: enable = 1

    	Performance Monitoring Enabled

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class OtnSecAdminState(Enum):
    """
    OtnSecAdminState (Enum Class)

    Otn sec admin state

    .. data:: normal = 0

    	In normal state

    .. data:: maintenance = 1

    	Under maintenance

    """

    normal = Enum.YLeaf(0, "normal")

    maintenance = Enum.YLeaf(1, "maintenance")


class OtnSendTtiTypeDapi(Enum):
    """
    OtnSendTtiTypeDapi (Enum Class)

    Otn send tti type dapi

    .. data:: send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 8

    	Send TTI DAPI ASCII string

    """

    send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = Enum.YLeaf(8, "send-tti-dapi-ascii/dapi-ascii")


class OtnSendTtiTypeFull(Enum):
    """
    OtnSendTtiTypeFull (Enum Class)

    Otn send tti type full

    .. data:: send_tti_full_ascii__FWD_SLASH__full_ascii = 4

    	Send TTI Full ASCII string

    .. data:: send_tti_hex__FWD_SLASH__hex = 6

    	Send TTI hex string

    """

    send_tti_full_ascii__FWD_SLASH__full_ascii = Enum.YLeaf(4, "send-tti-full-ascii/full-ascii")

    send_tti_hex__FWD_SLASH__hex = Enum.YLeaf(6, "send-tti-hex/hex")


class OtnSendTtiTypeOs(Enum):
    """
    OtnSendTtiTypeOs (Enum Class)

    Otn send tti type os

    .. data:: send_tti_os_ascii__FWD_SLASH__os_ascii = 10

    	Send TTI OS ASCII string

    .. data:: send_tti_os_hex__FWD_SLASH__os_hex = 12

    	Send TTI OS HEX string

    """

    send_tti_os_ascii__FWD_SLASH__os_ascii = Enum.YLeaf(10, "send-tti-os-ascii/os-ascii")

    send_tti_os_hex__FWD_SLASH__os_hex = Enum.YLeaf(12, "send-tti-os-hex/os-hex")


class OtnSendTtiTypeSapi(Enum):
    """
    OtnSendTtiTypeSapi (Enum Class)

    Otn send tti type sapi

    .. data:: send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 14

    	Send TTI SAPI ASCII string

    """

    send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = Enum.YLeaf(14, "send-tti-sapi-ascii/sapi-ascii")


class OtuForwardErrorCorrection(Enum):
    """
    OtuForwardErrorCorrection (Enum Class)

    Otu forward error correction

    .. data:: none = 1

    	No Fec

    .. data:: standard = 2

    	Standard Fec

    .. data:: enhanced_i7 = 4

    	EnhancedI7 Fec

    .. data:: enhanced_i4 = 8

    	Enhanced I4 Fec

    .. data:: enhanced_swizzle = 16

    	EnhancedSwizzle Fec

    .. data:: enhanced_hg20 = 32

    	EnhancedHG20 Fec

    .. data:: enhanced_hg7 = 64

    	EnhancedHG7 Fec

    .. data:: enhanced_sd15 = 512

    	EnhancedSD15 Fec

    .. data:: enhanced_sd27 = 1024

    	EnhancedSD27 Fec

    """

    none = Enum.YLeaf(1, "none")

    standard = Enum.YLeaf(2, "standard")

    enhanced_i7 = Enum.YLeaf(4, "enhanced-i7")

    enhanced_i4 = Enum.YLeaf(8, "enhanced-i4")

    enhanced_swizzle = Enum.YLeaf(16, "enhanced-swizzle")

    enhanced_hg20 = Enum.YLeaf(32, "enhanced-hg20")

    enhanced_hg7 = Enum.YLeaf(64, "enhanced-hg7")

    enhanced_sd15 = Enum.YLeaf(512, "enhanced-sd15")

    enhanced_sd27 = Enum.YLeaf(1024, "enhanced-sd27")


class OtuMode(Enum):
    """
    OtuMode (Enum Class)

    Otu mode

    .. data:: mode_invalid = 0

    	prbs Mode Invalid

    .. data:: mode_source = 1

    	Prbs Mode Source

    .. data:: mode_sink = 2

    	Prbs Mode Sink

    .. data:: mode_source_sink = 3

    	Prbs Mode Source_Sink

    """

    mode_invalid = Enum.YLeaf(0, "mode-invalid")

    mode_source = Enum.YLeaf(1, "mode-source")

    mode_sink = Enum.YLeaf(2, "mode-sink")

    mode_source_sink = Enum.YLeaf(3, "mode-source-sink")


class OtuPattern(Enum):
    """
    OtuPattern (Enum Class)

    Otu pattern

    .. data:: pattern_none = 0

    	prbs pattern None

    .. data:: pattern_pn31 = 1

    	Prbs pattern pn31

    .. data:: pattern_pn23 = 2

    	Prbs pattern pn23

    .. data:: pattern_pn11 = 4

    	Prbs pattern pn11

    .. data:: pattern_inverted_pn31 = 8

    	Prbs pattern inverted pn31

    .. data:: pattern_inverted_pn11 = 16

    	Prbs pattern inverted pn11

    .. data:: pattern_pn15 = 32

    	Prbs pattern pn15

    """

    pattern_none = Enum.YLeaf(0, "pattern-none")

    pattern_pn31 = Enum.YLeaf(1, "pattern-pn31")

    pattern_pn23 = Enum.YLeaf(2, "pattern-pn23")

    pattern_pn11 = Enum.YLeaf(4, "pattern-pn11")

    pattern_inverted_pn31 = Enum.YLeaf(8, "pattern-inverted-pn31")

    pattern_inverted_pn11 = Enum.YLeaf(16, "pattern-inverted-pn11")

    pattern_pn15 = Enum.YLeaf(32, "pattern-pn15")



