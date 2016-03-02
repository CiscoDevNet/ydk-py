""" Cisco_IOS_XR_atm_common_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AtmPvcData_Enum(Enum):
    """
    AtmPvcData_Enum

    Atm pvc data

    """

    """

    Data

    """
    DATA = 0

    """

    ILMI

    """
    ILMI = 2

    """

    Layer2

    """
    LAYER2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcData_Enum']


class AtmPvcEncapsulation_Enum(Enum):
    """
    AtmPvcEncapsulation_Enum

    Atm pvc encapsulation

    """

    """

    SNAP

    """
    SNAP = 3

    """

    VC MUX

    """
    VC_MUX = 4

    """

    NLPID

    """
    NLPID = 5

    """

    AAL0

    """
    AAL0 = 7

    """

    AAL5

    """
    AAL5 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcEncapsulation_Enum']


class AtmPvcShaping_Enum(Enum):
    """
    AtmPvcShaping_Enum

    Atm pvc shaping

    """

    """

    Constant Bit Rate

    """
    CBR = 1

    """

    Variable Bit Rate\-non real time

    """
    VBR_NRT = 2

    """

    Variable Bit Rate\-real time

    """
    VBR_RT = 3

    """

    Unspecified Bit Rate

    """
    UBR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcShaping_Enum']


class AtmVpShaping_Enum(Enum):
    """
    AtmVpShaping_Enum

    Atm vp shaping

    """

    """

    Constant Bit Rate

    """
    CBR = 1

    """

    Variable Bit Rate\-non real time

    """
    VBR_NRT = 2

    """

    Variable Bit Rate\-real time

    """
    VBR_RT = 3

    """

    Unspecified Bit Rate

    """
    UBR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmVpShaping_Enum']



