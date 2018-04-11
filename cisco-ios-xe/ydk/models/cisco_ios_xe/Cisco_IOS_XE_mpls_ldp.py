""" Cisco_IOS_XE_mpls_ldp 

This module contains a collection of YANG definitions
for the Cisco MPLS LDP configuration and operational data.


The configuration is held in the mpls\-ldp\-config container
which is broken into the following sections\:
  1) global\-cfg contains configuration applicable to the entire
       LSR.
  2) nbr\-table contains configuration for specific LDP neighbors
       or peers.
  3) passwords contains configuration regarding passwords, both
       local and those to be used with specific neighbors.
  4) label\-cfg contains the label allocation and advertisement
       configuration and filters.
  5) discovery contains the configuration for link\-hello and
       targetted hello protocol parameters including
       interface\-specific settings for transport.
  6) graceful\-restart contains the configuration for the
       graceful restart feature.
  7) logging contains the configuration for ldp\-specific logs.
  8) interfaces contains the configuration for each interface,
       including and routing interactions specific to that
       interface.

The operational state is held in the mpls\-ldp\-state container
which is broken the following sections\:
  1) oper\-summary contains the summarized global state.
  2) forwarding\-summary contains the summarized forwarding
       state.
  3) bindings\-summary contains the summarized forwarding state.
  4) vrf provides the detailed state on a per VRF basis.
  5) bindings\-advertise\-specs \- holds the advertisement
       specification filters
  6) discovery provides the LDP Discovery operational state.
  7) forwarding provides summary information regarding LDP
       forwarding setup and detailed information on the LDP
       forwarding rewrites
  8) bindings provides the detailed LDP Bindings of address to
       label.
  9) neighbors

The vrf\-table, provides the detailed state on a per VRF basis.
If the router only supports LDP in a single VRF then this table
will have a single entry using the vrf\-name 'default'.
Otherwise this table will have one entry for every VRF where
LDP is enabled on the device.

Each vrf includes\:
   A list parameters used by the VRF
   A capability table containing the capabilities exchanged with
     each neighbor.
   A table of backoff parameters used in this VRF.
   The graceful restart information used between the local
      device and the neighbors should any of them restart.
   An AF\-table which holds all information for a given Address
      Family. This is extensive and is described below.
   The LDP ID used by the device for this vrf.

The AF\-table holds information for a given Address Family
such as\:
     \- per\-interface state.
     \- IGP synchronization data.
     \- LDP bindings statistics.
     \- LDP forwarding statistics.


  Terms and Acronyms

  FRR \- Fast Re\-Reroute

  ICCP \- Inter\-Chassis Communication Protocol

  LACP \- Link Aggregation Control Protocol

  LDP \- Label Distribution Protocol

  LER \- Label Edge Router

  LFA \- Loop Free Alternative

  LIB \- Label Information Base

  LSR \- Label Switch Router

  MPLS \- Multi\-Protocol Label Switching

  PQ node \- A node which is a member of both the extended
      P\-space and the Q\-space as defined in
      draft\-ietf\-rtgwg\-rlfa\-node\-protection.

  VRF \- Virtual Route Forwarding

Copyright (c) 2014, 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AdjState(Enum):
    """
    AdjState (Enum Class)

    The current state of the session, all of the

    states 0 to 5 are based on the state machine

    for LDP adjacency peer.

    .. data:: nonex = 0

    	LDP adjacency state: nonexistent.

    .. data:: unsol_op_pdg = 1

    	LDP session state: unsolicited open pending.

    .. data:: deferred = 2

    	LDP session state: deferred.

    .. data:: estab = 3

    	LDP session state: established

    .. data:: lib_exp_wait = 4

    	LDP session state: LIB expension wait.

    .. data:: destroyed = 5

    	LDP session state: destroyed.

    """

    nonex = Enum.YLeaf(0, "nonex")

    unsol_op_pdg = Enum.YLeaf(1, "unsol-op-pdg")

    deferred = Enum.YLeaf(2, "deferred")

    estab = Enum.YLeaf(3, "estab")

    lib_exp_wait = Enum.YLeaf(4, "lib-exp-wait")

    destroyed = Enum.YLeaf(5, "destroyed")


class AdvLabelType(Enum):
    """
    AdvLabelType (Enum Class)

    This provides the configuration of the type of label to

    advertise for matching prefixes and peers.

    .. data:: use_lable = 1

    	Advertise the label for matching prefixes and peers.

    .. data:: use_explicit = 2

    	Advertise explicit null for matching prefixes and peers.

    .. data:: use_implicit = 3

    	Advertise imlicit null for matching prefixes and peers.

    .. data:: none = 4

    	Do not advertise labels for matching prefixes and peers.

    """

    use_lable = Enum.YLeaf(1, "use-lable")

    use_explicit = Enum.YLeaf(2, "use-explicit")

    use_implicit = Enum.YLeaf(3, "use-implicit")

    none = Enum.YLeaf(4, "none")


class Af(Enum):
    """
    Af (Enum Class)

    LDP Address Family

    .. data:: ldp_af_none = 0

    	No Address Family

    .. data:: ldp_af_ipv4 = 1

    	IPv4 AFI

    .. data:: ldp_af_ipv6 = 2

    	IPv6 AFI

    .. data:: ldp_af_ipv4_ipv6 = 3

    	Both IPv4/IPv6 AFIs

    """

    ldp_af_none = Enum.YLeaf(0, "ldp-af-none")

    ldp_af_ipv4 = Enum.YLeaf(1, "ldp-af-ipv4")

    ldp_af_ipv6 = Enum.YLeaf(2, "ldp-af-ipv6")

    ldp_af_ipv4_ipv6 = Enum.YLeaf(3, "ldp-af-ipv4-ipv6")


class AfId(Enum):
    """
    AfId (Enum Class)

    LDP AF type

    .. data:: ldp_af_id_none = 0

    	No Address Family

    .. data:: ldp_af_id_ipv4 = 1

    	IPv4 AFI

    .. data:: ldp_af_id_ipv6 = 2

    	IPv6 AFI

    """

    ldp_af_id_none = Enum.YLeaf(0, "ldp-af-id-none")

    ldp_af_id_ipv4 = Enum.YLeaf(1, "ldp-af-id-ipv4")

    ldp_af_id_ipv6 = Enum.YLeaf(2, "ldp-af-id-ipv6")


class DhcState(Enum):
    """
    DhcState (Enum Class)

    This is the Directed Hello Control State Type.

    .. data:: none = 0

    	There is no current Directed Hello Control State.

    .. data:: dhc_active = 1

    	The Directed Hello is Active.

    .. data:: dhc_passive = 2

    	The Directed Hello is Passive.

    .. data:: dhc_active_passive = 3

    	The Directed Hello is both Active and Passive.

    """

    none = Enum.YLeaf(0, "none")

    dhc_active = Enum.YLeaf(1, "dhc-active")

    dhc_passive = Enum.YLeaf(2, "dhc-passive")

    dhc_active_passive = Enum.YLeaf(3, "dhc-active-passive")


class IccpState(Enum):
    """
    IccpState (Enum Class)

    This enum describes the ICCP state as defined by the

    IETF in TBD.

    .. data:: nonexistent = 1

    	This state is the starting point for the state machine.

    	It indicates that no ICCP connection exists and that

    	there's no LDP session established between the PEs.

    .. data:: initialized = 2

    	This state indicates that an LDP session exists between

    	the PEs but LDP ICCP Capabilitiy have not yet been

    	exchanged between them.

    .. data:: capsent = 3

    	This state indicates that an LDP session exists between

    	the PEs and that the local PE has avertized LDP ICCP

    	Capability to its peer.

    .. data:: caprec = 4

    	This state indicates that an LDP session exists between

    	the PEs and that the local PE has both received and

    	advertized LDP ICCP Capability from/to its peer.

    .. data:: connecting = 5

    	This state indicates that the local PE has initiated an

    	ICCP connection to its peer, and is awaiting its

    	response.

    .. data:: operational = 6

    	This state indicates that the ICCP connection is

    	operational.

    """

    nonexistent = Enum.YLeaf(1, "nonexistent")

    initialized = Enum.YLeaf(2, "initialized")

    capsent = Enum.YLeaf(3, "capsent")

    caprec = Enum.YLeaf(4, "caprec")

    connecting = Enum.YLeaf(5, "connecting")

    operational = Enum.YLeaf(6, "operational")


class IgpSyncState(Enum):
    """
    IgpSyncState (Enum Class)

    This is the IGP Synchronization State.

    .. data:: isync_ready = 0

    	Achieved

    .. data:: isync_not_ready = 1

    	Not achieved

    .. data:: isync_deferred = 2

    	Deferred due to interface delay or global

    	restart delay

    """

    isync_ready = Enum.YLeaf(0, "isync-ready")

    isync_not_ready = Enum.YLeaf(1, "isync-not-ready")

    isync_deferred = Enum.YLeaf(2, "isync-deferred")


class LocalLabelState(Enum):
    """
    LocalLabelState (Enum Class)

    This id the MPLS LDP Local Label State Type.

    .. data:: local_label_state_none = 1

    	None

    .. data:: local_label_state_assigned = 2

    	Assigned

    .. data:: local_label_state_withdrawn = 3

    	Withdrawn

    """

    local_label_state_none = Enum.YLeaf(1, "local-label-state-none")

    local_label_state_assigned = Enum.YLeaf(2, "local-label-state-assigned")

    local_label_state_withdrawn = Enum.YLeaf(3, "local-label-state-withdrawn")


class LoopDetectionType(Enum):
    """
    LoopDetectionType (Enum Class)

    This specifies the type of loop detection either supported by

    the LSR or enabled on the LSR.

    .. data:: none = 1

    	Loop Detection is not enabled on this LSR.

    .. data:: other = 2

    	Loop Detection is enabled but by a method

    	other than those defined.

    .. data:: hop_count = 3

    	Loop Detection is supported by Hop Count only.

    .. data:: path_vector = 4

    	Loop Detection is supported by Path Vector only.

    .. data:: hop_count_and_path_vector = 5

    	Loop Detection is supported by both Hop Count

    	and Path Vector.

    """

    none = Enum.YLeaf(1, "none")

    other = Enum.YLeaf(2, "other")

    hop_count = Enum.YLeaf(3, "hop-count")

    path_vector = Enum.YLeaf(4, "path-vector")

    hop_count_and_path_vector = Enum.YLeaf(5, "hop-count-and-path-vector")


class NbrBgpAdvtState(Enum):
    """
    NbrBgpAdvtState (Enum Class)

    MPLS LDP Neighbor BGP Label Advertisement State

    Type.

    .. data:: not_applicable = 0

    	BGP Label Advertisement is not applicable.

    .. data:: permit = 1

    	BGP Label Advertisement is permitted.

    .. data:: deny = 2

    	BGP Label Advertisement denied.

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    permit = Enum.YLeaf(1, "permit")

    deny = Enum.YLeaf(2, "deny")


class SessionState(Enum):
    """
    SessionState (Enum Class)

    The current state of the session, all of the

    states 1 to 5 are based on the state machine

    for session negotiation behavior.

    .. data:: nonexistent = 1

    	LDP session state: nonexistent.

    .. data:: initialized = 2

    	LDP session state: initialized.

    .. data:: openrec = 3

    	LDP session state: openrec.

    .. data:: opensent = 4

    	LDP session state: opensent.

    .. data:: operational = 5

    	LDP session state: operational.

    """

    nonexistent = Enum.YLeaf(1, "nonexistent")

    initialized = Enum.YLeaf(2, "initialized")

    openrec = Enum.YLeaf(3, "openrec")

    opensent = Enum.YLeaf(4, "opensent")

    operational = Enum.YLeaf(5, "operational")



class NsrSyncNackRsn(Identity):
    """
    Base identity from which LDP Non\-Stop Routing peer LDP
    synchronization nack reason identities are derived.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsn, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn")


class NsrPeerSyncErr(Identity):
    """
    Base for MPLS LDP NSR peer synchronization error types.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErr, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err")


class IcpmType(Identity):
    """
    Base identity from which ICPM types can be derived. As this is
    an extensible protocol, new types are expected.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IcpmType, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:icpm-type")


class IccpType(Identity):
    """
    Base identity from which ICCP types can be derived. As this is
    an extensible protocol, new types are expected.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IccpType, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:iccp-type")


class NsrPeerSyncState(Identity):
    """
    Base identity for LDP NSR Peer Synchronization State.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncState, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-state")


class NsrStatus(Identity):
    """
    Base identity for Non\-Stop Routing State Type.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrStatus, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-status")


class DownNbrReason(Identity):
    """
    Base identity for the reason a neighbor is down.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(DownNbrReason, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:down-nbr-reason")


class RoutePathLblOwner(Identity):
    """
    Base Route path label owner type.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathLblOwner, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-lbl-owner")


class LabelType(Identity):
    """
    Base type for LDP Label Type
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LabelType, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:label-type")


class RoutePathType(Identity):
    """
    Base type for Route path type.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathType, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-type")


