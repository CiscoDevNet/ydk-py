""" Cisco_IOS_XE_utd_common_oper 

This module contains a collection of YANG definitions
common for all UTD operational data.
Copyright (c) 2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class UtdUpdateStatusVal(Enum):
    """
    UtdUpdateStatusVal (Enum Class)

    Unified Threat Defense (UTD) update status

    .. data:: utd_update_status_unknown = 0

    	Unified Threat Defense (UTD) update status is unknown

    .. data:: utd_update_status_success = 1

    	Unified Threat Defense (UTD) update successful

    .. data:: utd_update_status_failure = 2

    	Unified Threat Defense (UTD) update failed

    .. data:: utd_update_status_no_update = 3

    	Unified Threat Defense (UTD) update attemped but not required

    """

    utd_update_status_unknown = Enum.YLeaf(0, "utd-update-status-unknown")

    utd_update_status_success = Enum.YLeaf(1, "utd-update-status-success")

    utd_update_status_failure = Enum.YLeaf(2, "utd-update-status-failure")

    utd_update_status_no_update = Enum.YLeaf(3, "utd-update-status-no-update")



