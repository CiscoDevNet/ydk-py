""" Cisco_IOS_XR_atm_common_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AtmPvcDataEnum(Enum):
    """
    AtmPvcDataEnum

    Atm pvc data

    .. data:: DATA = 0

    	Data

    .. data:: ILMI = 2

    	ILMI

    .. data:: LAYER2 = 3

    	Layer2

    """

    DATA = 0

    ILMI = 2

    LAYER2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcDataEnum']


class AtmPvcEncapsulationEnum(Enum):
    """
    AtmPvcEncapsulationEnum

    Atm pvc encapsulation

    .. data:: SNAP = 3

    	SNAP

    .. data:: VC_MUX = 4

    	VC MUX

    .. data:: NLPID = 5

    	NLPID

    .. data:: AAL0 = 7

    	AAL0

    .. data:: AAL5 = 8

    	AAL5

    """

    SNAP = 3

    VC_MUX = 4

    NLPID = 5

    AAL0 = 7

    AAL5 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcEncapsulationEnum']


class AtmPvcShapingEnum(Enum):
    """
    AtmPvcShapingEnum

    Atm pvc shaping

    .. data:: CBR = 1

    	Constant Bit Rate

    .. data:: VBR_NRT = 2

    	Variable Bit Rate-non real time

    .. data:: VBR_RT = 3

    	Variable Bit Rate-real time

    .. data:: UBR = 6

    	Unspecified Bit Rate

    """

    CBR = 1

    VBR_NRT = 2

    VBR_RT = 3

    UBR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcShapingEnum']


class AtmVpShapingEnum(Enum):
    """
    AtmVpShapingEnum

    Atm vp shaping

    .. data:: CBR = 1

    	Constant Bit Rate

    .. data:: VBR_NRT = 2

    	Variable Bit Rate-non real time

    .. data:: VBR_RT = 3

    	Variable Bit Rate-real time

    .. data:: UBR = 6

    	Unspecified Bit Rate

    """

    CBR = 1

    VBR_NRT = 2

    VBR_RT = 3

    UBR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmVpShapingEnum']