class IgpSyncDownReason(Identity):
    """
    Base identity reason IGP Sync was not achieved.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReason, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason")


class MplsLdp(Entity):
    """
    MPLS LDP configuration and operational data.
    
    .. attribute:: mpls_ldp_state
    
    	MPLS LDP operational data
    	**type**\:  :py:class:`MplsLdpState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState>`
    
    .. attribute:: mpls_ldp_config
    
    	MPLS LDP Configuration
    	**type**\:  :py:class:`MplsLdpConfig <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(MplsLdp, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-ldp"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-ldp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("mpls-ldp-state", ("mpls_ldp_state", MplsLdp.MplsLdpState)), ("mpls-ldp-config", ("mpls_ldp_config", MplsLdp.MplsLdpConfig))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.mpls_ldp_state = MplsLdp.MplsLdpState()
        self.mpls_ldp_state.parent = self
        self._children_name_map["mpls_ldp_state"] = "mpls-ldp-state"
        self._children_yang_names.add("mpls-ldp-state")

        self.mpls_ldp_config = MplsLdp.MplsLdpConfig()
        self.mpls_ldp_config.parent = self
        self._children_name_map["mpls_ldp_config"] = "mpls-ldp-config"
        self._children_yang_names.add("mpls-ldp-config")
        self._segment_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp"


    class MplsLdpState(Entity):
        """
        MPLS LDP operational data.
        
        .. attribute:: oper_summary
        
        	LDP operational data summary
        	**type**\:  :py:class:`OperSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.OperSummary>`
        
        .. attribute:: forwarding_summary
        
        	Summary information regarding LDP forwarding setup
        	**type**\:  :py:class:`ForwardingSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary>`
        
        .. attribute:: bindings_summary
        
        	Aggregate counters for the MPLS LDP LIB
        	**type**\:  :py:class:`BindingsSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.BindingsSummary>`
        
        .. attribute:: nsr_summary_all
        
        	This is the LDP NSR summary for the device
        	**type**\:  :py:class:`NsrSummaryAll <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.NsrSummaryAll>`
        
        .. attribute:: icpm_summary_all
        
        	Summary info for LDP ICPM/ICCP
        	**type**\:  :py:class:`IcpmSummaryAll <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll>`
        
        .. attribute:: parameters
        
        	MPLS LDP Global Parameters
        	**type**\:  :py:class:`Parameters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Parameters>`
        
        .. attribute:: capabilities
        
        	LDP capability database information
        	**type**\:  :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Capabilities>`
        
        .. attribute:: backoff_parameters
        
        	MPLS LDP Session Backoff Information
        	**type**\:  :py:class:`BackoffParameters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.BackoffParameters>`
        
        .. attribute:: graceful_restart
        
        	MPLS LDP Graceful Restart Information
        	**type**\:  :py:class:`GracefulRestart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.GracefulRestart>`
        
        .. attribute:: vrfs
        
        	MPLS LDP per\-VRF operational data
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs>`
        
        .. attribute:: discovery
        
        	The LDP Discovery operational state
        	**type**\:  :py:class:`Discovery <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery>`
        
        .. attribute:: forwarding
        
        	Summary information regarding LDP forwarding setup and detailed LDP Forwarding rewrites
        	**type**\:  :py:class:`Forwarding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding>`
        
        .. attribute:: bindings
        
        	The detailed LDP Bindings
        	**type**\:  :py:class:`Bindings <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings>`
        
        .. attribute:: neighbors
        
        	The LDP Neighbors Information
        	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors>`
        
        .. attribute:: label_ranges
        
        	This contaions holds all the label ranges in use by this LDP instance
        	**type**\:  :py:class:`LabelRanges <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.LabelRanges>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(MplsLdp.MplsLdpState, self).__init__()

            self.yang_name = "mpls-ldp-state"
            self.yang_parent_name = "mpls-ldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("oper-summary", ("oper_summary", MplsLdp.MplsLdpState.OperSummary)), ("forwarding-summary", ("forwarding_summary", MplsLdp.MplsLdpState.ForwardingSummary)), ("bindings-summary", ("bindings_summary", MplsLdp.MplsLdpState.BindingsSummary)), ("nsr-summary-all", ("nsr_summary_all", MplsLdp.MplsLdpState.NsrSummaryAll)), ("icpm-summary-all", ("icpm_summary_all", MplsLdp.MplsLdpState.IcpmSummaryAll)), ("parameters", ("parameters", MplsLdp.MplsLdpState.Parameters)), ("capabilities", ("capabilities", MplsLdp.MplsLdpState.Capabilities)), ("backoff-parameters", ("backoff_parameters", MplsLdp.MplsLdpState.BackoffParameters)), ("graceful-restart", ("graceful_restart", MplsLdp.MplsLdpState.GracefulRestart)), ("vrfs", ("vrfs", MplsLdp.MplsLdpState.Vrfs)), ("discovery", ("discovery", MplsLdp.MplsLdpState.Discovery)), ("forwarding", ("forwarding", MplsLdp.MplsLdpState.Forwarding)), ("bindings", ("bindings", MplsLdp.MplsLdpState.Bindings)), ("neighbors", ("neighbors", MplsLdp.MplsLdpState.Neighbors)), ("label-ranges", ("label_ranges", MplsLdp.MplsLdpState.LabelRanges))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.oper_summary = MplsLdp.MplsLdpState.OperSummary()
            self.oper_summary.parent = self
            self._children_name_map["oper_summary"] = "oper-summary"
            self._children_yang_names.add("oper-summary")

            self.forwarding_summary = MplsLdp.MplsLdpState.ForwardingSummary()
            self.forwarding_summary.parent = self
            self._children_name_map["forwarding_summary"] = "forwarding-summary"
            self._children_yang_names.add("forwarding-summary")

            self.bindings_summary = MplsLdp.MplsLdpState.BindingsSummary()
            self.bindings_summary.parent = self
            self._children_name_map["bindings_summary"] = "bindings-summary"
            self._children_yang_names.add("bindings-summary")

            self.nsr_summary_all = MplsLdp.MplsLdpState.NsrSummaryAll()
            self.nsr_summary_all.parent = self
            self._children_name_map["nsr_summary_all"] = "nsr-summary-all"
            self._children_yang_names.add("nsr-summary-all")

            self.icpm_summary_all = MplsLdp.MplsLdpState.IcpmSummaryAll()
            self.icpm_summary_all.parent = self
            self._children_name_map["icpm_summary_all"] = "icpm-summary-all"
            self._children_yang_names.add("icpm-summary-all")

            self.parameters = MplsLdp.MplsLdpState.Parameters()
            self.parameters.parent = self
            self._children_name_map["parameters"] = "parameters"
            self._children_yang_names.add("parameters")

            self.capabilities = MplsLdp.MplsLdpState.Capabilities()
            self.capabilities.parent = self
            self._children_name_map["capabilities"] = "capabilities"
            self._children_yang_names.add("capabilities")

            self.backoff_parameters = MplsLdp.MplsLdpState.BackoffParameters()
            self.backoff_parameters.parent = self
            self._children_name_map["backoff_parameters"] = "backoff-parameters"
            self._children_yang_names.add("backoff-parameters")

            self.graceful_restart = MplsLdp.MplsLdpState.GracefulRestart()
            self.graceful_restart.parent = self
            self._children_name_map["graceful_restart"] = "graceful-restart"
            self._children_yang_names.add("graceful-restart")

            self.vrfs = MplsLdp.MplsLdpState.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._children_yang_names.add("vrfs")

            self.discovery = MplsLdp.MplsLdpState.Discovery()
            self.discovery.parent = self
            self._children_name_map["discovery"] = "discovery"
            self._children_yang_names.add("discovery")

            self.forwarding = MplsLdp.MplsLdpState.Forwarding()
            self.forwarding.parent = self
            self._children_name_map["forwarding"] = "forwarding"
            self._children_yang_names.add("forwarding")

            self.bindings = MplsLdp.MplsLdpState.Bindings()
            self.bindings.parent = self
            self._children_name_map["bindings"] = "bindings"
            self._children_yang_names.add("bindings")

            self.neighbors = MplsLdp.MplsLdpState.Neighbors()
            self.neighbors.parent = self
            self._children_name_map["neighbors"] = "neighbors"
            self._children_yang_names.add("neighbors")

            self.label_ranges = MplsLdp.MplsLdpState.LabelRanges()
            self.label_ranges.parent = self
            self._children_name_map["label_ranges"] = "label-ranges"
            self._children_yang_names.add("label-ranges")
            self._segment_path = lambda: "mpls-ldp-state"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/%s" % self._segment_path()


        class OperSummary(Entity):
            """
            LDP operational data summary
            
            .. attribute:: common
            
            	Common Summary information
            	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.OperSummary.Common>`
            
            .. attribute:: number_of_vrf
            
            	Number of configured VRFs (including default)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_vrf_oper
            
            	Number of configured operational VRFs (including default)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_interfaces
            
            	Number of known interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_fwd_ref_interfaces
            
            	Number of Forward Reference interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_autocfg_interfaces
            
            	Number of auto\-configured interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_of_ipv4_rib_tbl
            
            	Total number of ipv4 RIB tables
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_of_ipv4_rib_tbl_reg
            
            	Number of ipv4 RIB tables registered
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.OperSummary, self).__init__()

                self.yang_name = "oper-summary"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("common", ("common", MplsLdp.MplsLdpState.OperSummary.Common))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('number_of_vrf', YLeaf(YType.uint32, 'number-of-vrf')),
                    ('number_of_vrf_oper', YLeaf(YType.uint32, 'number-of-vrf-oper')),
                    ('number_of_interfaces', YLeaf(YType.uint32, 'number-of-interfaces')),
                    ('number_of_fwd_ref_interfaces', YLeaf(YType.uint32, 'number-of-fwd-ref-interfaces')),
                    ('number_of_autocfg_interfaces', YLeaf(YType.uint32, 'number-of-autocfg-interfaces')),
                    ('no_of_ipv4_rib_tbl', YLeaf(YType.uint32, 'no-of-ipv4-rib-tbl')),
                    ('no_of_ipv4_rib_tbl_reg', YLeaf(YType.uint32, 'no-of-ipv4-rib-tbl-reg')),
                ])
                self.number_of_vrf = None
                self.number_of_vrf_oper = None
                self.number_of_interfaces = None
                self.number_of_fwd_ref_interfaces = None
                self.number_of_autocfg_interfaces = None
                self.no_of_ipv4_rib_tbl = None
                self.no_of_ipv4_rib_tbl_reg = None

                self.common = MplsLdp.MplsLdpState.OperSummary.Common()
                self.common.parent = self
                self._children_name_map["common"] = "common"
                self._children_yang_names.add("common")
                self._segment_path = lambda: "oper-summary"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.OperSummary, ['number_of_vrf', 'number_of_vrf_oper', 'number_of_interfaces', 'number_of_fwd_ref_interfaces', 'number_of_autocfg_interfaces', 'no_of_ipv4_rib_tbl', 'no_of_ipv4_rib_tbl_reg'], name, value)


            class Common(Entity):
                """
                Common Summary information
                
                .. attribute:: address_families
                
                	Address Families enabled
                	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                
                .. attribute:: number_of_neighbors
                
                	Number of neighbor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_graceful_restart_neighbors
                
                	Number of Graceful Restart neighbor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_downstream_on_demand_neighbors
                
                	Number of Downstream\-On\-Demand neighbor
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: numberof_ipv4_hello_adj
                
                	Number of LDP discovery IPv4 hello adjacencies
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ipv4_routes
                
                	Number of resolved IPv4 routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ipv4_local_addresses
                
                	Number of IPv4 local addresses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ldp_interfaces
                
                	Number of LDP configured interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ipv4ldp_interfaces
                
                	Number of LDP IPv4 configured interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.OperSummary.Common, self).__init__()

                    self.yang_name = "common"
                    self.yang_parent_name = "oper-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address_families', YLeaf(YType.enumeration, 'address-families')),
                        ('number_of_neighbors', YLeaf(YType.uint32, 'number-of-neighbors')),
                        ('number_of_graceful_restart_neighbors', YLeaf(YType.uint32, 'number-of-graceful-restart-neighbors')),
                        ('number_of_downstream_on_demand_neighbors', YLeaf(YType.uint32, 'number-of-downstream-on-demand-neighbors')),
                        ('numberof_ipv4_hello_adj', YLeaf(YType.uint32, 'numberof-ipv4-hello-adj')),
                        ('number_of_ipv4_routes', YLeaf(YType.uint32, 'number-of-ipv4-routes')),
                        ('number_of_ipv4_local_addresses', YLeaf(YType.uint32, 'number-of-ipv4-local-addresses')),
                        ('number_of_ldp_interfaces', YLeaf(YType.uint32, 'number-of-ldp-interfaces')),
                        ('number_of_ipv4ldp_interfaces', YLeaf(YType.uint32, 'number-of-ipv4ldp-interfaces')),
                    ])
                    self.address_families = None
                    self.number_of_neighbors = None
                    self.number_of_graceful_restart_neighbors = None
                    self.number_of_downstream_on_demand_neighbors = None
                    self.numberof_ipv4_hello_adj = None
                    self.number_of_ipv4_routes = None
                    self.number_of_ipv4_local_addresses = None
                    self.number_of_ldp_interfaces = None
                    self.number_of_ipv4ldp_interfaces = None
                    self._segment_path = lambda: "common"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/oper-summary/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.OperSummary.Common, ['address_families', 'number_of_neighbors', 'number_of_graceful_restart_neighbors', 'number_of_downstream_on_demand_neighbors', 'numberof_ipv4_hello_adj', 'number_of_ipv4_routes', 'number_of_ipv4_local_addresses', 'number_of_ldp_interfaces', 'number_of_ipv4ldp_interfaces'], name, value)


        class ForwardingSummary(Entity):
            """
            Summary information regarding LDP forwarding
            setup
            
            .. attribute:: pfxs
            
            	MPLS LDP forwarding prefix rewrite summary
            	**type**\:  :py:class:`Pfxs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs>`
            
            .. attribute:: nhs
            
            	MPLS LDP forwarding rewrite next\-hop/path summary
            	**type**\:  :py:class:`Nhs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Nhs>`
            
            .. attribute:: intfs_fwd_count
            
            	MPLS forwarding enabled interface count
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: local_lbls
            
            	Local label allocated count
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.ForwardingSummary, self).__init__()

                self.yang_name = "forwarding-summary"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("pfxs", ("pfxs", MplsLdp.MplsLdpState.ForwardingSummary.Pfxs)), ("nhs", ("nhs", MplsLdp.MplsLdpState.ForwardingSummary.Nhs))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('intfs_fwd_count', YLeaf(YType.uint16, 'intfs-fwd-count')),
                    ('local_lbls', YLeaf(YType.uint16, 'local-lbls')),
                ])
                self.intfs_fwd_count = None
                self.local_lbls = None

                self.pfxs = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs()
                self.pfxs.parent = self
                self._children_name_map["pfxs"] = "pfxs"
                self._children_yang_names.add("pfxs")

                self.nhs = MplsLdp.MplsLdpState.ForwardingSummary.Nhs()
                self.nhs.parent = self
                self._children_name_map["nhs"] = "nhs"
                self._children_yang_names.add("nhs")
                self._segment_path = lambda: "forwarding-summary"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.ForwardingSummary, ['intfs_fwd_count', 'local_lbls'], name, value)


            class Pfxs(Entity):
                """
                MPLS LDP forwarding prefix rewrite summary
                
                .. attribute:: labeled_pfxs_aggr
                
                	Labeled prefix count for all paths
                	**type**\:  :py:class:`LabeledPfxsAggr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr>`
                
                .. attribute:: labeled_pfxs_primary
                
                	Labeled prefix count related to primary paths only
                	**type**\:  :py:class:`LabeledPfxsPrimary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary>`
                
                .. attribute:: labeled_pfxs_backup
                
                	Labeled prefix count related to backup paths only
                	**type**\:  :py:class:`LabeledPfxsBackup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup>`
                
                .. attribute:: total_pfxs
                
                	Total Prefix count
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: ecmp_pfxs
                
                	Count of prefixes with ECMP
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: protected_pfxs
                
                	Count of FRR protected prefixes
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs, self).__init__()

                    self.yang_name = "pfxs"
                    self.yang_parent_name = "forwarding-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("labeled-pfxs-aggr", ("labeled_pfxs_aggr", MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr)), ("labeled-pfxs-primary", ("labeled_pfxs_primary", MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary)), ("labeled-pfxs-backup", ("labeled_pfxs_backup", MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_pfxs', YLeaf(YType.uint16, 'total-pfxs')),
                        ('ecmp_pfxs', YLeaf(YType.uint16, 'ecmp-pfxs')),
                        ('protected_pfxs', YLeaf(YType.uint16, 'protected-pfxs')),
                    ])
                    self.total_pfxs = None
                    self.ecmp_pfxs = None
                    self.protected_pfxs = None

                    self.labeled_pfxs_aggr = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr()
                    self.labeled_pfxs_aggr.parent = self
                    self._children_name_map["labeled_pfxs_aggr"] = "labeled-pfxs-aggr"
                    self._children_yang_names.add("labeled-pfxs-aggr")

                    self.labeled_pfxs_primary = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary()
                    self.labeled_pfxs_primary.parent = self
                    self._children_name_map["labeled_pfxs_primary"] = "labeled-pfxs-primary"
                    self._children_yang_names.add("labeled-pfxs-primary")

                    self.labeled_pfxs_backup = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup()
                    self.labeled_pfxs_backup.parent = self
                    self._children_name_map["labeled_pfxs_backup"] = "labeled-pfxs-backup"
                    self._children_yang_names.add("labeled-pfxs-backup")
                    self._segment_path = lambda: "pfxs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding-summary/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs, ['total_pfxs', 'ecmp_pfxs', 'protected_pfxs'], name, value)


                class LabeledPfxsAggr(Entity):
                    """
                    Labeled prefix count for all paths
                    
                    .. attribute:: labeled_pfxs
                    
                    	Count of labeled prefixes with 1 or more paths labeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: labeled_pfxs_partial
                    
                    	Count of labeled prefixes with some (but not ALL) paths labeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: unlabeled_pfxs
                    
                    	Count of labeled prefixes with ALL paths unlabeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr, self).__init__()

                        self.yang_name = "labeled-pfxs-aggr"
                        self.yang_parent_name = "pfxs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('labeled_pfxs', YLeaf(YType.uint16, 'labeled-pfxs')),
                            ('labeled_pfxs_partial', YLeaf(YType.uint16, 'labeled-pfxs-partial')),
                            ('unlabeled_pfxs', YLeaf(YType.uint16, 'unlabeled-pfxs')),
                        ])
                        self.labeled_pfxs = None
                        self.labeled_pfxs_partial = None
                        self.unlabeled_pfxs = None
                        self._segment_path = lambda: "labeled-pfxs-aggr"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding-summary/pfxs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr, ['labeled_pfxs', 'labeled_pfxs_partial', 'unlabeled_pfxs'], name, value)


                class LabeledPfxsPrimary(Entity):
                    """
                    Labeled prefix count related to primary paths
                    only
                    
                    .. attribute:: labeled_pfxs
                    
                    	Count of labeled prefixes with 1 or more paths labeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: labeled_pfxs_partial
                    
                    	Count of labeled prefixes with some (but not ALL) paths labeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: unlabeled_pfxs
                    
                    	Count of labeled prefixes with ALL paths unlabeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary, self).__init__()

                        self.yang_name = "labeled-pfxs-primary"
                        self.yang_parent_name = "pfxs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('labeled_pfxs', YLeaf(YType.uint16, 'labeled-pfxs')),
                            ('labeled_pfxs_partial', YLeaf(YType.uint16, 'labeled-pfxs-partial')),
                            ('unlabeled_pfxs', YLeaf(YType.uint16, 'unlabeled-pfxs')),
                        ])
                        self.labeled_pfxs = None
                        self.labeled_pfxs_partial = None
                        self.unlabeled_pfxs = None
                        self._segment_path = lambda: "labeled-pfxs-primary"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding-summary/pfxs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary, ['labeled_pfxs', 'labeled_pfxs_partial', 'unlabeled_pfxs'], name, value)


                class LabeledPfxsBackup(Entity):
                    """
                    Labeled prefix count related to backup paths
                    only
                    
                    .. attribute:: labeled_pfxs
                    
                    	Count of labeled prefixes with 1 or more paths labeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: labeled_pfxs_partial
                    
                    	Count of labeled prefixes with some (but not ALL) paths labeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: unlabeled_pfxs
                    
                    	Count of labeled prefixes with ALL paths unlabeled
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup, self).__init__()

                        self.yang_name = "labeled-pfxs-backup"
                        self.yang_parent_name = "pfxs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('labeled_pfxs', YLeaf(YType.uint16, 'labeled-pfxs')),
                            ('labeled_pfxs_partial', YLeaf(YType.uint16, 'labeled-pfxs-partial')),
                            ('unlabeled_pfxs', YLeaf(YType.uint16, 'unlabeled-pfxs')),
                        ])
                        self.labeled_pfxs = None
                        self.labeled_pfxs_partial = None
                        self.unlabeled_pfxs = None
                        self._segment_path = lambda: "labeled-pfxs-backup"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding-summary/pfxs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup, ['labeled_pfxs', 'labeled_pfxs_partial', 'unlabeled_pfxs'], name, value)


            class Nhs(Entity):
                """
                MPLS LDP forwarding rewrite next\-hop/path summary
                
                .. attribute:: total_paths
                
                	Total path count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: protected_paths
                
                	Count of FRR protected paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: backup_paths
                
                	Count of non\-primary backup paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_backup_paths
                
                	Count of non\-primary remote backup paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: labeled_paths
                
                	Count of all labeled paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: labeled_backup_paths
                
                	Count of labeled backup paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.ForwardingSummary.Nhs, self).__init__()

                    self.yang_name = "nhs"
                    self.yang_parent_name = "forwarding-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_paths', YLeaf(YType.uint32, 'total-paths')),
                        ('protected_paths', YLeaf(YType.uint32, 'protected-paths')),
                        ('backup_paths', YLeaf(YType.uint32, 'backup-paths')),
                        ('remote_backup_paths', YLeaf(YType.uint32, 'remote-backup-paths')),
                        ('labeled_paths', YLeaf(YType.uint32, 'labeled-paths')),
                        ('labeled_backup_paths', YLeaf(YType.uint32, 'labeled-backup-paths')),
                    ])
                    self.total_paths = None
                    self.protected_paths = None
                    self.backup_paths = None
                    self.remote_backup_paths = None
                    self.labeled_paths = None
                    self.labeled_backup_paths = None
                    self._segment_path = lambda: "nhs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding-summary/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.ForwardingSummary.Nhs, ['total_paths', 'protected_paths', 'backup_paths', 'remote_backup_paths', 'labeled_paths', 'labeled_backup_paths'], name, value)


        class BindingsSummary(Entity):
            """
            Aggregate counters for the MPLS LDP LIB.
            
            .. attribute:: binding_total
            
            	Total bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_no_route
            
            	Bindings with no route
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_no_route
            
            	Local bindings with no route
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local
            
            	Number of local bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_null
            
            	Number of local null bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_implicit_null
            
            	Number of local implicit null bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_explicit_null
            
            	Number of local explicit null bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_non_null
            
            	Number of local non\-null bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_oor
            
            	This is the number of local bindings needing label but which hit the Out\-Of\-Resource condition
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lowest_allocated_label
            
            	Lowest allocated label
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: highest_allocated_label
            
            	Highest allocated label
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_remote
            
            	Number of remote bindings
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.BindingsSummary, self).__init__()

                self.yang_name = "bindings-summary"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('binding_total', YLeaf(YType.uint32, 'binding-total')),
                    ('binding_no_route', YLeaf(YType.uint32, 'binding-no-route')),
                    ('binding_local_no_route', YLeaf(YType.uint32, 'binding-local-no-route')),
                    ('binding_local', YLeaf(YType.uint32, 'binding-local')),
                    ('binding_local_null', YLeaf(YType.uint32, 'binding-local-null')),
                    ('binding_local_implicit_null', YLeaf(YType.uint32, 'binding-local-implicit-null')),
                    ('binding_local_explicit_null', YLeaf(YType.uint32, 'binding-local-explicit-null')),
                    ('binding_local_non_null', YLeaf(YType.uint32, 'binding-local-non-null')),
                    ('binding_local_oor', YLeaf(YType.uint32, 'binding-local-oor')),
                    ('lowest_allocated_label', YLeaf(YType.uint32, 'lowest-allocated-label')),
                    ('highest_allocated_label', YLeaf(YType.uint32, 'highest-allocated-label')),
                    ('binding_remote', YLeaf(YType.uint32, 'binding-remote')),
                ])
                self.binding_total = None
                self.binding_no_route = None
                self.binding_local_no_route = None
                self.binding_local = None
                self.binding_local_null = None
                self.binding_local_implicit_null = None
                self.binding_local_explicit_null = None
                self.binding_local_non_null = None
                self.binding_local_oor = None
                self.lowest_allocated_label = None
                self.highest_allocated_label = None
                self.binding_remote = None
                self._segment_path = lambda: "bindings-summary"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.BindingsSummary, ['binding_total', 'binding_no_route', 'binding_local_no_route', 'binding_local', 'binding_local_null', 'binding_local_implicit_null', 'binding_local_explicit_null', 'binding_local_non_null', 'binding_local_oor', 'lowest_allocated_label', 'highest_allocated_label', 'binding_remote'], name, value)


        class NsrSummaryAll(Entity):
            """
            This is the LDP NSR summary for the device.
            
            .. attribute:: nsr_sum_in_label_reqs_created
            
            	In label Request Records created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_in_label_reqs_freed
            
            	In label Request Records freed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_in_label_withdraw_created
            
            	In label Withdraw Records created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_in_label_withdraw_freed
            
            	In label Withdraw Records freed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_lcl_addr_withdraw_set
            
            	Local Address Withdraw set
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_lcl_addr_withdraw_cleared
            
            	Local Address Withdraw cleared
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.NsrSummaryAll, self).__init__()

                self.yang_name = "nsr-summary-all"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('nsr_sum_in_label_reqs_created', YLeaf(YType.uint32, 'nsr-sum-in-label-reqs-created')),
                    ('nsr_sum_in_label_reqs_freed', YLeaf(YType.uint32, 'nsr-sum-in-label-reqs-freed')),
                    ('nsr_sum_in_label_withdraw_created', YLeaf(YType.uint32, 'nsr-sum-in-label-withdraw-created')),
                    ('nsr_sum_in_label_withdraw_freed', YLeaf(YType.uint32, 'nsr-sum-in-label-withdraw-freed')),
                    ('nsr_sum_lcl_addr_withdraw_set', YLeaf(YType.uint32, 'nsr-sum-lcl-addr-withdraw-set')),
                    ('nsr_sum_lcl_addr_withdraw_cleared', YLeaf(YType.uint32, 'nsr-sum-lcl-addr-withdraw-cleared')),
                ])
                self.nsr_sum_in_label_reqs_created = None
                self.nsr_sum_in_label_reqs_freed = None
                self.nsr_sum_in_label_withdraw_created = None
                self.nsr_sum_in_label_withdraw_freed = None
                self.nsr_sum_lcl_addr_withdraw_set = None
                self.nsr_sum_lcl_addr_withdraw_cleared = None
                self._segment_path = lambda: "nsr-summary-all"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.NsrSummaryAll, ['nsr_sum_in_label_reqs_created', 'nsr_sum_in_label_reqs_freed', 'nsr_sum_in_label_withdraw_created', 'nsr_sum_in_label_withdraw_freed', 'nsr_sum_lcl_addr_withdraw_set', 'nsr_sum_lcl_addr_withdraw_cleared'], name, value)


        class IcpmSummaryAll(Entity):
            """
            Summary info for LDP ICPM/ICCP.
            
            .. attribute:: iccp_rg_conn_count
            
            	ICCP RG Connect count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: iccp_rg_disconn_count
            
            	ICCP RG Disconnect count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: iccp_rg_notif_count
            
            	ICCP RG Notif count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: iccp_rg_app_data_count
            
            	ICCP RG App Data count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: icpm_rgid_table_info
            
            	This defines the ICPM RGID Table
            	**type**\:  :py:class:`IcpmRgidTableInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo>`
            
            .. attribute:: icpm_session_table
            
            	This is a list of ICPM sessions
            	**type**\:  :py:class:`IcpmSessionTable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.IcpmSummaryAll, self).__init__()

                self.yang_name = "icpm-summary-all"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("icpm-rgid-table-info", ("icpm_rgid_table_info", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo)), ("icpm-session-table", ("icpm_session_table", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('iccp_rg_conn_count', YLeaf(YType.uint32, 'iccp-rg-conn-count')),
                    ('iccp_rg_disconn_count', YLeaf(YType.uint32, 'iccp-rg-disconn-count')),
                    ('iccp_rg_notif_count', YLeaf(YType.uint32, 'iccp-rg-notif-count')),
                    ('iccp_rg_app_data_count', YLeaf(YType.uint32, 'iccp-rg-app-data-count')),
                ])
                self.iccp_rg_conn_count = None
                self.iccp_rg_disconn_count = None
                self.iccp_rg_notif_count = None
                self.iccp_rg_app_data_count = None

                self.icpm_rgid_table_info = MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo()
                self.icpm_rgid_table_info.parent = self
                self._children_name_map["icpm_rgid_table_info"] = "icpm-rgid-table-info"
                self._children_yang_names.add("icpm-rgid-table-info")

                self.icpm_session_table = MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable()
                self.icpm_session_table.parent = self
                self._children_name_map["icpm_session_table"] = "icpm-session-table"
                self._children_yang_names.add("icpm-session-table")
                self._segment_path = lambda: "icpm-summary-all"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll, ['iccp_rg_conn_count', 'iccp_rg_disconn_count', 'iccp_rg_notif_count', 'iccp_rg_app_data_count'], name, value)


            class IcpmRgidTableInfo(Entity):
                """
                This defines the ICPM RGID Table
                
                .. attribute:: red_group
                
                	This is the data for an individual ICPM Rredundandy Group,
                	**type**\: list of  		 :py:class:`RedGroup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo, self).__init__()

                    self.yang_name = "icpm-rgid-table-info"
                    self.yang_parent_name = "icpm-summary-all"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("red-group", ("red_group", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup))])
                    self._leafs = OrderedDict()

                    self.red_group = YList(self)
                    self._segment_path = lambda: "icpm-rgid-table-info"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/icpm-summary-all/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo, [], name, value)


                class RedGroup(Entity):
                    """
                    This is the data for an individual ICPM Rredundandy
                    Group,
                    
                    .. attribute:: rg_id  (key)
                    
                    	This is the ICPM RG identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: icpm_protocols
                    
                    	This list contains all active icpm protocols
                    	**type**\: list of  		 :py:class:`IcpmProtocols <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup, self).__init__()

                        self.yang_name = "red-group"
                        self.yang_parent_name = "icpm-rgid-table-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rg_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("icpm-protocols", ("icpm_protocols", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols))])
                        self._leafs = OrderedDict([
                            ('rg_id', YLeaf(YType.uint32, 'rg-id')),
                        ])
                        self.rg_id = None

                        self.icpm_protocols = YList(self)
                        self._segment_path = lambda: "red-group" + "[rg-id='" + str(self.rg_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/icpm-summary-all/icpm-rgid-table-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup, ['rg_id'], name, value)


                    class IcpmProtocols(Entity):
                        """
                        This list contains all active icpm protocols.
                        
                        .. attribute:: icpm_type  (key)
                        
                        	ICPM Type
                        	**type**\:  :py:class:`IcpmType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IcpmType>`
                        
                        .. attribute:: redun_groups
                        
                        	List of Redundancy Groups
                        	**type**\: list of  		 :py:class:`RedunGroups <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols, self).__init__()

                            self.yang_name = "icpm-protocols"
                            self.yang_parent_name = "red-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['icpm_type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("redun-groups", ("redun_groups", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups))])
                            self._leafs = OrderedDict([
                                ('icpm_type', YLeaf(YType.identityref, 'icpm-type')),
                            ])
                            self.icpm_type = None

                            self.redun_groups = YList(self)
                            self._segment_path = lambda: "icpm-protocols" + "[icpm-type='" + str(self.icpm_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols, ['icpm_type'], name, value)


                        class RedunGroups(Entity):
                            """
                            List of Redundancy Groups
                            
                            .. attribute:: rg_id  (key)
                            
                            	Redundancy Group Identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_id
                            
                            	LSR identifier
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: client_id
                            
                            	Client Identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	ICCP State
                            	**type**\: str
                            
                            .. attribute:: iccp_apps
                            
                            	List of apps
                            	**type**\: list of  		 :py:class:`IccpApps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups, self).__init__()

                                self.yang_name = "redun-groups"
                                self.yang_parent_name = "icpm-protocols"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['rg_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("iccp-apps", ("iccp_apps", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps))])
                                self._leafs = OrderedDict([
                                    ('rg_id', YLeaf(YType.uint32, 'rg-id')),
                                    ('peer_id', YLeaf(YType.str, 'peer-id')),
                                    ('client_id', YLeaf(YType.uint32, 'client_id')),
                                    ('state', YLeaf(YType.str, 'state')),
                                ])
                                self.rg_id = None
                                self.peer_id = None
                                self.client_id = None
                                self.state = None

                                self.iccp_apps = YList(self)
                                self._segment_path = lambda: "redun-groups" + "[rg-id='" + str(self.rg_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups, ['rg_id', 'peer_id', 'client_id', 'state'], name, value)


                            class IccpApps(Entity):
                                """
                                List of apps
                                
                                .. attribute:: iccp_app  (key)
                                
                                	ICCP App Type
                                	**type**\:  :py:class:`IccpType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpType>`
                                
                                .. attribute:: app_state
                                
                                	App State
                                	**type**\:  :py:class:`IccpState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpState>`
                                
                                .. attribute:: ptcl_ver
                                
                                	ICCP App Protocol Version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps, self).__init__()

                                    self.yang_name = "iccp-apps"
                                    self.yang_parent_name = "redun-groups"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['iccp_app']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('iccp_app', YLeaf(YType.identityref, 'iccp-app')),
                                        ('app_state', YLeaf(YType.enumeration, 'app-state')),
                                        ('ptcl_ver', YLeaf(YType.uint32, 'ptcl-ver')),
                                    ])
                                    self.iccp_app = None
                                    self.app_state = None
                                    self.ptcl_ver = None
                                    self._segment_path = lambda: "iccp-apps" + "[iccp-app='" + str(self.iccp_app) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps, ['iccp_app', 'app_state', 'ptcl_ver'], name, value)


            class IcpmSessionTable(Entity):
                """
                This is a list of ICPM sessions.
                
                .. attribute:: session_table
                
                	ICPM LDP Session Table
                	**type**\: list of  		 :py:class:`SessionTable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable, self).__init__()

                    self.yang_name = "icpm-session-table"
                    self.yang_parent_name = "icpm-summary-all"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("session-table", ("session_table", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable))])
                    self._leafs = OrderedDict()

                    self.session_table = YList(self)
                    self._segment_path = lambda: "icpm-session-table"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/icpm-summary-all/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable, [], name, value)


                class SessionTable(Entity):
                    """
                    ICPM LDP Session Table
                    
                    .. attribute:: session_id  (key)
                    
                    	This is the ICPM sesion identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: icpm_protocols
                    
                    	This list contains all active icpm protocols
                    	**type**\: list of  		 :py:class:`IcpmProtocols <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable, self).__init__()

                        self.yang_name = "session-table"
                        self.yang_parent_name = "icpm-session-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['session_id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("icpm-protocols", ("icpm_protocols", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols))])
                        self._leafs = OrderedDict([
                            ('session_id', YLeaf(YType.uint32, 'session-id')),
                        ])
                        self.session_id = None

                        self.icpm_protocols = YList(self)
                        self._segment_path = lambda: "session-table" + "[session-id='" + str(self.session_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/icpm-summary-all/icpm-session-table/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable, ['session_id'], name, value)


                    class IcpmProtocols(Entity):
                        """
                        This list contains all active icpm protocols.
                        
                        .. attribute:: icpm_type  (key)
                        
                        	ICPM Type
                        	**type**\:  :py:class:`IcpmType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IcpmType>`
                        
                        .. attribute:: redun_groups
                        
                        	List of Redundancy Groups
                        	**type**\: list of  		 :py:class:`RedunGroups <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols, self).__init__()

                            self.yang_name = "icpm-protocols"
                            self.yang_parent_name = "session-table"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['icpm_type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("redun-groups", ("redun_groups", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups))])
                            self._leafs = OrderedDict([
                                ('icpm_type', YLeaf(YType.identityref, 'icpm-type')),
                            ])
                            self.icpm_type = None

                            self.redun_groups = YList(self)
                            self._segment_path = lambda: "icpm-protocols" + "[icpm-type='" + str(self.icpm_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols, ['icpm_type'], name, value)


                        class RedunGroups(Entity):
                            """
                            List of Redundancy Groups
                            
                            .. attribute:: rg_id  (key)
                            
                            	Redundancy Group Identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_id
                            
                            	LSR identifier
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: client_id
                            
                            	Client Identifier
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: state
                            
                            	ICCP State
                            	**type**\: str
                            
                            .. attribute:: iccp_apps
                            
                            	List of apps
                            	**type**\: list of  		 :py:class:`IccpApps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups, self).__init__()

                                self.yang_name = "redun-groups"
                                self.yang_parent_name = "icpm-protocols"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['rg_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("iccp-apps", ("iccp_apps", MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps))])
                                self._leafs = OrderedDict([
                                    ('rg_id', YLeaf(YType.uint32, 'rg-id')),
                                    ('peer_id', YLeaf(YType.str, 'peer-id')),
                                    ('client_id', YLeaf(YType.uint32, 'client_id')),
                                    ('state', YLeaf(YType.str, 'state')),
                                ])
                                self.rg_id = None
                                self.peer_id = None
                                self.client_id = None
                                self.state = None

                                self.iccp_apps = YList(self)
                                self._segment_path = lambda: "redun-groups" + "[rg-id='" + str(self.rg_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups, ['rg_id', 'peer_id', 'client_id', 'state'], name, value)


                            class IccpApps(Entity):
                                """
                                List of apps
                                
                                .. attribute:: iccp_app  (key)
                                
                                	ICCP App Type
                                	**type**\:  :py:class:`IccpType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpType>`
                                
                                .. attribute:: app_state
                                
                                	App State
                                	**type**\:  :py:class:`IccpState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpState>`
                                
                                .. attribute:: ptcl_ver
                                
                                	ICCP App Protocol Version
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    super(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps, self).__init__()

                                    self.yang_name = "iccp-apps"
                                    self.yang_parent_name = "redun-groups"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['iccp_app']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('iccp_app', YLeaf(YType.identityref, 'iccp-app')),
                                        ('app_state', YLeaf(YType.enumeration, 'app-state')),
                                        ('ptcl_ver', YLeaf(YType.uint32, 'ptcl-ver')),
                                    ])
                                    self.iccp_app = None
                                    self.app_state = None
                                    self.ptcl_ver = None
                                    self._segment_path = lambda: "iccp-apps" + "[iccp-app='" + str(self.iccp_app) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps, ['iccp_app', 'app_state', 'ptcl_ver'], name, value)


        class Parameters(Entity):
            """
            MPLS LDP Global Parameters
            
            .. attribute:: global_md5_password_enabled
            
            	Global MD5 password enabled
            	**type**\: bool
            
            .. attribute:: protocol_version
            
            	Protocol version
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: keepalive_interval
            
            	Keepalive interval in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: session_hold_time
            
            	Session hold time in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: le_no_route_timeout
            
            	LIB entry no route timeout in second
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: af_binding_withdraw_delay
            
            	Delay (sec) in Binding Withdrawal for an Address Family
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: max_intf_attached
            
            	Maximum number of LDP enabled attached interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_intf_te
            
            	Maximum number of LDP enabled TE interfaces
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_peer
            
            	Maximum number of LDP peers
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_of_mem_state
            
            	This is a counter of the number of times LDP attempted to create a label or binding and failed due a memory allocation failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: discovery_quick_start_disabled_on_interfaces
            
            	Discovery quick\-start disabled on some enabled interfaces
            	**type**\: bool
            
            .. attribute:: address_family_parameter
            
            	Per AF parameters
            	**type**\: list of  		 :py:class:`AddressFamilyParameter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter>`
            
            .. attribute:: dod_max_hop
            
            	Maximum number of hops for Downstream\-on\-Demand
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: feature
            
            	This entry describes an LDP feature available on the device. This does not indicate whether the feature is enabled, just the raw ability to support the feature. The features may include, but are not limited to\: 'Auto\-Configuration', 'Basic', 'ICPM', 'IP\-over\-MPLS', 'IGP\-Sync', 'LLAF', 'TCP\-MD5\-Rollover', 'TDP', and 'NSR'
            	**type**\: list of str
            
            .. attribute:: loop_detection
            
            	A indication of whether this LSR has enabled loop detection. Since Loop Detection is determined during Session Initialization, an individual session may not be running with loop detection.  This object simply gives an indication of whether or not the LSR has the ability enabled to support Loop Detection and which types
            	**type**\:  :py:class:`LoopDetectionType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LoopDetectionType>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Parameters, self).__init__()

                self.yang_name = "parameters"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("address-family-parameter", ("address_family_parameter", MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter))])
                self._leafs = OrderedDict([
                    ('global_md5_password_enabled', YLeaf(YType.boolean, 'global-md5-password-enabled')),
                    ('protocol_version', YLeaf(YType.uint32, 'protocol-version')),
                    ('keepalive_interval', YLeaf(YType.uint32, 'keepalive-interval')),
                    ('session_hold_time', YLeaf(YType.uint32, 'session-hold-time')),
                    ('le_no_route_timeout', YLeaf(YType.uint32, 'le-no-route-timeout')),
                    ('af_binding_withdraw_delay', YLeaf(YType.uint32, 'af-binding-withdraw-delay')),
                    ('max_intf_attached', YLeaf(YType.uint32, 'max-intf-attached')),
                    ('max_intf_te', YLeaf(YType.uint32, 'max-intf-te')),
                    ('max_peer', YLeaf(YType.uint32, 'max-peer')),
                    ('out_of_mem_state', YLeaf(YType.uint32, 'out-of-mem-state')),
                    ('discovery_quick_start_disabled_on_interfaces', YLeaf(YType.boolean, 'discovery-quick-start-disabled-on-interfaces')),
                    ('dod_max_hop', YLeaf(YType.uint32, 'dod-max-hop')),
                    ('feature', YLeafList(YType.str, 'feature')),
                    ('loop_detection', YLeaf(YType.enumeration, 'loop-detection')),
                ])
                self.global_md5_password_enabled = None
                self.protocol_version = None
                self.keepalive_interval = None
                self.session_hold_time = None
                self.le_no_route_timeout = None
                self.af_binding_withdraw_delay = None
                self.max_intf_attached = None
                self.max_intf_te = None
                self.max_peer = None
                self.out_of_mem_state = None
                self.discovery_quick_start_disabled_on_interfaces = None
                self.dod_max_hop = None
                self.feature = []
                self.loop_detection = None

                self.address_family_parameter = YList(self)
                self._segment_path = lambda: "parameters"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.Parameters, ['global_md5_password_enabled', 'protocol_version', 'keepalive_interval', 'session_hold_time', 'le_no_route_timeout', 'af_binding_withdraw_delay', 'max_intf_attached', 'max_intf_te', 'max_peer', 'out_of_mem_state', 'discovery_quick_start_disabled_on_interfaces', 'dod_max_hop', 'feature', 'loop_detection'], name, value)


            class AddressFamilyParameter(Entity):
                """
                Per AF parameters
                
                .. attribute:: address_family  (key)
                
                	Address Family
                	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                
                .. attribute:: discovery_transport_address
                
                	This is the Discovery transport address
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: is_accepting_targeted_hellos
                
                	Accepting targeted Hellos
                	**type**\: bool
                
                .. attribute:: targeted_hello_filter
                
                	This contains the filter name for targeted hellos. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter, self).__init__()

                    self.yang_name = "address-family-parameter"
                    self.yang_parent_name = "parameters"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['address_family']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('address_family', YLeaf(YType.enumeration, 'address-family')),
                        ('discovery_transport_address', YLeaf(YType.str, 'discovery-transport-address')),
                        ('is_accepting_targeted_hellos', YLeaf(YType.boolean, 'is-accepting-targeted-hellos')),
                        ('targeted_hello_filter', YLeaf(YType.str, 'targeted-hello-filter')),
                    ])
                    self.address_family = None
                    self.discovery_transport_address = None
                    self.is_accepting_targeted_hellos = None
                    self.targeted_hello_filter = None
                    self._segment_path = lambda: "address-family-parameter" + "[address-family='" + str(self.address_family) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/parameters/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter, ['address_family', 'discovery_transport_address', 'is_accepting_targeted_hellos', 'targeted_hello_filter'], name, value)


        class Capabilities(Entity):
            """
            LDP capability database information
            
            .. attribute:: capability
            
            	Information on LDP capability
            	**type**\: list of  		 :py:class:`Capability <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Capabilities.Capability>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Capabilities, self).__init__()

                self.yang_name = "capabilities"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("capability", ("capability", MplsLdp.MplsLdpState.Capabilities.Capability))])
                self._leafs = OrderedDict()

                self.capability = YList(self)
                self._segment_path = lambda: "capabilities"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.Capabilities, [], name, value)


            class Capability(Entity):
                """
                Information on LDP capability
                
                .. attribute:: cap_type  (key)
                
                	Capability type (IANA assigned)
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: capability_owner
                
                	Capability owner
                	**type**\: str
                
                .. attribute:: cap_des
                
                	Capability description
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: capability_data_length
                
                	Capability data length
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: capability_data
                
                	Capability data
                	**type**\: str
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Capabilities.Capability, self).__init__()

                    self.yang_name = "capability"
                    self.yang_parent_name = "capabilities"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['cap_type']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('cap_type', YLeaf(YType.uint16, 'cap-type')),
                        ('capability_owner', YLeaf(YType.str, 'capability-owner')),
                        ('cap_des', YLeaf(YType.str, 'cap-des')),
                        ('capability_data_length', YLeaf(YType.uint16, 'capability-data-length')),
                        ('capability_data', YLeaf(YType.str, 'capability-data')),
                    ])
                    self.cap_type = None
                    self.capability_owner = None
                    self.cap_des = None
                    self.capability_data_length = None
                    self.capability_data = None
                    self._segment_path = lambda: "capability" + "[cap-type='" + str(self.cap_type) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/capabilities/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Capabilities.Capability, ['cap_type', 'capability_owner', 'cap_des', 'capability_data_length', 'capability_data'], name, value)


        class BackoffParameters(Entity):
            """
            MPLS LDP Session Backoff Information
            
            .. attribute:: initial_seconds
            
            	Initial backoff value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: maximum_seconds
            
            	Maximum backoff value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: backoff_seconds
            
            	Current backoff seconds count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: waiting_seconds
            
            	Current backoff waiting seconds count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.BackoffParameters, self).__init__()

                self.yang_name = "backoff-parameters"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('initial_seconds', YLeaf(YType.uint32, 'initial-seconds')),
                    ('maximum_seconds', YLeaf(YType.uint32, 'maximum-seconds')),
                    ('backoff_seconds', YLeaf(YType.uint32, 'backoff-seconds')),
                    ('waiting_seconds', YLeaf(YType.uint32, 'waiting-seconds')),
                ])
                self.initial_seconds = None
                self.maximum_seconds = None
                self.backoff_seconds = None
                self.waiting_seconds = None
                self._segment_path = lambda: "backoff-parameters"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.BackoffParameters, ['initial_seconds', 'maximum_seconds', 'backoff_seconds', 'waiting_seconds'], name, value)


        class GracefulRestart(Entity):
            """
            MPLS LDP Graceful Restart Information
            
            .. attribute:: is_graceful_restart_configured
            
            	Is graceful restart configured
            	**type**\: bool
            
            .. attribute:: graceful_restart_reconnect_timeout
            
            	Reconnect timeout value in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: graceful_restart_forwarding_state_hold_time
            
            	Graceful restart forward state hold time in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: is_forwarding_state_hold_timer_running
            
            	Is graceful restart forwarding state hold timer running
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: forwarding_state_hold_timer_remaining_seconds
            
            	Forwarding state hold timer remaining time in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_graceful_restart_configured', YLeaf(YType.boolean, 'is-graceful-restart-configured')),
                    ('graceful_restart_reconnect_timeout', YLeaf(YType.uint32, 'graceful-restart-reconnect-timeout')),
                    ('graceful_restart_forwarding_state_hold_time', YLeaf(YType.uint32, 'graceful-restart-forwarding-state-hold-time')),
                    ('is_forwarding_state_hold_timer_running', YLeaf(YType.empty, 'is-forwarding-state-hold-timer-running')),
                    ('forwarding_state_hold_timer_remaining_seconds', YLeaf(YType.uint32, 'forwarding-state-hold-timer-remaining-seconds')),
                ])
                self.is_graceful_restart_configured = None
                self.graceful_restart_reconnect_timeout = None
                self.graceful_restart_forwarding_state_hold_time = None
                self.is_forwarding_state_hold_timer_running = None
                self.forwarding_state_hold_timer_remaining_seconds = None
                self._segment_path = lambda: "graceful-restart"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.GracefulRestart, ['is_graceful_restart_configured', 'graceful_restart_reconnect_timeout', 'graceful_restart_forwarding_state_hold_time', 'is_forwarding_state_hold_timer_running', 'forwarding_state_hold_timer_remaining_seconds'], name, value)


        class Vrfs(Entity):
            """
            MPLS LDP per\-VRF operational data.
            
            .. attribute:: vrf
            
            	MPLS LDP Operational data for a given VRF
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("vrf", ("vrf", MplsLdp.MplsLdpState.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                MPLS LDP Operational data for a given VRF.
                
                .. attribute:: vrf_name  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: vrf_summary
                
                	MPLS LDP per VRF summarized Information
                	**type**\:  :py:class:`VrfSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary>`
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_container_classes = OrderedDict([("vrf-summary", ("vrf_summary", MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary)), ("afs", ("afs", MplsLdp.MplsLdpState.Vrfs.Vrf.Afs))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ])
                    self.vrf_name = None

                    self.vrf_summary = MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary()
                    self.vrf_summary.parent = self
                    self._children_name_map["vrf_summary"] = "vrf-summary"
                    self._children_yang_names.add("vrf-summary")

                    self.afs = MplsLdp.MplsLdpState.Vrfs.Vrf.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                    self._children_yang_names.add("afs")
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/vrfs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf, ['vrf_name'], name, value)


                class VrfSummary(Entity):
                    """
                    MPLS LDP per VRF summarized Information
                    
                    .. attribute:: address_families
                    
                    	Address Families enabled
                    	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                    
                    .. attribute:: number_of_neighbors
                    
                    	Number of neighbor
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_graceful_restart_neighbors
                    
                    	Number of Graceful Restart neighbor
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_downstream_on_demand_neighbors
                    
                    	Number of Downstream\-On\-Demand neighbor
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: numberof_ipv4_hello_adj
                    
                    	Number of LDP discovery IPv4 hello adjacencies
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ipv4_routes
                    
                    	Number of resolved IPv4 routes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ipv4_local_addresses
                    
                    	Number of IPv4 local addresses
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ldp_interfaces
                    
                    	Number of LDP configured interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ipv4ldp_interfaces
                    
                    	Number of LDP IPv4 configured interfaces
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary, self).__init__()

                        self.yang_name = "vrf-summary"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address_families', YLeaf(YType.enumeration, 'address-families')),
                            ('number_of_neighbors', YLeaf(YType.uint32, 'number-of-neighbors')),
                            ('number_of_graceful_restart_neighbors', YLeaf(YType.uint32, 'number-of-graceful-restart-neighbors')),
                            ('number_of_downstream_on_demand_neighbors', YLeaf(YType.uint32, 'number-of-downstream-on-demand-neighbors')),
                            ('numberof_ipv4_hello_adj', YLeaf(YType.uint32, 'numberof-ipv4-hello-adj')),
                            ('number_of_ipv4_routes', YLeaf(YType.uint32, 'number-of-ipv4-routes')),
                            ('number_of_ipv4_local_addresses', YLeaf(YType.uint32, 'number-of-ipv4-local-addresses')),
                            ('number_of_ldp_interfaces', YLeaf(YType.uint32, 'number-of-ldp-interfaces')),
                            ('number_of_ipv4ldp_interfaces', YLeaf(YType.uint32, 'number-of-ipv4ldp-interfaces')),
                        ])
                        self.address_families = None
                        self.number_of_neighbors = None
                        self.number_of_graceful_restart_neighbors = None
                        self.number_of_downstream_on_demand_neighbors = None
                        self.numberof_ipv4_hello_adj = None
                        self.number_of_ipv4_routes = None
                        self.number_of_ipv4_local_addresses = None
                        self.number_of_ldp_interfaces = None
                        self.number_of_ipv4ldp_interfaces = None
                        self._segment_path = lambda: "vrf-summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary, ['address_families', 'number_of_neighbors', 'number_of_graceful_restart_neighbors', 'number_of_downstream_on_demand_neighbors', 'numberof_ipv4_hello_adj', 'number_of_ipv4_routes', 'number_of_ipv4_local_addresses', 'number_of_ldp_interfaces', 'number_of_ipv4ldp_interfaces'], name, value)


                class Afs(Entity):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	MPLS LDP Operational data for this Address Family
                    	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs, self).__init__()

                        self.yang_name = "afs"
                        self.yang_parent_name = "vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("af", ("af", MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af))])
                        self._leafs = OrderedDict()

                        self.af = YList(self)
                        self._segment_path = lambda: "afs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs, [], name, value)


                    class Af(Entity):
                        """
                        MPLS LDP Operational data for this Address Family.
                        
                        .. attribute:: af_name  (key)
                        
                        	Address Family name
                        	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                        
                        .. attribute:: interface_summary
                        
                        	This container holds a summary of information across all interfaces in this AF,
                        	**type**\:  :py:class:`InterfaceSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary>`
                        
                        .. attribute:: igp
                        
                        	LDP IGP Synchronization related information
                        	**type**\:  :py:class:`Igp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af, self).__init__()

                            self.yang_name = "af"
                            self.yang_parent_name = "afs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['af_name']
                            self._child_container_classes = OrderedDict([("interface-summary", ("interface_summary", MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary)), ("igp", ("igp", MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                            ])
                            self.af_name = None

                            self.interface_summary = MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary()
                            self.interface_summary.parent = self
                            self._children_name_map["interface_summary"] = "interface-summary"
                            self._children_yang_names.add("interface-summary")

                            self.igp = MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp()
                            self.igp.parent = self
                            self._children_name_map["igp"] = "igp"
                            self._children_yang_names.add("igp")
                            self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af, ['af_name'], name, value)


                        class InterfaceSummary(Entity):
                            """
                            This container holds a summary of information
                            across all interfaces in this AF,
                            
                            .. attribute:: known_ip_interface_count
                            
                            	Number of known IP Interfaces
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: known_ip_interface_ldp_enabled
                            
                            	Number of known IP Interfaces with LDP Enabled
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: configured_attached_interface
                            
                            	Number of attached interfaces configured in LDP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: configured_te_interface
                            
                            	Number of TE tunnel interfaces configured in LDP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: forward_references
                            
                            	Number of forward referenced interfaces
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: auto_config_disabled
                            
                            	Autoconfigure disabled
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: auto_config
                            
                            	Auto\-configured interfaces
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: auto_config_forward_reference_interfaces
                            
                            	Auto\-configured forward references
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary, self).__init__()

                                self.yang_name = "interface-summary"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('known_ip_interface_count', YLeaf(YType.uint32, 'known-ip-interface-count')),
                                    ('known_ip_interface_ldp_enabled', YLeaf(YType.uint32, 'known-ip-interface-ldp-enabled')),
                                    ('configured_attached_interface', YLeaf(YType.uint32, 'configured-attached-interface')),
                                    ('configured_te_interface', YLeaf(YType.uint32, 'configured-te-interface')),
                                    ('forward_references', YLeaf(YType.uint32, 'forward-references')),
                                    ('auto_config_disabled', YLeaf(YType.uint32, 'auto-config-disabled')),
                                    ('auto_config', YLeaf(YType.uint32, 'auto-config')),
                                    ('auto_config_forward_reference_interfaces', YLeaf(YType.uint32, 'auto-config-forward-reference-interfaces')),
                                ])
                                self.known_ip_interface_count = None
                                self.known_ip_interface_ldp_enabled = None
                                self.configured_attached_interface = None
                                self.configured_te_interface = None
                                self.forward_references = None
                                self.auto_config_disabled = None
                                self.auto_config = None
                                self.auto_config_forward_reference_interfaces = None
                                self._segment_path = lambda: "interface-summary"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary, ['known_ip_interface_count', 'known_ip_interface_ldp_enabled', 'configured_attached_interface', 'configured_te_interface', 'forward_references', 'auto_config_disabled', 'auto_config', 'auto_config_forward_reference_interfaces'], name, value)


                        class Igp(Entity):
                            """
                            LDP IGP Synchronization related information
                            
                            .. attribute:: sync
                            
                            	LDP\-IGP Synchronization related information for an interface
                            	**type**\: list of  		 :py:class:`Sync <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("sync", ("sync", MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync))])
                                self._leafs = OrderedDict()

                                self.sync = YList(self)
                                self._segment_path = lambda: "igp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp, [], name, value)


                            class Sync(Entity):
                                """
                                LDP\-IGP Synchronization related information
                                for an interface
                                
                                .. attribute:: interface  (key)
                                
                                	This leaf contains the interface name for the IGP Synchronization information
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: igp_sync_state
                                
                                	IGP Sync state
                                	**type**\:  :py:class:`IgpSyncState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IgpSyncState>`
                                
                                .. attribute:: is_delay_timer_running
                                
                                	This is set when the sync delay timer running
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: delay_timer_remaining
                                
                                	Remaining timer (seconds) until expiry of sync delay timer
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: seconds
                                
                                .. attribute:: igp_sync_down_reason
                                
                                	Reason IGP Sync Not Achieved
                                	**type**\:  :py:class:`IgpSyncDownReason <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IgpSyncDownReason>`
                                
                                .. attribute:: peers
                                
                                	MPLS LDP IGP Sync Interface Peer Information
                                	**type**\: list of  		 :py:class:`Peers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    super(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync, self).__init__()

                                    self.yang_name = "sync"
                                    self.yang_parent_name = "igp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("peers", ("peers", MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers))])
                                    self._leafs = OrderedDict([
                                        ('interface', YLeaf(YType.str, 'interface')),
                                        ('igp_sync_state', YLeaf(YType.enumeration, 'igp-sync-state')),
                                        ('is_delay_timer_running', YLeaf(YType.empty, 'is-delay-timer-running')),
                                        ('delay_timer_remaining', YLeaf(YType.uint32, 'delay-timer-remaining')),
                                        ('igp_sync_down_reason', YLeaf(YType.identityref, 'igp-sync-down-reason')),
                                    ])
                                    self.interface = None
                                    self.igp_sync_state = None
                                    self.is_delay_timer_running = None
                                    self.delay_timer_remaining = None
                                    self.igp_sync_down_reason = None

                                    self.peers = YList(self)
                                    self._segment_path = lambda: "sync" + "[interface='" + str(self.interface) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync, ['interface', 'igp_sync_state', 'is_delay_timer_running', 'delay_timer_remaining', 'igp_sync_down_reason'], name, value)


                                class Peers(Entity):
                                    """
                                    MPLS LDP IGP Sync Interface Peer Information
                                    
                                    .. attribute:: peer_id
                                    
                                    	Peer Identifier
                                    	**type**\: str
                                    
                                    .. attribute:: is_gr_enabled
                                    
                                    	Is GR enabled session
                                    	**type**\: bool
                                    
                                    .. attribute:: is_chkpt_created
                                    
                                    	This is set if this peer was created due to check\-pointing
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-ios-xe-oper'
                                    _revision = '2017-02-07'

                                    def __init__(self):
                                        super(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers, self).__init__()

                                        self.yang_name = "peers"
                                        self.yang_parent_name = "sync"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('peer_id', YLeaf(YType.str, 'peer-id')),
                                            ('is_gr_enabled', YLeaf(YType.boolean, 'is-gr-enabled')),
                                            ('is_chkpt_created', YLeaf(YType.empty, 'is-chkpt-created')),
                                        ])
                                        self.peer_id = None
                                        self.is_gr_enabled = None
                                        self.is_chkpt_created = None
                                        self._segment_path = lambda: "peers"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers, ['peer_id', 'is_gr_enabled', 'is_chkpt_created'], name, value)


        class Discovery(Entity):
            """
            The LDP Discovery operational state
            
            .. attribute:: discovery_stats
            
            	MPLS LDP Discovery Summary Information
            	**type**\:  :py:class:`DiscoveryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.DiscoveryStats>`
            
            .. attribute:: link_hello_state
            
            	This container holds information for LDP Discovery using non\-targeted Hellos. These are interface\-based hellos which form one or more adjacencies for each interface and also form adjacencies on multiple intefrfaces. Link Hellos can therefore form multiple adjacencies with the same peer
            	**type**\:  :py:class:`LinkHelloState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.LinkHelloState>`
            
            .. attribute:: targeted_hellos
            
            	The LDP Discovery Targeted Hello state
            	**type**\:  :py:class:`TargetedHellos <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.TargetedHellos>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Discovery, self).__init__()

                self.yang_name = "discovery"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("discovery-stats", ("discovery_stats", MplsLdp.MplsLdpState.Discovery.DiscoveryStats)), ("link-hello-state", ("link_hello_state", MplsLdp.MplsLdpState.Discovery.LinkHelloState)), ("targeted-hellos", ("targeted_hellos", MplsLdp.MplsLdpState.Discovery.TargetedHellos))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.discovery_stats = MplsLdp.MplsLdpState.Discovery.DiscoveryStats()
                self.discovery_stats.parent = self
                self._children_name_map["discovery_stats"] = "discovery-stats"
                self._children_yang_names.add("discovery-stats")

                self.link_hello_state = MplsLdp.MplsLdpState.Discovery.LinkHelloState()
                self.link_hello_state.parent = self
                self._children_name_map["link_hello_state"] = "link-hello-state"
                self._children_yang_names.add("link-hello-state")

                self.targeted_hellos = MplsLdp.MplsLdpState.Discovery.TargetedHellos()
                self.targeted_hellos.parent = self
                self._children_name_map["targeted_hellos"] = "targeted-hellos"
                self._children_yang_names.add("targeted-hellos")
                self._segment_path = lambda: "discovery"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()


            class DiscoveryStats(Entity):
                """
                MPLS LDP Discovery Summary Information
                
                .. attribute:: num_of_ldp_interfaces
                
                	Total Number of LDP configured interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_active_ldp_interfaces
                
                	Number of active LDP enabled interfaces
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_lnk_disc_xmit
                
                	Number of link hello discoveries in xmit state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_tgt_disc_xmit
                
                	Number of targeted hello discoveries in xmit state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_lnk_disc_recv
                
                	Number of link hello discoveries in recv state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_tgt_disc_recv
                
                	Number of targeted hello discoveries in recv state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Discovery.DiscoveryStats, self).__init__()

                    self.yang_name = "discovery-stats"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('num_of_ldp_interfaces', YLeaf(YType.uint32, 'num-of-ldp-interfaces')),
                        ('num_of_active_ldp_interfaces', YLeaf(YType.uint32, 'num-of-active-ldp-interfaces')),
                        ('num_of_lnk_disc_xmit', YLeaf(YType.uint32, 'num-of-lnk-disc-xmit')),
                        ('num_of_tgt_disc_xmit', YLeaf(YType.uint32, 'num-of-tgt-disc-xmit')),
                        ('num_of_lnk_disc_recv', YLeaf(YType.uint32, 'num-of-lnk-disc-recv')),
                        ('num_of_tgt_disc_recv', YLeaf(YType.uint32, 'num-of-tgt-disc-recv')),
                    ])
                    self.num_of_ldp_interfaces = None
                    self.num_of_active_ldp_interfaces = None
                    self.num_of_lnk_disc_xmit = None
                    self.num_of_tgt_disc_xmit = None
                    self.num_of_lnk_disc_recv = None
                    self.num_of_tgt_disc_recv = None
                    self._segment_path = lambda: "discovery-stats"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Discovery.DiscoveryStats, ['num_of_ldp_interfaces', 'num_of_active_ldp_interfaces', 'num_of_lnk_disc_xmit', 'num_of_tgt_disc_xmit', 'num_of_lnk_disc_recv', 'num_of_tgt_disc_recv'], name, value)


            class LinkHelloState(Entity):
                """
                This container holds information for LDP Discovery
                using non\-targeted Hellos. These are interface\-based
                hellos which form one or more adjacencies for each
                interface and also form adjacencies on multiple
                intefrfaces. Link Hellos can therefore form multiple
                adjacencies with the same peer.
                
                .. attribute:: link_hellos
                
                	Each entry represents a single LDP Hello Adjacency. An LDP Session can have one or more Hello Adjacencies
                	**type**\: list of  		 :py:class:`LinkHellos <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Discovery.LinkHelloState, self).__init__()

                    self.yang_name = "link-hello-state"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("link-hellos", ("link_hellos", MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos))])
                    self._leafs = OrderedDict()

                    self.link_hellos = YList(self)
                    self._segment_path = lambda: "link-hello-state"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Discovery.LinkHelloState, [], name, value)


                class LinkHellos(Entity):
                    """
                    Each entry represents a single LDP Hello Adjacency.
                    An LDP Session can have one or more Hello
                    Adjacencies.
                    
                    .. attribute:: interface  (key)
                    
                    	The Discovery Interface
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: nbr_transport_addr  (key)
                    
                    	This is the MPLS LDP Hello Neighbor transport address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds. This is the value used to send hello messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: local_src_addr
                    
                    	MPLS LDP Discovery Local source address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: local_transport_addr
                    
                    	MPLS LDP Discovery Local transport address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: nbr_src_addr
                    
                    	This is the MPLS LDP Hello Neighbor source address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: nbr_ldp_id
                    
                    	Neighbor LDP Identifier
                    	**type**\: str
                    
                    .. attribute:: session_up
                    
                    	Set when the session is up for this adjacency
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: nbr_hold_time
                    
                    	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the EntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: next_hello
                    
                    	Next hello due time in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: hold_time_remaining
                    
                    	This is the MPLS LDP Hello Discovery expiry time in seconds. If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**units**\: seconds
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos, self).__init__()

                        self.yang_name = "link-hellos"
                        self.yang_parent_name = "link-hello-state"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface','nbr_transport_addr']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('nbr_transport_addr', YLeaf(YType.str, 'nbr-transport-addr')),
                            ('hello_interval', YLeaf(YType.uint32, 'hello-interval')),
                            ('local_src_addr', YLeaf(YType.str, 'local-src-addr')),
                            ('local_transport_addr', YLeaf(YType.str, 'local-transport-addr')),
                            ('nbr_src_addr', YLeaf(YType.str, 'nbr-src-addr')),
                            ('nbr_ldp_id', YLeaf(YType.str, 'nbr-ldp-id')),
                            ('session_up', YLeaf(YType.empty, 'session-up')),
                            ('nbr_hold_time', YLeaf(YType.uint32, 'nbr-hold-time')),
                            ('next_hello', YLeaf(YType.uint32, 'next-hello')),
                            ('hold_time_remaining', YLeaf(YType.uint32, 'hold-time-remaining')),
                        ])
                        self.interface = None
                        self.nbr_transport_addr = None
                        self.hello_interval = None
                        self.local_src_addr = None
                        self.local_transport_addr = None
                        self.nbr_src_addr = None
                        self.nbr_ldp_id = None
                        self.session_up = None
                        self.nbr_hold_time = None
                        self.next_hello = None
                        self.hold_time_remaining = None
                        self._segment_path = lambda: "link-hellos" + "[interface='" + str(self.interface) + "']" + "[nbr-transport-addr='" + str(self.nbr_transport_addr) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/discovery/link-hello-state/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos, ['interface', 'nbr_transport_addr', 'hello_interval', 'local_src_addr', 'local_transport_addr', 'nbr_src_addr', 'nbr_ldp_id', 'session_up', 'nbr_hold_time', 'next_hello', 'hold_time_remaining'], name, value)


            class TargetedHellos(Entity):
                """
                The LDP Discovery Targeted Hello state.
                
                .. attribute:: targeted_hello_interval
                
                	Local Targeted Hello interval in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: targeted_hello_hold_time
                
                	Local Targeted hold time in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: targeted_hello
                
                	The LDP targeted discovery information for a specific target. Targetted discovery creates a single adjacency between two addresses and not indiviual adjacencies across physical interfaces
                	**type**\: list of  		 :py:class:`TargetedHello <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Discovery.TargetedHellos, self).__init__()

                    self.yang_name = "targeted-hellos"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("targeted-hello", ("targeted_hello", MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello))])
                    self._leafs = OrderedDict([
                        ('targeted_hello_interval', YLeaf(YType.uint32, 'targeted-hello-interval')),
                        ('targeted_hello_hold_time', YLeaf(YType.uint32, 'targeted-hello-hold-time')),
                    ])
                    self.targeted_hello_interval = None
                    self.targeted_hello_hold_time = None

                    self.targeted_hello = YList(self)
                    self._segment_path = lambda: "targeted-hellos"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Discovery.TargetedHellos, ['targeted_hello_interval', 'targeted_hello_hold_time'], name, value)


                class TargetedHello(Entity):
                    """
                    The LDP targeted discovery information for a specific
                    target. Targetted discovery creates a single adjacency
                    between two addresses and not indiviual adjacencies
                    across physical interfaces.
                    
                    .. attribute:: vrf_name  (key)
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\: str
                    
                    .. attribute:: target_address  (key)
                    
                    	The target IP Address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: local_address
                    
                    	Local IP Address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: neighbor_ldp_identifier
                    
                    	Neighbor LDP Identifier
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	This is the MPLS LDP Targeted Hello state
                    	**type**\:  :py:class:`DhcState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.DhcState>`
                    
                    .. attribute:: nbr_hold_time
                    
                    	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the EntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: next_hello
                    
                    	Next hello due time in milliseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: hold_time_remaining
                    
                    	This is the MPLS LDP Hello Discovery expiry time in seconds. If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**units**\: seconds
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello, self).__init__()

                        self.yang_name = "targeted-hello"
                        self.yang_parent_name = "targeted-hellos"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name','target_address']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ('target_address', YLeaf(YType.str, 'target-address')),
                            ('local_address', YLeaf(YType.str, 'local-address')),
                            ('neighbor_ldp_identifier', YLeaf(YType.str, 'neighbor-ldp-identifier')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('nbr_hold_time', YLeaf(YType.uint32, 'nbr-hold-time')),
                            ('next_hello', YLeaf(YType.uint32, 'next-hello')),
                            ('hold_time_remaining', YLeaf(YType.uint32, 'hold-time-remaining')),
                        ])
                        self.vrf_name = None
                        self.target_address = None
                        self.local_address = None
                        self.neighbor_ldp_identifier = None
                        self.state = None
                        self.nbr_hold_time = None
                        self.next_hello = None
                        self.hold_time_remaining = None
                        self._segment_path = lambda: "targeted-hello" + "[vrf-name='" + str(self.vrf_name) + "']" + "[target-address='" + str(self.target_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/discovery/targeted-hellos/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello, ['vrf_name', 'target_address', 'local_address', 'neighbor_ldp_identifier', 'state', 'nbr_hold_time', 'next_hello', 'hold_time_remaining'], name, value)


        class Forwarding(Entity):
            """
            Summary information regarding LDP forwarding
            setup and detailed LDP Forwarding rewrites
            
            .. attribute:: forwarding_vrf_summs
            
            	Summary of forwarding info for this VRF
            	**type**\:  :py:class:`ForwardingVrfSumms <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms>`
            
            .. attribute:: forwarding_detail
            
            	This leaf contain the individual LDP forwarding rewrite for a single prefix
            	**type**\: list of  		 :py:class:`ForwardingDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Forwarding, self).__init__()

                self.yang_name = "forwarding"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("forwarding-vrf-summs", ("forwarding_vrf_summs", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms))])
                self._child_list_classes = OrderedDict([("forwarding-detail", ("forwarding_detail", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail))])
                self._leafs = OrderedDict()

                self.forwarding_vrf_summs = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms()
                self.forwarding_vrf_summs.parent = self
                self._children_name_map["forwarding_vrf_summs"] = "forwarding-vrf-summs"
                self._children_yang_names.add("forwarding-vrf-summs")

                self.forwarding_detail = YList(self)
                self._segment_path = lambda: "forwarding"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.Forwarding, [], name, value)


            class ForwardingVrfSumms(Entity):
                """
                Summary of forwarding info for this VRF.
                
                .. attribute:: forwarding_vrf_summ
                
                	Summary of forwarding info for this VRF
                	**type**\: list of  		 :py:class:`ForwardingVrfSumm <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms, self).__init__()

                    self.yang_name = "forwarding-vrf-summs"
                    self.yang_parent_name = "forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("forwarding-vrf-summ", ("forwarding_vrf_summ", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm))])
                    self._leafs = OrderedDict()

                    self.forwarding_vrf_summ = YList(self)
                    self._segment_path = lambda: "forwarding-vrf-summs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms, [], name, value)


                class ForwardingVrfSumm(Entity):
                    """
                    Summary of forwarding info for this VRF.
                    
                    .. attribute:: vrf_name  (key)
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\: str
                    
                    .. attribute:: pfxs
                    
                    	MPLS LDP forwarding prefix rewrite summary
                    	**type**\:  :py:class:`Pfxs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs>`
                    
                    .. attribute:: nhs
                    
                    	MPLS LDP forwarding rewrite next\-hop/path summary
                    	**type**\:  :py:class:`Nhs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs>`
                    
                    .. attribute:: intfs_fwd_count
                    
                    	MPLS forwarding enabled interface count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_lbls
                    
                    	Local label allocated count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm, self).__init__()

                        self.yang_name = "forwarding-vrf-summ"
                        self.yang_parent_name = "forwarding-vrf-summs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name']
                        self._child_container_classes = OrderedDict([("pfxs", ("pfxs", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs)), ("nhs", ("nhs", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ('intfs_fwd_count', YLeaf(YType.uint16, 'intfs-fwd-count')),
                            ('local_lbls', YLeaf(YType.uint16, 'local-lbls')),
                        ])
                        self.vrf_name = None
                        self.intfs_fwd_count = None
                        self.local_lbls = None

                        self.pfxs = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs()
                        self.pfxs.parent = self
                        self._children_name_map["pfxs"] = "pfxs"
                        self._children_yang_names.add("pfxs")

                        self.nhs = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs()
                        self.nhs.parent = self
                        self._children_name_map["nhs"] = "nhs"
                        self._children_yang_names.add("nhs")
                        self._segment_path = lambda: "forwarding-vrf-summ" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding/forwarding-vrf-summs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm, ['vrf_name', 'intfs_fwd_count', 'local_lbls'], name, value)


                    class Pfxs(Entity):
                        """
                        MPLS LDP forwarding prefix rewrite summary
                        
                        .. attribute:: labeled_pfxs_aggr
                        
                        	Labeled prefix count for all paths
                        	**type**\:  :py:class:`LabeledPfxsAggr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr>`
                        
                        .. attribute:: labeled_pfxs_primary
                        
                        	Labeled prefix count related to primary paths only
                        	**type**\:  :py:class:`LabeledPfxsPrimary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary>`
                        
                        .. attribute:: labeled_pfxs_backup
                        
                        	Labeled prefix count related to backup paths only
                        	**type**\:  :py:class:`LabeledPfxsBackup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup>`
                        
                        .. attribute:: total_pfxs
                        
                        	Total Prefix count
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: ecmp_pfxs
                        
                        	Count of prefixes with ECMP
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: protected_pfxs
                        
                        	Count of FRR protected prefixes
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs, self).__init__()

                            self.yang_name = "pfxs"
                            self.yang_parent_name = "forwarding-vrf-summ"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("labeled-pfxs-aggr", ("labeled_pfxs_aggr", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr)), ("labeled-pfxs-primary", ("labeled_pfxs_primary", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary)), ("labeled-pfxs-backup", ("labeled_pfxs_backup", MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('total_pfxs', YLeaf(YType.uint16, 'total-pfxs')),
                                ('ecmp_pfxs', YLeaf(YType.uint16, 'ecmp-pfxs')),
                                ('protected_pfxs', YLeaf(YType.uint16, 'protected-pfxs')),
                            ])
                            self.total_pfxs = None
                            self.ecmp_pfxs = None
                            self.protected_pfxs = None

                            self.labeled_pfxs_aggr = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr()
                            self.labeled_pfxs_aggr.parent = self
                            self._children_name_map["labeled_pfxs_aggr"] = "labeled-pfxs-aggr"
                            self._children_yang_names.add("labeled-pfxs-aggr")

                            self.labeled_pfxs_primary = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary()
                            self.labeled_pfxs_primary.parent = self
                            self._children_name_map["labeled_pfxs_primary"] = "labeled-pfxs-primary"
                            self._children_yang_names.add("labeled-pfxs-primary")

                            self.labeled_pfxs_backup = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup()
                            self.labeled_pfxs_backup.parent = self
                            self._children_name_map["labeled_pfxs_backup"] = "labeled-pfxs-backup"
                            self._children_yang_names.add("labeled-pfxs-backup")
                            self._segment_path = lambda: "pfxs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs, ['total_pfxs', 'ecmp_pfxs', 'protected_pfxs'], name, value)


                        class LabeledPfxsAggr(Entity):
                            """
                            Labeled prefix count for all paths
                            
                            .. attribute:: labeled_pfxs
                            
                            	Count of labeled prefixes with 1 or more paths labeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: labeled_pfxs_partial
                            
                            	Count of labeled prefixes with some (but not ALL) paths labeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: unlabeled_pfxs
                            
                            	Count of labeled prefixes with ALL paths unlabeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr, self).__init__()

                                self.yang_name = "labeled-pfxs-aggr"
                                self.yang_parent_name = "pfxs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('labeled_pfxs', YLeaf(YType.uint16, 'labeled-pfxs')),
                                    ('labeled_pfxs_partial', YLeaf(YType.uint16, 'labeled-pfxs-partial')),
                                    ('unlabeled_pfxs', YLeaf(YType.uint16, 'unlabeled-pfxs')),
                                ])
                                self.labeled_pfxs = None
                                self.labeled_pfxs_partial = None
                                self.unlabeled_pfxs = None
                                self._segment_path = lambda: "labeled-pfxs-aggr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr, ['labeled_pfxs', 'labeled_pfxs_partial', 'unlabeled_pfxs'], name, value)


                        class LabeledPfxsPrimary(Entity):
                            """
                            Labeled prefix count related to primary paths
                            only
                            
                            .. attribute:: labeled_pfxs
                            
                            	Count of labeled prefixes with 1 or more paths labeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: labeled_pfxs_partial
                            
                            	Count of labeled prefixes with some (but not ALL) paths labeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: unlabeled_pfxs
                            
                            	Count of labeled prefixes with ALL paths unlabeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary, self).__init__()

                                self.yang_name = "labeled-pfxs-primary"
                                self.yang_parent_name = "pfxs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('labeled_pfxs', YLeaf(YType.uint16, 'labeled-pfxs')),
                                    ('labeled_pfxs_partial', YLeaf(YType.uint16, 'labeled-pfxs-partial')),
                                    ('unlabeled_pfxs', YLeaf(YType.uint16, 'unlabeled-pfxs')),
                                ])
                                self.labeled_pfxs = None
                                self.labeled_pfxs_partial = None
                                self.unlabeled_pfxs = None
                                self._segment_path = lambda: "labeled-pfxs-primary"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary, ['labeled_pfxs', 'labeled_pfxs_partial', 'unlabeled_pfxs'], name, value)


                        class LabeledPfxsBackup(Entity):
                            """
                            Labeled prefix count related to backup paths
                            only
                            
                            .. attribute:: labeled_pfxs
                            
                            	Count of labeled prefixes with 1 or more paths labeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: labeled_pfxs_partial
                            
                            	Count of labeled prefixes with some (but not ALL) paths labeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: unlabeled_pfxs
                            
                            	Count of labeled prefixes with ALL paths unlabeled
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup, self).__init__()

                                self.yang_name = "labeled-pfxs-backup"
                                self.yang_parent_name = "pfxs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('labeled_pfxs', YLeaf(YType.uint16, 'labeled-pfxs')),
                                    ('labeled_pfxs_partial', YLeaf(YType.uint16, 'labeled-pfxs-partial')),
                                    ('unlabeled_pfxs', YLeaf(YType.uint16, 'unlabeled-pfxs')),
                                ])
                                self.labeled_pfxs = None
                                self.labeled_pfxs_partial = None
                                self.unlabeled_pfxs = None
                                self._segment_path = lambda: "labeled-pfxs-backup"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup, ['labeled_pfxs', 'labeled_pfxs_partial', 'unlabeled_pfxs'], name, value)


                    class Nhs(Entity):
                        """
                        MPLS LDP forwarding rewrite next\-hop/path summary
                        
                        .. attribute:: total_paths
                        
                        	Total path count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protected_paths
                        
                        	Count of FRR protected paths
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: backup_paths
                        
                        	Count of non\-primary backup paths
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_backup_paths
                        
                        	Count of non\-primary remote backup paths
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: labeled_paths
                        
                        	Count of all labeled paths
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: labeled_backup_paths
                        
                        	Count of labeled backup paths
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs, self).__init__()

                            self.yang_name = "nhs"
                            self.yang_parent_name = "forwarding-vrf-summ"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('total_paths', YLeaf(YType.uint32, 'total-paths')),
                                ('protected_paths', YLeaf(YType.uint32, 'protected-paths')),
                                ('backup_paths', YLeaf(YType.uint32, 'backup-paths')),
                                ('remote_backup_paths', YLeaf(YType.uint32, 'remote-backup-paths')),
                                ('labeled_paths', YLeaf(YType.uint32, 'labeled-paths')),
                                ('labeled_backup_paths', YLeaf(YType.uint32, 'labeled-backup-paths')),
                            ])
                            self.total_paths = None
                            self.protected_paths = None
                            self.backup_paths = None
                            self.remote_backup_paths = None
                            self.labeled_paths = None
                            self.labeled_backup_paths = None
                            self._segment_path = lambda: "nhs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs, ['total_paths', 'protected_paths', 'backup_paths', 'remote_backup_paths', 'labeled_paths', 'labeled_backup_paths'], name, value)


            class ForwardingDetail(Entity):
                """
                This leaf contain the individual LDP forwarding rewrite
                for a single prefix.
                
                .. attribute:: vrf_name  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: prefix  (key)
                
                	The IP Prefix
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: fwd_prefix
                
                	This is the MPLS LDP Forward IP Prefix
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: route
                
                	MPLS LDP Forwarding Route information
                	**type**\:  :py:class:`Route <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route>`
                
                .. attribute:: table_id
                
                	Table ID associated with IP prefix
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: paths
                
                	MPLS LDP Forwarding Path info
                	**type**\: list of  		 :py:class:`Paths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail, self).__init__()

                    self.yang_name = "forwarding-detail"
                    self.yang_parent_name = "forwarding"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','prefix']
                    self._child_container_classes = OrderedDict([("route", ("route", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route))])
                    self._child_list_classes = OrderedDict([("paths", ("paths", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths))])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('prefix', YLeaf(YType.str, 'prefix')),
                        ('fwd_prefix', YLeaf(YType.str, 'fwd-prefix')),
                        ('table_id', YLeaf(YType.uint32, 'table-id')),
                        ('prefix_length', YLeaf(YType.uint8, 'prefix-length')),
                    ])
                    self.vrf_name = None
                    self.prefix = None
                    self.fwd_prefix = None
                    self.table_id = None
                    self.prefix_length = None

                    self.route = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route()
                    self.route.parent = self
                    self._children_name_map["route"] = "route"
                    self._children_yang_names.add("route")

                    self.paths = YList(self)
                    self._segment_path = lambda: "forwarding-detail" + "[vrf-name='" + str(self.vrf_name) + "']" + "[prefix='" + str(self.prefix) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/forwarding/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail, ['vrf_name', 'prefix', 'fwd_prefix', 'table_id', 'prefix_length'], name, value)


                class Route(Entity):
                    """
                    MPLS LDP Forwarding Route information
                    
                    .. attribute:: version
                    
                    	Route RIB version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: priority
                    
                    	Route priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: source
                    
                    	Route source protocol Id
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: type
                    
                    	Route type
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: metric
                    
                    	Route metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_local_vrf_leaked
                    
                    	Is this route leaked across local VRFs?
                    	**type**\: bool
                    
                    .. attribute:: routing_update_count
                    
                    	Number of routing updates
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: routing_update_timestamp
                    
                    	Last Routing update nanosec timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: routing_update_age
                    
                    	Last Routing update nanosec age
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: local_label
                    
                    	Local label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forwarding_update_count
                    
                    	Number of forwarding updates
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forwarding_update_timestamp
                    
                    	Last Forwarding update nanosec timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: forwarding_update_age
                    
                    	Last Forwarding update nanosec age
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route, self).__init__()

                        self.yang_name = "route"
                        self.yang_parent_name = "forwarding-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('version', YLeaf(YType.uint32, 'version')),
                            ('priority', YLeaf(YType.uint8, 'priority')),
                            ('source', YLeaf(YType.uint16, 'source')),
                            ('type', YLeaf(YType.uint16, 'type')),
                            ('metric', YLeaf(YType.uint32, 'metric')),
                            ('is_local_vrf_leaked', YLeaf(YType.boolean, 'is-local-vrf-leaked')),
                            ('routing_update_count', YLeaf(YType.uint32, 'routing-update-count')),
                            ('routing_update_timestamp', YLeaf(YType.uint64, 'routing-update-timestamp')),
                            ('routing_update_age', YLeaf(YType.uint64, 'routing-update-age')),
                            ('local_label', YLeaf(YType.uint32, 'local-label')),
                            ('forwarding_update_count', YLeaf(YType.uint32, 'forwarding-update-count')),
                            ('forwarding_update_timestamp', YLeaf(YType.uint64, 'forwarding-update-timestamp')),
                            ('forwarding_update_age', YLeaf(YType.uint64, 'forwarding-update-age')),
                        ])
                        self.version = None
                        self.priority = None
                        self.source = None
                        self.type = None
                        self.metric = None
                        self.is_local_vrf_leaked = None
                        self.routing_update_count = None
                        self.routing_update_timestamp = None
                        self.routing_update_age = None
                        self.local_label = None
                        self.forwarding_update_count = None
                        self.forwarding_update_timestamp = None
                        self.forwarding_update_age = None
                        self._segment_path = lambda: "route"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route, ['version', 'priority', 'source', 'type', 'metric', 'is_local_vrf_leaked', 'routing_update_count', 'routing_update_timestamp', 'routing_update_age', 'local_label', 'forwarding_update_count', 'forwarding_update_timestamp', 'forwarding_update_age'], name, value)


                class Paths(Entity):
                    """
                    MPLS LDP Forwarding Path info
                    
                    .. attribute:: routing
                    
                    	MPLS LDP Forwarding Path IP Routing information
                    	**type**\:  :py:class:`Routing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing>`
                    
                    .. attribute:: mpls
                    
                    	MPLS LDP Forwarding Path MPLS information
                    	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "forwarding-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("routing", ("routing", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing)), ("mpls", ("mpls", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.routing = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing()
                        self.routing.parent = self
                        self._children_name_map["routing"] = "routing"
                        self._children_yang_names.add("routing")

                        self.mpls = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls()
                        self.mpls.parent = self
                        self._children_name_map["mpls"] = "mpls"
                        self._children_yang_names.add("mpls")
                        self._segment_path = lambda: "paths"


                    class Routing(Entity):
                        """
                        MPLS LDP Forwarding Path IP Routing information
                        
                        .. attribute:: next_hop
                        
                        	This is the Next Hop address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: remote_node_id
                        
                        	This is the Remote/PQ node address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: has_remote_lfa_bkup
                        
                        	This is true if the path has a remote LFA backup
                        	**type**\: bool
                        
                        .. attribute:: interface
                        
                        	This is the interface
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: nh_is_overriden
                        
                        	This is set when the nexthop is overriden by LDP
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: nexthop_id
                        
                        	Nexthop Identifier
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_table_id
                        
                        	Table ID for nexthop address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: load_metric
                        
                        	Path's load metric for load balancing
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_id
                        
                        	path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: bkup_path_id
                        
                        	Backup path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: path_type
                        
                        	Routing path type
                        	**type**\:  :py:class:`RoutePathType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RoutePathType>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing, self).__init__()

                            self.yang_name = "routing"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('remote_node_id', YLeaf(YType.str, 'remote-node-id')),
                                ('has_remote_lfa_bkup', YLeaf(YType.boolean, 'has-remote-lfa-bkup')),
                                ('interface', YLeaf(YType.str, 'interface')),
                                ('nh_is_overriden', YLeaf(YType.empty, 'nh-is-overriden')),
                                ('nexthop_id', YLeaf(YType.uint32, 'nexthop-id')),
                                ('next_hop_table_id', YLeaf(YType.uint32, 'next-hop-table-id')),
                                ('load_metric', YLeaf(YType.uint32, 'load-metric')),
                                ('path_id', YLeaf(YType.uint8, 'path-id')),
                                ('bkup_path_id', YLeaf(YType.uint8, 'bkup-path-id')),
                                ('path_type', YLeaf(YType.identityref, 'path-type')),
                            ])
                            self.next_hop = None
                            self.remote_node_id = None
                            self.has_remote_lfa_bkup = None
                            self.interface = None
                            self.nh_is_overriden = None
                            self.nexthop_id = None
                            self.next_hop_table_id = None
                            self.load_metric = None
                            self.path_id = None
                            self.bkup_path_id = None
                            self.path_type = None
                            self._segment_path = lambda: "routing"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing, ['next_hop', 'remote_node_id', 'has_remote_lfa_bkup', 'interface', 'nh_is_overriden', 'nexthop_id', 'next_hop_table_id', 'load_metric', 'path_id', 'bkup_path_id', 'path_type'], name, value)


                    class Mpls(Entity):
                        """
                        MPLS LDP Forwarding Path MPLS information
                        
                        .. attribute:: mpls_outgoing_info
                        
                        	MPLS nexthop info
                        	**type**\:  :py:class:`MplsOutgoingInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo>`
                        
                        .. attribute:: remote_lfa
                        
                        	MPLS LDP Forwarding Path Remote LFA\-FRR backup MPLS info
                        	**type**\:  :py:class:`RemoteLfa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls, self).__init__()

                            self.yang_name = "mpls"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("mpls-outgoing-info", ("mpls_outgoing_info", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo)), ("remote-lfa", ("remote_lfa", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.mpls_outgoing_info = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo()
                            self.mpls_outgoing_info.parent = self
                            self._children_name_map["mpls_outgoing_info"] = "mpls-outgoing-info"
                            self._children_yang_names.add("mpls-outgoing-info")

                            self.remote_lfa = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa()
                            self.remote_lfa.parent = self
                            self._children_name_map["remote_lfa"] = "remote-lfa"
                            self._children_yang_names.add("remote-lfa")
                            self._segment_path = lambda: "mpls"


                        class MplsOutgoingInfo(Entity):
                            """
                            MPLS nexthop info
                            
                            .. attribute:: nexthop_peer_ldp_ident
                            
                            	Nexthop LDP peer
                            	**type**\:  :py:class:`NexthopPeerLdpIdent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent>`
                            
                            .. attribute:: out_label
                            
                            	Outgoing label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_label_type
                            
                            	Outgoing Label Type
                            	**type**\:  :py:class:`LabelType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LabelType>`
                            
                            .. attribute:: out_label_owner
                            
                            	Outgoing label owner
                            	**type**\:  :py:class:`RoutePathLblOwner <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RoutePathLblOwner>`
                            
                            .. attribute:: is_from_graceful_restartable_neighbor
                            
                            	Is from a GR neighbor
                            	**type**\: bool
                            
                            .. attribute:: is_stale
                            
                            	Is the entry stale? This may happen during a graceful restart
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo, self).__init__()

                                self.yang_name = "mpls-outgoing-info"
                                self.yang_parent_name = "mpls"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("nexthop-peer-ldp-ident", ("nexthop_peer_ldp_ident", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('out_label', YLeaf(YType.uint32, 'out-label')),
                                    ('out_label_type', YLeaf(YType.identityref, 'out-label-type')),
                                    ('out_label_owner', YLeaf(YType.identityref, 'out-label-owner')),
                                    ('is_from_graceful_restartable_neighbor', YLeaf(YType.boolean, 'is-from-graceful-restartable-neighbor')),
                                    ('is_stale', YLeaf(YType.boolean, 'is-stale')),
                                ])
                                self.out_label = None
                                self.out_label_type = None
                                self.out_label_owner = None
                                self.is_from_graceful_restartable_neighbor = None
                                self.is_stale = None

                                self.nexthop_peer_ldp_ident = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent()
                                self.nexthop_peer_ldp_ident.parent = self
                                self._children_name_map["nexthop_peer_ldp_ident"] = "nexthop-peer-ldp-ident"
                                self._children_yang_names.add("nexthop-peer-ldp-ident")
                                self._segment_path = lambda: "mpls-outgoing-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo, ['out_label', 'out_label_type', 'out_label_owner', 'is_from_graceful_restartable_neighbor', 'is_stale'], name, value)


                            class NexthopPeerLdpIdent(Entity):
                                """
                                Nexthop LDP peer
                                
                                .. attribute:: lsr_id
                                
                                	LSR identifier
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: label_space_id
                                
                                	Label space identifier
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent, self).__init__()

                                    self.yang_name = "nexthop-peer-ldp-ident"
                                    self.yang_parent_name = "mpls-outgoing-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('lsr_id', YLeaf(YType.str, 'lsr-id')),
                                        ('label_space_id', YLeaf(YType.uint16, 'label-space-id')),
                                    ])
                                    self.lsr_id = None
                                    self.label_space_id = None
                                    self._segment_path = lambda: "nexthop-peer-ldp-ident"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent, ['lsr_id', 'label_space_id'], name, value)


                        class RemoteLfa(Entity):
                            """
                            MPLS LDP Forwarding Path Remote LFA\-FRR backup
                            MPLS info
                            
                            .. attribute:: mpls_outgoing_info
                            
                            	Remote LFA MPLS nexthop info
                            	**type**\:  :py:class:`MplsOutgoingInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo>`
                            
                            .. attribute:: has_remote_lfa_bkup
                            
                            	Whether path has remote LFA backup
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa, self).__init__()

                                self.yang_name = "remote-lfa"
                                self.yang_parent_name = "mpls"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("mpls-outgoing-info", ("mpls_outgoing_info", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('has_remote_lfa_bkup', YLeaf(YType.boolean, 'has-remote-lfa-bkup')),
                                ])
                                self.has_remote_lfa_bkup = None

                                self.mpls_outgoing_info = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo()
                                self.mpls_outgoing_info.parent = self
                                self._children_name_map["mpls_outgoing_info"] = "mpls-outgoing-info"
                                self._children_yang_names.add("mpls-outgoing-info")
                                self._segment_path = lambda: "remote-lfa"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa, ['has_remote_lfa_bkup'], name, value)


                            class MplsOutgoingInfo(Entity):
                                """
                                Remote LFA MPLS nexthop info
                                
                                .. attribute:: nexthop_peer_ldp_ident
                                
                                	Nexthop LDP peer
                                	**type**\:  :py:class:`NexthopPeerLdpIdent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent>`
                                
                                .. attribute:: out_label
                                
                                	Outgoing label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: out_label_type
                                
                                	Outgoing Label Type
                                	**type**\:  :py:class:`LabelType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LabelType>`
                                
                                .. attribute:: out_label_owner
                                
                                	Outgoing label owner
                                	**type**\:  :py:class:`RoutePathLblOwner <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RoutePathLblOwner>`
                                
                                .. attribute:: is_from_graceful_restartable_neighbor
                                
                                	Is from a GR neighbor
                                	**type**\: bool
                                
                                .. attribute:: is_stale
                                
                                	Is the entry stale? This may happen during a graceful restart
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo, self).__init__()

                                    self.yang_name = "mpls-outgoing-info"
                                    self.yang_parent_name = "remote-lfa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("nexthop-peer-ldp-ident", ("nexthop_peer_ldp_ident", MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('out_label', YLeaf(YType.uint32, 'out-label')),
                                        ('out_label_type', YLeaf(YType.identityref, 'out-label-type')),
                                        ('out_label_owner', YLeaf(YType.identityref, 'out-label-owner')),
                                        ('is_from_graceful_restartable_neighbor', YLeaf(YType.boolean, 'is-from-graceful-restartable-neighbor')),
                                        ('is_stale', YLeaf(YType.boolean, 'is-stale')),
                                    ])
                                    self.out_label = None
                                    self.out_label_type = None
                                    self.out_label_owner = None
                                    self.is_from_graceful_restartable_neighbor = None
                                    self.is_stale = None

                                    self.nexthop_peer_ldp_ident = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent()
                                    self.nexthop_peer_ldp_ident.parent = self
                                    self._children_name_map["nexthop_peer_ldp_ident"] = "nexthop-peer-ldp-ident"
                                    self._children_yang_names.add("nexthop-peer-ldp-ident")
                                    self._segment_path = lambda: "mpls-outgoing-info"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo, ['out_label', 'out_label_type', 'out_label_owner', 'is_from_graceful_restartable_neighbor', 'is_stale'], name, value)


                                class NexthopPeerLdpIdent(Entity):
                                    """
                                    Nexthop LDP peer
                                    
                                    .. attribute:: lsr_id
                                    
                                    	LSR identifier
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: label_space_id
                                    
                                    	Label space identifier
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-ios-xe-oper'
                                    _revision = '2017-02-07'

                                    def __init__(self):
                                        super(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent, self).__init__()

                                        self.yang_name = "nexthop-peer-ldp-ident"
                                        self.yang_parent_name = "mpls-outgoing-info"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsr_id', YLeaf(YType.str, 'lsr-id')),
                                            ('label_space_id', YLeaf(YType.uint16, 'label-space-id')),
                                        ])
                                        self.lsr_id = None
                                        self.label_space_id = None
                                        self._segment_path = lambda: "nexthop-peer-ldp-ident"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent, ['lsr_id', 'label_space_id'], name, value)


        class Bindings(Entity):
            """
            The detailed LDP Bindings.
            
            .. attribute:: bindings_sum_afs
            
            	This container holds the bindings specific to this VRF and AF
            	**type**\:  :py:class:`BindingsSumAfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.BindingsSumAfs>`
            
            .. attribute:: binding
            
            	This list contains the MPLS LDP Label Bindings for each IP Prefix. Label bindings provide the local MPLS Label, a list of remote labels, any filters affecting advertisment of that filter, and a list of neighbors to which the label has been advertised
            	**type**\: list of  		 :py:class:`Binding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Bindings, self).__init__()

                self.yang_name = "bindings"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("bindings-sum-afs", ("bindings_sum_afs", MplsLdp.MplsLdpState.Bindings.BindingsSumAfs))])
                self._child_list_classes = OrderedDict([("binding", ("binding", MplsLdp.MplsLdpState.Bindings.Binding))])
                self._leafs = OrderedDict()

                self.bindings_sum_afs = MplsLdp.MplsLdpState.Bindings.BindingsSumAfs()
                self.bindings_sum_afs.parent = self
                self._children_name_map["bindings_sum_afs"] = "bindings-sum-afs"
                self._children_yang_names.add("bindings-sum-afs")

                self.binding = YList(self)
                self._segment_path = lambda: "bindings"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.Bindings, [], name, value)


            class BindingsSumAfs(Entity):
                """
                This container holds the bindings specific to this VRF
                and AF.
                
                .. attribute:: binding_sum_af
                
                	Counters for the LDP Label Information Base for this VRF/AF
                	**type**\: list of  		 :py:class:`BindingSumAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Bindings.BindingsSumAfs, self).__init__()

                    self.yang_name = "bindings-sum-afs"
                    self.yang_parent_name = "bindings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("binding-sum-af", ("binding_sum_af", MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf))])
                    self._leafs = OrderedDict()

                    self.binding_sum_af = YList(self)
                    self._segment_path = lambda: "bindings-sum-afs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/bindings/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Bindings.BindingsSumAfs, [], name, value)


                class BindingSumAf(Entity):
                    """
                    Counters for the LDP Label Information Base for this
                    VRF/AF.
                    
                    .. attribute:: vrf_name  (key)
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\: str
                    
                    .. attribute:: af_name  (key)
                    
                    	Address Family name
                    	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                    
                    .. attribute:: binding_total
                    
                    	Total bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_no_route
                    
                    	Bindings with no route
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_no_route
                    
                    	Local bindings with no route
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local
                    
                    	Number of local bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_null
                    
                    	Number of local null bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_implicit_null
                    
                    	Number of local implicit null bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_explicit_null
                    
                    	Number of local explicit null bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_non_null
                    
                    	Number of local non\-null bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_oor
                    
                    	This is the number of local bindings needing label but which hit the Out\-Of\-Resource condition
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lowest_allocated_label
                    
                    	Lowest allocated label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: highest_allocated_label
                    
                    	Highest allocated label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_remote
                    
                    	Number of remote bindings
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf, self).__init__()

                        self.yang_name = "binding-sum-af"
                        self.yang_parent_name = "bindings-sum-afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name','af_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ('af_name', YLeaf(YType.enumeration, 'af-name')),
                            ('binding_total', YLeaf(YType.uint32, 'binding-total')),
                            ('binding_no_route', YLeaf(YType.uint32, 'binding-no-route')),
                            ('binding_local_no_route', YLeaf(YType.uint32, 'binding-local-no-route')),
                            ('binding_local', YLeaf(YType.uint32, 'binding-local')),
                            ('binding_local_null', YLeaf(YType.uint32, 'binding-local-null')),
                            ('binding_local_implicit_null', YLeaf(YType.uint32, 'binding-local-implicit-null')),
                            ('binding_local_explicit_null', YLeaf(YType.uint32, 'binding-local-explicit-null')),
                            ('binding_local_non_null', YLeaf(YType.uint32, 'binding-local-non-null')),
                            ('binding_local_oor', YLeaf(YType.uint32, 'binding-local-oor')),
                            ('lowest_allocated_label', YLeaf(YType.uint32, 'lowest-allocated-label')),
                            ('highest_allocated_label', YLeaf(YType.uint32, 'highest-allocated-label')),
                            ('binding_remote', YLeaf(YType.uint32, 'binding-remote')),
                        ])
                        self.vrf_name = None
                        self.af_name = None
                        self.binding_total = None
                        self.binding_no_route = None
                        self.binding_local_no_route = None
                        self.binding_local = None
                        self.binding_local_null = None
                        self.binding_local_implicit_null = None
                        self.binding_local_explicit_null = None
                        self.binding_local_non_null = None
                        self.binding_local_oor = None
                        self.lowest_allocated_label = None
                        self.highest_allocated_label = None
                        self.binding_remote = None
                        self._segment_path = lambda: "binding-sum-af" + "[vrf-name='" + str(self.vrf_name) + "']" + "[af-name='" + str(self.af_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/bindings/bindings-sum-afs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf, ['vrf_name', 'af_name', 'binding_total', 'binding_no_route', 'binding_local_no_route', 'binding_local', 'binding_local_null', 'binding_local_implicit_null', 'binding_local_explicit_null', 'binding_local_non_null', 'binding_local_oor', 'lowest_allocated_label', 'highest_allocated_label', 'binding_remote'], name, value)


            class Binding(Entity):
                """
                This list contains the MPLS LDP Label Bindings for each
                IP Prefix. Label bindings provide the local MPLS Label,
                a list of remote labels, any filters affecting
                advertisment of that filter, and a list of neighbors to
                which the label has been advertised.
                
                .. attribute:: vrf_name  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: prefix  (key)
                
                	This leaf contains the IP Prefix being bound
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                .. attribute:: fwd_prefix
                
                	This is the MPLS LDP Binding IP Prefix
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: prefix_length
                
                	This is the MPLS LDP Binding Prefix Length
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: local_label
                
                	This is the MPLS LDP Binding Local label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: le_local_binding_revision
                
                	This is the MPLS LDP Binding Local Binding revision
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: le_local_label_state
                
                	This is the MPLS LDP Binding Local label state
                	**type**\:  :py:class:`LocalLabelState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LocalLabelState>`
                
                .. attribute:: is_no_route
                
                	This is true if the MPLS LDP Binding has no route
                	**type**\: bool
                
                .. attribute:: label_oor
                
                	This is true if the MPLS LDP Binding Label space is depleted, Out Of Resource. No new labels can be allocated
                	**type**\: bool
                
                .. attribute:: advertise_prefix_filter
                
                	This contains the filter name for this binding's prefix. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                .. attribute:: advertise_lsr_filter
                
                	This contains the filter name for this binding's Advertise LSR. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                .. attribute:: config_enforced_local_label_value
                
                	Config/User enforced local label value
                	**type**\: bool
                
                .. attribute:: remote_binding
                
                	MPLS LDP Remote Binding Information
                	**type**\: list of  		 :py:class:`RemoteBinding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding>`
                
                .. attribute:: peers_advertised_to
                
                	Peers to which this entry is advertised
                	**type**\: list of  		 :py:class:`PeersAdvertisedTo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Bindings.Binding, self).__init__()

                    self.yang_name = "binding"
                    self.yang_parent_name = "bindings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','prefix']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("remote-binding", ("remote_binding", MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding)), ("peers-advertised-to", ("peers_advertised_to", MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo))])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('prefix', YLeaf(YType.str, 'prefix')),
                        ('fwd_prefix', YLeaf(YType.str, 'fwd-prefix')),
                        ('prefix_length', YLeaf(YType.uint8, 'prefix-length')),
                        ('local_label', YLeaf(YType.uint32, 'local-label')),
                        ('le_local_binding_revision', YLeaf(YType.uint32, 'le-local-binding-revision')),
                        ('le_local_label_state', YLeaf(YType.enumeration, 'le-local-label-state')),
                        ('is_no_route', YLeaf(YType.boolean, 'is-no-route')),
                        ('label_oor', YLeaf(YType.boolean, 'label-oor')),
                        ('advertise_prefix_filter', YLeaf(YType.str, 'advertise-prefix-filter')),
                        ('advertise_lsr_filter', YLeaf(YType.str, 'advertise-lsr-filter')),
                        ('config_enforced_local_label_value', YLeaf(YType.boolean, 'config-enforced-local-label-value')),
                    ])
                    self.vrf_name = None
                    self.prefix = None
                    self.fwd_prefix = None
                    self.prefix_length = None
                    self.local_label = None
                    self.le_local_binding_revision = None
                    self.le_local_label_state = None
                    self.is_no_route = None
                    self.label_oor = None
                    self.advertise_prefix_filter = None
                    self.advertise_lsr_filter = None
                    self.config_enforced_local_label_value = None

                    self.remote_binding = YList(self)
                    self.peers_advertised_to = YList(self)
                    self._segment_path = lambda: "binding" + "[vrf-name='" + str(self.vrf_name) + "']" + "[prefix='" + str(self.prefix) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/bindings/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Bindings.Binding, ['vrf_name', 'prefix', 'fwd_prefix', 'prefix_length', 'local_label', 'le_local_binding_revision', 'le_local_label_state', 'is_no_route', 'label_oor', 'advertise_prefix_filter', 'advertise_lsr_filter', 'config_enforced_local_label_value'], name, value)


                class RemoteBinding(Entity):
                    """
                    MPLS LDP Remote Binding Information
                    
                    .. attribute:: assigning_peer_ldp_ident
                    
                    	Assigning peer
                    	**type**\:  :py:class:`AssigningPeerLdpIdent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent>`
                    
                    .. attribute:: remote_label
                    
                    	This is the remote Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_stale
                    
                    	Is the entry stale
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding, self).__init__()

                        self.yang_name = "remote-binding"
                        self.yang_parent_name = "binding"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("assigning-peer-ldp-ident", ("assigning_peer_ldp_ident", MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('remote_label', YLeaf(YType.uint32, 'remote-label')),
                            ('is_stale', YLeaf(YType.boolean, 'is-stale')),
                        ])
                        self.remote_label = None
                        self.is_stale = None

                        self.assigning_peer_ldp_ident = MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent()
                        self.assigning_peer_ldp_ident.parent = self
                        self._children_name_map["assigning_peer_ldp_ident"] = "assigning-peer-ldp-ident"
                        self._children_yang_names.add("assigning-peer-ldp-ident")
                        self._segment_path = lambda: "remote-binding"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding, ['remote_label', 'is_stale'], name, value)


                    class AssigningPeerLdpIdent(Entity):
                        """
                        Assigning peer
                        
                        .. attribute:: lsr_id
                        
                        	LSR identifier
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: label_space_id
                        
                        	Label space identifier
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent, self).__init__()

                            self.yang_name = "assigning-peer-ldp-ident"
                            self.yang_parent_name = "remote-binding"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('lsr_id', YLeaf(YType.str, 'lsr-id')),
                                ('label_space_id', YLeaf(YType.uint16, 'label-space-id')),
                            ])
                            self.lsr_id = None
                            self.label_space_id = None
                            self._segment_path = lambda: "assigning-peer-ldp-ident"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent, ['lsr_id', 'label_space_id'], name, value)


                class PeersAdvertisedTo(Entity):
                    """
                    Peers to which this entry is advertised.
                    
                    .. attribute:: lsr_id
                    
                    	LSR identifier
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: label_space_id
                    
                    	Label space identifier
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo, self).__init__()

                        self.yang_name = "peers-advertised-to"
                        self.yang_parent_name = "binding"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lsr_id', YLeaf(YType.str, 'lsr-id')),
                            ('label_space_id', YLeaf(YType.uint16, 'label-space-id')),
                        ])
                        self.lsr_id = None
                        self.label_space_id = None
                        self._segment_path = lambda: "peers-advertised-to"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo, ['lsr_id', 'label_space_id'], name, value)


        class Neighbors(Entity):
            """
            The LDP Neighbors Information
            
            .. attribute:: neighbor
            
            	Information on a particular LDP neighbor
            	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor>`
            
            .. attribute:: nbr_adjs
            
            	For this Neighbor, this is the list of adjacencies between the neighbor and the local node
            	**type**\: list of  		 :py:class:`NbrAdjs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NbrAdjs>`
            
            .. attribute:: stats_info
            
            	MPLS LDP Statistics Information
            	**type**\:  :py:class:`StatsInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.StatsInfo>`
            
            .. attribute:: backoffs
            
            	LDP Backoff Information
            	**type**\:  :py:class:`Backoffs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Backoffs>`
            
            .. attribute:: nsr_nbr_detail
            
            	This is the LDP NSR state for this neighbor
            	**type**\:  :py:class:`NsrNbrDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.Neighbors, self).__init__()

                self.yang_name = "neighbors"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("stats-info", ("stats_info", MplsLdp.MplsLdpState.Neighbors.StatsInfo)), ("backoffs", ("backoffs", MplsLdp.MplsLdpState.Neighbors.Backoffs)), ("nsr-nbr-detail", ("nsr_nbr_detail", MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail))])
                self._child_list_classes = OrderedDict([("neighbor", ("neighbor", MplsLdp.MplsLdpState.Neighbors.Neighbor)), ("nbr-adjs", ("nbr_adjs", MplsLdp.MplsLdpState.Neighbors.NbrAdjs))])
                self._leafs = OrderedDict()

                self.stats_info = MplsLdp.MplsLdpState.Neighbors.StatsInfo()
                self.stats_info.parent = self
                self._children_name_map["stats_info"] = "stats-info"
                self._children_yang_names.add("stats-info")

                self.backoffs = MplsLdp.MplsLdpState.Neighbors.Backoffs()
                self.backoffs.parent = self
                self._children_name_map["backoffs"] = "backoffs"
                self._children_yang_names.add("backoffs")

                self.nsr_nbr_detail = MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail()
                self.nsr_nbr_detail.parent = self
                self._children_name_map["nsr_nbr_detail"] = "nsr-nbr-detail"
                self._children_yang_names.add("nsr-nbr-detail")

                self.neighbor = YList(self)
                self.nbr_adjs = YList(self)
                self._segment_path = lambda: "neighbors"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.Neighbors, [], name, value)


            class Neighbor(Entity):
                """
                Information on a particular LDP neighbor
                
                .. attribute:: vrf_name  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: lsr_id  (key)
                
                	LSR ID of neighbor
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: label_space_id
                
                	Label space ID of neighbor
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: session_role
                
                	During session establishment the LSR/LER takes either the active role or the passive role based on address comparisons.  This object indicates whether this LSR/LER was behaving in an active role or passive role during this session's establishment.  The value of unknown(1), indicates that the role is not able to be determined at the present time
                	**type**\:  :py:class:`SessionRole <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.SessionRole>`
                
                .. attribute:: session_prot_ver
                
                	The version of the LDP Protocol which this session is using.  This is the version of the LDP protocol which has been negotiated during session initialization
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: up_time_seconds
                
                	Up time in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: nbr_path_vector_limit
                
                	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this neighor is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this neighbor is enabled and the Path Vector Limit is this value
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: nbr_stats
                
                	Neighbor Statistics
                	**type**\:  :py:class:`NbrStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats>`
                
                .. attribute:: graceful_restart_adjacency
                
                	This container holds the graceful restart information for this adjacency
                	**type**\:  :py:class:`GracefulRestartAdjacency <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency>`
                
                .. attribute:: downstream_on_demand
                
                	Is Label advertisement mode in Downstream On Demand mode or not?
                	**type**\: bool
                
                .. attribute:: tcp_information
                
                	MPLS LDP Neighbor TCP Information
                	**type**\:  :py:class:`TcpInformation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation>`
                
                .. attribute:: capabilities
                
                	Capabilities sent to and received from neighbor
                	**type**\:  :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities>`
                
                .. attribute:: peer_hold_time
                
                	Session holdtime value in seconds from the peer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: peer_keep_alive_interval
                
                	Session keepalive interval in seconds from the peer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: peer_state
                
                	LDP adjacency peer state
                	**type**\:  :py:class:`AdjState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AdjState>`
                
                .. attribute:: inbound_ipv4
                
                	This contains the IPv4 Inbound accept filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: inbound_ipv6_filter
                
                	This contains the IPv6 Inbound accept filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: outbound_ipv4_filter
                
                	This contains the IPv4 Outbound advertise filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: outbound_ipv6_filter
                
                	This contains the IPv6 Outbound advertise filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: has_sp
                
                	Session Protection enabled
                	**type**\: bool
                
                .. attribute:: sp_state
                
                	Session Protection state
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: sp_filter
                
                	This contains the Session Protection filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..80
                
                .. attribute:: sp_has_duration
                
                	Session Protection has non\-default duration
                	**type**\: bool
                
                .. attribute:: sp_duration
                
                	Session protection holdup time duration in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: spht_running
                
                	Session Protection holdup timer is running
                	**type**\: bool
                
                .. attribute:: spht_remaining
                
                	Session Protection holdup time remaining value in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: bgp_advertisement_state
                
                	BGP labeled prefixes advertisement state
                	**type**\:  :py:class:`NbrBgpAdvtState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NbrBgpAdvtState>`
                
                .. attribute:: advertise_bgp_prefixes
                
                	True if BGP labeled prefixes are advertised to the neighbor
                	**type**\: bool
                
                .. attribute:: client
                
                	Targeted Session clients
                	**type**\: list of str
                
                .. attribute:: duplicate_address
                
                	Duplicate IPv4/IPv6 address bound to this peer
                	**type**\: union of the below types:
                
                		**type**\: list of str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: list of str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: nbr_bound_address
                
                	This is the MPLS LDP Neighbor Bound IPv4/IPv6 Address
                	**type**\: union of the below types:
                
                		**type**\: list of str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: list of str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Neighbors.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','lsr_id']
                    self._child_container_classes = OrderedDict([("nbr-stats", ("nbr_stats", MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats)), ("graceful-restart-adjacency", ("graceful_restart_adjacency", MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency)), ("tcp-information", ("tcp_information", MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation)), ("capabilities", ("capabilities", MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('lsr_id', YLeaf(YType.str, 'lsr-id')),
                        ('label_space_id', YLeaf(YType.uint32, 'label-space-id')),
                        ('session_role', YLeaf(YType.enumeration, 'session-role')),
                        ('session_prot_ver', YLeaf(YType.uint32, 'session-prot-ver')),
                        ('up_time_seconds', YLeaf(YType.uint32, 'up-time-seconds')),
                        ('nbr_path_vector_limit', YLeaf(YType.int32, 'nbr-path-vector-limit')),
                        ('downstream_on_demand', YLeaf(YType.boolean, 'downstream-on-demand')),
                        ('peer_hold_time', YLeaf(YType.uint32, 'peer-hold-time')),
                        ('peer_keep_alive_interval', YLeaf(YType.uint32, 'peer-keep-alive-interval')),
                        ('peer_state', YLeaf(YType.enumeration, 'peer-state')),
                        ('inbound_ipv4', YLeaf(YType.str, 'inbound-ipv4')),
                        ('inbound_ipv6_filter', YLeaf(YType.str, 'inbound-ipv6-filter')),
                        ('outbound_ipv4_filter', YLeaf(YType.str, 'outbound-ipv4-filter')),
                        ('outbound_ipv6_filter', YLeaf(YType.str, 'outbound-ipv6-filter')),
                        ('has_sp', YLeaf(YType.boolean, 'has-sp')),
                        ('sp_state', YLeaf(YType.str, 'sp-state')),
                        ('sp_filter', YLeaf(YType.str, 'sp-filter')),
                        ('sp_has_duration', YLeaf(YType.boolean, 'sp-has-duration')),
                        ('sp_duration', YLeaf(YType.uint32, 'sp-duration')),
                        ('spht_running', YLeaf(YType.boolean, 'spht-running')),
                        ('spht_remaining', YLeaf(YType.uint32, 'spht-remaining')),
                        ('bgp_advertisement_state', YLeaf(YType.enumeration, 'bgp-advertisement-state')),
                        ('advertise_bgp_prefixes', YLeaf(YType.boolean, 'advertise-bgp-prefixes')),
                        ('client', YLeafList(YType.str, 'client')),
                        ('duplicate_address', YLeafList(YType.str, 'duplicate-address')),
                        ('nbr_bound_address', YLeafList(YType.str, 'nbr-bound-address')),
                    ])
                    self.vrf_name = None
                    self.lsr_id = None
                    self.label_space_id = None
                    self.session_role = None
                    self.session_prot_ver = None
                    self.up_time_seconds = None
                    self.nbr_path_vector_limit = None
                    self.downstream_on_demand = None
                    self.peer_hold_time = None
                    self.peer_keep_alive_interval = None
                    self.peer_state = None
                    self.inbound_ipv4 = None
                    self.inbound_ipv6_filter = None
                    self.outbound_ipv4_filter = None
                    self.outbound_ipv6_filter = None
                    self.has_sp = None
                    self.sp_state = None
                    self.sp_filter = None
                    self.sp_has_duration = None
                    self.sp_duration = None
                    self.spht_running = None
                    self.spht_remaining = None
                    self.bgp_advertisement_state = None
                    self.advertise_bgp_prefixes = None
                    self.client = []
                    self.duplicate_address = []
                    self.nbr_bound_address = []

                    self.nbr_stats = MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats()
                    self.nbr_stats.parent = self
                    self._children_name_map["nbr_stats"] = "nbr-stats"
                    self._children_yang_names.add("nbr-stats")

                    self.graceful_restart_adjacency = MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency()
                    self.graceful_restart_adjacency.parent = self
                    self._children_name_map["graceful_restart_adjacency"] = "graceful-restart-adjacency"
                    self._children_yang_names.add("graceful-restart-adjacency")

                    self.tcp_information = MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation()
                    self.tcp_information.parent = self
                    self._children_name_map["tcp_information"] = "tcp-information"
                    self._children_yang_names.add("tcp-information")

                    self.capabilities = MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities()
                    self.capabilities.parent = self
                    self._children_name_map["capabilities"] = "capabilities"
                    self._children_yang_names.add("capabilities")
                    self._segment_path = lambda: "neighbor" + "[vrf-name='" + str(self.vrf_name) + "']" + "[lsr-id='" + str(self.lsr_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor, ['vrf_name', 'lsr_id', 'label_space_id', 'session_role', 'session_prot_ver', 'up_time_seconds', 'nbr_path_vector_limit', 'downstream_on_demand', 'peer_hold_time', 'peer_keep_alive_interval', 'peer_state', 'inbound_ipv4', 'inbound_ipv6_filter', 'outbound_ipv4_filter', 'outbound_ipv6_filter', 'has_sp', 'sp_state', 'sp_filter', 'sp_has_duration', 'sp_duration', 'spht_running', 'spht_remaining', 'bgp_advertisement_state', 'advertise_bgp_prefixes', 'client', 'duplicate_address', 'nbr_bound_address'], name, value)

                class SessionRole(Enum):
                    """
                    SessionRole (Enum Class)

                    During session establishment the LSR/LER takes either

                    the active role or the passive role based on address

                    comparisons.  This object indicates whether this

                    LSR/LER was behaving in an active role or passive role

                    during this session's establishment.

                    The value of unknown(1), indicates that the role is not

                    able to be determined at the present time.

                    .. data:: unknown = 1

                    	The role of this LSR in the session is unknown.

                    .. data:: active = 2

                    	The role of this LSR in the session is active.

                    .. data:: passive = 3

                    	The role of this LSR in the session is passive.

                    """

                    unknown = Enum.YLeaf(1, "unknown")

                    active = Enum.YLeaf(2, "active")

                    passive = Enum.YLeaf(3, "passive")



                class NbrStats(Entity):
                    """
                    Neighbor Statistics.
                    
                    .. attribute:: ta_pies_sent
                    
                    	Number of MPLS LDP messages sent to this neighbor
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ta_pies_rcvd
                    
                    	Number of MPLS LDP messages received from this neighbor
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv4_discovery
                    
                    	Number of neighbor IPv4 discovery sources
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv6_discovery
                    
                    	Number of neighbor IPv6 discovery sources
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv4_addresses
                    
                    	Number of IPv4 addresses for which the neighbor is advertising labels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv6_addresses
                    
                    	Number of IPv6 addresses for which the neighbor is advertising labels
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv4_lbl
                    
                    	Number of IPv4 labels the neighbor is advertising
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv6_lbl
                    
                    	Number of IPv6 labels the neighbor is advertising
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats, self).__init__()

                        self.yang_name = "nbr-stats"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ta_pies_sent', YLeaf(YType.uint32, 'ta-pies-sent')),
                            ('ta_pies_rcvd', YLeaf(YType.uint32, 'ta-pies-rcvd')),
                            ('num_of_nbr_ipv4_discovery', YLeaf(YType.uint32, 'num-of-nbr-ipv4-discovery')),
                            ('num_of_nbr_ipv6_discovery', YLeaf(YType.uint32, 'num-of-nbr-ipv6-discovery')),
                            ('num_of_nbr_ipv4_addresses', YLeaf(YType.uint32, 'num-of-nbr-ipv4-addresses')),
                            ('num_of_nbr_ipv6_addresses', YLeaf(YType.uint32, 'num-of-nbr-ipv6-addresses')),
                            ('num_of_nbr_ipv4_lbl', YLeaf(YType.uint32, 'num-of-nbr-ipv4-lbl')),
                            ('num_of_nbr_ipv6_lbl', YLeaf(YType.uint32, 'num-of-nbr-ipv6-lbl')),
                        ])
                        self.ta_pies_sent = None
                        self.ta_pies_rcvd = None
                        self.num_of_nbr_ipv4_discovery = None
                        self.num_of_nbr_ipv6_discovery = None
                        self.num_of_nbr_ipv4_addresses = None
                        self.num_of_nbr_ipv6_addresses = None
                        self.num_of_nbr_ipv4_lbl = None
                        self.num_of_nbr_ipv6_lbl = None
                        self._segment_path = lambda: "nbr-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats, ['ta_pies_sent', 'ta_pies_rcvd', 'num_of_nbr_ipv4_discovery', 'num_of_nbr_ipv6_discovery', 'num_of_nbr_ipv4_addresses', 'num_of_nbr_ipv6_addresses', 'num_of_nbr_ipv4_lbl', 'num_of_nbr_ipv6_lbl'], name, value)


                class GracefulRestartAdjacency(Entity):
                    """
                    This container holds the graceful restart information
                    for this adjacency.
                    
                    .. attribute:: is_graceful_restartable
                    
                    	Is this neighbor graceful restartable?
                    	**type**\: bool
                    
                    .. attribute:: reconnect_timeout
                    
                    	This leaf is the reconnect timeout in microseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: microseconds
                    
                    .. attribute:: recovery_time
                    
                    	This leaf is the recovery time in microseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: microseconds
                    
                    .. attribute:: is_liveness_timer_running
                    
                    	This is set if the liveness timer is running
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: liveness_timer_remaining_seconds
                    
                    	Remaining time from liveness timer in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: is_recovery_timer_running
                    
                    	This is set if the recovery timer is running
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: recovery_timer_remaining_seconds
                    
                    	Recovery timer remaining time in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: down_nbr_flap_count
                    
                    	This is the current count of back\-to\-back flaps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: down_nbr_down_reason
                    
                    	This identity provides the reason that the LDP Session with this neighbor is down. The reason does not persist if the session was down but is now recovered
                    	**type**\:  :py:class:`DownNbrReason <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.DownNbrReason>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency, self).__init__()

                        self.yang_name = "graceful-restart-adjacency"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('is_graceful_restartable', YLeaf(YType.boolean, 'is-graceful-restartable')),
                            ('reconnect_timeout', YLeaf(YType.uint32, 'reconnect-timeout')),
                            ('recovery_time', YLeaf(YType.uint32, 'recovery-time')),
                            ('is_liveness_timer_running', YLeaf(YType.empty, 'is-liveness-timer-running')),
                            ('liveness_timer_remaining_seconds', YLeaf(YType.uint32, 'liveness-timer-remaining-seconds')),
                            ('is_recovery_timer_running', YLeaf(YType.empty, 'is-recovery-timer-running')),
                            ('recovery_timer_remaining_seconds', YLeaf(YType.uint32, 'recovery-timer-remaining-seconds')),
                            ('down_nbr_flap_count', YLeaf(YType.uint32, 'down-nbr-flap-count')),
                            ('down_nbr_down_reason', YLeaf(YType.identityref, 'down-nbr-down-reason')),
                        ])
                        self.is_graceful_restartable = None
                        self.reconnect_timeout = None
                        self.recovery_time = None
                        self.is_liveness_timer_running = None
                        self.liveness_timer_remaining_seconds = None
                        self.is_recovery_timer_running = None
                        self.recovery_timer_remaining_seconds = None
                        self.down_nbr_flap_count = None
                        self.down_nbr_down_reason = None
                        self._segment_path = lambda: "graceful-restart-adjacency"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency, ['is_graceful_restartable', 'reconnect_timeout', 'recovery_time', 'is_liveness_timer_running', 'liveness_timer_remaining_seconds', 'is_recovery_timer_running', 'recovery_timer_remaining_seconds', 'down_nbr_flap_count', 'down_nbr_down_reason'], name, value)


                class TcpInformation(Entity):
                    """
                    MPLS LDP Neighbor TCP Information
                    
                    .. attribute:: foreign_host
                    
                    	This is the foreign host address used by TCP
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: local_host
                    
                    	This is the local host address used by TCP
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_port
                    
                    	Local port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: is_md5_on
                    
                    	Is MD5 Digest on
                    	**type**\: bool
                    
                    .. attribute:: up_time
                    
                    	up time
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation, self).__init__()

                        self.yang_name = "tcp-information"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('foreign_host', YLeaf(YType.str, 'foreign-host')),
                            ('local_host', YLeaf(YType.str, 'local-host')),
                            ('foreign_port', YLeaf(YType.uint16, 'foreign-port')),
                            ('local_port', YLeaf(YType.uint16, 'local-port')),
                            ('is_md5_on', YLeaf(YType.boolean, 'is-md5-on')),
                            ('up_time', YLeaf(YType.str, 'up-time')),
                        ])
                        self.foreign_host = None
                        self.local_host = None
                        self.foreign_port = None
                        self.local_port = None
                        self.is_md5_on = None
                        self.up_time = None
                        self._segment_path = lambda: "tcp-information"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation, ['foreign_host', 'local_host', 'foreign_port', 'local_port', 'is_md5_on', 'up_time'], name, value)


                class Capabilities(Entity):
                    """
                    Capabilities sent to and received from neighbor
                    
                    .. attribute:: sent_caps
                    
                    	List of sent capabilities
                    	**type**\: list of  		 :py:class:`SentCaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps>`
                    
                    .. attribute:: received_caps
                    
                    	List of received capabilities
                    	**type**\: list of  		 :py:class:`ReceivedCaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities, self).__init__()

                        self.yang_name = "capabilities"
                        self.yang_parent_name = "neighbor"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("sent-caps", ("sent_caps", MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps)), ("received-caps", ("received_caps", MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps))])
                        self._leafs = OrderedDict()

                        self.sent_caps = YList(self)
                        self.received_caps = YList(self)
                        self._segment_path = lambda: "capabilities"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities, [], name, value)


                    class SentCaps(Entity):
                        """
                        List of sent capabilities
                        
                        .. attribute:: cap_type  (key)
                        
                        	Capability type (IANA assigned)
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cap_des
                        
                        	Capability description
                        	**type**\: str
                        
                        	**length:** 0..80
                        
                        .. attribute:: capability_data_length
                        
                        	Capability data length
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: capability_data
                        
                        	Capability data
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps, self).__init__()

                            self.yang_name = "sent-caps"
                            self.yang_parent_name = "capabilities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['cap_type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('cap_type', YLeaf(YType.uint16, 'cap-type')),
                                ('cap_des', YLeaf(YType.str, 'cap-des')),
                                ('capability_data_length', YLeaf(YType.uint16, 'capability-data-length')),
                                ('capability_data', YLeaf(YType.str, 'capability-data')),
                            ])
                            self.cap_type = None
                            self.cap_des = None
                            self.capability_data_length = None
                            self.capability_data = None
                            self._segment_path = lambda: "sent-caps" + "[cap-type='" + str(self.cap_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps, ['cap_type', 'cap_des', 'capability_data_length', 'capability_data'], name, value)


                    class ReceivedCaps(Entity):
                        """
                        List of received capabilities
                        
                        .. attribute:: cap_type  (key)
                        
                        	Capability type (IANA assigned)
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cap_des
                        
                        	Capability description
                        	**type**\: str
                        
                        	**length:** 0..80
                        
                        .. attribute:: capability_data_length
                        
                        	Capability data length
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: capability_data
                        
                        	Capability data
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps, self).__init__()

                            self.yang_name = "received-caps"
                            self.yang_parent_name = "capabilities"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['cap_type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('cap_type', YLeaf(YType.uint16, 'cap-type')),
                                ('cap_des', YLeaf(YType.str, 'cap-des')),
                                ('capability_data_length', YLeaf(YType.uint16, 'capability-data-length')),
                                ('capability_data', YLeaf(YType.str, 'capability-data')),
                            ])
                            self.cap_type = None
                            self.cap_des = None
                            self.capability_data_length = None
                            self.capability_data = None
                            self._segment_path = lambda: "received-caps" + "[cap-type='" + str(self.cap_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps, ['cap_type', 'cap_des', 'capability_data_length', 'capability_data'], name, value)


            class NbrAdjs(Entity):
                """
                For this Neighbor, this is the list of adjacencies
                between the neighbor and the local node.
                
                .. attribute:: interface
                
                	This is the interface used by MPLS LDP Link Hello
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: local_address
                
                	This is the local address used to send the Targeted Hello
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: target_address
                
                	This is the destination address used to send the Targeted Hello
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: target_state
                
                	This is the state of this Targeted Hello instance
                	**type**\:  :py:class:`DhcState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.DhcState>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Neighbors.NbrAdjs, self).__init__()

                    self.yang_name = "nbr-adjs"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface', YLeaf(YType.str, 'interface')),
                        ('local_address', YLeaf(YType.str, 'local-address')),
                        ('target_address', YLeaf(YType.str, 'target-address')),
                        ('target_state', YLeaf(YType.enumeration, 'target-state')),
                    ])
                    self.interface = None
                    self.local_address = None
                    self.target_address = None
                    self.target_state = None
                    self._segment_path = lambda: "nbr-adjs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.NbrAdjs, ['interface', 'local_address', 'target_address', 'target_state'], name, value)


            class StatsInfo(Entity):
                """
                MPLS LDP Statistics Information
                
                .. attribute:: message_out
                
                	MPLS LDP message sent counters to this neighbor
                	**type**\:  :py:class:`MessageOut <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut>`
                
                .. attribute:: message_in
                
                	MPLS LDP message received counters from this neighbor
                	**type**\:  :py:class:`MessageIn <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn>`
                
                .. attribute:: discon_time
                
                	The value of sysUpTime on the most recent occasion at which any one or more of this entity's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this entity of any counter32 object contained in the 'EntityStatsTable'.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_attempts
                
                	A count of the Session Initialization messages which were sent or received by this LDP Entity and were NAK'd.   In other words, this counter counts the number of session initializations that failed.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_reject_no_hello
                
                	A count of the Session Rejected/No Hello Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_rej_ad
                
                	A count of the Session Rejected/Parameters Advertisement Mode Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_rej_max_pdu
                
                	A count of the Session Rejected/Parameters  Max Pdu Length Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_rej_lr
                
                	A count of the Session Rejected/Parameters Label Range Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_ldpid
                
                	This object counts the number of Bad LDP Identifier Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_pdu_len
                
                	This object counts the number of Bad PDU Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_msg_len
                
                	This object counts the number of Bad Message Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_tlv_len
                
                	This object counts the number of Bad TLV Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: malformed_tlv_val
                
                	This object counts the number of Malformed TLV Value Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: keep_alive_exp
                
                	This object counts the number of Session Keep Alive Timer Expired Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: shutdown_notif_rec
                
                	This object counts the number of Shutdown Notifications received related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: shutdow_notif_sent
                
                	This object counts the number of Shutdown Notfications sent related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of  discon\-time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Neighbors.StatsInfo, self).__init__()

                    self.yang_name = "stats-info"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("message-out", ("message_out", MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut)), ("message-in", ("message_in", MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('discon_time', YLeaf(YType.uint32, 'discon-time')),
                        ('session_attempts', YLeaf(YType.uint32, 'session-attempts')),
                        ('sess_reject_no_hello', YLeaf(YType.uint32, 'sess-reject-no-hello')),
                        ('sess_rej_ad', YLeaf(YType.uint32, 'sess-rej-ad')),
                        ('sess_rej_max_pdu', YLeaf(YType.uint32, 'sess-rej-max-pdu')),
                        ('sess_rej_lr', YLeaf(YType.uint32, 'sess-rej-lr')),
                        ('bad_ldpid', YLeaf(YType.uint32, 'bad-ldpid')),
                        ('bad_pdu_len', YLeaf(YType.uint32, 'bad-pdu-len')),
                        ('bad_msg_len', YLeaf(YType.uint32, 'bad-msg-len')),
                        ('bad_tlv_len', YLeaf(YType.uint32, 'bad-tlv-len')),
                        ('malformed_tlv_val', YLeaf(YType.uint32, 'malformed-tlv-val')),
                        ('keep_alive_exp', YLeaf(YType.uint32, 'keep-alive-exp')),
                        ('shutdown_notif_rec', YLeaf(YType.uint32, 'shutdown-notif-rec')),
                        ('shutdow_notif_sent', YLeaf(YType.uint32, 'shutdow-notif-sent')),
                    ])
                    self.discon_time = None
                    self.session_attempts = None
                    self.sess_reject_no_hello = None
                    self.sess_rej_ad = None
                    self.sess_rej_max_pdu = None
                    self.sess_rej_lr = None
                    self.bad_ldpid = None
                    self.bad_pdu_len = None
                    self.bad_msg_len = None
                    self.bad_tlv_len = None
                    self.malformed_tlv_val = None
                    self.keep_alive_exp = None
                    self.shutdown_notif_rec = None
                    self.shutdow_notif_sent = None

                    self.message_out = MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut()
                    self.message_out.parent = self
                    self._children_name_map["message_out"] = "message-out"
                    self._children_yang_names.add("message-out")

                    self.message_in = MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn()
                    self.message_in.parent = self
                    self._children_name_map["message_in"] = "message-in"
                    self._children_yang_names.add("message-in")
                    self._segment_path = lambda: "stats-info"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.StatsInfo, ['discon_time', 'session_attempts', 'sess_reject_no_hello', 'sess_rej_ad', 'sess_rej_max_pdu', 'sess_rej_lr', 'bad_ldpid', 'bad_pdu_len', 'bad_msg_len', 'bad_tlv_len', 'malformed_tlv_val', 'keep_alive_exp', 'shutdown_notif_rec', 'shutdow_notif_sent'], name, value)


                class MessageOut(Entity):
                    """
                    MPLS LDP message sent counters to this neighbor.
                    
                    .. attribute:: total_count
                    
                    	Total count of all messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_count
                    
                    	Init message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_count
                    
                    	Address message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_withdraw_count
                    
                    	Address withdraw count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_map_count
                    
                    	Label map count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_withdraw_count
                    
                    	Label withdraw count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_release_count
                    
                    	Label release count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_request_count
                    
                    	Label request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_abort_request_count
                    
                    	Label abort request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification_count
                    
                    	Notification count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_count
                    
                    	Keepalive count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_conn_count
                    
                    	ICCP RG Connect count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_disconn_count
                    
                    	ICCP RG Disconnect count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_notif_count
                    
                    	ICCP RG Notify count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_app_data_count
                    
                    	ICCP RG App Data count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut, self).__init__()

                        self.yang_name = "message-out"
                        self.yang_parent_name = "stats-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('total_count', YLeaf(YType.uint32, 'total-count')),
                            ('init_count', YLeaf(YType.uint32, 'init-count')),
                            ('address_count', YLeaf(YType.uint32, 'address-count')),
                            ('address_withdraw_count', YLeaf(YType.uint32, 'address-withdraw-count')),
                            ('label_map_count', YLeaf(YType.uint32, 'label-map-count')),
                            ('label_withdraw_count', YLeaf(YType.uint32, 'label-withdraw-count')),
                            ('label_release_count', YLeaf(YType.uint32, 'label-release-count')),
                            ('label_request_count', YLeaf(YType.uint32, 'label-request-count')),
                            ('label_abort_request_count', YLeaf(YType.uint32, 'label-abort-request-count')),
                            ('notification_count', YLeaf(YType.uint32, 'notification-count')),
                            ('keep_alive_count', YLeaf(YType.uint32, 'keep-alive-count')),
                            ('iccp_rg_conn_count', YLeaf(YType.uint32, 'iccp-rg-conn-count')),
                            ('iccp_rg_disconn_count', YLeaf(YType.uint32, 'iccp-rg-disconn-count')),
                            ('iccp_rg_notif_count', YLeaf(YType.uint32, 'iccp-rg-notif-count')),
                            ('iccp_rg_app_data_count', YLeaf(YType.uint32, 'iccp-rg-app-data-count')),
                        ])
                        self.total_count = None
                        self.init_count = None
                        self.address_count = None
                        self.address_withdraw_count = None
                        self.label_map_count = None
                        self.label_withdraw_count = None
                        self.label_release_count = None
                        self.label_request_count = None
                        self.label_abort_request_count = None
                        self.notification_count = None
                        self.keep_alive_count = None
                        self.iccp_rg_conn_count = None
                        self.iccp_rg_disconn_count = None
                        self.iccp_rg_notif_count = None
                        self.iccp_rg_app_data_count = None
                        self._segment_path = lambda: "message-out"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/stats-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut, ['total_count', 'init_count', 'address_count', 'address_withdraw_count', 'label_map_count', 'label_withdraw_count', 'label_release_count', 'label_request_count', 'label_abort_request_count', 'notification_count', 'keep_alive_count', 'iccp_rg_conn_count', 'iccp_rg_disconn_count', 'iccp_rg_notif_count', 'iccp_rg_app_data_count'], name, value)


                class MessageIn(Entity):
                    """
                    MPLS LDP message received counters from this
                    neighbor.
                    
                    .. attribute:: total_count
                    
                    	Total count of all messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_count
                    
                    	Init message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_count
                    
                    	Address message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_withdraw_count
                    
                    	Address withdraw count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_map_count
                    
                    	Label map count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_withdraw_count
                    
                    	Label withdraw count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_release_count
                    
                    	Label release count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_request_count
                    
                    	Label request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_abort_request_count
                    
                    	Label abort request count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification_count
                    
                    	Notification count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_count
                    
                    	Keepalive count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_conn_count
                    
                    	ICCP RG Connect count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_disconn_count
                    
                    	ICCP RG Disconnect count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_notif_count
                    
                    	ICCP RG Notify count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_app_data_count
                    
                    	ICCP RG App Data count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn, self).__init__()

                        self.yang_name = "message-in"
                        self.yang_parent_name = "stats-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('total_count', YLeaf(YType.uint32, 'total-count')),
                            ('init_count', YLeaf(YType.uint32, 'init-count')),
                            ('address_count', YLeaf(YType.uint32, 'address-count')),
                            ('address_withdraw_count', YLeaf(YType.uint32, 'address-withdraw-count')),
                            ('label_map_count', YLeaf(YType.uint32, 'label-map-count')),
                            ('label_withdraw_count', YLeaf(YType.uint32, 'label-withdraw-count')),
                            ('label_release_count', YLeaf(YType.uint32, 'label-release-count')),
                            ('label_request_count', YLeaf(YType.uint32, 'label-request-count')),
                            ('label_abort_request_count', YLeaf(YType.uint32, 'label-abort-request-count')),
                            ('notification_count', YLeaf(YType.uint32, 'notification-count')),
                            ('keep_alive_count', YLeaf(YType.uint32, 'keep-alive-count')),
                            ('iccp_rg_conn_count', YLeaf(YType.uint32, 'iccp-rg-conn-count')),
                            ('iccp_rg_disconn_count', YLeaf(YType.uint32, 'iccp-rg-disconn-count')),
                            ('iccp_rg_notif_count', YLeaf(YType.uint32, 'iccp-rg-notif-count')),
                            ('iccp_rg_app_data_count', YLeaf(YType.uint32, 'iccp-rg-app-data-count')),
                        ])
                        self.total_count = None
                        self.init_count = None
                        self.address_count = None
                        self.address_withdraw_count = None
                        self.label_map_count = None
                        self.label_withdraw_count = None
                        self.label_release_count = None
                        self.label_request_count = None
                        self.label_abort_request_count = None
                        self.notification_count = None
                        self.keep_alive_count = None
                        self.iccp_rg_conn_count = None
                        self.iccp_rg_disconn_count = None
                        self.iccp_rg_notif_count = None
                        self.iccp_rg_app_data_count = None
                        self._segment_path = lambda: "message-in"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/stats-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn, ['total_count', 'init_count', 'address_count', 'address_withdraw_count', 'label_map_count', 'label_withdraw_count', 'label_release_count', 'label_request_count', 'label_abort_request_count', 'notification_count', 'keep_alive_count', 'iccp_rg_conn_count', 'iccp_rg_disconn_count', 'iccp_rg_notif_count', 'iccp_rg_app_data_count'], name, value)


            class Backoffs(Entity):
                """
                LDP Backoff Information
                
                .. attribute:: backoff_seconds
                
                	Current neighbor backoff count in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: waiting_seconds
                
                	Current neighbor backoff waiting count in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Neighbors.Backoffs, self).__init__()

                    self.yang_name = "backoffs"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('backoff_seconds', YLeaf(YType.uint32, 'backoff-seconds')),
                        ('waiting_seconds', YLeaf(YType.uint32, 'waiting-seconds')),
                    ])
                    self.backoff_seconds = None
                    self.waiting_seconds = None
                    self._segment_path = lambda: "backoffs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.Backoffs, ['backoff_seconds', 'waiting_seconds'], name, value)


            class NsrNbrDetail(Entity):
                """
                This is the LDP NSR state for this neighbor.
                
                .. attribute:: nsr_state
                
                	Non\-Stop Routing State
                	**type**\:  :py:class:`NsrStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrStatus>`
                
                .. attribute:: nsr_nbr_sync_state
                
                	NSR Sync State
                	**type**\:  :py:class:`NsrPeerSyncState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrPeerSyncState>`
                
                .. attribute:: nsr_nbr_last_sync_error
                
                	This is the last NSR sync error recieved. It indicates the last reason the sync failed even if the sync has now succeeded. This allows this information to be viewed when the state is flapping, even if the syncronization is successful at the time of the query
                	**type**\:  :py:class:`NsrPeerSyncErr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrPeerSyncErr>`
                
                .. attribute:: nsr_nbr_last_sync_nack_reason
                
                	Last NSR sync NACK reason
                	**type**\:  :py:class:`NsrSyncNackRsn <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrSyncNackRsn>`
                
                .. attribute:: nsr_nbr_pend_label_req_resps
                
                	Pending Label\-Request responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_pend_label_withdraw_resps
                
                	Pending Label\-Withdraw responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_pend_lcl_addr_withdraw_acks
                
                	Pending Local Address Withdraw Acks\:
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_reqs_created
                
                	In label Request Records created
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_reqs_freed
                
                	In label Request Records freed
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_withdraw_created
                
                	In label Withdraw Records created
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_withdraw_freed
                
                	In label Withdraw Records freed
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_lcl_addr_withdraw_set
                
                	Local Address Withdraw set
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_lcl_addr_withdraw_cleared
                
                	Local Address Withdraw cleared
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_xmit_ctxt_enq
                
                	Transmit contexts enqueued
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_xmit_ctxt_deq
                
                	Transmit contexts dequeued
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: nbr_sess
                
                	This container holds session information about the sessions between these two neighbors
                	**type**\:  :py:class:`NbrSess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess>`
                
                .. attribute:: path_vector_limit
                
                	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this Peer is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this Peer is enabled and the Path Vector Limit is this value
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail, self).__init__()

                    self.yang_name = "nsr-nbr-detail"
                    self.yang_parent_name = "neighbors"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("nbr-sess", ("nbr_sess", MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nsr_state', YLeaf(YType.identityref, 'nsr-state')),
                        ('nsr_nbr_sync_state', YLeaf(YType.identityref, 'nsr-nbr-sync-state')),
                        ('nsr_nbr_last_sync_error', YLeaf(YType.identityref, 'nsr-nbr-last-sync-error')),
                        ('nsr_nbr_last_sync_nack_reason', YLeaf(YType.identityref, 'nsr-nbr-last-sync-nack-reason')),
                        ('nsr_nbr_pend_label_req_resps', YLeaf(YType.uint32, 'nsr-nbr-pend-label-req-resps')),
                        ('nsr_nbr_pend_label_withdraw_resps', YLeaf(YType.uint32, 'nsr-nbr-pend-label-withdraw-resps')),
                        ('nsr_nbr_pend_lcl_addr_withdraw_acks', YLeaf(YType.uint32, 'nsr-nbr-pend-lcl-addr-withdraw-acks')),
                        ('nsr_nbr_in_label_reqs_created', YLeaf(YType.uint32, 'nsr-nbr-in-label-reqs-created')),
                        ('nsr_nbr_in_label_reqs_freed', YLeaf(YType.uint32, 'nsr-nbr-in-label-reqs-freed')),
                        ('nsr_nbr_in_label_withdraw_created', YLeaf(YType.uint32, 'nsr-nbr-in-label-withdraw-created')),
                        ('nsr_nbr_in_label_withdraw_freed', YLeaf(YType.uint32, 'nsr-nbr-in-label-withdraw-freed')),
                        ('nsr_nbr_lcl_addr_withdraw_set', YLeaf(YType.uint32, 'nsr-nbr-lcl-addr-withdraw-set')),
                        ('nsr_nbr_lcl_addr_withdraw_cleared', YLeaf(YType.uint32, 'nsr-nbr-lcl-addr-withdraw-cleared')),
                        ('nsr_nbr_xmit_ctxt_enq', YLeaf(YType.uint32, 'nsr-nbr-xmit-ctxt-enq')),
                        ('nsr_nbr_xmit_ctxt_deq', YLeaf(YType.uint32, 'nsr-nbr-xmit-ctxt-deq')),
                        ('path_vector_limit', YLeaf(YType.int32, 'path-vector-limit')),
                    ])
                    self.nsr_state = None
                    self.nsr_nbr_sync_state = None
                    self.nsr_nbr_last_sync_error = None
                    self.nsr_nbr_last_sync_nack_reason = None
                    self.nsr_nbr_pend_label_req_resps = None
                    self.nsr_nbr_pend_label_withdraw_resps = None
                    self.nsr_nbr_pend_lcl_addr_withdraw_acks = None
                    self.nsr_nbr_in_label_reqs_created = None
                    self.nsr_nbr_in_label_reqs_freed = None
                    self.nsr_nbr_in_label_withdraw_created = None
                    self.nsr_nbr_in_label_withdraw_freed = None
                    self.nsr_nbr_lcl_addr_withdraw_set = None
                    self.nsr_nbr_lcl_addr_withdraw_cleared = None
                    self.nsr_nbr_xmit_ctxt_enq = None
                    self.nsr_nbr_xmit_ctxt_deq = None
                    self.path_vector_limit = None

                    self.nbr_sess = MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess()
                    self.nbr_sess.parent = self
                    self._children_name_map["nbr_sess"] = "nbr-sess"
                    self._children_yang_names.add("nbr-sess")
                    self._segment_path = lambda: "nsr-nbr-detail"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail, ['nsr_state', 'nsr_nbr_sync_state', 'nsr_nbr_last_sync_error', 'nsr_nbr_last_sync_nack_reason', 'nsr_nbr_pend_label_req_resps', 'nsr_nbr_pend_label_withdraw_resps', 'nsr_nbr_pend_lcl_addr_withdraw_acks', 'nsr_nbr_in_label_reqs_created', 'nsr_nbr_in_label_reqs_freed', 'nsr_nbr_in_label_withdraw_created', 'nsr_nbr_in_label_withdraw_freed', 'nsr_nbr_lcl_addr_withdraw_set', 'nsr_nbr_lcl_addr_withdraw_cleared', 'nsr_nbr_xmit_ctxt_enq', 'nsr_nbr_xmit_ctxt_deq', 'path_vector_limit'], name, value)


                class NbrSess(Entity):
                    """
                    This container holds session information about the
                    sessions between these two neighbors.
                    
                    .. attribute:: last_stat_change
                    
                    	The value of sysUpTime at the time this Session entered its current state as denoted by the SessionState object
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	The current state of the session, all of the states 1 to 5 are based on the state machine for session negotiation behavior
                    	**type**\:  :py:class:`State <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess.State>`
                    
                    .. attribute:: keep_alive_remain
                    
                    	The keep alive hold time remaining for this session in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: keep_alive_time
                    
                    	The negotiated KeepAlive Time which represents the amount of seconds between keep alive messages.  The EntityKeepAliveHoldTimer related to this Session is the value that was proposed as the KeepAlive Time for this session.  This value is negotiated during session initialization between the entity's proposed value (i.e., the value configured in EntityKeepAliveHoldTimer) and the peer's proposed KeepAlive Hold Timer value. This value is the smaller of the two proposed values
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**units**\: seconds
                    
                    .. attribute:: max_pdu
                    
                    	The value of maximum allowable length for LDP PDUs this session.  This value may have been negotiated for during the Session Initialization.  This object is related to the EntityMaxPduLength object.  The EntityMaxPduLength object specifies the requested LDP PDU length, and this object reflects the negotiated LDP PDU length between the Entity and the Peer
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    	**units**\: octets
                    
                    .. attribute:: discon_time
                    
                    	The value of sysUpTime on the most recent occasion at which any one or more of this session's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this session of any counter32 object contained in the session\-stats table.  The initial value of this object is the value of sysUpTime when the entry was created in this table.  Also, a command generator can distinguish when a session between a given Entity and Peer goes away and a new session is established.  This value would change and thus indicate to the command generator that this is a different session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_mess_err
                    
                    	This object counts the number of Unknown Message Type Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_tlv
                    
                    	This object counts the number of Unknown TLV Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess, self).__init__()

                        self.yang_name = "nbr-sess"
                        self.yang_parent_name = "nsr-nbr-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('last_stat_change', YLeaf(YType.uint32, 'last-stat-change')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('keep_alive_remain', YLeaf(YType.uint32, 'keep-alive-remain')),
                            ('keep_alive_time', YLeaf(YType.uint32, 'keep-alive-time')),
                            ('max_pdu', YLeaf(YType.uint32, 'max-pdu')),
                            ('discon_time', YLeaf(YType.uint32, 'discon-time')),
                            ('unknown_mess_err', YLeaf(YType.uint32, 'unknown-mess-err')),
                            ('unknown_tlv', YLeaf(YType.uint32, 'unknown-tlv')),
                        ])
                        self.last_stat_change = None
                        self.state = None
                        self.keep_alive_remain = None
                        self.keep_alive_time = None
                        self.max_pdu = None
                        self.discon_time = None
                        self.unknown_mess_err = None
                        self.unknown_tlv = None
                        self._segment_path = lambda: "nbr-sess"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/neighbors/nsr-nbr-detail/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess, ['last_stat_change', 'state', 'keep_alive_remain', 'keep_alive_time', 'max_pdu', 'discon_time', 'unknown_mess_err', 'unknown_tlv'], name, value)

                    class State(Enum):
                        """
                        State (Enum Class)

                        The current state of the session, all of the

                        states 1 to 5 are based on the state machine

                        for session negotiation behavior.

                        .. data:: nonexistent = 1

                        	State: nonexistent.

                        .. data:: initialized = 2

                        	State: initialized.

                        .. data:: openrec = 3

                        	State: openrec.

                        .. data:: opensent = 4

                        	State: opensent.

                        .. data:: operational = 5

                        	State: operational.

                        """

                        nonexistent = Enum.YLeaf(1, "nonexistent")

                        initialized = Enum.YLeaf(2, "initialized")

                        openrec = Enum.YLeaf(3, "openrec")

                        opensent = Enum.YLeaf(4, "opensent")

                        operational = Enum.YLeaf(5, "operational")



        class LabelRanges(Entity):
            """
            This contaions holds all the label ranges in use
            by this LDP instance.
            
            .. attribute:: label_range
            
            	This entry contains a single range of labels represented by the configured Upper and Lower Bounds pairs.  NOTE\: there is NO corresponding LDP message which relates to the information in this table, however, this table does provide a way for a user to 'reserve' a generic label range.  NOTE\:  The ranges for a specific LDP Entity are UNIQUE and non\-overlapping
            	**type**\: list of  		 :py:class:`LabelRange <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.LabelRanges.LabelRange>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpState.LabelRanges, self).__init__()

                self.yang_name = "label-ranges"
                self.yang_parent_name = "mpls-ldp-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("label-range", ("label_range", MplsLdp.MplsLdpState.LabelRanges.LabelRange))])
                self._leafs = OrderedDict()

                self.label_range = YList(self)
                self._segment_path = lambda: "label-ranges"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpState.LabelRanges, [], name, value)


            class LabelRange(Entity):
                """
                This entry contains a single range of labels
                represented by the configured Upper and Lower
                Bounds pairs.  NOTE\: there is NO corresponding
                LDP message which relates to the information
                in this table, however, this table does provide
                a way for a user to 'reserve' a generic label
                range.
                
                NOTE\:  The ranges for a specific LDP Entity
                are UNIQUE and non\-overlapping.
                
                .. attribute:: lr_min  (key)
                
                	The minimum label configured for this range
                	**type**\: int
                
                	**range:** 0..1048575
                
                .. attribute:: lr_max  (key)
                
                	The maximum label configured for this range
                	**type**\: int
                
                	**range:** 0..1048575
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpState.LabelRanges.LabelRange, self).__init__()

                    self.yang_name = "label-range"
                    self.yang_parent_name = "label-ranges"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['lr_min','lr_max']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lr_min', YLeaf(YType.uint32, 'lr-min')),
                        ('lr_max', YLeaf(YType.uint32, 'lr-max')),
                    ])
                    self.lr_min = None
                    self.lr_max = None
                    self._segment_path = lambda: "label-range" + "[lr-min='" + str(self.lr_min) + "']" + "[lr-max='" + str(self.lr_max) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-state/label-ranges/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpState.LabelRanges.LabelRange, ['lr_min', 'lr_max'], name, value)


    class MplsLdpConfig(Entity):
        """
        MPLS LDP Configuration.
        
        .. attribute:: global_cfg
        
        	This contains hold all MPLS LDP Configuration with Global scope. These values affect the entire LSR unless overiddden by a parameter with a more localized scope
        	**type**\:  :py:class:`GlobalCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg>`
        
        .. attribute:: nbr_table
        
        	This container holds the list of neighbor configuration parameters
        	**type**\:  :py:class:`NbrTable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable>`
        
        .. attribute:: passwords
        
        	This holds the MPLS LDP password configuration for use with LDP neighbors
        	**type**\:  :py:class:`Passwords <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Passwords>`
        
        .. attribute:: session
        
        	Configure session parameters
        	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Session>`
        
        .. attribute:: label_cfg
        
        	This container holds the label allocation and advertisement configuration for the LDP Label Information Base. These control what prefixes may be allocated and advertised to peers
        	**type**\:  :py:class:`LabelCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.LabelCfg>`
        
        .. attribute:: discovery
        
        	LDP discovery
        	**type**\:  :py:class:`Discovery <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery>`
        
        .. attribute:: graceful_restart
        
        	Configure LDP Graceful Restart
        	**type**\:  :py:class:`GracefulRestart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GracefulRestart>`
        
        .. attribute:: logging
        
        	Enable LDP logging
        	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging>`
        
        .. attribute:: interfaces
        
        	MPLS LDP Interface configuration commands
        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces>`
        
        .. attribute:: routing
        
        	This containter provides the MPLS LDP config for routing protocols from which it can obtain addresses to associate with labels
        	**type**\:  :py:class:`Routing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Routing>`
        
        .. attribute:: dual_stack
        
        	This container holds the configuration of dual IPv4 and IPv6 stack peers
        	**type**\:  :py:class:`DualStack <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.DualStack>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(MplsLdp.MplsLdpConfig, self).__init__()

            self.yang_name = "mpls-ldp-config"
            self.yang_parent_name = "mpls-ldp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("global-cfg", ("global_cfg", MplsLdp.MplsLdpConfig.GlobalCfg)), ("nbr-table", ("nbr_table", MplsLdp.MplsLdpConfig.NbrTable)), ("passwords", ("passwords", MplsLdp.MplsLdpConfig.Passwords)), ("session", ("session", MplsLdp.MplsLdpConfig.Session)), ("label-cfg", ("label_cfg", MplsLdp.MplsLdpConfig.LabelCfg)), ("discovery", ("discovery", MplsLdp.MplsLdpConfig.Discovery)), ("graceful-restart", ("graceful_restart", MplsLdp.MplsLdpConfig.GracefulRestart)), ("logging", ("logging", MplsLdp.MplsLdpConfig.Logging)), ("interfaces", ("interfaces", MplsLdp.MplsLdpConfig.Interfaces)), ("routing", ("routing", MplsLdp.MplsLdpConfig.Routing)), ("dual-stack", ("dual_stack", MplsLdp.MplsLdpConfig.DualStack))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.global_cfg = MplsLdp.MplsLdpConfig.GlobalCfg()
            self.global_cfg.parent = self
            self._children_name_map["global_cfg"] = "global-cfg"
            self._children_yang_names.add("global-cfg")

            self.nbr_table = MplsLdp.MplsLdpConfig.NbrTable()
            self.nbr_table.parent = self
            self._children_name_map["nbr_table"] = "nbr-table"
            self._children_yang_names.add("nbr-table")

            self.passwords = MplsLdp.MplsLdpConfig.Passwords()
            self.passwords.parent = self
            self._children_name_map["passwords"] = "passwords"
            self._children_yang_names.add("passwords")

            self.session = MplsLdp.MplsLdpConfig.Session()
            self.session.parent = self
            self._children_name_map["session"] = "session"
            self._children_yang_names.add("session")

            self.label_cfg = MplsLdp.MplsLdpConfig.LabelCfg()
            self.label_cfg.parent = self
            self._children_name_map["label_cfg"] = "label-cfg"
            self._children_yang_names.add("label-cfg")

            self.discovery = MplsLdp.MplsLdpConfig.Discovery()
            self.discovery.parent = self
            self._children_name_map["discovery"] = "discovery"
            self._children_yang_names.add("discovery")

            self.graceful_restart = MplsLdp.MplsLdpConfig.GracefulRestart()
            self.graceful_restart.parent = self
            self._children_name_map["graceful_restart"] = "graceful-restart"
            self._children_yang_names.add("graceful-restart")

            self.logging = MplsLdp.MplsLdpConfig.Logging()
            self.logging.parent = self
            self._children_name_map["logging"] = "logging"
            self._children_yang_names.add("logging")

            self.interfaces = MplsLdp.MplsLdpConfig.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"
            self._children_yang_names.add("interfaces")

            self.routing = MplsLdp.MplsLdpConfig.Routing()
            self.routing.parent = self
            self._children_name_map["routing"] = "routing"
            self._children_yang_names.add("routing")

            self.dual_stack = MplsLdp.MplsLdpConfig.DualStack()
            self.dual_stack.parent = self
            self._children_name_map["dual_stack"] = "dual-stack"
            self._children_yang_names.add("dual-stack")
            self._segment_path = lambda: "mpls-ldp-config"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/%s" % self._segment_path()


        class GlobalCfg(Entity):
            """
            This contains hold all MPLS LDP Configuration with Global
            scope. These values affect the entire LSR unless
            overiddden by a parameter with a more localized scope.
            
            .. attribute:: shutdown
            
            	Writing this leaf tears down all LDP sessions, withdraws all outgoing labels from the forwarding plane, and frees all local labels that have been allocated
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable_nsr
            
            	This leaf controls whether Non\-Stop\-Routing should be enabled to include MPLS LDP
            	**type**\: bool
            
            .. attribute:: disable_quick_start
            
            	When set to true, disable LDP discovery's quick start mode for this LSR
            	**type**\: bool
            
            .. attribute:: loop_detection
            
            	This leaf enables or disables Loop Detection globally for the LSR
            	**type**\: bool
            
            .. attribute:: admin_status
            
            	This leaf controls the administrative status of LDP for this LSR. If set to disable, then all LDP activity will be disabled and all LDP sessions with peers will terminate. The LDP configuration will remain intact.  When the admin status is set back to 'enable', then LDP will resume operations and attempt to establish new sessions with the peers
            	**type**\:  :py:class:`AdminStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.AdminStatus>`
            
            .. attribute:: dcsp_val
            
            	This sets the 6\-bit Differentiated Services Code Point (DSCP) value in the TCP packets for LDP messages being sent from the LSR
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: high_priority
            
            	This sets the priority within the LSR for TCP packets for LDP messages being sent from the LSR. They are given a higher transmission priorty and will avoid being queued behind lower priority messages
            	**type**\: bool
            
            .. attribute:: seconds
            
            	Time in seconds to delay IGP sync after session comes up
            	**type**\: int
            
            	**range:** 5..300
            
            	**units**\: second
            
            .. attribute:: disable_delay
            
            	This choice causes IGP sync up immediately upon session up
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: seconds_delay_proc
            
            	Time in seconds to delay IGP sync after session comes up
            	**type**\: int
            
            	**range:** 5..300
            
            	**units**\: second
            
            .. attribute:: disable_delay_proc
            
            	This choice causes IGP sync up immediately upon session up
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: router_id
            
            	Configuration for LDP Router ID (LDP ID)
            	**type**\: list of  		 :py:class:`RouterId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.RouterId>`
            
            .. attribute:: session
            
            	Configure session parameters. Session parameters effect the session between LDP peers once the session has been established
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Session>`
            
            .. attribute:: per_af
            
            	This container holds the global per address family configuration
            	**type**\:  :py:class:`PerAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.PerAf>`
            
            .. attribute:: protocol
            
            	This leaf defines the protocol to be used. The default is LDP
            	**type**\:  :py:class:`Protocol <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Protocol>`
            
            .. attribute:: init_sess_thresh
            
            	When attempting to establish a session with a given Peer, the given LDP Entity should send out the YANG notification, 'init\-sess\-thresh\-ex', when the number of Session Initialization messages sent exceeds this threshold.  The notification is used to notify an operator when this Entity and its Peer are possibly engaged in an endless sequence of messages as each NAKs the other's  Initialization messages with Error Notification messages.  Setting this threshold which triggers the notification is one way to notify the operator.  The notification should be generated each time this threshold is exceeded and for every subsequent Initialization message which is NAK'd with an Error Notification message after this threshold is exceeded.  A value of 0 (zero) for this object indicates that the threshold is infinity, thus the YANG notification will never be generated
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.GlobalCfg, self).__init__()

                self.yang_name = "global-cfg"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("session", ("session", MplsLdp.MplsLdpConfig.GlobalCfg.Session)), ("per-af", ("per_af", MplsLdp.MplsLdpConfig.GlobalCfg.PerAf))])
                self._child_list_classes = OrderedDict([("router-id", ("router_id", MplsLdp.MplsLdpConfig.GlobalCfg.RouterId))])
                self._leafs = OrderedDict([
                    ('shutdown', YLeaf(YType.empty, 'shutdown')),
                    ('enable_nsr', YLeaf(YType.boolean, 'enable-nsr')),
                    ('disable_quick_start', YLeaf(YType.boolean, 'disable-quick-start')),
                    ('loop_detection', YLeaf(YType.boolean, 'loop-detection')),
                    ('admin_status', YLeaf(YType.enumeration, 'admin-status')),
                    ('dcsp_val', YLeaf(YType.uint32, 'dcsp-val')),
                    ('high_priority', YLeaf(YType.boolean, 'high-priority')),
                    ('seconds', YLeaf(YType.uint32, 'seconds')),
                    ('disable_delay', YLeaf(YType.empty, 'disable-delay')),
                    ('seconds_delay_proc', YLeaf(YType.uint32, 'seconds-delay-proc')),
                    ('disable_delay_proc', YLeaf(YType.empty, 'disable-delay-proc')),
                    ('protocol', YLeaf(YType.enumeration, 'protocol')),
                    ('init_sess_thresh', YLeaf(YType.int32, 'init-sess-thresh')),
                ])
                self.shutdown = None
                self.enable_nsr = None
                self.disable_quick_start = None
                self.loop_detection = None
                self.admin_status = None
                self.dcsp_val = None
                self.high_priority = None
                self.seconds = None
                self.disable_delay = None
                self.seconds_delay_proc = None
                self.disable_delay_proc = None
                self.protocol = None
                self.init_sess_thresh = None

                self.session = MplsLdp.MplsLdpConfig.GlobalCfg.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.per_af = MplsLdp.MplsLdpConfig.GlobalCfg.PerAf()
                self.per_af.parent = self
                self._children_name_map["per_af"] = "per-af"
                self._children_yang_names.add("per-af")

                self.router_id = YList(self)
                self._segment_path = lambda: "global-cfg"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg, ['shutdown', 'enable_nsr', 'disable_quick_start', 'loop_detection', 'admin_status', 'dcsp_val', 'high_priority', 'seconds', 'disable_delay', 'seconds_delay_proc', 'disable_delay_proc', 'protocol', 'init_sess_thresh'], name, value)

            class AdminStatus(Enum):
                """
                AdminStatus (Enum Class)

                This leaf controls the administrative status of LDP for

                this LSR. If set to disable, then all LDP activity will

                be disabled and all LDP sessions with peers will

                terminate. The LDP configuration will remain intact.

                When the admin status is set back to 'enable', then

                LDP will resume operations and attempt to establish new

                sessions with the peers.

                .. data:: enable = 1

                	Enable LDP globablly on this LSR.

                .. data:: disable = 2

                	Disable LDP globablly on this LSR.

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")


            class Protocol(Enum):
                """
                Protocol (Enum Class)

                This leaf defines the protocol to be used. The default

                is LDP.

                .. data:: ldp = 1

                	This LSR should use the LDP tagging protocol.

                .. data:: tdp = 2

                	This LSR should use the TDP tagging protocol.

                .. data:: both = 3

                	This LSR should use the both LDP and TDP tagging

                	protocol.

                """

                ldp = Enum.YLeaf(1, "ldp")

                tdp = Enum.YLeaf(2, "tdp")

                both = Enum.YLeaf(3, "both")



            class RouterId(Entity):
                """
                Configuration for LDP Router ID (LDP ID)
                
                .. attribute:: vrf_name  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: lsr_id_if
                
                	This defines the interface to use for the LDP LSR identifier address for all sessions. The IP address of this interface will be used as the identifier
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: lsr_id_ip
                
                	This is the IP address to be used as the LDP LSR ID for all sessions
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: force
                
                	Force the router to use the specified identifier as the router ID more quickly
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.GlobalCfg.RouterId, self).__init__()

                    self.yang_name = "router-id"
                    self.yang_parent_name = "global-cfg"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('lsr_id_if', YLeaf(YType.str, 'lsr-id-if')),
                        ('lsr_id_ip', YLeaf(YType.str, 'lsr-id-ip')),
                        ('force', YLeaf(YType.empty, 'force')),
                    ])
                    self.vrf_name = None
                    self.lsr_id_if = None
                    self.lsr_id_ip = None
                    self.force = None
                    self._segment_path = lambda: "router-id" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/global-cfg/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg.RouterId, ['vrf_name', 'lsr_id_if', 'lsr_id_ip', 'force'], name, value)


            class Session(Entity):
                """
                Configure session parameters. Session parameters effect
                the session between LDP peers once the session has been
                established.
                
                .. attribute:: downstream_on_demand
                
                	This container holds config for Downstream on Demand. For it to be enabled, the Downstream on demand feature has to be configured on both peers of the session. If only one peer in the session has downstream\-on\-demand feature configured, then the session does not use downstream\-on\-demand mode. If, after, a label request is sent, and no remote label is received from the peer, the router will periodically resend the label request. After the peer advertises a label after receiving the label request, it will automatically readvertise the label if any label attribute changes subsequently
                	**type**\: list of  		 :py:class:`DownstreamOnDemand <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand>`
                
                .. attribute:: backoff_init
                
                	Initial session backoff time (seconds). The LDP backoff mechanism prevents two incompatibly configured label switch routers (LSRs) from engaging in an unthrottled sequence of session setup failures.  For example, an incompatibility arises when two neighboring routers attempt to perform LC\-ATM (label\-controlled ATM) but the two are using different ranges of VPI/VCI values for labels.  If a session setup attempt fails due to an incompatibility, each LSR delays its next attempt (that is, backs off), increasing the delay exponentially with each successive failure until the maximum backoff delay is reached.  The default settings correspond to the lowest settings for initial and maximum backoff values defined by the LDP protocol specification. You should change the settings from the default values only if such settings result in undesirable behavior
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 15
                
                .. attribute:: backoff_max
                
                	The maximum session backoff time (seconds) The LDP backoff mechanism prevents two incompatibly configured label switch routers (LSRs) from engaging in an unthrottled sequence of session setup failures.  For example, an incompatibility arises when two neighboring routers attempt to perform LC\-ATM (label\-controlled ATM) but the two are using different ranges of VPI/VCI values for labels.  If a session setup attempt fails due to an incompatibility, each LSR delays its next attempt (that is, backs off), increasing the delay exponentially with each successive failure until the maximum backoff delay is reached.  The default settings correspond to the lowest settings for initial and maximum backoff values defined by the LDP protocol specification. You should change the settings from the default values only if such settings result in undesirable behavior
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 15
                
                .. attribute:: seconds
                
                	Number from 15 to 2147483, that defines the time, in seconds, an LDP session is maintained in the absence of LDP messages from the session peer
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: infinite
                
                	If set to true, the session is held indefinitely in the absence of LDP messages from the peer
                	**type**\: bool
                
                .. attribute:: protection
                
                	Configure Session Protection parameters
                	**type**\:  :py:class:`Protection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.GlobalCfg.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "global-cfg"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("protection", ("protection", MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection))])
                    self._child_list_classes = OrderedDict([("downstream-on-demand", ("downstream_on_demand", MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand))])
                    self._leafs = OrderedDict([
                        ('backoff_init', YLeaf(YType.uint32, 'backoff-init')),
                        ('backoff_max', YLeaf(YType.uint32, 'backoff-max')),
                        ('seconds', YLeaf(YType.uint16, 'seconds')),
                        ('infinite', YLeaf(YType.boolean, 'infinite')),
                    ])
                    self.backoff_init = None
                    self.backoff_max = None
                    self.seconds = None
                    self.infinite = None

                    self.protection = MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection()
                    self.protection.parent = self
                    self._children_name_map["protection"] = "protection"
                    self._children_yang_names.add("protection")

                    self.downstream_on_demand = YList(self)
                    self._segment_path = lambda: "session"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/global-cfg/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg.Session, ['backoff_init', 'backoff_max', 'seconds', 'infinite'], name, value)


                class DownstreamOnDemand(Entity):
                    """
                    This container holds config for Downstream on Demand.
                    For it to be enabled, the Downstream on demand
                    feature has to be configured on both peers of the
                    session. If only one peer in the session has
                    downstream\-on\-demand feature configured, then the
                    session does not use downstream\-on\-demand mode.
                    If, after, a label request is sent, and no remote
                    label is received from the peer, the router will
                    periodically resend the label request. After the
                    peer advertises a label after receiving the label
                    request, it will automatically readvertise the label
                    if any label attribute changes subsequently.
                    
                    .. attribute:: vrf_name  (key)
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\: str
                    
                    .. attribute:: enabled
                    
                    	Enable Downstream on Demand for this LSR. In this mode a label is not advertised to a peer, unless the peer explicitly requests it. At the same time, since the peer does not automatically advertise labels, the label request is sent whenever the next\-hop points out to a peer that no remote label has been assigned
                    	**type**\: bool
                    
                    .. attribute:: filter
                    
                    	This filter contains a list of peer IDs that are configured for downstream\-on\-demand mode. When the filter is changed or configured, the list of established neighbors is traversed. If a session's downstream\-on\-demand configuration has changed, the session is reset in order that the new down\-stream\-on\-demand mode can be configured. The reason for resetting the session is to ensure that the labels are properly advertised between the peers. When a new session is established, the ACL is verified to determine whether the session should negotiate for downstream\-on\-demand mode. If the filter string is configured and the corresponding filter does not exist or is empty, then downstream\-on\-demand mode is not configured for any neighbor. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand, self).__init__()

                        self.yang_name = "downstream-on-demand"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ('enabled', YLeaf(YType.boolean, 'enabled')),
                            ('filter', YLeaf(YType.str, 'filter')),
                        ])
                        self.vrf_name = None
                        self.enabled = None
                        self.filter = None
                        self._segment_path = lambda: "downstream-on-demand" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/global-cfg/session/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand, ['vrf_name', 'enabled', 'filter'], name, value)


                class Protection(Entity):
                    """
                    Configure Session Protection parameters
                    
                    .. attribute:: enable_prot
                    
                    	This is set true to enable session protection
                    	**type**\: bool
                    
                    .. attribute:: peer_filter
                    
                    	This is an optional filter to restrict session protection. If the string is null or unconfigured then session protection applied to all peers. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\: str
                    
                    .. attribute:: seconds
                    
                    	This is the sessiom holdup duration in seconds
                    	**type**\: int
                    
                    	**range:** 30..2147483
                    
                    .. attribute:: inf
                    
                    	This sessiom holdup duration is infinite
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection, self).__init__()

                        self.yang_name = "protection"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable_prot', YLeaf(YType.boolean, 'enable-prot')),
                            ('peer_filter', YLeaf(YType.str, 'peer-filter')),
                            ('seconds', YLeaf(YType.uint32, 'seconds')),
                            ('inf', YLeaf(YType.empty, 'inf')),
                        ])
                        self.enable_prot = None
                        self.peer_filter = None
                        self.seconds = None
                        self.inf = None
                        self._segment_path = lambda: "protection"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/global-cfg/session/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection, ['enable_prot', 'peer_filter', 'seconds', 'inf'], name, value)


            class PerAf(Entity):
                """
                This container holds the global per address family
                configuration.
                
                .. attribute:: af_cfg
                
                	This container holds the global per address family configuration
                	**type**\: list of  		 :py:class:`AfCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.GlobalCfg.PerAf, self).__init__()

                    self.yang_name = "per-af"
                    self.yang_parent_name = "global-cfg"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("af-cfg", ("af_cfg", MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg))])
                    self._leafs = OrderedDict()

                    self.af_cfg = YList(self)
                    self._segment_path = lambda: "per-af"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/global-cfg/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg.PerAf, [], name, value)


                class AfCfg(Entity):
                    """
                    This container holds the global per address family
                    configuration.
                    
                    .. attribute:: vrf_name  (key)
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\: str
                    
                    .. attribute:: af_name  (key)
                    
                    	Address Family name
                    	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                    
                    .. attribute:: default_route
                    
                    	When set true, this enables MPLS forwarding for the ip default route
                    	**type**\: bool
                    
                    .. attribute:: ipaddr
                    
                    	Advertise this address as the explicit address in LDP discovery hello messages and use it for LDP transport
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: interface
                    
                    	Advertise this interface's address as the explicit address in LDP discovery hello messages and use it for LDP transport
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: implicit
                    
                    	Do not advertise an explicit address in LDP discovery hello messages or advertise a default address. Use the default address for LDP transport
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg, self).__init__()

                        self.yang_name = "af-cfg"
                        self.yang_parent_name = "per-af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['vrf_name','af_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                            ('af_name', YLeaf(YType.enumeration, 'af-name')),
                            ('default_route', YLeaf(YType.boolean, 'default-route')),
                            ('ipaddr', YLeaf(YType.str, 'ipaddr')),
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('implicit', YLeaf(YType.empty, 'implicit')),
                        ])
                        self.vrf_name = None
                        self.af_name = None
                        self.default_route = None
                        self.ipaddr = None
                        self.interface = None
                        self.implicit = None
                        self._segment_path = lambda: "af-cfg" + "[vrf-name='" + str(self.vrf_name) + "']" + "[af-name='" + str(self.af_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/global-cfg/per-af/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg, ['vrf_name', 'af_name', 'default_route', 'ipaddr', 'interface', 'implicit'], name, value)


        class NbrTable(Entity):
            """
            This container holds the list of neighbor configuration
            parameters.
            
            .. attribute:: nbr_cfg
            
            	This entry holds the configuration of a single neighbor identified by the IP address of that neighbor
            	**type**\: list of  		 :py:class:`NbrCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable.NbrCfg>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.NbrTable, self).__init__()

                self.yang_name = "nbr-table"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("nbr-cfg", ("nbr_cfg", MplsLdp.MplsLdpConfig.NbrTable.NbrCfg))])
                self._leafs = OrderedDict()

                self.nbr_cfg = YList(self)
                self._segment_path = lambda: "nbr-table"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.NbrTable, [], name, value)


            class NbrCfg(Entity):
                """
                This entry holds the configuration of a single neighbor
                identified by the IP address of that neighbor.
                
                .. attribute:: nbr_vrf  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: nbr_ip  (key)
                
                	The IP address for the LDP neighbor. This may be IPv4 or IPv6
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: admin_status
                
                	The administrative status of this neighbor. If this object is changed from 'enable' to 'disable' and this entity has already attempted to establish contact with a neighbor, a 'tear\-down' for that session is issued and the session and all information related to that session ceases to exist).  When the admin status is set back to 'enable', then this Entity will attempt to establish a new session with the neighbor
                	**type**\:  :py:class:`AdminStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.AdminStatus>`
                
                .. attribute:: implicit_withdraw
                
                	Enable LDP implicit withdraw label for this peer
                	**type**\: bool
                
                .. attribute:: targeted
                
                	Establish or delete a targeted session
                	**type**\: bool
                
                .. attribute:: label_protocol
                
                	This leaf defines the protocol to be used. The default is LDP
                	**type**\:  :py:class:`LabelProtocol <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.LabelProtocol>`
                
                .. attribute:: label_binding_filter
                
                	Accept only labels matching this filter. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                .. attribute:: password
                
                	Enables password authentication and stores the password using a cryptographic hash
                	**type**\: str
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.NbrTable.NbrCfg, self).__init__()

                    self.yang_name = "nbr-cfg"
                    self.yang_parent_name = "nbr-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['nbr_vrf','nbr_ip']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nbr_vrf', YLeaf(YType.str, 'nbr-vrf')),
                        ('nbr_ip', YLeaf(YType.str, 'nbr-ip')),
                        ('admin_status', YLeaf(YType.enumeration, 'admin-status')),
                        ('implicit_withdraw', YLeaf(YType.boolean, 'implicit-withdraw')),
                        ('targeted', YLeaf(YType.boolean, 'targeted')),
                        ('label_protocol', YLeaf(YType.enumeration, 'label-protocol')),
                        ('label_binding_filter', YLeaf(YType.str, 'label-binding-filter')),
                        ('password', YLeaf(YType.str, 'password')),
                    ])
                    self.nbr_vrf = None
                    self.nbr_ip = None
                    self.admin_status = None
                    self.implicit_withdraw = None
                    self.targeted = None
                    self.label_protocol = None
                    self.label_binding_filter = None
                    self.password = None
                    self._segment_path = lambda: "nbr-cfg" + "[nbr-vrf='" + str(self.nbr_vrf) + "']" + "[nbr-ip='" + str(self.nbr_ip) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/nbr-table/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.NbrTable.NbrCfg, ['nbr_vrf', 'nbr_ip', 'admin_status', 'implicit_withdraw', 'targeted', 'label_protocol', 'label_binding_filter', 'password'], name, value)

                class AdminStatus(Enum):
                    """
                    AdminStatus (Enum Class)

                    The administrative status of this neighbor.

                    If this object is changed from 'enable' to 'disable'

                    and this entity has already attempted to establish

                    contact with a neighbor, a 'tear\-down' for that session

                    is issued and the session and all information related

                    to that session ceases to exist).

                    When the admin status is set back to 'enable', then

                    this Entity will attempt to establish a new session

                    with the neighbor.

                    .. data:: enable = 1

                    	Set the administrative status of this neighbor

                    	to enabled.

                    .. data:: disable = 2

                    	Set the administrative status of this neighbor

                    	to disabled.

                    """

                    enable = Enum.YLeaf(1, "enable")

                    disable = Enum.YLeaf(2, "disable")


                class LabelProtocol(Enum):
                    """
                    LabelProtocol (Enum Class)

                    This leaf defines the protocol to be used. The default

                    is LDP.

                    .. data:: ldp = 1

                    	This LSR should use the LDP tagging protocol.

                    .. data:: tdp = 2

                    	This LSR should use the TDP tagging protocol.

                    """

                    ldp = Enum.YLeaf(1, "ldp")

                    tdp = Enum.YLeaf(2, "tdp")



        class Passwords(Entity):
            """
            This holds the MPLS LDP password configuration for use
            with LDP neighbors.
            
            .. attribute:: password
            
            	This holds the MPLS LDP password configuration for use with a single LDP neighbor or group of LDP neighbors
            	**type**\: list of  		 :py:class:`Password <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Passwords.Password>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.Passwords, self).__init__()

                self.yang_name = "passwords"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("password", ("password", MplsLdp.MplsLdpConfig.Passwords.Password))])
                self._leafs = OrderedDict()

                self.password = YList(self)
                self._segment_path = lambda: "passwords"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.Passwords, [], name, value)


            class Password(Entity):
                """
                This holds the MPLS LDP password configuration for use
                with a single LDP neighbor or group of LDP neighbors.
                
                .. attribute:: nbr_vrf  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: nbr_id  (key)
                
                	This leaf holds the neighbor id for this password. This id may be an lsr\-id, an ip\-address, or a filter describing a group of neighbors
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                .. attribute:: password_num  (key)
                
                	This is a user\-assigned unique number identifying a password for this neighbor or group of neighbors. Multiple passwords may be assigned to a neighbor. If that is the case, each password is tried starting with the lowest number to the highest until a passsword matches or the list is exhausted
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pass_required
                
                	This leaf is set true if the password is required and false if the password is not required
                	**type**\: bool
                
                .. attribute:: clear_pass
                
                	This is a clear\-text (non\-encrypted password to be used with the neighbor
                	**type**\: str
                
                .. attribute:: encrypt_pass
                
                	This is an encrypted password to be used with the neighbor
                	**type**\: str
                
                .. attribute:: keychain_pass
                
                	This is a keychain identifier, which identifies an separately configured keychain to be used with the neighbor neighbor
                	**type**\: str
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Passwords.Password, self).__init__()

                    self.yang_name = "password"
                    self.yang_parent_name = "passwords"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['nbr_vrf','nbr_id','password_num']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nbr_vrf', YLeaf(YType.str, 'nbr-vrf')),
                        ('nbr_id', YLeaf(YType.str, 'nbr-id')),
                        ('password_num', YLeaf(YType.uint32, 'password-num')),
                        ('pass_required', YLeaf(YType.boolean, 'pass-required')),
                        ('clear_pass', YLeaf(YType.str, 'clear-pass')),
                        ('encrypt_pass', YLeaf(YType.str, 'encrypt-pass')),
                        ('keychain_pass', YLeaf(YType.str, 'keychain-pass')),
                    ])
                    self.nbr_vrf = None
                    self.nbr_id = None
                    self.password_num = None
                    self.pass_required = None
                    self.clear_pass = None
                    self.encrypt_pass = None
                    self.keychain_pass = None
                    self._segment_path = lambda: "password" + "[nbr-vrf='" + str(self.nbr_vrf) + "']" + "[nbr-id='" + str(self.nbr_id) + "']" + "[password-num='" + str(self.password_num) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/passwords/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.Passwords.Password, ['nbr_vrf', 'nbr_id', 'password_num', 'pass_required', 'clear_pass', 'encrypt_pass', 'keychain_pass'], name, value)


        class Session(Entity):
            """
            Configure session parameters
            
            .. attribute:: backoff
            
            	Initial session backoff time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**default value**\: 15
            
            .. attribute:: seconds
            
            	Session holdtime in seconds
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: infinite
            
            	Ignore LDP session holdtime
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('backoff', YLeaf(YType.uint32, 'backoff')),
                    ('seconds', YLeaf(YType.uint16, 'seconds')),
                    ('infinite', YLeaf(YType.empty, 'infinite')),
                ])
                self.backoff = None
                self.seconds = None
                self.infinite = None
                self._segment_path = lambda: "session"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.Session, ['backoff', 'seconds', 'infinite'], name, value)


        class LabelCfg(Entity):
            """
            This container holds the label allocation and
            advertisement configuration for the LDP Label Information
            Base. These control what prefixes may be allocated and
            advertised to peers.
            
            .. attribute:: label_af_cfg
            
            	This is an allocation filter and advertisement filters for LDP labels in this address family
            	**type**\: list of  		 :py:class:`LabelAfCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.LabelCfg, self).__init__()

                self.yang_name = "label-cfg"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("label-af-cfg", ("label_af_cfg", MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg))])
                self._leafs = OrderedDict()

                self.label_af_cfg = YList(self)
                self._segment_path = lambda: "label-cfg"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.LabelCfg, [], name, value)


            class LabelAfCfg(Entity):
                """
                This is an allocation filter and advertisement filters
                for LDP labels in this address family.
                
                .. attribute:: vrf_name  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: af_name  (key)
                
                	Address Family name
                	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                
                .. attribute:: prefix_filter
                
                	This contains the filter name for this label's prefix. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..64
                
                .. attribute:: host_route_enable
                
                	True if this LSR should allocate host\-routes only
                	**type**\: bool
                
                .. attribute:: advt_filter
                
                	MPLS LDP Label advertisement filter restrictions
                	**type**\: list of  		 :py:class:`AdvtFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg, self).__init__()

                    self.yang_name = "label-af-cfg"
                    self.yang_parent_name = "label-cfg"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name','af_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("advt-filter", ("advt_filter", MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter))])
                    self._leafs = OrderedDict([
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                        ('af_name', YLeaf(YType.enumeration, 'af-name')),
                        ('prefix_filter', YLeaf(YType.str, 'prefix-filter')),
                        ('host_route_enable', YLeaf(YType.boolean, 'host-route-enable')),
                    ])
                    self.vrf_name = None
                    self.af_name = None
                    self.prefix_filter = None
                    self.host_route_enable = None

                    self.advt_filter = YList(self)
                    self._segment_path = lambda: "label-af-cfg" + "[vrf-name='" + str(self.vrf_name) + "']" + "[af-name='" + str(self.af_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/label-cfg/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg, ['vrf_name', 'af_name', 'prefix_filter', 'host_route_enable'], name, value)


                class AdvtFilter(Entity):
                    """
                    MPLS LDP Label advertisement filter restrictions.
                    
                    .. attribute:: prefix_filter  (key)
                    
                    	This contains the filter name for this label's prefix.  The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: peer_filter  (key)
                    
                    	This contains the filter name for this label's Peer. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: interface  (key)
                    
                    	This is an optional interface that may be used to restrict the scope of the label advertisement
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: adv_label_cfg
                    
                    	This leaf controls what type of label is advertised for matching prefixes to the matching peers
                    	**type**\:  :py:class:`AdvLabelType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AdvLabelType>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter, self).__init__()

                        self.yang_name = "advt-filter"
                        self.yang_parent_name = "label-af-cfg"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['prefix_filter','peer_filter','interface']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix_filter', YLeaf(YType.str, 'prefix-filter')),
                            ('peer_filter', YLeaf(YType.str, 'peer-filter')),
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('adv_label_cfg', YLeaf(YType.enumeration, 'adv-label-cfg')),
                        ])
                        self.prefix_filter = None
                        self.peer_filter = None
                        self.interface = None
                        self.adv_label_cfg = None
                        self._segment_path = lambda: "advt-filter" + "[prefix-filter='" + str(self.prefix_filter) + "']" + "[peer-filter='" + str(self.peer_filter) + "']" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter, ['prefix_filter', 'peer_filter', 'interface', 'adv_label_cfg'], name, value)


        class Discovery(Entity):
            """
            LDP discovery
            
            .. attribute:: link_hello
            
            	This container holds the parameters for the non\-targeted link hello
            	**type**\:  :py:class:`LinkHello <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.LinkHello>`
            
            .. attribute:: targeted_hello
            
            	This container holds the parameters for the targeted link hello
            	**type**\:  :py:class:`TargetedHello <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.TargetedHello>`
            
            .. attribute:: instance_tlv
            
            	Set this leaf to true to disable transmit and receive processing for Type\-Length\-Value (TLV) in the discovery messages
            	**type**\: bool
            
            .. attribute:: int_trans_addrs
            
            	This list contains the per\-interface transport addresses, which overide the global and default values
            	**type**\:  :py:class:`IntTransAddrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.Discovery, self).__init__()

                self.yang_name = "discovery"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("link-hello", ("link_hello", MplsLdp.MplsLdpConfig.Discovery.LinkHello)), ("targeted-hello", ("targeted_hello", MplsLdp.MplsLdpConfig.Discovery.TargetedHello)), ("int-trans-addrs", ("int_trans_addrs", MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('instance_tlv', YLeaf(YType.boolean, 'instance-tlv')),
                ])
                self.instance_tlv = None

                self.link_hello = MplsLdp.MplsLdpConfig.Discovery.LinkHello()
                self.link_hello.parent = self
                self._children_name_map["link_hello"] = "link-hello"
                self._children_yang_names.add("link-hello")

                self.targeted_hello = MplsLdp.MplsLdpConfig.Discovery.TargetedHello()
                self.targeted_hello.parent = self
                self._children_name_map["targeted_hello"] = "targeted-hello"
                self._children_yang_names.add("targeted-hello")

                self.int_trans_addrs = MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs()
                self.int_trans_addrs.parent = self
                self._children_name_map["int_trans_addrs"] = "int-trans-addrs"
                self._children_yang_names.add("int-trans-addrs")
                self._segment_path = lambda: "discovery"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.Discovery, ['instance_tlv'], name, value)


            class LinkHello(Entity):
                """
                This container holds the parameters for the non\-targeted
                link hello.
                
                .. attribute:: holdtime
                
                	LDP discovery link hello holdtime in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: interval
                
                	LDP discovery link hello interval in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Discovery.LinkHello, self).__init__()

                    self.yang_name = "link-hello"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('holdtime', YLeaf(YType.uint16, 'holdtime')),
                        ('interval', YLeaf(YType.uint16, 'interval')),
                    ])
                    self.holdtime = None
                    self.interval = None
                    self._segment_path = lambda: "link-hello"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.Discovery.LinkHello, ['holdtime', 'interval'], name, value)


            class TargetedHello(Entity):
                """
                This container holds the parameters for the targeted
                link hello.
                
                .. attribute:: holdtime
                
                	LDP discovery targeted hello holdtime in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: interval
                
                	LDP discovery targeted hello interval in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: enable
                
                	Set to true if targeted hello messages may be accepted
                	**type**\: bool
                
                .. attribute:: accept
                
                	Enables router to respond to requests for targeted hello messages
                	**type**\:  :py:class:`Accept <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Discovery.TargetedHello, self).__init__()

                    self.yang_name = "targeted-hello"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("accept", ("accept", MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('holdtime', YLeaf(YType.uint16, 'holdtime')),
                        ('interval', YLeaf(YType.uint16, 'interval')),
                        ('enable', YLeaf(YType.boolean, 'enable')),
                    ])
                    self.holdtime = None
                    self.interval = None
                    self.enable = None

                    self.accept = MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept()
                    self.accept.parent = self
                    self._children_name_map["accept"] = "accept"
                    self._children_yang_names.add("accept")
                    self._segment_path = lambda: "targeted-hello"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.Discovery.TargetedHello, ['holdtime', 'interval', 'enable'], name, value)


                class Accept(Entity):
                    """
                    Enables router to respond to requests for targeted
                    hello messages
                    
                    .. attribute:: enable
                    
                    	Set to true if targeted hello messages may be accepted
                    	**type**\: bool
                    
                    .. attribute:: src_filter
                    
                    	Only respond to requests for targeted hello messages from sources matching this filter. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept, self).__init__()

                        self.yang_name = "accept"
                        self.yang_parent_name = "targeted-hello"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.boolean, 'enable')),
                            ('src_filter', YLeaf(YType.str, 'src-filter')),
                        ])
                        self.enable = None
                        self.src_filter = None
                        self._segment_path = lambda: "accept"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/discovery/targeted-hello/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept, ['enable', 'src_filter'], name, value)


            class IntTransAddrs(Entity):
                """
                This list contains the per\-interface transport
                addresses, which overide the global and default
                values.
                
                .. attribute:: int_trans_addr
                
                	This entry contains the per\-interface transport addresses, which overide the global and default values
                	**type**\: list of  		 :py:class:`IntTransAddr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs, self).__init__()

                    self.yang_name = "int-trans-addrs"
                    self.yang_parent_name = "discovery"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("int-trans-addr", ("int_trans_addr", MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr))])
                    self._leafs = OrderedDict()

                    self.int_trans_addr = YList(self)
                    self._segment_path = lambda: "int-trans-addrs"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/discovery/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs, [], name, value)


                class IntTransAddr(Entity):
                    """
                    This entry contains the per\-interface transport
                    addresses, which overide the global and default
                    values.
                    
                    .. attribute:: af_name  (key)
                    
                    	Address Family name
                    	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                    
                    .. attribute:: int_name  (key)
                    
                    	The Interface Name
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: trans_ip
                    
                    	Advertise this address as the address in LDP discovery hello messages and use it for LDP transport
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: trans_int
                    
                    	Advertise this interface's address as the address in LDP discovery hello messages and use it for LDP transport
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr, self).__init__()

                        self.yang_name = "int-trans-addr"
                        self.yang_parent_name = "int-trans-addrs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['af_name','int_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', YLeaf(YType.enumeration, 'af-name')),
                            ('int_name', YLeaf(YType.str, 'int-name')),
                            ('trans_ip', YLeaf(YType.str, 'trans-ip')),
                            ('trans_int', YLeaf(YType.str, 'trans-int')),
                        ])
                        self.af_name = None
                        self.int_name = None
                        self.trans_ip = None
                        self.trans_int = None
                        self._segment_path = lambda: "int-trans-addr" + "[af-name='" + str(self.af_name) + "']" + "[int-name='" + str(self.int_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/discovery/int-trans-addrs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr, ['af_name', 'int_name', 'trans_ip', 'trans_int'], name, value)


        class GracefulRestart(Entity):
            """
            Configure LDP Graceful Restart
            
            .. attribute:: is_graceful_restartable
            
            	Enable graceful restartable
            	**type**\: bool
            
            .. attribute:: forwarding_holding
            
            	Specifies the amount of time the MPLS LDP forwarding state must be preserved after the control plane restarts
            	**type**\: int
            
            	**range:** 5..300
            
            	**units**\: seconds
            
            .. attribute:: max_recovery
            
            	Amount of time (in seconds) that the router should hold stale label\-FEC bindings after an LDP session has been reestablished
            	**type**\: int
            
            	**range:** 5..300
            
            	**units**\: seconds
            
            .. attribute:: nbr_liveness
            
            	Amount of time (in seconds) that the router must wait for an LDP session to be reestablished
            	**type**\: int
            
            	**range:** 5..300
            
            	**units**\: seconds
            
            .. attribute:: helper
            
            	This contains the filter name for peers for which this LSR will act as a graceful\-restart helper
            	**type**\: list of  		 :py:class:`Helper <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GracefulRestart.Helper>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("helper", ("helper", MplsLdp.MplsLdpConfig.GracefulRestart.Helper))])
                self._leafs = OrderedDict([
                    ('is_graceful_restartable', YLeaf(YType.boolean, 'is-graceful-restartable')),
                    ('forwarding_holding', YLeaf(YType.uint32, 'forwarding-holding')),
                    ('max_recovery', YLeaf(YType.uint32, 'max-recovery')),
                    ('nbr_liveness', YLeaf(YType.uint32, 'nbr-liveness')),
                ])
                self.is_graceful_restartable = None
                self.forwarding_holding = None
                self.max_recovery = None
                self.nbr_liveness = None

                self.helper = YList(self)
                self._segment_path = lambda: "graceful-restart"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.GracefulRestart, ['is_graceful_restartable', 'forwarding_holding', 'max_recovery', 'nbr_liveness'], name, value)


            class Helper(Entity):
                """
                This contains the filter name for peers for which this
                LSR will act as a graceful\-restart helper.
                
                .. attribute:: helper_vrf  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: helper_filter  (key)
                
                	This contains the filter name for peers for which this LSR will act as a graceful\-restart helper. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\: str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.GracefulRestart.Helper, self).__init__()

                    self.yang_name = "helper"
                    self.yang_parent_name = "graceful-restart"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['helper_vrf','helper_filter']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('helper_vrf', YLeaf(YType.str, 'helper-vrf')),
                        ('helper_filter', YLeaf(YType.str, 'helper-filter')),
                    ])
                    self.helper_vrf = None
                    self.helper_filter = None
                    self._segment_path = lambda: "helper" + "[helper-vrf='" + str(self.helper_vrf) + "']" + "[helper-filter='" + str(self.helper_filter) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/graceful-restart/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.GracefulRestart.Helper, ['helper_vrf', 'helper_filter'], name, value)


        class Logging(Entity):
            """
            Enable LDP logging
            
            .. attribute:: graceful_restart
            
            	Enable logging of graceful\-restart messages
            	**type**\: bool
            
            .. attribute:: neighbor
            
            	Enable logging of neighbor messages
            	**type**\: bool
            
            .. attribute:: nsr
            
            	Enable logging of nsr messages
            	**type**\: bool
            
            .. attribute:: adjacency
            
            	Enable logging of adjacency messages
            	**type**\: bool
            
            .. attribute:: session_protection
            
            	Enable logging of session\-protection messages
            	**type**\: bool
            
            .. attribute:: password
            
            	Enable logging of password messages
            	**type**\:  :py:class:`Password <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging.Password>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("password", ("password", MplsLdp.MplsLdpConfig.Logging.Password))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('graceful_restart', YLeaf(YType.boolean, 'graceful-restart')),
                    ('neighbor', YLeaf(YType.boolean, 'neighbor')),
                    ('nsr', YLeaf(YType.boolean, 'nsr')),
                    ('adjacency', YLeaf(YType.boolean, 'adjacency')),
                    ('session_protection', YLeaf(YType.boolean, 'session-protection')),
                ])
                self.graceful_restart = None
                self.neighbor = None
                self.nsr = None
                self.adjacency = None
                self.session_protection = None

                self.password = MplsLdp.MplsLdpConfig.Logging.Password()
                self.password.parent = self
                self._children_name_map["password"] = "password"
                self._children_yang_names.add("password")
                self._segment_path = lambda: "logging"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.Logging, ['graceful_restart', 'neighbor', 'nsr', 'adjacency', 'session_protection'], name, value)


            class Password(Entity):
                """
                Enable logging of password messages.
                
                .. attribute:: config_msg
                
                	Log MPLS LDP password configuration changes
                	**type**\:  :py:class:`ConfigMsg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg>`
                
                .. attribute:: rollover_msg
                
                	Log MPLS LDP password rollover messages
                	**type**\:  :py:class:`RolloverMsg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Logging.Password, self).__init__()

                    self.yang_name = "password"
                    self.yang_parent_name = "logging"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("config-msg", ("config_msg", MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg)), ("rollover-msg", ("rollover_msg", MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.config_msg = MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg()
                    self.config_msg.parent = self
                    self._children_name_map["config_msg"] = "config-msg"
                    self._children_yang_names.add("config-msg")

                    self.rollover_msg = MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg()
                    self.rollover_msg.parent = self
                    self._children_name_map["rollover_msg"] = "rollover-msg"
                    self._children_yang_names.add("rollover-msg")
                    self._segment_path = lambda: "password"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/logging/%s" % self._segment_path()


                class ConfigMsg(Entity):
                    """
                    Log MPLS LDP password configuration changes.
                    
                    .. attribute:: enable
                    
                    	Log MPLS LDP password configuration changes
                    	**type**\: bool
                    
                    .. attribute:: rate_limit
                    
                    	This is the number of messages per minute to limit the logging. A value of 0 indicates no limits on the number of logged messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg, self).__init__()

                        self.yang_name = "config-msg"
                        self.yang_parent_name = "password"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.boolean, 'enable')),
                            ('rate_limit', YLeaf(YType.uint32, 'rate-limit')),
                        ])
                        self.enable = None
                        self.rate_limit = None
                        self._segment_path = lambda: "config-msg"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/logging/password/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg, ['enable', 'rate_limit'], name, value)


                class RolloverMsg(Entity):
                    """
                    Log MPLS LDP password rollover messages.
                    
                    .. attribute:: enable
                    
                    	Log MPLS LDP password rollover messages
                    	**type**\: bool
                    
                    .. attribute:: rate_limit
                    
                    	This is the number of messages per minute to limit the logging. A value of 0 indicates no limits on the number of logged messages
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg, self).__init__()

                        self.yang_name = "rollover-msg"
                        self.yang_parent_name = "password"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', YLeaf(YType.boolean, 'enable')),
                            ('rate_limit', YLeaf(YType.uint32, 'rate-limit')),
                        ])
                        self.enable = None
                        self.rate_limit = None
                        self._segment_path = lambda: "rollover-msg"
                        self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/logging/password/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg, ['enable', 'rate_limit'], name, value)


        class Interfaces(Entity):
            """
            MPLS LDP Interface configuration commands.
            
            .. attribute:: interface
            
            	MPLS LDP Interface configuration commands. Where a corresponding global configuration command exists, the interface level command will take precedence when configured
            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface", ("interface", MplsLdp.MplsLdpConfig.Interfaces.Interface))])
                self._leafs = OrderedDict()

                self.interface = YList(self)
                self._segment_path = lambda: "interfaces"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.Interfaces, [], name, value)


            class Interface(Entity):
                """
                MPLS LDP Interface configuration commands. Where a
                corresponding global configuration command exists, the
                interface level command will take precedence when
                configured.
                
                .. attribute:: vrf  (key)
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\: str
                
                .. attribute:: interface  (key)
                
                	The Interface Name
                	**type**\: str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: link_hello_int
                
                	LDP discovery link hello interval in seconds for this interface. This value overides the global setting
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                	**default value**\: 5
                
                .. attribute:: link_hello_hold
                
                	LDP discovery link hello holdtime in seconds for this interface. This value overides the global setting
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                	**default value**\: 15
                
                .. attribute:: disable_quick_start_int
                
                	When set to true, disable LDP discovery's quick start mode for this interface
                	**type**\: bool
                
                .. attribute:: seconds
                
                	Time in seconds to delay IGP sync after session comes up
                	**type**\: int
                
                	**range:** 5..300
                
                	**units**\: second
                
                .. attribute:: disable_delay
                
                	This choice causes IGP sync up immediately upon session up
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf','interface']
                    self._child_container_classes = OrderedDict([("afs", ("afs", MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf', YLeaf(YType.str, 'vrf')),
                        ('interface', YLeaf(YType.str, 'interface')),
                        ('link_hello_int', YLeaf(YType.uint32, 'link-hello-int')),
                        ('link_hello_hold', YLeaf(YType.uint32, 'link-hello-hold')),
                        ('disable_quick_start_int', YLeaf(YType.boolean, 'disable-quick-start-int')),
                        ('seconds', YLeaf(YType.uint32, 'seconds')),
                        ('disable_delay', YLeaf(YType.empty, 'disable-delay')),
                    ])
                    self.vrf = None
                    self.interface = None
                    self.link_hello_int = None
                    self.link_hello_hold = None
                    self.disable_quick_start_int = None
                    self.seconds = None
                    self.disable_delay = None

                    self.afs = MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                    self._children_yang_names.add("afs")
                    self._segment_path = lambda: "interface" + "[vrf='" + str(self.vrf) + "']" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/interfaces/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.Interfaces.Interface, ['vrf', 'interface', 'link_hello_int', 'link_hello_hold', 'disable_quick_start_int', 'seconds', 'disable_delay'], name, value)


                class Afs(Entity):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	MPLS LDP Operational data for this Address Family
                    	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs, self).__init__()

                        self.yang_name = "afs"
                        self.yang_parent_name = "interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("af", ("af", MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af))])
                        self._leafs = OrderedDict()

                        self.af = YList(self)
                        self._segment_path = lambda: "afs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs, [], name, value)


                    class Af(Entity):
                        """
                        MPLS LDP Operational data for this Address Family.
                        
                        .. attribute:: af_name  (key)
                        
                        	Address Family name
                        	**type**\:  :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.Af>`
                        
                        .. attribute:: enable
                        
                        	This is set true to enable LDP on this interface
                        	**type**\: bool
                        
                        .. attribute:: bgp_redist
                        
                        	MPLS LDP configuration for protocol redistribution. By default, redistribution of BGP routes is disabled. It can be enabled for all BGP routes or for a specific AS. Also it can be redistributed to all LDP peers or to a filtered group of peers
                        	**type**\:  :py:class:`BgpRedist <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist>`
                        
                        .. attribute:: autoconfig_disable
                        
                        	True if LDP autoconfig is explicitly disabled on this interface
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            super(MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af, self).__init__()

                            self.yang_name = "af"
                            self.yang_parent_name = "afs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['af_name']
                            self._child_container_classes = OrderedDict([("bgp-redist", ("bgp_redist", MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                ('enable', YLeaf(YType.boolean, 'enable')),
                                ('autoconfig_disable', YLeaf(YType.boolean, 'autoconfig-disable')),
                            ])
                            self.af_name = None
                            self.enable = None
                            self.autoconfig_disable = None

                            self.bgp_redist = MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist()
                            self.bgp_redist.parent = self
                            self._children_name_map["bgp_redist"] = "bgp-redist"
                            self._children_yang_names.add("bgp-redist")
                            self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af, ['af_name', 'enable', 'autoconfig_disable'], name, value)


                        class BgpRedist(Entity):
                            """
                            MPLS LDP configuration for protocol
                            redistribution. By default, redistribution of BGP
                            routes is disabled. It can be enabled for all
                            BGP routes or for a specific AS. Also it can be
                            redistributed to all LDP peers or to a filtered
                            group of peers.
                            
                            .. attribute:: as_xx
                            
                            	First half of BGP AS number in XX.YY format.  Mandatory Must be a non\-zero value if second half is zero
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: as_yy
                            
                            	Second half of BGP AS number in XX.YY format. Mandatory Must be a non\-zero value if first half is zero
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: advertise_to
                            
                            	Filter of neighbors to receive BGP route redistributions from LDP. If the list is empty or unset, all LDP neighbors will receive redistributions
                            	**type**\: str
                            
                            .. attribute:: enable
                            
                            	This is set true to allow LDP to redistribute BGP routes
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                super(MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist, self).__init__()

                                self.yang_name = "bgp-redist"
                                self.yang_parent_name = "af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('as_xx', YLeaf(YType.uint32, 'as-xx')),
                                    ('as_yy', YLeaf(YType.uint32, 'as-yy')),
                                    ('advertise_to', YLeaf(YType.str, 'advertise-to')),
                                    ('enable', YLeaf(YType.boolean, 'enable')),
                                ])
                                self.as_xx = None
                                self.as_yy = None
                                self.advertise_to = None
                                self.enable = None
                                self._segment_path = lambda: "bgp-redist"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist, ['as_xx', 'as_yy', 'advertise_to', 'enable'], name, value)


        class Routing(Entity):
            """
            This containter provides the MPLS LDP config for routing
            protocols from which it can obtain addresses to
            associate with labels.
            
            .. attribute:: routing_inst
            
            	This entry provides the MPLS LDP config for this routing instance
            	**type**\: list of  		 :py:class:`RoutingInst <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Routing.RoutingInst>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.Routing, self).__init__()

                self.yang_name = "routing"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("routing-inst", ("routing_inst", MplsLdp.MplsLdpConfig.Routing.RoutingInst))])
                self._leafs = OrderedDict()

                self.routing_inst = YList(self)
                self._segment_path = lambda: "routing"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.Routing, [], name, value)


            class RoutingInst(Entity):
                """
                This entry provides the MPLS LDP config for this
                routing instance.
                
                .. attribute:: routing_inst_name  (key)
                
                	Name of the routing instance for which this MPLS LDP configuration applies
                	**type**\: str
                
                .. attribute:: autoconfig_enable
                
                	This leaf enables or disables LDP for all interfaces covered by this routing instance subject to the autoconfig\-scope
                	**type**\: bool
                
                .. attribute:: area_id
                
                	This leaf restricts the LDP Autoconfiguration feature to enable LDP on interfaces belonging to an OSPF process for a specific area. If no area is specified, then this applies to all interfaces associated with the. If an area ID is specified, then only interfaces associated with that OSPF area are automatically enabled with LDP. Any interface\-specific ldp configuration will overide this setting for that interface
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: level_id
                
                	This leaf restricts the LDP Autoconfiguration feature to enable LDP on interfaces belonging to an ISIS process for a specific level. If no level is specified, then this applies to all interfaces associated with the. If a level is specified, then only interfaces associated with that ISIS level are automatically enabled with LDP. Any interface\-specific ldp configuration will overide this setting for that interface
                	**type**\:  :py:class:`LevelId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Routing.RoutingInst.LevelId>`
                
                .. attribute:: sync
                
                	When set to true this enables LDP IGP synchronization. Without syncrhonization, packet loss can occur because the actions of the IGP and LDP are not synchronized
                	**type**\: bool
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(MplsLdp.MplsLdpConfig.Routing.RoutingInst, self).__init__()

                    self.yang_name = "routing-inst"
                    self.yang_parent_name = "routing"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['routing_inst_name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('routing_inst_name', YLeaf(YType.str, 'routing-inst-name')),
                        ('autoconfig_enable', YLeaf(YType.boolean, 'autoconfig-enable')),
                        ('area_id', YLeaf(YType.uint32, 'area-id')),
                        ('level_id', YLeaf(YType.enumeration, 'level-id')),
                        ('sync', YLeaf(YType.boolean, 'sync')),
                    ])
                    self.routing_inst_name = None
                    self.autoconfig_enable = None
                    self.area_id = None
                    self.level_id = None
                    self.sync = None
                    self._segment_path = lambda: "routing-inst" + "[routing-inst-name='" + str(self.routing_inst_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/routing/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsLdp.MplsLdpConfig.Routing.RoutingInst, ['routing_inst_name', 'autoconfig_enable', 'area_id', 'level_id', 'sync'], name, value)

                class LevelId(Enum):
                    """
                    LevelId (Enum Class)

                    This leaf restricts the LDP Autoconfiguration

                    feature to enable LDP on interfaces belonging to

                    an ISIS process for a specific level. If no level

                    is specified, then this applies to all interfaces

                    associated with the. If a level is specified,

                    then only interfaces associated with that ISIS

                    level are automatically enabled with LDP.

                    Any interface\-specific ldp configuration will

                    overide this setting for that interface.

                    .. data:: level_1 = 1

                    	This leaf restricts the LDP Autoconfiguration

                    	feature to enable LDP on interfaces belonging

                    	to an IS-IS process level 1.

                    	Any interface-specific ldp configuration will

                    	overide this setting for that interface.

                    .. data:: level_2 = 2

                    	This leaf restricts the LDP Autoconfiguration

                    	feature to enable LDP on interfaces belonging

                    	to an IS-IS process level 1.

                    	Any interface-specific ldp configuration will

                    	overide this setting for that interface.

                    .. data:: level_1_2 = 3

                    	This leaf restricts the LDP Autoconfiguration

                    	feature to enable LDP on interfaces belonging

                    	to an IS-IS process level 2.

                    	Any interface-specific ldp configuration will

                    	overide this setting for that interface.

                    """

                    level_1 = Enum.YLeaf(1, "level-1")

                    level_2 = Enum.YLeaf(2, "level-2")

                    level_1_2 = Enum.YLeaf(3, "level-1-2")



        class DualStack(Entity):
            """
            This container holds the configuration of dual IPv4 and
            IPv6 stack peers.
            
            .. attribute:: max_wait
            
            	Wait time in seconds (0 indicates no preference)
            	**type**\: int
            
            	**range:** 0..60
            
            .. attribute:: prefer_ipv4_peers
            
            	This contains the filter name for peers where IPv4 connections are preferred over IPv6 connections. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
            	**type**\: str
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(MplsLdp.MplsLdpConfig.DualStack, self).__init__()

                self.yang_name = "dual-stack"
                self.yang_parent_name = "mpls-ldp-config"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('max_wait', YLeaf(YType.uint32, 'max-wait')),
                    ('prefer_ipv4_peers', YLeaf(YType.str, 'prefer-ipv4-peers')),
                ])
                self.max_wait = None
                self.prefer_ipv4_peers = None
                self._segment_path = lambda: "dual-stack"
                self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:mpls-ldp/mpls-ldp-config/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsLdp.MplsLdpConfig.DualStack, ['max_wait', 'prefer_ipv4_peers'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsLdp()
        return self._top_entity

class ClearMsgCounters(Entity):
    """
    This RPC clears the LDP message counters for either a single
    neighbor or for all neighbors.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearMsgCounters.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearMsgCounters.Output>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(ClearMsgCounters, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-msg-counters"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-ldp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearMsgCounters.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ClearMsgCounters.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-mpls-ldp:clear-msg-counters"


    class Input(Entity):
        """
        
        
        .. attribute:: vrf_name
        
        	This contains the VRF Name, where 'default' is used for the default vrf
        	**type**\: str
        
        .. attribute:: nbr_ip
        
        	LSR ID of the neighbor
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: all
        
        	Clear information for all neighbors
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(ClearMsgCounters.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-msg-counters"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('nbr_ip', YLeaf(YType.str, 'nbr-ip')),
                ('all', YLeaf(YType.empty, 'all')),
            ])
            self.vrf_name = None
            self.nbr_ip = None
            self.all = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:clear-msg-counters/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearMsgCounters.Input, ['vrf_name', 'nbr_ip', 'all'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: status
        
        	Return status will be 'OK' on success or an explanation string on failure
        	**type**\: str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(ClearMsgCounters.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear-msg-counters"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('status', YLeaf(YType.str, 'status')),
            ])
            self.status = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:clear-msg-counters/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearMsgCounters.Output, ['status'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearMsgCounters()
        return self._top_entity

class RestartNeighbor(Entity):
    """
    This RPC restarts a single LDP session or all LDP sessions,
    but does not restart the LDP process itself, if the device
    supports that capability.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RestartNeighbor.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RestartNeighbor.Output>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RestartNeighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "restart-neighbor"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-ldp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = RestartNeighbor.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = RestartNeighbor.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-mpls-ldp:restart-neighbor"


    class Input(Entity):
        """
        
        
        .. attribute:: vrf_name
        
        	This contains the VRF Name, where 'default' is used for the default vrf
        	**type**\: str
        
        .. attribute:: nbr_ip
        
        	LSR ID of the neighbor
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: all
        
        	Restart sessions for all neighbors
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(RestartNeighbor.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "restart-neighbor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('nbr_ip', YLeaf(YType.str, 'nbr-ip')),
                ('all', YLeaf(YType.empty, 'all')),
            ])
            self.vrf_name = None
            self.nbr_ip = None
            self.all = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:restart-neighbor/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RestartNeighbor.Input, ['vrf_name', 'nbr_ip', 'all'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: status
        
        	Return status will be 'OK' on success or an explanation string on failure
        	**type**\: str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(RestartNeighbor.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "restart-neighbor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('status', YLeaf(YType.str, 'status')),
            ])
            self.status = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:restart-neighbor/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RestartNeighbor.Output, ['status'], name, value)

    def clone_ptr(self):
        self._top_entity = RestartNeighbor()
        return self._top_entity

class ClearForwarding(Entity):
    """
    This command resets LDP installed forwarding state for all
    prefixes or a given prefix. It is useful when installed 
    LDP forwarding state needs to be reprogrammed in LSD and
    MPLS forwarding.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearForwarding.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearForwarding.Output>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(ClearForwarding, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-forwarding"
        self.yang_parent_name = "Cisco-IOS-XE-mpls-ldp"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearForwarding.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ClearForwarding.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "Cisco-IOS-XE-mpls-ldp:clear-forwarding"


    class Input(Entity):
        """
        
        
        .. attribute:: vrf_name
        
        	This contains the VRF Name, where 'default' is used for the default vrf
        	**type**\: str
        
        .. attribute:: prefix_ip
        
        	This case provides the IP prefix for the forwarding entry whose data should be cleared
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: all
        
        	This case is used to clear the forwarding entries for all prefixes
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(ClearForwarding.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-forwarding"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                ('prefix_ip', YLeaf(YType.str, 'prefix-ip')),
                ('all', YLeaf(YType.empty, 'all')),
            ])
            self.vrf_name = None
            self.prefix_ip = None
            self.all = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:clear-forwarding/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearForwarding.Input, ['vrf_name', 'prefix_ip', 'all'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: status
        
        	Return status will be 'OK' on success or an explanatory string on failure
        	**type**\: str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(ClearForwarding.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear-forwarding"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('status', YLeaf(YType.str, 'status')),
            ])
            self.status = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "Cisco-IOS-XE-mpls-ldp:clear-forwarding/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearForwarding.Output, ['status'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearForwarding()
        return self._top_entity

class NsrSyncNackRsnNone(Identity):
    """
    None
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnNone, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-none")


class NsrSyncNackRsnTblIdMismatch(Identity):
    """
    NSR failed with a table ID mismatch.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnTblIdMismatch, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-tbl-id-mismatch")


class NsrSyncNackRsnPpExists(Identity):
    """
    NSR failed with because pp already exists.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnPpExists, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-pp-exists")


class NsrSyncNackRsnMissingElem(Identity):
    """
    NSR failed due to a Missing Element.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnMissingElem, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-missing-elem")


class NsrSyncNackRsnNoPEndSock(Identity):
    """
    NSR failed because there was no P end socket.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnNoPEndSock, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-no-p-end-sock")


class NsrSyncNackRsnPEndSockNotSynced(Identity):
    """
    NSR failed because the P end sock was not synced.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnPEndSockNotSynced, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-p-end-sock-not-synced")


class NsrSyncNackRsnErrAdjAdd(Identity):
    """
    NSR failed due to an error adding the adjacency.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrAdjAdd, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-adj-add")


class NsrSyncNackRsnErrDhcAdd(Identity):
    """
    NSR failed with a error creating the directed hello control
    infrastructure.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrDhcAdd, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-dhc-add")


class NsrSyncNackRsnEnomem(Identity):
    """
    NSR failed due to an out of memory error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnEnomem, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-enomem")


class NsrSyncNackRsnErrTpCreate(Identity):
    """
    NSR failed creating the tp.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrTpCreate, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-tp-create")


class NsrSyncNackRsnErrPpCreate(Identity):
    """
    NSR failed creating the pp.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrPpCreate, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-pp-create")


class NsrSyncNackRsnErrAddrBind(Identity):
    """
    NSR failed to bind address.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrAddrBind, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-addr-bind")


class NsrSyncNackRsnErrRxBadPie(Identity):
    """
    NSR failed, received a bad PIE.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrRxBadPie, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-rx-bad-pie")


class NsrSyncNackRsnErrRxNotif(Identity):
    """
    NSR failed with a received notification error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrRxNotif, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-rx-notif")


class NsrSyncNackRsnErrRxUnexpOpen(Identity):
    """
    NSR failed due to an unexpected open.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrRxUnexpOpen, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-rx-unexp-open")


class NsrSyncNackRsnErrUnexpPeerDown(Identity):
    """
    NSR failed due to unexpected peer down.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrUnexpPeerDown, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-unexp-peer-down")


class NsrSyncNackRsnErrAppNotFound(Identity):
    """
    NSR failed due to app not found.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrAppNotFound, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-app-not-found")


class NsrSyncNackRsnErrAppInvalid(Identity):
    """
    NSR failed due to an app invalid error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnErrAppInvalid, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-err-app-invalid")


class NsrSyncNackRsnNoCtx(Identity):
    """
    NSR failed with a no context error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrSyncNackRsnNoCtx, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-sync-nack-rsn-no-ctx")


class NsrPeerSyncErrNone(Identity):
    """
    No error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrNone, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-none")


class NsrPeerSyncErrLdpSyncNack(Identity):
    """
    LDP Peer Sync failed, received sync nack.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrLdpSyncNack, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-ldp-sync-nack")


class NsrPeerSyncErrSyncPrep(Identity):
    """
    LDP Peer Sync failed, synch prep.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrSyncPrep, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-sync-prep")


class NsrPeerSyncErrTcpPeer(Identity):
    """
    LDP Peer Sync failed, tcp peer
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrTcpPeer, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-tcp-peer")


class NsrPeerSyncErrTcpGbl(Identity):
    """
    LDP Peer Sync failed, tcp gbl
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrTcpGbl, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-tcp-gbl")


class NsrPeerSyncErrLdpPeer(Identity):
    """
    LDP Peer Sync failed, ldp peer
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrLdpPeer, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-ldp-peer")


class NsrPeerSyncErrLdpGbl(Identity):
    """
    LDP Peer Sync failed, ldp gbl
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrLdpGbl, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-ldp-gbl")


class NsrPeerSyncErrAppFail(Identity):
    """
    LDP Peer Sync failed, app fail
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrPeerSyncErrAppFail, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-peer-sync-err-app-fail")


class IcpmTypeIccp(Identity):
    """
    ICCP Interchassis Communication Protocol.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IcpmTypeIccp, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:icpm-type-iccp")


class IccpTypeMlacp(Identity):
    """
    MLACP Multi\-chassic Link Aggregation Control Protocol.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IccpTypeMlacp, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:iccp-type-mlacp")


class LdpNsrPeerSyncStNone(Identity):
    """
    LDP NSR peer synchronization none.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LdpNsrPeerSyncStNone, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:ldp-nsr-peer-sync-st-none")


class LdpNsrPeerSyncStWait(Identity):
    """
    LDP NSR peer synchronization is wait.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LdpNsrPeerSyncStWait, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:ldp-nsr-peer-sync-st-wait")


class LdpNsrPeerSyncStReady(Identity):
    """
    LDP NSR peer synchronization is ready.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LdpNsrPeerSyncStReady, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:ldp-nsr-peer-sync-st-ready")


class LdpNsrPeerSyncStPrep(Identity):
    """
    LDP NSR peer synchronization is prep.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LdpNsrPeerSyncStPrep, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:ldp-nsr-peer-sync-st-prep")


class LdpNsrPeerSyncStAppWait(Identity):
    """
    LDP NSR peer synchronization is app wait.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LdpNsrPeerSyncStAppWait, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:ldp-nsr-peer-sync-st-app-wait")


class LdpNsrPeerSyncStOper(Identity):
    """
    LDP NSR peer synchronization is operational.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LdpNsrPeerSyncStOper, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:ldp-nsr-peer-sync-st-oper")


class NsrStatusReady(Identity):
    """
    Device is NSR Ready.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrStatusReady, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-status-ready")


class NsrStatusNotReady(Identity):
    """
    Device is not NSR Ready.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrStatusNotReady, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-status-not-ready")


class NsrStatusDisabled(Identity):
    """
    NSR is not enabled.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(NsrStatusDisabled, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:nsr-status-disabled")


class DownNbrReasonNa(Identity):
    """
    Not applicable, the neighbor is up..
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(DownNbrReasonNa, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:down-nbr-reason-na")


class DownNbrReasonNbrHold(Identity):
    """
    The neighbor sent error, hold time expired..
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(DownNbrReasonNbrHold, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:down-nbr-reason-nbr-hold")


class DownNbrReasonDiscHello(Identity):
    """
    The local discovery hello timer expired..
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(DownNbrReasonDiscHello, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:down-nbr-reason-disc-hello")


class RoutePathLblOwnerNone(Identity):
    """
    No label and no owner.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathLblOwnerNone, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-lbl-owner-none")


class RoutePathLblOwnerLdp(Identity):
    """
    Path outgoing label owned by LDP.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathLblOwnerLdp, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-lbl-owner-ldp")


class RoutePathLblOwnerBgp(Identity):
    """
    Path outgoing label owned by BGP.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathLblOwnerBgp, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-lbl-owner-bgp")


class RoutePathLblOwnerStatic(Identity):
    """
    Path outgoing label statically configured.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathLblOwnerStatic, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-lbl-owner-static")


class LabelTypeMpls(Identity):
    """
    The is an MPLS Label.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LabelTypeMpls, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:label-type-mpls")


class LabelTypeUnLabeled(Identity):
    """
    This is unlabeled
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LabelTypeUnLabeled, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:label-type-un-labeled")


class LabelTypeUnknown(Identity):
    """
    The label is unknown.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(LabelTypeUnknown, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:label-type-unknown")


class RoutePathIpNoFlag(Identity):
    """
    A primary path with no special flag/attribute
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathIpNoFlag, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-ip-no-flag")


class RoutePathIpProtected(Identity):
    """
    A primary path with LFA FRR protection
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathIpProtected, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-ip-protected")


class RoutePathIpBackup(Identity):
    """
    A non\-primary local LFA FRR (pure) backup path
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathIpBackup, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-ip-backup")


class RoutePathIpBackupRemote(Identity):
    """
    A non\-primary remote LFA FRR (pure) backup path
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathIpBackupRemote, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-ip-backup-remote")


class RoutePathIpBgpBackup(Identity):
    """
    A non\-primary BGP backup path
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(RoutePathIpBgpBackup, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:route-path-ip-bgp-backup")


class IgpSyncDownReasonNa(Identity):
    """
    Not Applicable.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReasonNa, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason-na")


class IgpSyncDownReasonNoHelloAdj(Identity):
    """
    No hello adjacency.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReasonNoHelloAdj, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason-no-hello-adj")


class IgpSyncDownReasonNoPeerSess(Identity):
    """
    No peer session.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReasonNoPeerSess, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason-no-peer-sess")


class IgpSyncDownReasonPeerUpdateNotDone(Identity):
    """
    Initial update to peer not done yet.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReasonPeerUpdateNotDone, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason-peer-update-not-done")


class IgpSyncDownReasonPeerUpdateNotReceived(Identity):
    """
    Initial update from peer not received yet.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReasonPeerUpdateNotReceived, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason-peer-update-not-received")


class IgpSyncDownReasonInternal(Identity):
    """
    Internal reason.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(IgpSyncDownReasonInternal, self).__init__("http://cisco.com/ns/yang/Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp", "Cisco-IOS-XE-mpls-ldp:igp-sync-down-reason-internal")


