""" Cisco_IOS_XR_controller_otu_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package configuration.

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


class OtnExpTtiTypeDapi(Enum):
    """
    OtnExpTtiTypeDapi

    Otn exp tti type dapi

    .. data:: exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 9

    	Expected TTI DAPI ASCII string

    """

    exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = Enum.YLeaf(9, "exp-tti-dapi-ascii/dapi-ascii")


class OtnExpTtiTypeFull(Enum):
    """
    OtnExpTtiTypeFull

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
    OtnExpTtiTypeOs

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
    OtnExpTtiTypeSapi

    Otn exp tti type sapi

    .. data:: exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 15

    	Expected TTI SAPI ASCII string

    """

    exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = Enum.YLeaf(15, "exp-tti-sapi-ascii/sapi-ascii")


class OtnLoopback(Enum):
    """
    OtnLoopback

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
    OtnPerMon

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
    OtnSecAdminState

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
    OtnSendTtiTypeDapi

    Otn send tti type dapi

    .. data:: send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 8

    	Send TTI DAPI ASCII string

    """

    send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = Enum.YLeaf(8, "send-tti-dapi-ascii/dapi-ascii")


class OtnSendTtiTypeFull(Enum):
    """
    OtnSendTtiTypeFull

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
    OtnSendTtiTypeOs

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
    OtnSendTtiTypeSapi

    Otn send tti type sapi

    .. data:: send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 14

    	Send TTI SAPI ASCII string

    """

    send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = Enum.YLeaf(14, "send-tti-sapi-ascii/sapi-ascii")


class OtuForwardErrorCorrection(Enum):
    """
    OtuForwardErrorCorrection

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

    """

    none = Enum.YLeaf(1, "none")

    standard = Enum.YLeaf(2, "standard")

    enhanced_i7 = Enum.YLeaf(4, "enhanced-i7")

    enhanced_i4 = Enum.YLeaf(8, "enhanced-i4")

    enhanced_swizzle = Enum.YLeaf(16, "enhanced-swizzle")

    enhanced_hg20 = Enum.YLeaf(32, "enhanced-hg20")

    enhanced_hg7 = Enum.YLeaf(64, "enhanced-hg7")



