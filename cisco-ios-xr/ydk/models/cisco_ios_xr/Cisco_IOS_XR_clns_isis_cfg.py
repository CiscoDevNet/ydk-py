""" Cisco_IOS_XR_clns_isis_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR clns\-isis package configuration.

This module contains definitions
for the following management objects\:
  isis\: IS\-IS configuration for all instances

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IsisAdjCheck(Enum):
    """
    IsisAdjCheck (Enum Class)

    Isis adj check

    .. data:: disabled = 0

    	Disabled

    """

    disabled = Enum.YLeaf(0, "disabled")


class IsisAdvTypeExternal(Enum):
    """
    IsisAdvTypeExternal (Enum Class)

    Isis adv type external

    .. data:: external = 1

    	External

    """

    external = Enum.YLeaf(1, "external")


class IsisAdvTypeInterLevel(Enum):
    """
    IsisAdvTypeInterLevel (Enum Class)

    Isis adv type inter level

    .. data:: inter_level = 1

    	InterLevel

    """

    inter_level = Enum.YLeaf(1, "inter-level")


class IsisApplication(Enum):
    """
    IsisApplication (Enum Class)

    Isis application

    .. data:: lfa = 0

    	LFA Application

    """

    lfa = Enum.YLeaf(0, "lfa")


class IsisApplicationAttribute(Enum):
    """
    IsisApplicationAttribute (Enum Class)

    Isis application attribute

    .. data:: srlg = 0

    	SRLG Attribute

    """

    srlg = Enum.YLeaf(0, "srlg")


class IsisApplyWeight(Enum):
    """
    IsisApplyWeight (Enum Class)

    Isis apply weight

    .. data:: ecmp_only = 1

    	Apply weight to ECMP prefixes

    .. data:: ucmp_only = 2

    	Apply weight to UCMP prefixes

    .. data:: ecmp_only_bandwidth = 3

    	Apply weight to ECMP prefixes

    """

    ecmp_only = Enum.YLeaf(1, "ecmp-only")

    ucmp_only = Enum.YLeaf(2, "ucmp-only")

    ecmp_only_bandwidth = Enum.YLeaf(3, "ecmp-only-bandwidth")


class IsisAttachedBit(Enum):
    """
    IsisAttachedBit (Enum Class)

    Isis attached bit

    .. data:: area = 0

    	Computed from the attached areas

    .. data:: on = 1

    	Forced ON

    .. data:: off = 2

    	Forced OFF

    """

    area = Enum.YLeaf(0, "area")

    on = Enum.YLeaf(1, "on")

    off = Enum.YLeaf(2, "off")


class IsisAuthenticationAlgorithm(Enum):
    """
    IsisAuthenticationAlgorithm (Enum Class)

    Isis authentication algorithm

    .. data:: cleartext = 1

    	Cleartext password

    .. data:: hmac_md5 = 2

    	HMAC-MD5 checksum

    .. data:: keychain = 3

    	Key Chain authentication

    """

    cleartext = Enum.YLeaf(1, "cleartext")

    hmac_md5 = Enum.YLeaf(2, "hmac-md5")

    keychain = Enum.YLeaf(3, "keychain")


class IsisAuthenticationFailureMode(Enum):
    """
    IsisAuthenticationFailureMode (Enum Class)

    Isis authentication failure mode

    .. data:: drop = 0

    	Drop non-authenticating PDUs

    .. data:: send_only = 1

    	Accept non-authenticating PDUs

    """

    drop = Enum.YLeaf(0, "drop")

    send_only = Enum.YLeaf(1, "send-only")


class IsisConfigurableLevels(Enum):
    """
    IsisConfigurableLevels (Enum Class)

    Isis configurable levels

    .. data:: level1 = 1

    	Level1

    .. data:: level2 = 2

    	Level2

    .. data:: level1_and2 = 3

    	Both Levels

    """

    level1 = Enum.YLeaf(1, "level1")

    level2 = Enum.YLeaf(2, "level2")

    level1_and2 = Enum.YLeaf(3, "level1-and2")


class IsisEnablePoi(Enum):
    """
    IsisEnablePoi (Enum Class)

    Isis enable poi

    .. data:: enable_poi_off = 0

    	Disable purge originator

    .. data:: enable_poi_on = 1

    	Enable purge originator

    """

    enable_poi_off = Enum.YLeaf(0, "enable-poi-off")

    enable_poi_on = Enum.YLeaf(1, "enable-poi-on")


class IsisHelloPadding(Enum):
    """
    IsisHelloPadding (Enum Class)

    Isis hello padding

    .. data:: never = 0

    	Never pad Hellos

    .. data:: sometimes = 1

    	Pad Hellos during adjacency formation only

    """

    never = Enum.YLeaf(0, "never")

    sometimes = Enum.YLeaf(1, "sometimes")


class IsisInterfaceAfState(Enum):
    """
    IsisInterfaceAfState (Enum Class)

    Isis interface af state

    .. data:: disable = 0

    	Disable

    """

    disable = Enum.YLeaf(0, "disable")


class IsisInterfaceFrrTiebreaker(Enum):
    """
    IsisInterfaceFrrTiebreaker (Enum Class)

    Isis interface frr tiebreaker

    .. data:: node_protecting = 3

    	Prefer node protecting backup path

    .. data:: srlg_disjoint = 6

    	Prefer SRLG disjoint backup path

    """

    node_protecting = Enum.YLeaf(3, "node-protecting")

    srlg_disjoint = Enum.YLeaf(6, "srlg-disjoint")


class IsisInterfaceState(Enum):
    """
    IsisInterfaceState (Enum Class)

    Isis interface state

    .. data:: shutdown = 0

    	Shutdown

    .. data:: suppressed = 1

    	Suppressed

    .. data:: passive = 2

    	Passive

    .. data:: enabled_active = 3

    	EnabledActive

    """

    shutdown = Enum.YLeaf(0, "shutdown")

    suppressed = Enum.YLeaf(1, "suppressed")

    passive = Enum.YLeaf(2, "passive")

    enabled_active = Enum.YLeaf(3, "enabled-active")


class IsisLabelPreference(Enum):
    """
    IsisLabelPreference (Enum Class)

    Isis label preference

    .. data:: ldp = 0

    	Label Distribution Protocol

    .. data:: segment_routing = 1

    	Segment Routing

    """

    ldp = Enum.YLeaf(0, "ldp")

    segment_routing = Enum.YLeaf(1, "segment-routing")


class IsisMetric(Enum):
    """
    IsisMetric (Enum Class)

    Isis metric

    .. data:: internal = 0

    	Internal metric

    .. data:: external = 1

    	External metric

    .. data:: rib_internal = 2

    	RIB Internal metric

    .. data:: rib_external = 3

    	RIB External metric

    """

    internal = Enum.YLeaf(0, "internal")

    external = Enum.YLeaf(1, "external")

    rib_internal = Enum.YLeaf(2, "rib-internal")

    rib_external = Enum.YLeaf(3, "rib-external")


class IsisMetricStyle(Enum):
    """
    IsisMetricStyle (Enum Class)

    Isis metric style

    .. data:: old_metric_style = 0

    	ISO 10589 metric style (old-style)

    .. data:: new_metric_style = 1

    	32-bit metric style (new-style)

    .. data:: both_metric_style = 2

    	Both forms of metric style

    .. data:: old_metric_style_transition = 3

    	Send ISO 10589 metric style but accept both

    .. data:: new_metric_style_transition = 4

    	Send 32-bit metric style but accept both

    """

    old_metric_style = Enum.YLeaf(0, "old-metric-style")

    new_metric_style = Enum.YLeaf(1, "new-metric-style")

    both_metric_style = Enum.YLeaf(2, "both-metric-style")

    old_metric_style_transition = Enum.YLeaf(3, "old-metric-style-transition")

    new_metric_style_transition = Enum.YLeaf(4, "new-metric-style-transition")


class IsisMibAdjacencyChangeBoolean(Enum):
    """
    IsisMibAdjacencyChangeBoolean (Enum Class)

    Isis mib adjacency change boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 17

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(17, "true")


class IsisMibAllBoolean(Enum):
    """
    IsisMibAllBoolean (Enum Class)

    Isis mib all boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 19

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(19, "true")


class IsisMibAreaMismatchBoolean(Enum):
    """
    IsisMibAreaMismatchBoolean (Enum Class)

    Isis mib area mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 12

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(12, "true")


class IsisMibAttemptToExceedMaxSequenceBoolean(Enum):
    """
    IsisMibAttemptToExceedMaxSequenceBoolean (Enum Class)

    Isis mib attempt to exceed max sequence boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 4

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(4, "true")


class IsisMibAuthenticationFailureBoolean(Enum):
    """
    IsisMibAuthenticationFailureBoolean (Enum Class)

    Isis mib authentication failure boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 10

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(10, "true")


class IsisMibAuthenticationTypeFailureBoolean(Enum):
    """
    IsisMibAuthenticationTypeFailureBoolean (Enum Class)

    Isis mib authentication type failure boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 9

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(9, "true")


class IsisMibCorruptedLspDetectedBoolean(Enum):
    """
    IsisMibCorruptedLspDetectedBoolean (Enum Class)

    Isis mib corrupted lsp detected boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 3

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(3, "true")


class IsisMibDatabaseOverFlowBoolean(Enum):
    """
    IsisMibDatabaseOverFlowBoolean (Enum Class)

    Isis mib database over flow boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 1

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(1, "true")


class IsisMibIdLengthMismatchBoolean(Enum):
    """
    IsisMibIdLengthMismatchBoolean (Enum Class)

    Isis mib id length mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 5

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(5, "true")


class IsisMibLspErrorDetectedBoolean(Enum):
    """
    IsisMibLspErrorDetectedBoolean (Enum Class)

    Isis mib lsp error detected boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 18

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(18, "true")


class IsisMibLspTooLargeToPropagateBoolean(Enum):
    """
    IsisMibLspTooLargeToPropagateBoolean (Enum Class)

    Isis mib lsp too large to propagate boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 14

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(14, "true")


class IsisMibManualAddressDropsBoolean(Enum):
    """
    IsisMibManualAddressDropsBoolean (Enum Class)

    Isis mib manual address drops boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 2

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(2, "true")


class IsisMibMaxAreaAddressMismatchBoolean(Enum):
    """
    IsisMibMaxAreaAddressMismatchBoolean (Enum Class)

    Isis mib max area address mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 6

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(6, "true")


class IsisMibOriginatedLspBufferSizeMismatchBoolean(Enum):
    """
    IsisMibOriginatedLspBufferSizeMismatchBoolean (Enum Class)

    Isis mib originated lsp buffer size mismatch

    boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 15

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(15, "true")


class IsisMibOwnLspPurgeBoolean(Enum):
    """
    IsisMibOwnLspPurgeBoolean (Enum Class)

    Isis mib own lsp purge boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 7

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(7, "true")


class IsisMibProtocolsSupportedMismatchBoolean(Enum):
    """
    IsisMibProtocolsSupportedMismatchBoolean (Enum Class)

    Isis mib protocols supported mismatch boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 16

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(16, "true")


class IsisMibRejectedAdjacencyBoolean(Enum):
    """
    IsisMibRejectedAdjacencyBoolean (Enum Class)

    Isis mib rejected adjacency boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 13

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(13, "true")


class IsisMibSequenceNumberSkipBoolean(Enum):
    """
    IsisMibSequenceNumberSkipBoolean (Enum Class)

    Isis mib sequence number skip boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 8

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(8, "true")


class IsisMibVersionSkewBoolean(Enum):
    """
    IsisMibVersionSkewBoolean (Enum Class)

    Isis mib version skew boolean

    .. data:: false = 0

    	Disable

    .. data:: true = 11

    	Enable

    """

    false = Enum.YLeaf(0, "false")

    true = Enum.YLeaf(11, "true")


class IsisMicroLoopAvoidance(Enum):
    """
    IsisMicroLoopAvoidance (Enum Class)

    Isis micro loop avoidance

    .. data:: not_set = 0

    	No Avoidance type set

    .. data:: micro_loop_avoidance_all = 1

    	Provide mirco loop avoidance for all prefixes

    .. data:: micro_loop_avoidance_protected = 2

    	Provide mirco loop avoidance only for protected

    	prefixes

    .. data:: micro_loop_avoidance_segement_routing = 3

    	Provide segment-routing mirco loop avoidance

    """

    not_set = Enum.YLeaf(0, "not-set")

    micro_loop_avoidance_all = Enum.YLeaf(1, "micro-loop-avoidance-all")

    micro_loop_avoidance_protected = Enum.YLeaf(2, "micro-loop-avoidance-protected")

    micro_loop_avoidance_segement_routing = Enum.YLeaf(3, "micro-loop-avoidance-segement-routing")


class IsisNsfFlavor(Enum):
    """
    IsisNsfFlavor (Enum Class)

    Isis nsf flavor

    .. data:: cisco_proprietary_nsf = 1

    	Cisco proprietary NSF

    .. data:: ietf_standard_nsf = 2

    	IETF standard NSF

    """

    cisco_proprietary_nsf = Enum.YLeaf(1, "cisco-proprietary-nsf")

    ietf_standard_nsf = Enum.YLeaf(2, "ietf-standard-nsf")


class IsisOverloadBitMode(Enum):
    """
    IsisOverloadBitMode (Enum Class)

    Isis overload bit mode

    .. data:: permanently_set = 1

    	Set always

    .. data:: startup_period = 2

    	Set during the startup period

    .. data:: wait_for_bgp = 3

    	Set until BGP comverges

    """

    permanently_set = Enum.YLeaf(1, "permanently-set")

    startup_period = Enum.YLeaf(2, "startup-period")

    wait_for_bgp = Enum.YLeaf(3, "wait-for-bgp")


class IsisPrefixPriority(Enum):
    """
    IsisPrefixPriority (Enum Class)

    Isis prefix priority

    .. data:: critical_priority = 0

    	Critical prefix priority

    .. data:: high_priority = 1

    	High prefix priority

    .. data:: medium_priority = 2

    	Medium prefix priority

    """

    critical_priority = Enum.YLeaf(0, "critical-priority")

    high_priority = Enum.YLeaf(1, "high-priority")

    medium_priority = Enum.YLeaf(2, "medium-priority")


class IsisRedistProto(Enum):
    """
    IsisRedistProto (Enum Class)

    Isis redist proto

    .. data:: connected = 0

    	Connected

    .. data:: static = 1

    	Static

    .. data:: ospf = 2

    	OSPF

    .. data:: bgp = 3

    	BGP

    .. data:: isis = 4

    	ISIS

    .. data:: ospfv3 = 5

    	OSPFv3

    .. data:: rip = 6

    	RIP

    .. data:: eigrp = 7

    	EIGRP

    .. data:: subscriber = 8

    	Subscriber

    .. data:: application = 9

    	Application

    .. data:: mobile = 10

    	Mobile

    """

    connected = Enum.YLeaf(0, "connected")

    static = Enum.YLeaf(1, "static")

    ospf = Enum.YLeaf(2, "ospf")

    bgp = Enum.YLeaf(3, "bgp")

    isis = Enum.YLeaf(4, "isis")

    ospfv3 = Enum.YLeaf(5, "ospfv3")

    rip = Enum.YLeaf(6, "rip")

    eigrp = Enum.YLeaf(7, "eigrp")

    subscriber = Enum.YLeaf(8, "subscriber")

    application = Enum.YLeaf(9, "application")

    mobile = Enum.YLeaf(10, "mobile")


class IsisRemoteLfa(Enum):
    """
    IsisRemoteLfa (Enum Class)

    Isis remote lfa

    .. data:: remote_lfa_none = 0

    	No remote LFA option set

    .. data:: remote_lfa_tunnel_ldp = 1

    	Construct remote LFA tunnel using MPLS LDP

    """

    remote_lfa_none = Enum.YLeaf(0, "remote-lfa-none")

    remote_lfa_tunnel_ldp = Enum.YLeaf(1, "remote-lfa-tunnel-ldp")


class IsisSnpAuth(Enum):
    """
    IsisSnpAuth (Enum Class)

    Isis snp auth

    .. data:: send_only = 0

    	Authenticate SNP send only

    .. data:: full = 1

    	Authenticate SNP send and recv

    """

    send_only = Enum.YLeaf(0, "send-only")

    full = Enum.YLeaf(1, "full")


class IsisTracingMode(Enum):
    """
    IsisTracingMode (Enum Class)

    Isis tracing mode

    .. data:: off = 0

    	No tracing

    .. data:: basic = 1

    	Basic tracing (less overhead)

    .. data:: enhanced = 2

    	Enhanced tracing (more overhead)

    """

    off = Enum.YLeaf(0, "off")

    basic = Enum.YLeaf(1, "basic")

    enhanced = Enum.YLeaf(2, "enhanced")


class IsisexplicitNullFlag(Enum):
    """
    IsisexplicitNullFlag (Enum Class)

    Isisexplicit null flag

    .. data:: disable = 0

    	Disable EXPLICITNULL

    .. data:: enable = 1

    	Enable EXPLICITNULL

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class Isisfrr(Enum):
    """
    Isisfrr (Enum Class)

    Isisfrr

    .. data:: per_link = 1

    	Prefix independent per-link computation

    .. data:: per_prefix = 2

    	Prefix dependent computation

    """

    per_link = Enum.YLeaf(1, "per-link")

    per_prefix = Enum.YLeaf(2, "per-prefix")


class IsisfrrLoadSharing(Enum):
    """
    IsisfrrLoadSharing (Enum Class)

    Isisfrr load sharing

    .. data:: disable = 1

    	Disable load sharing of prefixes across

    	multiple backups

    """

    disable = Enum.YLeaf(1, "disable")


class IsisfrrSrlgProtection(Enum):
    """
    IsisfrrSrlgProtection (Enum Class)

    Isisfrr srlg protection

    .. data:: local = 0

    	SRLG Attribute

    .. data:: weighted_global = 1

    	SRLG Attribute

    """

    local = Enum.YLeaf(0, "local")

    weighted_global = Enum.YLeaf(1, "weighted-global")


class IsisfrrTiebreaker(Enum):
    """
    IsisfrrTiebreaker (Enum Class)

    Isisfrr tiebreaker

    .. data:: downstream = 0

    	Prefer backup path via downstream node

    .. data:: lc_disjoint = 1

    	Prefer line card disjoint backup path

    .. data:: lowest_backup_metric = 2

    	Prefer backup path with lowest total metric

    .. data:: node_protecting = 3

    	Prefer node protecting backup path

    .. data:: primary_path = 4

    	Prefer backup path from ECMP set

    .. data:: secondary_path = 5

    	Prefer non-ECMP backup path

    .. data:: srlg_disjoint = 6

    	Prefer SRLG disjoint backup path

    """

    downstream = Enum.YLeaf(0, "downstream")

    lc_disjoint = Enum.YLeaf(1, "lc-disjoint")

    lowest_backup_metric = Enum.YLeaf(2, "lowest-backup-metric")

    node_protecting = Enum.YLeaf(3, "node-protecting")

    primary_path = Enum.YLeaf(4, "primary-path")

    secondary_path = Enum.YLeaf(5, "secondary-path")

    srlg_disjoint = Enum.YLeaf(6, "srlg-disjoint")


class IsisispfState(Enum):
    """
    IsisispfState (Enum Class)

    Isisispf state

    .. data:: enabled = 1

    	Enabled

    """

    enabled = Enum.YLeaf(1, "enabled")


class IsisphpFlag(Enum):
    """
    IsisphpFlag (Enum Class)

    Isisphp flag

    .. data:: enable = 0

    	Enable PHP

    .. data:: disable = 1

    	Disable PHP

    """

    enable = Enum.YLeaf(0, "enable")

    disable = Enum.YLeaf(1, "disable")


class Isissid1(Enum):
    """
    Isissid1 (Enum Class)

    Isissid1

    .. data:: index = 1

    	SID as an index

    .. data:: absolute = 2

    	SID as an absolute label

    """

    index = Enum.YLeaf(1, "index")

    absolute = Enum.YLeaf(2, "absolute")


class IsissidProtected(Enum):
    """
    IsissidProtected (Enum Class)

    Isissid protected

    .. data:: disable = 0

    	Not protected

    .. data:: enable = 1

    	Protected

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class NflagClear(Enum):
    """
    NflagClear (Enum Class)

    Nflag clear

    .. data:: disable = 0

    	Disable N-flag-clear

    .. data:: enable = 1

    	Enable N-flag-clear

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")



