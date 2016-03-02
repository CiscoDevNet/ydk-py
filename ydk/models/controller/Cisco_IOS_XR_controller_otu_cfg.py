""" Cisco_IOS_XR_controller_otu_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-otu package configuration.

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



class OtnExpTtiTypeDapi_Enum(Enum):
    """
    OtnExpTtiTypeDapi_Enum

    Otn exp tti type dapi

    """

    """

    Expected TTI DAPI ASCII string

    """
    EXP_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII = 9


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeDapi_Enum']


class OtnExpTtiTypeFull_Enum(Enum):
    """
    OtnExpTtiTypeFull_Enum

    Otn exp tti type full

    """

    """

    Expected TTI Full ASCII string

    """
    EXP_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII = 5

    """

    Expected TTI hex string

    """
    EXP_TTI_HEX__FWD_SLASH__HEX = 7


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeFull_Enum']


class OtnExpTtiTypeOs_Enum(Enum):
    """
    OtnExpTtiTypeOs_Enum

    Otn exp tti type os

    """

    """

    Expected TTI OS ASCII string

    """
    EXP_TTI_OS_ASCII__FWD_SLASH__OS_ASCII = 11

    """

    Expected TTI OS HEX string

    """
    EXP_TTI_OS_HEX__FWD_SLASH__OS_HEX = 13


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeOs_Enum']


class OtnExpTtiTypeSapi_Enum(Enum):
    """
    OtnExpTtiTypeSapi_Enum

    Otn exp tti type sapi

    """

    """

    Expected TTI SAPI ASCII string

    """
    EXP_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII = 15


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeSapi_Enum']


class OtnLoopback_Enum(Enum):
    """
    OtnLoopback_Enum

    Otn loopback

    """

    """

    Line loopback

    """
    LINE = 2

    """

    Internal loopback

    """
    INTERNAL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnLoopback_Enum']


class OtnPerMon_Enum(Enum):
    """
    OtnPerMon_Enum

    Otn per mon

    """

    """

    Performance Monitoring Disabled

    """
    DISABLE = 0

    """

    Performance Monitoring Enabled

    """
    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnPerMon_Enum']


class OtnSecAdminState_Enum(Enum):
    """
    OtnSecAdminState_Enum

    Otn sec admin state

    """

    """

    In normal state

    """
    NORMAL = 0

    """

    Under maintenance

    """
    MAINTENANCE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSecAdminState_Enum']


class OtnSendTtiTypeDapi_Enum(Enum):
    """
    OtnSendTtiTypeDapi_Enum

    Otn send tti type dapi

    """

    """

    Send TTI DAPI ASCII string

    """
    SEND_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII = 8


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeDapi_Enum']


class OtnSendTtiTypeFull_Enum(Enum):
    """
    OtnSendTtiTypeFull_Enum

    Otn send tti type full

    """

    """

    Send TTI Full ASCII string

    """
    SEND_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII = 4

    """

    Send TTI hex string

    """
    SEND_TTI_HEX__FWD_SLASH__HEX = 6


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeFull_Enum']


class OtnSendTtiTypeOs_Enum(Enum):
    """
    OtnSendTtiTypeOs_Enum

    Otn send tti type os

    """

    """

    Send TTI OS ASCII string

    """
    SEND_TTI_OS_ASCII__FWD_SLASH__OS_ASCII = 10

    """

    Send TTI OS HEX string

    """
    SEND_TTI_OS_HEX__FWD_SLASH__OS_HEX = 12


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeOs_Enum']


class OtnSendTtiTypeSapi_Enum(Enum):
    """
    OtnSendTtiTypeSapi_Enum

    Otn send tti type sapi

    """

    """

    Send TTI SAPI ASCII string

    """
    SEND_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII = 14


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeSapi_Enum']


class OtuForwardErrorCorrection_Enum(Enum):
    """
    OtuForwardErrorCorrection_Enum

    Otu forward error correction

    """

    """

    No Fec

    """
    NONE = 1

    """

    Standard Fec

    """
    STANDARD = 2

    """

    EnhancedI7 Fec

    """
    ENHANCED_I7 = 4

    """

    Enhanced I4 Fec

    """
    ENHANCED_I4 = 8

    """

    EnhancedSwizzle Fec

    """
    ENHANCED_SWIZZLE = 16

    """

    EnhancedHG20 Fec

    """
    ENHANCED_HG20 = 32

    """

    EnhancedHG7 Fec

    """
    ENHANCED_HG7 = 64


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtuForwardErrorCorrection_Enum']



