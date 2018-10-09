""" SNMPv2_TC 

This module contains definitions
for the Calvados model objects.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RowStatus(Enum):
    """
    RowStatus (Enum Class)

    .. data:: active = 1

    .. data:: notInService = 2

    .. data:: notReady = 3

    .. data:: createAndGo = 4

    .. data:: createAndWait = 5

    .. data:: destroy = 6

    """

    active = Enum.YLeaf(1, "active")

    notInService = Enum.YLeaf(2, "notInService")

    notReady = Enum.YLeaf(3, "notReady")

    createAndGo = Enum.YLeaf(4, "createAndGo")

    createAndWait = Enum.YLeaf(5, "createAndWait")

    destroy = Enum.YLeaf(6, "destroy")


class StorageType(Enum):
    """
    StorageType (Enum Class)

    .. data:: other = 1

    .. data:: volatile = 2

    .. data:: nonVolatile = 3

    .. data:: permanent = 4

    .. data:: readOnly = 5

    """

    other = Enum.YLeaf(1, "other")

    volatile = Enum.YLeaf(2, "volatile")

    nonVolatile = Enum.YLeaf(3, "nonVolatile")

    permanent = Enum.YLeaf(4, "permanent")

    readOnly = Enum.YLeaf(5, "readOnly")


class TruthValue(Enum):
    """
    TruthValue (Enum Class)

    .. data:: true = 1

    .. data:: false = 2

    """

    true = Enum.YLeaf(1, "true")

    false = Enum.YLeaf(2, "false")



