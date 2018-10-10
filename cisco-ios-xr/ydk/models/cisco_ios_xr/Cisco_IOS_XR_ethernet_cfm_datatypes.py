""" Cisco_IOS_XR_ethernet_cfm_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BandwidthNotificationState(Enum):
    """
    BandwidthNotificationState (Enum Class)

    Bandwidth notification state

    .. data:: ok = 1

    	Link is not degraded

    .. data:: degraded = 2

    	Link is in degraded state

    """

    ok = Enum.YLeaf(1, "ok")

    degraded = Enum.YLeaf(2, "degraded")


class CfmAisInterval(Enum):
    """
    CfmAisInterval (Enum Class)

    Cfm ais interval

    .. data:: Y_1s = 4

    	1s

    .. data:: Y_1m = 6

    	1m

    """

    Y_1s = Enum.YLeaf(4, "1s")

    Y_1m = Enum.YLeaf(6, "1m")


class CfmCcmInterval(Enum):
    """
    CfmCcmInterval (Enum Class)

    Cfm ccm interval

    .. data:: Y_3__DOT__3ms = 1

    	3.3ms

    .. data:: Y_10ms = 2

    	10ms

    .. data:: Y_100ms = 3

    	100ms

    .. data:: Y_1s = 4

    	1s

    .. data:: Y_10s = 5

    	10s

    .. data:: Y_1m = 6

    	1m

    .. data:: Y_10m = 7

    	10m

    """

    Y_3__DOT__3ms = Enum.YLeaf(1, "3.3ms")

    Y_10ms = Enum.YLeaf(2, "10ms")

    Y_100ms = Enum.YLeaf(3, "100ms")

    Y_1s = Enum.YLeaf(4, "1s")

    Y_10s = Enum.YLeaf(5, "10s")

    Y_1m = Enum.YLeaf(6, "1m")

    Y_10m = Enum.YLeaf(7, "10m")


class CfmMepDir(Enum):
    """
    CfmMepDir (Enum Class)

    Cfm mep dir

    .. data:: up = 0

    	Up MEP

    .. data:: down = 1

    	Down MEP

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")



