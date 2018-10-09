""" Cisco_IOS_XR_sysadmin_types 

This module contains definitions
for the Calvados model objects.

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

This module contains a collection of derived 
YANG data types specific to Sysadmin.

Copyright(c) 2011\-2016 by Cisco Systems, Inc.
All rights reserved.

Copyright (c) 2012\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Adminstate(Enum):
    """
    Adminstate (Enum Class)

    .. data:: disable = 0

    """

    disable = Enum.YLeaf(0, "disable")


class FabricLinkTypes(Enum):
    """
    FabricLinkTypes (Enum Class)

    .. data:: S1 = 0

    .. data:: S2 = 1

    .. data:: S3 = 2

    """

    S1 = Enum.YLeaf(0, "S1")

    S2 = Enum.YLeaf(1, "S2")

    S3 = Enum.YLeaf(2, "S3")


class GenericHaRole(Enum):
    """
    GenericHaRole (Enum Class)

    .. data:: no_ha_role = 0

    .. data:: Active = 1

    .. data:: Standby = 2

    """

    no_ha_role = Enum.YLeaf(0, "no-ha-role")

    Active = Enum.YLeaf(1, "Active")

    Standby = Enum.YLeaf(2, "Standby")


class GenericOperStatus(Enum):
    """
    GenericOperStatus (Enum Class)

    .. data:: up = 0

    .. data:: down = 1

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")


class GenericOperStatus_(Enum):
    """
    GenericOperStatus\_ (Enum Class)

    .. data:: up = 0

    .. data:: down = 1

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")


class GenericOperStatus__(Enum):
    """
    GenericOperStatus\_\_ (Enum Class)

    .. data:: up = 0

    .. data:: down = 1

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")


class RackId(Enum):
    """
    RackId (Enum Class)

    Identifies the rack number of FCC/LCC.

    LCC racks are identified by numbers rack0..7

    FCC racks are identified by numbers F0..F3

    BSC racks are identified by numbers 128..129

    .. data:: L0 = 0

    .. data:: L1 = 1

    .. data:: L2 = 2

    .. data:: L3 = 3

    .. data:: L4 = 4

    .. data:: L5 = 5

    .. data:: L6 = 6

    .. data:: L7 = 7

    .. data:: L8 = 8

    .. data:: L9 = 9

    .. data:: L10 = 10

    .. data:: L11 = 11

    .. data:: L12 = 12

    .. data:: L13 = 13

    .. data:: L14 = 14

    .. data:: L15 = 15

    .. data:: F0 = 16

    .. data:: F1 = 17

    .. data:: F2 = 18

    .. data:: F3 = 19

    .. data:: B0 = 20

    .. data:: B1 = 21

    """

    L0 = Enum.YLeaf(0, "L0")

    L1 = Enum.YLeaf(1, "L1")

    L2 = Enum.YLeaf(2, "L2")

    L3 = Enum.YLeaf(3, "L3")

    L4 = Enum.YLeaf(4, "L4")

    L5 = Enum.YLeaf(5, "L5")

    L6 = Enum.YLeaf(6, "L6")

    L7 = Enum.YLeaf(7, "L7")

    L8 = Enum.YLeaf(8, "L8")

    L9 = Enum.YLeaf(9, "L9")

    L10 = Enum.YLeaf(10, "L10")

    L11 = Enum.YLeaf(11, "L11")

    L12 = Enum.YLeaf(12, "L12")

    L13 = Enum.YLeaf(13, "L13")

    L14 = Enum.YLeaf(14, "L14")

    L15 = Enum.YLeaf(15, "L15")

    F0 = Enum.YLeaf(16, "F0")

    F1 = Enum.YLeaf(17, "F1")

    F2 = Enum.YLeaf(18, "F2")

    F3 = Enum.YLeaf(19, "F3")

    B0 = Enum.YLeaf(20, "B0")

    B1 = Enum.YLeaf(21, "B1")



