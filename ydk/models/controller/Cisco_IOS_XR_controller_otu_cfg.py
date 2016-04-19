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



class OtnExpTtiTypeDapiEnum(Enum):
    """
    OtnExpTtiTypeDapiEnum

    Otn exp tti type dapi

    .. data:: EXP_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII = 9

    	Expected TTI DAPI ASCII string

    """

    EXP_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII = 9


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeDapiEnum']


class OtnExpTtiTypeFullEnum(Enum):
    """
    OtnExpTtiTypeFullEnum

    Otn exp tti type full

    .. data:: EXP_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII = 5

    	Expected TTI Full ASCII string

    .. data:: EXP_TTI_HEX__FWD_SLASH__HEX = 7

    	Expected TTI hex string

    """

    EXP_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII = 5

    EXP_TTI_HEX__FWD_SLASH__HEX = 7


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeFullEnum']


class OtnExpTtiTypeOsEnum(Enum):
    """
    OtnExpTtiTypeOsEnum

    Otn exp tti type os

    .. data:: EXP_TTI_OS_ASCII__FWD_SLASH__OS_ASCII = 11

    	Expected TTI OS ASCII string

    .. data:: EXP_TTI_OS_HEX__FWD_SLASH__OS_HEX = 13

    	Expected TTI OS HEX string

    """

    EXP_TTI_OS_ASCII__FWD_SLASH__OS_ASCII = 11

    EXP_TTI_OS_HEX__FWD_SLASH__OS_HEX = 13


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeOsEnum']


class OtnExpTtiTypeSapiEnum(Enum):
    """
    OtnExpTtiTypeSapiEnum

    Otn exp tti type sapi

    .. data:: EXP_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII = 15

    	Expected TTI SAPI ASCII string

    """

    EXP_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII = 15


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnExpTtiTypeSapiEnum']


class OtnLoopbackEnum(Enum):
    """
    OtnLoopbackEnum

    Otn loopback

    .. data:: LINE = 2

    	Line loopback

    .. data:: INTERNAL = 4

    	Internal loopback

    """

    LINE = 2

    INTERNAL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnLoopbackEnum']


class OtnPerMonEnum(Enum):
    """
    OtnPerMonEnum

    Otn per mon

    .. data:: DISABLE = 0

    	Performance Monitoring Disabled

    .. data:: ENABLE = 1

    	Performance Monitoring Enabled

    """

    DISABLE = 0

    ENABLE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnPerMonEnum']


class OtnSecAdminStateEnum(Enum):
    """
    OtnSecAdminStateEnum

    Otn sec admin state

    .. data:: NORMAL = 0

    	In normal state

    .. data:: MAINTENANCE = 1

    	Under maintenance

    """

    NORMAL = 0

    MAINTENANCE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSecAdminStateEnum']


class OtnSendTtiTypeDapiEnum(Enum):
    """
    OtnSendTtiTypeDapiEnum

    Otn send tti type dapi

    .. data:: SEND_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII = 8

    	Send TTI DAPI ASCII string

    """

    SEND_TTI_DAPI_ASCII__FWD_SLASH__DAPI_ASCII = 8


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeDapiEnum']


class OtnSendTtiTypeFullEnum(Enum):
    """
    OtnSendTtiTypeFullEnum

    Otn send tti type full

    .. data:: SEND_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII = 4

    	Send TTI Full ASCII string

    .. data:: SEND_TTI_HEX__FWD_SLASH__HEX = 6

    	Send TTI hex string

    """

    SEND_TTI_FULL_ASCII__FWD_SLASH__FULL_ASCII = 4

    SEND_TTI_HEX__FWD_SLASH__HEX = 6


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeFullEnum']


class OtnSendTtiTypeOsEnum(Enum):
    """
    OtnSendTtiTypeOsEnum

    Otn send tti type os

    .. data:: SEND_TTI_OS_ASCII__FWD_SLASH__OS_ASCII = 10

    	Send TTI OS ASCII string

    .. data:: SEND_TTI_OS_HEX__FWD_SLASH__OS_HEX = 12

    	Send TTI OS HEX string

    """

    SEND_TTI_OS_ASCII__FWD_SLASH__OS_ASCII = 10

    SEND_TTI_OS_HEX__FWD_SLASH__OS_HEX = 12


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeOsEnum']


class OtnSendTtiTypeSapiEnum(Enum):
    """
    OtnSendTtiTypeSapiEnum

    Otn send tti type sapi

    .. data:: SEND_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII = 14

    	Send TTI SAPI ASCII string

    """

    SEND_TTI_SAPI_ASCII__FWD_SLASH__SAPI_ASCII = 14


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtnSendTtiTypeSapiEnum']


class OtuForwardErrorCorrectionEnum(Enum):
    """
    OtuForwardErrorCorrectionEnum

    Otu forward error correction

    .. data:: NONE = 1

    	No Fec

    .. data:: STANDARD = 2

    	Standard Fec

    .. data:: ENHANCED_I7 = 4

    	EnhancedI7 Fec

    .. data:: ENHANCED_I4 = 8

    	Enhanced I4 Fec

    .. data:: ENHANCED_SWIZZLE = 16

    	EnhancedSwizzle Fec

    .. data:: ENHANCED_HG20 = 32

    	EnhancedHG20 Fec

    .. data:: ENHANCED_HG7 = 64

    	EnhancedHG7 Fec

    """

    NONE = 1

    STANDARD = 2

    ENHANCED_I7 = 4

    ENHANCED_I4 = 8

    ENHANCED_SWIZZLE = 16

    ENHANCED_HG20 = 32

    ENHANCED_HG7 = 64


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_otu_cfg as meta
        return meta._meta_table['OtuForwardErrorCorrectionEnum']