class Isis(Entity):
    """
    IS\-IS configuration for all instances
    
    .. attribute:: instances
    
    	IS\-IS instance configuration
    	**type**\:  :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances>`
    
    

    """

    _prefix = 'clns-isis-cfg'
    _revision = '2018-06-14'

    def __init__(self):
        super(Isis, self).__init__()
        self._top_entity = None

        self.yang_name = "isis"
        self.yang_parent_name = "Cisco-IOS-XR-clns-isis-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("instances", ("instances", Isis.Instances))])
        self._leafs = OrderedDict()

        self.instances = Isis.Instances()
        self.instances.parent = self
        self._children_name_map["instances"] = "instances"
        self._segment_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Isis, [], name, value)


    class Instances(Entity):
        """
        IS\-IS instance configuration
        
        .. attribute:: instance
        
        	Configuration for a single IS\-IS instance
        	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance>`
        
        

        """

        _prefix = 'clns-isis-cfg'
        _revision = '2018-06-14'

        def __init__(self):
            super(Isis.Instances, self).__init__()

            self.yang_name = "instances"
            self.yang_parent_name = "isis"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("instance", ("instance", Isis.Instances.Instance))])
            self._leafs = OrderedDict()

            self.instance = YList(self)
            self._segment_path = lambda: "instances"
            self._absolute_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Isis.Instances, [], name, value)


        class Instance(Entity):
            """
            Configuration for a single IS\-IS instance
            
            .. attribute:: instance_name  (key)
            
            	Instance identifier
            	**type**\: str
            
            	**length:** 1..36
            
            .. attribute:: srgb
            
            	Segment Routing Global Block configuration
            	**type**\:  :py:class:`Srgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Srgb>`
            
            	**presence node**\: True
            
            .. attribute:: lsp_generation_intervals
            
            	LSP generation\-interval configuration
            	**type**\:  :py:class:`LspGenerationIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals>`
            
            .. attribute:: lsp_arrival_times
            
            	LSP arrival time configuration
            	**type**\:  :py:class:`LspArrivalTimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes>`
            
            .. attribute:: trace_buffer_size
            
            	Trace buffer size configuration
            	**type**\:  :py:class:`TraceBufferSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.TraceBufferSize>`
            
            .. attribute:: max_link_metrics
            
            	Max Link Metric configuration
            	**type**\:  :py:class:`MaxLinkMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics>`
            
            .. attribute:: adjacency_stagger
            
            	Stagger ISIS adjacency bring up
            	**type**\:  :py:class:`AdjacencyStagger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.AdjacencyStagger>`
            
            	**presence node**\: True
            
            .. attribute:: afs
            
            	Per\-address\-family configuration
            	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs>`
            
            .. attribute:: lsp_refresh_intervals
            
            	LSP refresh\-interval configuration
            	**type**\:  :py:class:`LspRefreshIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals>`
            
            .. attribute:: distribute
            
            	Distribute link\-state configuration
            	**type**\:  :py:class:`Distribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Distribute>`
            
            	**presence node**\: True
            
            .. attribute:: flex_algos
            
            	Flex\-Algo Table
            	**type**\:  :py:class:`FlexAlgos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.FlexAlgos>`
            
            .. attribute:: affinity_mappings
            
            	Affinity Mapping Table
            	**type**\:  :py:class:`AffinityMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.AffinityMappings>`
            
            .. attribute:: lsp_accept_passwords
            
            	LSP/SNP accept password configuration
            	**type**\:  :py:class:`LspAcceptPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords>`
            
            .. attribute:: lsp_mtus
            
            	LSP MTU configuration
            	**type**\:  :py:class:`LspMtus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus>`
            
            .. attribute:: srlg_table
            
            	SRLG configuration
            	**type**\:  :py:class:`SrlgTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.SrlgTable>`
            
            .. attribute:: nsf
            
            	IS\-IS NSF configuration
            	**type**\:  :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nsf>`
            
            .. attribute:: link_groups
            
            	Link Group
            	**type**\:  :py:class:`LinkGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups>`
            
            .. attribute:: lsp_check_intervals
            
            	LSP checksum check interval configuration
            	**type**\:  :py:class:`LspCheckIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals>`
            
            .. attribute:: lsp_passwords
            
            	LSP/SNP password configuration
            	**type**\:  :py:class:`LspPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords>`
            
            .. attribute:: nets
            
            	NET configuration
            	**type**\:  :py:class:`Nets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets>`
            
            .. attribute:: lsp_lifetimes
            
            	LSP lifetime configuration
            	**type**\:  :py:class:`LspLifetimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes>`
            
            .. attribute:: overload_bits
            
            	LSP overload\-bit configuration
            	**type**\:  :py:class:`OverloadBits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits>`
            
            .. attribute:: interfaces
            
            	Per\-interface configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces>`
            
            .. attribute:: running
            
            	Flag to indicate that instance should be running.  This must be the first object created when an IS\-IS instance is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS instance will exit
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_adjacency_changes
            
            	Log changes in adjacency state
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ignore_lsp_errors
            
            	If TRUE, LSPs recieved with bad checksums will result in the purging of that LSP from the LSP DB. If FALSE or not set, the received LSP will just be ignored
            	**type**\: bool
            
            .. attribute:: is_type
            
            	IS type of the IS\-IS process
            	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
            
            	**default value**\: level1-and2
            
            .. attribute:: tracing_mode
            
            	Tracing mode configuration
            	**type**\:  :py:class:`IsisTracingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisTracingMode>`
            
            	**default value**\: basic
            
            .. attribute:: vrf_context
            
            	VRF context for ISIS process
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: instance_id
            
            	Instance ID of the IS\-IS process
            	**type**\: int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: dynamic_host_name
            
            	If TRUE, dynamic hostname resolution is disabled, and system IDs will always be displayed by show and debug output
            	**type**\: bool
            
            .. attribute:: nsr
            
            	IS\-IS NSR configuration
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_pdu_drops
            
            	Log PDU drops
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2018-06-14'

            def __init__(self):
                super(Isis.Instances.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "instances"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['instance_name']
                self._child_classes = OrderedDict([("srgb", ("srgb", Isis.Instances.Instance.Srgb)), ("lsp-generation-intervals", ("lsp_generation_intervals", Isis.Instances.Instance.LspGenerationIntervals)), ("lsp-arrival-times", ("lsp_arrival_times", Isis.Instances.Instance.LspArrivalTimes)), ("trace-buffer-size", ("trace_buffer_size", Isis.Instances.Instance.TraceBufferSize)), ("max-link-metrics", ("max_link_metrics", Isis.Instances.Instance.MaxLinkMetrics)), ("adjacency-stagger", ("adjacency_stagger", Isis.Instances.Instance.AdjacencyStagger)), ("afs", ("afs", Isis.Instances.Instance.Afs)), ("lsp-refresh-intervals", ("lsp_refresh_intervals", Isis.Instances.Instance.LspRefreshIntervals)), ("distribute", ("distribute", Isis.Instances.Instance.Distribute)), ("flex-algos", ("flex_algos", Isis.Instances.Instance.FlexAlgos)), ("affinity-mappings", ("affinity_mappings", Isis.Instances.Instance.AffinityMappings)), ("lsp-accept-passwords", ("lsp_accept_passwords", Isis.Instances.Instance.LspAcceptPasswords)), ("lsp-mtus", ("lsp_mtus", Isis.Instances.Instance.LspMtus)), ("srlg-table", ("srlg_table", Isis.Instances.Instance.SrlgTable)), ("nsf", ("nsf", Isis.Instances.Instance.Nsf)), ("link-groups", ("link_groups", Isis.Instances.Instance.LinkGroups)), ("lsp-check-intervals", ("lsp_check_intervals", Isis.Instances.Instance.LspCheckIntervals)), ("lsp-passwords", ("lsp_passwords", Isis.Instances.Instance.LspPasswords)), ("nets", ("nets", Isis.Instances.Instance.Nets)), ("lsp-lifetimes", ("lsp_lifetimes", Isis.Instances.Instance.LspLifetimes)), ("overload-bits", ("overload_bits", Isis.Instances.Instance.OverloadBits)), ("interfaces", ("interfaces", Isis.Instances.Instance.Interfaces))])
                self._leafs = OrderedDict([
                    ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                    ('running', (YLeaf(YType.empty, 'running'), ['Empty'])),
                    ('log_adjacency_changes', (YLeaf(YType.empty, 'log-adjacency-changes'), ['Empty'])),
                    ('ignore_lsp_errors', (YLeaf(YType.boolean, 'ignore-lsp-errors'), ['bool'])),
                    ('is_type', (YLeaf(YType.enumeration, 'is-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                    ('tracing_mode', (YLeaf(YType.enumeration, 'tracing-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisTracingMode', '')])),
                    ('vrf_context', (YLeaf(YType.str, 'vrf-context'), ['str'])),
                    ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                    ('dynamic_host_name', (YLeaf(YType.boolean, 'dynamic-host-name'), ['bool'])),
                    ('nsr', (YLeaf(YType.empty, 'nsr'), ['Empty'])),
                    ('log_pdu_drops', (YLeaf(YType.empty, 'log-pdu-drops'), ['Empty'])),
                ])
                self.instance_name = None
                self.running = None
                self.log_adjacency_changes = None
                self.ignore_lsp_errors = None
                self.is_type = None
                self.tracing_mode = None
                self.vrf_context = None
                self.instance_id = None
                self.dynamic_host_name = None
                self.nsr = None
                self.log_pdu_drops = None

                self.srgb = None
                self._children_name_map["srgb"] = "srgb"

                self.lsp_generation_intervals = Isis.Instances.Instance.LspGenerationIntervals()
                self.lsp_generation_intervals.parent = self
                self._children_name_map["lsp_generation_intervals"] = "lsp-generation-intervals"

                self.lsp_arrival_times = Isis.Instances.Instance.LspArrivalTimes()
                self.lsp_arrival_times.parent = self
                self._children_name_map["lsp_arrival_times"] = "lsp-arrival-times"

                self.trace_buffer_size = Isis.Instances.Instance.TraceBufferSize()
                self.trace_buffer_size.parent = self
                self._children_name_map["trace_buffer_size"] = "trace-buffer-size"

                self.max_link_metrics = Isis.Instances.Instance.MaxLinkMetrics()
                self.max_link_metrics.parent = self
                self._children_name_map["max_link_metrics"] = "max-link-metrics"

                self.adjacency_stagger = None
                self._children_name_map["adjacency_stagger"] = "adjacency-stagger"

                self.afs = Isis.Instances.Instance.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"

                self.lsp_refresh_intervals = Isis.Instances.Instance.LspRefreshIntervals()
                self.lsp_refresh_intervals.parent = self
                self._children_name_map["lsp_refresh_intervals"] = "lsp-refresh-intervals"

                self.distribute = None
                self._children_name_map["distribute"] = "distribute"

                self.flex_algos = Isis.Instances.Instance.FlexAlgos()
                self.flex_algos.parent = self
                self._children_name_map["flex_algos"] = "flex-algos"

                self.affinity_mappings = Isis.Instances.Instance.AffinityMappings()
                self.affinity_mappings.parent = self
                self._children_name_map["affinity_mappings"] = "affinity-mappings"

                self.lsp_accept_passwords = Isis.Instances.Instance.LspAcceptPasswords()
                self.lsp_accept_passwords.parent = self
                self._children_name_map["lsp_accept_passwords"] = "lsp-accept-passwords"

                self.lsp_mtus = Isis.Instances.Instance.LspMtus()
                self.lsp_mtus.parent = self
                self._children_name_map["lsp_mtus"] = "lsp-mtus"

                self.srlg_table = Isis.Instances.Instance.SrlgTable()
                self.srlg_table.parent = self
                self._children_name_map["srlg_table"] = "srlg-table"

                self.nsf = Isis.Instances.Instance.Nsf()
                self.nsf.parent = self
                self._children_name_map["nsf"] = "nsf"

                self.link_groups = Isis.Instances.Instance.LinkGroups()
                self.link_groups.parent = self
                self._children_name_map["link_groups"] = "link-groups"

                self.lsp_check_intervals = Isis.Instances.Instance.LspCheckIntervals()
                self.lsp_check_intervals.parent = self
                self._children_name_map["lsp_check_intervals"] = "lsp-check-intervals"

                self.lsp_passwords = Isis.Instances.Instance.LspPasswords()
                self.lsp_passwords.parent = self
                self._children_name_map["lsp_passwords"] = "lsp-passwords"

                self.nets = Isis.Instances.Instance.Nets()
                self.nets.parent = self
                self._children_name_map["nets"] = "nets"

                self.lsp_lifetimes = Isis.Instances.Instance.LspLifetimes()
                self.lsp_lifetimes.parent = self
                self._children_name_map["lsp_lifetimes"] = "lsp-lifetimes"

                self.overload_bits = Isis.Instances.Instance.OverloadBits()
                self.overload_bits.parent = self
                self._children_name_map["overload_bits"] = "overload-bits"

                self.interfaces = Isis.Instances.Instance.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "instance" + "[instance-name='" + str(self.instance_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis/instances/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Isis.Instances.Instance, ['instance_name', 'running', 'log_adjacency_changes', 'ignore_lsp_errors', 'is_type', 'tracing_mode', 'vrf_context', 'instance_id', 'dynamic_host_name', 'nsr', 'log_pdu_drops'], name, value)


            class Srgb(Entity):
                """
                Segment Routing Global Block configuration
                
                .. attribute:: lower_bound
                
                	The lower bound of the SRGB
                	**type**\: int
                
                	**range:** 16000..1048574
                
                	**mandatory**\: True
                
                .. attribute:: upper_bound
                
                	The upper bound of the SRGB
                	**type**\: int
                
                	**range:** 16001..1048575
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.Srgb, self).__init__()

                    self.yang_name = "srgb"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('lower_bound', (YLeaf(YType.uint32, 'lower-bound'), ['int'])),
                        ('upper_bound', (YLeaf(YType.uint32, 'upper-bound'), ['int'])),
                    ])
                    self.lower_bound = None
                    self.upper_bound = None
                    self._segment_path = lambda: "srgb"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Srgb, ['lower_bound', 'upper_bound'], name, value)


            class LspGenerationIntervals(Entity):
                """
                LSP generation\-interval configuration
                
                .. attribute:: lsp_generation_interval
                
                	LSP generation scheduling parameters
                	**type**\: list of  		 :py:class:`LspGenerationInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspGenerationIntervals, self).__init__()

                    self.yang_name = "lsp-generation-intervals"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-generation-interval", ("lsp_generation_interval", Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval))])
                    self._leafs = OrderedDict()

                    self.lsp_generation_interval = YList(self)
                    self._segment_path = lambda: "lsp-generation-intervals"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspGenerationIntervals, [], name, value)


                class LspGenerationInterval(Entity):
                    """
                    LSP generation scheduling parameters
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum wait before generating local LSP in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: initial_wait
                    
                    	Initial wait before generating local LSP in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary wait before generating local LSP in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval, self).__init__()

                        self.yang_name = "lsp-generation-interval"
                        self.yang_parent_name = "lsp-generation-intervals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('maximum_wait', (YLeaf(YType.uint32, 'maximum-wait'), ['int'])),
                            ('initial_wait', (YLeaf(YType.uint32, 'initial-wait'), ['int'])),
                            ('secondary_wait', (YLeaf(YType.uint32, 'secondary-wait'), ['int'])),
                        ])
                        self.level = None
                        self.maximum_wait = None
                        self.initial_wait = None
                        self.secondary_wait = None
                        self._segment_path = lambda: "lsp-generation-interval" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval, ['level', 'maximum_wait', 'initial_wait', 'secondary_wait'], name, value)


            class LspArrivalTimes(Entity):
                """
                LSP arrival time configuration
                
                .. attribute:: lsp_arrival_time
                
                	Minimum LSP arrival time
                	**type**\: list of  		 :py:class:`LspArrivalTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspArrivalTimes, self).__init__()

                    self.yang_name = "lsp-arrival-times"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-arrival-time", ("lsp_arrival_time", Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime))])
                    self._leafs = OrderedDict()

                    self.lsp_arrival_time = YList(self)
                    self._segment_path = lambda: "lsp-arrival-times"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspArrivalTimes, [], name, value)


                class LspArrivalTime(Entity):
                    """
                    Minimum LSP arrival time
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum delay expected to take since last LSPin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: initial_wait
                    
                    	Initial delay expected to take since last LSPin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary delay expected to take since last LSPin milliseconds
                    	**type**\: int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime, self).__init__()

                        self.yang_name = "lsp-arrival-time"
                        self.yang_parent_name = "lsp-arrival-times"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('maximum_wait', (YLeaf(YType.uint32, 'maximum-wait'), ['int'])),
                            ('initial_wait', (YLeaf(YType.uint32, 'initial-wait'), ['int'])),
                            ('secondary_wait', (YLeaf(YType.uint32, 'secondary-wait'), ['int'])),
                        ])
                        self.level = None
                        self.maximum_wait = None
                        self.initial_wait = None
                        self.secondary_wait = None
                        self._segment_path = lambda: "lsp-arrival-time" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime, ['level', 'maximum_wait', 'initial_wait', 'secondary_wait'], name, value)


            class TraceBufferSize(Entity):
                """
                Trace buffer size configuration
                
                .. attribute:: detailed
                
                	Buffer size for detailed traces
                	**type**\: int
                
                	**range:** 1..1000000
                
                .. attribute:: standard
                
                	Buffer size for standard traces
                	**type**\: int
                
                	**range:** 1..1000000
                
                .. attribute:: severe
                
                	Buffer size for severe trace
                	**type**\: int
                
                	**range:** 1..1000000
                
                .. attribute:: hello
                
                	Buffer size for hello trace
                	**type**\: int
                
                	**range:** 1..1000000
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.TraceBufferSize, self).__init__()

                    self.yang_name = "trace-buffer-size"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('detailed', (YLeaf(YType.uint32, 'detailed'), ['int'])),
                        ('standard', (YLeaf(YType.uint32, 'standard'), ['int'])),
                        ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                        ('hello', (YLeaf(YType.uint32, 'hello'), ['int'])),
                    ])
                    self.detailed = None
                    self.standard = None
                    self.severe = None
                    self.hello = None
                    self._segment_path = lambda: "trace-buffer-size"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.TraceBufferSize, ['detailed', 'standard', 'severe', 'hello'], name, value)


            class MaxLinkMetrics(Entity):
                """
                Max Link Metric configuration
                
                .. attribute:: max_link_metric
                
                	Max Link Metric
                	**type**\: list of  		 :py:class:`MaxLinkMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.MaxLinkMetrics, self).__init__()

                    self.yang_name = "max-link-metrics"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("max-link-metric", ("max_link_metric", Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric))])
                    self._leafs = OrderedDict()

                    self.max_link_metric = YList(self)
                    self._segment_path = lambda: "max-link-metrics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.MaxLinkMetrics, [], name, value)


                class MaxLinkMetric(Entity):
                    """
                    Max Link Metric
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric, self).__init__()

                        self.yang_name = "max-link-metric"
                        self.yang_parent_name = "max-link-metrics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                        ])
                        self.level = None
                        self._segment_path = lambda: "max-link-metric" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric, ['level'], name, value)


            class AdjacencyStagger(Entity):
                """
                Stagger ISIS adjacency bring up
                
                .. attribute:: initial_nbr
                
                	Adjacency Stagger\: Initial number of neighbors to bring up per area
                	**type**\: int
                
                	**range:** 2..65000
                
                	**default value**\: 2
                
                .. attribute:: max_nbr
                
                	Adjacency Stagger\: Subsequent simultaneous number of neighbors to bring up
                	**type**\: int
                
                	**range:** 2..65000
                
                	**default value**\: 64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.AdjacencyStagger, self).__init__()

                    self.yang_name = "adjacency-stagger"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('initial_nbr', (YLeaf(YType.uint32, 'initial-nbr'), ['int'])),
                        ('max_nbr', (YLeaf(YType.uint32, 'max-nbr'), ['int'])),
                    ])
                    self.initial_nbr = None
                    self.max_nbr = None
                    self._segment_path = lambda: "adjacency-stagger"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.AdjacencyStagger, ['initial_nbr', 'max_nbr'], name, value)


            class Afs(Entity):
                """
                Per\-address\-family configuration
                
                .. attribute:: af
                
                	Configuration for an IS\-IS address\-family. If a named (non\-default) topology is being created it must be multicast
                	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("af", ("af", Isis.Instances.Instance.Afs.Af))])
                    self._leafs = OrderedDict()

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Afs, [], name, value)


                class Af(Entity):
                    """
                    Configuration for an IS\-IS address\-family. If
                    a named (non\-default) topology is being
                    created it must be multicast.
                    
                    .. attribute:: af_name  (key)
                    
                    	Address family
                    	**type**\:  :py:class:`IsisAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamily>`
                    
                    .. attribute:: saf_name  (key)
                    
                    	Sub address family
                    	**type**\:  :py:class:`IsisSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamily>`
                    
                    .. attribute:: af_data
                    
                    	Data container
                    	**type**\:  :py:class:`AfData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: topology_name
                    
                    	keys\: topology\-name
                    	**type**\: list of  		 :py:class:`TopologyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['af_name','saf_name']
                        self._child_classes = OrderedDict([("af-data", ("af_data", Isis.Instances.Instance.Afs.Af.AfData)), ("topology-name", ("topology_name", Isis.Instances.Instance.Afs.Af.TopologyName))])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamily', '')])),
                            ('saf_name', (YLeaf(YType.enumeration, 'saf-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamily', '')])),
                        ])
                        self.af_name = None
                        self.saf_name = None

                        self.af_data = None
                        self._children_name_map["af_data"] = "af-data"

                        self.topology_name = YList(self)
                        self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']" + "[saf-name='" + str(self.saf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.Afs.Af, ['af_name', 'saf_name'], name, value)


                    class AfData(Entity):
                        """
                        Data container.
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\:  :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting>`
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\:  :py:class:`MetricStyles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\:  :py:class:`FrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable>`
                        
                        .. attribute:: router_id
                        
                        	Stable IP address for system. Will only be applied for the unicast sub\-address\-family
                        	**type**\:  :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.RouterId>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\:  :py:class:`SpfPrefixPriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\:  :py:class:`SummaryPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\:  :py:class:`MicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance>`
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\:  :py:class:`Ucmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\:  :py:class:`MaxRedistPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\:  :py:class:`Propagations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\:  :py:class:`Redistributions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions>`
                        
                        .. attribute:: application_tables
                        
                        	Advertise application specific values
                        	**type**\:  :py:class:`ApplicationTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\:  :py:class:`SpfPeriodicIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals>`
                        
                        .. attribute:: distribute_list_in
                        
                        	Filter routes sent to the RIB
                        	**type**\:  :py:class:`DistributeListIn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\:  :py:class:`SpfIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\:  :py:class:`MonitorConvergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence>`
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\:  :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\:  :py:class:`AdminDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances>`
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\:  :py:class:`Ispf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:  :py:class:`MplsLdpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\: int
                        
                        	**range:** 1..64
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\: int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\:  :py:class:`IsisAdjCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheck>`
                        
                        .. attribute:: advertise_link_attributes
                        
                        	If TRUE, advertise additional link attributes in our LSP
                        	**type**\: bool
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\:  :py:class:`IsisApplyWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeight>`
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 115
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\: bool
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\:  :py:class:`IsisAttachedBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit>`
                        
                        	**default value**\: area
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\: bool
                        
                        .. attribute:: manual_adj_sids
                        
                        	Manual Adjacecy SID configuration
                        	**type**\:  :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\:  :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\:  :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Afs.Af.AfData, self).__init__()

                            self.yang_name = "af-data"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("segment-routing", ("segment_routing", Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting)), ("metric-styles", ("metric_styles", Isis.Instances.Instance.Afs.Af.AfData.MetricStyles)), ("frr-table", ("frr_table", Isis.Instances.Instance.Afs.Af.AfData.FrrTable)), ("router-id", ("router_id", Isis.Instances.Instance.Afs.Af.AfData.RouterId)), ("spf-prefix-priorities", ("spf_prefix_priorities", Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities)), ("summary-prefixes", ("summary_prefixes", Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes)), ("micro-loop-avoidance", ("micro_loop_avoidance", Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance)), ("ucmp", ("ucmp", Isis.Instances.Instance.Afs.Af.AfData.Ucmp)), ("max-redist-prefixes", ("max_redist_prefixes", Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes)), ("propagations", ("propagations", Isis.Instances.Instance.Afs.Af.AfData.Propagations)), ("redistributions", ("redistributions", Isis.Instances.Instance.Afs.Af.AfData.Redistributions)), ("application-tables", ("application_tables", Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables)), ("spf-periodic-intervals", ("spf_periodic_intervals", Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals)), ("distribute-list-in", ("distribute_list_in", Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn)), ("spf-intervals", ("spf_intervals", Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals)), ("monitor-convergence", ("monitor_convergence", Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence)), ("default-information", ("default_information", Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation)), ("admin-distances", ("admin_distances", Isis.Instances.Instance.Afs.Af.AfData.AdminDistances)), ("ispf", ("ispf", Isis.Instances.Instance.Afs.Af.AfData.Ispf)), ("mpls-ldp-global", ("mpls_ldp_global", Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal)), ("mpls", ("mpls", Isis.Instances.Instance.Afs.Af.AfData.Mpls)), ("manual-adj-sids", ("manual_adj_sids", Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids)), ("metrics", ("metrics", Isis.Instances.Instance.Afs.Af.AfData.Metrics)), ("weights", ("weights", Isis.Instances.Instance.Afs.Af.AfData.Weights))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                                ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                ('single_topology', (YLeaf(YType.empty, 'single-topology'), ['Empty'])),
                                ('adjacency_check', (YLeaf(YType.enumeration, 'adjacency-check'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheck', '')])),
                                ('advertise_link_attributes', (YLeaf(YType.boolean, 'advertise-link-attributes'), ['bool'])),
                                ('apply_weight', (YLeaf(YType.enumeration, 'apply-weight'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeight', '')])),
                                ('default_admin_distance', (YLeaf(YType.uint32, 'default-admin-distance'), ['int'])),
                                ('advertise_passive_only', (YLeaf(YType.empty, 'advertise-passive-only'), ['Empty'])),
                                ('ignore_attached_bit', (YLeaf(YType.boolean, 'ignore-attached-bit'), ['bool'])),
                                ('attached_bit', (YLeaf(YType.enumeration, 'attached-bit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBit', '')])),
                                ('route_source_first_hop', (YLeaf(YType.boolean, 'route-source-first-hop'), ['bool'])),
                            ])
                            self.maximum_paths = None
                            self.topology_id = None
                            self.single_topology = None
                            self.adjacency_check = None
                            self.advertise_link_attributes = None
                            self.apply_weight = None
                            self.default_admin_distance = None
                            self.advertise_passive_only = None
                            self.ignore_attached_bit = None
                            self.attached_bit = None
                            self.route_source_first_hop = None

                            self.segment_routing = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting()
                            self.segment_routing.parent = self
                            self._children_name_map["segment_routing"] = "segment-routing"

                            self.metric_styles = Isis.Instances.Instance.Afs.Af.AfData.MetricStyles()
                            self.metric_styles.parent = self
                            self._children_name_map["metric_styles"] = "metric-styles"

                            self.frr_table = Isis.Instances.Instance.Afs.Af.AfData.FrrTable()
                            self.frr_table.parent = self
                            self._children_name_map["frr_table"] = "frr-table"

                            self.router_id = Isis.Instances.Instance.Afs.Af.AfData.RouterId()
                            self.router_id.parent = self
                            self._children_name_map["router_id"] = "router-id"

                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self._children_name_map["spf_prefix_priorities"] = "spf-prefix-priorities"

                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self._children_name_map["summary_prefixes"] = "summary-prefixes"

                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self._children_name_map["micro_loop_avoidance"] = "micro-loop-avoidance"

                            self.ucmp = Isis.Instances.Instance.Afs.Af.AfData.Ucmp()
                            self.ucmp.parent = self
                            self._children_name_map["ucmp"] = "ucmp"

                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self._children_name_map["max_redist_prefixes"] = "max-redist-prefixes"

                            self.propagations = Isis.Instances.Instance.Afs.Af.AfData.Propagations()
                            self.propagations.parent = self
                            self._children_name_map["propagations"] = "propagations"

                            self.redistributions = Isis.Instances.Instance.Afs.Af.AfData.Redistributions()
                            self.redistributions.parent = self
                            self._children_name_map["redistributions"] = "redistributions"

                            self.application_tables = Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables()
                            self.application_tables.parent = self
                            self._children_name_map["application_tables"] = "application-tables"

                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self._children_name_map["spf_periodic_intervals"] = "spf-periodic-intervals"

                            self.distribute_list_in = Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn()
                            self.distribute_list_in.parent = self
                            self._children_name_map["distribute_list_in"] = "distribute-list-in"

                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals()
                            self.spf_intervals.parent = self
                            self._children_name_map["spf_intervals"] = "spf-intervals"

                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self._children_name_map["monitor_convergence"] = "monitor-convergence"

                            self.default_information = Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation()
                            self.default_information.parent = self
                            self._children_name_map["default_information"] = "default-information"

                            self.admin_distances = Isis.Instances.Instance.Afs.Af.AfData.AdminDistances()
                            self.admin_distances.parent = self
                            self._children_name_map["admin_distances"] = "admin-distances"

                            self.ispf = Isis.Instances.Instance.Afs.Af.AfData.Ispf()
                            self.ispf.parent = self
                            self._children_name_map["ispf"] = "ispf"

                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self._children_name_map["mpls_ldp_global"] = "mpls-ldp-global"

                            self.mpls = Isis.Instances.Instance.Afs.Af.AfData.Mpls()
                            self.mpls.parent = self
                            self._children_name_map["mpls"] = "mpls"

                            self.manual_adj_sids = Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids()
                            self.manual_adj_sids.parent = self
                            self._children_name_map["manual_adj_sids"] = "manual-adj-sids"

                            self.metrics = Isis.Instances.Instance.Afs.Af.AfData.Metrics()
                            self.metrics.parent = self
                            self._children_name_map["metrics"] = "metrics"

                            self.weights = Isis.Instances.Instance.Afs.Af.AfData.Weights()
                            self.weights.parent = self
                            self._children_name_map["weights"] = "weights"
                            self._segment_path = lambda: "af-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData, ['maximum_paths', 'topology_id', 'single_topology', 'adjacency_check', 'advertise_link_attributes', 'apply_weight', 'default_admin_distance', 'advertise_passive_only', 'ignore_attached_bit', 'attached_bit', 'route_source_first_hop'], name, value)


                        class SegmentRouting(Entity):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\:  :py:class:`PrefixSidMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap>`
                            
                            .. attribute:: bundle_member_adj_sid
                            
                            	Enable per bundle member adjacency SID
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\:  :py:class:`IsisLabelPreference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreference>`
                            
                            .. attribute:: srv6
                            
                            	Enable Segment Routing SRV6 configuration
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting, self).__init__()

                                self.yang_name = "segment-routing"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("prefix-sid-map", ("prefix_sid_map", Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap))])
                                self._leafs = OrderedDict([
                                    ('bundle_member_adj_sid', (YLeaf(YType.empty, 'bundle-member-adj-sid'), ['Empty'])),
                                    ('mpls', (YLeaf(YType.enumeration, 'mpls'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreference', '')])),
                                    ('srv6', (YLeaf(YType.empty, 'srv6'), ['Empty'])),
                                ])
                                self.bundle_member_adj_sid = None
                                self.mpls = None
                                self.srv6 = None

                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self
                                self._children_name_map["prefix_sid_map"] = "prefix-sid-map"
                                self._segment_path = lambda: "segment-routing"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting, ['bundle_member_adj_sid', 'mpls', 'srv6'], name, value)


                            class PrefixSidMap(Entity):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap, self).__init__()

                                    self.yang_name = "prefix-sid-map"
                                    self.yang_parent_name = "segment-routing"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('advertise_local', (YLeaf(YType.empty, 'advertise-local'), ['Empty'])),
                                        ('receive', (YLeaf(YType.boolean, 'receive'), ['bool'])),
                                    ])
                                    self.advertise_local = None
                                    self.receive = None
                                    self._segment_path = lambda: "prefix-sid-map"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap, ['advertise_local', 'receive'], name, value)


                        class MetricStyles(Entity):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of  		 :py:class:`MetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles, self).__init__()

                                self.yang_name = "metric-styles"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric-style", ("metric_style", Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle))])
                                self._leafs = OrderedDict()

                                self.metric_style = YList(self)
                                self._segment_path = lambda: "metric-styles"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles, [], name, value)


                            class MetricStyle(Entity):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\:  :py:class:`IsisMetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyle>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle, self).__init__()

                                    self.yang_name = "metric-style"
                                    self.yang_parent_name = "metric-styles"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('style', (YLeaf(YType.enumeration, 'style'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyle', '')])),
                                    ])
                                    self.level = None
                                    self.style = None
                                    self._segment_path = lambda: "metric-style" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle, ['level', 'style'], name, value)


                        class FrrTable(Entity):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\:  :py:class:`FrrLoadSharings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frrsrlg_protection_types
                            
                            	SRLG protection type configuration
                            	**type**\:  :py:class:`FrrsrlgProtectionTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\:  :py:class:`PriorityLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\:  :py:class:`FrrRemoteLfaPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\:  :py:class:`FrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\:  :py:class:`FrrUseCandOnlies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: frr_initial_delay
                            
                            	Delay before running FRR (milliseconds)
                            	**type**\: int
                            
                            	**range:** 100..60000
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable, self).__init__()

                                self.yang_name = "frr-table"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("frr-load-sharings", ("frr_load_sharings", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings)), ("frrsrlg-protection-types", ("frrsrlg_protection_types", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes)), ("priority-limits", ("priority_limits", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits)), ("frr-remote-lfa-prefixes", ("frr_remote_lfa_prefixes", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes)), ("frr-tiebreakers", ("frr_tiebreakers", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers)), ("frr-use-cand-onlies", ("frr_use_cand_onlies", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies))])
                                self._leafs = OrderedDict([
                                    ('frr_initial_delay', (YLeaf(YType.uint32, 'frr-initial-delay'), ['int'])),
                                ])
                                self.frr_initial_delay = None

                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self._children_name_map["frr_load_sharings"] = "frr-load-sharings"

                                self.frrsrlg_protection_types = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes()
                                self.frrsrlg_protection_types.parent = self
                                self._children_name_map["frrsrlg_protection_types"] = "frrsrlg-protection-types"

                                self.priority_limits = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self
                                self._children_name_map["priority_limits"] = "priority-limits"

                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self._children_name_map["frr_remote_lfa_prefixes"] = "frr-remote-lfa-prefixes"

                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self._children_name_map["frr_tiebreakers"] = "frr-tiebreakers"

                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self._children_name_map["frr_use_cand_onlies"] = "frr-use-cand-onlies"
                                self._segment_path = lambda: "frr-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable, ['frr_initial_delay'], name, value)


                            class FrrLoadSharings(Entity):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of  		 :py:class:`FrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings, self).__init__()

                                    self.yang_name = "frr-load-sharings"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-load-sharing", ("frr_load_sharing", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing))])
                                    self._leafs = OrderedDict()

                                    self.frr_load_sharing = YList(self)
                                    self._segment_path = lambda: "frr-load-sharings"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings, [], name, value)


                                class FrrLoadSharing(Entity):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\:  :py:class:`IsisfrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharing>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing, self).__init__()

                                        self.yang_name = "frr-load-sharing"
                                        self.yang_parent_name = "frr-load-sharings"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('load_sharing', (YLeaf(YType.enumeration, 'load-sharing'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharing', '')])),
                                        ])
                                        self.level = None
                                        self.load_sharing = None
                                        self._segment_path = lambda: "frr-load-sharing" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing, ['level', 'load_sharing'], name, value)


                            class FrrsrlgProtectionTypes(Entity):
                                """
                                SRLG protection type configuration
                                
                                .. attribute:: frrsrlg_protection_type
                                
                                	FRR SRLG Protection Type
                                	**type**\: list of  		 :py:class:`FrrsrlgProtectionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes, self).__init__()

                                    self.yang_name = "frrsrlg-protection-types"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frrsrlg-protection-type", ("frrsrlg_protection_type", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType))])
                                    self._leafs = OrderedDict()

                                    self.frrsrlg_protection_type = YList(self)
                                    self._segment_path = lambda: "frrsrlg-protection-types"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes, [], name, value)


                                class FrrsrlgProtectionType(Entity):
                                    """
                                    FRR SRLG Protection Type
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: protection_type
                                    
                                    	Protection Type
                                    	**type**\:  :py:class:`IsisfrrSrlgProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrSrlgProtection>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType, self).__init__()

                                        self.yang_name = "frrsrlg-protection-type"
                                        self.yang_parent_name = "frrsrlg-protection-types"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('protection_type', (YLeaf(YType.enumeration, 'protection-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrSrlgProtection', '')])),
                                        ])
                                        self.level = None
                                        self.protection_type = None
                                        self._segment_path = lambda: "frrsrlg-protection-type" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType, ['level', 'protection_type'], name, value)


                            class PriorityLimits(Entity):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of  		 :py:class:`PriorityLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits, self).__init__()

                                    self.yang_name = "priority-limits"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("priority-limit", ("priority_limit", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit))])
                                    self._leafs = OrderedDict()

                                    self.priority_limit = YList(self)
                                    self._segment_path = lambda: "priority-limits"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits, [], name, value)


                                class PriorityLimit(Entity):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: priority_limit_data
                                    
                                    	Data container
                                    	**type**\:  :py:class:`PriorityLimitData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData>`
                                    
                                    .. attribute:: frr_type
                                    
                                    	keys\: frr\-type
                                    	**type**\: list of  		 :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.FrrType>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit, self).__init__()

                                        self.yang_name = "priority-limit"
                                        self.yang_parent_name = "priority-limits"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([("priority-limit-data", ("priority_limit_data", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData)), ("frr-type", ("frr_type", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.FrrType))])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ])
                                        self.level = None

                                        self.priority_limit_data = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData()
                                        self.priority_limit_data.parent = self
                                        self._children_name_map["priority_limit_data"] = "priority-limit-data"

                                        self.frr_type = YList(self)
                                        self._segment_path = lambda: "priority-limit" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit, ['level'], name, value)


                                    class PriorityLimitData(Entity):
                                        """
                                        Data container.
                                        
                                        .. attribute:: priority
                                        
                                        	Compute for all prefixes upto the specified priority
                                        	**type**\:  :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData, self).__init__()

                                            self.yang_name = "priority-limit-data"
                                            self.yang_parent_name = "priority-limit"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority', '')])),
                                            ])
                                            self.priority = None
                                            self._segment_path = lambda: "priority-limit-data"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData, ['priority'], name, value)


                                    class FrrType(Entity):
                                        """
                                        keys\: frr\-type
                                        
                                        .. attribute:: frr_type  (key)
                                        
                                        	Computation Type
                                        	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                        
                                        .. attribute:: priority
                                        
                                        	Compute for all prefixes upto the specified priority
                                        	**type**\:  :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.FrrType, self).__init__()

                                            self.yang_name = "frr-type"
                                            self.yang_parent_name = "priority-limit"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['frr_type']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority', '')])),
                                            ])
                                            self.frr_type = None
                                            self.priority = None
                                            self._segment_path = lambda: "frr-type" + "[frr-type='" + str(self.frr_type) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit.FrrType, ['frr_type', 'priority'], name, value)


                            class FrrRemoteLfaPrefixes(Entity):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of  		 :py:class:`FrrRemoteLfaPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes, self).__init__()

                                    self.yang_name = "frr-remote-lfa-prefixes"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-remote-lfa-prefix", ("frr_remote_lfa_prefix", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix))])
                                    self._leafs = OrderedDict()

                                    self.frr_remote_lfa_prefix = YList(self)
                                    self._segment_path = lambda: "frr-remote-lfa-prefixes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes, [], name, value)


                                class FrrRemoteLfaPrefix(Entity):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\: str
                                    
                                    	**length:** 1..32
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, self).__init__()

                                        self.yang_name = "frr-remote-lfa-prefix"
                                        self.yang_parent_name = "frr-remote-lfa-prefixes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                                        ])
                                        self.level = None
                                        self.prefix_list_name = None
                                        self._segment_path = lambda: "frr-remote-lfa-prefix" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, ['level', 'prefix_list_name'], name, value)


                            class FrrTiebreakers(Entity):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of  		 :py:class:`FrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers, self).__init__()

                                    self.yang_name = "frr-tiebreakers"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-tiebreaker", ("frr_tiebreaker", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker))])
                                    self._leafs = OrderedDict()

                                    self.frr_tiebreaker = YList(self)
                                    self._segment_path = lambda: "frr-tiebreakers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers, [], name, value)


                                class FrrTiebreaker(Entity):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: tiebreaker  (key)
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\:  :py:class:`IsisfrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreaker>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker, self).__init__()

                                        self.yang_name = "frr-tiebreaker"
                                        self.yang_parent_name = "frr-tiebreakers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level','tiebreaker']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('tiebreaker', (YLeaf(YType.enumeration, 'tiebreaker'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreaker', '')])),
                                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                        ])
                                        self.level = None
                                        self.tiebreaker = None
                                        self.index = None
                                        self._segment_path = lambda: "frr-tiebreaker" + "[level='" + str(self.level) + "']" + "[tiebreaker='" + str(self.tiebreaker) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                            class FrrUseCandOnlies(Entity):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of  		 :py:class:`FrrUseCandOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies, self).__init__()

                                    self.yang_name = "frr-use-cand-onlies"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-use-cand-only", ("frr_use_cand_only", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly))])
                                    self._leafs = OrderedDict()

                                    self.frr_use_cand_only = YList(self)
                                    self._segment_path = lambda: "frr-use-cand-onlies"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies, [], name, value)


                                class FrrUseCandOnly(Entity):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: frr_type  (key)
                                    
                                    	Computation Type
                                    	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, self).__init__()

                                        self.yang_name = "frr-use-cand-only"
                                        self.yang_parent_name = "frr-use-cand-onlies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level','frr_type']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                        ])
                                        self.level = None
                                        self.frr_type = None
                                        self._segment_path = lambda: "frr-use-cand-only" + "[level='" + str(self.level) + "']" + "[frr-type='" + str(self.frr_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, ['level', 'frr_type'], name, value)


                        class RouterId(Entity):
                            """
                            Stable IP address for system. Will only be
                            applied for the unicast sub\-address\-family.
                            
                            .. attribute:: address
                            
                            	IPv4/IPv6 address to be used as a router ID. Precisely one of Address and Interface must be specified
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.RouterId, self).__init__()

                                self.yang_name = "router-id"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.address = None
                                self.interface_name = None
                                self._segment_path = lambda: "router-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.RouterId, ['address', 'interface_name'], name, value)


                        class SpfPrefixPriorities(Entity):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of  		 :py:class:`SpfPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities, self).__init__()

                                self.yang_name = "spf-prefix-priorities"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("spf-prefix-priority", ("spf_prefix_priority", Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority))])
                                self._leafs = OrderedDict()

                                self.spf_prefix_priority = YList(self)
                                self._segment_path = lambda: "spf-prefix-priorities"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities, [], name, value)


                            class SpfPrefixPriority(Entity):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level  (key)
                                
                                	SPF Level for prefix prioritization
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_priority_type  (key)
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\:  :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority, self).__init__()

                                    self.yang_name = "spf-prefix-priority"
                                    self.yang_parent_name = "spf-prefix-priorities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level','prefix_priority_type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('prefix_priority_type', (YLeaf(YType.enumeration, 'prefix-priority-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority', '')])),
                                        ('admin_tag', (YLeaf(YType.uint32, 'admin-tag'), ['int'])),
                                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                    ])
                                    self.level = None
                                    self.prefix_priority_type = None
                                    self.admin_tag = None
                                    self.access_list_name = None
                                    self._segment_path = lambda: "spf-prefix-priority" + "[level='" + str(self.level) + "']" + "[prefix-priority-type='" + str(self.prefix_priority_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority, ['level', 'prefix_priority_type', 'admin_tag', 'access_list_name'], name, value)


                        class SummaryPrefixes(Entity):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of  		 :py:class:`SummaryPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes, self).__init__()

                                self.yang_name = "summary-prefixes"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("summary-prefix", ("summary_prefix", Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix))])
                                self._leafs = OrderedDict()

                                self.summary_prefix = YList(self)
                                self._segment_path = lambda: "summary-prefixes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes, [], name, value)


                            class SummaryPrefix(Entity):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix  (key)
                                
                                	IP summary address prefix
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix, self).__init__()

                                    self.yang_name = "summary-prefix"
                                    self.yang_parent_name = "summary-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address_prefix']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_prefix', (YLeaf(YType.str, 'address-prefix'), ['str','str'])),
                                        ('tag', (YLeaf(YType.uint32, 'tag'), ['int'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.address_prefix = None
                                    self.tag = None
                                    self.level = None
                                    self._segment_path = lambda: "summary-prefix" + "[address-prefix='" + str(self.address_prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix, ['address_prefix', 'tag', 'level'], name, value)


                        class MicroLoopAvoidance(Entity):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\:  :py:class:`IsisMicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidance>`
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\: int
                            
                            	**range:** 1000..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 5000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance, self).__init__()

                                self.yang_name = "micro-loop-avoidance"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.enumeration, 'enable'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidance', '')])),
                                    ('rib_update_delay', (YLeaf(YType.uint32, 'rib-update-delay'), ['int'])),
                                ])
                                self.enable = None
                                self.rib_update_delay = None
                                self._segment_path = lambda: "micro-loop-avoidance"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance, ['enable', 'rib_update_delay'], name, value)


                        class Ucmp(Entity):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\:  :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\:  :py:class:`ExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces>`
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\: int
                            
                            	**range:** 100..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 100
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp, self).__init__()

                                self.yang_name = "ucmp"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enable", ("enable", Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable)), ("exclude-interfaces", ("exclude_interfaces", Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces))])
                                self._leafs = OrderedDict([
                                    ('delay_interval', (YLeaf(YType.uint32, 'delay-interval'), ['int'])),
                                ])
                                self.delay_interval = None

                                self.enable = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable()
                                self.enable.parent = self
                                self._children_name_map["enable"] = "enable"

                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self
                                self._children_name_map["exclude_interfaces"] = "exclude-interfaces"
                                self._segment_path = lambda: "ucmp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp, ['delay_interval'], name, value)


                            class Enable(Entity):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\: int
                                
                                	**range:** 101..10000
                                
                                	**default value**\: 200
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable, self).__init__()

                                    self.yang_name = "enable"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                                    ])
                                    self.variance = None
                                    self.prefix_list_name = None
                                    self._segment_path = lambda: "enable"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable, ['variance', 'prefix_list_name'], name, value)


                            class ExcludeInterfaces(Entity):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of  		 :py:class:`ExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces, self).__init__()

                                    self.yang_name = "exclude-interfaces"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("exclude-interface", ("exclude_interface", Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface))])
                                    self._leafs = OrderedDict()

                                    self.exclude_interface = YList(self)
                                    self._segment_path = lambda: "exclude-interfaces"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces, [], name, value)


                                class ExcludeInterface(Entity):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Name of the interface to be excluded
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface, self).__init__()

                                        self.yang_name = "exclude-interface"
                                        self.yang_parent_name = "exclude-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ])
                                        self.interface_name = None
                                        self._segment_path = lambda: "exclude-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface, ['interface_name'], name, value)


                        class MaxRedistPrefixes(Entity):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of  		 :py:class:`MaxRedistPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes, self).__init__()

                                self.yang_name = "max-redist-prefixes"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("max-redist-prefix", ("max_redist_prefix", Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix))])
                                self._leafs = OrderedDict()

                                self.max_redist_prefix = YList(self)
                                self._segment_path = lambda: "max-redist-prefixes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes, [], name, value)


                            class MaxRedistPrefix(Entity):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\: int
                                
                                	**range:** 1..28000
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix, self).__init__()

                                    self.yang_name = "max-redist-prefix"
                                    self.yang_parent_name = "max-redist-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('prefix_limit', (YLeaf(YType.uint32, 'prefix-limit'), ['int'])),
                                    ])
                                    self.level = None
                                    self.prefix_limit = None
                                    self._segment_path = lambda: "max-redist-prefix" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix, ['level', 'prefix_limit'], name, value)


                        class Propagations(Entity):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of  		 :py:class:`Propagation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Propagations, self).__init__()

                                self.yang_name = "propagations"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("propagation", ("propagation", Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation))])
                                self._leafs = OrderedDict()

                                self.propagation = YList(self)
                                self._segment_path = lambda: "propagations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Propagations, [], name, value)


                            class Propagation(Entity):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: source_level  (key)
                                
                                	Source level for routes
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: destination_level  (key)
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation, self).__init__()

                                    self.yang_name = "propagation"
                                    self.yang_parent_name = "propagations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['source_level','destination_level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('source_level', (YLeaf(YType.enumeration, 'source-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('destination_level', (YLeaf(YType.enumeration, 'destination-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                    ])
                                    self.source_level = None
                                    self.destination_level = None
                                    self.route_policy_name = None
                                    self._segment_path = lambda: "propagation" + "[source-level='" + str(self.source_level) + "']" + "[destination-level='" + str(self.destination_level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation, ['source_level', 'destination_level', 'route_policy_name'], name, value)


                        class Redistributions(Entity):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of  		 :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions, self).__init__()

                                self.yang_name = "redistributions"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("redistribution", ("redistribution", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution))])
                                self._leafs = OrderedDict()

                                self.redistribution = YList(self)
                                self._segment_path = lambda: "redistributions"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions, [], name, value)


                            class Redistribution(Entity):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name  (key)
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\:  :py:class:`IsisRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProto>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\:  :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of  		 :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of  		 :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of  		 :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution, self).__init__()

                                    self.yang_name = "redistribution"
                                    self.yang_parent_name = "redistributions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['protocol_name']
                                    self._child_classes = OrderedDict([("connected-or-static-or-rip-or-subscriber-or-mobile", ("connected_or_static_or_rip_or_subscriber_or_mobile", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile)), ("ospf-or-ospfv3-or-isis-or-application", ("ospf_or_ospfv3_or_isis_or_application", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication)), ("bgp", ("bgp", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp)), ("eigrp", ("eigrp", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp))])
                                    self._leafs = OrderedDict([
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProto', '')])),
                                    ])
                                    self.protocol_name = None

                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self._children_name_map["connected_or_static_or_rip_or_subscriber_or_mobile"] = "connected-or-static-or-rip-or-subscriber-or-mobile"

                                    self.ospf_or_ospfv3_or_isis_or_application = YList(self)
                                    self.bgp = YList(self)
                                    self.eigrp = YList(self)
                                    self._segment_path = lambda: "redistribution" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution, ['protocol_name'], name, value)


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(Entity):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, self).__init__()

                                        self.yang_name = "connected-or-static-or-rip-or-subscriber-or-mobile"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "connected-or-static-or-rip-or-subscriber-or-mobile"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, ['metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                                class OspfOrOspfv3OrIsisOrApplication(Entity):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name  (key)
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, self).__init__()

                                        self.yang_name = "ospf-or-ospfv3-or-isis-or-application"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['instance_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.instance_name = None
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "ospf-or-ospfv3-or-isis-or-application" + "[instance-name='" + str(self.instance_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, ['instance_name', 'metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                                class Bgp(Entity):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  (key)
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','as_yy']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "bgp" + "[as-xx='" + str(self.as_xx) + "']" + "[as-yy='" + str(self.as_yy) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp, ['as_xx', 'as_yy', 'metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                                class Eigrp(Entity):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz  (key)
                                    
                                    	Eigrp as number
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp, self).__init__()

                                        self.yang_name = "eigrp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_zz']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_zz', (YLeaf(YType.uint32, 'as-zz'), ['int'])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.as_zz = None
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "eigrp" + "[as-zz='" + str(self.as_zz) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp, ['as_zz', 'metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                        class ApplicationTables(Entity):
                            """
                            Advertise application specific values
                            
                            .. attribute:: application_table
                            
                            	Application Name
                            	**type**\: list of  		 :py:class:`ApplicationTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables, self).__init__()

                                self.yang_name = "application-tables"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("application-table", ("application_table", Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable))])
                                self._leafs = OrderedDict()

                                self.application_table = YList(self)
                                self._segment_path = lambda: "application-tables"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables, [], name, value)


                            class ApplicationTable(Entity):
                                """
                                Application Name
                                
                                .. attribute:: app_type  (key)
                                
                                	Application Type
                                	**type**\:  :py:class:`IsisApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplication>`
                                
                                .. attribute:: attribute_table
                                
                                	Attribute Name
                                	**type**\: list of  		 :py:class:`AttributeTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable, self).__init__()

                                    self.yang_name = "application-table"
                                    self.yang_parent_name = "application-tables"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['app_type']
                                    self._child_classes = OrderedDict([("attribute-table", ("attribute_table", Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable))])
                                    self._leafs = OrderedDict([
                                        ('app_type', (YLeaf(YType.enumeration, 'app-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplication', '')])),
                                    ])
                                    self.app_type = None

                                    self.attribute_table = YList(self)
                                    self._segment_path = lambda: "application-table" + "[app-type='" + str(self.app_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable, ['app_type'], name, value)


                                class AttributeTable(Entity):
                                    """
                                    Attribute Name
                                    
                                    .. attribute:: app_type  (key)
                                    
                                    	Application Type
                                    	**type**\:  :py:class:`IsisApplicationAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplicationAttribute>`
                                    
                                    .. attribute:: enable
                                    
                                    	If TRUE, advertise application link attribute in our LSP
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable, self).__init__()

                                        self.yang_name = "attribute-table"
                                        self.yang_parent_name = "application-table"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['app_type']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('app_type', (YLeaf(YType.enumeration, 'app-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplicationAttribute', '')])),
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                        ])
                                        self.app_type = None
                                        self.enable = None
                                        self._segment_path = lambda: "attribute-table" + "[app-type='" + str(self.app_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ApplicationTables.ApplicationTable.AttributeTable, ['app_type', 'enable'], name, value)


                        class SpfPeriodicIntervals(Entity):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of  		 :py:class:`SpfPeriodicInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals, self).__init__()

                                self.yang_name = "spf-periodic-intervals"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("spf-periodic-interval", ("spf_periodic_interval", Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval))])
                                self._leafs = OrderedDict()

                                self.spf_periodic_interval = YList(self)
                                self._segment_path = lambda: "spf-periodic-intervals"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals, [], name, value)


                            class SpfPeriodicInterval(Entity):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\: int
                                
                                	**range:** 0..3600
                                
                                	**mandatory**\: True
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval, self).__init__()

                                    self.yang_name = "spf-periodic-interval"
                                    self.yang_parent_name = "spf-periodic-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('periodic_interval', (YLeaf(YType.uint32, 'periodic-interval'), ['int'])),
                                    ])
                                    self.level = None
                                    self.periodic_interval = None
                                    self._segment_path = lambda: "spf-periodic-interval" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval, ['level', 'periodic_interval'], name, value)


                        class DistributeListIn(Entity):
                            """
                            Filter routes sent to the RIB
                            
                            .. attribute:: prefix_list_name
                            
                            	Prefix list to control routes installed in RIB
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: route_policy_name
                            
                            	Route policy to control routes installed in RIB
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn, self).__init__()

                                self.yang_name = "distribute-list-in"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                                    ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ])
                                self.prefix_list_name = None
                                self.route_policy_name = None
                                self._segment_path = lambda: "distribute-list-in"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.DistributeListIn, ['prefix_list_name', 'route_policy_name'], name, value)


                        class SpfIntervals(Entity):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of  		 :py:class:`SpfInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals, self).__init__()

                                self.yang_name = "spf-intervals"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("spf-interval", ("spf_interval", Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval))])
                                self._leafs = OrderedDict()

                                self.spf_interval = YList(self)
                                self._segment_path = lambda: "spf-intervals"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals, [], name, value)


                            class SpfInterval(Entity):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval, self).__init__()

                                    self.yang_name = "spf-interval"
                                    self.yang_parent_name = "spf-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('maximum_wait', (YLeaf(YType.uint32, 'maximum-wait'), ['int'])),
                                        ('initial_wait', (YLeaf(YType.uint32, 'initial-wait'), ['int'])),
                                        ('secondary_wait', (YLeaf(YType.uint32, 'secondary-wait'), ['int'])),
                                    ])
                                    self.level = None
                                    self.maximum_wait = None
                                    self.initial_wait = None
                                    self.secondary_wait = None
                                    self._segment_path = lambda: "spf-interval" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval, ['level', 'maximum_wait', 'initial_wait', 'secondary_wait'], name, value)


                        class MonitorConvergence(Entity):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence, self).__init__()

                                self.yang_name = "monitor-convergence"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ('track_ip_frr', (YLeaf(YType.empty, 'track-ip-frr'), ['Empty'])),
                                    ('prefix_list', (YLeaf(YType.str, 'prefix-list'), ['str'])),
                                ])
                                self.enable = None
                                self.track_ip_frr = None
                                self.prefix_list = None
                                self._segment_path = lambda: "monitor-convergence"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence, ['enable', 'track_ip_frr', 'prefix_list'], name, value)


                        class DefaultInformation(Entity):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\: bool
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation, self).__init__()

                                self.yang_name = "default-information"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('use_policy', (YLeaf(YType.boolean, 'use-policy'), ['bool'])),
                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                    ('external', (YLeaf(YType.empty, 'external'), ['Empty'])),
                                ])
                                self.use_policy = None
                                self.policy_name = None
                                self.external = None
                                self._segment_path = lambda: "default-information"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation, ['use_policy', 'policy_name', 'external'], name, value)


                        class AdminDistances(Entity):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of  		 :py:class:`AdminDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances, self).__init__()

                                self.yang_name = "admin-distances"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("admin-distance", ("admin_distance", Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance))])
                                self._leafs = OrderedDict()

                                self.admin_distance = YList(self)
                                self._segment_path = lambda: "admin-distances"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances, [], name, value)


                            class AdminDistance(Entity):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix  (key)
                                
                                	IP route source prefix
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**mandatory**\: True
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance, self).__init__()

                                    self.yang_name = "admin-distance"
                                    self.yang_parent_name = "admin-distances"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address_prefix']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_prefix', (YLeaf(YType.str, 'address-prefix'), ['str','str'])),
                                        ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                                        ('prefix_list', (YLeaf(YType.str, 'prefix-list'), ['str'])),
                                    ])
                                    self.address_prefix = None
                                    self.distance = None
                                    self.prefix_list = None
                                    self._segment_path = lambda: "admin-distance" + "[address-prefix='" + str(self.address_prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance, ['address_prefix', 'distance', 'prefix_list'], name, value)


                        class Ispf(Entity):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\:  :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Ispf, self).__init__()

                                self.yang_name = "ispf"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("states", ("states", Isis.Instances.Instance.Afs.Af.AfData.Ispf.States))])
                                self._leafs = OrderedDict()

                                self.states = Isis.Instances.Instance.Afs.Af.AfData.Ispf.States()
                                self.states.parent = self
                                self._children_name_map["states"] = "states"
                                self._segment_path = lambda: "ispf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ispf, [], name, value)


                            class States(Entity):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of  		 :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States, self).__init__()

                                    self.yang_name = "states"
                                    self.yang_parent_name = "ispf"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("state", ("state", Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State))])
                                    self._leafs = OrderedDict()

                                    self.state = YList(self)
                                    self._segment_path = lambda: "states"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States, [], name, value)


                                class State(Entity):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:  :py:class:`IsisispfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisispfState>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "states"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfState', '')])),
                                        ])
                                        self.level = None
                                        self.state = None
                                        self._segment_path = lambda: "state" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State, ['level', 'state'], name, value)


                        class MplsLdpGlobal(Entity):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal, self).__init__()

                                self.yang_name = "mpls-ldp-global"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('auto_config', (YLeaf(YType.boolean, 'auto-config'), ['bool'])),
                                ])
                                self.auto_config = None
                                self._segment_path = lambda: "mpls-ldp-global"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal, ['auto_config'], name, value)


                        class Mpls(Entity):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:  :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\:  :py:class:`Level <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level>`
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Mpls, self).__init__()

                                self.yang_name = "mpls"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("router-id", ("router_id", Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId)), ("level", ("level", Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level))])
                                self._leafs = OrderedDict([
                                    ('igp_intact', (YLeaf(YType.empty, 'igp-intact'), ['Empty'])),
                                    ('multicast_intact', (YLeaf(YType.empty, 'multicast-intact'), ['Empty'])),
                                ])
                                self.igp_intact = None
                                self.multicast_intact = None

                                self.router_id = Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId()
                                self.router_id.parent = self
                                self._children_name_map["router_id"] = "router-id"

                                self.level = Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level()
                                self.level.parent = self
                                self._children_name_map["level"] = "level"
                                self._segment_path = lambda: "mpls"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Mpls, ['igp_intact', 'multicast_intact'], name, value)


                            class RouterId(Entity):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId, self).__init__()

                                    self.yang_name = "router-id"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ])
                                    self.address = None
                                    self.interface_name = None
                                    self._segment_path = lambda: "router-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId, ['address', 'interface_name'], name, value)


                            class Level(Entity):
                                """
                                Enable MPLS for an IS\-IS at the given
                                levels
                                
                                .. attribute:: level1
                                
                                	Level 1 enabled
                                	**type**\: bool
                                
                                .. attribute:: level2
                                
                                	Level 2 enabled
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level, self).__init__()

                                    self.yang_name = "level"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level1', (YLeaf(YType.boolean, 'level1'), ['bool'])),
                                        ('level2', (YLeaf(YType.boolean, 'level2'), ['bool'])),
                                    ])
                                    self.level1 = None
                                    self.level2 = None
                                    self._segment_path = lambda: "level"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level, ['level1', 'level2'], name, value)


                        class ManualAdjSids(Entity):
                            """
                            Manual Adjacecy SID configuration
                            
                            .. attribute:: manual_adj_sid
                            
                            	Assign adjancency SID to an interface
                            	**type**\: list of  		 :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids, self).__init__()

                                self.yang_name = "manual-adj-sids"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("manual-adj-sid", ("manual_adj_sid", Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid))])
                                self._leafs = OrderedDict()

                                self.manual_adj_sid = YList(self)
                                self._segment_path = lambda: "manual-adj-sids"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids, [], name, value)


                            class ManualAdjSid(Entity):
                                """
                                Assign adjancency SID to an interface
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: sid_type  (key)
                                
                                	Sid type aboslute or index
                                	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                
                                .. attribute:: sid  (key)
                                
                                	Sid value
                                	**type**\: int
                                
                                	**range:** 0..1048575
                                
                                .. attribute:: protected
                                
                                	Enable/Disable SID protection
                                	**type**\:  :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid, self).__init__()

                                    self.yang_name = "manual-adj-sid"
                                    self.yang_parent_name = "manual-adj-sids"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level','sid_type','sid']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                        ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                        ('protected', (YLeaf(YType.enumeration, 'protected'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected', '')])),
                                    ])
                                    self.level = None
                                    self.sid_type = None
                                    self.sid = None
                                    self.protected = None
                                    self._segment_path = lambda: "manual-adj-sid" + "[level='" + str(self.level) + "']" + "[sid-type='" + str(self.sid_type) + "']" + "[sid='" + str(self.sid) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                        class Metrics(Entity):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of  		 :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Metrics, self).__init__()

                                self.yang_name = "metrics"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric", ("metric", Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric))])
                                self._leafs = OrderedDict()

                                self.metric = YList(self)
                                self._segment_path = lambda: "metrics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Metrics, [], name, value)


                            class Metric(Entity):
                                """
                                Metric configuration. Legal value depends on
                                the metric\-style specified for the topology. If
                                the metric\-style defined is narrow, then only a
                                value between <1\-63> is allowed and if the
                                metric\-style is defined as wide, then a value
                                between <1\-16777215> is allowed as the metric
                                value.  All routers exclude links with the
                                maximum wide metric (16777215) from their SPF
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: union of the below types:
                                
                                		**type**\:  :py:class:`Metric_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_>`
                                
                                		**type**\: int
                                
                                			**range:** 1..16777215
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric, self).__init__()

                                    self.yang_name = "metric"
                                    self.yang_parent_name = "metrics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('metric', (YLeaf(YType.str, 'metric'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis', 'Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_'),'int'])),
                                    ])
                                    self.level = None
                                    self.metric = None
                                    self._segment_path = lambda: "metric" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric, ['level', 'metric'], name, value)

                                class Metric_(Enum):
                                    """
                                    Metric\_ (Enum Class)

                                    Allowed metric\: <1\-63> for narrow,

                                    <1\-16777215> for wide

                                    .. data:: maximum = 16777215

                                    	Maximum wide metric.  All routers will

                                    	exclude this link from their SPF

                                    """

                                    maximum = Enum.YLeaf(16777215, "maximum")



                        class Weights(Entity):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of  		 :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Weights, self).__init__()

                                self.yang_name = "weights"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("weight", ("weight", Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight))])
                                self._leafs = OrderedDict()

                                self.weight = YList(self)
                                self._segment_path = lambda: "weights"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Weights, [], name, value)


                            class Weight(Entity):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\: int
                                
                                	**range:** 1..16777214
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight, self).__init__()

                                    self.yang_name = "weight"
                                    self.yang_parent_name = "weights"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                                    ])
                                    self.level = None
                                    self.weight = None
                                    self._segment_path = lambda: "weight" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight, ['level', 'weight'], name, value)


                    class TopologyName(Entity):
                        """
                        keys\: topology\-name
                        
                        .. attribute:: topology_name  (key)
                        
                        	Topology Name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\:  :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting>`
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\:  :py:class:`MetricStyles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\:  :py:class:`FrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable>`
                        
                        .. attribute:: router_id
                        
                        	Stable IP address for system. Will only be applied for the unicast sub\-address\-family
                        	**type**\:  :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.RouterId>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\:  :py:class:`SpfPrefixPriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\:  :py:class:`SummaryPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\:  :py:class:`MicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance>`
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\:  :py:class:`Ucmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\:  :py:class:`MaxRedistPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\:  :py:class:`Propagations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\:  :py:class:`Redistributions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions>`
                        
                        .. attribute:: application_tables
                        
                        	Advertise application specific values
                        	**type**\:  :py:class:`ApplicationTables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\:  :py:class:`SpfPeriodicIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals>`
                        
                        .. attribute:: distribute_list_in
                        
                        	Filter routes sent to the RIB
                        	**type**\:  :py:class:`DistributeListIn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\:  :py:class:`SpfIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\:  :py:class:`MonitorConvergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence>`
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\:  :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\:  :py:class:`AdminDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances>`
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\:  :py:class:`Ispf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:  :py:class:`MplsLdpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\: int
                        
                        	**range:** 1..64
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\: int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\:  :py:class:`IsisAdjCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheck>`
                        
                        .. attribute:: advertise_link_attributes
                        
                        	If TRUE, advertise additional link attributes in our LSP
                        	**type**\: bool
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\:  :py:class:`IsisApplyWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeight>`
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 115
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\: bool
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\:  :py:class:`IsisAttachedBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit>`
                        
                        	**default value**\: area
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\: bool
                        
                        .. attribute:: manual_adj_sids
                        
                        	Manual Adjacecy SID configuration
                        	**type**\:  :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\:  :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\:  :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Afs.Af.TopologyName, self).__init__()

                            self.yang_name = "topology-name"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['topology_name']
                            self._child_classes = OrderedDict([("segment-routing", ("segment_routing", Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting)), ("metric-styles", ("metric_styles", Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles)), ("frr-table", ("frr_table", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable)), ("router-id", ("router_id", Isis.Instances.Instance.Afs.Af.TopologyName.RouterId)), ("spf-prefix-priorities", ("spf_prefix_priorities", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities)), ("summary-prefixes", ("summary_prefixes", Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes)), ("micro-loop-avoidance", ("micro_loop_avoidance", Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance)), ("ucmp", ("ucmp", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp)), ("max-redist-prefixes", ("max_redist_prefixes", Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes)), ("propagations", ("propagations", Isis.Instances.Instance.Afs.Af.TopologyName.Propagations)), ("redistributions", ("redistributions", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions)), ("application-tables", ("application_tables", Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables)), ("spf-periodic-intervals", ("spf_periodic_intervals", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals)), ("distribute-list-in", ("distribute_list_in", Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn)), ("spf-intervals", ("spf_intervals", Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals)), ("monitor-convergence", ("monitor_convergence", Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence)), ("default-information", ("default_information", Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation)), ("admin-distances", ("admin_distances", Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances)), ("ispf", ("ispf", Isis.Instances.Instance.Afs.Af.TopologyName.Ispf)), ("mpls-ldp-global", ("mpls_ldp_global", Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal)), ("mpls", ("mpls", Isis.Instances.Instance.Afs.Af.TopologyName.Mpls)), ("manual-adj-sids", ("manual_adj_sids", Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids)), ("metrics", ("metrics", Isis.Instances.Instance.Afs.Af.TopologyName.Metrics)), ("weights", ("weights", Isis.Instances.Instance.Afs.Af.TopologyName.Weights))])
                            self._leafs = OrderedDict([
                                ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                                ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                                ('topology_id', (YLeaf(YType.uint32, 'topology-id'), ['int'])),
                                ('single_topology', (YLeaf(YType.empty, 'single-topology'), ['Empty'])),
                                ('adjacency_check', (YLeaf(YType.enumeration, 'adjacency-check'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdjCheck', '')])),
                                ('advertise_link_attributes', (YLeaf(YType.boolean, 'advertise-link-attributes'), ['bool'])),
                                ('apply_weight', (YLeaf(YType.enumeration, 'apply-weight'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplyWeight', '')])),
                                ('default_admin_distance', (YLeaf(YType.uint32, 'default-admin-distance'), ['int'])),
                                ('advertise_passive_only', (YLeaf(YType.empty, 'advertise-passive-only'), ['Empty'])),
                                ('ignore_attached_bit', (YLeaf(YType.boolean, 'ignore-attached-bit'), ['bool'])),
                                ('attached_bit', (YLeaf(YType.enumeration, 'attached-bit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAttachedBit', '')])),
                                ('route_source_first_hop', (YLeaf(YType.boolean, 'route-source-first-hop'), ['bool'])),
                            ])
                            self.topology_name = None
                            self.maximum_paths = None
                            self.topology_id = None
                            self.single_topology = None
                            self.adjacency_check = None
                            self.advertise_link_attributes = None
                            self.apply_weight = None
                            self.default_admin_distance = None
                            self.advertise_passive_only = None
                            self.ignore_attached_bit = None
                            self.attached_bit = None
                            self.route_source_first_hop = None

                            self.segment_routing = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting()
                            self.segment_routing.parent = self
                            self._children_name_map["segment_routing"] = "segment-routing"

                            self.metric_styles = Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles()
                            self.metric_styles.parent = self
                            self._children_name_map["metric_styles"] = "metric-styles"

                            self.frr_table = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable()
                            self.frr_table.parent = self
                            self._children_name_map["frr_table"] = "frr-table"

                            self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.RouterId()
                            self.router_id.parent = self
                            self._children_name_map["router_id"] = "router-id"

                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self._children_name_map["spf_prefix_priorities"] = "spf-prefix-priorities"

                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self._children_name_map["summary_prefixes"] = "summary-prefixes"

                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self._children_name_map["micro_loop_avoidance"] = "micro-loop-avoidance"

                            self.ucmp = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp()
                            self.ucmp.parent = self
                            self._children_name_map["ucmp"] = "ucmp"

                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self._children_name_map["max_redist_prefixes"] = "max-redist-prefixes"

                            self.propagations = Isis.Instances.Instance.Afs.Af.TopologyName.Propagations()
                            self.propagations.parent = self
                            self._children_name_map["propagations"] = "propagations"

                            self.redistributions = Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions()
                            self.redistributions.parent = self
                            self._children_name_map["redistributions"] = "redistributions"

                            self.application_tables = Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables()
                            self.application_tables.parent = self
                            self._children_name_map["application_tables"] = "application-tables"

                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self._children_name_map["spf_periodic_intervals"] = "spf-periodic-intervals"

                            self.distribute_list_in = Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn()
                            self.distribute_list_in.parent = self
                            self._children_name_map["distribute_list_in"] = "distribute-list-in"

                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals()
                            self.spf_intervals.parent = self
                            self._children_name_map["spf_intervals"] = "spf-intervals"

                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self._children_name_map["monitor_convergence"] = "monitor-convergence"

                            self.default_information = Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation()
                            self.default_information.parent = self
                            self._children_name_map["default_information"] = "default-information"

                            self.admin_distances = Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances()
                            self.admin_distances.parent = self
                            self._children_name_map["admin_distances"] = "admin-distances"

                            self.ispf = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf()
                            self.ispf.parent = self
                            self._children_name_map["ispf"] = "ispf"

                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self._children_name_map["mpls_ldp_global"] = "mpls-ldp-global"

                            self.mpls = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls()
                            self.mpls.parent = self
                            self._children_name_map["mpls"] = "mpls"

                            self.manual_adj_sids = Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids()
                            self.manual_adj_sids.parent = self
                            self._children_name_map["manual_adj_sids"] = "manual-adj-sids"

                            self.metrics = Isis.Instances.Instance.Afs.Af.TopologyName.Metrics()
                            self.metrics.parent = self
                            self._children_name_map["metrics"] = "metrics"

                            self.weights = Isis.Instances.Instance.Afs.Af.TopologyName.Weights()
                            self.weights.parent = self
                            self._children_name_map["weights"] = "weights"
                            self._segment_path = lambda: "topology-name" + "[topology-name='" + str(self.topology_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName, ['topology_name', 'maximum_paths', 'topology_id', 'single_topology', 'adjacency_check', 'advertise_link_attributes', 'apply_weight', 'default_admin_distance', 'advertise_passive_only', 'ignore_attached_bit', 'attached_bit', 'route_source_first_hop'], name, value)


                        class SegmentRouting(Entity):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\:  :py:class:`PrefixSidMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap>`
                            
                            .. attribute:: bundle_member_adj_sid
                            
                            	Enable per bundle member adjacency SID
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\:  :py:class:`IsisLabelPreference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreference>`
                            
                            .. attribute:: srv6
                            
                            	Enable Segment Routing SRV6 configuration
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting, self).__init__()

                                self.yang_name = "segment-routing"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("prefix-sid-map", ("prefix_sid_map", Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap))])
                                self._leafs = OrderedDict([
                                    ('bundle_member_adj_sid', (YLeaf(YType.empty, 'bundle-member-adj-sid'), ['Empty'])),
                                    ('mpls', (YLeaf(YType.enumeration, 'mpls'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisLabelPreference', '')])),
                                    ('srv6', (YLeaf(YType.empty, 'srv6'), ['Empty'])),
                                ])
                                self.bundle_member_adj_sid = None
                                self.mpls = None
                                self.srv6 = None

                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self
                                self._children_name_map["prefix_sid_map"] = "prefix-sid-map"
                                self._segment_path = lambda: "segment-routing"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting, ['bundle_member_adj_sid', 'mpls', 'srv6'], name, value)


                            class PrefixSidMap(Entity):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap, self).__init__()

                                    self.yang_name = "prefix-sid-map"
                                    self.yang_parent_name = "segment-routing"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('advertise_local', (YLeaf(YType.empty, 'advertise-local'), ['Empty'])),
                                        ('receive', (YLeaf(YType.boolean, 'receive'), ['bool'])),
                                    ])
                                    self.advertise_local = None
                                    self.receive = None
                                    self._segment_path = lambda: "prefix-sid-map"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap, ['advertise_local', 'receive'], name, value)


                        class MetricStyles(Entity):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of  		 :py:class:`MetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles, self).__init__()

                                self.yang_name = "metric-styles"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric-style", ("metric_style", Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle))])
                                self._leafs = OrderedDict()

                                self.metric_style = YList(self)
                                self._segment_path = lambda: "metric-styles"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles, [], name, value)


                            class MetricStyle(Entity):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\:  :py:class:`IsisMetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyle>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle, self).__init__()

                                    self.yang_name = "metric-style"
                                    self.yang_parent_name = "metric-styles"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('style', (YLeaf(YType.enumeration, 'style'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetricStyle', '')])),
                                    ])
                                    self.level = None
                                    self.style = None
                                    self._segment_path = lambda: "metric-style" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle, ['level', 'style'], name, value)


                        class FrrTable(Entity):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\:  :py:class:`FrrLoadSharings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frrsrlg_protection_types
                            
                            	SRLG protection type configuration
                            	**type**\:  :py:class:`FrrsrlgProtectionTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\:  :py:class:`PriorityLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\:  :py:class:`FrrRemoteLfaPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\:  :py:class:`FrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\:  :py:class:`FrrUseCandOnlies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: frr_initial_delay
                            
                            	Delay before running FRR (milliseconds)
                            	**type**\: int
                            
                            	**range:** 100..60000
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable, self).__init__()

                                self.yang_name = "frr-table"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("frr-load-sharings", ("frr_load_sharings", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings)), ("frrsrlg-protection-types", ("frrsrlg_protection_types", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes)), ("priority-limits", ("priority_limits", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits)), ("frr-remote-lfa-prefixes", ("frr_remote_lfa_prefixes", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes)), ("frr-tiebreakers", ("frr_tiebreakers", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers)), ("frr-use-cand-onlies", ("frr_use_cand_onlies", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies))])
                                self._leafs = OrderedDict([
                                    ('frr_initial_delay', (YLeaf(YType.uint32, 'frr-initial-delay'), ['int'])),
                                ])
                                self.frr_initial_delay = None

                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self._children_name_map["frr_load_sharings"] = "frr-load-sharings"

                                self.frrsrlg_protection_types = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes()
                                self.frrsrlg_protection_types.parent = self
                                self._children_name_map["frrsrlg_protection_types"] = "frrsrlg-protection-types"

                                self.priority_limits = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self
                                self._children_name_map["priority_limits"] = "priority-limits"

                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self._children_name_map["frr_remote_lfa_prefixes"] = "frr-remote-lfa-prefixes"

                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self._children_name_map["frr_tiebreakers"] = "frr-tiebreakers"

                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self._children_name_map["frr_use_cand_onlies"] = "frr-use-cand-onlies"
                                self._segment_path = lambda: "frr-table"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable, ['frr_initial_delay'], name, value)


                            class FrrLoadSharings(Entity):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of  		 :py:class:`FrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings, self).__init__()

                                    self.yang_name = "frr-load-sharings"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-load-sharing", ("frr_load_sharing", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing))])
                                    self._leafs = OrderedDict()

                                    self.frr_load_sharing = YList(self)
                                    self._segment_path = lambda: "frr-load-sharings"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings, [], name, value)


                                class FrrLoadSharing(Entity):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\:  :py:class:`IsisfrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharing>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing, self).__init__()

                                        self.yang_name = "frr-load-sharing"
                                        self.yang_parent_name = "frr-load-sharings"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('load_sharing', (YLeaf(YType.enumeration, 'load-sharing'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrLoadSharing', '')])),
                                        ])
                                        self.level = None
                                        self.load_sharing = None
                                        self._segment_path = lambda: "frr-load-sharing" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing, ['level', 'load_sharing'], name, value)


                            class FrrsrlgProtectionTypes(Entity):
                                """
                                SRLG protection type configuration
                                
                                .. attribute:: frrsrlg_protection_type
                                
                                	FRR SRLG Protection Type
                                	**type**\: list of  		 :py:class:`FrrsrlgProtectionType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes, self).__init__()

                                    self.yang_name = "frrsrlg-protection-types"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frrsrlg-protection-type", ("frrsrlg_protection_type", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType))])
                                    self._leafs = OrderedDict()

                                    self.frrsrlg_protection_type = YList(self)
                                    self._segment_path = lambda: "frrsrlg-protection-types"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes, [], name, value)


                                class FrrsrlgProtectionType(Entity):
                                    """
                                    FRR SRLG Protection Type
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: protection_type
                                    
                                    	Protection Type
                                    	**type**\:  :py:class:`IsisfrrSrlgProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrSrlgProtection>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType, self).__init__()

                                        self.yang_name = "frrsrlg-protection-type"
                                        self.yang_parent_name = "frrsrlg-protection-types"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('protection_type', (YLeaf(YType.enumeration, 'protection-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrSrlgProtection', '')])),
                                        ])
                                        self.level = None
                                        self.protection_type = None
                                        self._segment_path = lambda: "frrsrlg-protection-type" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrsrlgProtectionTypes.FrrsrlgProtectionType, ['level', 'protection_type'], name, value)


                            class PriorityLimits(Entity):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of  		 :py:class:`PriorityLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits, self).__init__()

                                    self.yang_name = "priority-limits"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("priority-limit", ("priority_limit", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit))])
                                    self._leafs = OrderedDict()

                                    self.priority_limit = YList(self)
                                    self._segment_path = lambda: "priority-limits"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits, [], name, value)


                                class PriorityLimit(Entity):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: priority_limit_data
                                    
                                    	Data container
                                    	**type**\:  :py:class:`PriorityLimitData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData>`
                                    
                                    .. attribute:: frr_type
                                    
                                    	keys\: frr\-type
                                    	**type**\: list of  		 :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.FrrType>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit, self).__init__()

                                        self.yang_name = "priority-limit"
                                        self.yang_parent_name = "priority-limits"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([("priority-limit-data", ("priority_limit_data", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData)), ("frr-type", ("frr_type", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.FrrType))])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ])
                                        self.level = None

                                        self.priority_limit_data = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData()
                                        self.priority_limit_data.parent = self
                                        self._children_name_map["priority_limit_data"] = "priority-limit-data"

                                        self.frr_type = YList(self)
                                        self._segment_path = lambda: "priority-limit" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit, ['level'], name, value)


                                    class PriorityLimitData(Entity):
                                        """
                                        Data container.
                                        
                                        .. attribute:: priority
                                        
                                        	Compute for all prefixes upto the specified priority
                                        	**type**\:  :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData, self).__init__()

                                            self.yang_name = "priority-limit-data"
                                            self.yang_parent_name = "priority-limit"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority', '')])),
                                            ])
                                            self.priority = None
                                            self._segment_path = lambda: "priority-limit-data"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.PriorityLimitData, ['priority'], name, value)


                                    class FrrType(Entity):
                                        """
                                        keys\: frr\-type
                                        
                                        .. attribute:: frr_type  (key)
                                        
                                        	Computation Type
                                        	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                        
                                        .. attribute:: priority
                                        
                                        	Compute for all prefixes upto the specified priority
                                        	**type**\:  :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.FrrType, self).__init__()

                                            self.yang_name = "frr-type"
                                            self.yang_parent_name = "priority-limit"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['frr_type']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                ('priority', (YLeaf(YType.enumeration, 'priority'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority', '')])),
                                            ])
                                            self.frr_type = None
                                            self.priority = None
                                            self._segment_path = lambda: "frr-type" + "[frr-type='" + str(self.frr_type) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit.FrrType, ['frr_type', 'priority'], name, value)


                            class FrrRemoteLfaPrefixes(Entity):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of  		 :py:class:`FrrRemoteLfaPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes, self).__init__()

                                    self.yang_name = "frr-remote-lfa-prefixes"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-remote-lfa-prefix", ("frr_remote_lfa_prefix", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix))])
                                    self._leafs = OrderedDict()

                                    self.frr_remote_lfa_prefix = YList(self)
                                    self._segment_path = lambda: "frr-remote-lfa-prefixes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes, [], name, value)


                                class FrrRemoteLfaPrefix(Entity):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\: str
                                    
                                    	**length:** 1..32
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, self).__init__()

                                        self.yang_name = "frr-remote-lfa-prefix"
                                        self.yang_parent_name = "frr-remote-lfa-prefixes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                                        ])
                                        self.level = None
                                        self.prefix_list_name = None
                                        self._segment_path = lambda: "frr-remote-lfa-prefix" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, ['level', 'prefix_list_name'], name, value)


                            class FrrTiebreakers(Entity):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of  		 :py:class:`FrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers, self).__init__()

                                    self.yang_name = "frr-tiebreakers"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-tiebreaker", ("frr_tiebreaker", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker))])
                                    self._leafs = OrderedDict()

                                    self.frr_tiebreaker = YList(self)
                                    self._segment_path = lambda: "frr-tiebreakers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers, [], name, value)


                                class FrrTiebreaker(Entity):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: tiebreaker  (key)
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\:  :py:class:`IsisfrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreaker>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker, self).__init__()

                                        self.yang_name = "frr-tiebreaker"
                                        self.yang_parent_name = "frr-tiebreakers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level','tiebreaker']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('tiebreaker', (YLeaf(YType.enumeration, 'tiebreaker'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisfrrTiebreaker', '')])),
                                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                        ])
                                        self.level = None
                                        self.tiebreaker = None
                                        self.index = None
                                        self._segment_path = lambda: "frr-tiebreaker" + "[level='" + str(self.level) + "']" + "[tiebreaker='" + str(self.tiebreaker) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                            class FrrUseCandOnlies(Entity):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of  		 :py:class:`FrrUseCandOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies, self).__init__()

                                    self.yang_name = "frr-use-cand-onlies"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("frr-use-cand-only", ("frr_use_cand_only", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly))])
                                    self._leafs = OrderedDict()

                                    self.frr_use_cand_only = YList(self)
                                    self._segment_path = lambda: "frr-use-cand-onlies"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies, [], name, value)


                                class FrrUseCandOnly(Entity):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: frr_type  (key)
                                    
                                    	Computation Type
                                    	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, self).__init__()

                                        self.yang_name = "frr-use-cand-only"
                                        self.yang_parent_name = "frr-use-cand-onlies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level','frr_type']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                        ])
                                        self.level = None
                                        self.frr_type = None
                                        self._segment_path = lambda: "frr-use-cand-only" + "[level='" + str(self.level) + "']" + "[frr-type='" + str(self.frr_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, ['level', 'frr_type'], name, value)


                        class RouterId(Entity):
                            """
                            Stable IP address for system. Will only be
                            applied for the unicast sub\-address\-family.
                            
                            .. attribute:: address
                            
                            	IPv4/IPv6 address to be used as a router ID. Precisely one of Address and Interface must be specified
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.RouterId, self).__init__()

                                self.yang_name = "router-id"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.address = None
                                self.interface_name = None
                                self._segment_path = lambda: "router-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.RouterId, ['address', 'interface_name'], name, value)


                        class SpfPrefixPriorities(Entity):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of  		 :py:class:`SpfPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities, self).__init__()

                                self.yang_name = "spf-prefix-priorities"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("spf-prefix-priority", ("spf_prefix_priority", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority))])
                                self._leafs = OrderedDict()

                                self.spf_prefix_priority = YList(self)
                                self._segment_path = lambda: "spf-prefix-priorities"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities, [], name, value)


                            class SpfPrefixPriority(Entity):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level  (key)
                                
                                	SPF Level for prefix prioritization
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_priority_type  (key)
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\:  :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority, self).__init__()

                                    self.yang_name = "spf-prefix-priority"
                                    self.yang_parent_name = "spf-prefix-priorities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level','prefix_priority_type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('prefix_priority_type', (YLeaf(YType.enumeration, 'prefix-priority-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisPrefixPriority', '')])),
                                        ('admin_tag', (YLeaf(YType.uint32, 'admin-tag'), ['int'])),
                                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                    ])
                                    self.level = None
                                    self.prefix_priority_type = None
                                    self.admin_tag = None
                                    self.access_list_name = None
                                    self._segment_path = lambda: "spf-prefix-priority" + "[level='" + str(self.level) + "']" + "[prefix-priority-type='" + str(self.prefix_priority_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority, ['level', 'prefix_priority_type', 'admin_tag', 'access_list_name'], name, value)


                        class SummaryPrefixes(Entity):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of  		 :py:class:`SummaryPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes, self).__init__()

                                self.yang_name = "summary-prefixes"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("summary-prefix", ("summary_prefix", Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix))])
                                self._leafs = OrderedDict()

                                self.summary_prefix = YList(self)
                                self._segment_path = lambda: "summary-prefixes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes, [], name, value)


                            class SummaryPrefix(Entity):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix  (key)
                                
                                	IP summary address prefix
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix, self).__init__()

                                    self.yang_name = "summary-prefix"
                                    self.yang_parent_name = "summary-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address_prefix']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_prefix', (YLeaf(YType.str, 'address-prefix'), ['str','str'])),
                                        ('tag', (YLeaf(YType.uint32, 'tag'), ['int'])),
                                        ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                    ])
                                    self.address_prefix = None
                                    self.tag = None
                                    self.level = None
                                    self._segment_path = lambda: "summary-prefix" + "[address-prefix='" + str(self.address_prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix, ['address_prefix', 'tag', 'level'], name, value)


                        class MicroLoopAvoidance(Entity):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\:  :py:class:`IsisMicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidance>`
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\: int
                            
                            	**range:** 1000..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 5000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance, self).__init__()

                                self.yang_name = "micro-loop-avoidance"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.enumeration, 'enable'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMicroLoopAvoidance', '')])),
                                    ('rib_update_delay', (YLeaf(YType.uint32, 'rib-update-delay'), ['int'])),
                                ])
                                self.enable = None
                                self.rib_update_delay = None
                                self._segment_path = lambda: "micro-loop-avoidance"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance, ['enable', 'rib_update_delay'], name, value)


                        class Ucmp(Entity):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\:  :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\:  :py:class:`ExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces>`
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\: int
                            
                            	**range:** 100..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 100
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp, self).__init__()

                                self.yang_name = "ucmp"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("enable", ("enable", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable)), ("exclude-interfaces", ("exclude_interfaces", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces))])
                                self._leafs = OrderedDict([
                                    ('delay_interval', (YLeaf(YType.uint32, 'delay-interval'), ['int'])),
                                ])
                                self.delay_interval = None

                                self.enable = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable()
                                self.enable.parent = self
                                self._children_name_map["enable"] = "enable"

                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self
                                self._children_name_map["exclude_interfaces"] = "exclude-interfaces"
                                self._segment_path = lambda: "ucmp"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp, ['delay_interval'], name, value)


                            class Enable(Entity):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\: int
                                
                                	**range:** 101..10000
                                
                                	**default value**\: 200
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable, self).__init__()

                                    self.yang_name = "enable"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                                    ])
                                    self.variance = None
                                    self.prefix_list_name = None
                                    self._segment_path = lambda: "enable"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable, ['variance', 'prefix_list_name'], name, value)


                            class ExcludeInterfaces(Entity):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of  		 :py:class:`ExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces, self).__init__()

                                    self.yang_name = "exclude-interfaces"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("exclude-interface", ("exclude_interface", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface))])
                                    self._leafs = OrderedDict()

                                    self.exclude_interface = YList(self)
                                    self._segment_path = lambda: "exclude-interfaces"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces, [], name, value)


                                class ExcludeInterface(Entity):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Name of the interface to be excluded
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface, self).__init__()

                                        self.yang_name = "exclude-interface"
                                        self.yang_parent_name = "exclude-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ])
                                        self.interface_name = None
                                        self._segment_path = lambda: "exclude-interface" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface, ['interface_name'], name, value)


                        class MaxRedistPrefixes(Entity):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of  		 :py:class:`MaxRedistPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes, self).__init__()

                                self.yang_name = "max-redist-prefixes"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("max-redist-prefix", ("max_redist_prefix", Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix))])
                                self._leafs = OrderedDict()

                                self.max_redist_prefix = YList(self)
                                self._segment_path = lambda: "max-redist-prefixes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes, [], name, value)


                            class MaxRedistPrefix(Entity):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\: int
                                
                                	**range:** 1..28000
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix, self).__init__()

                                    self.yang_name = "max-redist-prefix"
                                    self.yang_parent_name = "max-redist-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('prefix_limit', (YLeaf(YType.uint32, 'prefix-limit'), ['int'])),
                                    ])
                                    self.level = None
                                    self.prefix_limit = None
                                    self._segment_path = lambda: "max-redist-prefix" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix, ['level', 'prefix_limit'], name, value)


                        class Propagations(Entity):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of  		 :py:class:`Propagation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations, self).__init__()

                                self.yang_name = "propagations"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("propagation", ("propagation", Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation))])
                                self._leafs = OrderedDict()

                                self.propagation = YList(self)
                                self._segment_path = lambda: "propagations"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations, [], name, value)


                            class Propagation(Entity):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: source_level  (key)
                                
                                	Source level for routes
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: destination_level  (key)
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\: str
                                
                                	**length:** 1..64
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation, self).__init__()

                                    self.yang_name = "propagation"
                                    self.yang_parent_name = "propagations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['source_level','destination_level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('source_level', (YLeaf(YType.enumeration, 'source-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('destination_level', (YLeaf(YType.enumeration, 'destination-level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                    ])
                                    self.source_level = None
                                    self.destination_level = None
                                    self.route_policy_name = None
                                    self._segment_path = lambda: "propagation" + "[source-level='" + str(self.source_level) + "']" + "[destination-level='" + str(self.destination_level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation, ['source_level', 'destination_level', 'route_policy_name'], name, value)


                        class Redistributions(Entity):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of  		 :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions, self).__init__()

                                self.yang_name = "redistributions"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("redistribution", ("redistribution", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution))])
                                self._leafs = OrderedDict()

                                self.redistribution = YList(self)
                                self._segment_path = lambda: "redistributions"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions, [], name, value)


                            class Redistribution(Entity):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name  (key)
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\:  :py:class:`IsisRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProto>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\:  :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of  		 :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of  		 :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of  		 :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution, self).__init__()

                                    self.yang_name = "redistribution"
                                    self.yang_parent_name = "redistributions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['protocol_name']
                                    self._child_classes = OrderedDict([("connected-or-static-or-rip-or-subscriber-or-mobile", ("connected_or_static_or_rip_or_subscriber_or_mobile", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile)), ("ospf-or-ospfv3-or-isis-or-application", ("ospf_or_ospfv3_or_isis_or_application", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication)), ("bgp", ("bgp", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp)), ("eigrp", ("eigrp", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp))])
                                    self._leafs = OrderedDict([
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRedistProto', '')])),
                                    ])
                                    self.protocol_name = None

                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self._children_name_map["connected_or_static_or_rip_or_subscriber_or_mobile"] = "connected-or-static-or-rip-or-subscriber-or-mobile"

                                    self.ospf_or_ospfv3_or_isis_or_application = YList(self)
                                    self.bgp = YList(self)
                                    self.eigrp = YList(self)
                                    self._segment_path = lambda: "redistribution" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution, ['protocol_name'], name, value)


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(Entity):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, self).__init__()

                                        self.yang_name = "connected-or-static-or-rip-or-subscriber-or-mobile"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "connected-or-static-or-rip-or-subscriber-or-mobile"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, ['metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                                class OspfOrOspfv3OrIsisOrApplication(Entity):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name  (key)
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, self).__init__()

                                        self.yang_name = "ospf-or-ospfv3-or-isis-or-application"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['instance_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.instance_name = None
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "ospf-or-ospfv3-or-isis-or-application" + "[instance-name='" + str(self.instance_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, ['instance_name', 'metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                                class Bgp(Entity):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  (key)
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','as_yy']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "bgp" + "[as-xx='" + str(self.as_xx) + "']" + "[as-yy='" + str(self.as_yy) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp, ['as_xx', 'as_yy', 'metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                                class Eigrp(Entity):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz  (key)
                                    
                                    	Eigrp as number
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\: int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:  :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp, self).__init__()

                                        self.yang_name = "eigrp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_zz']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_zz', (YLeaf(YType.uint32, 'as-zz'), ['int'])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('levels', (YLeaf(YType.enumeration, 'levels'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                                            ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                            ('metric_type', (YLeaf(YType.enumeration, 'metric-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMetric', '')])),
                                            ('ospf_route_type', (YLeaf(YType.uint32, 'ospf-route-type'), ['int'])),
                                        ])
                                        self.as_zz = None
                                        self.metric = None
                                        self.levels = None
                                        self.route_policy_name = None
                                        self.metric_type = None
                                        self.ospf_route_type = None
                                        self._segment_path = lambda: "eigrp" + "[as-zz='" + str(self.as_zz) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp, ['as_zz', 'metric', 'levels', 'route_policy_name', 'metric_type', 'ospf_route_type'], name, value)


                        class ApplicationTables(Entity):
                            """
                            Advertise application specific values
                            
                            .. attribute:: application_table
                            
                            	Application Name
                            	**type**\: list of  		 :py:class:`ApplicationTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables, self).__init__()

                                self.yang_name = "application-tables"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("application-table", ("application_table", Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable))])
                                self._leafs = OrderedDict()

                                self.application_table = YList(self)
                                self._segment_path = lambda: "application-tables"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables, [], name, value)


                            class ApplicationTable(Entity):
                                """
                                Application Name
                                
                                .. attribute:: app_type  (key)
                                
                                	Application Type
                                	**type**\:  :py:class:`IsisApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplication>`
                                
                                .. attribute:: attribute_table
                                
                                	Attribute Name
                                	**type**\: list of  		 :py:class:`AttributeTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable, self).__init__()

                                    self.yang_name = "application-table"
                                    self.yang_parent_name = "application-tables"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['app_type']
                                    self._child_classes = OrderedDict([("attribute-table", ("attribute_table", Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable))])
                                    self._leafs = OrderedDict([
                                        ('app_type', (YLeaf(YType.enumeration, 'app-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplication', '')])),
                                    ])
                                    self.app_type = None

                                    self.attribute_table = YList(self)
                                    self._segment_path = lambda: "application-table" + "[app-type='" + str(self.app_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable, ['app_type'], name, value)


                                class AttributeTable(Entity):
                                    """
                                    Attribute Name
                                    
                                    .. attribute:: app_type  (key)
                                    
                                    	Application Type
                                    	**type**\:  :py:class:`IsisApplicationAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplicationAttribute>`
                                    
                                    .. attribute:: enable
                                    
                                    	If TRUE, advertise application link attribute in our LSP
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable, self).__init__()

                                        self.yang_name = "attribute-table"
                                        self.yang_parent_name = "application-table"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['app_type']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('app_type', (YLeaf(YType.enumeration, 'app-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisApplicationAttribute', '')])),
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                        ])
                                        self.app_type = None
                                        self.enable = None
                                        self._segment_path = lambda: "attribute-table" + "[app-type='" + str(self.app_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ApplicationTables.ApplicationTable.AttributeTable, ['app_type', 'enable'], name, value)


                        class SpfPeriodicIntervals(Entity):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of  		 :py:class:`SpfPeriodicInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals, self).__init__()

                                self.yang_name = "spf-periodic-intervals"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("spf-periodic-interval", ("spf_periodic_interval", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval))])
                                self._leafs = OrderedDict()

                                self.spf_periodic_interval = YList(self)
                                self._segment_path = lambda: "spf-periodic-intervals"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals, [], name, value)


                            class SpfPeriodicInterval(Entity):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\: int
                                
                                	**range:** 0..3600
                                
                                	**mandatory**\: True
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval, self).__init__()

                                    self.yang_name = "spf-periodic-interval"
                                    self.yang_parent_name = "spf-periodic-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('periodic_interval', (YLeaf(YType.uint32, 'periodic-interval'), ['int'])),
                                    ])
                                    self.level = None
                                    self.periodic_interval = None
                                    self._segment_path = lambda: "spf-periodic-interval" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval, ['level', 'periodic_interval'], name, value)


                        class DistributeListIn(Entity):
                            """
                            Filter routes sent to the RIB
                            
                            .. attribute:: prefix_list_name
                            
                            	Prefix list to control routes installed in RIB
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: route_policy_name
                            
                            	Route policy to control routes installed in RIB
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn, self).__init__()

                                self.yang_name = "distribute-list-in"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix_list_name', (YLeaf(YType.str, 'prefix-list-name'), ['str'])),
                                    ('route_policy_name', (YLeaf(YType.str, 'route-policy-name'), ['str'])),
                                ])
                                self.prefix_list_name = None
                                self.route_policy_name = None
                                self._segment_path = lambda: "distribute-list-in"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.DistributeListIn, ['prefix_list_name', 'route_policy_name'], name, value)


                        class SpfIntervals(Entity):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of  		 :py:class:`SpfInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals, self).__init__()

                                self.yang_name = "spf-intervals"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("spf-interval", ("spf_interval", Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval))])
                                self._leafs = OrderedDict()

                                self.spf_interval = YList(self)
                                self._segment_path = lambda: "spf-intervals"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals, [], name, value)


                            class SpfInterval(Entity):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\: int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval, self).__init__()

                                    self.yang_name = "spf-interval"
                                    self.yang_parent_name = "spf-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('maximum_wait', (YLeaf(YType.uint32, 'maximum-wait'), ['int'])),
                                        ('initial_wait', (YLeaf(YType.uint32, 'initial-wait'), ['int'])),
                                        ('secondary_wait', (YLeaf(YType.uint32, 'secondary-wait'), ['int'])),
                                    ])
                                    self.level = None
                                    self.maximum_wait = None
                                    self.initial_wait = None
                                    self.secondary_wait = None
                                    self._segment_path = lambda: "spf-interval" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval, ['level', 'maximum_wait', 'initial_wait', 'secondary_wait'], name, value)


                        class MonitorConvergence(Entity):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\: str
                            
                            	**length:** 1..32
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence, self).__init__()

                                self.yang_name = "monitor-convergence"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ('track_ip_frr', (YLeaf(YType.empty, 'track-ip-frr'), ['Empty'])),
                                    ('prefix_list', (YLeaf(YType.str, 'prefix-list'), ['str'])),
                                ])
                                self.enable = None
                                self.track_ip_frr = None
                                self.prefix_list = None
                                self._segment_path = lambda: "monitor-convergence"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence, ['enable', 'track_ip_frr', 'prefix_list'], name, value)


                        class DefaultInformation(Entity):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\: bool
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation, self).__init__()

                                self.yang_name = "default-information"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('use_policy', (YLeaf(YType.boolean, 'use-policy'), ['bool'])),
                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                    ('external', (YLeaf(YType.empty, 'external'), ['Empty'])),
                                ])
                                self.use_policy = None
                                self.policy_name = None
                                self.external = None
                                self._segment_path = lambda: "default-information"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation, ['use_policy', 'policy_name', 'external'], name, value)


                        class AdminDistances(Entity):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of  		 :py:class:`AdminDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances, self).__init__()

                                self.yang_name = "admin-distances"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("admin-distance", ("admin_distance", Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance))])
                                self._leafs = OrderedDict()

                                self.admin_distance = YList(self)
                                self._segment_path = lambda: "admin-distances"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances, [], name, value)


                            class AdminDistance(Entity):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix  (key)
                                
                                	IP route source prefix
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                	**mandatory**\: True
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance, self).__init__()

                                    self.yang_name = "admin-distance"
                                    self.yang_parent_name = "admin-distances"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['address_prefix']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address_prefix', (YLeaf(YType.str, 'address-prefix'), ['str','str'])),
                                        ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                                        ('prefix_list', (YLeaf(YType.str, 'prefix-list'), ['str'])),
                                    ])
                                    self.address_prefix = None
                                    self.distance = None
                                    self.prefix_list = None
                                    self._segment_path = lambda: "admin-distance" + "[address-prefix='" + str(self.address_prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance, ['address_prefix', 'distance', 'prefix_list'], name, value)


                        class Ispf(Entity):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\:  :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf, self).__init__()

                                self.yang_name = "ispf"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("states", ("states", Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States))])
                                self._leafs = OrderedDict()

                                self.states = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States()
                                self.states.parent = self
                                self._children_name_map["states"] = "states"
                                self._segment_path = lambda: "ispf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf, [], name, value)


                            class States(Entity):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of  		 :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States, self).__init__()

                                    self.yang_name = "states"
                                    self.yang_parent_name = "ispf"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("state", ("state", Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State))])
                                    self._leafs = OrderedDict()

                                    self.state = YList(self)
                                    self._segment_path = lambda: "states"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States, [], name, value)


                                class State(Entity):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level  (key)
                                    
                                    	Level to which configuration applies
                                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:  :py:class:`IsisispfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisispfState>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "states"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['level']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisispfState', '')])),
                                        ])
                                        self.level = None
                                        self.state = None
                                        self._segment_path = lambda: "state" + "[level='" + str(self.level) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State, ['level', 'state'], name, value)


                        class MplsLdpGlobal(Entity):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal, self).__init__()

                                self.yang_name = "mpls-ldp-global"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('auto_config', (YLeaf(YType.boolean, 'auto-config'), ['bool'])),
                                ])
                                self.auto_config = None
                                self._segment_path = lambda: "mpls-ldp-global"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal, ['auto_config'], name, value)


                        class Mpls(Entity):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:  :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\:  :py:class:`Level <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level>`
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls, self).__init__()

                                self.yang_name = "mpls"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("router-id", ("router_id", Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId)), ("level", ("level", Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level))])
                                self._leafs = OrderedDict([
                                    ('igp_intact', (YLeaf(YType.empty, 'igp-intact'), ['Empty'])),
                                    ('multicast_intact', (YLeaf(YType.empty, 'multicast-intact'), ['Empty'])),
                                ])
                                self.igp_intact = None
                                self.multicast_intact = None

                                self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId()
                                self.router_id.parent = self
                                self._children_name_map["router_id"] = "router-id"

                                self.level = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level()
                                self.level.parent = self
                                self._children_name_map["level"] = "level"
                                self._segment_path = lambda: "mpls"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls, ['igp_intact', 'multicast_intact'], name, value)


                            class RouterId(Entity):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId, self).__init__()

                                    self.yang_name = "router-id"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ])
                                    self.address = None
                                    self.interface_name = None
                                    self._segment_path = lambda: "router-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId, ['address', 'interface_name'], name, value)


                            class Level(Entity):
                                """
                                Enable MPLS for an IS\-IS at the given
                                levels
                                
                                .. attribute:: level1
                                
                                	Level 1 enabled
                                	**type**\: bool
                                
                                .. attribute:: level2
                                
                                	Level 2 enabled
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level, self).__init__()

                                    self.yang_name = "level"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level1', (YLeaf(YType.boolean, 'level1'), ['bool'])),
                                        ('level2', (YLeaf(YType.boolean, 'level2'), ['bool'])),
                                    ])
                                    self.level1 = None
                                    self.level2 = None
                                    self._segment_path = lambda: "level"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level, ['level1', 'level2'], name, value)


                        class ManualAdjSids(Entity):
                            """
                            Manual Adjacecy SID configuration
                            
                            .. attribute:: manual_adj_sid
                            
                            	Assign adjancency SID to an interface
                            	**type**\: list of  		 :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids, self).__init__()

                                self.yang_name = "manual-adj-sids"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("manual-adj-sid", ("manual_adj_sid", Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid))])
                                self._leafs = OrderedDict()

                                self.manual_adj_sid = YList(self)
                                self._segment_path = lambda: "manual-adj-sids"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids, [], name, value)


                            class ManualAdjSid(Entity):
                                """
                                Assign adjancency SID to an interface
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: sid_type  (key)
                                
                                	Sid type aboslute or index
                                	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                
                                .. attribute:: sid  (key)
                                
                                	Sid value
                                	**type**\: int
                                
                                	**range:** 0..1048575
                                
                                .. attribute:: protected
                                
                                	Enable/Disable SID protection
                                	**type**\:  :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid, self).__init__()

                                    self.yang_name = "manual-adj-sid"
                                    self.yang_parent_name = "manual-adj-sids"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level','sid_type','sid']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                        ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                        ('protected', (YLeaf(YType.enumeration, 'protected'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected', '')])),
                                    ])
                                    self.level = None
                                    self.sid_type = None
                                    self.sid = None
                                    self.protected = None
                                    self._segment_path = lambda: "manual-adj-sid" + "[level='" + str(self.level) + "']" + "[sid-type='" + str(self.sid_type) + "']" + "[sid='" + str(self.sid) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                        class Metrics(Entity):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of  		 :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics, self).__init__()

                                self.yang_name = "metrics"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric", ("metric", Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric))])
                                self._leafs = OrderedDict()

                                self.metric = YList(self)
                                self._segment_path = lambda: "metrics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics, [], name, value)


                            class Metric(Entity):
                                """
                                Metric configuration. Legal value depends on
                                the metric\-style specified for the topology. If
                                the metric\-style defined is narrow, then only a
                                value between <1\-63> is allowed and if the
                                metric\-style is defined as wide, then a value
                                between <1\-16777215> is allowed as the metric
                                value.  All routers exclude links with the
                                maximum wide metric (16777215) from their SPF
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: union of the below types:
                                
                                		**type**\:  :py:class:`Metric_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_>`
                                
                                		**type**\: int
                                
                                			**range:** 1..16777215
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric, self).__init__()

                                    self.yang_name = "metric"
                                    self.yang_parent_name = "metrics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('metric', (YLeaf(YType.str, 'metric'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis', 'Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_'),'int'])),
                                    ])
                                    self.level = None
                                    self.metric = None
                                    self._segment_path = lambda: "metric" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric, ['level', 'metric'], name, value)

                                class Metric_(Enum):
                                    """
                                    Metric\_ (Enum Class)

                                    Allowed metric\: <1\-63> for narrow,

                                    <1\-16777215> for wide

                                    .. data:: maximum = 16777215

                                    	Maximum wide metric.  All routers will

                                    	exclude this link from their SPF

                                    """

                                    maximum = Enum.YLeaf(16777215, "maximum")



                        class Weights(Entity):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of  		 :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Weights, self).__init__()

                                self.yang_name = "weights"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("weight", ("weight", Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight))])
                                self._leafs = OrderedDict()

                                self.weight = YList(self)
                                self._segment_path = lambda: "weights"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Weights, [], name, value)


                            class Weight(Entity):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level  (key)
                                
                                	Level to which configuration applies
                                	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\: int
                                
                                	**range:** 1..16777214
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight, self).__init__()

                                    self.yang_name = "weight"
                                    self.yang_parent_name = "weights"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['level']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                        ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                                    ])
                                    self.level = None
                                    self.weight = None
                                    self._segment_path = lambda: "weight" + "[level='" + str(self.level) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight, ['level', 'weight'], name, value)


            class LspRefreshIntervals(Entity):
                """
                LSP refresh\-interval configuration
                
                .. attribute:: lsp_refresh_interval
                
                	Interval between re\-flooding of unchanged LSPs
                	**type**\: list of  		 :py:class:`LspRefreshInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspRefreshIntervals, self).__init__()

                    self.yang_name = "lsp-refresh-intervals"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-refresh-interval", ("lsp_refresh_interval", Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval))])
                    self._leafs = OrderedDict()

                    self.lsp_refresh_interval = YList(self)
                    self._segment_path = lambda: "lsp-refresh-intervals"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspRefreshIntervals, [], name, value)


                class LspRefreshInterval(Entity):
                    """
                    Interval between re\-flooding of unchanged
                    LSPs
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: interval
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval, self).__init__()

                        self.yang_name = "lsp-refresh-interval"
                        self.yang_parent_name = "lsp-refresh-intervals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ])
                        self.level = None
                        self.interval = None
                        self._segment_path = lambda: "lsp-refresh-interval" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval, ['level', 'interval'], name, value)


            class Distribute(Entity):
                """
                Distribute link\-state configuration
                
                .. attribute:: dist_inst_id
                
                	Instance ID
                	**type**\: int
                
                	**range:** 32..4294967295
                
                .. attribute:: level
                
                	Level
                	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                
                .. attribute:: dist_throttle
                
                	Seconds
                	**type**\: int
                
                	**range:** 1..20
                
                	**units**\: second
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.Distribute, self).__init__()

                    self.yang_name = "distribute"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('dist_inst_id', (YLeaf(YType.uint32, 'dist-inst-id'), ['int'])),
                        ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                        ('dist_throttle', (YLeaf(YType.uint32, 'dist-throttle'), ['int'])),
                    ])
                    self.dist_inst_id = None
                    self.level = None
                    self.dist_throttle = None
                    self._segment_path = lambda: "distribute"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Distribute, ['dist_inst_id', 'level', 'dist_throttle'], name, value)


            class FlexAlgos(Entity):
                """
                Flex\-Algo Table
                
                .. attribute:: flex_algo
                
                	Configuration for an IS\-IS Flex\-Algo
                	**type**\: list of  		 :py:class:`FlexAlgo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.FlexAlgos.FlexAlgo>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.FlexAlgos, self).__init__()

                    self.yang_name = "flex-algos"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("flex-algo", ("flex_algo", Isis.Instances.Instance.FlexAlgos.FlexAlgo))])
                    self._leafs = OrderedDict()

                    self.flex_algo = YList(self)
                    self._segment_path = lambda: "flex-algos"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.FlexAlgos, [], name, value)


                class FlexAlgo(Entity):
                    """
                    Configuration for an IS\-IS Flex\-Algo
                    
                    .. attribute:: flex_algo  (key)
                    
                    	Flex Algo
                    	**type**\: int
                    
                    	**range:** 128..255
                    
                    .. attribute:: affinity_exclude_anies
                    
                    	Set the exclude\-any affinity
                    	**type**\:  :py:class:`AffinityExcludeAnies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies>`
                    
                    .. attribute:: running
                    
                    	This object must be set before any other configuration is supplied for an interface, and must be the last per\-interface configuration object to be removed
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: metric_type
                    
                    	Set the Flex\-Algo metric\-type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: priority
                    
                    	Set the Flex\-Algo priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.FlexAlgos.FlexAlgo, self).__init__()

                        self.yang_name = "flex-algo"
                        self.yang_parent_name = "flex-algos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['flex_algo']
                        self._child_classes = OrderedDict([("affinity-exclude-anies", ("affinity_exclude_anies", Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies))])
                        self._leafs = OrderedDict([
                            ('flex_algo', (YLeaf(YType.uint32, 'flex-algo'), ['int'])),
                            ('running', (YLeaf(YType.empty, 'running'), ['Empty'])),
                            ('metric_type', (YLeaf(YType.uint32, 'metric-type'), ['int'])),
                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                        ])
                        self.flex_algo = None
                        self.running = None
                        self.metric_type = None
                        self.priority = None

                        self.affinity_exclude_anies = Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies()
                        self.affinity_exclude_anies.parent = self
                        self._children_name_map["affinity_exclude_anies"] = "affinity-exclude-anies"
                        self._segment_path = lambda: "flex-algo" + "[flex-algo='" + str(self.flex_algo) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.FlexAlgos.FlexAlgo, ['flex_algo', 'running', 'metric_type', 'priority'], name, value)


                    class AffinityExcludeAnies(Entity):
                        """
                        Set the exclude\-any affinity
                        
                        .. attribute:: affinity_exclude_any
                        
                        	Array of Attribute Names
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies, self).__init__()

                            self.yang_name = "affinity-exclude-anies"
                            self.yang_parent_name = "flex-algo"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('affinity_exclude_any', (YLeafList(YType.str, 'affinity-exclude-any'), ['str'])),
                            ])
                            self.affinity_exclude_any = []
                            self._segment_path = lambda: "affinity-exclude-anies"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.FlexAlgos.FlexAlgo.AffinityExcludeAnies, ['affinity_exclude_any'], name, value)


            class AffinityMappings(Entity):
                """
                Affinity Mapping Table
                
                .. attribute:: affinity_mapping
                
                	Affinity Mapping configuration
                	**type**\: list of  		 :py:class:`AffinityMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.AffinityMappings.AffinityMapping>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.AffinityMappings, self).__init__()

                    self.yang_name = "affinity-mappings"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("affinity-mapping", ("affinity_mapping", Isis.Instances.Instance.AffinityMappings.AffinityMapping))])
                    self._leafs = OrderedDict()

                    self.affinity_mapping = YList(self)
                    self._segment_path = lambda: "affinity-mappings"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.AffinityMappings, [], name, value)


                class AffinityMapping(Entity):
                    """
                    Affinity Mapping configuration
                    
                    .. attribute:: affinity_name  (key)
                    
                    	Affinity Name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: value
                    
                    	Bit position
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.AffinityMappings.AffinityMapping, self).__init__()

                        self.yang_name = "affinity-mapping"
                        self.yang_parent_name = "affinity-mappings"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['affinity_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('affinity_name', (YLeaf(YType.str, 'affinity-name'), ['str'])),
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                        ])
                        self.affinity_name = None
                        self.value = None
                        self._segment_path = lambda: "affinity-mapping" + "[affinity-name='" + str(self.affinity_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.AffinityMappings.AffinityMapping, ['affinity_name', 'value'], name, value)


            class LspAcceptPasswords(Entity):
                """
                LSP/SNP accept password configuration
                
                .. attribute:: lsp_accept_password
                
                	LSP/SNP accept passwords. This requires the existence of an LSPPassword of the same level 
                	**type**\: list of  		 :py:class:`LspAcceptPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspAcceptPasswords, self).__init__()

                    self.yang_name = "lsp-accept-passwords"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-accept-password", ("lsp_accept_password", Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword))])
                    self._leafs = OrderedDict()

                    self.lsp_accept_password = YList(self)
                    self._segment_path = lambda: "lsp-accept-passwords"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspAcceptPasswords, [], name, value)


                class LspAcceptPassword(Entity):
                    """
                    LSP/SNP accept passwords. This requires the
                    existence of an LSPPassword of the same level
                    .
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: password
                    
                    	Password
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword, self).__init__()

                        self.yang_name = "lsp-accept-password"
                        self.yang_parent_name = "lsp-accept-passwords"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('password', (YLeaf(YType.str, 'password'), ['str'])),
                        ])
                        self.level = None
                        self.password = None
                        self._segment_path = lambda: "lsp-accept-password" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword, ['level', 'password'], name, value)


            class LspMtus(Entity):
                """
                LSP MTU configuration
                
                .. attribute:: lsp_mtu
                
                	LSP MTU
                	**type**\: list of  		 :py:class:`LspMtu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus.LspMtu>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspMtus, self).__init__()

                    self.yang_name = "lsp-mtus"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-mtu", ("lsp_mtu", Isis.Instances.Instance.LspMtus.LspMtu))])
                    self._leafs = OrderedDict()

                    self.lsp_mtu = YList(self)
                    self._segment_path = lambda: "lsp-mtus"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspMtus, [], name, value)


                class LspMtu(Entity):
                    """
                    LSP MTU
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: mtu
                    
                    	Bytes
                    	**type**\: int
                    
                    	**range:** 128..4352
                    
                    	**mandatory**\: True
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspMtus.LspMtu, self).__init__()

                        self.yang_name = "lsp-mtu"
                        self.yang_parent_name = "lsp-mtus"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                        ])
                        self.level = None
                        self.mtu = None
                        self._segment_path = lambda: "lsp-mtu" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspMtus.LspMtu, ['level', 'mtu'], name, value)


            class SrlgTable(Entity):
                """
                SRLG configuration
                
                .. attribute:: srlg_names
                
                	SRLG named configuration
                	**type**\:  :py:class:`SrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.SrlgTable.SrlgNames>`
                
                .. attribute:: srlg_admin_weight_default
                
                	Configure Default SRLG Admin Weight
                	**type**\: int
                
                	**range:** 0..16777215
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.SrlgTable, self).__init__()

                    self.yang_name = "srlg-table"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("srlg-names", ("srlg_names", Isis.Instances.Instance.SrlgTable.SrlgNames))])
                    self._leafs = OrderedDict([
                        ('srlg_admin_weight_default', (YLeaf(YType.uint32, 'srlg-admin-weight-default'), ['int'])),
                    ])
                    self.srlg_admin_weight_default = None

                    self.srlg_names = Isis.Instances.Instance.SrlgTable.SrlgNames()
                    self.srlg_names.parent = self
                    self._children_name_map["srlg_names"] = "srlg-names"
                    self._segment_path = lambda: "srlg-table"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.SrlgTable, ['srlg_admin_weight_default'], name, value)


                class SrlgNames(Entity):
                    """
                    SRLG named configuration
                    
                    .. attribute:: srlg_name
                    
                    	Configuration for an IS\-IS SRLG
                    	**type**\: list of  		 :py:class:`SrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.SrlgTable.SrlgNames, self).__init__()

                        self.yang_name = "srlg-names"
                        self.yang_parent_name = "srlg-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("srlg-name", ("srlg_name", Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName))])
                        self._leafs = OrderedDict()

                        self.srlg_name = YList(self)
                        self._segment_path = lambda: "srlg-names"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.SrlgTable.SrlgNames, [], name, value)


                    class SrlgName(Entity):
                        """
                        Configuration for an IS\-IS SRLG
                        
                        .. attribute:: srlg_name  (key)
                        
                        	Srlg name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: from_tos
                        
                        	Configure Static Remote SRLG
                        	**type**\:  :py:class:`FromTos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos>`
                        
                        .. attribute:: admin_weight
                        
                        	Configure SRLG Admin Weight
                        	**type**\: int
                        
                        	**range:** 0..16777215
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName, self).__init__()

                            self.yang_name = "srlg-name"
                            self.yang_parent_name = "srlg-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['srlg_name']
                            self._child_classes = OrderedDict([("from-tos", ("from_tos", Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos))])
                            self._leafs = OrderedDict([
                                ('srlg_name', (YLeaf(YType.str, 'srlg-name'), ['str'])),
                                ('admin_weight', (YLeaf(YType.uint32, 'admin-weight'), ['int'])),
                            ])
                            self.srlg_name = None
                            self.admin_weight = None

                            self.from_tos = Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos()
                            self.from_tos.parent = self
                            self._children_name_map["from_tos"] = "from-tos"
                            self._segment_path = lambda: "srlg-name" + "[srlg-name='" + str(self.srlg_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName, ['srlg_name', 'admin_weight'], name, value)


                        class FromTos(Entity):
                            """
                            Configure Static Remote SRLG
                            
                            .. attribute:: from_to
                            
                            	Local and remote addresses of a link
                            	**type**\: list of  		 :py:class:`FromTo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos, self).__init__()

                                self.yang_name = "from-tos"
                                self.yang_parent_name = "srlg-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("from-to", ("from_to", Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo))])
                                self._leafs = OrderedDict()

                                self.from_to = YList(self)
                                self._segment_path = lambda: "from-tos"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos, [], name, value)


                            class FromTo(Entity):
                                """
                                Local and remote addresses of a link
                                
                                .. attribute:: local_ipv4_address  (key)
                                
                                	Local IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: remote_ipv4_address  (key)
                                
                                	Remote IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo, self).__init__()

                                    self.yang_name = "from-to"
                                    self.yang_parent_name = "from-tos"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['local_ipv4_address','remote_ipv4_address']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('local_ipv4_address', (YLeaf(YType.str, 'local-ipv4-address'), ['str'])),
                                        ('remote_ipv4_address', (YLeaf(YType.str, 'remote-ipv4-address'), ['str'])),
                                    ])
                                    self.local_ipv4_address = None
                                    self.remote_ipv4_address = None
                                    self._segment_path = lambda: "from-to" + "[local-ipv4-address='" + str(self.local_ipv4_address) + "']" + "[remote-ipv4-address='" + str(self.remote_ipv4_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.SrlgTable.SrlgNames.SrlgName.FromTos.FromTo, ['local_ipv4_address', 'remote_ipv4_address'], name, value)


            class Nsf(Entity):
                """
                IS\-IS NSF configuration
                
                .. attribute:: flavor
                
                	NSF not configured if item is deleted
                	**type**\:  :py:class:`IsisNsfFlavor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisNsfFlavor>`
                
                .. attribute:: interface_timer
                
                	Per\-interface time period to wait for a restart ACK during an IETF\-NSF restart. This configuration has no effect if IETF\-NSF is not configured
                	**type**\: int
                
                	**range:** 1..20
                
                	**units**\: second
                
                	**default value**\: 1
                
                .. attribute:: max_interface_timer_expiry
                
                	Maximum number of times an interface timer may expire during an IETF\-NSF restart before the NSF restart is aborted. This configuration has no effect if IETF NSF is not configured
                	**type**\: int
                
                	**range:** 1..10
                
                	**default value**\: 10
                
                .. attribute:: lifetime
                
                	Maximum route lifetime following restart. When this lifetime expires, old routes will be purged from the RIB
                	**type**\: int
                
                	**range:** 5..300
                
                	**units**\: second
                
                	**default value**\: 90
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.Nsf, self).__init__()

                    self.yang_name = "nsf"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('flavor', (YLeaf(YType.enumeration, 'flavor'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisNsfFlavor', '')])),
                        ('interface_timer', (YLeaf(YType.uint32, 'interface-timer'), ['int'])),
                        ('max_interface_timer_expiry', (YLeaf(YType.uint32, 'max-interface-timer-expiry'), ['int'])),
                        ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                    ])
                    self.flavor = None
                    self.interface_timer = None
                    self.max_interface_timer_expiry = None
                    self.lifetime = None
                    self._segment_path = lambda: "nsf"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Nsf, ['flavor', 'interface_timer', 'max_interface_timer_expiry', 'lifetime'], name, value)


            class LinkGroups(Entity):
                """
                Link Group
                
                .. attribute:: link_group
                
                	Configuration for link group name
                	**type**\: list of  		 :py:class:`LinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups.LinkGroup>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LinkGroups, self).__init__()

                    self.yang_name = "link-groups"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("link-group", ("link_group", Isis.Instances.Instance.LinkGroups.LinkGroup))])
                    self._leafs = OrderedDict()

                    self.link_group = YList(self)
                    self._segment_path = lambda: "link-groups"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LinkGroups, [], name, value)


                class LinkGroup(Entity):
                    """
                    Configuration for link group name
                    
                    .. attribute:: link_group_name  (key)
                    
                    	Link Group Name
                    	**type**\: str
                    
                    	**length:** 1..40
                    
                    .. attribute:: metric_offset
                    
                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                    	**type**\: int
                    
                    	**range:** 0..16777215
                    
                    .. attribute:: revert_members
                    
                    	Revert Members
                    	**type**\: int
                    
                    	**range:** 2..64
                    
                    	**default value**\: 2
                    
                    .. attribute:: minimum_members
                    
                    	Minimum Members
                    	**type**\: int
                    
                    	**range:** 2..64
                    
                    	**default value**\: 2
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LinkGroups.LinkGroup, self).__init__()

                        self.yang_name = "link-group"
                        self.yang_parent_name = "link-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['link_group_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('link_group_name', (YLeaf(YType.str, 'link-group-name'), ['str'])),
                            ('metric_offset', (YLeaf(YType.uint32, 'metric-offset'), ['int'])),
                            ('revert_members', (YLeaf(YType.uint32, 'revert-members'), ['int'])),
                            ('minimum_members', (YLeaf(YType.uint32, 'minimum-members'), ['int'])),
                        ])
                        self.link_group_name = None
                        self.metric_offset = None
                        self.revert_members = None
                        self.minimum_members = None
                        self._segment_path = lambda: "link-group" + "[link-group-name='" + str(self.link_group_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LinkGroups.LinkGroup, ['link_group_name', 'metric_offset', 'revert_members', 'minimum_members'], name, value)


            class LspCheckIntervals(Entity):
                """
                LSP checksum check interval configuration
                
                .. attribute:: lsp_check_interval
                
                	LSP checksum check interval parameters
                	**type**\: list of  		 :py:class:`LspCheckInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspCheckIntervals, self).__init__()

                    self.yang_name = "lsp-check-intervals"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-check-interval", ("lsp_check_interval", Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval))])
                    self._leafs = OrderedDict()

                    self.lsp_check_interval = YList(self)
                    self._segment_path = lambda: "lsp-check-intervals"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspCheckIntervals, [], name, value)


                class LspCheckInterval(Entity):
                    """
                    LSP checksum check interval parameters
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: interval
                    
                    	LSP checksum check interval time in seconds
                    	**type**\: int
                    
                    	**range:** 10..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval, self).__init__()

                        self.yang_name = "lsp-check-interval"
                        self.yang_parent_name = "lsp-check-intervals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ])
                        self.level = None
                        self.interval = None
                        self._segment_path = lambda: "lsp-check-interval" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval, ['level', 'interval'], name, value)


            class LspPasswords(Entity):
                """
                LSP/SNP password configuration
                
                .. attribute:: lsp_password
                
                	LSP/SNP passwords. This must exist if an LSPAcceptPassword of the same level exists
                	**type**\: list of  		 :py:class:`LspPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords.LspPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspPasswords, self).__init__()

                    self.yang_name = "lsp-passwords"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-password", ("lsp_password", Isis.Instances.Instance.LspPasswords.LspPassword))])
                    self._leafs = OrderedDict()

                    self.lsp_password = YList(self)
                    self._segment_path = lambda: "lsp-passwords"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspPasswords, [], name, value)


                class LspPassword(Entity):
                    """
                    LSP/SNP passwords. This must exist if an
                    LSPAcceptPassword of the same level exists.
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: algorithm
                    
                    	Algorithm
                    	**type**\:  :py:class:`IsisAuthenticationAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithm>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: failure_mode
                    
                    	Failure Mode
                    	**type**\:  :py:class:`IsisAuthenticationFailureMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureMode>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: authentication_type
                    
                    	SNP packet authentication mode
                    	**type**\:  :py:class:`IsisSnpAuth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisSnpAuth>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: password
                    
                    	Password or unencrypted Key Chain name
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    .. attribute:: enable_poi
                    
                    	Enable POI
                    	**type**\:  :py:class:`IsisEnablePoi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisEnablePoi>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspPasswords.LspPassword, self).__init__()

                        self.yang_name = "lsp-password"
                        self.yang_parent_name = "lsp-passwords"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('algorithm', (YLeaf(YType.enumeration, 'algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithm', '')])),
                            ('failure_mode', (YLeaf(YType.enumeration, 'failure-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureMode', '')])),
                            ('authentication_type', (YLeaf(YType.enumeration, 'authentication-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisSnpAuth', '')])),
                            ('password', (YLeaf(YType.str, 'password'), ['str'])),
                            ('enable_poi', (YLeaf(YType.enumeration, 'enable-poi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisEnablePoi', '')])),
                        ])
                        self.level = None
                        self.algorithm = None
                        self.failure_mode = None
                        self.authentication_type = None
                        self.password = None
                        self.enable_poi = None
                        self._segment_path = lambda: "lsp-password" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspPasswords.LspPassword, ['level', 'algorithm', 'failure_mode', 'authentication_type', 'password', 'enable_poi'], name, value)


            class Nets(Entity):
                """
                NET configuration
                
                .. attribute:: net
                
                	Network Entity Title (NET)
                	**type**\: list of  		 :py:class:`Net <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets.Net>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.Nets, self).__init__()

                    self.yang_name = "nets"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("net", ("net", Isis.Instances.Instance.Nets.Net))])
                    self._leafs = OrderedDict()

                    self.net = YList(self)
                    self._segment_path = lambda: "nets"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Nets, [], name, value)


                class Net(Entity):
                    """
                    Network Entity Title (NET)
                    
                    .. attribute:: net_name  (key)
                    
                    	Network Entity Title
                    	**type**\: str
                    
                    	**pattern:** [a\-fA\-F0\-9]{2}(\\.[a\-fA\-F0\-9]{4}){3,9}\\.[a\-fA\-F0\-9]{2}
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.Nets.Net, self).__init__()

                        self.yang_name = "net"
                        self.yang_parent_name = "nets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['net_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('net_name', (YLeaf(YType.str, 'net-name'), ['str'])),
                        ])
                        self.net_name = None
                        self._segment_path = lambda: "net" + "[net-name='" + str(self.net_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.Nets.Net, ['net_name'], name, value)


            class LspLifetimes(Entity):
                """
                LSP lifetime configuration
                
                .. attribute:: lsp_lifetime
                
                	Maximum LSP lifetime
                	**type**\: list of  		 :py:class:`LspLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes.LspLifetime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.LspLifetimes, self).__init__()

                    self.yang_name = "lsp-lifetimes"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp-lifetime", ("lsp_lifetime", Isis.Instances.Instance.LspLifetimes.LspLifetime))])
                    self._leafs = OrderedDict()

                    self.lsp_lifetime = YList(self)
                    self._segment_path = lambda: "lsp-lifetimes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspLifetimes, [], name, value)


                class LspLifetime(Entity):
                    """
                    Maximum LSP lifetime
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: lifetime
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspLifetimes.LspLifetime, self).__init__()

                        self.yang_name = "lsp-lifetime"
                        self.yang_parent_name = "lsp-lifetimes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                        ])
                        self.level = None
                        self.lifetime = None
                        self._segment_path = lambda: "lsp-lifetime" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspLifetimes.LspLifetime, ['level', 'lifetime'], name, value)


            class OverloadBits(Entity):
                """
                LSP overload\-bit configuration
                
                .. attribute:: overload_bit
                
                	Set the overload bit in the System LSP so that other routers avoid this one in SPF calculations. This may be done either unconditionally, or on startup until either a set time has passed or IS\-IS is informed that BGP has converged. This is an Object with a union discriminated on an integer value of the ISISOverloadBitModeType
                	**type**\: list of  		 :py:class:`OverloadBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits.OverloadBit>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.OverloadBits, self).__init__()

                    self.yang_name = "overload-bits"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("overload-bit", ("overload_bit", Isis.Instances.Instance.OverloadBits.OverloadBit))])
                    self._leafs = OrderedDict()

                    self.overload_bit = YList(self)
                    self._segment_path = lambda: "overload-bits"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.OverloadBits, [], name, value)


                class OverloadBit(Entity):
                    """
                    Set the overload bit in the System LSP so
                    that other routers avoid this one in SPF
                    calculations. This may be done either
                    unconditionally, or on startup until either a
                    set time has passed or IS\-IS is informed that
                    BGP has converged. This is an Object with a
                    union discriminated on an integer value of
                    the ISISOverloadBitModeType.
                    
                    .. attribute:: level  (key)
                    
                    	Level to which configuration applies
                    	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: overload_bit_mode
                    
                    	Circumstances under which the overload bit is set in the system LSP
                    	**type**\:  :py:class:`IsisOverloadBitMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisOverloadBitMode>`
                    
                    .. attribute:: hippity_period
                    
                    	Time in seconds to advertise ourself as overloaded after process startup
                    	**type**\: int
                    
                    	**range:** 5..86400
                    
                    	**units**\: second
                    
                    .. attribute:: external_adv_type
                    
                    	Advertise prefixes from other protocols
                    	**type**\:  :py:class:`IsisAdvTypeExternal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeExternal>`
                    
                    .. attribute:: inter_level_adv_type
                    
                    	Advertise prefixes across ISIS levels
                    	**type**\:  :py:class:`IsisAdvTypeInterLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeInterLevel>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.OverloadBits.OverloadBit, self).__init__()

                        self.yang_name = "overload-bit"
                        self.yang_parent_name = "overload-bits"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['level']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                            ('overload_bit_mode', (YLeaf(YType.enumeration, 'overload-bit-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisOverloadBitMode', '')])),
                            ('hippity_period', (YLeaf(YType.uint32, 'hippity-period'), ['int'])),
                            ('external_adv_type', (YLeaf(YType.enumeration, 'external-adv-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeExternal', '')])),
                            ('inter_level_adv_type', (YLeaf(YType.enumeration, 'inter-level-adv-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAdvTypeInterLevel', '')])),
                        ])
                        self.level = None
                        self.overload_bit_mode = None
                        self.hippity_period = None
                        self.external_adv_type = None
                        self.inter_level_adv_type = None
                        self._segment_path = lambda: "overload-bit" + "[level='" + str(self.level) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.OverloadBits.OverloadBit, ['level', 'overload_bit_mode', 'hippity_period', 'external_adv_type', 'inter_level_adv_type'], name, value)


            class Interfaces(Entity):
                """
                Per\-interface configuration
                
                .. attribute:: interface
                
                	Configuration for an IS\-IS interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2018-06-14'

                def __init__(self):
                    super(Isis.Instances.Instance.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Isis.Instances.Instance.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Configuration for an IS\-IS interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: int_affinity_table
                    
                    	Interface Affinity Table
                    	**type**\:  :py:class:`IntAffinityTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable>`
                    
                    .. attribute:: lsp_retransmit_throttle_intervals
                    
                    	LSP\-retransmission\-throttle\-interval configuration
                    	**type**\:  :py:class:`LspRetransmitThrottleIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals>`
                    
                    .. attribute:: lsp_retransmit_intervals
                    
                    	LSP\-retransmission\-interval configuration
                    	**type**\:  :py:class:`LspRetransmitIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals>`
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: priorities
                    
                    	DIS\-election priority configuration
                    	**type**\:  :py:class:`Priorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities>`
                    
                    .. attribute:: hello_accept_passwords
                    
                    	IIH accept password configuration
                    	**type**\:  :py:class:`HelloAcceptPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords>`
                    
                    .. attribute:: hello_passwords
                    
                    	IIH password configuration
                    	**type**\:  :py:class:`HelloPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords>`
                    
                    .. attribute:: hello_paddings
                    
                    	Hello\-padding configuration
                    	**type**\:  :py:class:`HelloPaddings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings>`
                    
                    .. attribute:: hello_multipliers
                    
                    	Hello\-multiplier configuration
                    	**type**\:  :py:class:`HelloMultipliers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers>`
                    
                    .. attribute:: lsp_fast_flood_thresholds
                    
                    	LSP fast flood threshold configuration
                    	**type**\:  :py:class:`LspFastFloodThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds>`
                    
                    .. attribute:: prefix_attribute_n_flag_clears
                    
                    	Prefix attribute N flag clear configuration
                    	**type**\:  :py:class:`PrefixAttributeNFlagClears <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears>`
                    
                    .. attribute:: hello_intervals
                    
                    	Hello\-interval configuration
                    	**type**\:  :py:class:`HelloIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals>`
                    
                    .. attribute:: interface_afs
                    
                    	Per\-interface address\-family configuration
                    	**type**\:  :py:class:`InterfaceAfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs>`
                    
                    .. attribute:: csnp_intervals
                    
                    	CSNP\-interval configuration
                    	**type**\:  :py:class:`CsnpIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals>`
                    
                    .. attribute:: lsp_intervals
                    
                    	LSP\-interval configuration
                    	**type**\:  :py:class:`LspIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals>`
                    
                    .. attribute:: running
                    
                    	This object must be set before any other configuration is supplied for an interface, and must be the last per\-interface configuration object to be removed
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: circuit_type
                    
                    	Configure circuit type for interface
                    	**type**\:  :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                    
                    	**default value**\: level1-and2
                    
                    .. attribute:: point_to_point
                    
                    	IS\-IS will attempt to form point\-to\-point over LAN adjacencies over this interface
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: state
                    
                    	Enable/Disable routing
                    	**type**\:  :py:class:`IsisInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceState>`
                    
                    .. attribute:: mesh_group
                    
                    	Mesh\-group configuration
                    	**type**\: union of the below types:
                    
                    		**type**\:  :py:class:`MeshGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.MeshGroup>`
                    
                    		**type**\: int
                    
                    			**range:** 0..4294967295
                    
                    .. attribute:: link_down_fast_detect
                    
                    	Configure high priority detection of interface down event
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2018-06-14'

                    def __init__(self):
                        super(Isis.Instances.Instance.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("int-affinity-table", ("int_affinity_table", Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable)), ("lsp-retransmit-throttle-intervals", ("lsp_retransmit_throttle_intervals", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals)), ("lsp-retransmit-intervals", ("lsp_retransmit_intervals", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals)), ("bfd", ("bfd", Isis.Instances.Instance.Interfaces.Interface.Bfd)), ("priorities", ("priorities", Isis.Instances.Instance.Interfaces.Interface.Priorities)), ("hello-accept-passwords", ("hello_accept_passwords", Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords)), ("hello-passwords", ("hello_passwords", Isis.Instances.Instance.Interfaces.Interface.HelloPasswords)), ("hello-paddings", ("hello_paddings", Isis.Instances.Instance.Interfaces.Interface.HelloPaddings)), ("hello-multipliers", ("hello_multipliers", Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers)), ("lsp-fast-flood-thresholds", ("lsp_fast_flood_thresholds", Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds)), ("prefix-attribute-n-flag-clears", ("prefix_attribute_n_flag_clears", Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears)), ("hello-intervals", ("hello_intervals", Isis.Instances.Instance.Interfaces.Interface.HelloIntervals)), ("interface-afs", ("interface_afs", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs)), ("csnp-intervals", ("csnp_intervals", Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals)), ("lsp-intervals", ("lsp_intervals", Isis.Instances.Instance.Interfaces.Interface.LspIntervals))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('running', (YLeaf(YType.empty, 'running'), ['Empty'])),
                            ('circuit_type', (YLeaf(YType.enumeration, 'circuit-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisConfigurableLevels', '')])),
                            ('point_to_point', (YLeaf(YType.empty, 'point-to-point'), ['Empty'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceState', '')])),
                            ('mesh_group', (YLeaf(YType.str, 'mesh-group'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis', 'Instances.Instance.Interfaces.Interface.MeshGroup'),'int'])),
                            ('link_down_fast_detect', (YLeaf(YType.empty, 'link-down-fast-detect'), ['Empty'])),
                        ])
                        self.interface_name = None
                        self.running = None
                        self.circuit_type = None
                        self.point_to_point = None
                        self.state = None
                        self.mesh_group = None
                        self.link_down_fast_detect = None

                        self.int_affinity_table = Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable()
                        self.int_affinity_table.parent = self
                        self._children_name_map["int_affinity_table"] = "int-affinity-table"

                        self.lsp_retransmit_throttle_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals()
                        self.lsp_retransmit_throttle_intervals.parent = self
                        self._children_name_map["lsp_retransmit_throttle_intervals"] = "lsp-retransmit-throttle-intervals"

                        self.lsp_retransmit_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals()
                        self.lsp_retransmit_intervals.parent = self
                        self._children_name_map["lsp_retransmit_intervals"] = "lsp-retransmit-intervals"

                        self.bfd = Isis.Instances.Instance.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self._children_name_map["bfd"] = "bfd"

                        self.priorities = Isis.Instances.Instance.Interfaces.Interface.Priorities()
                        self.priorities.parent = self
                        self._children_name_map["priorities"] = "priorities"

                        self.hello_accept_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords()
                        self.hello_accept_passwords.parent = self
                        self._children_name_map["hello_accept_passwords"] = "hello-accept-passwords"

                        self.hello_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloPasswords()
                        self.hello_passwords.parent = self
                        self._children_name_map["hello_passwords"] = "hello-passwords"

                        self.hello_paddings = Isis.Instances.Instance.Interfaces.Interface.HelloPaddings()
                        self.hello_paddings.parent = self
                        self._children_name_map["hello_paddings"] = "hello-paddings"

                        self.hello_multipliers = Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers()
                        self.hello_multipliers.parent = self
                        self._children_name_map["hello_multipliers"] = "hello-multipliers"

                        self.lsp_fast_flood_thresholds = Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds()
                        self.lsp_fast_flood_thresholds.parent = self
                        self._children_name_map["lsp_fast_flood_thresholds"] = "lsp-fast-flood-thresholds"

                        self.prefix_attribute_n_flag_clears = Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears()
                        self.prefix_attribute_n_flag_clears.parent = self
                        self._children_name_map["prefix_attribute_n_flag_clears"] = "prefix-attribute-n-flag-clears"

                        self.hello_intervals = Isis.Instances.Instance.Interfaces.Interface.HelloIntervals()
                        self.hello_intervals.parent = self
                        self._children_name_map["hello_intervals"] = "hello-intervals"

                        self.interface_afs = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs()
                        self.interface_afs.parent = self
                        self._children_name_map["interface_afs"] = "interface-afs"

                        self.csnp_intervals = Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals()
                        self.csnp_intervals.parent = self
                        self._children_name_map["csnp_intervals"] = "csnp-intervals"

                        self.lsp_intervals = Isis.Instances.Instance.Interfaces.Interface.LspIntervals()
                        self.lsp_intervals.parent = self
                        self._children_name_map["lsp_intervals"] = "lsp-intervals"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface, ['interface_name', 'running', 'circuit_type', 'point_to_point', 'state', 'mesh_group', 'link_down_fast_detect'], name, value)

                    class MeshGroup(Enum):
                        """
                        MeshGroup (Enum Class)

                        Mesh\-group configuration

                        .. data:: blocked = 0

                        	Blocked mesh group.  Changed LSPs are not

                        	flooded over blocked interfaces

                        """

                        blocked = Enum.YLeaf(0, "blocked")



                    class IntAffinityTable(Entity):
                        """
                        Interface Affinity Table
                        
                        .. attribute:: flex_algos
                        
                        	Set the interface affinities used by Flex\-Algo
                        	**type**\:  :py:class:`FlexAlgos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable, self).__init__()

                            self.yang_name = "int-affinity-table"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("flex-algos", ("flex_algos", Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos))])
                            self._leafs = OrderedDict()

                            self.flex_algos = Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos()
                            self.flex_algos.parent = self
                            self._children_name_map["flex_algos"] = "flex-algos"
                            self._segment_path = lambda: "int-affinity-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable, [], name, value)


                        class FlexAlgos(Entity):
                            """
                            Set the interface affinities used by
                            Flex\-Algo
                            
                            .. attribute:: flex_algo
                            
                            	Array of Attribute Names
                            	**type**\: list of str
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos, self).__init__()

                                self.yang_name = "flex-algos"
                                self.yang_parent_name = "int-affinity-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flex_algo', (YLeafList(YType.str, 'flex-algo'), ['str'])),
                                ])
                                self.flex_algo = []
                                self._segment_path = lambda: "flex-algos"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.IntAffinityTable.FlexAlgos, ['flex_algo'], name, value)


                    class LspRetransmitThrottleIntervals(Entity):
                        """
                        LSP\-retransmission\-throttle\-interval
                        configuration
                        
                        .. attribute:: lsp_retransmit_throttle_interval
                        
                        	Minimum interval betwen retransissions of different LSPs
                        	**type**\: list of  		 :py:class:`LspRetransmitThrottleInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals, self).__init__()

                            self.yang_name = "lsp-retransmit-throttle-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lsp-retransmit-throttle-interval", ("lsp_retransmit_throttle_interval", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval))])
                            self._leafs = OrderedDict()

                            self.lsp_retransmit_throttle_interval = YList(self)
                            self._segment_path = lambda: "lsp-retransmit-throttle-intervals"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals, [], name, value)


                        class LspRetransmitThrottleInterval(Entity):
                            """
                            Minimum interval betwen retransissions of
                            different LSPs
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval, self).__init__()

                                self.yang_name = "lsp-retransmit-throttle-interval"
                                self.yang_parent_name = "lsp-retransmit-throttle-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.level = None
                                self.interval = None
                                self._segment_path = lambda: "lsp-retransmit-throttle-interval" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval, ['level', 'interval'], name, value)


                    class LspRetransmitIntervals(Entity):
                        """
                        LSP\-retransmission\-interval configuration
                        
                        .. attribute:: lsp_retransmit_interval
                        
                        	Interval between retransmissions of the same LSP
                        	**type**\: list of  		 :py:class:`LspRetransmitInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals, self).__init__()

                            self.yang_name = "lsp-retransmit-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lsp-retransmit-interval", ("lsp_retransmit_interval", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval))])
                            self._leafs = OrderedDict()

                            self.lsp_retransmit_interval = YList(self)
                            self._segment_path = lambda: "lsp-retransmit-intervals"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals, [], name, value)


                        class LspRetransmitInterval(Entity):
                            """
                            Interval between retransmissions of the
                            same LSP
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval, self).__init__()

                                self.yang_name = "lsp-retransmit-interval"
                                self.yang_parent_name = "lsp-retransmit-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.level = None
                                self.interval = None
                                self._segment_path = lambda: "lsp-retransmit-interval" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval, ['level', 'interval'], name, value)


                    class Bfd(Entity):
                        """
                        BFD configuration
                        
                        .. attribute:: enable_ipv6
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\: bool
                        
                        .. attribute:: enable_ipv4
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\: bool
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by isis
                        	**type**\: int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by isis
                        	**type**\: int
                        
                        	**range:** 2..50
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.Bfd, self).__init__()

                            self.yang_name = "bfd"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable_ipv6', (YLeaf(YType.boolean, 'enable-ipv6'), ['bool'])),
                                ('enable_ipv4', (YLeaf(YType.boolean, 'enable-ipv4'), ['bool'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                            ])
                            self.enable_ipv6 = None
                            self.enable_ipv4 = None
                            self.interval = None
                            self.detection_multiplier = None
                            self._segment_path = lambda: "bfd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.Bfd, ['enable_ipv6', 'enable_ipv4', 'interval', 'detection_multiplier'], name, value)


                    class Priorities(Entity):
                        """
                        DIS\-election priority configuration
                        
                        .. attribute:: priority
                        
                        	DIS\-election priority
                        	**type**\: list of  		 :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.Priorities, self).__init__()

                            self.yang_name = "priorities"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("priority", ("priority", Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority))])
                            self._leafs = OrderedDict()

                            self.priority = YList(self)
                            self._segment_path = lambda: "priorities"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.Priorities, [], name, value)


                        class Priority(Entity):
                            """
                            DIS\-election priority
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: priority_value
                            
                            	Priority
                            	**type**\: int
                            
                            	**range:** 0..127
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "priorities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('priority_value', (YLeaf(YType.uint32, 'priority-value'), ['int'])),
                                ])
                                self.level = None
                                self.priority_value = None
                                self._segment_path = lambda: "priority" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority, ['level', 'priority_value'], name, value)


                    class HelloAcceptPasswords(Entity):
                        """
                        IIH accept password configuration
                        
                        .. attribute:: hello_accept_password
                        
                        	IIH accept passwords. This requires the existence of a HelloPassword of the same level
                        	**type**\: list of  		 :py:class:`HelloAcceptPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords, self).__init__()

                            self.yang_name = "hello-accept-passwords"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hello-accept-password", ("hello_accept_password", Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword))])
                            self._leafs = OrderedDict()

                            self.hello_accept_password = YList(self)
                            self._segment_path = lambda: "hello-accept-passwords"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords, [], name, value)


                        class HelloAcceptPassword(Entity):
                            """
                            IIH accept passwords. This requires the
                            existence of a HelloPassword of the same
                            level.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: password
                            
                            	Password
                            	**type**\: str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword, self).__init__()

                                self.yang_name = "hello-accept-password"
                                self.yang_parent_name = "hello-accept-passwords"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                                ])
                                self.level = None
                                self.password = None
                                self._segment_path = lambda: "hello-accept-password" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword, ['level', 'password'], name, value)


                    class HelloPasswords(Entity):
                        """
                        IIH password configuration
                        
                        .. attribute:: hello_password
                        
                        	IIH passwords. This must exist if a HelloAcceptPassword of the same level exists
                        	**type**\: list of  		 :py:class:`HelloPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords, self).__init__()

                            self.yang_name = "hello-passwords"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hello-password", ("hello_password", Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword))])
                            self._leafs = OrderedDict()

                            self.hello_password = YList(self)
                            self._segment_path = lambda: "hello-passwords"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords, [], name, value)


                        class HelloPassword(Entity):
                            """
                            IIH passwords. This must exist if a
                            HelloAcceptPassword of the same level
                            exists.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: algorithm
                            
                            	Algorithm
                            	**type**\:  :py:class:`IsisAuthenticationAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithm>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: failure_mode
                            
                            	Failure Mode
                            	**type**\:  :py:class:`IsisAuthenticationFailureMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureMode>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: password
                            
                            	Password or unencrypted Key Chain name
                            	**type**\: str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword, self).__init__()

                                self.yang_name = "hello-password"
                                self.yang_parent_name = "hello-passwords"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('algorithm', (YLeaf(YType.enumeration, 'algorithm'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationAlgorithm', '')])),
                                    ('failure_mode', (YLeaf(YType.enumeration, 'failure-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisAuthenticationFailureMode', '')])),
                                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                                ])
                                self.level = None
                                self.algorithm = None
                                self.failure_mode = None
                                self.password = None
                                self._segment_path = lambda: "hello-password" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword, ['level', 'algorithm', 'failure_mode', 'password'], name, value)


                    class HelloPaddings(Entity):
                        """
                        Hello\-padding configuration
                        
                        .. attribute:: hello_padding
                        
                        	Pad IIHs to the interface MTU
                        	**type**\: list of  		 :py:class:`HelloPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings, self).__init__()

                            self.yang_name = "hello-paddings"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hello-padding", ("hello_padding", Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding))])
                            self._leafs = OrderedDict()

                            self.hello_padding = YList(self)
                            self._segment_path = lambda: "hello-paddings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings, [], name, value)


                        class HelloPadding(Entity):
                            """
                            Pad IIHs to the interface MTU
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: padding_type
                            
                            	Hello padding type value
                            	**type**\:  :py:class:`IsisHelloPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisHelloPadding>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding, self).__init__()

                                self.yang_name = "hello-padding"
                                self.yang_parent_name = "hello-paddings"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('padding_type', (YLeaf(YType.enumeration, 'padding-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisHelloPadding', '')])),
                                ])
                                self.level = None
                                self.padding_type = None
                                self._segment_path = lambda: "hello-padding" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding, ['level', 'padding_type'], name, value)


                    class HelloMultipliers(Entity):
                        """
                        Hello\-multiplier configuration
                        
                        .. attribute:: hello_multiplier
                        
                        	Hello\-multiplier configuration. The number of successive IIHs that may be missed on an adjacency before it is considered down
                        	**type**\: list of  		 :py:class:`HelloMultiplier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers, self).__init__()

                            self.yang_name = "hello-multipliers"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hello-multiplier", ("hello_multiplier", Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier))])
                            self._leafs = OrderedDict()

                            self.hello_multiplier = YList(self)
                            self._segment_path = lambda: "hello-multipliers"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers, [], name, value)


                        class HelloMultiplier(Entity):
                            """
                            Hello\-multiplier configuration. The number
                            of successive IIHs that may be missed on an
                            adjacency before it is considered down.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: multiplier
                            
                            	Hello multiplier value
                            	**type**\: int
                            
                            	**range:** 3..1000
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier, self).__init__()

                                self.yang_name = "hello-multiplier"
                                self.yang_parent_name = "hello-multipliers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('multiplier', (YLeaf(YType.uint32, 'multiplier'), ['int'])),
                                ])
                                self.level = None
                                self.multiplier = None
                                self._segment_path = lambda: "hello-multiplier" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier, ['level', 'multiplier'], name, value)


                    class LspFastFloodThresholds(Entity):
                        """
                        LSP fast flood threshold configuration
                        
                        .. attribute:: lsp_fast_flood_threshold
                        
                        	Number of LSPs to send back to back on an interface
                        	**type**\: list of  		 :py:class:`LspFastFloodThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds, self).__init__()

                            self.yang_name = "lsp-fast-flood-thresholds"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lsp-fast-flood-threshold", ("lsp_fast_flood_threshold", Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold))])
                            self._leafs = OrderedDict()

                            self.lsp_fast_flood_threshold = YList(self)
                            self._segment_path = lambda: "lsp-fast-flood-thresholds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds, [], name, value)


                        class LspFastFloodThreshold(Entity):
                            """
                            Number of LSPs to send back to back on an
                            interface.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: count
                            
                            	Count
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold, self).__init__()

                                self.yang_name = "lsp-fast-flood-threshold"
                                self.yang_parent_name = "lsp-fast-flood-thresholds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                ])
                                self.level = None
                                self.count = None
                                self._segment_path = lambda: "lsp-fast-flood-threshold" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold, ['level', 'count'], name, value)


                    class PrefixAttributeNFlagClears(Entity):
                        """
                        Prefix attribute N flag clear configuration
                        
                        .. attribute:: prefix_attribute_n_flag_clear
                        
                        	Clear the N flag in prefix attribute flags sub\-TLV
                        	**type**\: list of  		 :py:class:`PrefixAttributeNFlagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears, self).__init__()

                            self.yang_name = "prefix-attribute-n-flag-clears"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("prefix-attribute-n-flag-clear", ("prefix_attribute_n_flag_clear", Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear))])
                            self._leafs = OrderedDict()

                            self.prefix_attribute_n_flag_clear = YList(self)
                            self._segment_path = lambda: "prefix-attribute-n-flag-clears"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears, [], name, value)


                        class PrefixAttributeNFlagClear(Entity):
                            """
                            Clear the N flag in prefix attribute flags
                            sub\-TLV
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear, self).__init__()

                                self.yang_name = "prefix-attribute-n-flag-clear"
                                self.yang_parent_name = "prefix-attribute-n-flag-clears"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                ])
                                self.level = None
                                self._segment_path = lambda: "prefix-attribute-n-flag-clear" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear, ['level'], name, value)


                    class HelloIntervals(Entity):
                        """
                        Hello\-interval configuration
                        
                        .. attribute:: hello_interval
                        
                        	Hello\-interval configuration. The interval at which IIH packets will be sent. This will be three times quicker on a LAN interface which has been electted DIS
                        	**type**\: list of  		 :py:class:`HelloInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals, self).__init__()

                            self.yang_name = "hello-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("hello-interval", ("hello_interval", Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval))])
                            self._leafs = OrderedDict()

                            self.hello_interval = YList(self)
                            self._segment_path = lambda: "hello-intervals"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals, [], name, value)


                        class HelloInterval(Entity):
                            """
                            Hello\-interval configuration. The interval
                            at which IIH packets will be sent. This
                            will be three times quicker on a LAN
                            interface which has been electted DIS.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval, self).__init__()

                                self.yang_name = "hello-interval"
                                self.yang_parent_name = "hello-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.level = None
                                self.interval = None
                                self._segment_path = lambda: "hello-interval" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval, ['level', 'interval'], name, value)


                    class InterfaceAfs(Entity):
                        """
                        Per\-interface address\-family configuration
                        
                        .. attribute:: interface_af
                        
                        	Configuration for an IS\-IS address\-family on a single interface. If a named (non\-default) topology is being created it must be multicast. Also the topology ID mustbe set first and delete last in the router configuration
                        	**type**\: list of  		 :py:class:`InterfaceAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs, self).__init__()

                            self.yang_name = "interface-afs"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-af", ("interface_af", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf))])
                            self._leafs = OrderedDict()

                            self.interface_af = YList(self)
                            self._segment_path = lambda: "interface-afs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs, [], name, value)


                        class InterfaceAf(Entity):
                            """
                            Configuration for an IS\-IS address\-family
                            on a single interface. If a named
                            (non\-default) topology is being created it
                            must be multicast. Also the topology ID
                            mustbe set first and delete last in the
                            router configuration.
                            
                            .. attribute:: af_name  (key)
                            
                            	Address family
                            	**type**\:  :py:class:`IsisAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamily>`
                            
                            .. attribute:: saf_name  (key)
                            
                            	Sub address family
                            	**type**\:  :py:class:`IsisSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamily>`
                            
                            .. attribute:: interface_af_data
                            
                            	Data container
                            	**type**\:  :py:class:`InterfaceAfData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData>`
                            
                            .. attribute:: topology_name
                            
                            	keys\: topology\-name
                            	**type**\: list of  		 :py:class:`TopologyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf, self).__init__()

                                self.yang_name = "interface-af"
                                self.yang_parent_name = "interface-afs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['af_name','saf_name']
                                self._child_classes = OrderedDict([("interface-af-data", ("interface_af_data", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData)), ("topology-name", ("topology_name", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName))])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisAddressFamily', '')])),
                                    ('saf_name', (YLeaf(YType.enumeration, 'saf-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisSubAddressFamily', '')])),
                                ])
                                self.af_name = None
                                self.saf_name = None

                                self.interface_af_data = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData()
                                self.interface_af_data.parent = self
                                self._children_name_map["interface_af_data"] = "interface-af-data"

                                self.topology_name = YList(self)
                                self._segment_path = lambda: "interface-af" + "[af-name='" + str(self.af_name) + "']" + "[saf-name='" + str(self.saf_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf, ['af_name', 'saf_name'], name, value)


                            class InterfaceAfData(Entity):
                                """
                                Data container.
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:  :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\:  :py:class:`InterfaceFrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\:  :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp>`
                                
                                .. attribute:: prefix_sspfsid
                                
                                	Assign prefix SSPF SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:  :py:class:`PrefixSspfsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: algorithm_prefix_sids
                                
                                	Algorithm SID Table
                                	**type**\:  :py:class:`AlgorithmPrefixSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\:  :py:class:`AutoMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics>`
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\:  :py:class:`AdminTags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\:  :py:class:`InterfaceLinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\:  :py:class:`IsisInterfaceAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfState>`
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: manual_adj_sids
                                
                                	Manual Adjacecy SID configuration
                                	**type**\:  :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids>`
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\:  :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\:  :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData, self).__init__()

                                    self.yang_name = "interface-af-data"
                                    self.yang_parent_name = "interface-af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("prefix-sid", ("prefix_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid)), ("interface-frr-table", ("interface_frr_table", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable)), ("mpls-ldp", ("mpls_ldp", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp)), ("prefix-sspfsid", ("prefix_sspfsid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid)), ("algorithm-prefix-sids", ("algorithm_prefix_sids", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids)), ("auto-metrics", ("auto_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics)), ("admin-tags", ("admin_tags", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags)), ("interface-link-group", ("interface_link_group", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup)), ("manual-adj-sids", ("manual_adj_sids", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids)), ("metrics", ("metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics)), ("weights", ("weights", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights))])
                                    self._leafs = OrderedDict([
                                        ('interface_af_state', (YLeaf(YType.enumeration, 'interface-af-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfState', '')])),
                                        ('running', (YLeaf(YType.empty, 'running'), ['Empty'])),
                                    ])
                                    self.interface_af_state = None
                                    self.running = None

                                    self.prefix_sid = None
                                    self._children_name_map["prefix_sid"] = "prefix-sid"

                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self._children_name_map["interface_frr_table"] = "interface-frr-table"

                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self._children_name_map["mpls_ldp"] = "mpls-ldp"

                                    self.prefix_sspfsid = None
                                    self._children_name_map["prefix_sspfsid"] = "prefix-sspfsid"

                                    self.algorithm_prefix_sids = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids()
                                    self.algorithm_prefix_sids.parent = self
                                    self._children_name_map["algorithm_prefix_sids"] = "algorithm-prefix-sids"

                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self._children_name_map["auto_metrics"] = "auto-metrics"

                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags()
                                    self.admin_tags.parent = self
                                    self._children_name_map["admin_tags"] = "admin-tags"

                                    self.interface_link_group = None
                                    self._children_name_map["interface_link_group"] = "interface-link-group"

                                    self.manual_adj_sids = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids()
                                    self.manual_adj_sids.parent = self
                                    self._children_name_map["manual_adj_sids"] = "manual-adj-sids"

                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics()
                                    self.metrics.parent = self
                                    self._children_name_map["metrics"] = "metrics"

                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights()
                                    self.weights.parent = self
                                    self._children_name_map["weights"] = "weights"
                                    self._segment_path = lambda: "interface-af-data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData, ['interface_af_state', 'running'], name, value)


                                class PrefixSid(Entity):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:  :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:  :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:  :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid, self).__init__()

                                        self.yang_name = "prefix-sid"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                            ('php', (YLeaf(YType.enumeration, 'php'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag', '')])),
                                            ('explicit_null', (YLeaf(YType.enumeration, 'explicit-null'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag', '')])),
                                            ('nflag_clear', (YLeaf(YType.enumeration, 'nflag-clear'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear', '')])),
                                        ])
                                        self.type = None
                                        self.value = None
                                        self.php = None
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self._segment_path = lambda: "prefix-sid"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid, ['type', 'value', 'php', 'explicit_null', 'nflag_clear'], name, value)


                                class InterfaceFrrTable(Entity):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\:  :py:class:`FrrlfaCandidateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\:  :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\:  :py:class:`FrrTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\:  :py:class:`FrrRemoteLfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: interface_frr_tiebreaker_defaults
                                    
                                    	Interface FRR Default tiebreaker configuration
                                    	**type**\:  :py:class:`InterfaceFrrTiebreakerDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\:  :py:class:`FrrtilfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\:  :py:class:`FrrExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: interface_frr_tiebreakers
                                    
                                    	Interface FRR tiebreakers configuration
                                    	**type**\:  :py:class:`InterfaceFrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable, self).__init__()

                                        self.yang_name = "interface-frr-table"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("frrlfa-candidate-interfaces", ("frrlfa_candidate_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces)), ("frr-remote-lfa-max-metrics", ("frr_remote_lfa_max_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics)), ("frr-types", ("frr_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes)), ("frr-remote-lfa-types", ("frr_remote_lfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes)), ("interface-frr-tiebreaker-defaults", ("interface_frr_tiebreaker_defaults", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults)), ("frrtilfa-types", ("frrtilfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes)), ("frr-exclude-interfaces", ("frr_exclude_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces)), ("interface-frr-tiebreakers", ("interface_frr_tiebreakers", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers))])
                                        self._leafs = OrderedDict()

                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self._children_name_map["frrlfa_candidate_interfaces"] = "frrlfa-candidate-interfaces"

                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self._children_name_map["frr_remote_lfa_max_metrics"] = "frr-remote-lfa-max-metrics"

                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self._children_name_map["frr_types"] = "frr-types"

                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self._children_name_map["frr_remote_lfa_types"] = "frr-remote-lfa-types"

                                        self.interface_frr_tiebreaker_defaults = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults()
                                        self.interface_frr_tiebreaker_defaults.parent = self
                                        self._children_name_map["interface_frr_tiebreaker_defaults"] = "interface-frr-tiebreaker-defaults"

                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self
                                        self._children_name_map["frrtilfa_types"] = "frrtilfa-types"

                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self._children_name_map["frr_exclude_interfaces"] = "frr-exclude-interfaces"

                                        self.interface_frr_tiebreakers = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers()
                                        self.interface_frr_tiebreakers.parent = self
                                        self._children_name_map["interface_frr_tiebreakers"] = "interface-frr-tiebreakers"
                                        self._segment_path = lambda: "interface-frr-table"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable, [], name, value)


                                    class FrrlfaCandidateInterfaces(Entity):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of  		 :py:class:`FrrlfaCandidateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces, self).__init__()

                                            self.yang_name = "frrlfa-candidate-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frrlfa-candidate-interface", ("frrlfa_candidate_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface))])
                                            self._leafs = OrderedDict()

                                            self.frrlfa_candidate_interface = YList(self)
                                            self._segment_path = lambda: "frrlfa-candidate-interfaces"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces, [], name, value)


                                        class FrrlfaCandidateInterface(Entity):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: interface_name  (key)
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            .. attribute:: frr_type  (key)
                                            
                                            	Computation Type
                                            	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, self).__init__()

                                                self.yang_name = "frrlfa-candidate-interface"
                                                self.yang_parent_name = "frrlfa-candidate-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['interface_name','frr_type']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                    ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                    ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                                ])
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None
                                                self._segment_path = lambda: "frrlfa-candidate-interface" + "[interface-name='" + str(self.interface_name) + "']" + "[frr-type='" + str(self.frr_type) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class FrrRemoteLfaMaxMetrics(Entity):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of  		 :py:class:`FrrRemoteLfaMaxMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, self).__init__()

                                            self.yang_name = "frr-remote-lfa-max-metrics"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-remote-lfa-max-metric", ("frr_remote_lfa_max_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric))])
                                            self._leafs = OrderedDict()

                                            self.frr_remote_lfa_max_metric = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-max-metrics"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, [], name, value)


                                        class FrrRemoteLfaMaxMetric(Entity):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\: int
                                            
                                            	**range:** 1..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, self).__init__()

                                                self.yang_name = "frr-remote-lfa-max-metric"
                                                self.yang_parent_name = "frr-remote-lfa-max-metrics"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('max_metric', (YLeaf(YType.uint32, 'max-metric'), ['int'])),
                                                ])
                                                self.level = None
                                                self.max_metric = None
                                                self._segment_path = lambda: "frr-remote-lfa-max-metric" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, ['level', 'max_metric'], name, value)


                                    class FrrTypes(Entity):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of  		 :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes, self).__init__()

                                            self.yang_name = "frr-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-type", ("frr_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType))])
                                            self._leafs = OrderedDict()

                                            self.frr_type = YList(self)
                                            self._segment_path = lambda: "frr-types"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes, [], name, value)


                                        class FrrType(Entity):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType, self).__init__()

                                                self.yang_name = "frr-type"
                                                self.yang_parent_name = "frr-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                ])
                                                self.level = None
                                                self.type = None
                                                self._segment_path = lambda: "frr-type" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType, ['level', 'type'], name, value)


                                    class FrrRemoteLfaTypes(Entity):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of  		 :py:class:`FrrRemoteLfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes, self).__init__()

                                            self.yang_name = "frr-remote-lfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-remote-lfa-type", ("frr_remote_lfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType))])
                                            self._leafs = OrderedDict()

                                            self.frr_remote_lfa_type = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-types"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes, [], name, value)


                                        class FrrRemoteLfaType(Entity):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\:  :py:class:`IsisRemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfa>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, self).__init__()

                                                self.yang_name = "frr-remote-lfa-type"
                                                self.yang_parent_name = "frr-remote-lfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfa', '')])),
                                                ])
                                                self.level = None
                                                self.type = None
                                                self._segment_path = lambda: "frr-remote-lfa-type" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, ['level', 'type'], name, value)


                                    class InterfaceFrrTiebreakerDefaults(Entity):
                                        """
                                        Interface FRR Default tiebreaker
                                        configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker_default
                                        
                                        	Configure default tiebreaker
                                        	**type**\: list of  		 :py:class:`InterfaceFrrTiebreakerDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, self).__init__()

                                            self.yang_name = "interface-frr-tiebreaker-defaults"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface-frr-tiebreaker-default", ("interface_frr_tiebreaker_default", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault))])
                                            self._leafs = OrderedDict()

                                            self.interface_frr_tiebreaker_default = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreaker-defaults"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, [], name, value)


                                        class InterfaceFrrTiebreakerDefault(Entity):
                                            """
                                            Configure default tiebreaker
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker-default"
                                                self.yang_parent_name = "interface-frr-tiebreaker-defaults"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ])
                                                self.level = None
                                                self._segment_path = lambda: "interface-frr-tiebreaker-default" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, ['level'], name, value)


                                    class FrrtilfaTypes(Entity):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of  		 :py:class:`FrrtilfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes, self).__init__()

                                            self.yang_name = "frrtilfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frrtilfa-type", ("frrtilfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType))])
                                            self._leafs = OrderedDict()

                                            self.frrtilfa_type = YList(self)
                                            self._segment_path = lambda: "frrtilfa-types"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes, [], name, value)


                                        class FrrtilfaType(Entity):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, self).__init__()

                                                self.yang_name = "frrtilfa-type"
                                                self.yang_parent_name = "frrtilfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ])
                                                self.level = None
                                                self._segment_path = lambda: "frrtilfa-type" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, ['level'], name, value)


                                    class FrrExcludeInterfaces(Entity):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of  		 :py:class:`FrrExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces, self).__init__()

                                            self.yang_name = "frr-exclude-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-exclude-interface", ("frr_exclude_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface))])
                                            self._leafs = OrderedDict()

                                            self.frr_exclude_interface = YList(self)
                                            self._segment_path = lambda: "frr-exclude-interfaces"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces, [], name, value)


                                        class FrrExcludeInterface(Entity):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: interface_name  (key)
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            .. attribute:: frr_type  (key)
                                            
                                            	Computation Type
                                            	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, self).__init__()

                                                self.yang_name = "frr-exclude-interface"
                                                self.yang_parent_name = "frr-exclude-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['interface_name','frr_type']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                    ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                    ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                                ])
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None
                                                self._segment_path = lambda: "frr-exclude-interface" + "[interface-name='" + str(self.interface_name) + "']" + "[frr-type='" + str(self.frr_type) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class InterfaceFrrTiebreakers(Entity):
                                        """
                                        Interface FRR tiebreakers configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker
                                        
                                        	Configure tiebreaker for multiple backups
                                        	**type**\: list of  		 :py:class:`InterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers, self).__init__()

                                            self.yang_name = "interface-frr-tiebreakers"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface-frr-tiebreaker", ("interface_frr_tiebreaker", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker))])
                                            self._leafs = OrderedDict()

                                            self.interface_frr_tiebreaker = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreakers"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers, [], name, value)


                                        class InterfaceFrrTiebreaker(Entity):
                                            """
                                            Configure tiebreaker for multiple
                                            backups
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: tiebreaker  (key)
                                            
                                            	Tiebreaker for which configuration applies
                                            	**type**\:  :py:class:`IsisInterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceFrrTiebreaker>`
                                            
                                            .. attribute:: index
                                            
                                            	Preference order among tiebreakers
                                            	**type**\: int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker"
                                                self.yang_parent_name = "interface-frr-tiebreakers"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level','tiebreaker']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('tiebreaker', (YLeaf(YType.enumeration, 'tiebreaker'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreaker', '')])),
                                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                                ])
                                                self.level = None
                                                self.tiebreaker = None
                                                self.index = None
                                                self._segment_path = lambda: "interface-frr-tiebreaker" + "[level='" + str(self.level) + "']" + "[tiebreaker='" + str(self.tiebreaker) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                                class MplsLdp(Entity):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp, self).__init__()

                                        self.yang_name = "mpls-ldp"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sync_level', (YLeaf(YType.uint32, 'sync-level'), ['int'])),
                                        ])
                                        self.sync_level = None
                                        self._segment_path = lambda: "mpls-ldp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp, ['sync_level'], name, value)


                                class PrefixSspfsid(Entity):
                                    """
                                    Assign prefix SSPF SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:  :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:  :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:  :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid, self).__init__()

                                        self.yang_name = "prefix-sspfsid"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                            ('php', (YLeaf(YType.enumeration, 'php'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag', '')])),
                                            ('explicit_null', (YLeaf(YType.enumeration, 'explicit-null'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag', '')])),
                                            ('nflag_clear', (YLeaf(YType.enumeration, 'nflag-clear'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear', '')])),
                                        ])
                                        self.type = None
                                        self.value = None
                                        self.php = None
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self._segment_path = lambda: "prefix-sspfsid"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid, ['type', 'value', 'php', 'explicit_null', 'nflag_clear'], name, value)


                                class AlgorithmPrefixSids(Entity):
                                    """
                                    Algorithm SID Table
                                    
                                    .. attribute:: algorithm_prefix_sid
                                    
                                    	Assign prefix SID for algorithm to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                    	**type**\: list of  		 :py:class:`AlgorithmPrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids, self).__init__()

                                        self.yang_name = "algorithm-prefix-sids"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("algorithm-prefix-sid", ("algorithm_prefix_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid))])
                                        self._leafs = OrderedDict()

                                        self.algorithm_prefix_sid = YList(self)
                                        self._segment_path = lambda: "algorithm-prefix-sids"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids, [], name, value)


                                    class AlgorithmPrefixSid(Entity):
                                        """
                                        Assign prefix SID for algorithm to an
                                        interface, ISISPHPFlag will be rejected
                                        if set to disable, ISISEXPLICITNULLFlag
                                        will override the value of ISISPHPFlag
                                        
                                        .. attribute:: algo  (key)
                                        
                                        	Algorithm
                                        	**type**\: int
                                        
                                        	**range:** 128..255
                                        
                                        .. attribute:: type
                                        
                                        	SID type for the interface
                                        	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: value
                                        
                                        	SID value for the interface
                                        	**type**\: int
                                        
                                        	**range:** 0..1048575
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: php
                                        
                                        	Enable/Disable Penultimate Hop Popping
                                        	**type**\:  :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: explicit_null
                                        
                                        	Enable/Disable Explicit\-NULL flag
                                        	**type**\:  :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: nflag_clear
                                        
                                        	Clear N\-flag for the prefix\-SID
                                        	**type**\:  :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid, self).__init__()

                                            self.yang_name = "algorithm-prefix-sid"
                                            self.yang_parent_name = "algorithm-prefix-sids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['algo']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('algo', (YLeaf(YType.uint32, 'algo'), ['int'])),
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('php', (YLeaf(YType.enumeration, 'php'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag', '')])),
                                                ('explicit_null', (YLeaf(YType.enumeration, 'explicit-null'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag', '')])),
                                                ('nflag_clear', (YLeaf(YType.enumeration, 'nflag-clear'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear', '')])),
                                            ])
                                            self.algo = None
                                            self.type = None
                                            self.value = None
                                            self.php = None
                                            self.explicit_null = None
                                            self.nflag_clear = None
                                            self._segment_path = lambda: "algorithm-prefix-sid" + "[algo='" + str(self.algo) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AlgorithmPrefixSids.AlgorithmPrefixSid, ['algo', 'type', 'value', 'php', 'explicit_null', 'nflag_clear'], name, value)


                                class AutoMetrics(Entity):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of  		 :py:class:`AutoMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics, self).__init__()

                                        self.yang_name = "auto-metrics"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("auto-metric", ("auto_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric))])
                                        self._leafs = OrderedDict()

                                        self.auto_metric = YList(self)
                                        self._segment_path = lambda: "auto-metrics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics, [], name, value)


                                    class AutoMetric(Entity):
                                        """
                                        AutoMetric Proactive\-Protect
                                        configuration. Legal value depends on
                                        the metric\-style specified for the
                                        topology. If the metric\-style defined is
                                        narrow, then only a value between <1\-63>
                                        is allowed and if the metric\-style is
                                        defined as wide, then a value between
                                        <1\-16777214> is allowed as the
                                        auto\-metric value.
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric, self).__init__()

                                            self.yang_name = "auto-metric"
                                            self.yang_parent_name = "auto-metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('proactive_protect', (YLeaf(YType.uint32, 'proactive-protect'), ['int'])),
                                            ])
                                            self.level = None
                                            self.proactive_protect = None
                                            self._segment_path = lambda: "auto-metric" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric, ['level', 'proactive_protect'], name, value)


                                class AdminTags(Entity):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of  		 :py:class:`AdminTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags, self).__init__()

                                        self.yang_name = "admin-tags"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("admin-tag", ("admin_tag", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag))])
                                        self._leafs = OrderedDict()

                                        self.admin_tag = YList(self)
                                        self._segment_path = lambda: "admin-tags"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags, [], name, value)


                                    class AdminTag(Entity):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag, self).__init__()

                                            self.yang_name = "admin-tag"
                                            self.yang_parent_name = "admin-tags"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('admin_tag', (YLeaf(YType.uint32, 'admin-tag'), ['int'])),
                                            ])
                                            self.level = None
                                            self.admin_tag = None
                                            self._segment_path = lambda: "admin-tag" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag, ['level', 'admin_tag'], name, value)


                                class InterfaceLinkGroup(Entity):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\: str
                                    
                                    	**length:** 1..40
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup, self).__init__()

                                        self.yang_name = "interface-link-group"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('link_group', (YLeaf(YType.str, 'link-group'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.link_group = None
                                        self.level = None
                                        self._segment_path = lambda: "interface-link-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup, ['link_group', 'level'], name, value)


                                class ManualAdjSids(Entity):
                                    """
                                    Manual Adjacecy SID configuration
                                    
                                    .. attribute:: manual_adj_sid
                                    
                                    	Assign adjancency SID to an interface
                                    	**type**\: list of  		 :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids, self).__init__()

                                        self.yang_name = "manual-adj-sids"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("manual-adj-sid", ("manual_adj_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid))])
                                        self._leafs = OrderedDict()

                                        self.manual_adj_sid = YList(self)
                                        self._segment_path = lambda: "manual-adj-sids"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids, [], name, value)


                                    class ManualAdjSid(Entity):
                                        """
                                        Assign adjancency SID to an interface
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: sid_type  (key)
                                        
                                        	Sid type aboslute or index
                                        	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                        
                                        .. attribute:: sid  (key)
                                        
                                        	Sid value
                                        	**type**\: int
                                        
                                        	**range:** 0..1048575
                                        
                                        .. attribute:: protected
                                        
                                        	Enable/Disable SID protection
                                        	**type**\:  :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid, self).__init__()

                                            self.yang_name = "manual-adj-sid"
                                            self.yang_parent_name = "manual-adj-sids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level','sid_type','sid']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                                ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                                ('protected', (YLeaf(YType.enumeration, 'protected'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected', '')])),
                                            ])
                                            self.level = None
                                            self.sid_type = None
                                            self.sid = None
                                            self.protected = None
                                            self._segment_path = lambda: "manual-adj-sid" + "[level='" + str(self.level) + "']" + "[sid-type='" + str(self.sid_type) + "']" + "[sid='" + str(self.sid) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                                class Metrics(Entity):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of  		 :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics, self).__init__()

                                        self.yang_name = "metrics"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("metric", ("metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric))])
                                        self._leafs = OrderedDict()

                                        self.metric = YList(self)
                                        self._segment_path = lambda: "metrics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics, [], name, value)


                                    class Metric(Entity):
                                        """
                                        Metric configuration. Legal value depends on
                                        the metric\-style specified for the topology. If
                                        the metric\-style defined is narrow, then only a
                                        value between <1\-63> is allowed and if the
                                        metric\-style is defined as wide, then a value
                                        between <1\-16777215> is allowed as the metric
                                        value.  All routers exclude links with the
                                        maximum wide metric (16777215) from their SPF
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: union of the below types:
                                        
                                        		**type**\:  :py:class:`Metric_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_>`
                                        
                                        		**type**\: int
                                        
                                        			**range:** 1..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric, self).__init__()

                                            self.yang_name = "metric"
                                            self.yang_parent_name = "metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('metric', (YLeaf(YType.str, 'metric'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis', 'Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_'),'int'])),
                                            ])
                                            self.level = None
                                            self.metric = None
                                            self._segment_path = lambda: "metric" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric, ['level', 'metric'], name, value)

                                        class Metric_(Enum):
                                            """
                                            Metric\_ (Enum Class)

                                            Allowed metric\: <1\-63> for narrow,

                                            <1\-16777215> for wide

                                            .. data:: maximum = 16777215

                                            	Maximum wide metric.  All routers will

                                            	exclude this link from their SPF

                                            """

                                            maximum = Enum.YLeaf(16777215, "maximum")



                                class Weights(Entity):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of  		 :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights, self).__init__()

                                        self.yang_name = "weights"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("weight", ("weight", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight))])
                                        self._leafs = OrderedDict()

                                        self.weight = YList(self)
                                        self._segment_path = lambda: "weights"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights, [], name, value)


                                    class Weight(Entity):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight, self).__init__()

                                            self.yang_name = "weight"
                                            self.yang_parent_name = "weights"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                                            ])
                                            self.level = None
                                            self.weight = None
                                            self._segment_path = lambda: "weight" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight, ['level', 'weight'], name, value)


                            class TopologyName(Entity):
                                """
                                keys\: topology\-name
                                
                                .. attribute:: topology_name  (key)
                                
                                	Topology Name
                                	**type**\: str
                                
                                	**length:** 1..32
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:  :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\:  :py:class:`InterfaceFrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\:  :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp>`
                                
                                .. attribute:: prefix_sspfsid
                                
                                	Assign prefix SSPF SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:  :py:class:`PrefixSspfsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: algorithm_prefix_sids
                                
                                	Algorithm SID Table
                                	**type**\:  :py:class:`AlgorithmPrefixSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\:  :py:class:`AutoMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics>`
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\:  :py:class:`AdminTags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\:  :py:class:`InterfaceLinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\:  :py:class:`IsisInterfaceAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfState>`
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: manual_adj_sids
                                
                                	Manual Adjacecy SID configuration
                                	**type**\:  :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids>`
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\:  :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\:  :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2018-06-14'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName, self).__init__()

                                    self.yang_name = "topology-name"
                                    self.yang_parent_name = "interface-af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['topology_name']
                                    self._child_classes = OrderedDict([("prefix-sid", ("prefix_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid)), ("interface-frr-table", ("interface_frr_table", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable)), ("mpls-ldp", ("mpls_ldp", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp)), ("prefix-sspfsid", ("prefix_sspfsid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid)), ("algorithm-prefix-sids", ("algorithm_prefix_sids", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids)), ("auto-metrics", ("auto_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics)), ("admin-tags", ("admin_tags", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags)), ("interface-link-group", ("interface_link_group", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup)), ("manual-adj-sids", ("manual_adj_sids", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids)), ("metrics", ("metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics)), ("weights", ("weights", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights))])
                                    self._leafs = OrderedDict([
                                        ('topology_name', (YLeaf(YType.str, 'topology-name'), ['str'])),
                                        ('interface_af_state', (YLeaf(YType.enumeration, 'interface-af-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceAfState', '')])),
                                        ('running', (YLeaf(YType.empty, 'running'), ['Empty'])),
                                    ])
                                    self.topology_name = None
                                    self.interface_af_state = None
                                    self.running = None

                                    self.prefix_sid = None
                                    self._children_name_map["prefix_sid"] = "prefix-sid"

                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self._children_name_map["interface_frr_table"] = "interface-frr-table"

                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self._children_name_map["mpls_ldp"] = "mpls-ldp"

                                    self.prefix_sspfsid = None
                                    self._children_name_map["prefix_sspfsid"] = "prefix-sspfsid"

                                    self.algorithm_prefix_sids = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids()
                                    self.algorithm_prefix_sids.parent = self
                                    self._children_name_map["algorithm_prefix_sids"] = "algorithm-prefix-sids"

                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self._children_name_map["auto_metrics"] = "auto-metrics"

                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags()
                                    self.admin_tags.parent = self
                                    self._children_name_map["admin_tags"] = "admin-tags"

                                    self.interface_link_group = None
                                    self._children_name_map["interface_link_group"] = "interface-link-group"

                                    self.manual_adj_sids = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids()
                                    self.manual_adj_sids.parent = self
                                    self._children_name_map["manual_adj_sids"] = "manual-adj-sids"

                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics()
                                    self.metrics.parent = self
                                    self._children_name_map["metrics"] = "metrics"

                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights()
                                    self.weights.parent = self
                                    self._children_name_map["weights"] = "weights"
                                    self._segment_path = lambda: "topology-name" + "[topology-name='" + str(self.topology_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName, ['topology_name', 'interface_af_state', 'running'], name, value)


                                class PrefixSid(Entity):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:  :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:  :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:  :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid, self).__init__()

                                        self.yang_name = "prefix-sid"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                            ('php', (YLeaf(YType.enumeration, 'php'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag', '')])),
                                            ('explicit_null', (YLeaf(YType.enumeration, 'explicit-null'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag', '')])),
                                            ('nflag_clear', (YLeaf(YType.enumeration, 'nflag-clear'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear', '')])),
                                        ])
                                        self.type = None
                                        self.value = None
                                        self.php = None
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self._segment_path = lambda: "prefix-sid"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid, ['type', 'value', 'php', 'explicit_null', 'nflag_clear'], name, value)


                                class InterfaceFrrTable(Entity):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\:  :py:class:`FrrlfaCandidateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\:  :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\:  :py:class:`FrrTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\:  :py:class:`FrrRemoteLfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: interface_frr_tiebreaker_defaults
                                    
                                    	Interface FRR Default tiebreaker configuration
                                    	**type**\:  :py:class:`InterfaceFrrTiebreakerDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\:  :py:class:`FrrtilfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\:  :py:class:`FrrExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: interface_frr_tiebreakers
                                    
                                    	Interface FRR tiebreakers configuration
                                    	**type**\:  :py:class:`InterfaceFrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable, self).__init__()

                                        self.yang_name = "interface-frr-table"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("frrlfa-candidate-interfaces", ("frrlfa_candidate_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces)), ("frr-remote-lfa-max-metrics", ("frr_remote_lfa_max_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics)), ("frr-types", ("frr_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes)), ("frr-remote-lfa-types", ("frr_remote_lfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes)), ("interface-frr-tiebreaker-defaults", ("interface_frr_tiebreaker_defaults", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults)), ("frrtilfa-types", ("frrtilfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes)), ("frr-exclude-interfaces", ("frr_exclude_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces)), ("interface-frr-tiebreakers", ("interface_frr_tiebreakers", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers))])
                                        self._leafs = OrderedDict()

                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self._children_name_map["frrlfa_candidate_interfaces"] = "frrlfa-candidate-interfaces"

                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self._children_name_map["frr_remote_lfa_max_metrics"] = "frr-remote-lfa-max-metrics"

                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self._children_name_map["frr_types"] = "frr-types"

                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self._children_name_map["frr_remote_lfa_types"] = "frr-remote-lfa-types"

                                        self.interface_frr_tiebreaker_defaults = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults()
                                        self.interface_frr_tiebreaker_defaults.parent = self
                                        self._children_name_map["interface_frr_tiebreaker_defaults"] = "interface-frr-tiebreaker-defaults"

                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self
                                        self._children_name_map["frrtilfa_types"] = "frrtilfa-types"

                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self._children_name_map["frr_exclude_interfaces"] = "frr-exclude-interfaces"

                                        self.interface_frr_tiebreakers = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers()
                                        self.interface_frr_tiebreakers.parent = self
                                        self._children_name_map["interface_frr_tiebreakers"] = "interface-frr-tiebreakers"
                                        self._segment_path = lambda: "interface-frr-table"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable, [], name, value)


                                    class FrrlfaCandidateInterfaces(Entity):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of  		 :py:class:`FrrlfaCandidateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces, self).__init__()

                                            self.yang_name = "frrlfa-candidate-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frrlfa-candidate-interface", ("frrlfa_candidate_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface))])
                                            self._leafs = OrderedDict()

                                            self.frrlfa_candidate_interface = YList(self)
                                            self._segment_path = lambda: "frrlfa-candidate-interfaces"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces, [], name, value)


                                        class FrrlfaCandidateInterface(Entity):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: interface_name  (key)
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            .. attribute:: frr_type  (key)
                                            
                                            	Computation Type
                                            	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, self).__init__()

                                                self.yang_name = "frrlfa-candidate-interface"
                                                self.yang_parent_name = "frrlfa-candidate-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['interface_name','frr_type']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                    ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                    ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                                ])
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None
                                                self._segment_path = lambda: "frrlfa-candidate-interface" + "[interface-name='" + str(self.interface_name) + "']" + "[frr-type='" + str(self.frr_type) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class FrrRemoteLfaMaxMetrics(Entity):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of  		 :py:class:`FrrRemoteLfaMaxMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, self).__init__()

                                            self.yang_name = "frr-remote-lfa-max-metrics"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-remote-lfa-max-metric", ("frr_remote_lfa_max_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric))])
                                            self._leafs = OrderedDict()

                                            self.frr_remote_lfa_max_metric = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-max-metrics"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, [], name, value)


                                        class FrrRemoteLfaMaxMetric(Entity):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\: int
                                            
                                            	**range:** 1..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, self).__init__()

                                                self.yang_name = "frr-remote-lfa-max-metric"
                                                self.yang_parent_name = "frr-remote-lfa-max-metrics"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('max_metric', (YLeaf(YType.uint32, 'max-metric'), ['int'])),
                                                ])
                                                self.level = None
                                                self.max_metric = None
                                                self._segment_path = lambda: "frr-remote-lfa-max-metric" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, ['level', 'max_metric'], name, value)


                                    class FrrTypes(Entity):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of  		 :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes, self).__init__()

                                            self.yang_name = "frr-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-type", ("frr_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType))])
                                            self._leafs = OrderedDict()

                                            self.frr_type = YList(self)
                                            self._segment_path = lambda: "frr-types"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes, [], name, value)


                                        class FrrType(Entity):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType, self).__init__()

                                                self.yang_name = "frr-type"
                                                self.yang_parent_name = "frr-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                ])
                                                self.level = None
                                                self.type = None
                                                self._segment_path = lambda: "frr-type" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType, ['level', 'type'], name, value)


                                    class FrrRemoteLfaTypes(Entity):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of  		 :py:class:`FrrRemoteLfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes, self).__init__()

                                            self.yang_name = "frr-remote-lfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-remote-lfa-type", ("frr_remote_lfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType))])
                                            self._leafs = OrderedDict()

                                            self.frr_remote_lfa_type = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-types"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes, [], name, value)


                                        class FrrRemoteLfaType(Entity):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\:  :py:class:`IsisRemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfa>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, self).__init__()

                                                self.yang_name = "frr-remote-lfa-type"
                                                self.yang_parent_name = "frr-remote-lfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisRemoteLfa', '')])),
                                                ])
                                                self.level = None
                                                self.type = None
                                                self._segment_path = lambda: "frr-remote-lfa-type" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, ['level', 'type'], name, value)


                                    class InterfaceFrrTiebreakerDefaults(Entity):
                                        """
                                        Interface FRR Default tiebreaker
                                        configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker_default
                                        
                                        	Configure default tiebreaker
                                        	**type**\: list of  		 :py:class:`InterfaceFrrTiebreakerDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, self).__init__()

                                            self.yang_name = "interface-frr-tiebreaker-defaults"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface-frr-tiebreaker-default", ("interface_frr_tiebreaker_default", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault))])
                                            self._leafs = OrderedDict()

                                            self.interface_frr_tiebreaker_default = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreaker-defaults"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, [], name, value)


                                        class InterfaceFrrTiebreakerDefault(Entity):
                                            """
                                            Configure default tiebreaker
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker-default"
                                                self.yang_parent_name = "interface-frr-tiebreaker-defaults"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ])
                                                self.level = None
                                                self._segment_path = lambda: "interface-frr-tiebreaker-default" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, ['level'], name, value)


                                    class FrrtilfaTypes(Entity):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of  		 :py:class:`FrrtilfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes, self).__init__()

                                            self.yang_name = "frrtilfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frrtilfa-type", ("frrtilfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType))])
                                            self._leafs = OrderedDict()

                                            self.frrtilfa_type = YList(self)
                                            self._segment_path = lambda: "frrtilfa-types"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes, [], name, value)


                                        class FrrtilfaType(Entity):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, self).__init__()

                                                self.yang_name = "frrtilfa-type"
                                                self.yang_parent_name = "frrtilfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ])
                                                self.level = None
                                                self._segment_path = lambda: "frrtilfa-type" + "[level='" + str(self.level) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, ['level'], name, value)


                                    class FrrExcludeInterfaces(Entity):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of  		 :py:class:`FrrExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces, self).__init__()

                                            self.yang_name = "frr-exclude-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("frr-exclude-interface", ("frr_exclude_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface))])
                                            self._leafs = OrderedDict()

                                            self.frr_exclude_interface = YList(self)
                                            self._segment_path = lambda: "frr-exclude-interfaces"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces, [], name, value)


                                        class FrrExcludeInterface(Entity):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: interface_name  (key)
                                            
                                            	Interface
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            .. attribute:: frr_type  (key)
                                            
                                            	Computation Type
                                            	**type**\:  :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\: int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, self).__init__()

                                                self.yang_name = "frr-exclude-interface"
                                                self.yang_parent_name = "frr-exclude-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['interface_name','frr_type']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                    ('frr_type', (YLeaf(YType.enumeration, 'frr-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isisfrr', '')])),
                                                    ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                                ])
                                                self.interface_name = None
                                                self.frr_type = None
                                                self.level = None
                                                self._segment_path = lambda: "frr-exclude-interface" + "[interface-name='" + str(self.interface_name) + "']" + "[frr-type='" + str(self.frr_type) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class InterfaceFrrTiebreakers(Entity):
                                        """
                                        Interface FRR tiebreakers configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker
                                        
                                        	Configure tiebreaker for multiple backups
                                        	**type**\: list of  		 :py:class:`InterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers, self).__init__()

                                            self.yang_name = "interface-frr-tiebreakers"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface-frr-tiebreaker", ("interface_frr_tiebreaker", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker))])
                                            self._leafs = OrderedDict()

                                            self.interface_frr_tiebreaker = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreakers"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers, [], name, value)


                                        class InterfaceFrrTiebreaker(Entity):
                                            """
                                            Configure tiebreaker for multiple
                                            backups
                                            
                                            .. attribute:: level  (key)
                                            
                                            	Level to which configuration applies
                                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: tiebreaker  (key)
                                            
                                            	Tiebreaker for which configuration applies
                                            	**type**\:  :py:class:`IsisInterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceFrrTiebreaker>`
                                            
                                            .. attribute:: index
                                            
                                            	Preference order among tiebreakers
                                            	**type**\: int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2018-06-14'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker"
                                                self.yang_parent_name = "interface-frr-tiebreakers"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['level','tiebreaker']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                    ('tiebreaker', (YLeaf(YType.enumeration, 'tiebreaker'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisInterfaceFrrTiebreaker', '')])),
                                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                                ])
                                                self.level = None
                                                self.tiebreaker = None
                                                self.index = None
                                                self._segment_path = lambda: "interface-frr-tiebreaker" + "[level='" + str(self.level) + "']" + "[tiebreaker='" + str(self.tiebreaker) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                                class MplsLdp(Entity):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp, self).__init__()

                                        self.yang_name = "mpls-ldp"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('sync_level', (YLeaf(YType.uint32, 'sync-level'), ['int'])),
                                        ])
                                        self.sync_level = None
                                        self._segment_path = lambda: "mpls-ldp"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp, ['sync_level'], name, value)


                                class PrefixSspfsid(Entity):
                                    """
                                    Assign prefix SSPF SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\: int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:  :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:  :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:  :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid, self).__init__()

                                        self.yang_name = "prefix-sspfsid"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                            ('php', (YLeaf(YType.enumeration, 'php'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag', '')])),
                                            ('explicit_null', (YLeaf(YType.enumeration, 'explicit-null'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag', '')])),
                                            ('nflag_clear', (YLeaf(YType.enumeration, 'nflag-clear'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear', '')])),
                                        ])
                                        self.type = None
                                        self.value = None
                                        self.php = None
                                        self.explicit_null = None
                                        self.nflag_clear = None
                                        self._segment_path = lambda: "prefix-sspfsid"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid, ['type', 'value', 'php', 'explicit_null', 'nflag_clear'], name, value)


                                class AlgorithmPrefixSids(Entity):
                                    """
                                    Algorithm SID Table
                                    
                                    .. attribute:: algorithm_prefix_sid
                                    
                                    	Assign prefix SID for algorithm to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                    	**type**\: list of  		 :py:class:`AlgorithmPrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids, self).__init__()

                                        self.yang_name = "algorithm-prefix-sids"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("algorithm-prefix-sid", ("algorithm_prefix_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid))])
                                        self._leafs = OrderedDict()

                                        self.algorithm_prefix_sid = YList(self)
                                        self._segment_path = lambda: "algorithm-prefix-sids"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids, [], name, value)


                                    class AlgorithmPrefixSid(Entity):
                                        """
                                        Assign prefix SID for algorithm to an
                                        interface, ISISPHPFlag will be rejected
                                        if set to disable, ISISEXPLICITNULLFlag
                                        will override the value of ISISPHPFlag
                                        
                                        .. attribute:: algo  (key)
                                        
                                        	Algorithm
                                        	**type**\: int
                                        
                                        	**range:** 128..255
                                        
                                        .. attribute:: type
                                        
                                        	SID type for the interface
                                        	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: value
                                        
                                        	SID value for the interface
                                        	**type**\: int
                                        
                                        	**range:** 0..1048575
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: php
                                        
                                        	Enable/Disable Penultimate Hop Popping
                                        	**type**\:  :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: explicit_null
                                        
                                        	Enable/Disable Explicit\-NULL flag
                                        	**type**\:  :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: nflag_clear
                                        
                                        	Clear N\-flag for the prefix\-SID
                                        	**type**\:  :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid, self).__init__()

                                            self.yang_name = "algorithm-prefix-sid"
                                            self.yang_parent_name = "algorithm-prefix-sids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['algo']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('algo', (YLeaf(YType.uint32, 'algo'), ['int'])),
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                                ('php', (YLeaf(YType.enumeration, 'php'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisphpFlag', '')])),
                                                ('explicit_null', (YLeaf(YType.enumeration, 'explicit-null'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisexplicitNullFlag', '')])),
                                                ('nflag_clear', (YLeaf(YType.enumeration, 'nflag-clear'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'NflagClear', '')])),
                                            ])
                                            self.algo = None
                                            self.type = None
                                            self.value = None
                                            self.php = None
                                            self.explicit_null = None
                                            self.nflag_clear = None
                                            self._segment_path = lambda: "algorithm-prefix-sid" + "[algo='" + str(self.algo) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AlgorithmPrefixSids.AlgorithmPrefixSid, ['algo', 'type', 'value', 'php', 'explicit_null', 'nflag_clear'], name, value)


                                class AutoMetrics(Entity):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of  		 :py:class:`AutoMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics, self).__init__()

                                        self.yang_name = "auto-metrics"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("auto-metric", ("auto_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric))])
                                        self._leafs = OrderedDict()

                                        self.auto_metric = YList(self)
                                        self._segment_path = lambda: "auto-metrics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics, [], name, value)


                                    class AutoMetric(Entity):
                                        """
                                        AutoMetric Proactive\-Protect
                                        configuration. Legal value depends on
                                        the metric\-style specified for the
                                        topology. If the metric\-style defined is
                                        narrow, then only a value between <1\-63>
                                        is allowed and if the metric\-style is
                                        defined as wide, then a value between
                                        <1\-16777214> is allowed as the
                                        auto\-metric value.
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric, self).__init__()

                                            self.yang_name = "auto-metric"
                                            self.yang_parent_name = "auto-metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('proactive_protect', (YLeaf(YType.uint32, 'proactive-protect'), ['int'])),
                                            ])
                                            self.level = None
                                            self.proactive_protect = None
                                            self._segment_path = lambda: "auto-metric" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric, ['level', 'proactive_protect'], name, value)


                                class AdminTags(Entity):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of  		 :py:class:`AdminTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags, self).__init__()

                                        self.yang_name = "admin-tags"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("admin-tag", ("admin_tag", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag))])
                                        self._leafs = OrderedDict()

                                        self.admin_tag = YList(self)
                                        self._segment_path = lambda: "admin-tags"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags, [], name, value)


                                    class AdminTag(Entity):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag, self).__init__()

                                            self.yang_name = "admin-tag"
                                            self.yang_parent_name = "admin-tags"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('admin_tag', (YLeaf(YType.uint32, 'admin-tag'), ['int'])),
                                            ])
                                            self.level = None
                                            self.admin_tag = None
                                            self._segment_path = lambda: "admin-tag" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag, ['level', 'admin_tag'], name, value)


                                class InterfaceLinkGroup(Entity):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\: str
                                    
                                    	**length:** 1..40
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\: int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup, self).__init__()

                                        self.yang_name = "interface-link-group"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('link_group', (YLeaf(YType.str, 'link-group'), ['str'])),
                                            ('level', (YLeaf(YType.uint32, 'level'), ['int'])),
                                        ])
                                        self.link_group = None
                                        self.level = None
                                        self._segment_path = lambda: "interface-link-group"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup, ['link_group', 'level'], name, value)


                                class ManualAdjSids(Entity):
                                    """
                                    Manual Adjacecy SID configuration
                                    
                                    .. attribute:: manual_adj_sid
                                    
                                    	Assign adjancency SID to an interface
                                    	**type**\: list of  		 :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids, self).__init__()

                                        self.yang_name = "manual-adj-sids"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("manual-adj-sid", ("manual_adj_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid))])
                                        self._leafs = OrderedDict()

                                        self.manual_adj_sid = YList(self)
                                        self._segment_path = lambda: "manual-adj-sids"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids, [], name, value)


                                    class ManualAdjSid(Entity):
                                        """
                                        Assign adjancency SID to an interface
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: sid_type  (key)
                                        
                                        	Sid type aboslute or index
                                        	**type**\:  :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                        
                                        .. attribute:: sid  (key)
                                        
                                        	Sid value
                                        	**type**\: int
                                        
                                        	**range:** 0..1048575
                                        
                                        .. attribute:: protected
                                        
                                        	Enable/Disable SID protection
                                        	**type**\:  :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid, self).__init__()

                                            self.yang_name = "manual-adj-sid"
                                            self.yang_parent_name = "manual-adj-sids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level','sid_type','sid']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('sid_type', (YLeaf(YType.enumeration, 'sid-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isissid1', '')])),
                                                ('sid', (YLeaf(YType.uint32, 'sid'), ['int'])),
                                                ('protected', (YLeaf(YType.enumeration, 'protected'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsissidProtected', '')])),
                                            ])
                                            self.level = None
                                            self.sid_type = None
                                            self.sid = None
                                            self.protected = None
                                            self._segment_path = lambda: "manual-adj-sid" + "[level='" + str(self.level) + "']" + "[sid-type='" + str(self.sid_type) + "']" + "[sid='" + str(self.sid) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                                class Metrics(Entity):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of  		 :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics, self).__init__()

                                        self.yang_name = "metrics"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("metric", ("metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric))])
                                        self._leafs = OrderedDict()

                                        self.metric = YList(self)
                                        self._segment_path = lambda: "metrics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics, [], name, value)


                                    class Metric(Entity):
                                        """
                                        Metric configuration. Legal value depends on
                                        the metric\-style specified for the topology. If
                                        the metric\-style defined is narrow, then only a
                                        value between <1\-63> is allowed and if the
                                        metric\-style is defined as wide, then a value
                                        between <1\-16777215> is allowed as the metric
                                        value.  All routers exclude links with the
                                        maximum wide metric (16777215) from their SPF
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: union of the below types:
                                        
                                        		**type**\:  :py:class:`Metric_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_>`
                                        
                                        		**type**\: int
                                        
                                        			**range:** 1..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric, self).__init__()

                                            self.yang_name = "metric"
                                            self.yang_parent_name = "metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('metric', (YLeaf(YType.str, 'metric'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'Isis', 'Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric_'),'int'])),
                                            ])
                                            self.level = None
                                            self.metric = None
                                            self._segment_path = lambda: "metric" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric, ['level', 'metric'], name, value)

                                        class Metric_(Enum):
                                            """
                                            Metric\_ (Enum Class)

                                            Allowed metric\: <1\-63> for narrow,

                                            <1\-16777215> for wide

                                            .. data:: maximum = 16777215

                                            	Maximum wide metric.  All routers will

                                            	exclude this link from their SPF

                                            """

                                            maximum = Enum.YLeaf(16777215, "maximum")



                                class Weights(Entity):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of  		 :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2018-06-14'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights, self).__init__()

                                        self.yang_name = "weights"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("weight", ("weight", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight))])
                                        self._leafs = OrderedDict()

                                        self.weight = YList(self)
                                        self._segment_path = lambda: "weights"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights, [], name, value)


                                    class Weight(Entity):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level  (key)
                                        
                                        	Level to which configuration applies
                                        	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\: int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2018-06-14'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight, self).__init__()

                                            self.yang_name = "weight"
                                            self.yang_parent_name = "weights"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['level']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                                ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                                            ])
                                            self.level = None
                                            self.weight = None
                                            self._segment_path = lambda: "weight" + "[level='" + str(self.level) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight, ['level', 'weight'], name, value)


                    class CsnpIntervals(Entity):
                        """
                        CSNP\-interval configuration
                        
                        .. attribute:: csnp_interval
                        
                        	CSNP\-interval configuration. No fixed default value as this depends on the media type of the interface
                        	**type**\: list of  		 :py:class:`CsnpInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals, self).__init__()

                            self.yang_name = "csnp-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("csnp-interval", ("csnp_interval", Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval))])
                            self._leafs = OrderedDict()

                            self.csnp_interval = YList(self)
                            self._segment_path = lambda: "csnp-intervals"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals, [], name, value)


                        class CsnpInterval(Entity):
                            """
                            CSNP\-interval configuration. No fixed
                            default value as this depends on the media
                            type of the interface.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval, self).__init__()

                                self.yang_name = "csnp-interval"
                                self.yang_parent_name = "csnp-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.level = None
                                self.interval = None
                                self._segment_path = lambda: "csnp-interval" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval, ['level', 'interval'], name, value)


                    class LspIntervals(Entity):
                        """
                        LSP\-interval configuration
                        
                        .. attribute:: lsp_interval
                        
                        	Interval between transmission of LSPs on interface
                        	**type**\: list of  		 :py:class:`LspInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2018-06-14'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspIntervals, self).__init__()

                            self.yang_name = "lsp-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("lsp-interval", ("lsp_interval", Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval))])
                            self._leafs = OrderedDict()

                            self.lsp_interval = YList(self)
                            self._segment_path = lambda: "lsp-intervals"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspIntervals, [], name, value)


                        class LspInterval(Entity):
                            """
                            Interval between transmission of LSPs on
                            interface.
                            
                            .. attribute:: level  (key)
                            
                            	Level to which configuration applies
                            	**type**\:  :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2018-06-14'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval, self).__init__()

                                self.yang_name = "lsp-interval"
                                self.yang_parent_name = "lsp-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['level']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('level', (YLeaf(YType.enumeration, 'level'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes', 'IsisInternalLevel', '')])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.level = None
                                self.interval = None
                                self._segment_path = lambda: "lsp-interval" + "[level='" + str(self.level) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval, ['level', 'interval'], name, value)

    def clone_ptr(self):
        self._top_entity = Isis()
        return self._top_entity

