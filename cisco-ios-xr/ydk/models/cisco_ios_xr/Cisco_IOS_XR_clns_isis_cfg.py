""" Cisco_IOS_XR_clns_isis_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR clns\-isis package configuration.

This module contains definitions
for the following management objects\:
  isis\: IS\-IS configuration for all instances

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IsisAdjCheck(Enum):
    """
    IsisAdjCheck

    Isis adj check

    .. data:: disabled = 0

    	Disabled

    """

    disabled = Enum.YLeaf(0, "disabled")


class IsisAdvTypeExternal(Enum):
    """
    IsisAdvTypeExternal

    Isis adv type external

    .. data:: external = 1

    	External

    """

    external = Enum.YLeaf(1, "external")


class IsisAdvTypeInterLevel(Enum):
    """
    IsisAdvTypeInterLevel

    Isis adv type inter level

    .. data:: inter_level = 1

    	InterLevel

    """

    inter_level = Enum.YLeaf(1, "inter-level")


class IsisApplyWeight(Enum):
    """
    IsisApplyWeight

    Isis apply weight

    .. data:: ecmp_only = 1

    	Apply weight to ECMP prefixes

    .. data:: ucmp_only = 2

    	Apply weight to UCMP prefixes

    """

    ecmp_only = Enum.YLeaf(1, "ecmp-only")

    ucmp_only = Enum.YLeaf(2, "ucmp-only")


class IsisAttachedBit(Enum):
    """
    IsisAttachedBit

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
    IsisAuthenticationAlgorithm

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
    IsisAuthenticationFailureMode

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
    IsisConfigurableLevels

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


class IsisHelloPadding(Enum):
    """
    IsisHelloPadding

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
    IsisInterfaceAfState

    Isis interface af state

    .. data:: disable = 0

    	Disable

    """

    disable = Enum.YLeaf(0, "disable")


class IsisInterfaceFrrTiebreaker(Enum):
    """
    IsisInterfaceFrrTiebreaker

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
    IsisInterfaceState

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
    IsisLabelPreference

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
    IsisMetric

    Isis metric

    .. data:: internal = 0

    	Internal metric

    .. data:: external = 1

    	External metric

    """

    internal = Enum.YLeaf(0, "internal")

    external = Enum.YLeaf(1, "external")


class IsisMetricStyle(Enum):
    """
    IsisMetricStyle

    Isis metric style

    .. data:: old_metric_style = 0

    	ISO 10589 metric style (old-style)

    .. data:: new_metric_style = 1

    	32-bit metric style (new-style)

    .. data:: both_metric_style = 2

    	Both forms of metric style

    """

    old_metric_style = Enum.YLeaf(0, "old-metric-style")

    new_metric_style = Enum.YLeaf(1, "new-metric-style")

    both_metric_style = Enum.YLeaf(2, "both-metric-style")


class IsisMetricStyleTransition(Enum):
    """
    IsisMetricStyleTransition

    Isis metric style transition

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


class IsisMibAdjacencyChangeBoolean(Enum):
    """
    IsisMibAdjacencyChangeBoolean

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
    IsisMibAllBoolean

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
    IsisMibAreaMismatchBoolean

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
    IsisMibAttemptToExceedMaxSequenceBoolean

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
    IsisMibAuthenticationFailureBoolean

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
    IsisMibAuthenticationTypeFailureBoolean

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
    IsisMibCorruptedLspDetectedBoolean

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
    IsisMibDatabaseOverFlowBoolean

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
    IsisMibIdLengthMismatchBoolean

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
    IsisMibLspErrorDetectedBoolean

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
    IsisMibLspTooLargeToPropagateBoolean

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
    IsisMibManualAddressDropsBoolean

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
    IsisMibMaxAreaAddressMismatchBoolean

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
    IsisMibOriginatedLspBufferSizeMismatchBoolean

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
    IsisMibOwnLspPurgeBoolean

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
    IsisMibProtocolsSupportedMismatchBoolean

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
    IsisMibRejectedAdjacencyBoolean

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
    IsisMibSequenceNumberSkipBoolean

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
    IsisMibVersionSkewBoolean

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
    IsisMicroLoopAvoidance

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
    IsisNsfFlavor

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
    IsisOverloadBitMode

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
    IsisPrefixPriority

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
    IsisRedistProto

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
    IsisRemoteLfa

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
    IsisSnpAuth

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
    IsisTracingMode

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
    IsisexplicitNullFlag

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
    Isisfrr

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
    IsisfrrLoadSharing

    Isisfrr load sharing

    .. data:: disable = 1

    	Disable load sharing of prefixes across

    	multiple backups

    """

    disable = Enum.YLeaf(1, "disable")


class IsisfrrTiebreaker(Enum):
    """
    IsisfrrTiebreaker

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
    IsisispfState

    Isisispf state

    .. data:: enabled = 1

    	Enabled

    """

    enabled = Enum.YLeaf(1, "enabled")


class IsisphpFlag(Enum):
    """
    IsisphpFlag

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
    Isissid1

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
    IsissidProtected

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
    NflagClear

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
    	**type**\:   :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances>`
    
    

    """

    _prefix = 'clns-isis-cfg'
    _revision = '2017-06-02'

    def __init__(self):
        super(Isis, self).__init__()
        self._top_entity = None

        self.yang_name = "isis"
        self.yang_parent_name = "Cisco-IOS-XR-clns-isis-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"instances" : ("instances", Isis.Instances)}
        self._child_list_classes = {}

        self.instances = Isis.Instances()
        self.instances.parent = self
        self._children_name_map["instances"] = "instances"
        self._children_yang_names.add("instances")
        self._segment_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis"


    class Instances(Entity):
        """
        IS\-IS instance configuration
        
        .. attribute:: instance
        
        	Configuration for a single IS\-IS instance
        	**type**\: list of    :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance>`
        
        

        """

        _prefix = 'clns-isis-cfg'
        _revision = '2017-06-02'

        def __init__(self):
            super(Isis.Instances, self).__init__()

            self.yang_name = "instances"
            self.yang_parent_name = "isis"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"instance" : ("instance", Isis.Instances.Instance)}

            self.instance = YList(self)
            self._segment_path = lambda: "instances"
            self._absolute_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Isis.Instances, [], name, value)


        class Instance(Entity):
            """
            Configuration for a single IS\-IS instance
            
            .. attribute:: instance_name  <key>
            
            	Instance identifier
            	**type**\:  str
            
            	**length:** 1..40
            
            .. attribute:: adjacency_stagger
            
            	Stagger ISIS adjacency bring up
            	**type**\:   :py:class:`AdjacencyStagger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.AdjacencyStagger>`
            
            	**presence node**\: True
            
            .. attribute:: afs
            
            	Per\-address\-family configuration
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs>`
            
            .. attribute:: distribute
            
            	IS\-IS Distribute BGP\-LS configuration
            	**type**\:   :py:class:`Distribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Distribute>`
            
            	**presence node**\: True
            
            .. attribute:: dynamic_host_name
            
            	If TRUE, dynamic hostname resolution is disabled, and system IDs will always be displayed by show and debug output
            	**type**\:  bool
            
            .. attribute:: ignore_lsp_errors
            
            	If TRUE, LSPs recieved with bad checksums will result in the purging of that LSP from the LSP DB. If FALSE or not set, the received LSP will just be ignored
            	**type**\:  bool
            
            .. attribute:: instance_id
            
            	Instance ID of the IS\-IS process
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**default value**\: 0
            
            .. attribute:: interfaces
            
            	Per\-interface configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces>`
            
            .. attribute:: is_type
            
            	IS type of the IS\-IS process
            	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
            
            	**default value**\: level1-and2
            
            .. attribute:: link_groups
            
            	Link Group
            	**type**\:   :py:class:`LinkGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups>`
            
            .. attribute:: log_adjacency_changes
            
            	Log changes in adjacency state
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: log_pdu_drops
            
            	Log PDU drops
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: lsp_accept_passwords
            
            	LSP/SNP accept password configuration
            	**type**\:   :py:class:`LspAcceptPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords>`
            
            .. attribute:: lsp_arrival_times
            
            	LSP arrival time configuration
            	**type**\:   :py:class:`LspArrivalTimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes>`
            
            .. attribute:: lsp_check_intervals
            
            	LSP checksum check interval configuration
            	**type**\:   :py:class:`LspCheckIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals>`
            
            .. attribute:: lsp_generation_intervals
            
            	LSP generation\-interval configuration
            	**type**\:   :py:class:`LspGenerationIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals>`
            
            .. attribute:: lsp_lifetimes
            
            	LSP lifetime configuration
            	**type**\:   :py:class:`LspLifetimes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes>`
            
            .. attribute:: lsp_mtus
            
            	LSP MTU configuration
            	**type**\:   :py:class:`LspMtus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus>`
            
            .. attribute:: lsp_passwords
            
            	LSP/SNP password configuration
            	**type**\:   :py:class:`LspPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords>`
            
            .. attribute:: lsp_refresh_intervals
            
            	LSP refresh\-interval configuration
            	**type**\:   :py:class:`LspRefreshIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals>`
            
            .. attribute:: max_link_metrics
            
            	Max Link Metric configuration
            	**type**\:   :py:class:`MaxLinkMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics>`
            
            .. attribute:: nets
            
            	NET configuration
            	**type**\:   :py:class:`Nets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets>`
            
            .. attribute:: nsf
            
            	IS\-IS NSF configuration
            	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nsf>`
            
            .. attribute:: nsr
            
            	IS\-IS NSR configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: overload_bits
            
            	LSP overload\-bit configuration
            	**type**\:   :py:class:`OverloadBits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits>`
            
            .. attribute:: running
            
            	Flag to indicate that instance should be running.  This must be the first object created when an IS\-IS instance is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS instance will exit
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: srgb
            
            	Segment Routing Global Block configuration
            	**type**\:   :py:class:`Srgb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Srgb>`
            
            	**presence node**\: True
            
            .. attribute:: trace_buffer_size
            
            	Trace buffer size configuration
            	**type**\:   :py:class:`TraceBufferSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.TraceBufferSize>`
            
            .. attribute:: tracing_mode
            
            	Tracing mode configuration
            	**type**\:   :py:class:`IsisTracingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisTracingMode>`
            
            	**default value**\: basic
            
            

            """

            _prefix = 'clns-isis-cfg'
            _revision = '2017-06-02'

            def __init__(self):
                super(Isis.Instances.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "instances"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"adjacency-stagger" : ("adjacency_stagger", Isis.Instances.Instance.AdjacencyStagger), "afs" : ("afs", Isis.Instances.Instance.Afs), "distribute" : ("distribute", Isis.Instances.Instance.Distribute), "interfaces" : ("interfaces", Isis.Instances.Instance.Interfaces), "link-groups" : ("link_groups", Isis.Instances.Instance.LinkGroups), "lsp-accept-passwords" : ("lsp_accept_passwords", Isis.Instances.Instance.LspAcceptPasswords), "lsp-arrival-times" : ("lsp_arrival_times", Isis.Instances.Instance.LspArrivalTimes), "lsp-check-intervals" : ("lsp_check_intervals", Isis.Instances.Instance.LspCheckIntervals), "lsp-generation-intervals" : ("lsp_generation_intervals", Isis.Instances.Instance.LspGenerationIntervals), "lsp-lifetimes" : ("lsp_lifetimes", Isis.Instances.Instance.LspLifetimes), "lsp-mtus" : ("lsp_mtus", Isis.Instances.Instance.LspMtus), "lsp-passwords" : ("lsp_passwords", Isis.Instances.Instance.LspPasswords), "lsp-refresh-intervals" : ("lsp_refresh_intervals", Isis.Instances.Instance.LspRefreshIntervals), "max-link-metrics" : ("max_link_metrics", Isis.Instances.Instance.MaxLinkMetrics), "nets" : ("nets", Isis.Instances.Instance.Nets), "nsf" : ("nsf", Isis.Instances.Instance.Nsf), "overload-bits" : ("overload_bits", Isis.Instances.Instance.OverloadBits), "srgb" : ("srgb", Isis.Instances.Instance.Srgb), "trace-buffer-size" : ("trace_buffer_size", Isis.Instances.Instance.TraceBufferSize)}
                self._child_list_classes = {}

                self.instance_name = YLeaf(YType.str, "instance-name")

                self.dynamic_host_name = YLeaf(YType.boolean, "dynamic-host-name")

                self.ignore_lsp_errors = YLeaf(YType.boolean, "ignore-lsp-errors")

                self.instance_id = YLeaf(YType.uint32, "instance-id")

                self.is_type = YLeaf(YType.enumeration, "is-type")

                self.log_adjacency_changes = YLeaf(YType.empty, "log-adjacency-changes")

                self.log_pdu_drops = YLeaf(YType.empty, "log-pdu-drops")

                self.nsr = YLeaf(YType.empty, "nsr")

                self.running = YLeaf(YType.empty, "running")

                self.tracing_mode = YLeaf(YType.enumeration, "tracing-mode")

                self.adjacency_stagger = None
                self._children_name_map["adjacency_stagger"] = "adjacency-stagger"
                self._children_yang_names.add("adjacency-stagger")

                self.afs = Isis.Instances.Instance.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._children_yang_names.add("afs")

                self.distribute = None
                self._children_name_map["distribute"] = "distribute"
                self._children_yang_names.add("distribute")

                self.interfaces = Isis.Instances.Instance.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

                self.link_groups = Isis.Instances.Instance.LinkGroups()
                self.link_groups.parent = self
                self._children_name_map["link_groups"] = "link-groups"
                self._children_yang_names.add("link-groups")

                self.lsp_accept_passwords = Isis.Instances.Instance.LspAcceptPasswords()
                self.lsp_accept_passwords.parent = self
                self._children_name_map["lsp_accept_passwords"] = "lsp-accept-passwords"
                self._children_yang_names.add("lsp-accept-passwords")

                self.lsp_arrival_times = Isis.Instances.Instance.LspArrivalTimes()
                self.lsp_arrival_times.parent = self
                self._children_name_map["lsp_arrival_times"] = "lsp-arrival-times"
                self._children_yang_names.add("lsp-arrival-times")

                self.lsp_check_intervals = Isis.Instances.Instance.LspCheckIntervals()
                self.lsp_check_intervals.parent = self
                self._children_name_map["lsp_check_intervals"] = "lsp-check-intervals"
                self._children_yang_names.add("lsp-check-intervals")

                self.lsp_generation_intervals = Isis.Instances.Instance.LspGenerationIntervals()
                self.lsp_generation_intervals.parent = self
                self._children_name_map["lsp_generation_intervals"] = "lsp-generation-intervals"
                self._children_yang_names.add("lsp-generation-intervals")

                self.lsp_lifetimes = Isis.Instances.Instance.LspLifetimes()
                self.lsp_lifetimes.parent = self
                self._children_name_map["lsp_lifetimes"] = "lsp-lifetimes"
                self._children_yang_names.add("lsp-lifetimes")

                self.lsp_mtus = Isis.Instances.Instance.LspMtus()
                self.lsp_mtus.parent = self
                self._children_name_map["lsp_mtus"] = "lsp-mtus"
                self._children_yang_names.add("lsp-mtus")

                self.lsp_passwords = Isis.Instances.Instance.LspPasswords()
                self.lsp_passwords.parent = self
                self._children_name_map["lsp_passwords"] = "lsp-passwords"
                self._children_yang_names.add("lsp-passwords")

                self.lsp_refresh_intervals = Isis.Instances.Instance.LspRefreshIntervals()
                self.lsp_refresh_intervals.parent = self
                self._children_name_map["lsp_refresh_intervals"] = "lsp-refresh-intervals"
                self._children_yang_names.add("lsp-refresh-intervals")

                self.max_link_metrics = Isis.Instances.Instance.MaxLinkMetrics()
                self.max_link_metrics.parent = self
                self._children_name_map["max_link_metrics"] = "max-link-metrics"
                self._children_yang_names.add("max-link-metrics")

                self.nets = Isis.Instances.Instance.Nets()
                self.nets.parent = self
                self._children_name_map["nets"] = "nets"
                self._children_yang_names.add("nets")

                self.nsf = Isis.Instances.Instance.Nsf()
                self.nsf.parent = self
                self._children_name_map["nsf"] = "nsf"
                self._children_yang_names.add("nsf")

                self.overload_bits = Isis.Instances.Instance.OverloadBits()
                self.overload_bits.parent = self
                self._children_name_map["overload_bits"] = "overload-bits"
                self._children_yang_names.add("overload-bits")

                self.srgb = None
                self._children_name_map["srgb"] = "srgb"
                self._children_yang_names.add("srgb")

                self.trace_buffer_size = Isis.Instances.Instance.TraceBufferSize()
                self.trace_buffer_size.parent = self
                self._children_name_map["trace_buffer_size"] = "trace-buffer-size"
                self._children_yang_names.add("trace-buffer-size")
                self._segment_path = lambda: "instance" + "[instance-name='" + self.instance_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-clns-isis-cfg:isis/instances/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Isis.Instances.Instance, ['instance_name', 'dynamic_host_name', 'ignore_lsp_errors', 'instance_id', 'is_type', 'log_adjacency_changes', 'log_pdu_drops', 'nsr', 'running', 'tracing_mode'], name, value)


            class AdjacencyStagger(Entity):
                """
                Stagger ISIS adjacency bring up
                
                .. attribute:: initial_nbr
                
                	Adjacency Stagger\: Initial number of neighbors to bring up per area
                	**type**\:  int
                
                	**range:** 2..65000
                
                	**default value**\: 2
                
                .. attribute:: max_nbr
                
                	Adjacency Stagger\: Subsequent simultaneous number of neighbors to bring up
                	**type**\:  int
                
                	**range:** 2..65000
                
                	**default value**\: 64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.AdjacencyStagger, self).__init__()

                    self.yang_name = "adjacency-stagger"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.initial_nbr = YLeaf(YType.uint32, "initial-nbr")

                    self.max_nbr = YLeaf(YType.uint32, "max-nbr")
                    self._segment_path = lambda: "adjacency-stagger"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.AdjacencyStagger, ['initial_nbr', 'max_nbr'], name, value)


            class Afs(Entity):
                """
                Per\-address\-family configuration
                
                .. attribute:: af
                
                	Configuration for an IS\-IS address\-family. If a named (non\-default) topology is being created it must be multicast
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"af" : ("af", Isis.Instances.Instance.Afs.Af)}

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Afs, [], name, value)


                class Af(Entity):
                    """
                    Configuration for an IS\-IS address\-family. If
                    a named (non\-default) topology is being
                    created it must be multicast.
                    
                    .. attribute:: af_name  <key>
                    
                    	Address family
                    	**type**\:   :py:class:`IsisAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamily>`
                    
                    .. attribute:: saf_name  <key>
                    
                    	Sub address family
                    	**type**\:   :py:class:`IsisSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamily>`
                    
                    .. attribute:: af_data
                    
                    	Data container
                    	**type**\:   :py:class:`AfData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: topology_name
                    
                    	keys\: topology\-name
                    	**type**\: list of    :py:class:`TopologyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"af-data" : ("af_data", Isis.Instances.Instance.Afs.Af.AfData)}
                        self._child_list_classes = {"topology-name" : ("topology_name", Isis.Instances.Instance.Afs.Af.TopologyName)}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.saf_name = YLeaf(YType.enumeration, "saf-name")

                        self.af_data = None
                        self._children_name_map["af_data"] = "af-data"
                        self._children_yang_names.add("af-data")

                        self.topology_name = YList(self)
                        self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']" + "[saf-name='" + self.saf_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.Afs.Af, ['af_name', 'saf_name'], name, value)


                    class AfData(Entity):
                        """
                        Data container.
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\:   :py:class:`IsisAdjCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheck>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\:   :py:class:`AdminDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances>`
                        
                        .. attribute:: advertise_link_attributes
                        
                        	If TRUE, advertise additional link attributes in our LSP
                        	**type**\:  bool
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\:   :py:class:`IsisApplyWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeight>`
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\:   :py:class:`IsisAttachedBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit>`
                        
                        	**default value**\: area
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 115
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\:   :py:class:`FrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\:  bool
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\:   :py:class:`Ispf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf>`
                        
                        .. attribute:: manual_adj_sids
                        
                        	Manual Adjacecy SID configuration
                        	**type**\:   :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\:   :py:class:`MaxRedistPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\:  int
                        
                        	**range:** 1..64
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\:   :py:class:`MetricStyles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\:   :py:class:`MicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\:   :py:class:`MonitorConvergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`MplsLdpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\:   :py:class:`Propagations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\:   :py:class:`Redistributions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions>`
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\:  bool
                        
                        .. attribute:: router_id
                        
                        	Stable IP address for system. Will only be applied for the unicast sub\-address\-family
                        	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.RouterId>`
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\:   :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting>`
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\:   :py:class:`SpfIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\:   :py:class:`SpfPeriodicIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\:   :py:class:`SpfPrefixPriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\:   :py:class:`SummaryPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes>`
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\:  int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\:   :py:class:`Ucmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Afs.Af.AfData, self).__init__()

                            self.yang_name = "af-data"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"admin-distances" : ("admin_distances", Isis.Instances.Instance.Afs.Af.AfData.AdminDistances), "default-information" : ("default_information", Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation), "frr-table" : ("frr_table", Isis.Instances.Instance.Afs.Af.AfData.FrrTable), "ispf" : ("ispf", Isis.Instances.Instance.Afs.Af.AfData.Ispf), "manual-adj-sids" : ("manual_adj_sids", Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids), "max-redist-prefixes" : ("max_redist_prefixes", Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes), "metric-styles" : ("metric_styles", Isis.Instances.Instance.Afs.Af.AfData.MetricStyles), "metrics" : ("metrics", Isis.Instances.Instance.Afs.Af.AfData.Metrics), "micro-loop-avoidance" : ("micro_loop_avoidance", Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance), "monitor-convergence" : ("monitor_convergence", Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence), "mpls" : ("mpls", Isis.Instances.Instance.Afs.Af.AfData.Mpls), "mpls-ldp-global" : ("mpls_ldp_global", Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal), "propagations" : ("propagations", Isis.Instances.Instance.Afs.Af.AfData.Propagations), "redistributions" : ("redistributions", Isis.Instances.Instance.Afs.Af.AfData.Redistributions), "router-id" : ("router_id", Isis.Instances.Instance.Afs.Af.AfData.RouterId), "segment-routing" : ("segment_routing", Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting), "spf-intervals" : ("spf_intervals", Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals), "spf-periodic-intervals" : ("spf_periodic_intervals", Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals), "spf-prefix-priorities" : ("spf_prefix_priorities", Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities), "summary-prefixes" : ("summary_prefixes", Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes), "ucmp" : ("ucmp", Isis.Instances.Instance.Afs.Af.AfData.Ucmp), "weights" : ("weights", Isis.Instances.Instance.Afs.Af.AfData.Weights)}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.adjacency_check = YLeaf(YType.enumeration, "adjacency-check")

                            self.advertise_link_attributes = YLeaf(YType.boolean, "advertise-link-attributes")

                            self.advertise_passive_only = YLeaf(YType.empty, "advertise-passive-only")

                            self.apply_weight = YLeaf(YType.enumeration, "apply-weight")

                            self.attached_bit = YLeaf(YType.enumeration, "attached-bit")

                            self.default_admin_distance = YLeaf(YType.uint32, "default-admin-distance")

                            self.ignore_attached_bit = YLeaf(YType.boolean, "ignore-attached-bit")

                            self.maximum_paths = YLeaf(YType.uint32, "maximum-paths")

                            self.route_source_first_hop = YLeaf(YType.boolean, "route-source-first-hop")

                            self.single_topology = YLeaf(YType.empty, "single-topology")

                            self.topology_id = YLeaf(YType.uint32, "topology-id")

                            self.admin_distances = Isis.Instances.Instance.Afs.Af.AfData.AdminDistances()
                            self.admin_distances.parent = self
                            self._children_name_map["admin_distances"] = "admin-distances"
                            self._children_yang_names.add("admin-distances")

                            self.default_information = Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation()
                            self.default_information.parent = self
                            self._children_name_map["default_information"] = "default-information"
                            self._children_yang_names.add("default-information")

                            self.frr_table = Isis.Instances.Instance.Afs.Af.AfData.FrrTable()
                            self.frr_table.parent = self
                            self._children_name_map["frr_table"] = "frr-table"
                            self._children_yang_names.add("frr-table")

                            self.ispf = Isis.Instances.Instance.Afs.Af.AfData.Ispf()
                            self.ispf.parent = self
                            self._children_name_map["ispf"] = "ispf"
                            self._children_yang_names.add("ispf")

                            self.manual_adj_sids = Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids()
                            self.manual_adj_sids.parent = self
                            self._children_name_map["manual_adj_sids"] = "manual-adj-sids"
                            self._children_yang_names.add("manual-adj-sids")

                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self._children_name_map["max_redist_prefixes"] = "max-redist-prefixes"
                            self._children_yang_names.add("max-redist-prefixes")

                            self.metric_styles = Isis.Instances.Instance.Afs.Af.AfData.MetricStyles()
                            self.metric_styles.parent = self
                            self._children_name_map["metric_styles"] = "metric-styles"
                            self._children_yang_names.add("metric-styles")

                            self.metrics = Isis.Instances.Instance.Afs.Af.AfData.Metrics()
                            self.metrics.parent = self
                            self._children_name_map["metrics"] = "metrics"
                            self._children_yang_names.add("metrics")

                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self._children_name_map["micro_loop_avoidance"] = "micro-loop-avoidance"
                            self._children_yang_names.add("micro-loop-avoidance")

                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self._children_name_map["monitor_convergence"] = "monitor-convergence"
                            self._children_yang_names.add("monitor-convergence")

                            self.mpls = Isis.Instances.Instance.Afs.Af.AfData.Mpls()
                            self.mpls.parent = self
                            self._children_name_map["mpls"] = "mpls"
                            self._children_yang_names.add("mpls")

                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self._children_name_map["mpls_ldp_global"] = "mpls-ldp-global"
                            self._children_yang_names.add("mpls-ldp-global")

                            self.propagations = Isis.Instances.Instance.Afs.Af.AfData.Propagations()
                            self.propagations.parent = self
                            self._children_name_map["propagations"] = "propagations"
                            self._children_yang_names.add("propagations")

                            self.redistributions = Isis.Instances.Instance.Afs.Af.AfData.Redistributions()
                            self.redistributions.parent = self
                            self._children_name_map["redistributions"] = "redistributions"
                            self._children_yang_names.add("redistributions")

                            self.router_id = Isis.Instances.Instance.Afs.Af.AfData.RouterId()
                            self.router_id.parent = self
                            self._children_name_map["router_id"] = "router-id"
                            self._children_yang_names.add("router-id")

                            self.segment_routing = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting()
                            self.segment_routing.parent = self
                            self._children_name_map["segment_routing"] = "segment-routing"
                            self._children_yang_names.add("segment-routing")

                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals()
                            self.spf_intervals.parent = self
                            self._children_name_map["spf_intervals"] = "spf-intervals"
                            self._children_yang_names.add("spf-intervals")

                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self._children_name_map["spf_periodic_intervals"] = "spf-periodic-intervals"
                            self._children_yang_names.add("spf-periodic-intervals")

                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self._children_name_map["spf_prefix_priorities"] = "spf-prefix-priorities"
                            self._children_yang_names.add("spf-prefix-priorities")

                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self._children_name_map["summary_prefixes"] = "summary-prefixes"
                            self._children_yang_names.add("summary-prefixes")

                            self.ucmp = Isis.Instances.Instance.Afs.Af.AfData.Ucmp()
                            self.ucmp.parent = self
                            self._children_name_map["ucmp"] = "ucmp"
                            self._children_yang_names.add("ucmp")

                            self.weights = Isis.Instances.Instance.Afs.Af.AfData.Weights()
                            self.weights.parent = self
                            self._children_name_map["weights"] = "weights"
                            self._children_yang_names.add("weights")
                            self._segment_path = lambda: "af-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData, ['adjacency_check', 'advertise_link_attributes', 'advertise_passive_only', 'apply_weight', 'attached_bit', 'default_admin_distance', 'ignore_attached_bit', 'maximum_paths', 'route_source_first_hop', 'single_topology', 'topology_id'], name, value)


                        class AdminDistances(Entity):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of    :py:class:`AdminDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances, self).__init__()

                                self.yang_name = "admin-distances"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"admin-distance" : ("admin_distance", Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance)}

                                self.admin_distance = YList(self)
                                self._segment_path = lambda: "admin-distances"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances, [], name, value)


                            class AdminDistance(Entity):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP route source prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**mandatory**\: True
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance, self).__init__()

                                    self.yang_name = "admin-distance"
                                    self.yang_parent_name = "admin-distances"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address_prefix = YLeaf(YType.str, "address-prefix")

                                    self.distance = YLeaf(YType.uint32, "distance")

                                    self.prefix_list = YLeaf(YType.str, "prefix-list")
                                    self._segment_path = lambda: "admin-distance" + "[address-prefix='" + self.address_prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.AdminDistances.AdminDistance, ['address_prefix', 'distance', 'prefix_list'], name, value)


                        class DefaultInformation(Entity):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation, self).__init__()

                                self.yang_name = "default-information"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.external = YLeaf(YType.empty, "external")

                                self.policy_name = YLeaf(YType.str, "policy-name")

                                self.use_policy = YLeaf(YType.boolean, "use-policy")
                                self._segment_path = lambda: "default-information"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.DefaultInformation, ['external', 'policy_name', 'use_policy'], name, value)


                        class FrrTable(Entity):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\:   :py:class:`FrrLoadSharings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\:   :py:class:`FrrRemoteLfaPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\:   :py:class:`FrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\:   :py:class:`FrrUseCandOnlies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\:   :py:class:`PriorityLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable, self).__init__()

                                self.yang_name = "frr-table"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"frr-load-sharings" : ("frr_load_sharings", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings), "frr-remote-lfa-prefixes" : ("frr_remote_lfa_prefixes", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes), "frr-tiebreakers" : ("frr_tiebreakers", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers), "frr-use-cand-onlies" : ("frr_use_cand_onlies", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies), "priority-limits" : ("priority_limits", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits)}
                                self._child_list_classes = {}

                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self._children_name_map["frr_load_sharings"] = "frr-load-sharings"
                                self._children_yang_names.add("frr-load-sharings")

                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self._children_name_map["frr_remote_lfa_prefixes"] = "frr-remote-lfa-prefixes"
                                self._children_yang_names.add("frr-remote-lfa-prefixes")

                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self._children_name_map["frr_tiebreakers"] = "frr-tiebreakers"
                                self._children_yang_names.add("frr-tiebreakers")

                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self._children_name_map["frr_use_cand_onlies"] = "frr-use-cand-onlies"
                                self._children_yang_names.add("frr-use-cand-onlies")

                                self.priority_limits = Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self
                                self._children_name_map["priority_limits"] = "priority-limits"
                                self._children_yang_names.add("priority-limits")
                                self._segment_path = lambda: "frr-table"


                            class FrrLoadSharings(Entity):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of    :py:class:`FrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings, self).__init__()

                                    self.yang_name = "frr-load-sharings"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-load-sharing" : ("frr_load_sharing", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing)}

                                    self.frr_load_sharing = YList(self)
                                    self._segment_path = lambda: "frr-load-sharings"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings, [], name, value)


                                class FrrLoadSharing(Entity):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\:   :py:class:`IsisfrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharing>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing, self).__init__()

                                        self.yang_name = "frr-load-sharing"
                                        self.yang_parent_name = "frr-load-sharings"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.load_sharing = YLeaf(YType.enumeration, "load-sharing")
                                        self._segment_path = lambda: "frr-load-sharing" + "[level='" + self.level.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrLoadSharings.FrrLoadSharing, ['level', 'load_sharing'], name, value)


                            class FrrRemoteLfaPrefixes(Entity):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of    :py:class:`FrrRemoteLfaPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes, self).__init__()

                                    self.yang_name = "frr-remote-lfa-prefixes"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-remote-lfa-prefix" : ("frr_remote_lfa_prefix", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix)}

                                    self.frr_remote_lfa_prefix = YList(self)
                                    self._segment_path = lambda: "frr-remote-lfa-prefixes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes, [], name, value)


                                class FrrRemoteLfaPrefix(Entity):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, self).__init__()

                                        self.yang_name = "frr-remote-lfa-prefix"
                                        self.yang_parent_name = "frr-remote-lfa-prefixes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")
                                        self._segment_path = lambda: "frr-remote-lfa-prefix" + "[level='" + self.level.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, ['level', 'prefix_list_name'], name, value)


                            class FrrTiebreakers(Entity):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of    :py:class:`FrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers, self).__init__()

                                    self.yang_name = "frr-tiebreakers"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-tiebreaker" : ("frr_tiebreaker", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker)}

                                    self.frr_tiebreaker = YList(self)
                                    self._segment_path = lambda: "frr-tiebreakers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers, [], name, value)


                                class FrrTiebreaker(Entity):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: tiebreaker  <key>
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\:   :py:class:`IsisfrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreaker>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker, self).__init__()

                                        self.yang_name = "frr-tiebreaker"
                                        self.yang_parent_name = "frr-tiebreakers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.tiebreaker = YLeaf(YType.enumeration, "tiebreaker")

                                        self.index = YLeaf(YType.uint32, "index")
                                        self._segment_path = lambda: "frr-tiebreaker" + "[level='" + self.level.get() + "']" + "[tiebreaker='" + self.tiebreaker.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrTiebreakers.FrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                            class FrrUseCandOnlies(Entity):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of    :py:class:`FrrUseCandOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies, self).__init__()

                                    self.yang_name = "frr-use-cand-onlies"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-use-cand-only" : ("frr_use_cand_only", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly)}

                                    self.frr_use_cand_only = YList(self)
                                    self._segment_path = lambda: "frr-use-cand-onlies"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies, [], name, value)


                                class FrrUseCandOnly(Entity):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, self).__init__()

                                        self.yang_name = "frr-use-cand-only"
                                        self.yang_parent_name = "frr-use-cand-onlies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.frr_type = YLeaf(YType.enumeration, "frr-type")
                                        self._segment_path = lambda: "frr-use-cand-only" + "[level='" + self.level.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, ['level', 'frr_type'], name, value)


                            class PriorityLimits(Entity):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of    :py:class:`PriorityLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits, self).__init__()

                                    self.yang_name = "priority-limits"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"priority-limit" : ("priority_limit", Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit)}

                                    self.priority_limit = YList(self)
                                    self._segment_path = lambda: "priority-limits"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits, [], name, value)


                                class PriorityLimit(Entity):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                    
                                    .. attribute:: priority
                                    
                                    	Compute for all prefixes upto the specified priority
                                    	**type**\:   :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit, self).__init__()

                                        self.yang_name = "priority-limit"
                                        self.yang_parent_name = "priority-limits"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.frr_type = YLeaf(YType.enumeration, "frr-type")

                                        self.priority = YLeaf(YType.enumeration, "priority")
                                        self._segment_path = lambda: "priority-limit" + "[level='" + self.level.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.FrrTable.PriorityLimits.PriorityLimit, ['level', 'frr_type', 'priority'], name, value)


                        class Ispf(Entity):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\:   :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Ispf, self).__init__()

                                self.yang_name = "ispf"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"states" : ("states", Isis.Instances.Instance.Afs.Af.AfData.Ispf.States)}
                                self._child_list_classes = {}

                                self.states = Isis.Instances.Instance.Afs.Af.AfData.Ispf.States()
                                self.states.parent = self
                                self._children_name_map["states"] = "states"
                                self._children_yang_names.add("states")
                                self._segment_path = lambda: "ispf"


                            class States(Entity):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of    :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States, self).__init__()

                                    self.yang_name = "states"
                                    self.yang_parent_name = "ispf"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"state" : ("state", Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State)}

                                    self.state = YList(self)
                                    self._segment_path = lambda: "states"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States, [], name, value)


                                class State(Entity):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:   :py:class:`IsisispfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisispfState>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "states"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.state = YLeaf(YType.enumeration, "state")
                                        self._segment_path = lambda: "state" + "[level='" + self.level.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ispf.States.State, ['level', 'state'], name, value)


                        class ManualAdjSids(Entity):
                            """
                            Manual Adjacecy SID configuration
                            
                            .. attribute:: manual_adj_sid
                            
                            	Assign adjancency SID to an interface
                            	**type**\: list of    :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids, self).__init__()

                                self.yang_name = "manual-adj-sids"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"manual-adj-sid" : ("manual_adj_sid", Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid)}

                                self.manual_adj_sid = YList(self)
                                self._segment_path = lambda: "manual-adj-sids"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids, [], name, value)


                            class ManualAdjSid(Entity):
                                """
                                Assign adjancency SID to an interface
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: sid_type  <key>
                                
                                	Sid type aboslute or index
                                	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                
                                .. attribute:: sid  <key>
                                
                                	Sid value
                                	**type**\:  int
                                
                                	**range:** 0..1048575
                                
                                .. attribute:: protected
                                
                                	Enable/Disable SID protection
                                	**type**\:   :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid, self).__init__()

                                    self.yang_name = "manual-adj-sid"
                                    self.yang_parent_name = "manual-adj-sids"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.sid_type = YLeaf(YType.enumeration, "sid-type")

                                    self.sid = YLeaf(YType.uint32, "sid")

                                    self.protected = YLeaf(YType.enumeration, "protected")
                                    self._segment_path = lambda: "manual-adj-sid" + "[level='" + self.level.get() + "']" + "[sid-type='" + self.sid_type.get() + "']" + "[sid='" + self.sid.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                        class MaxRedistPrefixes(Entity):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of    :py:class:`MaxRedistPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes, self).__init__()

                                self.yang_name = "max-redist-prefixes"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"max-redist-prefix" : ("max_redist_prefix", Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix)}

                                self.max_redist_prefix = YList(self)
                                self._segment_path = lambda: "max-redist-prefixes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes, [], name, value)


                            class MaxRedistPrefix(Entity):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\:  int
                                
                                	**range:** 1..28000
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix, self).__init__()

                                    self.yang_name = "max-redist-prefix"
                                    self.yang_parent_name = "max-redist-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.prefix_limit = YLeaf(YType.uint32, "prefix-limit")
                                    self._segment_path = lambda: "max-redist-prefix" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MaxRedistPrefixes.MaxRedistPrefix, ['level', 'prefix_limit'], name, value)


                        class MetricStyles(Entity):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of    :py:class:`MetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles, self).__init__()

                                self.yang_name = "metric-styles"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"metric-style" : ("metric_style", Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle)}

                                self.metric_style = YList(self)
                                self._segment_path = lambda: "metric-styles"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles, [], name, value)


                            class MetricStyle(Entity):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\:   :py:class:`IsisMetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyle>`
                                
                                	**default value**\: old-metric-style
                                
                                .. attribute:: transition_state
                                
                                	Transition state
                                	**type**\:   :py:class:`IsisMetricStyleTransition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleTransition>`
                                
                                	**default value**\: disabled
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle, self).__init__()

                                    self.yang_name = "metric-style"
                                    self.yang_parent_name = "metric-styles"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.style = YLeaf(YType.enumeration, "style")

                                    self.transition_state = YLeaf(YType.enumeration, "transition-state")
                                    self._segment_path = lambda: "metric-style" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MetricStyles.MetricStyle, ['level', 'style', 'transition_state'], name, value)


                        class Metrics(Entity):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Metrics, self).__init__()

                                self.yang_name = "metrics"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"metric" : ("metric", Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric)}

                                self.metric = YList(self)
                                self._segment_path = lambda: "metrics"

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
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: one of the below types:
                                
                                	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric>`
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric, self).__init__()

                                    self.yang_name = "metric"
                                    self.yang_parent_name = "metrics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.metric = YLeaf(YType.str, "metric")
                                    self._segment_path = lambda: "metric" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Metrics.Metric, ['level', 'metric'], name, value)

                                class Metric(Enum):
                                    """
                                    Metric

                                    Allowed metric\: <1\-63> for narrow,

                                    <1\-16777215> for wide

                                    .. data:: maximum = 16777215

                                    	Maximum wide metric.  All routers will

                                    	exclude this link from their SPF

                                    """

                                    maximum = Enum.YLeaf(16777215, "maximum")



                        class MicroLoopAvoidance(Entity):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\:   :py:class:`IsisMicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidance>`
                            
                            	**default value**\: micro-loop-avoidance-all
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\:  int
                            
                            	**range:** 1000..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 5000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance, self).__init__()

                                self.yang_name = "micro-loop-avoidance"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.enumeration, "enable")

                                self.rib_update_delay = YLeaf(YType.uint32, "rib-update-delay")
                                self._segment_path = lambda: "micro-loop-avoidance"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MicroLoopAvoidance, ['enable', 'rib_update_delay'], name, value)


                        class MonitorConvergence(Entity):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence, self).__init__()

                                self.yang_name = "monitor-convergence"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.prefix_list = YLeaf(YType.str, "prefix-list")

                                self.track_ip_frr = YLeaf(YType.empty, "track-ip-frr")
                                self._segment_path = lambda: "monitor-convergence"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MonitorConvergence, ['enable', 'prefix_list', 'track_ip_frr'], name, value)


                        class Mpls(Entity):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\:   :py:class:`Level <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Mpls, self).__init__()

                                self.yang_name = "mpls"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"level" : ("level", Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level), "router-id" : ("router_id", Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId)}
                                self._child_list_classes = {}

                                self.igp_intact = YLeaf(YType.empty, "igp-intact")

                                self.multicast_intact = YLeaf(YType.empty, "multicast-intact")

                                self.level = Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level()
                                self.level.parent = self
                                self._children_name_map["level"] = "level"
                                self._children_yang_names.add("level")

                                self.router_id = Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId()
                                self.router_id.parent = self
                                self._children_name_map["router_id"] = "router-id"
                                self._children_yang_names.add("router-id")
                                self._segment_path = lambda: "mpls"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Mpls, ['igp_intact', 'multicast_intact'], name, value)


                            class Level(Entity):
                                """
                                Enable MPLS for an IS\-IS at the given
                                levels
                                
                                .. attribute:: level1
                                
                                	Level 1 enabled
                                	**type**\:  bool
                                
                                .. attribute:: level2
                                
                                	Level 2 enabled
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level, self).__init__()

                                    self.yang_name = "level"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level1 = YLeaf(YType.boolean, "level1")

                                    self.level2 = YLeaf(YType.boolean, "level2")
                                    self._segment_path = lambda: "level"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Mpls.Level, ['level1', 'level2'], name, value)


                            class RouterId(Entity):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId, self).__init__()

                                    self.yang_name = "router-id"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")
                                    self._segment_path = lambda: "router-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Mpls.RouterId, ['address', 'interface_name'], name, value)


                        class MplsLdpGlobal(Entity):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal, self).__init__()

                                self.yang_name = "mpls-ldp-global"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.auto_config = YLeaf(YType.boolean, "auto-config")
                                self._segment_path = lambda: "mpls-ldp-global"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.MplsLdpGlobal, ['auto_config'], name, value)


                        class Propagations(Entity):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of    :py:class:`Propagation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Propagations, self).__init__()

                                self.yang_name = "propagations"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"propagation" : ("propagation", Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation)}

                                self.propagation = YList(self)
                                self._segment_path = lambda: "propagations"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Propagations, [], name, value)


                            class Propagation(Entity):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: source_level  <key>
                                
                                	Source level for routes
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: destination_level  <key>
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation, self).__init__()

                                    self.yang_name = "propagation"
                                    self.yang_parent_name = "propagations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.source_level = YLeaf(YType.enumeration, "source-level")

                                    self.destination_level = YLeaf(YType.enumeration, "destination-level")

                                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                    self._segment_path = lambda: "propagation" + "[source-level='" + self.source_level.get() + "']" + "[destination-level='" + self.destination_level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Propagations.Propagation, ['source_level', 'destination_level', 'route_policy_name'], name, value)


                        class Redistributions(Entity):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of    :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions, self).__init__()

                                self.yang_name = "redistributions"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"redistribution" : ("redistribution", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution)}

                                self.redistribution = YList(self)
                                self._segment_path = lambda: "redistributions"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions, [], name, value)


                            class Redistribution(Entity):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name  <key>
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\:   :py:class:`IsisRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProto>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\:   :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp>`
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of    :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution, self).__init__()

                                    self.yang_name = "redistribution"
                                    self.yang_parent_name = "redistributions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"connected-or-static-or-rip-or-subscriber-or-mobile" : ("connected_or_static_or_rip_or_subscriber_or_mobile", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile)}
                                    self._child_list_classes = {"bgp" : ("bgp", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp), "eigrp" : ("eigrp", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp), "ospf-or-ospfv3-or-isis-or-application" : ("ospf_or_ospfv3_or_isis_or_application", Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication)}

                                    self.protocol_name = YLeaf(YType.enumeration, "protocol-name")

                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self._children_name_map["connected_or_static_or_rip_or_subscriber_or_mobile"] = "connected-or-static-or-rip-or-subscriber-or-mobile"
                                    self._children_yang_names.add("connected-or-static-or-rip-or-subscriber-or-mobile")

                                    self.bgp = YList(self)
                                    self.eigrp = YList(self)
                                    self.ospf_or_ospfv3_or_isis_or_application = YList(self)
                                    self._segment_path = lambda: "redistribution" + "[protocol-name='" + self.protocol_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution, ['protocol_name'], name, value)


                                class Bgp(Entity):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  <key>
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                                        self.as_yy = YLeaf(YType.uint32, "as-yy")

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "bgp" + "[as-xx='" + self.as_xx.get() + "']" + "[as-yy='" + self.as_yy.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Bgp, ['as_xx', 'as_yy', 'levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(Entity):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, self).__init__()

                                        self.yang_name = "connected-or-static-or-rip-or-subscriber-or-mobile"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "connected-or-static-or-rip-or-subscriber-or-mobile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, ['levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                                class Eigrp(Entity):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz  <key>
                                    
                                    	Eigrp as number
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp, self).__init__()

                                        self.yang_name = "eigrp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.as_zz = YLeaf(YType.uint32, "as-zz")

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "eigrp" + "[as-zz='" + self.as_zz.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.Eigrp, ['as_zz', 'levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                                class OspfOrOspfv3OrIsisOrApplication(Entity):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name  <key>
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, self).__init__()

                                        self.yang_name = "ospf-or-ospfv3-or-isis-or-application"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.instance_name = YLeaf(YType.str, "instance-name")

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "ospf-or-ospfv3-or-isis-or-application" + "[instance-name='" + self.instance_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, ['instance_name', 'levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                        class RouterId(Entity):
                            """
                            Stable IP address for system. Will only be
                            applied for the unicast sub\-address\-family.
                            
                            .. attribute:: address
                            
                            	IPv4/IPv6 address to be used as a router ID. Precisely one of Address and Interface must be specified
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: interface_name
                            
                            	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.RouterId, self).__init__()

                                self.yang_name = "router-id"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.address = YLeaf(YType.str, "address")

                                self.interface_name = YLeaf(YType.str, "interface-name")
                                self._segment_path = lambda: "router-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.RouterId, ['address', 'interface_name'], name, value)


                        class SegmentRouting(Entity):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: bundle_member_adj_sid
                            
                            	Enable per bundle member adjacency SID
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\:   :py:class:`IsisLabelPreference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreference>`
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\:   :py:class:`PrefixSidMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting, self).__init__()

                                self.yang_name = "segment-routing"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"prefix-sid-map" : ("prefix_sid_map", Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap)}
                                self._child_list_classes = {}

                                self.bundle_member_adj_sid = YLeaf(YType.empty, "bundle-member-adj-sid")

                                self.mpls = YLeaf(YType.enumeration, "mpls")

                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self
                                self._children_name_map["prefix_sid_map"] = "prefix-sid-map"
                                self._children_yang_names.add("prefix-sid-map")
                                self._segment_path = lambda: "segment-routing"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting, ['bundle_member_adj_sid', 'mpls'], name, value)


                            class PrefixSidMap(Entity):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap, self).__init__()

                                    self.yang_name = "prefix-sid-map"
                                    self.yang_parent_name = "segment-routing"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.advertise_local = YLeaf(YType.empty, "advertise-local")

                                    self.receive = YLeaf(YType.boolean, "receive")
                                    self._segment_path = lambda: "prefix-sid-map"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SegmentRouting.PrefixSidMap, ['advertise_local', 'receive'], name, value)


                        class SpfIntervals(Entity):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of    :py:class:`SpfInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals, self).__init__()

                                self.yang_name = "spf-intervals"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"spf-interval" : ("spf_interval", Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval)}

                                self.spf_interval = YList(self)
                                self._segment_path = lambda: "spf-intervals"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals, [], name, value)


                            class SpfInterval(Entity):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval, self).__init__()

                                    self.yang_name = "spf-interval"
                                    self.yang_parent_name = "spf-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.initial_wait = YLeaf(YType.uint32, "initial-wait")

                                    self.maximum_wait = YLeaf(YType.uint32, "maximum-wait")

                                    self.secondary_wait = YLeaf(YType.uint32, "secondary-wait")
                                    self._segment_path = lambda: "spf-interval" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfIntervals.SpfInterval, ['level', 'initial_wait', 'maximum_wait', 'secondary_wait'], name, value)


                        class SpfPeriodicIntervals(Entity):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of    :py:class:`SpfPeriodicInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals, self).__init__()

                                self.yang_name = "spf-periodic-intervals"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"spf-periodic-interval" : ("spf_periodic_interval", Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval)}

                                self.spf_periodic_interval = YList(self)
                                self._segment_path = lambda: "spf-periodic-intervals"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals, [], name, value)


                            class SpfPeriodicInterval(Entity):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**mandatory**\: True
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval, self).__init__()

                                    self.yang_name = "spf-periodic-interval"
                                    self.yang_parent_name = "spf-periodic-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.periodic_interval = YLeaf(YType.uint32, "periodic-interval")
                                    self._segment_path = lambda: "spf-periodic-interval" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPeriodicIntervals.SpfPeriodicInterval, ['level', 'periodic_interval'], name, value)


                        class SpfPrefixPriorities(Entity):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of    :py:class:`SpfPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities, self).__init__()

                                self.yang_name = "spf-prefix-priorities"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"spf-prefix-priority" : ("spf_prefix_priority", Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority)}

                                self.spf_prefix_priority = YList(self)
                                self._segment_path = lambda: "spf-prefix-priorities"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities, [], name, value)


                            class SpfPrefixPriority(Entity):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level  <key>
                                
                                	SPF Level for prefix prioritization
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_priority_type  <key>
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\:   :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority, self).__init__()

                                    self.yang_name = "spf-prefix-priority"
                                    self.yang_parent_name = "spf-prefix-priorities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.prefix_priority_type = YLeaf(YType.enumeration, "prefix-priority-type")

                                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                                    self.admin_tag = YLeaf(YType.uint32, "admin-tag")
                                    self._segment_path = lambda: "spf-prefix-priority" + "[level='" + self.level.get() + "']" + "[prefix-priority-type='" + self.prefix_priority_type.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SpfPrefixPriorities.SpfPrefixPriority, ['level', 'prefix_priority_type', 'access_list_name', 'admin_tag'], name, value)


                        class SummaryPrefixes(Entity):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of    :py:class:`SummaryPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes, self).__init__()

                                self.yang_name = "summary-prefixes"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"summary-prefix" : ("summary_prefix", Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix)}

                                self.summary_prefix = YList(self)
                                self._segment_path = lambda: "summary-prefixes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes, [], name, value)


                            class SummaryPrefix(Entity):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP summary address prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\:  int
                                
                                	**range:** 1..2
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix, self).__init__()

                                    self.yang_name = "summary-prefix"
                                    self.yang_parent_name = "summary-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address_prefix = YLeaf(YType.str, "address-prefix")

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.tag = YLeaf(YType.uint32, "tag")
                                    self._segment_path = lambda: "summary-prefix" + "[address-prefix='" + self.address_prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.SummaryPrefixes.SummaryPrefix, ['address_prefix', 'level', 'tag'], name, value)


                        class Ucmp(Entity):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\:  int
                            
                            	**range:** 100..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 100
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\:   :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\:   :py:class:`ExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp, self).__init__()

                                self.yang_name = "ucmp"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"enable" : ("enable", Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable), "exclude-interfaces" : ("exclude_interfaces", Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces)}
                                self._child_list_classes = {}

                                self.delay_interval = YLeaf(YType.uint32, "delay-interval")

                                self.enable = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable()
                                self.enable.parent = self
                                self._children_name_map["enable"] = "enable"
                                self._children_yang_names.add("enable")

                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self
                                self._children_name_map["exclude_interfaces"] = "exclude-interfaces"
                                self._children_yang_names.add("exclude-interfaces")
                                self._segment_path = lambda: "ucmp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp, ['delay_interval'], name, value)


                            class Enable(Entity):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\:  int
                                
                                	**range:** 101..10000
                                
                                	**default value**\: 200
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable, self).__init__()

                                    self.yang_name = "enable"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                                    self.variance = YLeaf(YType.uint32, "variance")
                                    self._segment_path = lambda: "enable"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.Enable, ['prefix_list_name', 'variance'], name, value)


                            class ExcludeInterfaces(Entity):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of    :py:class:`ExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces, self).__init__()

                                    self.yang_name = "exclude-interfaces"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"exclude-interface" : ("exclude_interface", Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface)}

                                    self.exclude_interface = YList(self)
                                    self._segment_path = lambda: "exclude-interfaces"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces, [], name, value)


                                class ExcludeInterface(Entity):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Name of the interface to be excluded
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface, self).__init__()

                                        self.yang_name = "exclude-interface"
                                        self.yang_parent_name = "exclude-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")
                                        self._segment_path = lambda: "exclude-interface" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Ucmp.ExcludeInterfaces.ExcludeInterface, ['interface_name'], name, value)


                        class Weights(Entity):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.AfData.Weights, self).__init__()

                                self.yang_name = "weights"
                                self.yang_parent_name = "af-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"weight" : ("weight", Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight)}

                                self.weight = YList(self)
                                self._segment_path = lambda: "weights"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Weights, [], name, value)


                            class Weight(Entity):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\:  int
                                
                                	**range:** 1..16777214
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight, self).__init__()

                                    self.yang_name = "weight"
                                    self.yang_parent_name = "weights"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.weight = YLeaf(YType.uint32, "weight")
                                    self._segment_path = lambda: "weight" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.AfData.Weights.Weight, ['level', 'weight'], name, value)


                    class TopologyName(Entity):
                        """
                        keys\: topology\-name
                        
                        .. attribute:: topology_name  <key>
                        
                        	Topology Name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: adjacency_check
                        
                        	Suppress check for consistent AF support on received IIHs
                        	**type**\:   :py:class:`IsisAdjCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdjCheck>`
                        
                        .. attribute:: admin_distances
                        
                        	Per\-route administrative distanceconfiguration
                        	**type**\:   :py:class:`AdminDistances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances>`
                        
                        .. attribute:: advertise_link_attributes
                        
                        	If TRUE, advertise additional link attributes in our LSP
                        	**type**\:  bool
                        
                        .. attribute:: advertise_passive_only
                        
                        	If enabled, advertise prefixes of passive interfaces only
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: apply_weight
                        
                        	Apply weights to UCMP or ECMP only
                        	**type**\:   :py:class:`IsisApplyWeight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisApplyWeight>`
                        
                        .. attribute:: attached_bit
                        
                        	Set the attached bit in this router's level 1 System LSP
                        	**type**\:   :py:class:`IsisAttachedBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAttachedBit>`
                        
                        	**default value**\: area
                        
                        .. attribute:: default_admin_distance
                        
                        	Default IS\-IS administrative distance configuration
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 115
                        
                        .. attribute:: default_information
                        
                        	Control origination of a default route with the option of using a policy.  If no policy is specified the default route is advertised with zero cost in level 2 only
                        	**type**\:   :py:class:`DefaultInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation>`
                        
                        .. attribute:: frr_table
                        
                        	Fast\-ReRoute configuration
                        	**type**\:   :py:class:`FrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable>`
                        
                        .. attribute:: ignore_attached_bit
                        
                        	If TRUE, Ignore other routers attached bit
                        	**type**\:  bool
                        
                        .. attribute:: ispf
                        
                        	ISPF configuration
                        	**type**\:   :py:class:`Ispf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf>`
                        
                        .. attribute:: manual_adj_sids
                        
                        	Manual Adjacecy SID configuration
                        	**type**\:   :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids>`
                        
                        .. attribute:: max_redist_prefixes
                        
                        	Maximum number of redistributed prefixesconfiguration
                        	**type**\:   :py:class:`MaxRedistPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes>`
                        
                        .. attribute:: maximum_paths
                        
                        	Maximum number of active parallel paths per route
                        	**type**\:  int
                        
                        	**range:** 1..64
                        
                        .. attribute:: metric_styles
                        
                        	Metric\-style configuration
                        	**type**\:   :py:class:`MetricStyles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles>`
                        
                        .. attribute:: metrics
                        
                        	Metric configuration
                        	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics>`
                        
                        .. attribute:: micro_loop_avoidance
                        
                        	Micro Loop Avoidance configuration
                        	**type**\:   :py:class:`MicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance>`
                        
                        .. attribute:: monitor_convergence
                        
                        	Enable convergence monitoring
                        	**type**\:   :py:class:`MonitorConvergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence>`
                        
                        .. attribute:: mpls
                        
                        	MPLS configuration. MPLS configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls>`
                        
                        .. attribute:: mpls_ldp_global
                        
                        	MPLS LDP configuration. MPLS LDP configuration will only be applied for the IPv4\-unicast address\-family
                        	**type**\:   :py:class:`MplsLdpGlobal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal>`
                        
                        .. attribute:: propagations
                        
                        	Route propagation configuration
                        	**type**\:   :py:class:`Propagations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations>`
                        
                        .. attribute:: redistributions
                        
                        	Protocol redistribution configuration
                        	**type**\:   :py:class:`Redistributions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions>`
                        
                        .. attribute:: route_source_first_hop
                        
                        	If TRUE, routes will be installed with the IP address of the first\-hop node as the source instead of the originating node
                        	**type**\:  bool
                        
                        .. attribute:: router_id
                        
                        	Stable IP address for system. Will only be applied for the unicast sub\-address\-family
                        	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.RouterId>`
                        
                        .. attribute:: segment_routing
                        
                        	Enable Segment Routing configuration
                        	**type**\:   :py:class:`SegmentRouting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting>`
                        
                        .. attribute:: single_topology
                        
                        	Run IPv6 Unicast using the standard (IPv4 Unicast) topology
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: spf_intervals
                        
                        	SPF\-interval configuration
                        	**type**\:   :py:class:`SpfIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals>`
                        
                        .. attribute:: spf_periodic_intervals
                        
                        	Peoridic SPF configuration
                        	**type**\:   :py:class:`SpfPeriodicIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals>`
                        
                        .. attribute:: spf_prefix_priorities
                        
                        	SPF Prefix Priority configuration
                        	**type**\:   :py:class:`SpfPrefixPriorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities>`
                        
                        .. attribute:: summary_prefixes
                        
                        	Summary\-prefix configuration
                        	**type**\:   :py:class:`SummaryPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes>`
                        
                        .. attribute:: topology_id
                        
                        	Set the topology ID for a named (non\-default) topology. This object must be set before any other configuration is supplied for a named (non\-default) topology , and must be the last configuration object to be removed. This item should not be supplied for the non\-named default topologies
                        	**type**\:  int
                        
                        	**range:** 6..4095
                        
                        .. attribute:: ucmp
                        
                        	UCMP (UnEqual Cost MultiPath) configuration
                        	**type**\:   :py:class:`Ucmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp>`
                        
                        .. attribute:: weights
                        
                        	Weight configuration
                        	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Afs.Af.TopologyName, self).__init__()

                            self.yang_name = "topology-name"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"admin-distances" : ("admin_distances", Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances), "default-information" : ("default_information", Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation), "frr-table" : ("frr_table", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable), "ispf" : ("ispf", Isis.Instances.Instance.Afs.Af.TopologyName.Ispf), "manual-adj-sids" : ("manual_adj_sids", Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids), "max-redist-prefixes" : ("max_redist_prefixes", Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes), "metric-styles" : ("metric_styles", Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles), "metrics" : ("metrics", Isis.Instances.Instance.Afs.Af.TopologyName.Metrics), "micro-loop-avoidance" : ("micro_loop_avoidance", Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance), "monitor-convergence" : ("monitor_convergence", Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence), "mpls" : ("mpls", Isis.Instances.Instance.Afs.Af.TopologyName.Mpls), "mpls-ldp-global" : ("mpls_ldp_global", Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal), "propagations" : ("propagations", Isis.Instances.Instance.Afs.Af.TopologyName.Propagations), "redistributions" : ("redistributions", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions), "router-id" : ("router_id", Isis.Instances.Instance.Afs.Af.TopologyName.RouterId), "segment-routing" : ("segment_routing", Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting), "spf-intervals" : ("spf_intervals", Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals), "spf-periodic-intervals" : ("spf_periodic_intervals", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals), "spf-prefix-priorities" : ("spf_prefix_priorities", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities), "summary-prefixes" : ("summary_prefixes", Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes), "ucmp" : ("ucmp", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp), "weights" : ("weights", Isis.Instances.Instance.Afs.Af.TopologyName.Weights)}
                            self._child_list_classes = {}

                            self.topology_name = YLeaf(YType.str, "topology-name")

                            self.adjacency_check = YLeaf(YType.enumeration, "adjacency-check")

                            self.advertise_link_attributes = YLeaf(YType.boolean, "advertise-link-attributes")

                            self.advertise_passive_only = YLeaf(YType.empty, "advertise-passive-only")

                            self.apply_weight = YLeaf(YType.enumeration, "apply-weight")

                            self.attached_bit = YLeaf(YType.enumeration, "attached-bit")

                            self.default_admin_distance = YLeaf(YType.uint32, "default-admin-distance")

                            self.ignore_attached_bit = YLeaf(YType.boolean, "ignore-attached-bit")

                            self.maximum_paths = YLeaf(YType.uint32, "maximum-paths")

                            self.route_source_first_hop = YLeaf(YType.boolean, "route-source-first-hop")

                            self.single_topology = YLeaf(YType.empty, "single-topology")

                            self.topology_id = YLeaf(YType.uint32, "topology-id")

                            self.admin_distances = Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances()
                            self.admin_distances.parent = self
                            self._children_name_map["admin_distances"] = "admin-distances"
                            self._children_yang_names.add("admin-distances")

                            self.default_information = Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation()
                            self.default_information.parent = self
                            self._children_name_map["default_information"] = "default-information"
                            self._children_yang_names.add("default-information")

                            self.frr_table = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable()
                            self.frr_table.parent = self
                            self._children_name_map["frr_table"] = "frr-table"
                            self._children_yang_names.add("frr-table")

                            self.ispf = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf()
                            self.ispf.parent = self
                            self._children_name_map["ispf"] = "ispf"
                            self._children_yang_names.add("ispf")

                            self.manual_adj_sids = Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids()
                            self.manual_adj_sids.parent = self
                            self._children_name_map["manual_adj_sids"] = "manual-adj-sids"
                            self._children_yang_names.add("manual-adj-sids")

                            self.max_redist_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes()
                            self.max_redist_prefixes.parent = self
                            self._children_name_map["max_redist_prefixes"] = "max-redist-prefixes"
                            self._children_yang_names.add("max-redist-prefixes")

                            self.metric_styles = Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles()
                            self.metric_styles.parent = self
                            self._children_name_map["metric_styles"] = "metric-styles"
                            self._children_yang_names.add("metric-styles")

                            self.metrics = Isis.Instances.Instance.Afs.Af.TopologyName.Metrics()
                            self.metrics.parent = self
                            self._children_name_map["metrics"] = "metrics"
                            self._children_yang_names.add("metrics")

                            self.micro_loop_avoidance = Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance()
                            self.micro_loop_avoidance.parent = self
                            self._children_name_map["micro_loop_avoidance"] = "micro-loop-avoidance"
                            self._children_yang_names.add("micro-loop-avoidance")

                            self.monitor_convergence = Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence()
                            self.monitor_convergence.parent = self
                            self._children_name_map["monitor_convergence"] = "monitor-convergence"
                            self._children_yang_names.add("monitor-convergence")

                            self.mpls = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls()
                            self.mpls.parent = self
                            self._children_name_map["mpls"] = "mpls"
                            self._children_yang_names.add("mpls")

                            self.mpls_ldp_global = Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal()
                            self.mpls_ldp_global.parent = self
                            self._children_name_map["mpls_ldp_global"] = "mpls-ldp-global"
                            self._children_yang_names.add("mpls-ldp-global")

                            self.propagations = Isis.Instances.Instance.Afs.Af.TopologyName.Propagations()
                            self.propagations.parent = self
                            self._children_name_map["propagations"] = "propagations"
                            self._children_yang_names.add("propagations")

                            self.redistributions = Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions()
                            self.redistributions.parent = self
                            self._children_name_map["redistributions"] = "redistributions"
                            self._children_yang_names.add("redistributions")

                            self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.RouterId()
                            self.router_id.parent = self
                            self._children_name_map["router_id"] = "router-id"
                            self._children_yang_names.add("router-id")

                            self.segment_routing = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting()
                            self.segment_routing.parent = self
                            self._children_name_map["segment_routing"] = "segment-routing"
                            self._children_yang_names.add("segment-routing")

                            self.spf_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals()
                            self.spf_intervals.parent = self
                            self._children_name_map["spf_intervals"] = "spf-intervals"
                            self._children_yang_names.add("spf-intervals")

                            self.spf_periodic_intervals = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals()
                            self.spf_periodic_intervals.parent = self
                            self._children_name_map["spf_periodic_intervals"] = "spf-periodic-intervals"
                            self._children_yang_names.add("spf-periodic-intervals")

                            self.spf_prefix_priorities = Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities()
                            self.spf_prefix_priorities.parent = self
                            self._children_name_map["spf_prefix_priorities"] = "spf-prefix-priorities"
                            self._children_yang_names.add("spf-prefix-priorities")

                            self.summary_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes()
                            self.summary_prefixes.parent = self
                            self._children_name_map["summary_prefixes"] = "summary-prefixes"
                            self._children_yang_names.add("summary-prefixes")

                            self.ucmp = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp()
                            self.ucmp.parent = self
                            self._children_name_map["ucmp"] = "ucmp"
                            self._children_yang_names.add("ucmp")

                            self.weights = Isis.Instances.Instance.Afs.Af.TopologyName.Weights()
                            self.weights.parent = self
                            self._children_name_map["weights"] = "weights"
                            self._children_yang_names.add("weights")
                            self._segment_path = lambda: "topology-name" + "[topology-name='" + self.topology_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName, ['topology_name', 'adjacency_check', 'advertise_link_attributes', 'advertise_passive_only', 'apply_weight', 'attached_bit', 'default_admin_distance', 'ignore_attached_bit', 'maximum_paths', 'route_source_first_hop', 'single_topology', 'topology_id'], name, value)


                        class AdminDistances(Entity):
                            """
                            Per\-route administrative
                            distanceconfiguration
                            
                            .. attribute:: admin_distance
                            
                            	Administrative distance configuration. The supplied distance is applied to all routes discovered from the specified source, or only those that match the supplied prefix list if this is specified
                            	**type**\: list of    :py:class:`AdminDistance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances, self).__init__()

                                self.yang_name = "admin-distances"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"admin-distance" : ("admin_distance", Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance)}

                                self.admin_distance = YList(self)
                                self._segment_path = lambda: "admin-distances"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances, [], name, value)


                            class AdminDistance(Entity):
                                """
                                Administrative distance configuration. The
                                supplied distance is applied to all routes
                                discovered from the specified source, or
                                only those that match the supplied prefix
                                list if this is specified
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP route source prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: distance
                                
                                	Administrative distance
                                	**type**\:  int
                                
                                	**range:** 1..255
                                
                                	**mandatory**\: True
                                
                                .. attribute:: prefix_list
                                
                                	List of prefixes to which this distance applies
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance, self).__init__()

                                    self.yang_name = "admin-distance"
                                    self.yang_parent_name = "admin-distances"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address_prefix = YLeaf(YType.str, "address-prefix")

                                    self.distance = YLeaf(YType.uint32, "distance")

                                    self.prefix_list = YLeaf(YType.str, "prefix-list")
                                    self._segment_path = lambda: "admin-distance" + "[address-prefix='" + self.address_prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.AdminDistances.AdminDistance, ['address_prefix', 'distance', 'prefix_list'], name, value)


                        class DefaultInformation(Entity):
                            """
                            Control origination of a default route with
                            the option of using a policy.  If no policy
                            is specified the default route is
                            advertised with zero cost in level 2 only.
                            
                            .. attribute:: external
                            
                            	Flag to indicate that the default prefix should be originated as an external route
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy_name
                            
                            	Policy name
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: use_policy
                            
                            	Flag to indicate whether default origination is controlled using a policy
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation, self).__init__()

                                self.yang_name = "default-information"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.external = YLeaf(YType.empty, "external")

                                self.policy_name = YLeaf(YType.str, "policy-name")

                                self.use_policy = YLeaf(YType.boolean, "use-policy")
                                self._segment_path = lambda: "default-information"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.DefaultInformation, ['external', 'policy_name', 'use_policy'], name, value)


                        class FrrTable(Entity):
                            """
                            Fast\-ReRoute configuration
                            
                            .. attribute:: frr_load_sharings
                            
                            	Load share prefixes across multiple backups
                            	**type**\:   :py:class:`FrrLoadSharings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings>`
                            
                            .. attribute:: frr_remote_lfa_prefixes
                            
                            	FRR remote LFA prefix list filter configuration
                            	**type**\:   :py:class:`FrrRemoteLfaPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes>`
                            
                            .. attribute:: frr_tiebreakers
                            
                            	FRR tiebreakers configuration
                            	**type**\:   :py:class:`FrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers>`
                            
                            .. attribute:: frr_use_cand_onlies
                            
                            	FRR use candidate only configuration
                            	**type**\:   :py:class:`FrrUseCandOnlies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies>`
                            
                            .. attribute:: priority_limits
                            
                            	FRR prefix\-limit configuration
                            	**type**\:   :py:class:`PriorityLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable, self).__init__()

                                self.yang_name = "frr-table"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"frr-load-sharings" : ("frr_load_sharings", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings), "frr-remote-lfa-prefixes" : ("frr_remote_lfa_prefixes", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes), "frr-tiebreakers" : ("frr_tiebreakers", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers), "frr-use-cand-onlies" : ("frr_use_cand_onlies", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies), "priority-limits" : ("priority_limits", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits)}
                                self._child_list_classes = {}

                                self.frr_load_sharings = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings()
                                self.frr_load_sharings.parent = self
                                self._children_name_map["frr_load_sharings"] = "frr-load-sharings"
                                self._children_yang_names.add("frr-load-sharings")

                                self.frr_remote_lfa_prefixes = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes()
                                self.frr_remote_lfa_prefixes.parent = self
                                self._children_name_map["frr_remote_lfa_prefixes"] = "frr-remote-lfa-prefixes"
                                self._children_yang_names.add("frr-remote-lfa-prefixes")

                                self.frr_tiebreakers = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers()
                                self.frr_tiebreakers.parent = self
                                self._children_name_map["frr_tiebreakers"] = "frr-tiebreakers"
                                self._children_yang_names.add("frr-tiebreakers")

                                self.frr_use_cand_onlies = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies()
                                self.frr_use_cand_onlies.parent = self
                                self._children_name_map["frr_use_cand_onlies"] = "frr-use-cand-onlies"
                                self._children_yang_names.add("frr-use-cand-onlies")

                                self.priority_limits = Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits()
                                self.priority_limits.parent = self
                                self._children_name_map["priority_limits"] = "priority-limits"
                                self._children_yang_names.add("priority-limits")
                                self._segment_path = lambda: "frr-table"


                            class FrrLoadSharings(Entity):
                                """
                                Load share prefixes across multiple
                                backups
                                
                                .. attribute:: frr_load_sharing
                                
                                	Disable load sharing
                                	**type**\: list of    :py:class:`FrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings, self).__init__()

                                    self.yang_name = "frr-load-sharings"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-load-sharing" : ("frr_load_sharing", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing)}

                                    self.frr_load_sharing = YList(self)
                                    self._segment_path = lambda: "frr-load-sharings"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings, [], name, value)


                                class FrrLoadSharing(Entity):
                                    """
                                    Disable load sharing
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: load_sharing
                                    
                                    	Load sharing
                                    	**type**\:   :py:class:`IsisfrrLoadSharing <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrLoadSharing>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing, self).__init__()

                                        self.yang_name = "frr-load-sharing"
                                        self.yang_parent_name = "frr-load-sharings"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.load_sharing = YLeaf(YType.enumeration, "load-sharing")
                                        self._segment_path = lambda: "frr-load-sharing" + "[level='" + self.level.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrLoadSharings.FrrLoadSharing, ['level', 'load_sharing'], name, value)


                            class FrrRemoteLfaPrefixes(Entity):
                                """
                                FRR remote LFA prefix list filter
                                configuration
                                
                                .. attribute:: frr_remote_lfa_prefix
                                
                                	Filter remote LFA router IDs using prefix\-list
                                	**type**\: list of    :py:class:`FrrRemoteLfaPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes, self).__init__()

                                    self.yang_name = "frr-remote-lfa-prefixes"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-remote-lfa-prefix" : ("frr_remote_lfa_prefix", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix)}

                                    self.frr_remote_lfa_prefix = YList(self)
                                    self._segment_path = lambda: "frr-remote-lfa-prefixes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes, [], name, value)


                                class FrrRemoteLfaPrefix(Entity):
                                    """
                                    Filter remote LFA router IDs using
                                    prefix\-list
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: prefix_list_name
                                    
                                    	Name of the prefix list
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, self).__init__()

                                        self.yang_name = "frr-remote-lfa-prefix"
                                        self.yang_parent_name = "frr-remote-lfa-prefixes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")
                                        self._segment_path = lambda: "frr-remote-lfa-prefix" + "[level='" + self.level.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrRemoteLfaPrefixes.FrrRemoteLfaPrefix, ['level', 'prefix_list_name'], name, value)


                            class FrrTiebreakers(Entity):
                                """
                                FRR tiebreakers configuration
                                
                                .. attribute:: frr_tiebreaker
                                
                                	Configure tiebreaker for multiple backups
                                	**type**\: list of    :py:class:`FrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers, self).__init__()

                                    self.yang_name = "frr-tiebreakers"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-tiebreaker" : ("frr_tiebreaker", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker)}

                                    self.frr_tiebreaker = YList(self)
                                    self._segment_path = lambda: "frr-tiebreakers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers, [], name, value)


                                class FrrTiebreaker(Entity):
                                    """
                                    Configure tiebreaker for multiple backups
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: tiebreaker  <key>
                                    
                                    	Tiebreaker for which configuration applies
                                    	**type**\:   :py:class:`IsisfrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisfrrTiebreaker>`
                                    
                                    .. attribute:: index
                                    
                                    	Preference order among tiebreakers
                                    	**type**\:  int
                                    
                                    	**range:** 1..255
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker, self).__init__()

                                        self.yang_name = "frr-tiebreaker"
                                        self.yang_parent_name = "frr-tiebreakers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.tiebreaker = YLeaf(YType.enumeration, "tiebreaker")

                                        self.index = YLeaf(YType.uint32, "index")
                                        self._segment_path = lambda: "frr-tiebreaker" + "[level='" + self.level.get() + "']" + "[tiebreaker='" + self.tiebreaker.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrTiebreakers.FrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                            class FrrUseCandOnlies(Entity):
                                """
                                FRR use candidate only configuration
                                
                                .. attribute:: frr_use_cand_only
                                
                                	Configure use candidate only to exclude interfaces as backup
                                	**type**\: list of    :py:class:`FrrUseCandOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies, self).__init__()

                                    self.yang_name = "frr-use-cand-onlies"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"frr-use-cand-only" : ("frr_use_cand_only", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly)}

                                    self.frr_use_cand_only = YList(self)
                                    self._segment_path = lambda: "frr-use-cand-onlies"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies, [], name, value)


                                class FrrUseCandOnly(Entity):
                                    """
                                    Configure use candidate only to exclude
                                    interfaces as backup
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, self).__init__()

                                        self.yang_name = "frr-use-cand-only"
                                        self.yang_parent_name = "frr-use-cand-onlies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.frr_type = YLeaf(YType.enumeration, "frr-type")
                                        self._segment_path = lambda: "frr-use-cand-only" + "[level='" + self.level.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.FrrUseCandOnlies.FrrUseCandOnly, ['level', 'frr_type'], name, value)


                            class PriorityLimits(Entity):
                                """
                                FRR prefix\-limit configuration
                                
                                .. attribute:: priority_limit
                                
                                	Limit backup computation upto the prefix priority
                                	**type**\: list of    :py:class:`PriorityLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits, self).__init__()

                                    self.yang_name = "priority-limits"
                                    self.yang_parent_name = "frr-table"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"priority-limit" : ("priority_limit", Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit)}

                                    self.priority_limit = YList(self)
                                    self._segment_path = lambda: "priority-limits"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits, [], name, value)


                                class PriorityLimit(Entity):
                                    """
                                    Limit backup computation upto the prefix
                                    priority
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: frr_type  <key>
                                    
                                    	Computation Type
                                    	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                    
                                    .. attribute:: priority
                                    
                                    	Compute for all prefixes upto the specified priority
                                    	**type**\:   :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit, self).__init__()

                                        self.yang_name = "priority-limit"
                                        self.yang_parent_name = "priority-limits"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.frr_type = YLeaf(YType.enumeration, "frr-type")

                                        self.priority = YLeaf(YType.enumeration, "priority")
                                        self._segment_path = lambda: "priority-limit" + "[level='" + self.level.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.FrrTable.PriorityLimits.PriorityLimit, ['level', 'frr_type', 'priority'], name, value)


                        class Ispf(Entity):
                            """
                            ISPF configuration
                            
                            .. attribute:: states
                            
                            	ISPF state (enable/disable)
                            	**type**\:   :py:class:`States <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf, self).__init__()

                                self.yang_name = "ispf"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"states" : ("states", Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States)}
                                self._child_list_classes = {}

                                self.states = Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States()
                                self.states.parent = self
                                self._children_name_map["states"] = "states"
                                self._children_yang_names.add("states")
                                self._segment_path = lambda: "ispf"


                            class States(Entity):
                                """
                                ISPF state (enable/disable)
                                
                                .. attribute:: state
                                
                                	Enable/disable ISPF
                                	**type**\: list of    :py:class:`State <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States, self).__init__()

                                    self.yang_name = "states"
                                    self.yang_parent_name = "ispf"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"state" : ("state", Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State)}

                                    self.state = YList(self)
                                    self._segment_path = lambda: "states"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States, [], name, value)


                                class State(Entity):
                                    """
                                    Enable/disable ISPF
                                    
                                    .. attribute:: level  <key>
                                    
                                    	Level to which configuration applies
                                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                    
                                    .. attribute:: state
                                    
                                    	State
                                    	**type**\:   :py:class:`IsisispfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisispfState>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State, self).__init__()

                                        self.yang_name = "state"
                                        self.yang_parent_name = "states"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.level = YLeaf(YType.enumeration, "level")

                                        self.state = YLeaf(YType.enumeration, "state")
                                        self._segment_path = lambda: "state" + "[level='" + self.level.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ispf.States.State, ['level', 'state'], name, value)


                        class ManualAdjSids(Entity):
                            """
                            Manual Adjacecy SID configuration
                            
                            .. attribute:: manual_adj_sid
                            
                            	Assign adjancency SID to an interface
                            	**type**\: list of    :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids, self).__init__()

                                self.yang_name = "manual-adj-sids"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"manual-adj-sid" : ("manual_adj_sid", Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid)}

                                self.manual_adj_sid = YList(self)
                                self._segment_path = lambda: "manual-adj-sids"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids, [], name, value)


                            class ManualAdjSid(Entity):
                                """
                                Assign adjancency SID to an interface
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: sid_type  <key>
                                
                                	Sid type aboslute or index
                                	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                
                                .. attribute:: sid  <key>
                                
                                	Sid value
                                	**type**\:  int
                                
                                	**range:** 0..1048575
                                
                                .. attribute:: protected
                                
                                	Enable/Disable SID protection
                                	**type**\:   :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid, self).__init__()

                                    self.yang_name = "manual-adj-sid"
                                    self.yang_parent_name = "manual-adj-sids"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.sid_type = YLeaf(YType.enumeration, "sid-type")

                                    self.sid = YLeaf(YType.uint32, "sid")

                                    self.protected = YLeaf(YType.enumeration, "protected")
                                    self._segment_path = lambda: "manual-adj-sid" + "[level='" + self.level.get() + "']" + "[sid-type='" + self.sid_type.get() + "']" + "[sid='" + self.sid.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                        class MaxRedistPrefixes(Entity):
                            """
                            Maximum number of redistributed
                            prefixesconfiguration
                            
                            .. attribute:: max_redist_prefix
                            
                            	An upper limit on the number of redistributed prefixes which may be included in the local system's LSP
                            	**type**\: list of    :py:class:`MaxRedistPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes, self).__init__()

                                self.yang_name = "max-redist-prefixes"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"max-redist-prefix" : ("max_redist_prefix", Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix)}

                                self.max_redist_prefix = YList(self)
                                self._segment_path = lambda: "max-redist-prefixes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes, [], name, value)


                            class MaxRedistPrefix(Entity):
                                """
                                An upper limit on the number of
                                redistributed prefixes which may be
                                included in the local system's LSP
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_limit
                                
                                	Max number of prefixes
                                	**type**\:  int
                                
                                	**range:** 1..28000
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix, self).__init__()

                                    self.yang_name = "max-redist-prefix"
                                    self.yang_parent_name = "max-redist-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.prefix_limit = YLeaf(YType.uint32, "prefix-limit")
                                    self._segment_path = lambda: "max-redist-prefix" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MaxRedistPrefixes.MaxRedistPrefix, ['level', 'prefix_limit'], name, value)


                        class MetricStyles(Entity):
                            """
                            Metric\-style configuration
                            
                            .. attribute:: metric_style
                            
                            	Configuration of metric style in LSPs
                            	**type**\: list of    :py:class:`MetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles, self).__init__()

                                self.yang_name = "metric-styles"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"metric-style" : ("metric_style", Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle)}

                                self.metric_style = YList(self)
                                self._segment_path = lambda: "metric-styles"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles, [], name, value)


                            class MetricStyle(Entity):
                                """
                                Configuration of metric style in LSPs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: style
                                
                                	Metric Style
                                	**type**\:   :py:class:`IsisMetricStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyle>`
                                
                                	**default value**\: old-metric-style
                                
                                .. attribute:: transition_state
                                
                                	Transition state
                                	**type**\:   :py:class:`IsisMetricStyleTransition <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetricStyleTransition>`
                                
                                	**default value**\: disabled
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle, self).__init__()

                                    self.yang_name = "metric-style"
                                    self.yang_parent_name = "metric-styles"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.style = YLeaf(YType.enumeration, "style")

                                    self.transition_state = YLeaf(YType.enumeration, "transition-state")
                                    self._segment_path = lambda: "metric-style" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MetricStyles.MetricStyle, ['level', 'style', 'transition_state'], name, value)


                        class Metrics(Entity):
                            """
                            Metric configuration
                            
                            .. attribute:: metric
                            
                            	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                            	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics, self).__init__()

                                self.yang_name = "metrics"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"metric" : ("metric", Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric)}

                                self.metric = YList(self)
                                self._segment_path = lambda: "metrics"

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
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: metric
                                
                                	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                	**type**\: one of the below types:
                                
                                	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric>`
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                	**type**\:  int
                                
                                	**range:** 1..16777215
                                
                                	**mandatory**\: True
                                
                                
                                ----
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric, self).__init__()

                                    self.yang_name = "metric"
                                    self.yang_parent_name = "metrics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.metric = YLeaf(YType.str, "metric")
                                    self._segment_path = lambda: "metric" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Metrics.Metric, ['level', 'metric'], name, value)

                                class Metric(Enum):
                                    """
                                    Metric

                                    Allowed metric\: <1\-63> for narrow,

                                    <1\-16777215> for wide

                                    .. data:: maximum = 16777215

                                    	Maximum wide metric.  All routers will

                                    	exclude this link from their SPF

                                    """

                                    maximum = Enum.YLeaf(16777215, "maximum")



                        class MicroLoopAvoidance(Entity):
                            """
                            Micro Loop Avoidance configuration
                            
                            .. attribute:: enable
                            
                            	MicroLoop avoidance enable configuration
                            	**type**\:   :py:class:`IsisMicroLoopAvoidance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMicroLoopAvoidance>`
                            
                            	**default value**\: micro-loop-avoidance-all
                            
                            .. attribute:: rib_update_delay
                            
                            	Value of delay in msecs in updating RIB
                            	**type**\:  int
                            
                            	**range:** 1000..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 5000
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance, self).__init__()

                                self.yang_name = "micro-loop-avoidance"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.enumeration, "enable")

                                self.rib_update_delay = YLeaf(YType.uint32, "rib-update-delay")
                                self._segment_path = lambda: "micro-loop-avoidance"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MicroLoopAvoidance, ['enable', 'rib_update_delay'], name, value)


                        class MonitorConvergence(Entity):
                            """
                            Enable convergence monitoring
                            
                            .. attribute:: enable
                            
                            	Enable convergence monitoring
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: prefix_list
                            
                            	Enable the monitoring of individual prefixes (prefix list name)
                            	**type**\:  str
                            
                            	**length:** 1..32
                            
                            .. attribute:: track_ip_frr
                            
                            	Enable the Tracking of IP\-Frr Convergence
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence, self).__init__()

                                self.yang_name = "monitor-convergence"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.prefix_list = YLeaf(YType.str, "prefix-list")

                                self.track_ip_frr = YLeaf(YType.empty, "track-ip-frr")
                                self._segment_path = lambda: "monitor-convergence"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MonitorConvergence, ['enable', 'prefix_list', 'track_ip_frr'], name, value)


                        class Mpls(Entity):
                            """
                            MPLS configuration. MPLS configuration will
                            only be applied for the IPv4\-unicast
                            address\-family.
                            
                            .. attribute:: igp_intact
                            
                            	Install TE and non\-TE nexthops in the RIB
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: level
                            
                            	Enable MPLS for an IS\-IS at the given levels
                            	**type**\:   :py:class:`Level <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level>`
                            
                            .. attribute:: multicast_intact
                            
                            	Install non\-TE nexthops in the RIB for use by multicast
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: router_id
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:   :py:class:`RouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls, self).__init__()

                                self.yang_name = "mpls"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"level" : ("level", Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level), "router-id" : ("router_id", Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId)}
                                self._child_list_classes = {}

                                self.igp_intact = YLeaf(YType.empty, "igp-intact")

                                self.multicast_intact = YLeaf(YType.empty, "multicast-intact")

                                self.level = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level()
                                self.level.parent = self
                                self._children_name_map["level"] = "level"
                                self._children_yang_names.add("level")

                                self.router_id = Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId()
                                self.router_id.parent = self
                                self._children_name_map["router_id"] = "router-id"
                                self._children_yang_names.add("router-id")
                                self._segment_path = lambda: "mpls"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls, ['igp_intact', 'multicast_intact'], name, value)


                            class Level(Entity):
                                """
                                Enable MPLS for an IS\-IS at the given
                                levels
                                
                                .. attribute:: level1
                                
                                	Level 1 enabled
                                	**type**\:  bool
                                
                                .. attribute:: level2
                                
                                	Level 2 enabled
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level, self).__init__()

                                    self.yang_name = "level"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level1 = YLeaf(YType.boolean, "level1")

                                    self.level2 = YLeaf(YType.boolean, "level2")
                                    self._segment_path = lambda: "level"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.Level, ['level1', 'level2'], name, value)


                            class RouterId(Entity):
                                """
                                Traffic Engineering stable IP address for
                                system
                                
                                .. attribute:: address
                                
                                	IPv4 address to be used as a router ID. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId, self).__init__()

                                    self.yang_name = "router-id"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.interface_name = YLeaf(YType.str, "interface-name")
                                    self._segment_path = lambda: "router-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Mpls.RouterId, ['address', 'interface_name'], name, value)


                        class MplsLdpGlobal(Entity):
                            """
                            MPLS LDP configuration. MPLS LDP
                            configuration will only be applied for the
                            IPv4\-unicast address\-family.
                            
                            .. attribute:: auto_config
                            
                            	If TRUE, LDP will be enabled onall IS\-IS interfaces enabled for this address\-family
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal, self).__init__()

                                self.yang_name = "mpls-ldp-global"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.auto_config = YLeaf(YType.boolean, "auto-config")
                                self._segment_path = lambda: "mpls-ldp-global"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.MplsLdpGlobal, ['auto_config'], name, value)


                        class Propagations(Entity):
                            """
                            Route propagation configuration
                            
                            .. attribute:: propagation
                            
                            	Propagate routes between IS\-IS levels
                            	**type**\: list of    :py:class:`Propagation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations, self).__init__()

                                self.yang_name = "propagations"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"propagation" : ("propagation", Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation)}

                                self.propagation = YList(self)
                                self._segment_path = lambda: "propagations"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations, [], name, value)


                            class Propagation(Entity):
                                """
                                Propagate routes between IS\-IS levels
                                
                                .. attribute:: source_level  <key>
                                
                                	Source level for routes
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: destination_level  <key>
                                
                                	Destination level for routes.  Must differ from SourceLevel
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: route_policy_name
                                
                                	Route policy limiting routes to be propagated
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation, self).__init__()

                                    self.yang_name = "propagation"
                                    self.yang_parent_name = "propagations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.source_level = YLeaf(YType.enumeration, "source-level")

                                    self.destination_level = YLeaf(YType.enumeration, "destination-level")

                                    self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                    self._segment_path = lambda: "propagation" + "[source-level='" + self.source_level.get() + "']" + "[destination-level='" + self.destination_level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Propagations.Propagation, ['source_level', 'destination_level', 'route_policy_name'], name, value)


                        class Redistributions(Entity):
                            """
                            Protocol redistribution configuration
                            
                            .. attribute:: redistribution
                            
                            	Redistribution of other protocols into this IS\-IS instance
                            	**type**\: list of    :py:class:`Redistribution <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions, self).__init__()

                                self.yang_name = "redistributions"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"redistribution" : ("redistribution", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution)}

                                self.redistribution = YList(self)
                                self._segment_path = lambda: "redistributions"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions, [], name, value)


                            class Redistribution(Entity):
                                """
                                Redistribution of other protocols into
                                this IS\-IS instance
                                
                                .. attribute:: protocol_name  <key>
                                
                                	The protocol to be redistributed.  OSPFv3 may not be specified for an IPv4 topology and OSPF may not be specified for an IPv6 topology
                                	**type**\:   :py:class:`IsisRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRedistProto>`
                                
                                .. attribute:: bgp
                                
                                	bgp
                                	**type**\: list of    :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp>`
                                
                                .. attribute:: connected_or_static_or_rip_or_subscriber_or_mobile
                                
                                	connected or static or rip or subscriber or mobile
                                	**type**\:   :py:class:`ConnectedOrStaticOrRipOrSubscriberOrMobile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: eigrp
                                
                                	eigrp
                                	**type**\: list of    :py:class:`Eigrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp>`
                                
                                .. attribute:: ospf_or_ospfv3_or_isis_or_application
                                
                                	ospf or ospfv3 or isis or application
                                	**type**\: list of    :py:class:`OspfOrOspfv3OrIsisOrApplication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution, self).__init__()

                                    self.yang_name = "redistribution"
                                    self.yang_parent_name = "redistributions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"connected-or-static-or-rip-or-subscriber-or-mobile" : ("connected_or_static_or_rip_or_subscriber_or_mobile", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile)}
                                    self._child_list_classes = {"bgp" : ("bgp", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp), "eigrp" : ("eigrp", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp), "ospf-or-ospfv3-or-isis-or-application" : ("ospf_or_ospfv3_or_isis_or_application", Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication)}

                                    self.protocol_name = YLeaf(YType.enumeration, "protocol-name")

                                    self.connected_or_static_or_rip_or_subscriber_or_mobile = None
                                    self._children_name_map["connected_or_static_or_rip_or_subscriber_or_mobile"] = "connected-or-static-or-rip-or-subscriber-or-mobile"
                                    self._children_yang_names.add("connected-or-static-or-rip-or-subscriber-or-mobile")

                                    self.bgp = YList(self)
                                    self.eigrp = YList(self)
                                    self.ospf_or_ospfv3_or_isis_or_application = YList(self)
                                    self._segment_path = lambda: "redistribution" + "[protocol-name='" + self.protocol_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution, ['protocol_name'], name, value)


                                class Bgp(Entity):
                                    """
                                    bgp
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	First half of BGP AS number in XX.YY format.  Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if second half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  <key>
                                    
                                    	Second half of BGP AS number in XX.YY format. Mandatory if Protocol is BGP and must not be specified otherwise. Must be a non\-zero value if first half is zero
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp, self).__init__()

                                        self.yang_name = "bgp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.as_xx = YLeaf(YType.uint32, "as-xx")

                                        self.as_yy = YLeaf(YType.uint32, "as-yy")

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "bgp" + "[as-xx='" + self.as_xx.get() + "']" + "[as-yy='" + self.as_yy.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Bgp, ['as_xx', 'as_yy', 'levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                                class ConnectedOrStaticOrRipOrSubscriberOrMobile(Entity):
                                    """
                                    connected or static or rip or subscriber
                                    or mobile
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, self).__init__()

                                        self.yang_name = "connected-or-static-or-rip-or-subscriber-or-mobile"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "connected-or-static-or-rip-or-subscriber-or-mobile"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.ConnectedOrStaticOrRipOrSubscriberOrMobile, ['levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                                class Eigrp(Entity):
                                    """
                                    eigrp
                                    
                                    .. attribute:: as_zz  <key>
                                    
                                    	Eigrp as number
                                    	**type**\:  int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp, self).__init__()

                                        self.yang_name = "eigrp"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.as_zz = YLeaf(YType.uint32, "as-zz")

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "eigrp" + "[as-zz='" + self.as_zz.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.Eigrp, ['as_zz', 'levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                                class OspfOrOspfv3OrIsisOrApplication(Entity):
                                    """
                                    ospf or ospfv3 or isis or application
                                    
                                    .. attribute:: instance_name  <key>
                                    
                                    	Protocol Instance Identifier.  Mandatory for ISIS, OSPF and application, must not be specified otherwise
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: levels
                                    
                                    	Levels to redistribute routes into
                                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                                    	**type**\:  int
                                    
                                    	**range:** 0..16777215
                                    
                                    .. attribute:: metric_type
                                    
                                    	IS\-IS metric type
                                    	**type**\:   :py:class:`IsisMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisMetric>`
                                    
                                    .. attribute:: ospf_route_type
                                    
                                    	OSPF route types to redistribute.  May only be specified if Protocol is OSPF
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: route_policy_name
                                    
                                    	Route policy to control redistribution
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, self).__init__()

                                        self.yang_name = "ospf-or-ospfv3-or-isis-or-application"
                                        self.yang_parent_name = "redistribution"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.instance_name = YLeaf(YType.str, "instance-name")

                                        self.levels = YLeaf(YType.enumeration, "levels")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                        self.ospf_route_type = YLeaf(YType.int32, "ospf-route-type")

                                        self.route_policy_name = YLeaf(YType.str, "route-policy-name")
                                        self._segment_path = lambda: "ospf-or-ospfv3-or-isis-or-application" + "[instance-name='" + self.instance_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Redistributions.Redistribution.OspfOrOspfv3OrIsisOrApplication, ['instance_name', 'levels', 'metric', 'metric_type', 'ospf_route_type', 'route_policy_name'], name, value)


                        class RouterId(Entity):
                            """
                            Stable IP address for system. Will only be
                            applied for the unicast sub\-address\-family.
                            
                            .. attribute:: address
                            
                            	IPv4/IPv6 address to be used as a router ID. Precisely one of Address and Interface must be specified
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: interface_name
                            
                            	Interface with designated stable IP address to be used as a router ID. This must be a Loopback interface. Precisely one of Address and Interface must be specified
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.RouterId, self).__init__()

                                self.yang_name = "router-id"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.address = YLeaf(YType.str, "address")

                                self.interface_name = YLeaf(YType.str, "interface-name")
                                self._segment_path = lambda: "router-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.RouterId, ['address', 'interface_name'], name, value)


                        class SegmentRouting(Entity):
                            """
                            Enable Segment Routing configuration
                            
                            .. attribute:: bundle_member_adj_sid
                            
                            	Enable per bundle member adjacency SID
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: mpls
                            
                            	Prefer segment routing labels over LDP labels
                            	**type**\:   :py:class:`IsisLabelPreference <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisLabelPreference>`
                            
                            .. attribute:: prefix_sid_map
                            
                            	Enable Segment Routing prefix SID map configuration
                            	**type**\:   :py:class:`PrefixSidMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting, self).__init__()

                                self.yang_name = "segment-routing"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"prefix-sid-map" : ("prefix_sid_map", Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap)}
                                self._child_list_classes = {}

                                self.bundle_member_adj_sid = YLeaf(YType.empty, "bundle-member-adj-sid")

                                self.mpls = YLeaf(YType.enumeration, "mpls")

                                self.prefix_sid_map = Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap()
                                self.prefix_sid_map.parent = self
                                self._children_name_map["prefix_sid_map"] = "prefix-sid-map"
                                self._children_yang_names.add("prefix-sid-map")
                                self._segment_path = lambda: "segment-routing"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting, ['bundle_member_adj_sid', 'mpls'], name, value)


                            class PrefixSidMap(Entity):
                                """
                                Enable Segment Routing prefix SID map
                                configuration
                                
                                .. attribute:: advertise_local
                                
                                	Enable Segment Routing prefix SID map advertise local
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: receive
                                
                                	If TRUE, remote prefix SID map advertisements will be used. If FALSE, they will not be used
                                	**type**\:  bool
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap, self).__init__()

                                    self.yang_name = "prefix-sid-map"
                                    self.yang_parent_name = "segment-routing"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.advertise_local = YLeaf(YType.empty, "advertise-local")

                                    self.receive = YLeaf(YType.boolean, "receive")
                                    self._segment_path = lambda: "prefix-sid-map"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SegmentRouting.PrefixSidMap, ['advertise_local', 'receive'], name, value)


                        class SpfIntervals(Entity):
                            """
                            SPF\-interval configuration
                            
                            .. attribute:: spf_interval
                            
                            	Route calculation scheduling parameters
                            	**type**\: list of    :py:class:`SpfInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals, self).__init__()

                                self.yang_name = "spf-intervals"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"spf-interval" : ("spf_interval", Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval)}

                                self.spf_interval = YList(self)
                                self._segment_path = lambda: "spf-intervals"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals, [], name, value)


                            class SpfInterval(Entity):
                                """
                                Route calculation scheduling parameters
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: initial_wait
                                
                                	Initial wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: maximum_wait
                                
                                	Maximum wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                .. attribute:: secondary_wait
                                
                                	Secondary wait before running a route calculation in milliseconds
                                	**type**\:  int
                                
                                	**range:** 0..120000
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval, self).__init__()

                                    self.yang_name = "spf-interval"
                                    self.yang_parent_name = "spf-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.initial_wait = YLeaf(YType.uint32, "initial-wait")

                                    self.maximum_wait = YLeaf(YType.uint32, "maximum-wait")

                                    self.secondary_wait = YLeaf(YType.uint32, "secondary-wait")
                                    self._segment_path = lambda: "spf-interval" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfIntervals.SpfInterval, ['level', 'initial_wait', 'maximum_wait', 'secondary_wait'], name, value)


                        class SpfPeriodicIntervals(Entity):
                            """
                            Peoridic SPF configuration
                            
                            .. attribute:: spf_periodic_interval
                            
                            	Maximum interval between spf runs
                            	**type**\: list of    :py:class:`SpfPeriodicInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals, self).__init__()

                                self.yang_name = "spf-periodic-intervals"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"spf-periodic-interval" : ("spf_periodic_interval", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval)}

                                self.spf_periodic_interval = YList(self)
                                self._segment_path = lambda: "spf-periodic-intervals"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals, [], name, value)


                            class SpfPeriodicInterval(Entity):
                                """
                                Maximum interval between spf runs
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: periodic_interval
                                
                                	Maximum interval in between SPF runs in seconds
                                	**type**\:  int
                                
                                	**range:** 0..3600
                                
                                	**mandatory**\: True
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval, self).__init__()

                                    self.yang_name = "spf-periodic-interval"
                                    self.yang_parent_name = "spf-periodic-intervals"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.periodic_interval = YLeaf(YType.uint32, "periodic-interval")
                                    self._segment_path = lambda: "spf-periodic-interval" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPeriodicIntervals.SpfPeriodicInterval, ['level', 'periodic_interval'], name, value)


                        class SpfPrefixPriorities(Entity):
                            """
                            SPF Prefix Priority configuration
                            
                            .. attribute:: spf_prefix_priority
                            
                            	Determine SPF priority for prefixes
                            	**type**\: list of    :py:class:`SpfPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities, self).__init__()

                                self.yang_name = "spf-prefix-priorities"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"spf-prefix-priority" : ("spf_prefix_priority", Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority)}

                                self.spf_prefix_priority = YList(self)
                                self._segment_path = lambda: "spf-prefix-priorities"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities, [], name, value)


                            class SpfPrefixPriority(Entity):
                                """
                                Determine SPF priority for prefixes
                                
                                .. attribute:: level  <key>
                                
                                	SPF Level for prefix prioritization
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: prefix_priority_type  <key>
                                
                                	SPF Priority to assign matching prefixes
                                	**type**\:   :py:class:`IsisPrefixPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisPrefixPriority>`
                                
                                .. attribute:: access_list_name
                                
                                	Access List to determine prefixes for this priority
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                .. attribute:: admin_tag
                                
                                	Tag value to determine prefixes for this priority
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority, self).__init__()

                                    self.yang_name = "spf-prefix-priority"
                                    self.yang_parent_name = "spf-prefix-priorities"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.prefix_priority_type = YLeaf(YType.enumeration, "prefix-priority-type")

                                    self.access_list_name = YLeaf(YType.str, "access-list-name")

                                    self.admin_tag = YLeaf(YType.uint32, "admin-tag")
                                    self._segment_path = lambda: "spf-prefix-priority" + "[level='" + self.level.get() + "']" + "[prefix-priority-type='" + self.prefix_priority_type.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SpfPrefixPriorities.SpfPrefixPriority, ['level', 'prefix_priority_type', 'access_list_name', 'admin_tag'], name, value)


                        class SummaryPrefixes(Entity):
                            """
                            Summary\-prefix configuration
                            
                            .. attribute:: summary_prefix
                            
                            	Configure IP address prefixes to advertise
                            	**type**\: list of    :py:class:`SummaryPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes, self).__init__()

                                self.yang_name = "summary-prefixes"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"summary-prefix" : ("summary_prefix", Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix)}

                                self.summary_prefix = YList(self)
                                self._segment_path = lambda: "summary-prefixes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes, [], name, value)


                            class SummaryPrefix(Entity):
                                """
                                Configure IP address prefixes to advertise
                                
                                .. attribute:: address_prefix  <key>
                                
                                	IP summary address prefix
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                                
                                
                                ----
                                .. attribute:: level
                                
                                	Level in which to summarize routes
                                	**type**\:  int
                                
                                	**range:** 1..2
                                
                                .. attribute:: tag
                                
                                	The tag value
                                	**type**\:  int
                                
                                	**range:** 1..4294967295
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix, self).__init__()

                                    self.yang_name = "summary-prefix"
                                    self.yang_parent_name = "summary-prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address_prefix = YLeaf(YType.str, "address-prefix")

                                    self.level = YLeaf(YType.uint32, "level")

                                    self.tag = YLeaf(YType.uint32, "tag")
                                    self._segment_path = lambda: "summary-prefix" + "[address-prefix='" + self.address_prefix.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.SummaryPrefixes.SummaryPrefix, ['address_prefix', 'level', 'tag'], name, value)


                        class Ucmp(Entity):
                            """
                            UCMP (UnEqual Cost MultiPath) configuration
                            
                            .. attribute:: delay_interval
                            
                            	Delay in msecs between primary SPF and UCMP computation
                            	**type**\:  int
                            
                            	**range:** 100..65535
                            
                            	**units**\: millisecond
                            
                            	**default value**\: 100
                            
                            .. attribute:: enable
                            
                            	UCMP feature enable configuration
                            	**type**\:   :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable>`
                            
                            .. attribute:: exclude_interfaces
                            
                            	Interfaces excluded from UCMP path computation
                            	**type**\:   :py:class:`ExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp, self).__init__()

                                self.yang_name = "ucmp"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"enable" : ("enable", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable), "exclude-interfaces" : ("exclude_interfaces", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces)}
                                self._child_list_classes = {}

                                self.delay_interval = YLeaf(YType.uint32, "delay-interval")

                                self.enable = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable()
                                self.enable.parent = self
                                self._children_name_map["enable"] = "enable"
                                self._children_yang_names.add("enable")

                                self.exclude_interfaces = Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces()
                                self.exclude_interfaces.parent = self
                                self._children_name_map["exclude_interfaces"] = "exclude-interfaces"
                                self._children_yang_names.add("exclude-interfaces")
                                self._segment_path = lambda: "ucmp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp, ['delay_interval'], name, value)


                            class Enable(Entity):
                                """
                                UCMP feature enable configuration
                                
                                .. attribute:: prefix_list_name
                                
                                	Name of the Prefix List
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: variance
                                
                                	Value of variance
                                	**type**\:  int
                                
                                	**range:** 101..10000
                                
                                	**default value**\: 200
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable, self).__init__()

                                    self.yang_name = "enable"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.prefix_list_name = YLeaf(YType.str, "prefix-list-name")

                                    self.variance = YLeaf(YType.uint32, "variance")
                                    self._segment_path = lambda: "enable"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.Enable, ['prefix_list_name', 'variance'], name, value)


                            class ExcludeInterfaces(Entity):
                                """
                                Interfaces excluded from UCMP path
                                computation
                                
                                .. attribute:: exclude_interface
                                
                                	Exclude this interface from UCMP path computation
                                	**type**\: list of    :py:class:`ExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces, self).__init__()

                                    self.yang_name = "exclude-interfaces"
                                    self.yang_parent_name = "ucmp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"exclude-interface" : ("exclude_interface", Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface)}

                                    self.exclude_interface = YList(self)
                                    self._segment_path = lambda: "exclude-interfaces"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces, [], name, value)


                                class ExcludeInterface(Entity):
                                    """
                                    Exclude this interface from UCMP path
                                    computation
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Name of the interface to be excluded
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface, self).__init__()

                                        self.yang_name = "exclude-interface"
                                        self.yang_parent_name = "exclude-interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.interface_name = YLeaf(YType.str, "interface-name")
                                        self._segment_path = lambda: "exclude-interface" + "[interface-name='" + self.interface_name.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Ucmp.ExcludeInterfaces.ExcludeInterface, ['interface_name'], name, value)


                        class Weights(Entity):
                            """
                            Weight configuration
                            
                            .. attribute:: weight
                            
                            	Weight configuration under interface for load balancing
                            	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Afs.Af.TopologyName.Weights, self).__init__()

                                self.yang_name = "weights"
                                self.yang_parent_name = "topology-name"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"weight" : ("weight", Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight)}

                                self.weight = YList(self)
                                self._segment_path = lambda: "weights"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Weights, [], name, value)


                            class Weight(Entity):
                                """
                                Weight configuration under interface for load
                                balancing
                                
                                .. attribute:: level  <key>
                                
                                	Level to which configuration applies
                                	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                
                                .. attribute:: weight
                                
                                	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                	**type**\:  int
                                
                                	**range:** 1..16777214
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight, self).__init__()

                                    self.yang_name = "weight"
                                    self.yang_parent_name = "weights"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.level = YLeaf(YType.enumeration, "level")

                                    self.weight = YLeaf(YType.uint32, "weight")
                                    self._segment_path = lambda: "weight" + "[level='" + self.level.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Afs.Af.TopologyName.Weights.Weight, ['level', 'weight'], name, value)


            class Distribute(Entity):
                """
                IS\-IS Distribute BGP\-LS configuration
                
                .. attribute:: dist_inst_id
                
                	Instance ID
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: dist_throttle
                
                	Seconds
                	**type**\:  int
                
                	**range:** 1..20
                
                	**units**\: second
                
                .. attribute:: level
                
                	Level
                	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.Distribute, self).__init__()

                    self.yang_name = "distribute"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.dist_inst_id = YLeaf(YType.uint32, "dist-inst-id")

                    self.dist_throttle = YLeaf(YType.uint32, "dist-throttle")

                    self.level = YLeaf(YType.enumeration, "level")
                    self._segment_path = lambda: "distribute"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Distribute, ['dist_inst_id', 'dist_throttle', 'level'], name, value)


            class Interfaces(Entity):
                """
                Per\-interface configuration
                
                .. attribute:: interface
                
                	Configuration for an IS\-IS interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", Isis.Instances.Instance.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Configuration for an IS\-IS interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: circuit_type
                    
                    	Configure circuit type for interface
                    	**type**\:   :py:class:`IsisConfigurableLevels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisConfigurableLevels>`
                    
                    	**default value**\: level1-and2
                    
                    .. attribute:: csnp_intervals
                    
                    	CSNP\-interval configuration
                    	**type**\:   :py:class:`CsnpIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals>`
                    
                    .. attribute:: hello_accept_passwords
                    
                    	IIH accept password configuration
                    	**type**\:   :py:class:`HelloAcceptPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords>`
                    
                    .. attribute:: hello_intervals
                    
                    	Hello\-interval configuration
                    	**type**\:   :py:class:`HelloIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals>`
                    
                    .. attribute:: hello_multipliers
                    
                    	Hello\-multiplier configuration
                    	**type**\:   :py:class:`HelloMultipliers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers>`
                    
                    .. attribute:: hello_paddings
                    
                    	Hello\-padding configuration
                    	**type**\:   :py:class:`HelloPaddings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings>`
                    
                    .. attribute:: hello_passwords
                    
                    	IIH password configuration
                    	**type**\:   :py:class:`HelloPasswords <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords>`
                    
                    .. attribute:: interface_afs
                    
                    	Per\-interface address\-family configuration
                    	**type**\:   :py:class:`InterfaceAfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs>`
                    
                    .. attribute:: link_down_fast_detect
                    
                    	Configure high priority detection of interface down event
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: lsp_fast_flood_thresholds
                    
                    	LSP fast flood threshold configuration
                    	**type**\:   :py:class:`LspFastFloodThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds>`
                    
                    .. attribute:: lsp_intervals
                    
                    	LSP\-interval configuration
                    	**type**\:   :py:class:`LspIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals>`
                    
                    .. attribute:: lsp_retransmit_intervals
                    
                    	LSP\-retransmission\-interval configuration
                    	**type**\:   :py:class:`LspRetransmitIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals>`
                    
                    .. attribute:: lsp_retransmit_throttle_intervals
                    
                    	LSP\-retransmission\-throttle\-interval configuration
                    	**type**\:   :py:class:`LspRetransmitThrottleIntervals <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals>`
                    
                    .. attribute:: mesh_group
                    
                    	Mesh\-group configuration
                    	**type**\: one of the below types:
                    
                    	**type**\:   :py:class:`MeshGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.MeshGroup>`
                    
                    
                    ----
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    
                    ----
                    .. attribute:: point_to_point
                    
                    	IS\-IS will attempt to form point\-to\-point over LAN adjacencies over this interface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: prefix_attribute_n_flag_clears
                    
                    	Prefix attribute N flag clear configuration
                    	**type**\:   :py:class:`PrefixAttributeNFlagClears <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears>`
                    
                    .. attribute:: priorities
                    
                    	DIS\-election priority configuration
                    	**type**\:   :py:class:`Priorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities>`
                    
                    .. attribute:: running
                    
                    	This object must be set before any other configuration is supplied for an interface, and must be the last per\-interface configuration object to be removed
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: state
                    
                    	Enable/Disable routing
                    	**type**\:   :py:class:`IsisInterfaceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceState>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"bfd" : ("bfd", Isis.Instances.Instance.Interfaces.Interface.Bfd), "csnp-intervals" : ("csnp_intervals", Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals), "hello-accept-passwords" : ("hello_accept_passwords", Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords), "hello-intervals" : ("hello_intervals", Isis.Instances.Instance.Interfaces.Interface.HelloIntervals), "hello-multipliers" : ("hello_multipliers", Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers), "hello-paddings" : ("hello_paddings", Isis.Instances.Instance.Interfaces.Interface.HelloPaddings), "hello-passwords" : ("hello_passwords", Isis.Instances.Instance.Interfaces.Interface.HelloPasswords), "interface-afs" : ("interface_afs", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs), "lsp-fast-flood-thresholds" : ("lsp_fast_flood_thresholds", Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds), "lsp-intervals" : ("lsp_intervals", Isis.Instances.Instance.Interfaces.Interface.LspIntervals), "lsp-retransmit-intervals" : ("lsp_retransmit_intervals", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals), "lsp-retransmit-throttle-intervals" : ("lsp_retransmit_throttle_intervals", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals), "prefix-attribute-n-flag-clears" : ("prefix_attribute_n_flag_clears", Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears), "priorities" : ("priorities", Isis.Instances.Instance.Interfaces.Interface.Priorities)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.circuit_type = YLeaf(YType.enumeration, "circuit-type")

                        self.link_down_fast_detect = YLeaf(YType.empty, "link-down-fast-detect")

                        self.mesh_group = YLeaf(YType.str, "mesh-group")

                        self.point_to_point = YLeaf(YType.empty, "point-to-point")

                        self.running = YLeaf(YType.empty, "running")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.bfd = Isis.Instances.Instance.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self._children_name_map["bfd"] = "bfd"
                        self._children_yang_names.add("bfd")

                        self.csnp_intervals = Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals()
                        self.csnp_intervals.parent = self
                        self._children_name_map["csnp_intervals"] = "csnp-intervals"
                        self._children_yang_names.add("csnp-intervals")

                        self.hello_accept_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords()
                        self.hello_accept_passwords.parent = self
                        self._children_name_map["hello_accept_passwords"] = "hello-accept-passwords"
                        self._children_yang_names.add("hello-accept-passwords")

                        self.hello_intervals = Isis.Instances.Instance.Interfaces.Interface.HelloIntervals()
                        self.hello_intervals.parent = self
                        self._children_name_map["hello_intervals"] = "hello-intervals"
                        self._children_yang_names.add("hello-intervals")

                        self.hello_multipliers = Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers()
                        self.hello_multipliers.parent = self
                        self._children_name_map["hello_multipliers"] = "hello-multipliers"
                        self._children_yang_names.add("hello-multipliers")

                        self.hello_paddings = Isis.Instances.Instance.Interfaces.Interface.HelloPaddings()
                        self.hello_paddings.parent = self
                        self._children_name_map["hello_paddings"] = "hello-paddings"
                        self._children_yang_names.add("hello-paddings")

                        self.hello_passwords = Isis.Instances.Instance.Interfaces.Interface.HelloPasswords()
                        self.hello_passwords.parent = self
                        self._children_name_map["hello_passwords"] = "hello-passwords"
                        self._children_yang_names.add("hello-passwords")

                        self.interface_afs = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs()
                        self.interface_afs.parent = self
                        self._children_name_map["interface_afs"] = "interface-afs"
                        self._children_yang_names.add("interface-afs")

                        self.lsp_fast_flood_thresholds = Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds()
                        self.lsp_fast_flood_thresholds.parent = self
                        self._children_name_map["lsp_fast_flood_thresholds"] = "lsp-fast-flood-thresholds"
                        self._children_yang_names.add("lsp-fast-flood-thresholds")

                        self.lsp_intervals = Isis.Instances.Instance.Interfaces.Interface.LspIntervals()
                        self.lsp_intervals.parent = self
                        self._children_name_map["lsp_intervals"] = "lsp-intervals"
                        self._children_yang_names.add("lsp-intervals")

                        self.lsp_retransmit_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals()
                        self.lsp_retransmit_intervals.parent = self
                        self._children_name_map["lsp_retransmit_intervals"] = "lsp-retransmit-intervals"
                        self._children_yang_names.add("lsp-retransmit-intervals")

                        self.lsp_retransmit_throttle_intervals = Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals()
                        self.lsp_retransmit_throttle_intervals.parent = self
                        self._children_name_map["lsp_retransmit_throttle_intervals"] = "lsp-retransmit-throttle-intervals"
                        self._children_yang_names.add("lsp-retransmit-throttle-intervals")

                        self.prefix_attribute_n_flag_clears = Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears()
                        self.prefix_attribute_n_flag_clears.parent = self
                        self._children_name_map["prefix_attribute_n_flag_clears"] = "prefix-attribute-n-flag-clears"
                        self._children_yang_names.add("prefix-attribute-n-flag-clears")

                        self.priorities = Isis.Instances.Instance.Interfaces.Interface.Priorities()
                        self.priorities.parent = self
                        self._children_name_map["priorities"] = "priorities"
                        self._children_yang_names.add("priorities")
                        self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface, ['interface_name', 'circuit_type', 'link_down_fast_detect', 'mesh_group', 'point_to_point', 'running', 'state'], name, value)

                    class MeshGroup(Enum):
                        """
                        MeshGroup

                        Mesh\-group configuration

                        .. data:: blocked = 0

                        	Blocked mesh group.  Changed LSPs are not

                        	flooded over blocked interfaces

                        """

                        blocked = Enum.YLeaf(0, "blocked")



                    class Bfd(Entity):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by isis
                        	**type**\:  int
                        
                        	**range:** 2..50
                        
                        .. attribute:: enable_ipv4
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\:  bool
                        
                        .. attribute:: enable_ipv6
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\:  bool
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by isis
                        	**type**\:  int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.Bfd, self).__init__()

                            self.yang_name = "bfd"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.detection_multiplier = YLeaf(YType.uint32, "detection-multiplier")

                            self.enable_ipv4 = YLeaf(YType.boolean, "enable-ipv4")

                            self.enable_ipv6 = YLeaf(YType.boolean, "enable-ipv6")

                            self.interval = YLeaf(YType.uint32, "interval")
                            self._segment_path = lambda: "bfd"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.Bfd, ['detection_multiplier', 'enable_ipv4', 'enable_ipv6', 'interval'], name, value)


                    class CsnpIntervals(Entity):
                        """
                        CSNP\-interval configuration
                        
                        .. attribute:: csnp_interval
                        
                        	CSNP\-interval configuration. No fixed default value as this depends on the media type of the interface
                        	**type**\: list of    :py:class:`CsnpInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals, self).__init__()

                            self.yang_name = "csnp-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"csnp-interval" : ("csnp_interval", Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval)}

                            self.csnp_interval = YList(self)
                            self._segment_path = lambda: "csnp-intervals"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals, [], name, value)


                        class CsnpInterval(Entity):
                            """
                            CSNP\-interval configuration. No fixed
                            default value as this depends on the media
                            type of the interface.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval, self).__init__()

                                self.yang_name = "csnp-interval"
                                self.yang_parent_name = "csnp-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.interval = YLeaf(YType.uint32, "interval")
                                self._segment_path = lambda: "csnp-interval" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.CsnpIntervals.CsnpInterval, ['level', 'interval'], name, value)


                    class HelloAcceptPasswords(Entity):
                        """
                        IIH accept password configuration
                        
                        .. attribute:: hello_accept_password
                        
                        	IIH accept passwords. This requires the existence of a HelloPassword of the same level
                        	**type**\: list of    :py:class:`HelloAcceptPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords, self).__init__()

                            self.yang_name = "hello-accept-passwords"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hello-accept-password" : ("hello_accept_password", Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword)}

                            self.hello_accept_password = YList(self)
                            self._segment_path = lambda: "hello-accept-passwords"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords, [], name, value)


                        class HelloAcceptPassword(Entity):
                            """
                            IIH accept passwords. This requires the
                            existence of a HelloPassword of the same
                            level.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: password
                            
                            	Password
                            	**type**\:  str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword, self).__init__()

                                self.yang_name = "hello-accept-password"
                                self.yang_parent_name = "hello-accept-passwords"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.password = YLeaf(YType.str, "password")
                                self._segment_path = lambda: "hello-accept-password" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloAcceptPasswords.HelloAcceptPassword, ['level', 'password'], name, value)


                    class HelloIntervals(Entity):
                        """
                        Hello\-interval configuration
                        
                        .. attribute:: hello_interval
                        
                        	Hello\-interval configuration. The interval at which IIH packets will be sent. This will be three times quicker on a LAN interface which has been electted DIS
                        	**type**\: list of    :py:class:`HelloInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals, self).__init__()

                            self.yang_name = "hello-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hello-interval" : ("hello_interval", Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval)}

                            self.hello_interval = YList(self)
                            self._segment_path = lambda: "hello-intervals"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals, [], name, value)


                        class HelloInterval(Entity):
                            """
                            Hello\-interval configuration. The interval
                            at which IIH packets will be sent. This
                            will be three times quicker on a LAN
                            interface which has been electted DIS.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval, self).__init__()

                                self.yang_name = "hello-interval"
                                self.yang_parent_name = "hello-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.interval = YLeaf(YType.uint32, "interval")
                                self._segment_path = lambda: "hello-interval" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloIntervals.HelloInterval, ['level', 'interval'], name, value)


                    class HelloMultipliers(Entity):
                        """
                        Hello\-multiplier configuration
                        
                        .. attribute:: hello_multiplier
                        
                        	Hello\-multiplier configuration. The number of successive IIHs that may be missed on an adjacency before it is considered down
                        	**type**\: list of    :py:class:`HelloMultiplier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers, self).__init__()

                            self.yang_name = "hello-multipliers"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hello-multiplier" : ("hello_multiplier", Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier)}

                            self.hello_multiplier = YList(self)
                            self._segment_path = lambda: "hello-multipliers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers, [], name, value)


                        class HelloMultiplier(Entity):
                            """
                            Hello\-multiplier configuration. The number
                            of successive IIHs that may be missed on an
                            adjacency before it is considered down.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: multiplier
                            
                            	Hello multiplier value
                            	**type**\:  int
                            
                            	**range:** 3..1000
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier, self).__init__()

                                self.yang_name = "hello-multiplier"
                                self.yang_parent_name = "hello-multipliers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.multiplier = YLeaf(YType.uint32, "multiplier")
                                self._segment_path = lambda: "hello-multiplier" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloMultipliers.HelloMultiplier, ['level', 'multiplier'], name, value)


                    class HelloPaddings(Entity):
                        """
                        Hello\-padding configuration
                        
                        .. attribute:: hello_padding
                        
                        	Pad IIHs to the interface MTU
                        	**type**\: list of    :py:class:`HelloPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings, self).__init__()

                            self.yang_name = "hello-paddings"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hello-padding" : ("hello_padding", Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding)}

                            self.hello_padding = YList(self)
                            self._segment_path = lambda: "hello-paddings"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings, [], name, value)


                        class HelloPadding(Entity):
                            """
                            Pad IIHs to the interface MTU
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: padding_type
                            
                            	Hello padding type value
                            	**type**\:   :py:class:`IsisHelloPadding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisHelloPadding>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding, self).__init__()

                                self.yang_name = "hello-padding"
                                self.yang_parent_name = "hello-paddings"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.padding_type = YLeaf(YType.enumeration, "padding-type")
                                self._segment_path = lambda: "hello-padding" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPaddings.HelloPadding, ['level', 'padding_type'], name, value)


                    class HelloPasswords(Entity):
                        """
                        IIH password configuration
                        
                        .. attribute:: hello_password
                        
                        	IIH passwords. This must exist if a HelloAcceptPassword of the same level exists
                        	**type**\: list of    :py:class:`HelloPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords, self).__init__()

                            self.yang_name = "hello-passwords"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hello-password" : ("hello_password", Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword)}

                            self.hello_password = YList(self)
                            self._segment_path = lambda: "hello-passwords"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords, [], name, value)


                        class HelloPassword(Entity):
                            """
                            IIH passwords. This must exist if a
                            HelloAcceptPassword of the same level
                            exists.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: algorithm
                            
                            	Algorithm
                            	**type**\:   :py:class:`IsisAuthenticationAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithm>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: failure_mode
                            
                            	Failure Mode
                            	**type**\:   :py:class:`IsisAuthenticationFailureMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureMode>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: password
                            
                            	Password or unencrypted Key Chain name
                            	**type**\:  str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword, self).__init__()

                                self.yang_name = "hello-password"
                                self.yang_parent_name = "hello-passwords"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.algorithm = YLeaf(YType.enumeration, "algorithm")

                                self.failure_mode = YLeaf(YType.enumeration, "failure-mode")

                                self.password = YLeaf(YType.str, "password")
                                self._segment_path = lambda: "hello-password" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.HelloPasswords.HelloPassword, ['level', 'algorithm', 'failure_mode', 'password'], name, value)


                    class InterfaceAfs(Entity):
                        """
                        Per\-interface address\-family configuration
                        
                        .. attribute:: interface_af
                        
                        	Configuration for an IS\-IS address\-family on a single interface. If a named (non\-default) topology is being created it must be multicast. Also the topology ID mustbe set first and delete last in the router configuration
                        	**type**\: list of    :py:class:`InterfaceAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs, self).__init__()

                            self.yang_name = "interface-afs"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"interface-af" : ("interface_af", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf)}

                            self.interface_af = YList(self)
                            self._segment_path = lambda: "interface-afs"

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
                            
                            .. attribute:: af_name  <key>
                            
                            	Address family
                            	**type**\:   :py:class:`IsisAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisAddressFamily>`
                            
                            .. attribute:: saf_name  <key>
                            
                            	Sub address family
                            	**type**\:   :py:class:`IsisSubAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisSubAddressFamily>`
                            
                            .. attribute:: interface_af_data
                            
                            	Data container
                            	**type**\:   :py:class:`InterfaceAfData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData>`
                            
                            .. attribute:: topology_name
                            
                            	keys\: topology\-name
                            	**type**\: list of    :py:class:`TopologyName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf, self).__init__()

                                self.yang_name = "interface-af"
                                self.yang_parent_name = "interface-afs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"interface-af-data" : ("interface_af_data", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData)}
                                self._child_list_classes = {"topology-name" : ("topology_name", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName)}

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.saf_name = YLeaf(YType.enumeration, "saf-name")

                                self.interface_af_data = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData()
                                self.interface_af_data.parent = self
                                self._children_name_map["interface_af_data"] = "interface-af-data"
                                self._children_yang_names.add("interface-af-data")

                                self.topology_name = YList(self)
                                self._segment_path = lambda: "interface-af" + "[af-name='" + self.af_name.get() + "']" + "[saf-name='" + self.saf_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf, ['af_name', 'saf_name'], name, value)


                            class InterfaceAfData(Entity):
                                """
                                Data container.
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\:   :py:class:`AdminTags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\:   :py:class:`AutoMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics>`
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\:   :py:class:`IsisInterfaceAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfState>`
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\:   :py:class:`InterfaceFrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\:   :py:class:`InterfaceLinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: manual_adj_sids
                                
                                	Manual Adjacecy SID configuration
                                	**type**\:   :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids>`
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp>`
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: prefix_sspfsid
                                
                                	Assign prefix SSPF SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSspfsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData, self).__init__()

                                    self.yang_name = "interface-af-data"
                                    self.yang_parent_name = "interface-af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"admin-tags" : ("admin_tags", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags), "auto-metrics" : ("auto_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics), "interface-frr-table" : ("interface_frr_table", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable), "interface-link-group" : ("interface_link_group", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup), "manual-adj-sids" : ("manual_adj_sids", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids), "metrics" : ("metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics), "mpls-ldp" : ("mpls_ldp", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp), "prefix-sid" : ("prefix_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid), "prefix-sspfsid" : ("prefix_sspfsid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid), "weights" : ("weights", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights)}
                                    self._child_list_classes = {}

                                    self.interface_af_state = YLeaf(YType.enumeration, "interface-af-state")

                                    self.running = YLeaf(YType.empty, "running")

                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags()
                                    self.admin_tags.parent = self
                                    self._children_name_map["admin_tags"] = "admin-tags"
                                    self._children_yang_names.add("admin-tags")

                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self._children_name_map["auto_metrics"] = "auto-metrics"
                                    self._children_yang_names.add("auto-metrics")

                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self._children_name_map["interface_frr_table"] = "interface-frr-table"
                                    self._children_yang_names.add("interface-frr-table")

                                    self.interface_link_group = None
                                    self._children_name_map["interface_link_group"] = "interface-link-group"
                                    self._children_yang_names.add("interface-link-group")

                                    self.manual_adj_sids = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids()
                                    self.manual_adj_sids.parent = self
                                    self._children_name_map["manual_adj_sids"] = "manual-adj-sids"
                                    self._children_yang_names.add("manual-adj-sids")

                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics()
                                    self.metrics.parent = self
                                    self._children_name_map["metrics"] = "metrics"
                                    self._children_yang_names.add("metrics")

                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self._children_name_map["mpls_ldp"] = "mpls-ldp"
                                    self._children_yang_names.add("mpls-ldp")

                                    self.prefix_sid = None
                                    self._children_name_map["prefix_sid"] = "prefix-sid"
                                    self._children_yang_names.add("prefix-sid")

                                    self.prefix_sspfsid = None
                                    self._children_name_map["prefix_sspfsid"] = "prefix-sspfsid"
                                    self._children_yang_names.add("prefix-sspfsid")

                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights()
                                    self.weights.parent = self
                                    self._children_name_map["weights"] = "weights"
                                    self._children_yang_names.add("weights")
                                    self._segment_path = lambda: "interface-af-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData, ['interface_af_state', 'running'], name, value)


                                class AdminTags(Entity):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of    :py:class:`AdminTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags, self).__init__()

                                        self.yang_name = "admin-tags"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"admin-tag" : ("admin_tag", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag)}

                                        self.admin_tag = YList(self)
                                        self._segment_path = lambda: "admin-tags"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags, [], name, value)


                                    class AdminTag(Entity):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag, self).__init__()

                                            self.yang_name = "admin-tag"
                                            self.yang_parent_name = "admin-tags"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.admin_tag = YLeaf(YType.uint32, "admin-tag")
                                            self._segment_path = lambda: "admin-tag" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AdminTags.AdminTag, ['level', 'admin_tag'], name, value)


                                class AutoMetrics(Entity):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of    :py:class:`AutoMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics, self).__init__()

                                        self.yang_name = "auto-metrics"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"auto-metric" : ("auto_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric)}

                                        self.auto_metric = YList(self)
                                        self._segment_path = lambda: "auto-metrics"

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
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric, self).__init__()

                                            self.yang_name = "auto-metric"
                                            self.yang_parent_name = "auto-metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.proactive_protect = YLeaf(YType.uint32, "proactive-protect")
                                            self._segment_path = lambda: "auto-metric" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.AutoMetrics.AutoMetric, ['level', 'proactive_protect'], name, value)


                                class InterfaceFrrTable(Entity):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\:   :py:class:`FrrExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\:   :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\:   :py:class:`FrrRemoteLfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\:   :py:class:`FrrTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\:   :py:class:`FrrlfaCandidateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\:   :py:class:`FrrtilfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    .. attribute:: interface_frr_tiebreaker_defaults
                                    
                                    	Interface FRR Default tiebreaker configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakerDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults>`
                                    
                                    .. attribute:: interface_frr_tiebreakers
                                    
                                    	Interface FRR tiebreakers configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable, self).__init__()

                                        self.yang_name = "interface-frr-table"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"frr-exclude-interfaces" : ("frr_exclude_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces), "frr-remote-lfa-max-metrics" : ("frr_remote_lfa_max_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics), "frr-remote-lfa-types" : ("frr_remote_lfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes), "frr-types" : ("frr_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes), "frrlfa-candidate-interfaces" : ("frrlfa_candidate_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces), "frrtilfa-types" : ("frrtilfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes), "interface-frr-tiebreaker-defaults" : ("interface_frr_tiebreaker_defaults", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults), "interface-frr-tiebreakers" : ("interface_frr_tiebreakers", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers)}
                                        self._child_list_classes = {}

                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self._children_name_map["frr_exclude_interfaces"] = "frr-exclude-interfaces"
                                        self._children_yang_names.add("frr-exclude-interfaces")

                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self._children_name_map["frr_remote_lfa_max_metrics"] = "frr-remote-lfa-max-metrics"
                                        self._children_yang_names.add("frr-remote-lfa-max-metrics")

                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self._children_name_map["frr_remote_lfa_types"] = "frr-remote-lfa-types"
                                        self._children_yang_names.add("frr-remote-lfa-types")

                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self._children_name_map["frr_types"] = "frr-types"
                                        self._children_yang_names.add("frr-types")

                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self._children_name_map["frrlfa_candidate_interfaces"] = "frrlfa-candidate-interfaces"
                                        self._children_yang_names.add("frrlfa-candidate-interfaces")

                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self
                                        self._children_name_map["frrtilfa_types"] = "frrtilfa-types"
                                        self._children_yang_names.add("frrtilfa-types")

                                        self.interface_frr_tiebreaker_defaults = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults()
                                        self.interface_frr_tiebreaker_defaults.parent = self
                                        self._children_name_map["interface_frr_tiebreaker_defaults"] = "interface-frr-tiebreaker-defaults"
                                        self._children_yang_names.add("interface-frr-tiebreaker-defaults")

                                        self.interface_frr_tiebreakers = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers()
                                        self.interface_frr_tiebreakers.parent = self
                                        self._children_name_map["interface_frr_tiebreakers"] = "interface-frr-tiebreakers"
                                        self._children_yang_names.add("interface-frr-tiebreakers")
                                        self._segment_path = lambda: "interface-frr-table"


                                    class FrrExcludeInterfaces(Entity):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of    :py:class:`FrrExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces, self).__init__()

                                            self.yang_name = "frr-exclude-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-exclude-interface" : ("frr_exclude_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface)}

                                            self.frr_exclude_interface = YList(self)
                                            self._segment_path = lambda: "frr-exclude-interfaces"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces, [], name, value)


                                        class FrrExcludeInterface(Entity):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, self).__init__()

                                                self.yang_name = "frr-exclude-interface"
                                                self.yang_parent_name = "frr-exclude-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.interface_name = YLeaf(YType.str, "interface-name")

                                                self.frr_type = YLeaf(YType.enumeration, "frr-type")

                                                self.level = YLeaf(YType.uint32, "level")
                                                self._segment_path = lambda: "frr-exclude-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class FrrRemoteLfaMaxMetrics(Entity):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of    :py:class:`FrrRemoteLfaMaxMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, self).__init__()

                                            self.yang_name = "frr-remote-lfa-max-metrics"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-remote-lfa-max-metric" : ("frr_remote_lfa_max_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric)}

                                            self.frr_remote_lfa_max_metric = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-max-metrics"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, [], name, value)


                                        class FrrRemoteLfaMaxMetric(Entity):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\:  int
                                            
                                            	**range:** 1..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, self).__init__()

                                                self.yang_name = "frr-remote-lfa-max-metric"
                                                self.yang_parent_name = "frr-remote-lfa-max-metrics"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.max_metric = YLeaf(YType.uint32, "max-metric")
                                                self._segment_path = lambda: "frr-remote-lfa-max-metric" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, ['level', 'max_metric'], name, value)


                                    class FrrRemoteLfaTypes(Entity):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrRemoteLfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes, self).__init__()

                                            self.yang_name = "frr-remote-lfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-remote-lfa-type" : ("frr_remote_lfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType)}

                                            self.frr_remote_lfa_type = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-types"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes, [], name, value)


                                        class FrrRemoteLfaType(Entity):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\:   :py:class:`IsisRemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfa>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, self).__init__()

                                                self.yang_name = "frr-remote-lfa-type"
                                                self.yang_parent_name = "frr-remote-lfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.type = YLeaf(YType.enumeration, "type")
                                                self._segment_path = lambda: "frr-remote-lfa-type" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, ['level', 'type'], name, value)


                                    class FrrTypes(Entity):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of    :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes, self).__init__()

                                            self.yang_name = "frr-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-type" : ("frr_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType)}

                                            self.frr_type = YList(self)
                                            self._segment_path = lambda: "frr-types"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes, [], name, value)


                                        class FrrType(Entity):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType, self).__init__()

                                                self.yang_name = "frr-type"
                                                self.yang_parent_name = "frr-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.type = YLeaf(YType.enumeration, "type")
                                                self._segment_path = lambda: "frr-type" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrTypes.FrrType, ['level', 'type'], name, value)


                                    class FrrlfaCandidateInterfaces(Entity):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of    :py:class:`FrrlfaCandidateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces, self).__init__()

                                            self.yang_name = "frrlfa-candidate-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frrlfa-candidate-interface" : ("frrlfa_candidate_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface)}

                                            self.frrlfa_candidate_interface = YList(self)
                                            self._segment_path = lambda: "frrlfa-candidate-interfaces"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces, [], name, value)


                                        class FrrlfaCandidateInterface(Entity):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, self).__init__()

                                                self.yang_name = "frrlfa-candidate-interface"
                                                self.yang_parent_name = "frrlfa-candidate-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.interface_name = YLeaf(YType.str, "interface-name")

                                                self.frr_type = YLeaf(YType.enumeration, "frr-type")

                                                self.level = YLeaf(YType.uint32, "level")
                                                self._segment_path = lambda: "frrlfa-candidate-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class FrrtilfaTypes(Entity):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrtilfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes, self).__init__()

                                            self.yang_name = "frrtilfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frrtilfa-type" : ("frrtilfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType)}

                                            self.frrtilfa_type = YList(self)
                                            self._segment_path = lambda: "frrtilfa-types"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes, [], name, value)


                                        class FrrtilfaType(Entity):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, self).__init__()

                                                self.yang_name = "frrtilfa-type"
                                                self.yang_parent_name = "frrtilfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")
                                                self._segment_path = lambda: "frrtilfa-type" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, ['level'], name, value)


                                    class InterfaceFrrTiebreakerDefaults(Entity):
                                        """
                                        Interface FRR Default tiebreaker
                                        configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker_default
                                        
                                        	Configure default tiebreaker
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreakerDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, self).__init__()

                                            self.yang_name = "interface-frr-tiebreaker-defaults"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"interface-frr-tiebreaker-default" : ("interface_frr_tiebreaker_default", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault)}

                                            self.interface_frr_tiebreaker_default = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreaker-defaults"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, [], name, value)


                                        class InterfaceFrrTiebreakerDefault(Entity):
                                            """
                                            Configure default tiebreaker
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker-default"
                                                self.yang_parent_name = "interface-frr-tiebreaker-defaults"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")
                                                self._segment_path = lambda: "interface-frr-tiebreaker-default" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, ['level'], name, value)


                                    class InterfaceFrrTiebreakers(Entity):
                                        """
                                        Interface FRR tiebreakers configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker
                                        
                                        	Configure tiebreaker for multiple backups
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers, self).__init__()

                                            self.yang_name = "interface-frr-tiebreakers"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"interface-frr-tiebreaker" : ("interface_frr_tiebreaker", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker)}

                                            self.interface_frr_tiebreaker = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreakers"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers, [], name, value)


                                        class InterfaceFrrTiebreaker(Entity):
                                            """
                                            Configure tiebreaker for multiple
                                            backups
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: tiebreaker  <key>
                                            
                                            	Tiebreaker for which configuration applies
                                            	**type**\:   :py:class:`IsisInterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceFrrTiebreaker>`
                                            
                                            .. attribute:: index
                                            
                                            	Preference order among tiebreakers
                                            	**type**\:  int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker"
                                                self.yang_parent_name = "interface-frr-tiebreakers"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.tiebreaker = YLeaf(YType.enumeration, "tiebreaker")

                                                self.index = YLeaf(YType.uint32, "index")
                                                self._segment_path = lambda: "interface-frr-tiebreaker" + "[level='" + self.level.get() + "']" + "[tiebreaker='" + self.tiebreaker.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                                class InterfaceLinkGroup(Entity):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\:  str
                                    
                                    	**length:** 1..40
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup, self).__init__()

                                        self.yang_name = "interface-link-group"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.level = YLeaf(YType.uint32, "level")

                                        self.link_group = YLeaf(YType.str, "link-group")
                                        self._segment_path = lambda: "interface-link-group"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.InterfaceLinkGroup, ['level', 'link_group'], name, value)


                                class ManualAdjSids(Entity):
                                    """
                                    Manual Adjacecy SID configuration
                                    
                                    .. attribute:: manual_adj_sid
                                    
                                    	Assign adjancency SID to an interface
                                    	**type**\: list of    :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids, self).__init__()

                                        self.yang_name = "manual-adj-sids"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"manual-adj-sid" : ("manual_adj_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid)}

                                        self.manual_adj_sid = YList(self)
                                        self._segment_path = lambda: "manual-adj-sids"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids, [], name, value)


                                    class ManualAdjSid(Entity):
                                        """
                                        Assign adjancency SID to an interface
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: sid_type  <key>
                                        
                                        	Sid type aboslute or index
                                        	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                        
                                        .. attribute:: sid  <key>
                                        
                                        	Sid value
                                        	**type**\:  int
                                        
                                        	**range:** 0..1048575
                                        
                                        .. attribute:: protected
                                        
                                        	Enable/Disable SID protection
                                        	**type**\:   :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid, self).__init__()

                                            self.yang_name = "manual-adj-sid"
                                            self.yang_parent_name = "manual-adj-sids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.sid_type = YLeaf(YType.enumeration, "sid-type")

                                            self.sid = YLeaf(YType.uint32, "sid")

                                            self.protected = YLeaf(YType.enumeration, "protected")
                                            self._segment_path = lambda: "manual-adj-sid" + "[level='" + self.level.get() + "']" + "[sid-type='" + self.sid_type.get() + "']" + "[sid='" + self.sid.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                                class Metrics(Entity):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics, self).__init__()

                                        self.yang_name = "metrics"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"metric" : ("metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric)}

                                        self.metric = YList(self)
                                        self._segment_path = lambda: "metrics"

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
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric>`
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric, self).__init__()

                                            self.yang_name = "metric"
                                            self.yang_parent_name = "metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.metric = YLeaf(YType.str, "metric")
                                            self._segment_path = lambda: "metric" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Metrics.Metric, ['level', 'metric'], name, value)

                                        class Metric(Enum):
                                            """
                                            Metric

                                            Allowed metric\: <1\-63> for narrow,

                                            <1\-16777215> for wide

                                            .. data:: maximum = 16777215

                                            	Maximum wide metric.  All routers will

                                            	exclude this link from their SPF

                                            """

                                            maximum = Enum.YLeaf(16777215, "maximum")



                                class MplsLdp(Entity):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp, self).__init__()

                                        self.yang_name = "mpls-ldp"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.sync_level = YLeaf(YType.uint32, "sync-level")
                                        self._segment_path = lambda: "mpls-ldp"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.MplsLdp, ['sync_level'], name, value)


                                class PrefixSid(Entity):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid, self).__init__()

                                        self.yang_name = "prefix-sid"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.explicit_null = YLeaf(YType.enumeration, "explicit-null")

                                        self.nflag_clear = YLeaf(YType.enumeration, "nflag-clear")

                                        self.php = YLeaf(YType.enumeration, "php")

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.value = YLeaf(YType.uint32, "value")
                                        self._segment_path = lambda: "prefix-sid"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSid, ['explicit_null', 'nflag_clear', 'php', 'type', 'value'], name, value)


                                class PrefixSspfsid(Entity):
                                    """
                                    Assign prefix SSPF SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid, self).__init__()

                                        self.yang_name = "prefix-sspfsid"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.explicit_null = YLeaf(YType.enumeration, "explicit-null")

                                        self.nflag_clear = YLeaf(YType.enumeration, "nflag-clear")

                                        self.php = YLeaf(YType.enumeration, "php")

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.value = YLeaf(YType.uint32, "value")
                                        self._segment_path = lambda: "prefix-sspfsid"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.PrefixSspfsid, ['explicit_null', 'nflag_clear', 'php', 'type', 'value'], name, value)


                                class Weights(Entity):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights, self).__init__()

                                        self.yang_name = "weights"
                                        self.yang_parent_name = "interface-af-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"weight" : ("weight", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight)}

                                        self.weight = YList(self)
                                        self._segment_path = lambda: "weights"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights, [], name, value)


                                    class Weight(Entity):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight, self).__init__()

                                            self.yang_name = "weight"
                                            self.yang_parent_name = "weights"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.weight = YLeaf(YType.uint32, "weight")
                                            self._segment_path = lambda: "weight" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.InterfaceAfData.Weights.Weight, ['level', 'weight'], name, value)


                            class TopologyName(Entity):
                                """
                                keys\: topology\-name
                                
                                .. attribute:: topology_name  <key>
                                
                                	Topology Name
                                	**type**\:  str
                                
                                	**length:** 1..32
                                
                                .. attribute:: admin_tags
                                
                                	admin\-tag configuration
                                	**type**\:   :py:class:`AdminTags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags>`
                                
                                .. attribute:: auto_metrics
                                
                                	AutoMetric configuration
                                	**type**\:   :py:class:`AutoMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics>`
                                
                                .. attribute:: interface_af_state
                                
                                	Interface state
                                	**type**\:   :py:class:`IsisInterfaceAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceAfState>`
                                
                                .. attribute:: interface_frr_table
                                
                                	Fast\-ReRoute configuration
                                	**type**\:   :py:class:`InterfaceFrrTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable>`
                                
                                .. attribute:: interface_link_group
                                
                                	Provide link group name and level
                                	**type**\:   :py:class:`InterfaceLinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: manual_adj_sids
                                
                                	Manual Adjacecy SID configuration
                                	**type**\:   :py:class:`ManualAdjSids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids>`
                                
                                .. attribute:: metrics
                                
                                	Metric configuration
                                	**type**\:   :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics>`
                                
                                .. attribute:: mpls_ldp
                                
                                	MPLS LDP configuration
                                	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp>`
                                
                                .. attribute:: prefix_sid
                                
                                	Assign prefix SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: prefix_sspfsid
                                
                                	Assign prefix SSPF SID to an interface, ISISPHPFlag will be rejected if set to disable, ISISEXPLICITNULLFlag will override the value of ISISPHPFlag
                                	**type**\:   :py:class:`PrefixSspfsid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: running
                                
                                	The presence of this object allows an address\-family to be run over the interface in question.This must be the first object created under the InterfaceAddressFamily container, and the last one deleted
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: weights
                                
                                	Weight configuration
                                	**type**\:   :py:class:`Weights <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights>`
                                
                                

                                """

                                _prefix = 'clns-isis-cfg'
                                _revision = '2017-06-02'

                                def __init__(self):
                                    super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName, self).__init__()

                                    self.yang_name = "topology-name"
                                    self.yang_parent_name = "interface-af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"admin-tags" : ("admin_tags", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags), "auto-metrics" : ("auto_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics), "interface-frr-table" : ("interface_frr_table", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable), "interface-link-group" : ("interface_link_group", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup), "manual-adj-sids" : ("manual_adj_sids", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids), "metrics" : ("metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics), "mpls-ldp" : ("mpls_ldp", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp), "prefix-sid" : ("prefix_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid), "prefix-sspfsid" : ("prefix_sspfsid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid), "weights" : ("weights", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights)}
                                    self._child_list_classes = {}

                                    self.topology_name = YLeaf(YType.str, "topology-name")

                                    self.interface_af_state = YLeaf(YType.enumeration, "interface-af-state")

                                    self.running = YLeaf(YType.empty, "running")

                                    self.admin_tags = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags()
                                    self.admin_tags.parent = self
                                    self._children_name_map["admin_tags"] = "admin-tags"
                                    self._children_yang_names.add("admin-tags")

                                    self.auto_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics()
                                    self.auto_metrics.parent = self
                                    self._children_name_map["auto_metrics"] = "auto-metrics"
                                    self._children_yang_names.add("auto-metrics")

                                    self.interface_frr_table = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable()
                                    self.interface_frr_table.parent = self
                                    self._children_name_map["interface_frr_table"] = "interface-frr-table"
                                    self._children_yang_names.add("interface-frr-table")

                                    self.interface_link_group = None
                                    self._children_name_map["interface_link_group"] = "interface-link-group"
                                    self._children_yang_names.add("interface-link-group")

                                    self.manual_adj_sids = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids()
                                    self.manual_adj_sids.parent = self
                                    self._children_name_map["manual_adj_sids"] = "manual-adj-sids"
                                    self._children_yang_names.add("manual-adj-sids")

                                    self.metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics()
                                    self.metrics.parent = self
                                    self._children_name_map["metrics"] = "metrics"
                                    self._children_yang_names.add("metrics")

                                    self.mpls_ldp = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp()
                                    self.mpls_ldp.parent = self
                                    self._children_name_map["mpls_ldp"] = "mpls-ldp"
                                    self._children_yang_names.add("mpls-ldp")

                                    self.prefix_sid = None
                                    self._children_name_map["prefix_sid"] = "prefix-sid"
                                    self._children_yang_names.add("prefix-sid")

                                    self.prefix_sspfsid = None
                                    self._children_name_map["prefix_sspfsid"] = "prefix-sspfsid"
                                    self._children_yang_names.add("prefix-sspfsid")

                                    self.weights = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights()
                                    self.weights.parent = self
                                    self._children_name_map["weights"] = "weights"
                                    self._children_yang_names.add("weights")
                                    self._segment_path = lambda: "topology-name" + "[topology-name='" + self.topology_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName, ['topology_name', 'interface_af_state', 'running'], name, value)


                                class AdminTags(Entity):
                                    """
                                    admin\-tag configuration
                                    
                                    .. attribute:: admin_tag
                                    
                                    	Admin tag for advertised interface connected routes
                                    	**type**\: list of    :py:class:`AdminTag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags, self).__init__()

                                        self.yang_name = "admin-tags"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"admin-tag" : ("admin_tag", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag)}

                                        self.admin_tag = YList(self)
                                        self._segment_path = lambda: "admin-tags"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags, [], name, value)


                                    class AdminTag(Entity):
                                        """
                                        Admin tag for advertised interface
                                        connected routes
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: admin_tag
                                        
                                        	Tag to associate with connected routes
                                        	**type**\:  int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag, self).__init__()

                                            self.yang_name = "admin-tag"
                                            self.yang_parent_name = "admin-tags"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.admin_tag = YLeaf(YType.uint32, "admin-tag")
                                            self._segment_path = lambda: "admin-tag" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AdminTags.AdminTag, ['level', 'admin_tag'], name, value)


                                class AutoMetrics(Entity):
                                    """
                                    AutoMetric configuration
                                    
                                    .. attribute:: auto_metric
                                    
                                    	AutoMetric Proactive\-Protect configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777214> is allowed as the auto\-metric value
                                    	**type**\: list of    :py:class:`AutoMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics, self).__init__()

                                        self.yang_name = "auto-metrics"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"auto-metric" : ("auto_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric)}

                                        self.auto_metric = YList(self)
                                        self._segment_path = lambda: "auto-metrics"

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
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: proactive_protect
                                        
                                        	Allowed auto metric\:<1\-63> for narrow ,<1\-16777214> for wide
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric, self).__init__()

                                            self.yang_name = "auto-metric"
                                            self.yang_parent_name = "auto-metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.proactive_protect = YLeaf(YType.uint32, "proactive-protect")
                                            self._segment_path = lambda: "auto-metric" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.AutoMetrics.AutoMetric, ['level', 'proactive_protect'], name, value)


                                class InterfaceFrrTable(Entity):
                                    """
                                    Fast\-ReRoute configuration
                                    
                                    .. attribute:: frr_exclude_interfaces
                                    
                                    	FRR exclusion configuration
                                    	**type**\:   :py:class:`FrrExcludeInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces>`
                                    
                                    .. attribute:: frr_remote_lfa_max_metrics
                                    
                                    	Remote LFA maxmimum metric
                                    	**type**\:   :py:class:`FrrRemoteLfaMaxMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics>`
                                    
                                    .. attribute:: frr_remote_lfa_types
                                    
                                    	Remote LFA Enable
                                    	**type**\:   :py:class:`FrrRemoteLfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes>`
                                    
                                    .. attribute:: frr_types
                                    
                                    	Type of FRR computation per level
                                    	**type**\:   :py:class:`FrrTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes>`
                                    
                                    .. attribute:: frrlfa_candidate_interfaces
                                    
                                    	FRR LFA candidate configuration
                                    	**type**\:   :py:class:`FrrlfaCandidateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces>`
                                    
                                    .. attribute:: frrtilfa_types
                                    
                                    	TI LFA Enable
                                    	**type**\:   :py:class:`FrrtilfaTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes>`
                                    
                                    .. attribute:: interface_frr_tiebreaker_defaults
                                    
                                    	Interface FRR Default tiebreaker configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakerDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults>`
                                    
                                    .. attribute:: interface_frr_tiebreakers
                                    
                                    	Interface FRR tiebreakers configuration
                                    	**type**\:   :py:class:`InterfaceFrrTiebreakers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable, self).__init__()

                                        self.yang_name = "interface-frr-table"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"frr-exclude-interfaces" : ("frr_exclude_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces), "frr-remote-lfa-max-metrics" : ("frr_remote_lfa_max_metrics", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics), "frr-remote-lfa-types" : ("frr_remote_lfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes), "frr-types" : ("frr_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes), "frrlfa-candidate-interfaces" : ("frrlfa_candidate_interfaces", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces), "frrtilfa-types" : ("frrtilfa_types", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes), "interface-frr-tiebreaker-defaults" : ("interface_frr_tiebreaker_defaults", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults), "interface-frr-tiebreakers" : ("interface_frr_tiebreakers", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers)}
                                        self._child_list_classes = {}

                                        self.frr_exclude_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces()
                                        self.frr_exclude_interfaces.parent = self
                                        self._children_name_map["frr_exclude_interfaces"] = "frr-exclude-interfaces"
                                        self._children_yang_names.add("frr-exclude-interfaces")

                                        self.frr_remote_lfa_max_metrics = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics()
                                        self.frr_remote_lfa_max_metrics.parent = self
                                        self._children_name_map["frr_remote_lfa_max_metrics"] = "frr-remote-lfa-max-metrics"
                                        self._children_yang_names.add("frr-remote-lfa-max-metrics")

                                        self.frr_remote_lfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes()
                                        self.frr_remote_lfa_types.parent = self
                                        self._children_name_map["frr_remote_lfa_types"] = "frr-remote-lfa-types"
                                        self._children_yang_names.add("frr-remote-lfa-types")

                                        self.frr_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes()
                                        self.frr_types.parent = self
                                        self._children_name_map["frr_types"] = "frr-types"
                                        self._children_yang_names.add("frr-types")

                                        self.frrlfa_candidate_interfaces = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces()
                                        self.frrlfa_candidate_interfaces.parent = self
                                        self._children_name_map["frrlfa_candidate_interfaces"] = "frrlfa-candidate-interfaces"
                                        self._children_yang_names.add("frrlfa-candidate-interfaces")

                                        self.frrtilfa_types = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes()
                                        self.frrtilfa_types.parent = self
                                        self._children_name_map["frrtilfa_types"] = "frrtilfa-types"
                                        self._children_yang_names.add("frrtilfa-types")

                                        self.interface_frr_tiebreaker_defaults = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults()
                                        self.interface_frr_tiebreaker_defaults.parent = self
                                        self._children_name_map["interface_frr_tiebreaker_defaults"] = "interface-frr-tiebreaker-defaults"
                                        self._children_yang_names.add("interface-frr-tiebreaker-defaults")

                                        self.interface_frr_tiebreakers = Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers()
                                        self.interface_frr_tiebreakers.parent = self
                                        self._children_name_map["interface_frr_tiebreakers"] = "interface-frr-tiebreakers"
                                        self._children_yang_names.add("interface-frr-tiebreakers")
                                        self._segment_path = lambda: "interface-frr-table"


                                    class FrrExcludeInterfaces(Entity):
                                        """
                                        FRR exclusion configuration
                                        
                                        .. attribute:: frr_exclude_interface
                                        
                                        	Exclude an interface from computation
                                        	**type**\: list of    :py:class:`FrrExcludeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces, self).__init__()

                                            self.yang_name = "frr-exclude-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-exclude-interface" : ("frr_exclude_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface)}

                                            self.frr_exclude_interface = YList(self)
                                            self._segment_path = lambda: "frr-exclude-interfaces"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces, [], name, value)


                                        class FrrExcludeInterface(Entity):
                                            """
                                            Exclude an interface from computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, self).__init__()

                                                self.yang_name = "frr-exclude-interface"
                                                self.yang_parent_name = "frr-exclude-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.interface_name = YLeaf(YType.str, "interface-name")

                                                self.frr_type = YLeaf(YType.enumeration, "frr-type")

                                                self.level = YLeaf(YType.uint32, "level")
                                                self._segment_path = lambda: "frr-exclude-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrExcludeInterfaces.FrrExcludeInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class FrrRemoteLfaMaxMetrics(Entity):
                                        """
                                        Remote LFA maxmimum metric
                                        
                                        .. attribute:: frr_remote_lfa_max_metric
                                        
                                        	Configure the maximum metric for selecting a remote LFA node
                                        	**type**\: list of    :py:class:`FrrRemoteLfaMaxMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, self).__init__()

                                            self.yang_name = "frr-remote-lfa-max-metrics"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-remote-lfa-max-metric" : ("frr_remote_lfa_max_metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric)}

                                            self.frr_remote_lfa_max_metric = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-max-metrics"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics, [], name, value)


                                        class FrrRemoteLfaMaxMetric(Entity):
                                            """
                                            Configure the maximum metric for
                                            selecting a remote LFA node
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: max_metric
                                            
                                            	Value of the metric
                                            	**type**\:  int
                                            
                                            	**range:** 1..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, self).__init__()

                                                self.yang_name = "frr-remote-lfa-max-metric"
                                                self.yang_parent_name = "frr-remote-lfa-max-metrics"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.max_metric = YLeaf(YType.uint32, "max-metric")
                                                self._segment_path = lambda: "frr-remote-lfa-max-metric" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaMaxMetrics.FrrRemoteLfaMaxMetric, ['level', 'max_metric'], name, value)


                                    class FrrRemoteLfaTypes(Entity):
                                        """
                                        Remote LFA Enable
                                        
                                        .. attribute:: frr_remote_lfa_type
                                        
                                        	Enable remote lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrRemoteLfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes, self).__init__()

                                            self.yang_name = "frr-remote-lfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-remote-lfa-type" : ("frr_remote_lfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType)}

                                            self.frr_remote_lfa_type = YList(self)
                                            self._segment_path = lambda: "frr-remote-lfa-types"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes, [], name, value)


                                        class FrrRemoteLfaType(Entity):
                                            """
                                            Enable remote lfa for a particular
                                            level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Remote LFA Type
                                            	**type**\:   :py:class:`IsisRemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisRemoteLfa>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, self).__init__()

                                                self.yang_name = "frr-remote-lfa-type"
                                                self.yang_parent_name = "frr-remote-lfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.type = YLeaf(YType.enumeration, "type")
                                                self._segment_path = lambda: "frr-remote-lfa-type" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrRemoteLfaTypes.FrrRemoteLfaType, ['level', 'type'], name, value)


                                    class FrrTypes(Entity):
                                        """
                                        Type of FRR computation per level
                                        
                                        .. attribute:: frr_type
                                        
                                        	Type of computation for prefixes reachable via interface
                                        	**type**\: list of    :py:class:`FrrType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes, self).__init__()

                                            self.yang_name = "frr-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frr-type" : ("frr_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType)}

                                            self.frr_type = YList(self)
                                            self._segment_path = lambda: "frr-types"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes, [], name, value)


                                        class FrrType(Entity):
                                            """
                                            Type of computation for prefixes
                                            reachable via interface
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: type
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType, self).__init__()

                                                self.yang_name = "frr-type"
                                                self.yang_parent_name = "frr-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.type = YLeaf(YType.enumeration, "type")
                                                self._segment_path = lambda: "frr-type" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrTypes.FrrType, ['level', 'type'], name, value)


                                    class FrrlfaCandidateInterfaces(Entity):
                                        """
                                        FRR LFA candidate configuration
                                        
                                        .. attribute:: frrlfa_candidate_interface
                                        
                                        	Include an interface to LFA candidate in computation
                                        	**type**\: list of    :py:class:`FrrlfaCandidateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces, self).__init__()

                                            self.yang_name = "frrlfa-candidate-interfaces"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frrlfa-candidate-interface" : ("frrlfa_candidate_interface", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface)}

                                            self.frrlfa_candidate_interface = YList(self)
                                            self._segment_path = lambda: "frrlfa-candidate-interfaces"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces, [], name, value)


                                        class FrrlfaCandidateInterface(Entity):
                                            """
                                            Include an interface to LFA candidate
                                            in computation
                                            
                                            .. attribute:: interface_name  <key>
                                            
                                            	Interface
                                            	**type**\:  str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                                            
                                            .. attribute:: frr_type  <key>
                                            
                                            	Computation Type
                                            	**type**\:   :py:class:`Isisfrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isisfrr>`
                                            
                                            .. attribute:: level
                                            
                                            	Level
                                            	**type**\:  int
                                            
                                            	**range:** 0..2
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, self).__init__()

                                                self.yang_name = "frrlfa-candidate-interface"
                                                self.yang_parent_name = "frrlfa-candidate-interfaces"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.interface_name = YLeaf(YType.str, "interface-name")

                                                self.frr_type = YLeaf(YType.enumeration, "frr-type")

                                                self.level = YLeaf(YType.uint32, "level")
                                                self._segment_path = lambda: "frrlfa-candidate-interface" + "[interface-name='" + self.interface_name.get() + "']" + "[frr-type='" + self.frr_type.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrlfaCandidateInterfaces.FrrlfaCandidateInterface, ['interface_name', 'frr_type', 'level'], name, value)


                                    class FrrtilfaTypes(Entity):
                                        """
                                        TI LFA Enable
                                        
                                        .. attribute:: frrtilfa_type
                                        
                                        	Enable TI lfa for a particular level
                                        	**type**\: list of    :py:class:`FrrtilfaType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes, self).__init__()

                                            self.yang_name = "frrtilfa-types"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"frrtilfa-type" : ("frrtilfa_type", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType)}

                                            self.frrtilfa_type = YList(self)
                                            self._segment_path = lambda: "frrtilfa-types"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes, [], name, value)


                                        class FrrtilfaType(Entity):
                                            """
                                            Enable TI lfa for a particular level
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, self).__init__()

                                                self.yang_name = "frrtilfa-type"
                                                self.yang_parent_name = "frrtilfa-types"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")
                                                self._segment_path = lambda: "frrtilfa-type" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.FrrtilfaTypes.FrrtilfaType, ['level'], name, value)


                                    class InterfaceFrrTiebreakerDefaults(Entity):
                                        """
                                        Interface FRR Default tiebreaker
                                        configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker_default
                                        
                                        	Configure default tiebreaker
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreakerDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, self).__init__()

                                            self.yang_name = "interface-frr-tiebreaker-defaults"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"interface-frr-tiebreaker-default" : ("interface_frr_tiebreaker_default", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault)}

                                            self.interface_frr_tiebreaker_default = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreaker-defaults"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults, [], name, value)


                                        class InterfaceFrrTiebreakerDefault(Entity):
                                            """
                                            Configure default tiebreaker
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker-default"
                                                self.yang_parent_name = "interface-frr-tiebreaker-defaults"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")
                                                self._segment_path = lambda: "interface-frr-tiebreaker-default" + "[level='" + self.level.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakerDefaults.InterfaceFrrTiebreakerDefault, ['level'], name, value)


                                    class InterfaceFrrTiebreakers(Entity):
                                        """
                                        Interface FRR tiebreakers configuration
                                        
                                        .. attribute:: interface_frr_tiebreaker
                                        
                                        	Configure tiebreaker for multiple backups
                                        	**type**\: list of    :py:class:`InterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker>`
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers, self).__init__()

                                            self.yang_name = "interface-frr-tiebreakers"
                                            self.yang_parent_name = "interface-frr-table"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"interface-frr-tiebreaker" : ("interface_frr_tiebreaker", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker)}

                                            self.interface_frr_tiebreaker = YList(self)
                                            self._segment_path = lambda: "interface-frr-tiebreakers"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers, [], name, value)


                                        class InterfaceFrrTiebreaker(Entity):
                                            """
                                            Configure tiebreaker for multiple
                                            backups
                                            
                                            .. attribute:: level  <key>
                                            
                                            	Level to which configuration applies
                                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                            
                                            .. attribute:: tiebreaker  <key>
                                            
                                            	Tiebreaker for which configuration applies
                                            	**type**\:   :py:class:`IsisInterfaceFrrTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisInterfaceFrrTiebreaker>`
                                            
                                            .. attribute:: index
                                            
                                            	Preference order among tiebreakers
                                            	**type**\:  int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'clns-isis-cfg'
                                            _revision = '2017-06-02'

                                            def __init__(self):
                                                super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, self).__init__()

                                                self.yang_name = "interface-frr-tiebreaker"
                                                self.yang_parent_name = "interface-frr-tiebreakers"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.level = YLeaf(YType.enumeration, "level")

                                                self.tiebreaker = YLeaf(YType.enumeration, "tiebreaker")

                                                self.index = YLeaf(YType.uint32, "index")
                                                self._segment_path = lambda: "interface-frr-tiebreaker" + "[level='" + self.level.get() + "']" + "[tiebreaker='" + self.tiebreaker.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceFrrTable.InterfaceFrrTiebreakers.InterfaceFrrTiebreaker, ['level', 'tiebreaker', 'index'], name, value)


                                class InterfaceLinkGroup(Entity):
                                    """
                                    Provide link group name and level
                                    
                                    .. attribute:: level
                                    
                                    	Level in which link group will be effective
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: link_group
                                    
                                    	Link Group
                                    	**type**\:  str
                                    
                                    	**length:** 1..40
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup, self).__init__()

                                        self.yang_name = "interface-link-group"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.level = YLeaf(YType.uint32, "level")

                                        self.link_group = YLeaf(YType.str, "link-group")
                                        self._segment_path = lambda: "interface-link-group"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.InterfaceLinkGroup, ['level', 'link_group'], name, value)


                                class ManualAdjSids(Entity):
                                    """
                                    Manual Adjacecy SID configuration
                                    
                                    .. attribute:: manual_adj_sid
                                    
                                    	Assign adjancency SID to an interface
                                    	**type**\: list of    :py:class:`ManualAdjSid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids, self).__init__()

                                        self.yang_name = "manual-adj-sids"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"manual-adj-sid" : ("manual_adj_sid", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid)}

                                        self.manual_adj_sid = YList(self)
                                        self._segment_path = lambda: "manual-adj-sids"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids, [], name, value)


                                    class ManualAdjSid(Entity):
                                        """
                                        Assign adjancency SID to an interface
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: sid_type  <key>
                                        
                                        	Sid type aboslute or index
                                        	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                        
                                        .. attribute:: sid  <key>
                                        
                                        	Sid value
                                        	**type**\:  int
                                        
                                        	**range:** 0..1048575
                                        
                                        .. attribute:: protected
                                        
                                        	Enable/Disable SID protection
                                        	**type**\:   :py:class:`IsissidProtected <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsissidProtected>`
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid, self).__init__()

                                            self.yang_name = "manual-adj-sid"
                                            self.yang_parent_name = "manual-adj-sids"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.sid_type = YLeaf(YType.enumeration, "sid-type")

                                            self.sid = YLeaf(YType.uint32, "sid")

                                            self.protected = YLeaf(YType.enumeration, "protected")
                                            self._segment_path = lambda: "manual-adj-sid" + "[level='" + self.level.get() + "']" + "[sid-type='" + self.sid_type.get() + "']" + "[sid='" + self.sid.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.ManualAdjSids.ManualAdjSid, ['level', 'sid_type', 'sid', 'protected'], name, value)


                                class Metrics(Entity):
                                    """
                                    Metric configuration
                                    
                                    .. attribute:: metric
                                    
                                    	Metric configuration. Legal value depends on the metric\-style specified for the topology. If the metric\-style defined is narrow, then only a value between <1\-63> is allowed and if the metric\-style is defined as wide, then a value between <1\-16777215> is allowed as the metric value.  All routers exclude links with the maximum wide metric (16777215) from their SPF
                                    	**type**\: list of    :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics, self).__init__()

                                        self.yang_name = "metrics"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"metric" : ("metric", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric)}

                                        self.metric = YList(self)
                                        self._segment_path = lambda: "metrics"

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
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: metric
                                        
                                        	Allowed metric\: <1\-63> for narrow, <1\-16777215> for wide
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric.Metric>`
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        
                                        ----
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric, self).__init__()

                                            self.yang_name = "metric"
                                            self.yang_parent_name = "metrics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.metric = YLeaf(YType.str, "metric")
                                            self._segment_path = lambda: "metric" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Metrics.Metric, ['level', 'metric'], name, value)

                                        class Metric(Enum):
                                            """
                                            Metric

                                            Allowed metric\: <1\-63> for narrow,

                                            <1\-16777215> for wide

                                            .. data:: maximum = 16777215

                                            	Maximum wide metric.  All routers will

                                            	exclude this link from their SPF

                                            """

                                            maximum = Enum.YLeaf(16777215, "maximum")



                                class MplsLdp(Entity):
                                    """
                                    MPLS LDP configuration
                                    
                                    .. attribute:: sync_level
                                    
                                    	Enable MPLS LDP Synchronization for an IS\-IS level
                                    	**type**\:  int
                                    
                                    	**range:** 0..2
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp, self).__init__()

                                        self.yang_name = "mpls-ldp"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.sync_level = YLeaf(YType.uint32, "sync-level")
                                        self._segment_path = lambda: "mpls-ldp"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.MplsLdp, ['sync_level'], name, value)


                                class PrefixSid(Entity):
                                    """
                                    Assign prefix SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid, self).__init__()

                                        self.yang_name = "prefix-sid"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.explicit_null = YLeaf(YType.enumeration, "explicit-null")

                                        self.nflag_clear = YLeaf(YType.enumeration, "nflag-clear")

                                        self.php = YLeaf(YType.enumeration, "php")

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.value = YLeaf(YType.uint32, "value")
                                        self._segment_path = lambda: "prefix-sid"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSid, ['explicit_null', 'nflag_clear', 'php', 'type', 'value'], name, value)


                                class PrefixSspfsid(Entity):
                                    """
                                    Assign prefix SSPF SID to an interface,
                                    ISISPHPFlag will be rejected if set to
                                    disable, ISISEXPLICITNULLFlag will
                                    override the value of ISISPHPFlag
                                    
                                    .. attribute:: explicit_null
                                    
                                    	Enable/Disable Explicit\-NULL flag
                                    	**type**\:   :py:class:`IsisexplicitNullFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisexplicitNullFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: nflag_clear
                                    
                                    	Clear N\-flag for the prefix\-SID
                                    	**type**\:   :py:class:`NflagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.NflagClear>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: php
                                    
                                    	Enable/Disable Penultimate Hop Popping
                                    	**type**\:   :py:class:`IsisphpFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisphpFlag>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: type
                                    
                                    	SID type for the interface
                                    	**type**\:   :py:class:`Isissid1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isissid1>`
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: value
                                    
                                    	SID value for the interface
                                    	**type**\:  int
                                    
                                    	**range:** 0..1048575
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid, self).__init__()

                                        self.yang_name = "prefix-sspfsid"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}
                                        self.is_presence_container = True

                                        self.explicit_null = YLeaf(YType.enumeration, "explicit-null")

                                        self.nflag_clear = YLeaf(YType.enumeration, "nflag-clear")

                                        self.php = YLeaf(YType.enumeration, "php")

                                        self.type = YLeaf(YType.enumeration, "type")

                                        self.value = YLeaf(YType.uint32, "value")
                                        self._segment_path = lambda: "prefix-sspfsid"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.PrefixSspfsid, ['explicit_null', 'nflag_clear', 'php', 'type', 'value'], name, value)


                                class Weights(Entity):
                                    """
                                    Weight configuration
                                    
                                    .. attribute:: weight
                                    
                                    	Weight configuration under interface for load balancing
                                    	**type**\: list of    :py:class:`Weight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight>`
                                    
                                    

                                    """

                                    _prefix = 'clns-isis-cfg'
                                    _revision = '2017-06-02'

                                    def __init__(self):
                                        super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights, self).__init__()

                                        self.yang_name = "weights"
                                        self.yang_parent_name = "topology-name"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"weight" : ("weight", Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight)}

                                        self.weight = YList(self)
                                        self._segment_path = lambda: "weights"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights, [], name, value)


                                    class Weight(Entity):
                                        """
                                        Weight configuration under interface for load
                                        balancing
                                        
                                        .. attribute:: level  <key>
                                        
                                        	Level to which configuration applies
                                        	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                                        
                                        .. attribute:: weight
                                        
                                        	Weight to be configured under interface for Load Balancing. Allowed weight\: <1\-16777215>
                                        	**type**\:  int
                                        
                                        	**range:** 1..16777214
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'clns-isis-cfg'
                                        _revision = '2017-06-02'

                                        def __init__(self):
                                            super(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight, self).__init__()

                                            self.yang_name = "weight"
                                            self.yang_parent_name = "weights"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.level = YLeaf(YType.enumeration, "level")

                                            self.weight = YLeaf(YType.uint32, "weight")
                                            self._segment_path = lambda: "weight" + "[level='" + self.level.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.InterfaceAfs.InterfaceAf.TopologyName.Weights.Weight, ['level', 'weight'], name, value)


                    class LspFastFloodThresholds(Entity):
                        """
                        LSP fast flood threshold configuration
                        
                        .. attribute:: lsp_fast_flood_threshold
                        
                        	Number of LSPs to send back to back on an interface
                        	**type**\: list of    :py:class:`LspFastFloodThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds, self).__init__()

                            self.yang_name = "lsp-fast-flood-thresholds"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lsp-fast-flood-threshold" : ("lsp_fast_flood_threshold", Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold)}

                            self.lsp_fast_flood_threshold = YList(self)
                            self._segment_path = lambda: "lsp-fast-flood-thresholds"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds, [], name, value)


                        class LspFastFloodThreshold(Entity):
                            """
                            Number of LSPs to send back to back on an
                            interface.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: count
                            
                            	Count
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold, self).__init__()

                                self.yang_name = "lsp-fast-flood-threshold"
                                self.yang_parent_name = "lsp-fast-flood-thresholds"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.count = YLeaf(YType.uint32, "count")
                                self._segment_path = lambda: "lsp-fast-flood-threshold" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspFastFloodThresholds.LspFastFloodThreshold, ['level', 'count'], name, value)


                    class LspIntervals(Entity):
                        """
                        LSP\-interval configuration
                        
                        .. attribute:: lsp_interval
                        
                        	Interval between transmission of LSPs on interface
                        	**type**\: list of    :py:class:`LspInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspIntervals, self).__init__()

                            self.yang_name = "lsp-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lsp-interval" : ("lsp_interval", Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval)}

                            self.lsp_interval = YList(self)
                            self._segment_path = lambda: "lsp-intervals"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspIntervals, [], name, value)


                        class LspInterval(Entity):
                            """
                            Interval between transmission of LSPs on
                            interface.
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval, self).__init__()

                                self.yang_name = "lsp-interval"
                                self.yang_parent_name = "lsp-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.interval = YLeaf(YType.uint32, "interval")
                                self._segment_path = lambda: "lsp-interval" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspIntervals.LspInterval, ['level', 'interval'], name, value)


                    class LspRetransmitIntervals(Entity):
                        """
                        LSP\-retransmission\-interval configuration
                        
                        .. attribute:: lsp_retransmit_interval
                        
                        	Interval between retransmissions of the same LSP
                        	**type**\: list of    :py:class:`LspRetransmitInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals, self).__init__()

                            self.yang_name = "lsp-retransmit-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lsp-retransmit-interval" : ("lsp_retransmit_interval", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval)}

                            self.lsp_retransmit_interval = YList(self)
                            self._segment_path = lambda: "lsp-retransmit-intervals"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals, [], name, value)


                        class LspRetransmitInterval(Entity):
                            """
                            Interval between retransmissions of the
                            same LSP
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Seconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval, self).__init__()

                                self.yang_name = "lsp-retransmit-interval"
                                self.yang_parent_name = "lsp-retransmit-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.interval = YLeaf(YType.uint32, "interval")
                                self._segment_path = lambda: "lsp-retransmit-interval" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitIntervals.LspRetransmitInterval, ['level', 'interval'], name, value)


                    class LspRetransmitThrottleIntervals(Entity):
                        """
                        LSP\-retransmission\-throttle\-interval
                        configuration
                        
                        .. attribute:: lsp_retransmit_throttle_interval
                        
                        	Minimum interval betwen retransissions of different LSPs
                        	**type**\: list of    :py:class:`LspRetransmitThrottleInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals, self).__init__()

                            self.yang_name = "lsp-retransmit-throttle-intervals"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"lsp-retransmit-throttle-interval" : ("lsp_retransmit_throttle_interval", Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval)}

                            self.lsp_retransmit_throttle_interval = YList(self)
                            self._segment_path = lambda: "lsp-retransmit-throttle-intervals"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals, [], name, value)


                        class LspRetransmitThrottleInterval(Entity):
                            """
                            Minimum interval betwen retransissions of
                            different LSPs
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: interval
                            
                            	Milliseconds
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval, self).__init__()

                                self.yang_name = "lsp-retransmit-throttle-interval"
                                self.yang_parent_name = "lsp-retransmit-throttle-intervals"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.interval = YLeaf(YType.uint32, "interval")
                                self._segment_path = lambda: "lsp-retransmit-throttle-interval" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.LspRetransmitThrottleIntervals.LspRetransmitThrottleInterval, ['level', 'interval'], name, value)


                    class PrefixAttributeNFlagClears(Entity):
                        """
                        Prefix attribute N flag clear configuration
                        
                        .. attribute:: prefix_attribute_n_flag_clear
                        
                        	Clear the N flag in prefix attribute flags sub\-TLV
                        	**type**\: list of    :py:class:`PrefixAttributeNFlagClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears, self).__init__()

                            self.yang_name = "prefix-attribute-n-flag-clears"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"prefix-attribute-n-flag-clear" : ("prefix_attribute_n_flag_clear", Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear)}

                            self.prefix_attribute_n_flag_clear = YList(self)
                            self._segment_path = lambda: "prefix-attribute-n-flag-clears"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears, [], name, value)


                        class PrefixAttributeNFlagClear(Entity):
                            """
                            Clear the N flag in prefix attribute flags
                            sub\-TLV
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear, self).__init__()

                                self.yang_name = "prefix-attribute-n-flag-clear"
                                self.yang_parent_name = "prefix-attribute-n-flag-clears"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")
                                self._segment_path = lambda: "prefix-attribute-n-flag-clear" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.PrefixAttributeNFlagClears.PrefixAttributeNFlagClear, ['level'], name, value)


                    class Priorities(Entity):
                        """
                        DIS\-election priority configuration
                        
                        .. attribute:: priority
                        
                        	DIS\-election priority
                        	**type**\: list of    :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority>`
                        
                        

                        """

                        _prefix = 'clns-isis-cfg'
                        _revision = '2017-06-02'

                        def __init__(self):
                            super(Isis.Instances.Instance.Interfaces.Interface.Priorities, self).__init__()

                            self.yang_name = "priorities"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"priority" : ("priority", Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority)}

                            self.priority = YList(self)
                            self._segment_path = lambda: "priorities"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.Priorities, [], name, value)


                        class Priority(Entity):
                            """
                            DIS\-election priority
                            
                            .. attribute:: level  <key>
                            
                            	Level to which configuration applies
                            	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                            
                            .. attribute:: priority_value
                            
                            	Priority
                            	**type**\:  int
                            
                            	**range:** 0..127
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'clns-isis-cfg'
                            _revision = '2017-06-02'

                            def __init__(self):
                                super(Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority, self).__init__()

                                self.yang_name = "priority"
                                self.yang_parent_name = "priorities"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.level = YLeaf(YType.enumeration, "level")

                                self.priority_value = YLeaf(YType.uint32, "priority-value")
                                self._segment_path = lambda: "priority" + "[level='" + self.level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Isis.Instances.Instance.Interfaces.Interface.Priorities.Priority, ['level', 'priority_value'], name, value)


            class LinkGroups(Entity):
                """
                Link Group
                
                .. attribute:: link_group
                
                	Configuration for link group name
                	**type**\: list of    :py:class:`LinkGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LinkGroups.LinkGroup>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LinkGroups, self).__init__()

                    self.yang_name = "link-groups"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"link-group" : ("link_group", Isis.Instances.Instance.LinkGroups.LinkGroup)}

                    self.link_group = YList(self)
                    self._segment_path = lambda: "link-groups"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LinkGroups, [], name, value)


                class LinkGroup(Entity):
                    """
                    Configuration for link group name
                    
                    .. attribute:: link_group_name  <key>
                    
                    	Link Group Name
                    	**type**\:  str
                    
                    	**length:** 1..40
                    
                    .. attribute:: enable
                    
                    	Flag to indicate that linkgroup should be running.  This must be the first object created when a linkgroup is configured, and the last object deleted when it is deconfigured.  When this object is deleted, the IS\-IS linkgroup will be removed
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: metric_offset
                    
                    	Metric for redistributed routes\: <0\-63> for narrow, <0\-16777215> for wide
                    	**type**\:  int
                    
                    	**range:** 0..16777215
                    
                    .. attribute:: minimum_members
                    
                    	Minimum Members
                    	**type**\:  int
                    
                    	**range:** 2..64
                    
                    	**default value**\: 2
                    
                    .. attribute:: revert_members
                    
                    	Revert Members
                    	**type**\:  int
                    
                    	**range:** 2..64
                    
                    	**default value**\: 2
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LinkGroups.LinkGroup, self).__init__()

                        self.yang_name = "link-group"
                        self.yang_parent_name = "link-groups"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.link_group_name = YLeaf(YType.str, "link-group-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.metric_offset = YLeaf(YType.uint32, "metric-offset")

                        self.minimum_members = YLeaf(YType.uint32, "minimum-members")

                        self.revert_members = YLeaf(YType.uint32, "revert-members")
                        self._segment_path = lambda: "link-group" + "[link-group-name='" + self.link_group_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LinkGroups.LinkGroup, ['link_group_name', 'enable', 'metric_offset', 'minimum_members', 'revert_members'], name, value)


            class LspAcceptPasswords(Entity):
                """
                LSP/SNP accept password configuration
                
                .. attribute:: lsp_accept_password
                
                	LSP/SNP accept passwords. This requires the existence of an LSPPassword of the same level 
                	**type**\: list of    :py:class:`LspAcceptPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspAcceptPasswords, self).__init__()

                    self.yang_name = "lsp-accept-passwords"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-accept-password" : ("lsp_accept_password", Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword)}

                    self.lsp_accept_password = YList(self)
                    self._segment_path = lambda: "lsp-accept-passwords"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspAcceptPasswords, [], name, value)


                class LspAcceptPassword(Entity):
                    """
                    LSP/SNP accept passwords. This requires the
                    existence of an LSPPassword of the same level
                    .
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: password
                    
                    	Password
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword, self).__init__()

                        self.yang_name = "lsp-accept-password"
                        self.yang_parent_name = "lsp-accept-passwords"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.password = YLeaf(YType.str, "password")
                        self._segment_path = lambda: "lsp-accept-password" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspAcceptPasswords.LspAcceptPassword, ['level', 'password'], name, value)


            class LspArrivalTimes(Entity):
                """
                LSP arrival time configuration
                
                .. attribute:: lsp_arrival_time
                
                	Minimum LSP arrival time
                	**type**\: list of    :py:class:`LspArrivalTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspArrivalTimes, self).__init__()

                    self.yang_name = "lsp-arrival-times"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-arrival-time" : ("lsp_arrival_time", Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime)}

                    self.lsp_arrival_time = YList(self)
                    self._segment_path = lambda: "lsp-arrival-times"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspArrivalTimes, [], name, value)


                class LspArrivalTime(Entity):
                    """
                    Minimum LSP arrival time
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: initial_wait
                    
                    	Initial delay expected to take since last LSPin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum delay expected to take since last LSPin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary delay expected to take since last LSPin milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime, self).__init__()

                        self.yang_name = "lsp-arrival-time"
                        self.yang_parent_name = "lsp-arrival-times"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.initial_wait = YLeaf(YType.uint32, "initial-wait")

                        self.maximum_wait = YLeaf(YType.uint32, "maximum-wait")

                        self.secondary_wait = YLeaf(YType.uint32, "secondary-wait")
                        self._segment_path = lambda: "lsp-arrival-time" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspArrivalTimes.LspArrivalTime, ['level', 'initial_wait', 'maximum_wait', 'secondary_wait'], name, value)


            class LspCheckIntervals(Entity):
                """
                LSP checksum check interval configuration
                
                .. attribute:: lsp_check_interval
                
                	LSP checksum check interval parameters
                	**type**\: list of    :py:class:`LspCheckInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspCheckIntervals, self).__init__()

                    self.yang_name = "lsp-check-intervals"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-check-interval" : ("lsp_check_interval", Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval)}

                    self.lsp_check_interval = YList(self)
                    self._segment_path = lambda: "lsp-check-intervals"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspCheckIntervals, [], name, value)


                class LspCheckInterval(Entity):
                    """
                    LSP checksum check interval parameters
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: interval
                    
                    	LSP checksum check interval time in seconds
                    	**type**\:  int
                    
                    	**range:** 10..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval, self).__init__()

                        self.yang_name = "lsp-check-interval"
                        self.yang_parent_name = "lsp-check-intervals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.interval = YLeaf(YType.uint32, "interval")
                        self._segment_path = lambda: "lsp-check-interval" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspCheckIntervals.LspCheckInterval, ['level', 'interval'], name, value)


            class LspGenerationIntervals(Entity):
                """
                LSP generation\-interval configuration
                
                .. attribute:: lsp_generation_interval
                
                	LSP generation scheduling parameters
                	**type**\: list of    :py:class:`LspGenerationInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspGenerationIntervals, self).__init__()

                    self.yang_name = "lsp-generation-intervals"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-generation-interval" : ("lsp_generation_interval", Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval)}

                    self.lsp_generation_interval = YList(self)
                    self._segment_path = lambda: "lsp-generation-intervals"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspGenerationIntervals, [], name, value)


                class LspGenerationInterval(Entity):
                    """
                    LSP generation scheduling parameters
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: initial_wait
                    
                    	Initial wait before generating local LSP in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: maximum_wait
                    
                    	Maximum wait before generating local LSP in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    .. attribute:: secondary_wait
                    
                    	Secondary wait before generating local LSP in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..120000
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval, self).__init__()

                        self.yang_name = "lsp-generation-interval"
                        self.yang_parent_name = "lsp-generation-intervals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.initial_wait = YLeaf(YType.uint32, "initial-wait")

                        self.maximum_wait = YLeaf(YType.uint32, "maximum-wait")

                        self.secondary_wait = YLeaf(YType.uint32, "secondary-wait")
                        self._segment_path = lambda: "lsp-generation-interval" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspGenerationIntervals.LspGenerationInterval, ['level', 'initial_wait', 'maximum_wait', 'secondary_wait'], name, value)


            class LspLifetimes(Entity):
                """
                LSP lifetime configuration
                
                .. attribute:: lsp_lifetime
                
                	Maximum LSP lifetime
                	**type**\: list of    :py:class:`LspLifetime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspLifetimes.LspLifetime>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspLifetimes, self).__init__()

                    self.yang_name = "lsp-lifetimes"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-lifetime" : ("lsp_lifetime", Isis.Instances.Instance.LspLifetimes.LspLifetime)}

                    self.lsp_lifetime = YList(self)
                    self._segment_path = lambda: "lsp-lifetimes"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspLifetimes, [], name, value)


                class LspLifetime(Entity):
                    """
                    Maximum LSP lifetime
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: lifetime
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspLifetimes.LspLifetime, self).__init__()

                        self.yang_name = "lsp-lifetime"
                        self.yang_parent_name = "lsp-lifetimes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.lifetime = YLeaf(YType.uint32, "lifetime")
                        self._segment_path = lambda: "lsp-lifetime" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspLifetimes.LspLifetime, ['level', 'lifetime'], name, value)


            class LspMtus(Entity):
                """
                LSP MTU configuration
                
                .. attribute:: lsp_mtu
                
                	LSP MTU
                	**type**\: list of    :py:class:`LspMtu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspMtus.LspMtu>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspMtus, self).__init__()

                    self.yang_name = "lsp-mtus"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-mtu" : ("lsp_mtu", Isis.Instances.Instance.LspMtus.LspMtu)}

                    self.lsp_mtu = YList(self)
                    self._segment_path = lambda: "lsp-mtus"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspMtus, [], name, value)


                class LspMtu(Entity):
                    """
                    LSP MTU
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: mtu
                    
                    	Bytes
                    	**type**\:  int
                    
                    	**range:** 128..4352
                    
                    	**mandatory**\: True
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspMtus.LspMtu, self).__init__()

                        self.yang_name = "lsp-mtu"
                        self.yang_parent_name = "lsp-mtus"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.mtu = YLeaf(YType.uint32, "mtu")
                        self._segment_path = lambda: "lsp-mtu" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspMtus.LspMtu, ['level', 'mtu'], name, value)


            class LspPasswords(Entity):
                """
                LSP/SNP password configuration
                
                .. attribute:: lsp_password
                
                	LSP/SNP passwords. This must exist if an LSPAcceptPassword of the same level exists
                	**type**\: list of    :py:class:`LspPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspPasswords.LspPassword>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspPasswords, self).__init__()

                    self.yang_name = "lsp-passwords"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-password" : ("lsp_password", Isis.Instances.Instance.LspPasswords.LspPassword)}

                    self.lsp_password = YList(self)
                    self._segment_path = lambda: "lsp-passwords"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspPasswords, [], name, value)


                class LspPassword(Entity):
                    """
                    LSP/SNP passwords. This must exist if an
                    LSPAcceptPassword of the same level exists.
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: algorithm
                    
                    	Algorithm
                    	**type**\:   :py:class:`IsisAuthenticationAlgorithm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationAlgorithm>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: authentication_type
                    
                    	SNP packet authentication mode
                    	**type**\:   :py:class:`IsisSnpAuth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisSnpAuth>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: failure_mode
                    
                    	Failure Mode
                    	**type**\:   :py:class:`IsisAuthenticationFailureMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAuthenticationFailureMode>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: password
                    
                    	Password or unencrypted Key Chain name
                    	**type**\:  str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspPasswords.LspPassword, self).__init__()

                        self.yang_name = "lsp-password"
                        self.yang_parent_name = "lsp-passwords"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.algorithm = YLeaf(YType.enumeration, "algorithm")

                        self.authentication_type = YLeaf(YType.enumeration, "authentication-type")

                        self.failure_mode = YLeaf(YType.enumeration, "failure-mode")

                        self.password = YLeaf(YType.str, "password")
                        self._segment_path = lambda: "lsp-password" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspPasswords.LspPassword, ['level', 'algorithm', 'authentication_type', 'failure_mode', 'password'], name, value)


            class LspRefreshIntervals(Entity):
                """
                LSP refresh\-interval configuration
                
                .. attribute:: lsp_refresh_interval
                
                	Interval between re\-flooding of unchanged LSPs
                	**type**\: list of    :py:class:`LspRefreshInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.LspRefreshIntervals, self).__init__()

                    self.yang_name = "lsp-refresh-intervals"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"lsp-refresh-interval" : ("lsp_refresh_interval", Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval)}

                    self.lsp_refresh_interval = YList(self)
                    self._segment_path = lambda: "lsp-refresh-intervals"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.LspRefreshIntervals, [], name, value)


                class LspRefreshInterval(Entity):
                    """
                    Interval between re\-flooding of unchanged
                    LSPs
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: interval
                    
                    	Seconds
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval, self).__init__()

                        self.yang_name = "lsp-refresh-interval"
                        self.yang_parent_name = "lsp-refresh-intervals"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.interval = YLeaf(YType.uint32, "interval")
                        self._segment_path = lambda: "lsp-refresh-interval" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.LspRefreshIntervals.LspRefreshInterval, ['level', 'interval'], name, value)


            class MaxLinkMetrics(Entity):
                """
                Max Link Metric configuration
                
                .. attribute:: max_link_metric
                
                	Max Link Metric
                	**type**\: list of    :py:class:`MaxLinkMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.MaxLinkMetrics, self).__init__()

                    self.yang_name = "max-link-metrics"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"max-link-metric" : ("max_link_metric", Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric)}

                    self.max_link_metric = YList(self)
                    self._segment_path = lambda: "max-link-metrics"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.MaxLinkMetrics, [], name, value)


                class MaxLinkMetric(Entity):
                    """
                    Max Link Metric
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric, self).__init__()

                        self.yang_name = "max-link-metric"
                        self.yang_parent_name = "max-link-metrics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")
                        self._segment_path = lambda: "max-link-metric" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.MaxLinkMetrics.MaxLinkMetric, ['level'], name, value)


            class Nets(Entity):
                """
                NET configuration
                
                .. attribute:: net
                
                	Network Entity Title (NET)
                	**type**\: list of    :py:class:`Net <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.Nets.Net>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.Nets, self).__init__()

                    self.yang_name = "nets"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"net" : ("net", Isis.Instances.Instance.Nets.Net)}

                    self.net = YList(self)
                    self._segment_path = lambda: "nets"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Nets, [], name, value)


                class Net(Entity):
                    """
                    Network Entity Title (NET)
                    
                    .. attribute:: net_name  <key>
                    
                    	Network Entity Title
                    	**type**\:  str
                    
                    	**pattern:** [a\-fA\-F0\-9]{2}(\\.[a\-fA\-F0\-9]{4}){3,9}\\.[a\-fA\-F0\-9]{2}
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.Nets.Net, self).__init__()

                        self.yang_name = "net"
                        self.yang_parent_name = "nets"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.net_name = YLeaf(YType.str, "net-name")
                        self._segment_path = lambda: "net" + "[net-name='" + self.net_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.Nets.Net, ['net_name'], name, value)


            class Nsf(Entity):
                """
                IS\-IS NSF configuration
                
                .. attribute:: flavor
                
                	NSF not configured if item is deleted
                	**type**\:   :py:class:`IsisNsfFlavor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisNsfFlavor>`
                
                .. attribute:: interface_timer
                
                	Per\-interface time period to wait for a restart ACK during an IETF\-NSF restart. This configuration has no effect if IETF\-NSF is not configured
                	**type**\:  int
                
                	**range:** 1..20
                
                	**units**\: second
                
                	**default value**\: 1
                
                .. attribute:: lifetime
                
                	Maximum route lifetime following restart. When this lifetime expires, old routes will be purged from the RIB
                	**type**\:  int
                
                	**range:** 5..300
                
                	**units**\: second
                
                	**default value**\: 90
                
                .. attribute:: max_interface_timer_expiry
                
                	Maximum number of times an interface timer may expire during an IETF\-NSF restart before the NSF restart is aborted. This configuration has no effect if IETF NSF is not configured
                	**type**\:  int
                
                	**range:** 1..10
                
                	**default value**\: 10
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.Nsf, self).__init__()

                    self.yang_name = "nsf"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.flavor = YLeaf(YType.enumeration, "flavor")

                    self.interface_timer = YLeaf(YType.uint32, "interface-timer")

                    self.lifetime = YLeaf(YType.uint32, "lifetime")

                    self.max_interface_timer_expiry = YLeaf(YType.uint32, "max-interface-timer-expiry")
                    self._segment_path = lambda: "nsf"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Nsf, ['flavor', 'interface_timer', 'lifetime', 'max_interface_timer_expiry'], name, value)


            class OverloadBits(Entity):
                """
                LSP overload\-bit configuration
                
                .. attribute:: overload_bit
                
                	Set the overload bit in the System LSP so that other routers avoid this one in SPF calculations. This may be done either unconditionally, or on startup until either a set time has passed or IS\-IS is informed that BGP has converged. This is an Object with a union discriminated on an integer value of the ISISOverloadBitModeType
                	**type**\: list of    :py:class:`OverloadBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.Isis.Instances.Instance.OverloadBits.OverloadBit>`
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.OverloadBits, self).__init__()

                    self.yang_name = "overload-bits"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"overload-bit" : ("overload_bit", Isis.Instances.Instance.OverloadBits.OverloadBit)}

                    self.overload_bit = YList(self)
                    self._segment_path = lambda: "overload-bits"

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
                    
                    .. attribute:: level  <key>
                    
                    	Level to which configuration applies
                    	**type**\:   :py:class:`IsisInternalLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes.IsisInternalLevel>`
                    
                    .. attribute:: external_adv_type
                    
                    	Advertise prefixes from other protocols
                    	**type**\:   :py:class:`IsisAdvTypeExternal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeExternal>`
                    
                    .. attribute:: hippity_period
                    
                    	Time in seconds to advertise ourself as overloaded after process startup
                    	**type**\:  int
                    
                    	**range:** 5..86400
                    
                    	**units**\: second
                    
                    .. attribute:: inter_level_adv_type
                    
                    	Advertise prefixes across ISIS levels
                    	**type**\:   :py:class:`IsisAdvTypeInterLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisAdvTypeInterLevel>`
                    
                    .. attribute:: overload_bit_mode
                    
                    	Circumstances under which the overload bit is set in the system LSP
                    	**type**\:   :py:class:`IsisOverloadBitMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg.IsisOverloadBitMode>`
                    
                    

                    """

                    _prefix = 'clns-isis-cfg'
                    _revision = '2017-06-02'

                    def __init__(self):
                        super(Isis.Instances.Instance.OverloadBits.OverloadBit, self).__init__()

                        self.yang_name = "overload-bit"
                        self.yang_parent_name = "overload-bits"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.level = YLeaf(YType.enumeration, "level")

                        self.external_adv_type = YLeaf(YType.enumeration, "external-adv-type")

                        self.hippity_period = YLeaf(YType.uint32, "hippity-period")

                        self.inter_level_adv_type = YLeaf(YType.enumeration, "inter-level-adv-type")

                        self.overload_bit_mode = YLeaf(YType.enumeration, "overload-bit-mode")
                        self._segment_path = lambda: "overload-bit" + "[level='" + self.level.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Isis.Instances.Instance.OverloadBits.OverloadBit, ['level', 'external_adv_type', 'hippity_period', 'inter_level_adv_type', 'overload_bit_mode'], name, value)


            class Srgb(Entity):
                """
                Segment Routing Global Block configuration
                
                .. attribute:: lower_bound
                
                	The lower bound of the SRGB
                	**type**\:  int
                
                	**range:** 16000..1048574
                
                	**mandatory**\: True
                
                .. attribute:: upper_bound
                
                	The upper bound of the SRGB
                	**type**\:  int
                
                	**range:** 16001..1048575
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.Srgb, self).__init__()

                    self.yang_name = "srgb"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.lower_bound = YLeaf(YType.uint32, "lower-bound")

                    self.upper_bound = YLeaf(YType.uint32, "upper-bound")
                    self._segment_path = lambda: "srgb"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.Srgb, ['lower_bound', 'upper_bound'], name, value)


            class TraceBufferSize(Entity):
                """
                Trace buffer size configuration
                
                .. attribute:: detailed
                
                	Buffer size for detailed traces
                	**type**\:  int
                
                	**range:** 1..1000000
                
                .. attribute:: hello
                
                	Buffer size for hello trace
                	**type**\:  int
                
                	**range:** 1..1000000
                
                .. attribute:: severe
                
                	Buffer size for severe trace
                	**type**\:  int
                
                	**range:** 1..1000000
                
                .. attribute:: standard
                
                	Buffer size for standard traces
                	**type**\:  int
                
                	**range:** 1..1000000
                
                

                """

                _prefix = 'clns-isis-cfg'
                _revision = '2017-06-02'

                def __init__(self):
                    super(Isis.Instances.Instance.TraceBufferSize, self).__init__()

                    self.yang_name = "trace-buffer-size"
                    self.yang_parent_name = "instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.detailed = YLeaf(YType.uint32, "detailed")

                    self.hello = YLeaf(YType.uint32, "hello")

                    self.severe = YLeaf(YType.uint32, "severe")

                    self.standard = YLeaf(YType.uint32, "standard")
                    self._segment_path = lambda: "trace-buffer-size"

                def __setattr__(self, name, value):
                    self._perform_setattr(Isis.Instances.Instance.TraceBufferSize, ['detailed', 'hello', 'severe', 'standard'], name, value)

    def clone_ptr(self):
        self._top_entity = Isis()
        return self._top_entity

