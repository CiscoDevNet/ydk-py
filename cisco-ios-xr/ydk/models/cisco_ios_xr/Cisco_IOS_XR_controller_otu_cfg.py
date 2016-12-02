""" Cisco_IOS_XR_controller_otu_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package configuration.

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



class OtnExpTtiTypeDapiEnum(Enum):
    """
    OtnExpTtiTypeDapiEnum

    Otn exp tti type dapi

    .. data:: exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 9

    	Expected TTI DAPI ASCII string

    """

    exp_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeDapiEnum']


class OtnExpTtiTypeFullEnum(Enum):
    """
    OtnExpTtiTypeFullEnum

    Otn exp tti type full

    .. data:: exp_tti_full_ascii__FWD_SLASH__full_ascii = 5

    	Expected TTI Full ASCII string

    .. data:: exp_tti_hex__FWD_SLASH__hex = 7

    	Expected TTI hex string

    """

    exp_tti_full_ascii__FWD_SLASH__full_ascii = 5

    exp_tti_hex__FWD_SLASH__hex = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeFullEnum']


class OtnExpTtiTypeOsEnum(Enum):
    """
    OtnExpTtiTypeOsEnum

    Otn exp tti type os

    .. data:: exp_tti_os_ascii__FWD_SLASH__os_ascii = 11

    	Expected TTI OS ASCII string

    .. data:: exp_tti_os_hex__FWD_SLASH__os_hex = 13

    	Expected TTI OS HEX string

    """

    exp_tti_os_ascii__FWD_SLASH__os_ascii = 11

    exp_tti_os_hex__FWD_SLASH__os_hex = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeOsEnum']


class OtnExpTtiTypeSapiEnum(Enum):
    """
    OtnExpTtiTypeSapiEnum

    Otn exp tti type sapi

    .. data:: exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 15

    	Expected TTI SAPI ASCII string

    """

    exp_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeSapiEnum']


class OtnLoopbackEnum(Enum):
    """
    OtnLoopbackEnum

    Otn loopback

    .. data:: line = 2

    	Line loopback

    .. data:: internal = 4

    	Internal loopback

    """

    line = 2

    internal = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnLoopbackEnum']


class OtnPerMonEnum(Enum):
    """
    OtnPerMonEnum

    Otn per mon

    .. data:: disable = 0

    	Performance Monitoring Disabled

    .. data:: enable = 1

    	Performance Monitoring Enabled

    """

    disable = 0

    enable = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnPerMonEnum']


class OtnSecAdminStateEnum(Enum):
    """
    OtnSecAdminStateEnum

    Otn sec admin state

    .. data:: normal = 0

    	In normal state

    .. data:: maintenance = 1

    	Under maintenance

    """

    normal = 0

    maintenance = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSecAdminStateEnum']


class OtnSendTtiTypeDapiEnum(Enum):
    """
    OtnSendTtiTypeDapiEnum

    Otn send tti type dapi

    .. data:: send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 8

    	Send TTI DAPI ASCII string

    """

    send_tti_dapi_ascii__FWD_SLASH__dapi_ascii = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeDapiEnum']


class OtnSendTtiTypeFullEnum(Enum):
    """
    OtnSendTtiTypeFullEnum

    Otn send tti type full

    .. data:: send_tti_full_ascii__FWD_SLASH__full_ascii = 4

    	Send TTI Full ASCII string

    .. data:: send_tti_hex__FWD_SLASH__hex = 6

    	Send TTI hex string

    """

    send_tti_full_ascii__FWD_SLASH__full_ascii = 4

    send_tti_hex__FWD_SLASH__hex = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeFullEnum']


class OtnSendTtiTypeOsEnum(Enum):
    """
    OtnSendTtiTypeOsEnum

    Otn send tti type os

    .. data:: send_tti_os_ascii__FWD_SLASH__os_ascii = 10

    	Send TTI OS ASCII string

    .. data:: send_tti_os_hex__FWD_SLASH__os_hex = 12

    	Send TTI OS HEX string

    """

    send_tti_os_ascii__FWD_SLASH__os_ascii = 10

    send_tti_os_hex__FWD_SLASH__os_hex = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeOsEnum']


class OtnSendTtiTypeSapiEnum(Enum):
    """
    OtnSendTtiTypeSapiEnum

    Otn send tti type sapi

    .. data:: send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 14

    	Send TTI SAPI ASCII string

    """

    send_tti_sapi_ascii__FWD_SLASH__sapi_ascii = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeSapiEnum']


class OtuForwardErrorCorrectionEnum(Enum):
    """
    OtuForwardErrorCorrectionEnum

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

    none = 1

    standard = 2

    enhanced_i7 = 4

    enhanced_i4 = 8

    enhanced_swizzle = 16

    enhanced_hg20 = 32

    enhanced_hg7 = 64


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtuForwardErrorCorrectionEnum']



