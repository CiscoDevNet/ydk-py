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



class OpticsDwdmCarrierGrid_Enum(Enum):
    """
    OpticsDwdmCarrierGrid_Enum

    Optics dwdm carrier grid

    """

    """

    50GHz Grid

    """
    Y_50G_HZ_GRID = 0

    """

    100MHz Grid

    """
    Y_100MHZ_GRID = 1


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsDwdmCarrierGrid_Enum']


class OpticsDwdmCarrierParam_Enum(Enum):
    """
    OpticsDwdmCarrierParam_Enum

    Optics dwdm carrier param

    """

    """

    ITU Wave Channel Number

    """
    ITU_CH = 0

    """

    Wavelength in nm

    """
    WAVELENGTH = 1

    """

    Frequency in Hertz

    """
    FREQUENCY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsDwdmCarrierParam_Enum']


class OpticsLoopback_Enum(Enum):
    """
    OpticsLoopback_Enum

    Optics loopback

    """

    """

    No Loopback

    """
    NONE = 0

    """

    Internal Loopback

    """
    INTERNAL = 1

    """

    Line Loopback

    """
    LINE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['OpticsLoopback_Enum']


class Threshold_Enum(Enum):
    """
    Threshold_Enum

    Threshold

    """

    """

    Low Threshold

    """
    LOW = 1

    """

    High Threshold

    """
    HIGH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.controller._meta import _Cisco_IOS_XR_controller_optics_cfg as meta
        return meta._meta_table['Threshold_Enum']



