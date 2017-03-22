""" Cisco_IOS_XR_controller_optics_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package configuration.

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



class OpticsDwdmCarrierGridEnum(Enum):
    """
    OpticsDwdmCarrierGridEnum

    Optics dwdm carrier grid

    .. data:: Y_50g_hz_grid = 0

    	50GHz Grid

    .. data:: Y_100mhz_grid = 1

    	100MHz Grid

    """

    Y_50g_hz_grid = 0

    Y_100mhz_grid = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsDwdmCarrierGridEnum']


class OpticsDwdmCarrierParamEnum(Enum):
    """
    OpticsDwdmCarrierParamEnum

    Optics dwdm carrier param

    .. data:: itu_ch = 0

    	ITU Wave Channel Number

    .. data:: wavelength = 1

    	Wavelength in nm

    .. data:: frequency = 2

    	Frequency in Hertz

    """

    itu_ch = 0

    wavelength = 1

    frequency = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsDwdmCarrierParamEnum']


class OpticsFecEnum(Enum):
    """
    OpticsFecEnum

    Optics fec

    .. data:: fec_none = 0

    	No Fec

    .. data:: fec_h15 = 1

    	Enhanced H15

    .. data:: fec_h25 = 2

    	Enhanced H25

    .. data:: fec_h15_de = 4

    	Enhanced H15 DE

    .. data:: fec_h25_de = 8

    	Enhanced H25 DE

    """

    fec_none = 0

    fec_h15 = 1

    fec_h25 = 2

    fec_h15_de = 4

    fec_h25_de = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsFecEnum']


class OpticsLoopbackEnum(Enum):
    """
    OpticsLoopbackEnum

    Optics loopback

    .. data:: none = 0

    	No Loopback

    .. data:: internal = 1

    	Internal Loopback

    .. data:: line = 2

    	Line Loopback

    """

    none = 0

    internal = 1

    line = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsLoopbackEnum']


class OpticsOtsAmpliControlModeEnum(Enum):
    """
    OpticsOtsAmpliControlModeEnum

    Optics ots ampli control mode

    .. data:: automatic = 1

    	Automatic Amplifier Mode

    .. data:: manual = 2

    	Manual Amplifier Mode

    """

    automatic = 1

    manual = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsOtsAmpliControlModeEnum']


class OpticsOtsAmpliGainRangeEnum(Enum):
    """
    OpticsOtsAmpliGainRangeEnum

    Optics ots ampli gain range

    .. data:: normal = 1

    	Normal Amplifier Gain Range

    .. data:: extended = 2

    	Extended Amplifier Gain Range

    """

    normal = 1

    extended = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsOtsAmpliGainRangeEnum']


class OpticsOtsSafetyControlModeEnum(Enum):
    """
    OpticsOtsSafetyControlModeEnum

    Optics ots safety control mode

    .. data:: auto = 1

    	Automatic Safety Control Mode

    .. data:: disabled = 2

    	Disable Safety Control Mode

    """

    auto = 1

    disabled = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsOtsSafetyControlModeEnum']


class ThresholdEnum(Enum):
    """
    ThresholdEnum

    Threshold

    .. data:: low = 1

    	Low Threshold

    .. data:: high = 2

    	High Threshold

    """

    low = 1

    high = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['ThresholdEnum']



