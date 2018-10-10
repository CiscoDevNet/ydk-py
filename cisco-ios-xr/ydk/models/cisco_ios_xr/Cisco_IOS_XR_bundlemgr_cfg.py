""" Cisco_IOS_XR_bundlemgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR bundlemgr package configuration.

This module contains definitions
for the following management objects\:
  lacp\: Link Aggregation Control Protocol commands

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-rgmgr\-cfg,
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BfdMode(Enum):
    """
    BfdMode (Enum Class)

    Bfd mode

    .. data:: no_cfg = 0

    	BFD mode not configured on per-bundle basis

    .. data:: cisco = 1

    	BFD mode Cisco

    .. data:: ietf = 2

    	BFD mode IETF

    """

    no_cfg = Enum.YLeaf(0, "no-cfg")

    cisco = Enum.YLeaf(1, "cisco")

    ietf = Enum.YLeaf(2, "ietf")


class BundleCiscoExtTypes(Enum):
    """
    BundleCiscoExtTypes (Enum Class)

    Bundle cisco ext types

    .. data:: lon_signaling_off = 0

    	LON signaling disabled

    .. data:: lon_signaling_on = 1

    	LON signaling enabled

    """

    lon_signaling_off = Enum.YLeaf(0, "lon-signaling-off")

    lon_signaling_on = Enum.YLeaf(1, "lon-signaling-on")


class BundleLoadBalance(Enum):
    """
    BundleLoadBalance (Enum Class)

    Bundle load balance

    .. data:: default = 0

    	Default hash function used

    .. data:: efp_auto = 1

    	Send all traffic for this EFP over an

    	automatically selected member

    .. data:: efp_value = 2

    	Send all traffic for this EFP over the member

    	corresponding to the specified hash function

    .. data:: source_ip = 3

    	Load balance according to source IP address

    .. data:: destination_ip = 4

    	Load balance according to detination IP address

    """

    default = Enum.YLeaf(0, "default")

    efp_auto = Enum.YLeaf(1, "efp-auto")

    efp_value = Enum.YLeaf(2, "efp-value")

    source_ip = Enum.YLeaf(3, "source-ip")

    destination_ip = Enum.YLeaf(4, "destination-ip")


class BundleMaximumActiveLinksMode(Enum):
    """
    BundleMaximumActiveLinksMode (Enum Class)

    Bundle maximum active links mode

    .. data:: default = 0

    	Default

    .. data:: hot_standby = 1

    	Hot standby

    """

    default = Enum.YLeaf(0, "default")

    hot_standby = Enum.YLeaf(1, "hot-standby")


class BundleMinimumBandwidthRange(Enum):
    """
    BundleMinimumBandwidthRange (Enum Class)

    Bundle minimum bandwidth range

    .. data:: none = 0

    	None

    .. data:: kbps = 1

    	kbps

    .. data:: mbps = 2

    	mbps

    .. data:: gbps = 3

    	gbps

    """

    none = Enum.YLeaf(0, "none")

    kbps = Enum.YLeaf(1, "kbps")

    mbps = Enum.YLeaf(2, "mbps")

    gbps = Enum.YLeaf(3, "gbps")


class BundleMode(Enum):
    """
    BundleMode (Enum Class)

    Bundle mode

    .. data:: on = 0

    	On

    .. data:: active = 1

    	Active

    .. data:: passive = 2

    	Passive

    """

    on = Enum.YLeaf(0, "on")

    active = Enum.YLeaf(1, "active")

    passive = Enum.YLeaf(2, "passive")


class BundlePeriod(Enum):
    """
    BundlePeriod (Enum Class)

    Bundle period

    .. data:: true = 1

    	Use the standard LACP short period (1s)

    """

    true = Enum.YLeaf(1, "true")


class BundlePortActivity(Enum):
    """
    BundlePortActivity (Enum Class)

    Bundle port activity

    .. data:: on = 1

    	On

    .. data:: active = 2

    	Active

    .. data:: passive = 3

    	Passive

    .. data:: inherit = 4

    	Inherit

    """

    on = Enum.YLeaf(1, "on")

    active = Enum.YLeaf(2, "active")

    passive = Enum.YLeaf(3, "passive")

    inherit = Enum.YLeaf(4, "inherit")


class ChurnLogging(Enum):
    """
    ChurnLogging (Enum Class)

    Churn logging

    .. data:: actor = 1

    	Logging for actor churn only

    .. data:: partner = 2

    	Logging for partner churn only

    .. data:: both = 3

    	Logging for actor and partner churn

    """

    actor = Enum.YLeaf(1, "actor")

    partner = Enum.YLeaf(2, "partner")

    both = Enum.YLeaf(3, "both")


class MlacpMaximizeParameter(Enum):
    """
    MlacpMaximizeParameter (Enum Class)

    Mlacp maximize parameter

    .. data:: links = 1

    	Maximize the number of operational links

    .. data:: bandwidth = 2

    	Maximize the operational bandwidth

    """

    links = Enum.YLeaf(1, "links")

    bandwidth = Enum.YLeaf(2, "bandwidth")


class MlacpSwitchover(Enum):
    """
    MlacpSwitchover (Enum Class)

    Mlacp switchover

    .. data:: brute_force = 1

    	Brute force shutdown

    .. data:: revertive = 2

    	Revertive behavior

    """

    brute_force = Enum.YLeaf(1, "brute-force")

    revertive = Enum.YLeaf(2, "revertive")


class PeriodShortEnum(Enum):
    """
    PeriodShortEnum (Enum Class)

    Period short enum

    .. data:: true = 1

    	Use the standard LACP short period (1s)

    """

    true = Enum.YLeaf(1, "true")



class Lacp(Entity):
    """
    Link Aggregation Control Protocol commands
    
    .. attribute:: system_mac
    
    	Unique identifier for this system
    	**type**\: str
    
    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
    
    .. attribute:: system_priority
    
    	Priority for this system. Lower value is higher priority
    	**type**\: int
    
    	**range:** 1..65535
    
    	**default value**\: 32768
    
    

    """

    _prefix = 'bundlemgr-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(Lacp, self).__init__()
        self._top_entity = None

        self.yang_name = "lacp"
        self.yang_parent_name = "Cisco-IOS-XR-bundlemgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('system_mac', (YLeaf(YType.str, 'system-mac'), ['str'])),
            ('system_priority', (YLeaf(YType.uint32, 'system-priority'), ['int'])),
        ])
        self.system_mac = None
        self.system_priority = None
        self._segment_path = lambda: "Cisco-IOS-XR-bundlemgr-cfg:lacp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Lacp, ['system_mac', 'system_priority'], name, value)

    def clone_ptr(self):
        self._top_entity = Lacp()
        return self._top_entity

