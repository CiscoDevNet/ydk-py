""" Cisco_IOS_XR_controller_optics_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR controller\-optics package configuration.

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



class OpticsDwdmCarrierGridEnum(Enum):
    """
    OpticsDwdmCarrierGridEnum

    Optics dwdm carrier grid

    .. data:: Y_50G_HZ_GRID = 0

    	50GHz Grid

    .. data:: Y_100MHZ_GRID = 1

    	100MHz Grid

    """

    Y_50G_HZ_GRID = 0

    Y_100MHZ_GRID = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsDwdmCarrierGridEnum']


class OpticsDwdmCarrierParamEnum(Enum):
    """
    OpticsDwdmCarrierParamEnum

    Optics dwdm carrier param

    .. data:: ITU_CH = 0

    	ITU Wave Channel Number

    .. data:: WAVELENGTH = 1

    	Wavelength in nm

    .. data:: FREQUENCY = 2

    	Frequency in Hertz

    """

    ITU_CH = 0

    WAVELENGTH = 1

    FREQUENCY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsDwdmCarrierParamEnum']


class OpticsLoopbackEnum(Enum):
    """
    OpticsLoopbackEnum

    Optics loopback

    .. data:: NONE = 0

    	No Loopback

    .. data:: INTERNAL = 1

    	Internal Loopback

    .. data:: LINE = 2

    	Line Loopback

    """

    NONE = 0

    INTERNAL = 1

    LINE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsLoopbackEnum']


class ThresholdEnum(Enum):
    """
    ThresholdEnum

    Threshold

    .. data:: LOW = 1

    	Low Threshold

    .. data:: HIGH = 2

    	High Threshold

    """

    LOW = 1

    HIGH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['ThresholdEnum']



