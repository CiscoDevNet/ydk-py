""" Cisco_IOS_XR_sysadmin_entity_state_tc_mib 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2015\-2017 by Cisco Systems, Inc.
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



class EntityAdminState(Enum):
    """
    EntityAdminState (Enum Class)

    .. data:: unknown = 1

    .. data:: locked = 2

    .. data:: shuttingDown = 3

    .. data:: unlocked = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    locked = Enum.YLeaf(2, "locked")

    shuttingDown = Enum.YLeaf(3, "shuttingDown")

    unlocked = Enum.YLeaf(4, "unlocked")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_state_tc_mib as meta
        return meta._meta_table['EntityAdminState']


class EntityOperState(Enum):
    """
    EntityOperState (Enum Class)

    .. data:: unknown = 1

    .. data:: disabled = 2

    .. data:: enabled = 3

    .. data:: testing = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    disabled = Enum.YLeaf(2, "disabled")

    enabled = Enum.YLeaf(3, "enabled")

    testing = Enum.YLeaf(4, "testing")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_state_tc_mib as meta
        return meta._meta_table['EntityOperState']


class EntityStandbyStatus(Enum):
    """
    EntityStandbyStatus (Enum Class)

    .. data:: unknown = 1

    .. data:: hotStandby = 2

    .. data:: coldStandby = 3

    .. data:: providingService = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    hotStandby = Enum.YLeaf(2, "hotStandby")

    coldStandby = Enum.YLeaf(3, "coldStandby")

    providingService = Enum.YLeaf(4, "providingService")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_state_tc_mib as meta
        return meta._meta_table['EntityStandbyStatus']


class EntityUsageState(Enum):
    """
    EntityUsageState (Enum Class)

    .. data:: unknown = 1

    .. data:: idle = 2

    .. data:: active = 3

    .. data:: busy = 4

    """

    unknown = Enum.YLeaf(1, "unknown")

    idle = Enum.YLeaf(2, "idle")

    active = Enum.YLeaf(3, "active")

    busy = Enum.YLeaf(4, "busy")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sysadmin_entity_state_tc_mib as meta
        return meta._meta_table['EntityUsageState']



