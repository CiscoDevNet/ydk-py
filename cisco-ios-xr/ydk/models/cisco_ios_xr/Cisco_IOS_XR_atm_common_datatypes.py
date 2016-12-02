""" Cisco_IOS_XR_atm_common_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
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

    .. data:: data = 0

    	Data

    .. data:: ilmi = 2

    	ILMI

    .. data:: layer2 = 3

    	Layer2

    """

    data = 0

    ilmi = 2

    layer2 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcDataEnum']


class AtmPvcEncapsulationEnum(Enum):
    """
    AtmPvcEncapsulationEnum

    Atm pvc encapsulation

    .. data:: snap = 3

    	SNAP

    .. data:: vc_mux = 4

    	VC MUX

    .. data:: nlpid = 5

    	NLPID

    .. data:: aal0 = 7

    	AAL0

    .. data:: aal5 = 8

    	AAL5

    """

    snap = 3

    vc_mux = 4

    nlpid = 5

    aal0 = 7

    aal5 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcEncapsulationEnum']


class AtmPvcShapingEnum(Enum):
    """
    AtmPvcShapingEnum

    Atm pvc shaping

    .. data:: cbr = 1

    	Constant Bit Rate

    .. data:: vbr_nrt = 2

    	Variable Bit Rate-non real time

    .. data:: vbr_rt = 3

    	Variable Bit Rate-real time

    .. data:: ubr = 6

    	Unspecified Bit Rate

    """

    cbr = 1

    vbr_nrt = 2

    vbr_rt = 3

    ubr = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcShapingEnum']


class AtmVpShapingEnum(Enum):
    """
    AtmVpShapingEnum

    Atm vp shaping

    .. data:: cbr = 1

    	Constant Bit Rate

    .. data:: vbr_nrt = 2

    	Variable Bit Rate-non real time

    .. data:: vbr_rt = 3

    	Variable Bit Rate-real time

    .. data:: ubr = 6

    	Unspecified Bit Rate

    """

    cbr = 1

    vbr_nrt = 2

    vbr_rt = 3

    ubr = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmVpShapingEnum']



