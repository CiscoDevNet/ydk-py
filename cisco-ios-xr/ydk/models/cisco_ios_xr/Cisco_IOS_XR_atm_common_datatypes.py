""" Cisco_IOS_XR_atm_common_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AtmPvcData(Enum):
    """
    AtmPvcData (Enum Class)

    Atm pvc data

    .. data:: data = 0

    	Data

    .. data:: ilmi = 2

    	ILMI

    .. data:: layer2 = 3

    	Layer2

    """

    data = Enum.YLeaf(0, "data")

    ilmi = Enum.YLeaf(2, "ilmi")

    layer2 = Enum.YLeaf(3, "layer2")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcData']


class AtmPvcEncapsulation(Enum):
    """
    AtmPvcEncapsulation (Enum Class)

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

    snap = Enum.YLeaf(3, "snap")

    vc_mux = Enum.YLeaf(4, "vc-mux")

    nlpid = Enum.YLeaf(5, "nlpid")

    aal0 = Enum.YLeaf(7, "aal0")

    aal5 = Enum.YLeaf(8, "aal5")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcEncapsulation']


class AtmPvcShaping(Enum):
    """
    AtmPvcShaping (Enum Class)

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

    cbr = Enum.YLeaf(1, "cbr")

    vbr_nrt = Enum.YLeaf(2, "vbr-nrt")

    vbr_rt = Enum.YLeaf(3, "vbr-rt")

    ubr = Enum.YLeaf(6, "ubr")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmPvcShaping']


class AtmVpShaping(Enum):
    """
    AtmVpShaping (Enum Class)

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

    cbr = Enum.YLeaf(1, "cbr")

    vbr_nrt = Enum.YLeaf(2, "vbr-nrt")

    vbr_rt = Enum.YLeaf(3, "vbr-rt")

    ubr = Enum.YLeaf(6, "ubr")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_atm_common_datatypes as meta
        return meta._meta_table['AtmVpShaping']



