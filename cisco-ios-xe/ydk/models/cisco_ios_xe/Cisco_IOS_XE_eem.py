""" Cisco_IOS_XE_eem 

Cisco XE Native Embedded Event Manager (EEM) Yang model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class OperatorType(Enum):
    """
    OperatorType (Enum Class)

    .. data:: eq = 0

    .. data:: ge = 1

    .. data:: gt = 2

    .. data:: le = 3

    .. data:: lt = 4

    .. data:: ne = 5

    """

    eq = Enum.YLeaf(0, "eq")

    ge = Enum.YLeaf(1, "ge")

    gt = Enum.YLeaf(2, "gt")

    le = Enum.YLeaf(3, "le")

    lt = Enum.YLeaf(4, "lt")

    ne = Enum.YLeaf(5, "ne")



