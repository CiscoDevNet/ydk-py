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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AdjStateEnum(Enum):
    """
    AdjStateEnum

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

    nonex = 0

    unsol_op_pdg = 1

    deferred = 2

    estab = 3

    lib_exp_wait = 4

    destroyed = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['AdjStateEnum']


class AdvLabelTypeEnum(Enum):
    """
    AdvLabelTypeEnum

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

    use_lable = 1

    use_explicit = 2

    use_implicit = 3

    none = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['AdvLabelTypeEnum']


class AfEnum(Enum):
    """
    AfEnum

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

    ldp_af_none = 0

    ldp_af_ipv4 = 1

    ldp_af_ipv6 = 2

    ldp_af_ipv4_ipv6 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['AfEnum']


class AfIdEnum(Enum):
    """
    AfIdEnum

    LDP AF type

    .. data:: ldp_af_id_none = 0

    	No Address Family

    .. data:: ldp_af_id_ipv4 = 1

    	IPv4 AFI

    .. data:: ldp_af_id_ipv6 = 2

    	IPv6 AFI

    """

    ldp_af_id_none = 0

    ldp_af_id_ipv4 = 1

    ldp_af_id_ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['AfIdEnum']


class DhcStateEnum(Enum):
    """
    DhcStateEnum

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

    none = 0

    dhc_active = 1

    dhc_passive = 2

    dhc_active_passive = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['DhcStateEnum']


class IccpStateEnum(Enum):
    """
    IccpStateEnum

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

    nonexistent = 1

    initialized = 2

    capsent = 3

    caprec = 4

    connecting = 5

    operational = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IccpStateEnum']


class IgpSyncStateEnum(Enum):
    """
    IgpSyncStateEnum

    This is the IGP Synchronization State.

    .. data:: isync_ready = 0

    	Achieved

    .. data:: isync_not_ready = 1

    	Not achieved

    .. data:: isync_deferred = 2

    	Deferred due to interface delay or global

    	restart delay

    """

    isync_ready = 0

    isync_not_ready = 1

    isync_deferred = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncStateEnum']


class LocalLabelStateEnum(Enum):
    """
    LocalLabelStateEnum

    This id the MPLS LDP Local Label State Type.

    .. data:: local_label_state_none = 1

    	None

    .. data:: local_label_state_assigned = 2

    	Assigned

    .. data:: local_label_state_withdrawn = 3

    	Withdrawn

    """

    local_label_state_none = 1

    local_label_state_assigned = 2

    local_label_state_withdrawn = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LocalLabelStateEnum']


class LoopDetectionTypeEnum(Enum):
    """
    LoopDetectionTypeEnum

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

    none = 1

    other = 2

    hop_count = 3

    path_vector = 4

    hop_count_and_path_vector = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LoopDetectionTypeEnum']


class NbrBgpAdvtStateEnum(Enum):
    """
    NbrBgpAdvtStateEnum

    MPLS LDP Neighbor BGP Label Advertisement State

    Type.

    .. data:: not_applicable = 0

    	BGP Label Advertisement is not applicable.

    .. data:: permit = 1

    	BGP Label Advertisement is permitted.

    .. data:: deny = 2

    	BGP Label Advertisement denied.

    """

    not_applicable = 0

    permit = 1

    deny = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NbrBgpAdvtStateEnum']


class SessionStateEnum(Enum):
    """
    SessionStateEnum

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

    nonexistent = 1

    initialized = 2

    openrec = 3

    opensent = 4

    operational = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['SessionStateEnum']



class LabelTypeIdentity(object):
    """
    Base type for LDP Label Type
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LabelTypeIdentity']['meta_info']


class RoutePathLblOwnerIdentity(object):
    """
    Base Route path label owner type.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathLblOwnerIdentity']['meta_info']


class NsrPeerSyncStateIdentity(object):
    """
    Base identity for LDP NSR Peer Synchronization State.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncStateIdentity']['meta_info']


class RoutePathTypeIdentity(object):
    """
    Base type for Route path type.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathTypeIdentity']['meta_info']


class NsrStatusIdentity(object):
    """
    Base identity for Non\-Stop Routing State Type.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrStatusIdentity']['meta_info']


class IgpSyncDownReasonIdentity(object):
    """
    Base identity reason IGP Sync was not achieved.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonIdentity']['meta_info']


class IcpmTypeIdentity(object):
    """
    Base identity from which ICPM types can be derived. As this is
    an extensible protocol, new types are expected.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IcpmTypeIdentity']['meta_info']


class NsrPeerSyncErrIdentity(object):
    """
    Base for MPLS LDP NSR peer synchronization error types.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrIdentity']['meta_info']


class NsrSyncNackRsnIdentity(object):
    """
    Base identity from which LDP Non\-Stop Routing peer LDP
    synchronization nack reason identities are derived.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnIdentity']['meta_info']


class DownNbrReasonIdentity(object):
    """
    Base identity for the reason a neighbor is down.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['DownNbrReasonIdentity']['meta_info']


class IccpTypeIdentity(object):
    """
    Base identity from which ICCP types can be derived. As this is
    an extensible protocol, new types are expected.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IccpTypeIdentity']['meta_info']


class MplsLdp(object):
    """
    MPLS LDP configuration and operational data.
    
    .. attribute:: mpls_ldp_config
    
    	MPLS LDP Configuration
    	**type**\:   :py:class:`MplsLdpConfig <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig>`
    
    .. attribute:: mpls_ldp_state
    
    	MPLS LDP operational data
    	**type**\:   :py:class:`MplsLdpState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.mpls_ldp_config = MplsLdp.MplsLdpConfig()
        self.mpls_ldp_config.parent = self
        self.mpls_ldp_state = MplsLdp.MplsLdpState()
        self.mpls_ldp_state.parent = self


    class MplsLdpState(object):
        """
        MPLS LDP operational data.
        
        .. attribute:: backoff_parameters
        
        	MPLS LDP Session Backoff Information
        	**type**\:   :py:class:`BackoffParameters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.BackoffParameters>`
        
        .. attribute:: bindings
        
        	The detailed LDP Bindings
        	**type**\:   :py:class:`Bindings <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings>`
        
        .. attribute:: bindings_summary
        
        	Aggregate counters for the MPLS LDP LIB
        	**type**\:   :py:class:`BindingsSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.BindingsSummary>`
        
        .. attribute:: capabilities
        
        	LDP capability database information
        	**type**\:   :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Capabilities>`
        
        .. attribute:: discovery
        
        	The LDP Discovery operational state
        	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery>`
        
        .. attribute:: forwarding
        
        	Summary information regarding LDP forwarding setup and detailed LDP Forwarding rewrites
        	**type**\:   :py:class:`Forwarding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding>`
        
        .. attribute:: forwarding_summary
        
        	Summary information regarding LDP forwarding setup
        	**type**\:   :py:class:`ForwardingSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary>`
        
        .. attribute:: graceful_restart
        
        	MPLS LDP Graceful Restart Information
        	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.GracefulRestart>`
        
        .. attribute:: icpm_summary_all
        
        	Summary info for LDP ICPM/ICCP
        	**type**\:   :py:class:`IcpmSummaryAll <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll>`
        
        .. attribute:: label_ranges
        
        	This contaions holds all the label ranges in use by this LDP instance
        	**type**\:   :py:class:`LabelRanges <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.LabelRanges>`
        
        .. attribute:: neighbors
        
        	The LDP Neighbors Information
        	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors>`
        
        .. attribute:: nsr_summary_all
        
        	This is the LDP NSR summary for the device
        	**type**\:   :py:class:`NsrSummaryAll <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.NsrSummaryAll>`
        
        .. attribute:: oper_summary
        
        	LDP operational data summary
        	**type**\:   :py:class:`OperSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.OperSummary>`
        
        .. attribute:: parameters
        
        	MPLS LDP Global Parameters
        	**type**\:   :py:class:`Parameters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Parameters>`
        
        .. attribute:: vrfs
        
        	MPLS LDP per\-VRF operational data
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.backoff_parameters = MplsLdp.MplsLdpState.BackoffParameters()
            self.backoff_parameters.parent = self
            self.bindings = MplsLdp.MplsLdpState.Bindings()
            self.bindings.parent = self
            self.bindings_summary = MplsLdp.MplsLdpState.BindingsSummary()
            self.bindings_summary.parent = self
            self.capabilities = MplsLdp.MplsLdpState.Capabilities()
            self.capabilities.parent = self
            self.discovery = MplsLdp.MplsLdpState.Discovery()
            self.discovery.parent = self
            self.forwarding = MplsLdp.MplsLdpState.Forwarding()
            self.forwarding.parent = self
            self.forwarding_summary = MplsLdp.MplsLdpState.ForwardingSummary()
            self.forwarding_summary.parent = self
            self.graceful_restart = MplsLdp.MplsLdpState.GracefulRestart()
            self.graceful_restart.parent = self
            self.icpm_summary_all = MplsLdp.MplsLdpState.IcpmSummaryAll()
            self.icpm_summary_all.parent = self
            self.label_ranges = MplsLdp.MplsLdpState.LabelRanges()
            self.label_ranges.parent = self
            self.neighbors = MplsLdp.MplsLdpState.Neighbors()
            self.neighbors.parent = self
            self.nsr_summary_all = MplsLdp.MplsLdpState.NsrSummaryAll()
            self.nsr_summary_all.parent = self
            self.oper_summary = MplsLdp.MplsLdpState.OperSummary()
            self.oper_summary.parent = self
            self.parameters = MplsLdp.MplsLdpState.Parameters()
            self.parameters.parent = self
            self.vrfs = MplsLdp.MplsLdpState.Vrfs()
            self.vrfs.parent = self


        class OperSummary(object):
            """
            LDP operational data summary
            
            .. attribute:: common
            
            	Common Summary information
            	**type**\:   :py:class:`Common <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.OperSummary.Common>`
            
            .. attribute:: no_of_ipv4_rib_tbl
            
            	Total number of ipv4 RIB tables
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_of_ipv4_rib_tbl_reg
            
            	Number of ipv4 RIB tables registered
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_autocfg_interfaces
            
            	Number of auto\-configured interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_fwd_ref_interfaces
            
            	Number of Forward Reference interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_interfaces
            
            	Number of known interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_vrf
            
            	Number of configured VRFs (including default)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_vrf_oper
            
            	Number of configured operational VRFs (including default)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.common = MplsLdp.MplsLdpState.OperSummary.Common()
                self.common.parent = self
                self.no_of_ipv4_rib_tbl = None
                self.no_of_ipv4_rib_tbl_reg = None
                self.number_of_autocfg_interfaces = None
                self.number_of_fwd_ref_interfaces = None
                self.number_of_interfaces = None
                self.number_of_vrf = None
                self.number_of_vrf_oper = None


            class Common(object):
                """
                Common Summary information
                
                .. attribute:: address_families
                
                	Address Families enabled
                	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                
                .. attribute:: number_of_downstream_on_demand_neighbors
                
                	Number of Downstream\-On\-Demand neighbor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_graceful_restart_neighbors
                
                	Number of Graceful Restart neighbor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ipv4_local_addresses
                
                	Number of IPv4 local addresses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ipv4_routes
                
                	Number of resolved IPv4 routes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ipv4ldp_interfaces
                
                	Number of LDP IPv4 configured interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_ldp_interfaces
                
                	Number of LDP configured interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_neighbors
                
                	Number of neighbor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: numberof_ipv4_hello_adj
                
                	Number of LDP discovery IPv4 hello adjacencies
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.address_families = None
                    self.number_of_downstream_on_demand_neighbors = None
                    self.number_of_graceful_restart_neighbors = None
                    self.number_of_ipv4_local_addresses = None
                    self.number_of_ipv4_routes = None
                    self.number_of_ipv4ldp_interfaces = None
                    self.number_of_ldp_interfaces = None
                    self.number_of_neighbors = None
                    self.numberof_ipv4_hello_adj = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:oper-summary/Cisco-IOS-XE-mpls-ldp:common'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.address_families is not None:
                        return True

                    if self.number_of_downstream_on_demand_neighbors is not None:
                        return True

                    if self.number_of_graceful_restart_neighbors is not None:
                        return True

                    if self.number_of_ipv4_local_addresses is not None:
                        return True

                    if self.number_of_ipv4_routes is not None:
                        return True

                    if self.number_of_ipv4ldp_interfaces is not None:
                        return True

                    if self.number_of_ldp_interfaces is not None:
                        return True

                    if self.number_of_neighbors is not None:
                        return True

                    if self.numberof_ipv4_hello_adj is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.OperSummary.Common']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:oper-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.common is not None and self.common._has_data():
                    return True

                if self.no_of_ipv4_rib_tbl is not None:
                    return True

                if self.no_of_ipv4_rib_tbl_reg is not None:
                    return True

                if self.number_of_autocfg_interfaces is not None:
                    return True

                if self.number_of_fwd_ref_interfaces is not None:
                    return True

                if self.number_of_interfaces is not None:
                    return True

                if self.number_of_vrf is not None:
                    return True

                if self.number_of_vrf_oper is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.OperSummary']['meta_info']


        class ForwardingSummary(object):
            """
            Summary information regarding LDP forwarding
            setup
            
            .. attribute:: intfs_fwd_count
            
            	MPLS forwarding enabled interface count
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: local_lbls
            
            	Local label allocated count
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nhs
            
            	MPLS LDP forwarding rewrite next\-hop/path summary
            	**type**\:   :py:class:`Nhs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Nhs>`
            
            .. attribute:: pfxs
            
            	MPLS LDP forwarding prefix rewrite summary
            	**type**\:   :py:class:`Pfxs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.intfs_fwd_count = None
                self.local_lbls = None
                self.nhs = MplsLdp.MplsLdpState.ForwardingSummary.Nhs()
                self.nhs.parent = self
                self.pfxs = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs()
                self.pfxs.parent = self


            class Pfxs(object):
                """
                MPLS LDP forwarding prefix rewrite summary
                
                .. attribute:: ecmp_pfxs
                
                	Count of prefixes with ECMP
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: labeled_pfxs_aggr
                
                	Labeled prefix count for all paths
                	**type**\:   :py:class:`LabeledPfxsAggr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr>`
                
                .. attribute:: labeled_pfxs_backup
                
                	Labeled prefix count related to backup paths only
                	**type**\:   :py:class:`LabeledPfxsBackup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup>`
                
                .. attribute:: labeled_pfxs_primary
                
                	Labeled prefix count related to primary paths only
                	**type**\:   :py:class:`LabeledPfxsPrimary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary>`
                
                .. attribute:: protected_pfxs
                
                	Count of FRR protected prefixes
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: total_pfxs
                
                	Total Prefix count
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.ecmp_pfxs = None
                    self.labeled_pfxs_aggr = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr()
                    self.labeled_pfxs_aggr.parent = self
                    self.labeled_pfxs_backup = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup()
                    self.labeled_pfxs_backup.parent = self
                    self.labeled_pfxs_primary = MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary()
                    self.labeled_pfxs_primary.parent = self
                    self.protected_pfxs = None
                    self.total_pfxs = None


                class LabeledPfxsAggr(object):
                    """
                    Labeled prefix count for all paths
                    
                    .. attribute:: labeled_pfxs
                    
                    	Count of labeled prefixes with 1 or more paths labeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: labeled_pfxs_partial
                    
                    	Count of labeled prefixes with some (but not ALL) paths labeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: unlabeled_pfxs
                    
                    	Count of labeled prefixes with ALL paths unlabeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.labeled_pfxs = None
                        self.labeled_pfxs_partial = None
                        self.unlabeled_pfxs = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding-summary/Cisco-IOS-XE-mpls-ldp:pfxs/Cisco-IOS-XE-mpls-ldp:labeled-pfxs-aggr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.labeled_pfxs is not None:
                            return True

                        if self.labeled_pfxs_partial is not None:
                            return True

                        if self.unlabeled_pfxs is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsAggr']['meta_info']


                class LabeledPfxsPrimary(object):
                    """
                    Labeled prefix count related to primary paths
                    only
                    
                    .. attribute:: labeled_pfxs
                    
                    	Count of labeled prefixes with 1 or more paths labeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: labeled_pfxs_partial
                    
                    	Count of labeled prefixes with some (but not ALL) paths labeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: unlabeled_pfxs
                    
                    	Count of labeled prefixes with ALL paths unlabeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.labeled_pfxs = None
                        self.labeled_pfxs_partial = None
                        self.unlabeled_pfxs = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding-summary/Cisco-IOS-XE-mpls-ldp:pfxs/Cisco-IOS-XE-mpls-ldp:labeled-pfxs-primary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.labeled_pfxs is not None:
                            return True

                        if self.labeled_pfxs_partial is not None:
                            return True

                        if self.unlabeled_pfxs is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsPrimary']['meta_info']


                class LabeledPfxsBackup(object):
                    """
                    Labeled prefix count related to backup paths
                    only
                    
                    .. attribute:: labeled_pfxs
                    
                    	Count of labeled prefixes with 1 or more paths labeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: labeled_pfxs_partial
                    
                    	Count of labeled prefixes with some (but not ALL) paths labeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: unlabeled_pfxs
                    
                    	Count of labeled prefixes with ALL paths unlabeled
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.labeled_pfxs = None
                        self.labeled_pfxs_partial = None
                        self.unlabeled_pfxs = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding-summary/Cisco-IOS-XE-mpls-ldp:pfxs/Cisco-IOS-XE-mpls-ldp:labeled-pfxs-backup'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.labeled_pfxs is not None:
                            return True

                        if self.labeled_pfxs_partial is not None:
                            return True

                        if self.unlabeled_pfxs is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs.LabeledPfxsBackup']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding-summary/Cisco-IOS-XE-mpls-ldp:pfxs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ecmp_pfxs is not None:
                        return True

                    if self.labeled_pfxs_aggr is not None and self.labeled_pfxs_aggr._has_data():
                        return True

                    if self.labeled_pfxs_backup is not None and self.labeled_pfxs_backup._has_data():
                        return True

                    if self.labeled_pfxs_primary is not None and self.labeled_pfxs_primary._has_data():
                        return True

                    if self.protected_pfxs is not None:
                        return True

                    if self.total_pfxs is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Pfxs']['meta_info']


            class Nhs(object):
                """
                MPLS LDP forwarding rewrite next\-hop/path summary
                
                .. attribute:: backup_paths
                
                	Count of non\-primary backup paths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: labeled_backup_paths
                
                	Count of labeled backup paths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: labeled_paths
                
                	Count of all labeled paths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: protected_paths
                
                	Count of FRR protected paths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_backup_paths
                
                	Count of non\-primary remote backup paths
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_paths
                
                	Total path count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.backup_paths = None
                    self.labeled_backup_paths = None
                    self.labeled_paths = None
                    self.protected_paths = None
                    self.remote_backup_paths = None
                    self.total_paths = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding-summary/Cisco-IOS-XE-mpls-ldp:nhs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.backup_paths is not None:
                        return True

                    if self.labeled_backup_paths is not None:
                        return True

                    if self.labeled_paths is not None:
                        return True

                    if self.protected_paths is not None:
                        return True

                    if self.remote_backup_paths is not None:
                        return True

                    if self.total_paths is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.ForwardingSummary.Nhs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.intfs_fwd_count is not None:
                    return True

                if self.local_lbls is not None:
                    return True

                if self.nhs is not None and self.nhs._has_data():
                    return True

                if self.pfxs is not None and self.pfxs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.ForwardingSummary']['meta_info']


        class BindingsSummary(object):
            """
            Aggregate counters for the MPLS LDP LIB.
            
            .. attribute:: binding_local
            
            	Number of local bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_explicit_null
            
            	Number of local explicit null bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_implicit_null
            
            	Number of local implicit null bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_no_route
            
            	Local bindings with no route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_non_null
            
            	Number of local non\-null bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_null
            
            	Number of local null bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_local_oor
            
            	This is the number of local bindings needing label but which hit the Out\-Of\-Resource condition
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_no_route
            
            	Bindings with no route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_remote
            
            	Number of remote bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: binding_total
            
            	Total bindings
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: highest_allocated_label
            
            	Highest allocated label
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: lowest_allocated_label
            
            	Lowest allocated label
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.binding_local = None
                self.binding_local_explicit_null = None
                self.binding_local_implicit_null = None
                self.binding_local_no_route = None
                self.binding_local_non_null = None
                self.binding_local_null = None
                self.binding_local_oor = None
                self.binding_no_route = None
                self.binding_remote = None
                self.binding_total = None
                self.highest_allocated_label = None
                self.lowest_allocated_label = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:bindings-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.binding_local is not None:
                    return True

                if self.binding_local_explicit_null is not None:
                    return True

                if self.binding_local_implicit_null is not None:
                    return True

                if self.binding_local_no_route is not None:
                    return True

                if self.binding_local_non_null is not None:
                    return True

                if self.binding_local_null is not None:
                    return True

                if self.binding_local_oor is not None:
                    return True

                if self.binding_no_route is not None:
                    return True

                if self.binding_remote is not None:
                    return True

                if self.binding_total is not None:
                    return True

                if self.highest_allocated_label is not None:
                    return True

                if self.lowest_allocated_label is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.BindingsSummary']['meta_info']


        class NsrSummaryAll(object):
            """
            This is the LDP NSR summary for the device.
            
            .. attribute:: nsr_sum_in_label_reqs_created
            
            	In label Request Records created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_in_label_reqs_freed
            
            	In label Request Records freed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_in_label_withdraw_created
            
            	In label Withdraw Records created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_in_label_withdraw_freed
            
            	In label Withdraw Records freed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_lcl_addr_withdraw_cleared
            
            	Local Address Withdraw cleared
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nsr_sum_lcl_addr_withdraw_set
            
            	Local Address Withdraw set
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.nsr_sum_in_label_reqs_created = None
                self.nsr_sum_in_label_reqs_freed = None
                self.nsr_sum_in_label_withdraw_created = None
                self.nsr_sum_in_label_withdraw_freed = None
                self.nsr_sum_lcl_addr_withdraw_cleared = None
                self.nsr_sum_lcl_addr_withdraw_set = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:nsr-summary-all'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.nsr_sum_in_label_reqs_created is not None:
                    return True

                if self.nsr_sum_in_label_reqs_freed is not None:
                    return True

                if self.nsr_sum_in_label_withdraw_created is not None:
                    return True

                if self.nsr_sum_in_label_withdraw_freed is not None:
                    return True

                if self.nsr_sum_lcl_addr_withdraw_cleared is not None:
                    return True

                if self.nsr_sum_lcl_addr_withdraw_set is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.NsrSummaryAll']['meta_info']


        class IcpmSummaryAll(object):
            """
            Summary info for LDP ICPM/ICCP.
            
            .. attribute:: iccp_rg_app_data_count
            
            	ICCP RG App Data count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iccp_rg_conn_count
            
            	ICCP RG Connect count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iccp_rg_disconn_count
            
            	ICCP RG Disconnect count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: iccp_rg_notif_count
            
            	ICCP RG Notif count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: icpm_rgid_table_info
            
            	This defines the ICPM RGID Table
            	**type**\:   :py:class:`IcpmRgidTableInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo>`
            
            .. attribute:: icpm_session_table
            
            	This is a list of ICPM sessions
            	**type**\:   :py:class:`IcpmSessionTable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.iccp_rg_app_data_count = None
                self.iccp_rg_conn_count = None
                self.iccp_rg_disconn_count = None
                self.iccp_rg_notif_count = None
                self.icpm_rgid_table_info = MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo()
                self.icpm_rgid_table_info.parent = self
                self.icpm_session_table = MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable()
                self.icpm_session_table.parent = self


            class IcpmRgidTableInfo(object):
                """
                This defines the ICPM RGID Table
                
                .. attribute:: red_group
                
                	This is the data for an individual ICPM Rredundandy Group,
                	**type**\: list of    :py:class:`RedGroup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.red_group = YList()
                    self.red_group.parent = self
                    self.red_group.name = 'red_group'


                class RedGroup(object):
                    """
                    This is the data for an individual ICPM Rredundandy
                    Group,
                    
                    .. attribute:: rg_id  <key>
                    
                    	This is the ICPM RG identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: icpm_protocols
                    
                    	This list contains all active icpm protocols
                    	**type**\: list of    :py:class:`IcpmProtocols <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.rg_id = None
                        self.icpm_protocols = YList()
                        self.icpm_protocols.parent = self
                        self.icpm_protocols.name = 'icpm_protocols'


                    class IcpmProtocols(object):
                        """
                        This list contains all active icpm protocols.
                        
                        .. attribute:: icpm_type  <key>
                        
                        	ICPM Type
                        	**type**\:   :py:class:`IcpmTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IcpmTypeIdentity>`
                        
                        .. attribute:: redun_groups
                        
                        	List of Redundancy Groups
                        	**type**\: list of    :py:class:`RedunGroups <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.icpm_type = None
                            self.redun_groups = YList()
                            self.redun_groups.parent = self
                            self.redun_groups.name = 'redun_groups'


                        class RedunGroups(object):
                            """
                            List of Redundancy Groups
                            
                            .. attribute:: rg_id  <key>
                            
                            	Redundancy Group Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: client_id
                            
                            	Client Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iccp_apps
                            
                            	List of apps
                            	**type**\: list of    :py:class:`IccpApps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps>`
                            
                            .. attribute:: peer_id
                            
                            	LSR identifier
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: state
                            
                            	ICCP State
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.rg_id = None
                                self.client_id = None
                                self.iccp_apps = YList()
                                self.iccp_apps.parent = self
                                self.iccp_apps.name = 'iccp_apps'
                                self.peer_id = None
                                self.state = None


                            class IccpApps(object):
                                """
                                List of apps
                                
                                .. attribute:: iccp_app  <key>
                                
                                	ICCP App Type
                                	**type**\:   :py:class:`IccpTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpTypeIdentity>`
                                
                                .. attribute:: app_state
                                
                                	App State
                                	**type**\:   :py:class:`IccpStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpStateEnum>`
                                
                                .. attribute:: ptcl_ver
                                
                                	ICCP App Protocol Version
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    self.parent = None
                                    self.iccp_app = None
                                    self.app_state = None
                                    self.ptcl_ver = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.iccp_app is None:
                                        raise YPYModelError('Key property iccp_app is None')

                                    return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:iccp-apps[Cisco-IOS-XE-mpls-ldp:iccp-app = ' + str(self.iccp_app) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.iccp_app is not None:
                                        return True

                                    if self.app_state is not None:
                                        return True

                                    if self.ptcl_ver is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                    return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups.IccpApps']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.rg_id is None:
                                    raise YPYModelError('Key property rg_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:redun-groups[Cisco-IOS-XE-mpls-ldp:rg-id = ' + str(self.rg_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.rg_id is not None:
                                    return True

                                if self.client_id is not None:
                                    return True

                                if self.iccp_apps is not None:
                                    for child_ref in self.iccp_apps:
                                        if child_ref._has_data():
                                            return True

                                if self.peer_id is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols.RedunGroups']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.icpm_type is None:
                                raise YPYModelError('Key property icpm_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:icpm-protocols[Cisco-IOS-XE-mpls-ldp:icpm-type = ' + str(self.icpm_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.icpm_type is not None:
                                return True

                            if self.redun_groups is not None:
                                for child_ref in self.redun_groups:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup.IcpmProtocols']['meta_info']

                    @property
                    def _common_path(self):
                        if self.rg_id is None:
                            raise YPYModelError('Key property rg_id is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:icpm-summary-all/Cisco-IOS-XE-mpls-ldp:icpm-rgid-table-info/Cisco-IOS-XE-mpls-ldp:red-group[Cisco-IOS-XE-mpls-ldp:rg-id = ' + str(self.rg_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.rg_id is not None:
                            return True

                        if self.icpm_protocols is not None:
                            for child_ref in self.icpm_protocols:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo.RedGroup']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:icpm-summary-all/Cisco-IOS-XE-mpls-ldp:icpm-rgid-table-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.red_group is not None:
                        for child_ref in self.red_group:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmRgidTableInfo']['meta_info']


            class IcpmSessionTable(object):
                """
                This is a list of ICPM sessions.
                
                .. attribute:: session_table
                
                	ICPM LDP Session Table
                	**type**\: list of    :py:class:`SessionTable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.session_table = YList()
                    self.session_table.parent = self
                    self.session_table.name = 'session_table'


                class SessionTable(object):
                    """
                    ICPM LDP Session Table
                    
                    .. attribute:: session_id  <key>
                    
                    	This is the ICPM sesion identifier
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: icpm_protocols
                    
                    	This list contains all active icpm protocols
                    	**type**\: list of    :py:class:`IcpmProtocols <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.icpm_protocols = YList()
                        self.icpm_protocols.parent = self
                        self.icpm_protocols.name = 'icpm_protocols'


                    class IcpmProtocols(object):
                        """
                        This list contains all active icpm protocols.
                        
                        .. attribute:: icpm_type  <key>
                        
                        	ICPM Type
                        	**type**\:   :py:class:`IcpmTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IcpmTypeIdentity>`
                        
                        .. attribute:: redun_groups
                        
                        	List of Redundancy Groups
                        	**type**\: list of    :py:class:`RedunGroups <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.icpm_type = None
                            self.redun_groups = YList()
                            self.redun_groups.parent = self
                            self.redun_groups.name = 'redun_groups'


                        class RedunGroups(object):
                            """
                            List of Redundancy Groups
                            
                            .. attribute:: rg_id  <key>
                            
                            	Redundancy Group Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: client_id
                            
                            	Client Identifier
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: iccp_apps
                            
                            	List of apps
                            	**type**\: list of    :py:class:`IccpApps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps>`
                            
                            .. attribute:: peer_id
                            
                            	LSR identifier
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: state
                            
                            	ICCP State
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.rg_id = None
                                self.client_id = None
                                self.iccp_apps = YList()
                                self.iccp_apps.parent = self
                                self.iccp_apps.name = 'iccp_apps'
                                self.peer_id = None
                                self.state = None


                            class IccpApps(object):
                                """
                                List of apps
                                
                                .. attribute:: iccp_app  <key>
                                
                                	ICCP App Type
                                	**type**\:   :py:class:`IccpTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpTypeIdentity>`
                                
                                .. attribute:: app_state
                                
                                	App State
                                	**type**\:   :py:class:`IccpStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IccpStateEnum>`
                                
                                .. attribute:: ptcl_ver
                                
                                	ICCP App Protocol Version
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    self.parent = None
                                    self.iccp_app = None
                                    self.app_state = None
                                    self.ptcl_ver = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.iccp_app is None:
                                        raise YPYModelError('Key property iccp_app is None')

                                    return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:iccp-apps[Cisco-IOS-XE-mpls-ldp:iccp-app = ' + str(self.iccp_app) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.iccp_app is not None:
                                        return True

                                    if self.app_state is not None:
                                        return True

                                    if self.ptcl_ver is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                    return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups.IccpApps']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.rg_id is None:
                                    raise YPYModelError('Key property rg_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:redun-groups[Cisco-IOS-XE-mpls-ldp:rg-id = ' + str(self.rg_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.rg_id is not None:
                                    return True

                                if self.client_id is not None:
                                    return True

                                if self.iccp_apps is not None:
                                    for child_ref in self.iccp_apps:
                                        if child_ref._has_data():
                                            return True

                                if self.peer_id is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols.RedunGroups']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.icpm_type is None:
                                raise YPYModelError('Key property icpm_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:icpm-protocols[Cisco-IOS-XE-mpls-ldp:icpm-type = ' + str(self.icpm_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.icpm_type is not None:
                                return True

                            if self.redun_groups is not None:
                                for child_ref in self.redun_groups:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable.IcpmProtocols']['meta_info']

                    @property
                    def _common_path(self):
                        if self.session_id is None:
                            raise YPYModelError('Key property session_id is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:icpm-summary-all/Cisco-IOS-XE-mpls-ldp:icpm-session-table/Cisco-IOS-XE-mpls-ldp:session-table[Cisco-IOS-XE-mpls-ldp:session-id = ' + str(self.session_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.icpm_protocols is not None:
                            for child_ref in self.icpm_protocols:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable.SessionTable']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:icpm-summary-all/Cisco-IOS-XE-mpls-ldp:icpm-session-table'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_table is not None:
                        for child_ref in self.session_table:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll.IcpmSessionTable']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:icpm-summary-all'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.iccp_rg_app_data_count is not None:
                    return True

                if self.iccp_rg_conn_count is not None:
                    return True

                if self.iccp_rg_disconn_count is not None:
                    return True

                if self.iccp_rg_notif_count is not None:
                    return True

                if self.icpm_rgid_table_info is not None and self.icpm_rgid_table_info._has_data():
                    return True

                if self.icpm_session_table is not None and self.icpm_session_table._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.IcpmSummaryAll']['meta_info']


        class Parameters(object):
            """
            MPLS LDP Global Parameters
            
            .. attribute:: address_family_parameter
            
            	Per AF parameters
            	**type**\: list of    :py:class:`AddressFamilyParameter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter>`
            
            .. attribute:: af_binding_withdraw_delay
            
            	Delay (sec) in Binding Withdrawal for an Address Family
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: discovery_quick_start_disabled_on_interfaces
            
            	Discovery quick\-start disabled on some enabled interfaces
            	**type**\:  bool
            
            .. attribute:: dod_max_hop
            
            	Maximum number of hops for Downstream\-on\-Demand
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: feature
            
            	This entry describes an LDP feature available on the device. This does not indicate whether the feature is enabled, just the raw ability to support the feature. The features may include, but are not limited to\: 'Auto\-Configuration', 'Basic', 'ICPM', 'IP\-over\-MPLS', 'IGP\-Sync', 'LLAF', 'TCP\-MD5\-Rollover', 'TDP', and 'NSR'
            	**type**\:  list of str
            
            .. attribute:: global_md5_password_enabled
            
            	Global MD5 password enabled
            	**type**\:  bool
            
            .. attribute:: keepalive_interval
            
            	Keepalive interval in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: le_no_route_timeout
            
            	LIB entry no route timeout in second
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: loop_detection
            
            	A indication of whether this LSR has enabled loop detection. Since Loop Detection is determined during Session Initialization, an individual session may not be running with loop detection.  This object simply gives an indication of whether or not the LSR has the ability enabled to support Loop Detection and which types
            	**type**\:   :py:class:`LoopDetectionTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LoopDetectionTypeEnum>`
            
            .. attribute:: max_intf_attached
            
            	Maximum number of LDP enabled attached interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_intf_te
            
            	Maximum number of LDP enabled TE interfaces
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_peer
            
            	Maximum number of LDP peers
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: out_of_mem_state
            
            	This is a counter of the number of times LDP attempted to create a label or binding and failed due a memory allocation failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: protocol_version
            
            	Protocol version
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_hold_time
            
            	Session hold time in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.address_family_parameter = YList()
                self.address_family_parameter.parent = self
                self.address_family_parameter.name = 'address_family_parameter'
                self.af_binding_withdraw_delay = None
                self.discovery_quick_start_disabled_on_interfaces = None
                self.dod_max_hop = None
                self.feature = YLeafList()
                self.feature.parent = self
                self.feature.name = 'feature'
                self.global_md5_password_enabled = None
                self.keepalive_interval = None
                self.le_no_route_timeout = None
                self.loop_detection = None
                self.max_intf_attached = None
                self.max_intf_te = None
                self.max_peer = None
                self.out_of_mem_state = None
                self.protocol_version = None
                self.session_hold_time = None


            class AddressFamilyParameter(object):
                """
                Per AF parameters
                
                .. attribute:: address_family  <key>
                
                	Address Family
                	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                
                .. attribute:: discovery_transport_address
                
                	This is the Discovery transport address
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: is_accepting_targeted_hellos
                
                	Accepting targeted Hellos
                	**type**\:  bool
                
                .. attribute:: targeted_hello_filter
                
                	This contains the filter name for targeted hellos. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.address_family = None
                    self.discovery_transport_address = None
                    self.is_accepting_targeted_hellos = None
                    self.targeted_hello_filter = None

                @property
                def _common_path(self):
                    if self.address_family is None:
                        raise YPYModelError('Key property address_family is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:parameters/Cisco-IOS-XE-mpls-ldp:address-family-parameter[Cisco-IOS-XE-mpls-ldp:address-family = ' + str(self.address_family) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.address_family is not None:
                        return True

                    if self.discovery_transport_address is not None:
                        return True

                    if self.is_accepting_targeted_hellos is not None:
                        return True

                    if self.targeted_hello_filter is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Parameters.AddressFamilyParameter']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.address_family_parameter is not None:
                    for child_ref in self.address_family_parameter:
                        if child_ref._has_data():
                            return True

                if self.af_binding_withdraw_delay is not None:
                    return True

                if self.discovery_quick_start_disabled_on_interfaces is not None:
                    return True

                if self.dod_max_hop is not None:
                    return True

                if self.feature is not None:
                    for child in self.feature:
                        if child is not None:
                            return True

                if self.global_md5_password_enabled is not None:
                    return True

                if self.keepalive_interval is not None:
                    return True

                if self.le_no_route_timeout is not None:
                    return True

                if self.loop_detection is not None:
                    return True

                if self.max_intf_attached is not None:
                    return True

                if self.max_intf_te is not None:
                    return True

                if self.max_peer is not None:
                    return True

                if self.out_of_mem_state is not None:
                    return True

                if self.protocol_version is not None:
                    return True

                if self.session_hold_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Parameters']['meta_info']


        class Capabilities(object):
            """
            LDP capability database information
            
            .. attribute:: capability
            
            	Information on LDP capability
            	**type**\: list of    :py:class:`Capability <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Capabilities.Capability>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.capability = YList()
                self.capability.parent = self
                self.capability.name = 'capability'


            class Capability(object):
                """
                Information on LDP capability
                
                .. attribute:: cap_type  <key>
                
                	Capability type (IANA assigned)
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: cap_des
                
                	Capability description
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: capability_data
                
                	Capability data
                	**type**\:  str
                
                .. attribute:: capability_data_length
                
                	Capability data length
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: capability_owner
                
                	Capability owner
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.cap_type = None
                    self.cap_des = None
                    self.capability_data = None
                    self.capability_data_length = None
                    self.capability_owner = None

                @property
                def _common_path(self):
                    if self.cap_type is None:
                        raise YPYModelError('Key property cap_type is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:capabilities/Cisco-IOS-XE-mpls-ldp:capability[Cisco-IOS-XE-mpls-ldp:cap-type = ' + str(self.cap_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.cap_type is not None:
                        return True

                    if self.cap_des is not None:
                        return True

                    if self.capability_data is not None:
                        return True

                    if self.capability_data_length is not None:
                        return True

                    if self.capability_owner is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Capabilities.Capability']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:capabilities'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.capability is not None:
                    for child_ref in self.capability:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Capabilities']['meta_info']


        class BackoffParameters(object):
            """
            MPLS LDP Session Backoff Information
            
            .. attribute:: backoff_seconds
            
            	Current backoff seconds count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: initial_seconds
            
            	Initial backoff value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: maximum_seconds
            
            	Maximum backoff value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: waiting_seconds
            
            	Current backoff waiting seconds count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.backoff_seconds = None
                self.initial_seconds = None
                self.maximum_seconds = None
                self.waiting_seconds = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:backoff-parameters'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.backoff_seconds is not None:
                    return True

                if self.initial_seconds is not None:
                    return True

                if self.maximum_seconds is not None:
                    return True

                if self.waiting_seconds is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.BackoffParameters']['meta_info']


        class GracefulRestart(object):
            """
            MPLS LDP Graceful Restart Information
            
            .. attribute:: forwarding_state_hold_timer_remaining_seconds
            
            	Forwarding state hold timer remaining time in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: graceful_restart_forwarding_state_hold_time
            
            	Graceful restart forward state hold time in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: graceful_restart_reconnect_timeout
            
            	Reconnect timeout value in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: is_forwarding_state_hold_timer_running
            
            	Is graceful restart forwarding state hold timer running
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: is_graceful_restart_configured
            
            	Is graceful restart configured
            	**type**\:  bool
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.forwarding_state_hold_timer_remaining_seconds = None
                self.graceful_restart_forwarding_state_hold_time = None
                self.graceful_restart_reconnect_timeout = None
                self.is_forwarding_state_hold_timer_running = None
                self.is_graceful_restart_configured = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:graceful-restart'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.forwarding_state_hold_timer_remaining_seconds is not None:
                    return True

                if self.graceful_restart_forwarding_state_hold_time is not None:
                    return True

                if self.graceful_restart_reconnect_timeout is not None:
                    return True

                if self.is_forwarding_state_hold_timer_running is not None:
                    return True

                if self.is_graceful_restart_configured is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.GracefulRestart']['meta_info']


        class Vrfs(object):
            """
            MPLS LDP per\-VRF operational data.
            
            .. attribute:: vrf
            
            	MPLS LDP Operational data for a given VRF
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.vrf = YList()
                self.vrf.parent = self
                self.vrf.name = 'vrf'


            class Vrf(object):
                """
                MPLS LDP Operational data for a given VRF.
                
                .. attribute:: vrf_name  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs>`
                
                .. attribute:: vrf_summary
                
                	MPLS LDP per VRF summarized Information
                	**type**\:   :py:class:`VrfSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.afs = MplsLdp.MplsLdpState.Vrfs.Vrf.Afs()
                    self.afs.parent = self
                    self.vrf_summary = MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary()
                    self.vrf_summary.parent = self


                class VrfSummary(object):
                    """
                    MPLS LDP per VRF summarized Information
                    
                    .. attribute:: address_families
                    
                    	Address Families enabled
                    	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                    
                    .. attribute:: number_of_downstream_on_demand_neighbors
                    
                    	Number of Downstream\-On\-Demand neighbor
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_graceful_restart_neighbors
                    
                    	Number of Graceful Restart neighbor
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ipv4_local_addresses
                    
                    	Number of IPv4 local addresses
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ipv4_routes
                    
                    	Number of resolved IPv4 routes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ipv4ldp_interfaces
                    
                    	Number of LDP IPv4 configured interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_ldp_interfaces
                    
                    	Number of LDP configured interfaces
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_neighbors
                    
                    	Number of neighbor
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: numberof_ipv4_hello_adj
                    
                    	Number of LDP discovery IPv4 hello adjacencies
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.address_families = None
                        self.number_of_downstream_on_demand_neighbors = None
                        self.number_of_graceful_restart_neighbors = None
                        self.number_of_ipv4_local_addresses = None
                        self.number_of_ipv4_routes = None
                        self.number_of_ipv4ldp_interfaces = None
                        self.number_of_ldp_interfaces = None
                        self.number_of_neighbors = None
                        self.numberof_ipv4_hello_adj = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:vrf-summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address_families is not None:
                            return True

                        if self.number_of_downstream_on_demand_neighbors is not None:
                            return True

                        if self.number_of_graceful_restart_neighbors is not None:
                            return True

                        if self.number_of_ipv4_local_addresses is not None:
                            return True

                        if self.number_of_ipv4_routes is not None:
                            return True

                        if self.number_of_ipv4ldp_interfaces is not None:
                            return True

                        if self.number_of_ldp_interfaces is not None:
                            return True

                        if self.number_of_neighbors is not None:
                            return True

                        if self.numberof_ipv4_hello_adj is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.VrfSummary']['meta_info']


                class Afs(object):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	MPLS LDP Operational data for this Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.af = YList()
                        self.af.parent = self
                        self.af.name = 'af'


                    class Af(object):
                        """
                        MPLS LDP Operational data for this Address Family.
                        
                        .. attribute:: af_name  <key>
                        
                        	Address Family name
                        	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                        
                        .. attribute:: igp
                        
                        	LDP IGP Synchronization related information
                        	**type**\:   :py:class:`Igp <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp>`
                        
                        .. attribute:: interface_summary
                        
                        	This container holds a summary of information across all interfaces in this AF,
                        	**type**\:   :py:class:`InterfaceSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.igp = MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp()
                            self.igp.parent = self
                            self.interface_summary = MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary()
                            self.interface_summary.parent = self


                        class InterfaceSummary(object):
                            """
                            This container holds a summary of information
                            across all interfaces in this AF,
                            
                            .. attribute:: auto_config
                            
                            	Auto\-configured interfaces
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: auto_config_disabled
                            
                            	Autoconfigure disabled
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: auto_config_forward_reference_interfaces
                            
                            	Auto\-configured forward references
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: configured_attached_interface
                            
                            	Number of attached interfaces configured in LDP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: configured_te_interface
                            
                            	Number of TE tunnel interfaces configured in LDP
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: forward_references
                            
                            	Number of forward referenced interfaces
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: known_ip_interface_count
                            
                            	Number of known IP Interfaces
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: known_ip_interface_ldp_enabled
                            
                            	Number of known IP Interfaces with LDP Enabled
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.auto_config = None
                                self.auto_config_disabled = None
                                self.auto_config_forward_reference_interfaces = None
                                self.configured_attached_interface = None
                                self.configured_te_interface = None
                                self.forward_references = None
                                self.known_ip_interface_count = None
                                self.known_ip_interface_ldp_enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:interface-summary'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.auto_config is not None:
                                    return True

                                if self.auto_config_disabled is not None:
                                    return True

                                if self.auto_config_forward_reference_interfaces is not None:
                                    return True

                                if self.configured_attached_interface is not None:
                                    return True

                                if self.configured_te_interface is not None:
                                    return True

                                if self.forward_references is not None:
                                    return True

                                if self.known_ip_interface_count is not None:
                                    return True

                                if self.known_ip_interface_ldp_enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.InterfaceSummary']['meta_info']


                        class Igp(object):
                            """
                            LDP IGP Synchronization related information
                            
                            .. attribute:: sync
                            
                            	LDP\-IGP Synchronization related information for an interface
                            	**type**\: list of    :py:class:`Sync <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.sync = YList()
                                self.sync.parent = self
                                self.sync.name = 'sync'


                            class Sync(object):
                                """
                                LDP\-IGP Synchronization related information
                                for an interface
                                
                                .. attribute:: interface  <key>
                                
                                	This leaf contains the interface name for the IGP Synchronization information
                                	**type**\:  str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: delay_timer_remaining
                                
                                	Remaining timer (seconds) until expiry of sync delay timer
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: seconds
                                
                                .. attribute:: igp_sync_down_reason
                                
                                	Reason IGP Sync Not Achieved
                                	**type**\:   :py:class:`IgpSyncDownReasonIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IgpSyncDownReasonIdentity>`
                                
                                .. attribute:: igp_sync_state
                                
                                	IGP Sync state
                                	**type**\:   :py:class:`IgpSyncStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.IgpSyncStateEnum>`
                                
                                .. attribute:: is_delay_timer_running
                                
                                	This is set when the sync delay timer running
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: peers
                                
                                	MPLS LDP IGP Sync Interface Peer Information
                                	**type**\: list of    :py:class:`Peers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    self.parent = None
                                    self.interface = None
                                    self.delay_timer_remaining = None
                                    self.igp_sync_down_reason = None
                                    self.igp_sync_state = None
                                    self.is_delay_timer_running = None
                                    self.peers = YList()
                                    self.peers.parent = self
                                    self.peers.name = 'peers'


                                class Peers(object):
                                    """
                                    MPLS LDP IGP Sync Interface Peer Information
                                    
                                    .. attribute:: is_chkpt_created
                                    
                                    	This is set if this peer was created due to check\-pointing
                                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: is_gr_enabled
                                    
                                    	Is GR enabled session
                                    	**type**\:  bool
                                    
                                    .. attribute:: peer_id
                                    
                                    	Peer Identifier
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-ios-xe-oper'
                                    _revision = '2017-02-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.is_chkpt_created = None
                                        self.is_gr_enabled = None
                                        self.peer_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:peers'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.is_chkpt_created is not None:
                                            return True

                                        if self.is_gr_enabled is not None:
                                            return True

                                        if self.peer_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                        return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync.Peers']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface is None:
                                        raise YPYModelError('Key property interface is None')

                                    return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:sync[Cisco-IOS-XE-mpls-ldp:interface = ' + str(self.interface) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface is not None:
                                        return True

                                    if self.delay_timer_remaining is not None:
                                        return True

                                    if self.igp_sync_down_reason is not None:
                                        return True

                                    if self.igp_sync_state is not None:
                                        return True

                                    if self.is_delay_timer_running is not None:
                                        return True

                                    if self.peers is not None:
                                        for child_ref in self.peers:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                    return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp.Sync']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:igp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sync is not None:
                                    for child_ref in self.sync:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af.Igp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.af_name is None:
                                raise YPYModelError('Key property af_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:af[Cisco-IOS-XE-mpls-ldp:af-name = ' + str(self.af_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.igp is not None and self.igp._has_data():
                                return True

                            if self.interface_summary is not None and self.interface_summary._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs.Af']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:afs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af is not None:
                            for child_ref in self.af:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf.Afs']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:vrfs/Cisco-IOS-XE-mpls-ldp:vrf[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.afs is not None and self.afs._has_data():
                        return True

                    if self.vrf_summary is not None and self.vrf_summary._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:vrfs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf is not None:
                    for child_ref in self.vrf:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Vrfs']['meta_info']


        class Discovery(object):
            """
            The LDP Discovery operational state
            
            .. attribute:: discovery_stats
            
            	MPLS LDP Discovery Summary Information
            	**type**\:   :py:class:`DiscoveryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.DiscoveryStats>`
            
            .. attribute:: link_hello_state
            
            	This container holds information for LDP Discovery using non\-targeted Hellos. These are interface\-based hellos which form one or more adjacencies for each interface and also form adjacencies on multiple intefrfaces. Link Hellos can therefore form multiple adjacencies with the same peer
            	**type**\:   :py:class:`LinkHelloState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.LinkHelloState>`
            
            .. attribute:: targeted_hellos
            
            	The LDP Discovery Targeted Hello state
            	**type**\:   :py:class:`TargetedHellos <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.TargetedHellos>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.discovery_stats = MplsLdp.MplsLdpState.Discovery.DiscoveryStats()
                self.discovery_stats.parent = self
                self.link_hello_state = MplsLdp.MplsLdpState.Discovery.LinkHelloState()
                self.link_hello_state.parent = self
                self.targeted_hellos = MplsLdp.MplsLdpState.Discovery.TargetedHellos()
                self.targeted_hellos.parent = self


            class DiscoveryStats(object):
                """
                MPLS LDP Discovery Summary Information
                
                .. attribute:: num_of_active_ldp_interfaces
                
                	Number of active LDP enabled interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_ldp_interfaces
                
                	Total Number of LDP configured interfaces
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_lnk_disc_recv
                
                	Number of link hello discoveries in recv state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_lnk_disc_xmit
                
                	Number of link hello discoveries in xmit state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_tgt_disc_recv
                
                	Number of targeted hello discoveries in recv state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_of_tgt_disc_xmit
                
                	Number of targeted hello discoveries in xmit state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.num_of_active_ldp_interfaces = None
                    self.num_of_ldp_interfaces = None
                    self.num_of_lnk_disc_recv = None
                    self.num_of_lnk_disc_xmit = None
                    self.num_of_tgt_disc_recv = None
                    self.num_of_tgt_disc_xmit = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:discovery-stats'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.num_of_active_ldp_interfaces is not None:
                        return True

                    if self.num_of_ldp_interfaces is not None:
                        return True

                    if self.num_of_lnk_disc_recv is not None:
                        return True

                    if self.num_of_lnk_disc_xmit is not None:
                        return True

                    if self.num_of_tgt_disc_recv is not None:
                        return True

                    if self.num_of_tgt_disc_xmit is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Discovery.DiscoveryStats']['meta_info']


            class LinkHelloState(object):
                """
                This container holds information for LDP Discovery
                using non\-targeted Hellos. These are interface\-based
                hellos which form one or more adjacencies for each
                interface and also form adjacencies on multiple
                intefrfaces. Link Hellos can therefore form multiple
                adjacencies with the same peer.
                
                .. attribute:: link_hellos
                
                	Each entry represents a single LDP Hello Adjacency. An LDP Session can have one or more Hello Adjacencies
                	**type**\: list of    :py:class:`LinkHellos <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.link_hellos = YList()
                    self.link_hellos.parent = self
                    self.link_hellos.name = 'link_hellos'


                class LinkHellos(object):
                    """
                    Each entry represents a single LDP Hello Adjacency.
                    An LDP Session can have one or more Hello
                    Adjacencies.
                    
                    .. attribute:: interface  <key>
                    
                    	The Discovery Interface
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: nbr_transport_addr  <key>
                    
                    	This is the MPLS LDP Hello Neighbor transport address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds. This is the value used to send hello messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: hold_time_remaining
                    
                    	This is the MPLS LDP Hello Discovery expiry time in seconds. If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: seconds
                    
                    .. attribute:: local_src_addr
                    
                    	MPLS LDP Discovery Local source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: local_transport_addr
                    
                    	MPLS LDP Discovery Local transport address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: nbr_hold_time
                    
                    	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the EntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: nbr_ldp_id
                    
                    	Neighbor LDP Identifier
                    	**type**\:  str
                    
                    .. attribute:: nbr_src_addr
                    
                    	This is the MPLS LDP Hello Neighbor source address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: next_hello
                    
                    	Next hello due time in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: session_up
                    
                    	Set when the session is up for this adjacency
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.interface = None
                        self.nbr_transport_addr = None
                        self.hello_interval = None
                        self.hold_time_remaining = None
                        self.local_src_addr = None
                        self.local_transport_addr = None
                        self.nbr_hold_time = None
                        self.nbr_ldp_id = None
                        self.nbr_src_addr = None
                        self.next_hello = None
                        self.session_up = None

                    @property
                    def _common_path(self):
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')
                        if self.nbr_transport_addr is None:
                            raise YPYModelError('Key property nbr_transport_addr is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:link-hello-state/Cisco-IOS-XE-mpls-ldp:link-hellos[Cisco-IOS-XE-mpls-ldp:interface = ' + str(self.interface) + '][Cisco-IOS-XE-mpls-ldp:nbr-transport-addr = ' + str(self.nbr_transport_addr) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.nbr_transport_addr is not None:
                            return True

                        if self.hello_interval is not None:
                            return True

                        if self.hold_time_remaining is not None:
                            return True

                        if self.local_src_addr is not None:
                            return True

                        if self.local_transport_addr is not None:
                            return True

                        if self.nbr_hold_time is not None:
                            return True

                        if self.nbr_ldp_id is not None:
                            return True

                        if self.nbr_src_addr is not None:
                            return True

                        if self.next_hello is not None:
                            return True

                        if self.session_up is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Discovery.LinkHelloState.LinkHellos']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:link-hello-state'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.link_hellos is not None:
                        for child_ref in self.link_hellos:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Discovery.LinkHelloState']['meta_info']


            class TargetedHellos(object):
                """
                The LDP Discovery Targeted Hello state.
                
                .. attribute:: targeted_hello
                
                	The LDP targeted discovery information for a specific target. Targetted discovery creates a single adjacency between two addresses and not indiviual adjacencies across physical interfaces
                	**type**\: list of    :py:class:`TargetedHello <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello>`
                
                .. attribute:: targeted_hello_hold_time
                
                	Local Targeted hold time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: targeted_hello_interval
                
                	Local Targeted Hello interval in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.targeted_hello = YList()
                    self.targeted_hello.parent = self
                    self.targeted_hello.name = 'targeted_hello'
                    self.targeted_hello_hold_time = None
                    self.targeted_hello_interval = None


                class TargetedHello(object):
                    """
                    The LDP targeted discovery information for a specific
                    target. Targetted discovery creates a single adjacency
                    between two addresses and not indiviual adjacencies
                    across physical interfaces.
                    
                    .. attribute:: vrf_name  <key>
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\:  str
                    
                    .. attribute:: target_address  <key>
                    
                    	The target IP Address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: hold_time_remaining
                    
                    	This is the MPLS LDP Hello Discovery expiry time in seconds. If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**units**\: seconds
                    
                    .. attribute:: local_address
                    
                    	Local IP Address
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: nbr_hold_time
                    
                    	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the EntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: neighbor_ldp_identifier
                    
                    	Neighbor LDP Identifier
                    	**type**\:  str
                    
                    .. attribute:: next_hello
                    
                    	Next hello due time in milliseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: state
                    
                    	This is the MPLS LDP Targeted Hello state
                    	**type**\:   :py:class:`DhcStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.DhcStateEnum>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.target_address = None
                        self.hold_time_remaining = None
                        self.local_address = None
                        self.nbr_hold_time = None
                        self.neighbor_ldp_identifier = None
                        self.next_hello = None
                        self.state = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')
                        if self.target_address is None:
                            raise YPYModelError('Key property target_address is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:targeted-hellos/Cisco-IOS-XE-mpls-ldp:targeted-hello[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:target-address = ' + str(self.target_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.target_address is not None:
                            return True

                        if self.hold_time_remaining is not None:
                            return True

                        if self.local_address is not None:
                            return True

                        if self.nbr_hold_time is not None:
                            return True

                        if self.neighbor_ldp_identifier is not None:
                            return True

                        if self.next_hello is not None:
                            return True

                        if self.state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Discovery.TargetedHellos.TargetedHello']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:targeted-hellos'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.targeted_hello is not None:
                        for child_ref in self.targeted_hello:
                            if child_ref._has_data():
                                return True

                    if self.targeted_hello_hold_time is not None:
                        return True

                    if self.targeted_hello_interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Discovery.TargetedHellos']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:discovery'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.discovery_stats is not None and self.discovery_stats._has_data():
                    return True

                if self.link_hello_state is not None and self.link_hello_state._has_data():
                    return True

                if self.targeted_hellos is not None and self.targeted_hellos._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Discovery']['meta_info']


        class Forwarding(object):
            """
            Summary information regarding LDP forwarding
            setup and detailed LDP Forwarding rewrites
            
            .. attribute:: forwarding_detail
            
            	This leaf contain the individual LDP forwarding rewrite for a single prefix
            	**type**\: list of    :py:class:`ForwardingDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail>`
            
            .. attribute:: forwarding_vrf_summs
            
            	Summary of forwarding info for this VRF
            	**type**\:   :py:class:`ForwardingVrfSumms <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.forwarding_detail = YList()
                self.forwarding_detail.parent = self
                self.forwarding_detail.name = 'forwarding_detail'
                self.forwarding_vrf_summs = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms()
                self.forwarding_vrf_summs.parent = self


            class ForwardingVrfSumms(object):
                """
                Summary of forwarding info for this VRF.
                
                .. attribute:: forwarding_vrf_summ
                
                	Summary of forwarding info for this VRF
                	**type**\: list of    :py:class:`ForwardingVrfSumm <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.forwarding_vrf_summ = YList()
                    self.forwarding_vrf_summ.parent = self
                    self.forwarding_vrf_summ.name = 'forwarding_vrf_summ'


                class ForwardingVrfSumm(object):
                    """
                    Summary of forwarding info for this VRF.
                    
                    .. attribute:: vrf_name  <key>
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\:  str
                    
                    .. attribute:: intfs_fwd_count
                    
                    	MPLS forwarding enabled interface count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_lbls
                    
                    	Local label allocated count
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: nhs
                    
                    	MPLS LDP forwarding rewrite next\-hop/path summary
                    	**type**\:   :py:class:`Nhs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs>`
                    
                    .. attribute:: pfxs
                    
                    	MPLS LDP forwarding prefix rewrite summary
                    	**type**\:   :py:class:`Pfxs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.intfs_fwd_count = None
                        self.local_lbls = None
                        self.nhs = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs()
                        self.nhs.parent = self
                        self.pfxs = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs()
                        self.pfxs.parent = self


                    class Pfxs(object):
                        """
                        MPLS LDP forwarding prefix rewrite summary
                        
                        .. attribute:: ecmp_pfxs
                        
                        	Count of prefixes with ECMP
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: labeled_pfxs_aggr
                        
                        	Labeled prefix count for all paths
                        	**type**\:   :py:class:`LabeledPfxsAggr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr>`
                        
                        .. attribute:: labeled_pfxs_backup
                        
                        	Labeled prefix count related to backup paths only
                        	**type**\:   :py:class:`LabeledPfxsBackup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup>`
                        
                        .. attribute:: labeled_pfxs_primary
                        
                        	Labeled prefix count related to primary paths only
                        	**type**\:   :py:class:`LabeledPfxsPrimary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary>`
                        
                        .. attribute:: protected_pfxs
                        
                        	Count of FRR protected prefixes
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: total_pfxs
                        
                        	Total Prefix count
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.ecmp_pfxs = None
                            self.labeled_pfxs_aggr = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr()
                            self.labeled_pfxs_aggr.parent = self
                            self.labeled_pfxs_backup = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup()
                            self.labeled_pfxs_backup.parent = self
                            self.labeled_pfxs_primary = MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary()
                            self.labeled_pfxs_primary.parent = self
                            self.protected_pfxs = None
                            self.total_pfxs = None


                        class LabeledPfxsAggr(object):
                            """
                            Labeled prefix count for all paths
                            
                            .. attribute:: labeled_pfxs
                            
                            	Count of labeled prefixes with 1 or more paths labeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: labeled_pfxs_partial
                            
                            	Count of labeled prefixes with some (but not ALL) paths labeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: unlabeled_pfxs
                            
                            	Count of labeled prefixes with ALL paths unlabeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.labeled_pfxs = None
                                self.labeled_pfxs_partial = None
                                self.unlabeled_pfxs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:labeled-pfxs-aggr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.labeled_pfxs is not None:
                                    return True

                                if self.labeled_pfxs_partial is not None:
                                    return True

                                if self.unlabeled_pfxs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsAggr']['meta_info']


                        class LabeledPfxsPrimary(object):
                            """
                            Labeled prefix count related to primary paths
                            only
                            
                            .. attribute:: labeled_pfxs
                            
                            	Count of labeled prefixes with 1 or more paths labeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: labeled_pfxs_partial
                            
                            	Count of labeled prefixes with some (but not ALL) paths labeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: unlabeled_pfxs
                            
                            	Count of labeled prefixes with ALL paths unlabeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.labeled_pfxs = None
                                self.labeled_pfxs_partial = None
                                self.unlabeled_pfxs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:labeled-pfxs-primary'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.labeled_pfxs is not None:
                                    return True

                                if self.labeled_pfxs_partial is not None:
                                    return True

                                if self.unlabeled_pfxs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsPrimary']['meta_info']


                        class LabeledPfxsBackup(object):
                            """
                            Labeled prefix count related to backup paths
                            only
                            
                            .. attribute:: labeled_pfxs
                            
                            	Count of labeled prefixes with 1 or more paths labeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: labeled_pfxs_partial
                            
                            	Count of labeled prefixes with some (but not ALL) paths labeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: unlabeled_pfxs
                            
                            	Count of labeled prefixes with ALL paths unlabeled
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.labeled_pfxs = None
                                self.labeled_pfxs_partial = None
                                self.unlabeled_pfxs = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:labeled-pfxs-backup'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.labeled_pfxs is not None:
                                    return True

                                if self.labeled_pfxs_partial is not None:
                                    return True

                                if self.unlabeled_pfxs is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs.LabeledPfxsBackup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:pfxs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ecmp_pfxs is not None:
                                return True

                            if self.labeled_pfxs_aggr is not None and self.labeled_pfxs_aggr._has_data():
                                return True

                            if self.labeled_pfxs_backup is not None and self.labeled_pfxs_backup._has_data():
                                return True

                            if self.labeled_pfxs_primary is not None and self.labeled_pfxs_primary._has_data():
                                return True

                            if self.protected_pfxs is not None:
                                return True

                            if self.total_pfxs is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Pfxs']['meta_info']


                    class Nhs(object):
                        """
                        MPLS LDP forwarding rewrite next\-hop/path summary
                        
                        .. attribute:: backup_paths
                        
                        	Count of non\-primary backup paths
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: labeled_backup_paths
                        
                        	Count of labeled backup paths
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: labeled_paths
                        
                        	Count of all labeled paths
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protected_paths
                        
                        	Count of FRR protected paths
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_backup_paths
                        
                        	Count of non\-primary remote backup paths
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_paths
                        
                        	Total path count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.backup_paths = None
                            self.labeled_backup_paths = None
                            self.labeled_paths = None
                            self.protected_paths = None
                            self.remote_backup_paths = None
                            self.total_paths = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:nhs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.backup_paths is not None:
                                return True

                            if self.labeled_backup_paths is not None:
                                return True

                            if self.labeled_paths is not None:
                                return True

                            if self.protected_paths is not None:
                                return True

                            if self.remote_backup_paths is not None:
                                return True

                            if self.total_paths is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm.Nhs']['meta_info']

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding/Cisco-IOS-XE-mpls-ldp:forwarding-vrf-summs/Cisco-IOS-XE-mpls-ldp:forwarding-vrf-summ[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.intfs_fwd_count is not None:
                            return True

                        if self.local_lbls is not None:
                            return True

                        if self.nhs is not None and self.nhs._has_data():
                            return True

                        if self.pfxs is not None and self.pfxs._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms.ForwardingVrfSumm']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding/Cisco-IOS-XE-mpls-ldp:forwarding-vrf-summs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.forwarding_vrf_summ is not None:
                        for child_ref in self.forwarding_vrf_summ:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingVrfSumms']['meta_info']


            class ForwardingDetail(object):
                """
                This leaf contain the individual LDP forwarding rewrite
                for a single prefix.
                
                .. attribute:: vrf_name  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	The IP Prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: fwd_prefix
                
                	This is the MPLS LDP Forward IP Prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: paths
                
                	MPLS LDP Forwarding Path info
                	**type**\: list of    :py:class:`Paths <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths>`
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: route
                
                	MPLS LDP Forwarding Route information
                	**type**\:   :py:class:`Route <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route>`
                
                .. attribute:: table_id
                
                	Table ID associated with IP prefix
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.prefix = None
                    self.fwd_prefix = None
                    self.paths = YList()
                    self.paths.parent = self
                    self.paths.name = 'paths'
                    self.prefix_length = None
                    self.route = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route()
                    self.route.parent = self
                    self.table_id = None


                class Route(object):
                    """
                    MPLS LDP Forwarding Route information
                    
                    .. attribute:: forwarding_update_age
                    
                    	Last Forwarding update nanosec age
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: forwarding_update_count
                    
                    	Number of forwarding updates
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forwarding_update_timestamp
                    
                    	Last Forwarding update nanosec timestamp
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: is_local_vrf_leaked
                    
                    	Is this route leaked across local VRFs?
                    	**type**\:  bool
                    
                    .. attribute:: local_label
                    
                    	Local label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: metric
                    
                    	Route metric
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: priority
                    
                    	Route priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: routing_update_age
                    
                    	Last Routing update nanosec age
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: routing_update_count
                    
                    	Number of routing updates
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: routing_update_timestamp
                    
                    	Last Routing update nanosec timestamp
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: nanoseconds
                    
                    .. attribute:: source
                    
                    	Route source protocol Id
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: type
                    
                    	Route type
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: version
                    
                    	Route RIB version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.forwarding_update_age = None
                        self.forwarding_update_count = None
                        self.forwarding_update_timestamp = None
                        self.is_local_vrf_leaked = None
                        self.local_label = None
                        self.metric = None
                        self.priority = None
                        self.routing_update_age = None
                        self.routing_update_count = None
                        self.routing_update_timestamp = None
                        self.source = None
                        self.type = None
                        self.version = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:route'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.forwarding_update_age is not None:
                            return True

                        if self.forwarding_update_count is not None:
                            return True

                        if self.forwarding_update_timestamp is not None:
                            return True

                        if self.is_local_vrf_leaked is not None:
                            return True

                        if self.local_label is not None:
                            return True

                        if self.metric is not None:
                            return True

                        if self.priority is not None:
                            return True

                        if self.routing_update_age is not None:
                            return True

                        if self.routing_update_count is not None:
                            return True

                        if self.routing_update_timestamp is not None:
                            return True

                        if self.source is not None:
                            return True

                        if self.type is not None:
                            return True

                        if self.version is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Route']['meta_info']


                class Paths(object):
                    """
                    MPLS LDP Forwarding Path info
                    
                    .. attribute:: mpls
                    
                    	MPLS LDP Forwarding Path MPLS information
                    	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls>`
                    
                    .. attribute:: routing
                    
                    	MPLS LDP Forwarding Path IP Routing information
                    	**type**\:   :py:class:`Routing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.mpls = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls()
                        self.mpls.parent = self
                        self.routing = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing()
                        self.routing.parent = self


                    class Routing(object):
                        """
                        MPLS LDP Forwarding Path IP Routing information
                        
                        .. attribute:: bkup_path_id
                        
                        	Backup path Id
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: has_remote_lfa_bkup
                        
                        	This is true if the path has a remote LFA backup
                        	**type**\:  bool
                        
                        .. attribute:: interface
                        
                        	This is the interface
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        .. attribute:: load_metric
                        
                        	Path's load metric for load balancing
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop
                        
                        	This is the Next Hop address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: next_hop_table_id
                        
                        	Table ID for nexthop address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nexthop_id
                        
                        	Nexthop Identifier
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nh_is_overriden
                        
                        	This is set when the nexthop is overriden by LDP
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: path_id
                        
                        	path Id
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: path_type
                        
                        	Routing path type
                        	**type**\:   :py:class:`RoutePathTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RoutePathTypeIdentity>`
                        
                        .. attribute:: remote_node_id
                        
                        	This is the Remote/PQ node address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.bkup_path_id = None
                            self.has_remote_lfa_bkup = None
                            self.interface = None
                            self.load_metric = None
                            self.next_hop = None
                            self.next_hop_table_id = None
                            self.nexthop_id = None
                            self.nh_is_overriden = None
                            self.path_id = None
                            self.path_type = None
                            self.remote_node_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:routing'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.bkup_path_id is not None:
                                return True

                            if self.has_remote_lfa_bkup is not None:
                                return True

                            if self.interface is not None:
                                return True

                            if self.load_metric is not None:
                                return True

                            if self.next_hop is not None:
                                return True

                            if self.next_hop_table_id is not None:
                                return True

                            if self.nexthop_id is not None:
                                return True

                            if self.nh_is_overriden is not None:
                                return True

                            if self.path_id is not None:
                                return True

                            if self.path_type is not None:
                                return True

                            if self.remote_node_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Routing']['meta_info']


                    class Mpls(object):
                        """
                        MPLS LDP Forwarding Path MPLS information
                        
                        .. attribute:: mpls_outgoing_info
                        
                        	MPLS nexthop info
                        	**type**\:   :py:class:`MplsOutgoingInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo>`
                        
                        .. attribute:: remote_lfa
                        
                        	MPLS LDP Forwarding Path Remote LFA\-FRR backup MPLS info
                        	**type**\:   :py:class:`RemoteLfa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.mpls_outgoing_info = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo()
                            self.mpls_outgoing_info.parent = self
                            self.remote_lfa = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa()
                            self.remote_lfa.parent = self


                        class MplsOutgoingInfo(object):
                            """
                            MPLS nexthop info
                            
                            .. attribute:: is_from_graceful_restartable_neighbor
                            
                            	Is from a GR neighbor
                            	**type**\:  bool
                            
                            .. attribute:: is_stale
                            
                            	Is the entry stale? This may happen during a graceful restart
                            	**type**\:  bool
                            
                            .. attribute:: nexthop_peer_ldp_ident
                            
                            	Nexthop LDP peer
                            	**type**\:   :py:class:`NexthopPeerLdpIdent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent>`
                            
                            .. attribute:: out_label
                            
                            	Outgoing label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_label_owner
                            
                            	Outgoing label owner
                            	**type**\:   :py:class:`RoutePathLblOwnerIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RoutePathLblOwnerIdentity>`
                            
                            .. attribute:: out_label_type
                            
                            	Outgoing Label Type
                            	**type**\:   :py:class:`LabelTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LabelTypeIdentity>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.is_from_graceful_restartable_neighbor = None
                                self.is_stale = None
                                self.nexthop_peer_ldp_ident = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent()
                                self.nexthop_peer_ldp_ident.parent = self
                                self.out_label = None
                                self.out_label_owner = None
                                self.out_label_type = None


                            class NexthopPeerLdpIdent(object):
                                """
                                Nexthop LDP peer
                                
                                .. attribute:: label_space_id
                                
                                	Label space identifier
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: lsr_id
                                
                                	LSR identifier
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    self.parent = None
                                    self.label_space_id = None
                                    self.lsr_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:nexthop-peer-ldp-ident'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.label_space_id is not None:
                                        return True

                                    if self.lsr_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                    return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo.NexthopPeerLdpIdent']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:mpls-outgoing-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.is_from_graceful_restartable_neighbor is not None:
                                    return True

                                if self.is_stale is not None:
                                    return True

                                if self.nexthop_peer_ldp_ident is not None and self.nexthop_peer_ldp_ident._has_data():
                                    return True

                                if self.out_label is not None:
                                    return True

                                if self.out_label_owner is not None:
                                    return True

                                if self.out_label_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.MplsOutgoingInfo']['meta_info']


                        class RemoteLfa(object):
                            """
                            MPLS LDP Forwarding Path Remote LFA\-FRR backup
                            MPLS info
                            
                            .. attribute:: has_remote_lfa_bkup
                            
                            	Whether path has remote LFA backup
                            	**type**\:  bool
                            
                            .. attribute:: mpls_outgoing_info
                            
                            	Remote LFA MPLS nexthop info
                            	**type**\:   :py:class:`MplsOutgoingInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.has_remote_lfa_bkup = None
                                self.mpls_outgoing_info = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo()
                                self.mpls_outgoing_info.parent = self


                            class MplsOutgoingInfo(object):
                                """
                                Remote LFA MPLS nexthop info
                                
                                .. attribute:: is_from_graceful_restartable_neighbor
                                
                                	Is from a GR neighbor
                                	**type**\:  bool
                                
                                .. attribute:: is_stale
                                
                                	Is the entry stale? This may happen during a graceful restart
                                	**type**\:  bool
                                
                                .. attribute:: nexthop_peer_ldp_ident
                                
                                	Nexthop LDP peer
                                	**type**\:   :py:class:`NexthopPeerLdpIdent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent>`
                                
                                .. attribute:: out_label
                                
                                	Outgoing label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: out_label_owner
                                
                                	Outgoing label owner
                                	**type**\:   :py:class:`RoutePathLblOwnerIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RoutePathLblOwnerIdentity>`
                                
                                .. attribute:: out_label_type
                                
                                	Outgoing Label Type
                                	**type**\:   :py:class:`LabelTypeIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LabelTypeIdentity>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-ios-xe-oper'
                                _revision = '2017-02-07'

                                def __init__(self):
                                    self.parent = None
                                    self.is_from_graceful_restartable_neighbor = None
                                    self.is_stale = None
                                    self.nexthop_peer_ldp_ident = MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent()
                                    self.nexthop_peer_ldp_ident.parent = self
                                    self.out_label = None
                                    self.out_label_owner = None
                                    self.out_label_type = None


                                class NexthopPeerLdpIdent(object):
                                    """
                                    Nexthop LDP peer
                                    
                                    .. attribute:: label_space_id
                                    
                                    	Label space identifier
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: lsr_id
                                    
                                    	LSR identifier
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    

                                    """

                                    _prefix = 'mpls-ldp-ios-xe-oper'
                                    _revision = '2017-02-07'

                                    def __init__(self):
                                        self.parent = None
                                        self.label_space_id = None
                                        self.lsr_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:nexthop-peer-ldp-ident'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.label_space_id is not None:
                                            return True

                                        if self.lsr_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                        return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo.NexthopPeerLdpIdent']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:mpls-outgoing-info'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.is_from_graceful_restartable_neighbor is not None:
                                        return True

                                    if self.is_stale is not None:
                                        return True

                                    if self.nexthop_peer_ldp_ident is not None and self.nexthop_peer_ldp_ident._has_data():
                                        return True

                                    if self.out_label is not None:
                                        return True

                                    if self.out_label_owner is not None:
                                        return True

                                    if self.out_label_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                    return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa.MplsOutgoingInfo']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:remote-lfa'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.has_remote_lfa_bkup is not None:
                                    return True

                                if self.mpls_outgoing_info is not None and self.mpls_outgoing_info._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls.RemoteLfa']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:mpls'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.mpls_outgoing_info is not None and self.mpls_outgoing_info._has_data():
                                return True

                            if self.remote_lfa is not None and self.remote_lfa._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths.Mpls']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:paths'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.mpls is not None and self.mpls._has_data():
                            return True

                        if self.routing is not None and self.routing._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail.Paths']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.prefix is None:
                        raise YPYModelError('Key property prefix is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding/Cisco-IOS-XE-mpls-ldp:forwarding-detail[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:prefix = ' + str(self.prefix) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.fwd_prefix is not None:
                        return True

                    if self.paths is not None:
                        for child_ref in self.paths:
                            if child_ref._has_data():
                                return True

                    if self.prefix_length is not None:
                        return True

                    if self.route is not None and self.route._has_data():
                        return True

                    if self.table_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Forwarding.ForwardingDetail']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:forwarding'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.forwarding_detail is not None:
                    for child_ref in self.forwarding_detail:
                        if child_ref._has_data():
                            return True

                if self.forwarding_vrf_summs is not None and self.forwarding_vrf_summs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Forwarding']['meta_info']


        class Bindings(object):
            """
            The detailed LDP Bindings.
            
            .. attribute:: binding
            
            	This list contains the MPLS LDP Label Bindings for each IP Prefix. Label bindings provide the local MPLS Label, a list of remote labels, any filters affecting advertisment of that filter, and a list of neighbors to which the label has been advertised
            	**type**\: list of    :py:class:`Binding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding>`
            
            .. attribute:: bindings_sum_afs
            
            	This container holds the bindings specific to this VRF and AF
            	**type**\:   :py:class:`BindingsSumAfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.BindingsSumAfs>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.binding = YList()
                self.binding.parent = self
                self.binding.name = 'binding'
                self.bindings_sum_afs = MplsLdp.MplsLdpState.Bindings.BindingsSumAfs()
                self.bindings_sum_afs.parent = self


            class BindingsSumAfs(object):
                """
                This container holds the bindings specific to this VRF
                and AF.
                
                .. attribute:: binding_sum_af
                
                	Counters for the LDP Label Information Base for this VRF/AF
                	**type**\: list of    :py:class:`BindingSumAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.binding_sum_af = YList()
                    self.binding_sum_af.parent = self
                    self.binding_sum_af.name = 'binding_sum_af'


                class BindingSumAf(object):
                    """
                    Counters for the LDP Label Information Base for this
                    VRF/AF.
                    
                    .. attribute:: vrf_name  <key>
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\:  str
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                    
                    .. attribute:: binding_local
                    
                    	Number of local bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_explicit_null
                    
                    	Number of local explicit null bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_implicit_null
                    
                    	Number of local implicit null bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_no_route
                    
                    	Local bindings with no route
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_non_null
                    
                    	Number of local non\-null bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_null
                    
                    	Number of local null bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_local_oor
                    
                    	This is the number of local bindings needing label but which hit the Out\-Of\-Resource condition
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_no_route
                    
                    	Bindings with no route
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_remote
                    
                    	Number of remote bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: binding_total
                    
                    	Total bindings
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: highest_allocated_label
                    
                    	Highest allocated label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: lowest_allocated_label
                    
                    	Lowest allocated label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.af_name = None
                        self.binding_local = None
                        self.binding_local_explicit_null = None
                        self.binding_local_implicit_null = None
                        self.binding_local_no_route = None
                        self.binding_local_non_null = None
                        self.binding_local_null = None
                        self.binding_local_oor = None
                        self.binding_no_route = None
                        self.binding_remote = None
                        self.binding_total = None
                        self.highest_allocated_label = None
                        self.lowest_allocated_label = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')
                        if self.af_name is None:
                            raise YPYModelError('Key property af_name is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:bindings/Cisco-IOS-XE-mpls-ldp:bindings-sum-afs/Cisco-IOS-XE-mpls-ldp:binding-sum-af[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:af-name = ' + str(self.af_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.binding_local is not None:
                            return True

                        if self.binding_local_explicit_null is not None:
                            return True

                        if self.binding_local_implicit_null is not None:
                            return True

                        if self.binding_local_no_route is not None:
                            return True

                        if self.binding_local_non_null is not None:
                            return True

                        if self.binding_local_null is not None:
                            return True

                        if self.binding_local_oor is not None:
                            return True

                        if self.binding_no_route is not None:
                            return True

                        if self.binding_remote is not None:
                            return True

                        if self.binding_total is not None:
                            return True

                        if self.highest_allocated_label is not None:
                            return True

                        if self.lowest_allocated_label is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Bindings.BindingsSumAfs.BindingSumAf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:bindings/Cisco-IOS-XE-mpls-ldp:bindings-sum-afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.binding_sum_af is not None:
                        for child_ref in self.binding_sum_af:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Bindings.BindingsSumAfs']['meta_info']


            class Binding(object):
                """
                This list contains the MPLS LDP Label Bindings for each
                IP Prefix. Label bindings provide the local MPLS Label,
                a list of remote labels, any filters affecting
                advertisment of that filter, and a list of neighbors to
                which the label has been advertised.
                
                .. attribute:: vrf_name  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: prefix  <key>
                
                	This leaf contains the IP Prefix being bound
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                
                
                ----
                .. attribute:: advertise_lsr_filter
                
                	This contains the filter name for this binding's Advertise LSR. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                .. attribute:: advertise_prefix_filter
                
                	This contains the filter name for this binding's prefix. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                .. attribute:: config_enforced_local_label_value
                
                	Config/User enforced local label value
                	**type**\:  bool
                
                .. attribute:: fwd_prefix
                
                	This is the MPLS LDP Binding IP Prefix
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: is_no_route
                
                	This is true if the MPLS LDP Binding has no route
                	**type**\:  bool
                
                .. attribute:: label_oor
                
                	This is true if the MPLS LDP Binding Label space is depleted, Out Of Resource. No new labels can be allocated
                	**type**\:  bool
                
                .. attribute:: le_local_binding_revision
                
                	This is the MPLS LDP Binding Local Binding revision
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: le_local_label_state
                
                	This is the MPLS LDP Binding Local label state
                	**type**\:   :py:class:`LocalLabelStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.LocalLabelStateEnum>`
                
                .. attribute:: local_label
                
                	This is the MPLS LDP Binding Local label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peers_advertised_to
                
                	Peers to which this entry is advertised
                	**type**\: list of    :py:class:`PeersAdvertisedTo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo>`
                
                .. attribute:: prefix_length
                
                	This is the MPLS LDP Binding Prefix Length
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: remote_binding
                
                	MPLS LDP Remote Binding Information
                	**type**\: list of    :py:class:`RemoteBinding <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.prefix = None
                    self.advertise_lsr_filter = None
                    self.advertise_prefix_filter = None
                    self.config_enforced_local_label_value = None
                    self.fwd_prefix = None
                    self.is_no_route = None
                    self.label_oor = None
                    self.le_local_binding_revision = None
                    self.le_local_label_state = None
                    self.local_label = None
                    self.peers_advertised_to = YList()
                    self.peers_advertised_to.parent = self
                    self.peers_advertised_to.name = 'peers_advertised_to'
                    self.prefix_length = None
                    self.remote_binding = YList()
                    self.remote_binding.parent = self
                    self.remote_binding.name = 'remote_binding'


                class RemoteBinding(object):
                    """
                    MPLS LDP Remote Binding Information
                    
                    .. attribute:: assigning_peer_ldp_ident
                    
                    	Assigning peer
                    	**type**\:   :py:class:`AssigningPeerLdpIdent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent>`
                    
                    .. attribute:: is_stale
                    
                    	Is the entry stale
                    	**type**\:  bool
                    
                    .. attribute:: remote_label
                    
                    	This is the remote Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.assigning_peer_ldp_ident = MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent()
                        self.assigning_peer_ldp_ident.parent = self
                        self.is_stale = None
                        self.remote_label = None


                    class AssigningPeerLdpIdent(object):
                        """
                        Assigning peer
                        
                        .. attribute:: label_space_id
                        
                        	Label space identifier
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: lsr_id
                        
                        	LSR identifier
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.label_space_id = None
                            self.lsr_id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:assigning-peer-ldp-ident'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.label_space_id is not None:
                                return True

                            if self.lsr_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding.AssigningPeerLdpIdent']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:remote-binding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.assigning_peer_ldp_ident is not None and self.assigning_peer_ldp_ident._has_data():
                            return True

                        if self.is_stale is not None:
                            return True

                        if self.remote_label is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Bindings.Binding.RemoteBinding']['meta_info']


                class PeersAdvertisedTo(object):
                    """
                    Peers to which this entry is advertised.
                    
                    .. attribute:: label_space_id
                    
                    	Label space identifier
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: lsr_id
                    
                    	LSR identifier
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.label_space_id = None
                        self.lsr_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:peers-advertised-to'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.label_space_id is not None:
                            return True

                        if self.lsr_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Bindings.Binding.PeersAdvertisedTo']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.prefix is None:
                        raise YPYModelError('Key property prefix is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:bindings/Cisco-IOS-XE-mpls-ldp:binding[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:prefix = ' + str(self.prefix) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.prefix is not None:
                        return True

                    if self.advertise_lsr_filter is not None:
                        return True

                    if self.advertise_prefix_filter is not None:
                        return True

                    if self.config_enforced_local_label_value is not None:
                        return True

                    if self.fwd_prefix is not None:
                        return True

                    if self.is_no_route is not None:
                        return True

                    if self.label_oor is not None:
                        return True

                    if self.le_local_binding_revision is not None:
                        return True

                    if self.le_local_label_state is not None:
                        return True

                    if self.local_label is not None:
                        return True

                    if self.peers_advertised_to is not None:
                        for child_ref in self.peers_advertised_to:
                            if child_ref._has_data():
                                return True

                    if self.prefix_length is not None:
                        return True

                    if self.remote_binding is not None:
                        for child_ref in self.remote_binding:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Bindings.Binding']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:bindings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.binding is not None:
                    for child_ref in self.binding:
                        if child_ref._has_data():
                            return True

                if self.bindings_sum_afs is not None and self.bindings_sum_afs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Bindings']['meta_info']


        class Neighbors(object):
            """
            The LDP Neighbors Information
            
            .. attribute:: backoffs
            
            	LDP Backoff Information
            	**type**\:   :py:class:`Backoffs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Backoffs>`
            
            .. attribute:: nbr_adjs
            
            	For this Neighbor, this is the list of adjacencies between the neighbor and the local node
            	**type**\: list of    :py:class:`NbrAdjs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NbrAdjs>`
            
            .. attribute:: neighbor
            
            	Information on a particular LDP neighbor
            	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor>`
            
            .. attribute:: nsr_nbr_detail
            
            	This is the LDP NSR state for this neighbor
            	**type**\:   :py:class:`NsrNbrDetail <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail>`
            
            .. attribute:: stats_info
            
            	MPLS LDP Statistics Information
            	**type**\:   :py:class:`StatsInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.StatsInfo>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.backoffs = MplsLdp.MplsLdpState.Neighbors.Backoffs()
                self.backoffs.parent = self
                self.nbr_adjs = YList()
                self.nbr_adjs.parent = self
                self.nbr_adjs.name = 'nbr_adjs'
                self.neighbor = YList()
                self.neighbor.parent = self
                self.neighbor.name = 'neighbor'
                self.nsr_nbr_detail = MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail()
                self.nsr_nbr_detail.parent = self
                self.stats_info = MplsLdp.MplsLdpState.Neighbors.StatsInfo()
                self.stats_info.parent = self


            class Neighbor(object):
                """
                Information on a particular LDP neighbor
                
                .. attribute:: vrf_name  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: lsr_id  <key>
                
                	LSR ID of neighbor
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: advertise_bgp_prefixes
                
                	True if BGP labeled prefixes are advertised to the neighbor
                	**type**\:  bool
                
                .. attribute:: bgp_advertisement_state
                
                	BGP labeled prefixes advertisement state
                	**type**\:   :py:class:`NbrBgpAdvtStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NbrBgpAdvtStateEnum>`
                
                .. attribute:: capabilities
                
                	Capabilities sent to and received from neighbor
                	**type**\:   :py:class:`Capabilities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities>`
                
                .. attribute:: client
                
                	Targeted Session clients
                	**type**\:  list of str
                
                .. attribute:: downstream_on_demand
                
                	Is Label advertisement mode in Downstream On Demand mode or not?
                	**type**\:  bool
                
                .. attribute:: duplicate_address
                
                	Duplicate IPv4/IPv6 address bound to this peer
                	**type**\: one of the below types:
                
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: graceful_restart_adjacency
                
                	This container holds the graceful restart information for this adjacency
                	**type**\:   :py:class:`GracefulRestartAdjacency <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency>`
                
                .. attribute:: has_sp
                
                	Session Protection enabled
                	**type**\:  bool
                
                .. attribute:: inbound_ipv4
                
                	This contains the IPv4 Inbound accept filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: inbound_ipv6_filter
                
                	This contains the IPv6 Inbound accept filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: label_space_id
                
                	Label space ID of neighbor
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: nbr_bound_address
                
                	This is the MPLS LDP Neighbor Bound IPv4/IPv6 Address
                	**type**\: one of the below types:
                
                	**type**\:  list of str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: nbr_path_vector_limit
                
                	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this neighor is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this neighbor is enabled and the Path Vector Limit is this value
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: nbr_stats
                
                	Neighbor Statistics
                	**type**\:   :py:class:`NbrStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats>`
                
                .. attribute:: outbound_ipv4_filter
                
                	This contains the IPv4 Outbound advertise filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: outbound_ipv6_filter
                
                	This contains the IPv6 Outbound advertise filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: peer_hold_time
                
                	Session holdtime value in seconds from the peer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: peer_keep_alive_interval
                
                	Session keepalive interval in seconds from the peer
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: peer_state
                
                	LDP adjacency peer state
                	**type**\:   :py:class:`AdjStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AdjStateEnum>`
                
                .. attribute:: session_prot_ver
                
                	The version of the LDP Protocol which this session is using.  This is the version of the LDP protocol which has been negotiated during session initialization
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: session_role
                
                	During session establishment the LSR/LER takes either the active role or the passive role based on address comparisons.  This object indicates whether this LSR/LER was behaving in an active role or passive role during this session's establishment.  The value of unknown(1), indicates that the role is not able to be determined at the present time
                	**type**\:   :py:class:`SessionRoleEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.SessionRoleEnum>`
                
                .. attribute:: sp_duration
                
                	Session protection holdup time duration in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: sp_filter
                
                	This contains the Session Protection filter name. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: sp_has_duration
                
                	Session Protection has non\-default duration
                	**type**\:  bool
                
                .. attribute:: sp_state
                
                	Session Protection state
                	**type**\:  str
                
                	**length:** 0..80
                
                .. attribute:: spht_remaining
                
                	Session Protection holdup time remaining value in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: spht_running
                
                	Session Protection holdup timer is running
                	**type**\:  bool
                
                .. attribute:: tcp_information
                
                	MPLS LDP Neighbor TCP Information
                	**type**\:   :py:class:`TcpInformation <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation>`
                
                .. attribute:: up_time_seconds
                
                	Up time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.lsr_id = None
                    self.advertise_bgp_prefixes = None
                    self.bgp_advertisement_state = None
                    self.capabilities = MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities()
                    self.capabilities.parent = self
                    self.client = YLeafList()
                    self.client.parent = self
                    self.client.name = 'client'
                    self.downstream_on_demand = None
                    self.duplicate_address = YLeafList()
                    self.duplicate_address.parent = self
                    self.duplicate_address.name = 'duplicate_address'
                    self.graceful_restart_adjacency = MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency()
                    self.graceful_restart_adjacency.parent = self
                    self.has_sp = None
                    self.inbound_ipv4 = None
                    self.inbound_ipv6_filter = None
                    self.label_space_id = None
                    self.nbr_bound_address = YLeafList()
                    self.nbr_bound_address.parent = self
                    self.nbr_bound_address.name = 'nbr_bound_address'
                    self.nbr_path_vector_limit = None
                    self.nbr_stats = MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats()
                    self.nbr_stats.parent = self
                    self.outbound_ipv4_filter = None
                    self.outbound_ipv6_filter = None
                    self.peer_hold_time = None
                    self.peer_keep_alive_interval = None
                    self.peer_state = None
                    self.session_prot_ver = None
                    self.session_role = None
                    self.sp_duration = None
                    self.sp_filter = None
                    self.sp_has_duration = None
                    self.sp_state = None
                    self.spht_remaining = None
                    self.spht_running = None
                    self.tcp_information = MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation()
                    self.tcp_information.parent = self
                    self.up_time_seconds = None

                class SessionRoleEnum(Enum):
                    """
                    SessionRoleEnum

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

                    unknown = 1

                    active = 2

                    passive = 3


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.SessionRoleEnum']



                class NbrStats(object):
                    """
                    Neighbor Statistics.
                    
                    .. attribute:: num_of_nbr_ipv4_addresses
                    
                    	Number of IPv4 addresses for which the neighbor is advertising labels
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv4_discovery
                    
                    	Number of neighbor IPv4 discovery sources
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv4_lbl
                    
                    	Number of IPv4 labels the neighbor is advertising
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv6_addresses
                    
                    	Number of IPv6 addresses for which the neighbor is advertising labels
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv6_discovery
                    
                    	Number of neighbor IPv6 discovery sources
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_of_nbr_ipv6_lbl
                    
                    	Number of IPv6 labels the neighbor is advertising
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ta_pies_rcvd
                    
                    	Number of MPLS LDP messages received from this neighbor
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ta_pies_sent
                    
                    	Number of MPLS LDP messages sent to this neighbor
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.num_of_nbr_ipv4_addresses = None
                        self.num_of_nbr_ipv4_discovery = None
                        self.num_of_nbr_ipv4_lbl = None
                        self.num_of_nbr_ipv6_addresses = None
                        self.num_of_nbr_ipv6_discovery = None
                        self.num_of_nbr_ipv6_lbl = None
                        self.ta_pies_rcvd = None
                        self.ta_pies_sent = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:nbr-stats'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.num_of_nbr_ipv4_addresses is not None:
                            return True

                        if self.num_of_nbr_ipv4_discovery is not None:
                            return True

                        if self.num_of_nbr_ipv4_lbl is not None:
                            return True

                        if self.num_of_nbr_ipv6_addresses is not None:
                            return True

                        if self.num_of_nbr_ipv6_discovery is not None:
                            return True

                        if self.num_of_nbr_ipv6_lbl is not None:
                            return True

                        if self.ta_pies_rcvd is not None:
                            return True

                        if self.ta_pies_sent is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.NbrStats']['meta_info']


                class GracefulRestartAdjacency(object):
                    """
                    This container holds the graceful restart information
                    for this adjacency.
                    
                    .. attribute:: down_nbr_down_reason
                    
                    	This identity provides the reason that the LDP Session with this neighbor is down. The reason does not persist if the session was down but is now recovered
                    	**type**\:   :py:class:`DownNbrReasonIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.DownNbrReasonIdentity>`
                    
                    .. attribute:: down_nbr_flap_count
                    
                    	This is the current count of back\-to\-back flaps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_graceful_restartable
                    
                    	Is this neighbor graceful restartable?
                    	**type**\:  bool
                    
                    .. attribute:: is_liveness_timer_running
                    
                    	This is set if the liveness timer is running
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: is_recovery_timer_running
                    
                    	This is set if the recovery timer is running
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: liveness_timer_remaining_seconds
                    
                    	Remaining time from liveness timer in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: reconnect_timeout
                    
                    	This leaf is the reconnect timeout in microseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: microseconds
                    
                    .. attribute:: recovery_time
                    
                    	This leaf is the recovery time in microseconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: microseconds
                    
                    .. attribute:: recovery_timer_remaining_seconds
                    
                    	Recovery timer remaining time in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.down_nbr_down_reason = None
                        self.down_nbr_flap_count = None
                        self.is_graceful_restartable = None
                        self.is_liveness_timer_running = None
                        self.is_recovery_timer_running = None
                        self.liveness_timer_remaining_seconds = None
                        self.reconnect_timeout = None
                        self.recovery_time = None
                        self.recovery_timer_remaining_seconds = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:graceful-restart-adjacency'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.down_nbr_down_reason is not None:
                            return True

                        if self.down_nbr_flap_count is not None:
                            return True

                        if self.is_graceful_restartable is not None:
                            return True

                        if self.is_liveness_timer_running is not None:
                            return True

                        if self.is_recovery_timer_running is not None:
                            return True

                        if self.liveness_timer_remaining_seconds is not None:
                            return True

                        if self.reconnect_timeout is not None:
                            return True

                        if self.recovery_time is not None:
                            return True

                        if self.recovery_timer_remaining_seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.GracefulRestartAdjacency']['meta_info']


                class TcpInformation(object):
                    """
                    MPLS LDP Neighbor TCP Information
                    
                    .. attribute:: foreign_host
                    
                    	This is the foreign host address used by TCP
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: foreign_port
                    
                    	Foreign port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: is_md5_on
                    
                    	Is MD5 Digest on
                    	**type**\:  bool
                    
                    .. attribute:: local_host
                    
                    	This is the local host address used by TCP
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: local_port
                    
                    	Local port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: up_time
                    
                    	up time
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.foreign_host = None
                        self.foreign_port = None
                        self.is_md5_on = None
                        self.local_host = None
                        self.local_port = None
                        self.up_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:tcp-information'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.foreign_host is not None:
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.is_md5_on is not None:
                            return True

                        if self.local_host is not None:
                            return True

                        if self.local_port is not None:
                            return True

                        if self.up_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.TcpInformation']['meta_info']


                class Capabilities(object):
                    """
                    Capabilities sent to and received from neighbor
                    
                    .. attribute:: received_caps
                    
                    	List of received capabilities
                    	**type**\: list of    :py:class:`ReceivedCaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps>`
                    
                    .. attribute:: sent_caps
                    
                    	List of sent capabilities
                    	**type**\: list of    :py:class:`SentCaps <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.received_caps = YList()
                        self.received_caps.parent = self
                        self.received_caps.name = 'received_caps'
                        self.sent_caps = YList()
                        self.sent_caps.parent = self
                        self.sent_caps.name = 'sent_caps'


                    class SentCaps(object):
                        """
                        List of sent capabilities
                        
                        .. attribute:: cap_type  <key>
                        
                        	Capability type (IANA assigned)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cap_des
                        
                        	Capability description
                        	**type**\:  str
                        
                        	**length:** 0..80
                        
                        .. attribute:: capability_data
                        
                        	Capability data
                        	**type**\:  str
                        
                        .. attribute:: capability_data_length
                        
                        	Capability data length
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.cap_type = None
                            self.cap_des = None
                            self.capability_data = None
                            self.capability_data_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.cap_type is None:
                                raise YPYModelError('Key property cap_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:sent-caps[Cisco-IOS-XE-mpls-ldp:cap-type = ' + str(self.cap_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.cap_type is not None:
                                return True

                            if self.cap_des is not None:
                                return True

                            if self.capability_data is not None:
                                return True

                            if self.capability_data_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.SentCaps']['meta_info']


                    class ReceivedCaps(object):
                        """
                        List of received capabilities
                        
                        .. attribute:: cap_type  <key>
                        
                        	Capability type (IANA assigned)
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cap_des
                        
                        	Capability description
                        	**type**\:  str
                        
                        	**length:** 0..80
                        
                        .. attribute:: capability_data
                        
                        	Capability data
                        	**type**\:  str
                        
                        .. attribute:: capability_data_length
                        
                        	Capability data length
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.cap_type = None
                            self.cap_des = None
                            self.capability_data = None
                            self.capability_data_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.cap_type is None:
                                raise YPYModelError('Key property cap_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:received-caps[Cisco-IOS-XE-mpls-ldp:cap-type = ' + str(self.cap_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.cap_type is not None:
                                return True

                            if self.cap_des is not None:
                                return True

                            if self.capability_data is not None:
                                return True

                            if self.capability_data_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities.ReceivedCaps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:capabilities'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.received_caps is not None:
                            for child_ref in self.received_caps:
                                if child_ref._has_data():
                                    return True

                        if self.sent_caps is not None:
                            for child_ref in self.sent_caps:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor.Capabilities']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.lsr_id is None:
                        raise YPYModelError('Key property lsr_id is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:neighbor[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:lsr-id = ' + str(self.lsr_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.lsr_id is not None:
                        return True

                    if self.advertise_bgp_prefixes is not None:
                        return True

                    if self.bgp_advertisement_state is not None:
                        return True

                    if self.capabilities is not None and self.capabilities._has_data():
                        return True

                    if self.client is not None:
                        for child in self.client:
                            if child is not None:
                                return True

                    if self.downstream_on_demand is not None:
                        return True

                    if self.duplicate_address is not None:
                        for child in self.duplicate_address:
                            if child is not None:
                                return True

                    if self.graceful_restart_adjacency is not None and self.graceful_restart_adjacency._has_data():
                        return True

                    if self.has_sp is not None:
                        return True

                    if self.inbound_ipv4 is not None:
                        return True

                    if self.inbound_ipv6_filter is not None:
                        return True

                    if self.label_space_id is not None:
                        return True

                    if self.nbr_bound_address is not None:
                        for child in self.nbr_bound_address:
                            if child is not None:
                                return True

                    if self.nbr_path_vector_limit is not None:
                        return True

                    if self.nbr_stats is not None and self.nbr_stats._has_data():
                        return True

                    if self.outbound_ipv4_filter is not None:
                        return True

                    if self.outbound_ipv6_filter is not None:
                        return True

                    if self.peer_hold_time is not None:
                        return True

                    if self.peer_keep_alive_interval is not None:
                        return True

                    if self.peer_state is not None:
                        return True

                    if self.session_prot_ver is not None:
                        return True

                    if self.session_role is not None:
                        return True

                    if self.sp_duration is not None:
                        return True

                    if self.sp_filter is not None:
                        return True

                    if self.sp_has_duration is not None:
                        return True

                    if self.sp_state is not None:
                        return True

                    if self.spht_remaining is not None:
                        return True

                    if self.spht_running is not None:
                        return True

                    if self.tcp_information is not None and self.tcp_information._has_data():
                        return True

                    if self.up_time_seconds is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Neighbor']['meta_info']


            class NbrAdjs(object):
                """
                For this Neighbor, this is the list of adjacencies
                between the neighbor and the local node.
                
                .. attribute:: interface
                
                	This is the interface used by MPLS LDP Link Hello
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: local_address
                
                	This is the local address used to send the Targeted Hello
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: target_address
                
                	This is the destination address used to send the Targeted Hello
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: target_state
                
                	This is the state of this Targeted Hello instance
                	**type**\:   :py:class:`DhcStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.DhcStateEnum>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.interface = None
                    self.local_address = None
                    self.target_address = None
                    self.target_state = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:nbr-adjs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface is not None:
                        return True

                    if self.local_address is not None:
                        return True

                    if self.target_address is not None:
                        return True

                    if self.target_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.NbrAdjs']['meta_info']


            class StatsInfo(object):
                """
                MPLS LDP Statistics Information
                
                .. attribute:: bad_ldpid
                
                	This object counts the number of Bad LDP Identifier Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_msg_len
                
                	This object counts the number of Bad Message Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_pdu_len
                
                	This object counts the number of Bad PDU Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_tlv_len
                
                	This object counts the number of Bad TLV Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: discon_time
                
                	The value of sysUpTime on the most recent occasion at which any one or more of this entity's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this entity of any counter32 object contained in the 'EntityStatsTable'.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: keep_alive_exp
                
                	This object counts the number of Session Keep Alive Timer Expired Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: malformed_tlv_val
                
                	This object counts the number of Malformed TLV Value Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: message_in
                
                	MPLS LDP message received counters from this neighbor
                	**type**\:   :py:class:`MessageIn <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn>`
                
                .. attribute:: message_out
                
                	MPLS LDP message sent counters to this neighbor
                	**type**\:   :py:class:`MessageOut <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut>`
                
                .. attribute:: sess_rej_ad
                
                	A count of the Session Rejected/Parameters Advertisement Mode Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_rej_lr
                
                	A count of the Session Rejected/Parameters Label Range Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_rej_max_pdu
                
                	A count of the Session Rejected/Parameters  Max Pdu Length Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sess_reject_no_hello
                
                	A count of the Session Rejected/No Hello Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_attempts
                
                	A count of the Session Initialization messages which were sent or received by this LDP Entity and were NAK'd.   In other words, this counter counts the number of session initializations that failed.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: shutdow_notif_sent
                
                	This object counts the number of Shutdown Notfications sent related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of  discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: shutdown_notif_rec
                
                	This object counts the number of Shutdown Notifications received related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bad_ldpid = None
                    self.bad_msg_len = None
                    self.bad_pdu_len = None
                    self.bad_tlv_len = None
                    self.discon_time = None
                    self.keep_alive_exp = None
                    self.malformed_tlv_val = None
                    self.message_in = MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn()
                    self.message_in.parent = self
                    self.message_out = MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut()
                    self.message_out.parent = self
                    self.sess_rej_ad = None
                    self.sess_rej_lr = None
                    self.sess_rej_max_pdu = None
                    self.sess_reject_no_hello = None
                    self.session_attempts = None
                    self.shutdow_notif_sent = None
                    self.shutdown_notif_rec = None


                class MessageOut(object):
                    """
                    MPLS LDP message sent counters to this neighbor.
                    
                    .. attribute:: address_count
                    
                    	Address message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_withdraw_count
                    
                    	Address withdraw count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_app_data_count
                    
                    	ICCP RG App Data count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_conn_count
                    
                    	ICCP RG Connect count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_disconn_count
                    
                    	ICCP RG Disconnect count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_notif_count
                    
                    	ICCP RG Notify count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_count
                    
                    	Init message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_count
                    
                    	Keepalive count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_abort_request_count
                    
                    	Label abort request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_map_count
                    
                    	Label map count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_release_count
                    
                    	Label release count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_request_count
                    
                    	Label request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_withdraw_count
                    
                    	Label withdraw count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification_count
                    
                    	Notification count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_count
                    
                    	Total count of all messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.address_count = None
                        self.address_withdraw_count = None
                        self.iccp_rg_app_data_count = None
                        self.iccp_rg_conn_count = None
                        self.iccp_rg_disconn_count = None
                        self.iccp_rg_notif_count = None
                        self.init_count = None
                        self.keep_alive_count = None
                        self.label_abort_request_count = None
                        self.label_map_count = None
                        self.label_release_count = None
                        self.label_request_count = None
                        self.label_withdraw_count = None
                        self.notification_count = None
                        self.total_count = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:stats-info/Cisco-IOS-XE-mpls-ldp:message-out'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address_count is not None:
                            return True

                        if self.address_withdraw_count is not None:
                            return True

                        if self.iccp_rg_app_data_count is not None:
                            return True

                        if self.iccp_rg_conn_count is not None:
                            return True

                        if self.iccp_rg_disconn_count is not None:
                            return True

                        if self.iccp_rg_notif_count is not None:
                            return True

                        if self.init_count is not None:
                            return True

                        if self.keep_alive_count is not None:
                            return True

                        if self.label_abort_request_count is not None:
                            return True

                        if self.label_map_count is not None:
                            return True

                        if self.label_release_count is not None:
                            return True

                        if self.label_request_count is not None:
                            return True

                        if self.label_withdraw_count is not None:
                            return True

                        if self.notification_count is not None:
                            return True

                        if self.total_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageOut']['meta_info']


                class MessageIn(object):
                    """
                    MPLS LDP message received counters from this
                    neighbor.
                    
                    .. attribute:: address_count
                    
                    	Address message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_withdraw_count
                    
                    	Address withdraw count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_app_data_count
                    
                    	ICCP RG App Data count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_conn_count
                    
                    	ICCP RG Connect count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_disconn_count
                    
                    	ICCP RG Disconnect count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iccp_rg_notif_count
                    
                    	ICCP RG Notify count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: init_count
                    
                    	Init message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_count
                    
                    	Keepalive count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_abort_request_count
                    
                    	Label abort request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_map_count
                    
                    	Label map count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_release_count
                    
                    	Label release count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_request_count
                    
                    	Label request count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_withdraw_count
                    
                    	Label withdraw count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification_count
                    
                    	Notification count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_count
                    
                    	Total count of all messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.address_count = None
                        self.address_withdraw_count = None
                        self.iccp_rg_app_data_count = None
                        self.iccp_rg_conn_count = None
                        self.iccp_rg_disconn_count = None
                        self.iccp_rg_notif_count = None
                        self.init_count = None
                        self.keep_alive_count = None
                        self.label_abort_request_count = None
                        self.label_map_count = None
                        self.label_release_count = None
                        self.label_request_count = None
                        self.label_withdraw_count = None
                        self.notification_count = None
                        self.total_count = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:stats-info/Cisco-IOS-XE-mpls-ldp:message-in'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address_count is not None:
                            return True

                        if self.address_withdraw_count is not None:
                            return True

                        if self.iccp_rg_app_data_count is not None:
                            return True

                        if self.iccp_rg_conn_count is not None:
                            return True

                        if self.iccp_rg_disconn_count is not None:
                            return True

                        if self.iccp_rg_notif_count is not None:
                            return True

                        if self.init_count is not None:
                            return True

                        if self.keep_alive_count is not None:
                            return True

                        if self.label_abort_request_count is not None:
                            return True

                        if self.label_map_count is not None:
                            return True

                        if self.label_release_count is not None:
                            return True

                        if self.label_request_count is not None:
                            return True

                        if self.label_withdraw_count is not None:
                            return True

                        if self.notification_count is not None:
                            return True

                        if self.total_count is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo.MessageIn']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:stats-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bad_ldpid is not None:
                        return True

                    if self.bad_msg_len is not None:
                        return True

                    if self.bad_pdu_len is not None:
                        return True

                    if self.bad_tlv_len is not None:
                        return True

                    if self.discon_time is not None:
                        return True

                    if self.keep_alive_exp is not None:
                        return True

                    if self.malformed_tlv_val is not None:
                        return True

                    if self.message_in is not None and self.message_in._has_data():
                        return True

                    if self.message_out is not None and self.message_out._has_data():
                        return True

                    if self.sess_rej_ad is not None:
                        return True

                    if self.sess_rej_lr is not None:
                        return True

                    if self.sess_rej_max_pdu is not None:
                        return True

                    if self.sess_reject_no_hello is not None:
                        return True

                    if self.session_attempts is not None:
                        return True

                    if self.shutdow_notif_sent is not None:
                        return True

                    if self.shutdown_notif_rec is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.StatsInfo']['meta_info']


            class Backoffs(object):
                """
                LDP Backoff Information
                
                .. attribute:: backoff_seconds
                
                	Current neighbor backoff count in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                .. attribute:: waiting_seconds
                
                	Current neighbor backoff waiting count in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.backoff_seconds = None
                    self.waiting_seconds = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:backoffs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.backoff_seconds is not None:
                        return True

                    if self.waiting_seconds is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.Backoffs']['meta_info']


            class NsrNbrDetail(object):
                """
                This is the LDP NSR state for this neighbor.
                
                .. attribute:: nbr_sess
                
                	This container holds session information about the sessions between these two neighbors
                	**type**\:   :py:class:`NbrSess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess>`
                
                .. attribute:: nsr_nbr_in_label_reqs_created
                
                	In label Request Records created
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_reqs_freed
                
                	In label Request Records freed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_withdraw_created
                
                	In label Withdraw Records created
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_in_label_withdraw_freed
                
                	In label Withdraw Records freed
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_last_sync_error
                
                	This is the last NSR sync error recieved. It indicates the last reason the sync failed even if the sync has now succeeded. This allows this information to be viewed when the state is flapping, even if the syncronization is successful at the time of the query
                	**type**\:   :py:class:`NsrPeerSyncErrIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrPeerSyncErrIdentity>`
                
                .. attribute:: nsr_nbr_last_sync_nack_reason
                
                	Last NSR sync NACK reason
                	**type**\:   :py:class:`NsrSyncNackRsnIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrSyncNackRsnIdentity>`
                
                .. attribute:: nsr_nbr_lcl_addr_withdraw_cleared
                
                	Local Address Withdraw cleared
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_lcl_addr_withdraw_set
                
                	Local Address Withdraw set
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_pend_label_req_resps
                
                	Pending Label\-Request responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_pend_label_withdraw_resps
                
                	Pending Label\-Withdraw responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_pend_lcl_addr_withdraw_acks
                
                	Pending Local Address Withdraw Acks\:
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_sync_state
                
                	NSR Sync State
                	**type**\:   :py:class:`NsrPeerSyncStateIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrPeerSyncStateIdentity>`
                
                .. attribute:: nsr_nbr_xmit_ctxt_deq
                
                	Transmit contexts dequeued
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_nbr_xmit_ctxt_enq
                
                	Transmit contexts enqueued
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: nsr_state
                
                	Non\-Stop Routing State
                	**type**\:   :py:class:`NsrStatusIdentity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.NsrStatusIdentity>`
                
                .. attribute:: path_vector_limit
                
                	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this Peer is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this Peer is enabled and the Path Vector Limit is this value
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.nbr_sess = MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess()
                    self.nbr_sess.parent = self
                    self.nsr_nbr_in_label_reqs_created = None
                    self.nsr_nbr_in_label_reqs_freed = None
                    self.nsr_nbr_in_label_withdraw_created = None
                    self.nsr_nbr_in_label_withdraw_freed = None
                    self.nsr_nbr_last_sync_error = None
                    self.nsr_nbr_last_sync_nack_reason = None
                    self.nsr_nbr_lcl_addr_withdraw_cleared = None
                    self.nsr_nbr_lcl_addr_withdraw_set = None
                    self.nsr_nbr_pend_label_req_resps = None
                    self.nsr_nbr_pend_label_withdraw_resps = None
                    self.nsr_nbr_pend_lcl_addr_withdraw_acks = None
                    self.nsr_nbr_sync_state = None
                    self.nsr_nbr_xmit_ctxt_deq = None
                    self.nsr_nbr_xmit_ctxt_enq = None
                    self.nsr_state = None
                    self.path_vector_limit = None


                class NbrSess(object):
                    """
                    This container holds session information about the
                    sessions between these two neighbors.
                    
                    .. attribute:: discon_time
                    
                    	The value of sysUpTime on the most recent occasion at which any one or more of this session's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this session of any counter32 object contained in the session\-stats table.  The initial value of this object is the value of sysUpTime when the entry was created in this table.  Also, a command generator can distinguish when a session between a given Entity and Peer goes away and a new session is established.  This value would change and thus indicate to the command generator that this is a different session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_remain
                    
                    	The keep alive hold time remaining for this session in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: keep_alive_time
                    
                    	The negotiated KeepAlive Time which represents the amount of seconds between keep alive messages.  The EntityKeepAliveHoldTimer related to this Session is the value that was proposed as the KeepAlive Time for this session.  This value is negotiated during session initialization between the entity's proposed value (i.e., the value configured in EntityKeepAliveHoldTimer) and the peer's proposed KeepAlive Hold Timer value. This value is the smaller of the two proposed values
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**units**\: seconds
                    
                    .. attribute:: last_stat_change
                    
                    	The value of sysUpTime at the time this Session entered its current state as denoted by the SessionState object
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_pdu
                    
                    	The value of maximum allowable length for LDP PDUs this session.  This value may have been negotiated for during the Session Initialization.  This object is related to the EntityMaxPduLength object.  The EntityMaxPduLength object specifies the requested LDP PDU length, and this object reflects the negotiated LDP PDU length between the Entity and the Peer
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**units**\: octets
                    
                    .. attribute:: state
                    
                    	The current state of the session, all of the states 1 to 5 are based on the state machine for session negotiation behavior
                    	**type**\:   :py:class:`StateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess.StateEnum>`
                    
                    .. attribute:: unknown_mess_err
                    
                    	This object counts the number of Unknown Message Type Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_tlv
                    
                    	This object counts the number of Unknown TLV Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of discon\-time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.discon_time = None
                        self.keep_alive_remain = None
                        self.keep_alive_time = None
                        self.last_stat_change = None
                        self.max_pdu = None
                        self.state = None
                        self.unknown_mess_err = None
                        self.unknown_tlv = None

                    class StateEnum(Enum):
                        """
                        StateEnum

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

                        nonexistent = 1

                        initialized = 2

                        openrec = 3

                        opensent = 4

                        operational = 5


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess.StateEnum']


                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:nsr-nbr-detail/Cisco-IOS-XE-mpls-ldp:nbr-sess'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.discon_time is not None:
                            return True

                        if self.keep_alive_remain is not None:
                            return True

                        if self.keep_alive_time is not None:
                            return True

                        if self.last_stat_change is not None:
                            return True

                        if self.max_pdu is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.unknown_mess_err is not None:
                            return True

                        if self.unknown_tlv is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail.NbrSess']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors/Cisco-IOS-XE-mpls-ldp:nsr-nbr-detail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.nbr_sess is not None and self.nbr_sess._has_data():
                        return True

                    if self.nsr_nbr_in_label_reqs_created is not None:
                        return True

                    if self.nsr_nbr_in_label_reqs_freed is not None:
                        return True

                    if self.nsr_nbr_in_label_withdraw_created is not None:
                        return True

                    if self.nsr_nbr_in_label_withdraw_freed is not None:
                        return True

                    if self.nsr_nbr_last_sync_error is not None:
                        return True

                    if self.nsr_nbr_last_sync_nack_reason is not None:
                        return True

                    if self.nsr_nbr_lcl_addr_withdraw_cleared is not None:
                        return True

                    if self.nsr_nbr_lcl_addr_withdraw_set is not None:
                        return True

                    if self.nsr_nbr_pend_label_req_resps is not None:
                        return True

                    if self.nsr_nbr_pend_label_withdraw_resps is not None:
                        return True

                    if self.nsr_nbr_pend_lcl_addr_withdraw_acks is not None:
                        return True

                    if self.nsr_nbr_sync_state is not None:
                        return True

                    if self.nsr_nbr_xmit_ctxt_deq is not None:
                        return True

                    if self.nsr_nbr_xmit_ctxt_enq is not None:
                        return True

                    if self.nsr_state is not None:
                        return True

                    if self.path_vector_limit is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.Neighbors.NsrNbrDetail']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:neighbors'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.backoffs is not None and self.backoffs._has_data():
                    return True

                if self.nbr_adjs is not None:
                    for child_ref in self.nbr_adjs:
                        if child_ref._has_data():
                            return True

                if self.neighbor is not None:
                    for child_ref in self.neighbor:
                        if child_ref._has_data():
                            return True

                if self.nsr_nbr_detail is not None and self.nsr_nbr_detail._has_data():
                    return True

                if self.stats_info is not None and self.stats_info._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.Neighbors']['meta_info']


        class LabelRanges(object):
            """
            This contaions holds all the label ranges in use
            by this LDP instance.
            
            .. attribute:: label_range
            
            	This entry contains a single range of labels represented by the configured Upper and Lower Bounds pairs.  NOTE\: there is NO corresponding LDP message which relates to the information in this table, however, this table does provide a way for a user to 'reserve' a generic label range.  NOTE\:  The ranges for a specific LDP Entity are UNIQUE and non\-overlapping
            	**type**\: list of    :py:class:`LabelRange <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpState.LabelRanges.LabelRange>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.label_range = YList()
                self.label_range.parent = self
                self.label_range.name = 'label_range'


            class LabelRange(object):
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
                
                .. attribute:: lr_min  <key>
                
                	The minimum label configured for this range
                	**type**\:  int
                
                	**range:** 0..1048575
                
                .. attribute:: lr_max  <key>
                
                	The maximum label configured for this range
                	**type**\:  int
                
                	**range:** 0..1048575
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.lr_min = None
                    self.lr_max = None

                @property
                def _common_path(self):
                    if self.lr_min is None:
                        raise YPYModelError('Key property lr_min is None')
                    if self.lr_max is None:
                        raise YPYModelError('Key property lr_max is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:label-ranges/Cisco-IOS-XE-mpls-ldp:label-range[Cisco-IOS-XE-mpls-ldp:lr-min = ' + str(self.lr_min) + '][Cisco-IOS-XE-mpls-ldp:lr-max = ' + str(self.lr_max) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.lr_min is not None:
                        return True

                    if self.lr_max is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpState.LabelRanges.LabelRange']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state/Cisco-IOS-XE-mpls-ldp:label-ranges'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.label_range is not None:
                    for child_ref in self.label_range:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpState.LabelRanges']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-state'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.backoff_parameters is not None and self.backoff_parameters._has_data():
                return True

            if self.bindings is not None and self.bindings._has_data():
                return True

            if self.bindings_summary is not None and self.bindings_summary._has_data():
                return True

            if self.capabilities is not None and self.capabilities._has_data():
                return True

            if self.discovery is not None and self.discovery._has_data():
                return True

            if self.forwarding is not None and self.forwarding._has_data():
                return True

            if self.forwarding_summary is not None and self.forwarding_summary._has_data():
                return True

            if self.graceful_restart is not None and self.graceful_restart._has_data():
                return True

            if self.icpm_summary_all is not None and self.icpm_summary_all._has_data():
                return True

            if self.label_ranges is not None and self.label_ranges._has_data():
                return True

            if self.neighbors is not None and self.neighbors._has_data():
                return True

            if self.nsr_summary_all is not None and self.nsr_summary_all._has_data():
                return True

            if self.oper_summary is not None and self.oper_summary._has_data():
                return True

            if self.parameters is not None and self.parameters._has_data():
                return True

            if self.vrfs is not None and self.vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['MplsLdp.MplsLdpState']['meta_info']


    class MplsLdpConfig(object):
        """
        MPLS LDP Configuration.
        
        .. attribute:: discovery
        
        	LDP discovery
        	**type**\:   :py:class:`Discovery <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery>`
        
        .. attribute:: dual_stack
        
        	This container holds the configuration of dual IPv4 and IPv6 stack peers
        	**type**\:   :py:class:`DualStack <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.DualStack>`
        
        .. attribute:: global_cfg
        
        	This contains hold all MPLS LDP Configuration with Global scope. These values affect the entire LSR unless overiddden by a parameter with a more localized scope
        	**type**\:   :py:class:`GlobalCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg>`
        
        .. attribute:: graceful_restart
        
        	Configure LDP Graceful Restart
        	**type**\:   :py:class:`GracefulRestart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GracefulRestart>`
        
        .. attribute:: interfaces
        
        	MPLS LDP Interface configuration commands
        	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces>`
        
        .. attribute:: label_cfg
        
        	This container holds the label allocation and advertisement configuration for the LDP Label Information Base. These control what prefixes may be allocated and advertised to peers
        	**type**\:   :py:class:`LabelCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.LabelCfg>`
        
        .. attribute:: logging
        
        	Enable LDP logging
        	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging>`
        
        .. attribute:: nbr_table
        
        	This container holds the list of neighbor configuration parameters
        	**type**\:   :py:class:`NbrTable <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable>`
        
        .. attribute:: passwords
        
        	This holds the MPLS LDP password configuration for use with LDP neighbors
        	**type**\:   :py:class:`Passwords <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Passwords>`
        
        .. attribute:: routing
        
        	This containter provides the MPLS LDP config for routing protocols from which it can obtain addresses to associate with labels
        	**type**\:   :py:class:`Routing <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Routing>`
        
        .. attribute:: session
        
        	Configure session parameters
        	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Session>`
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.discovery = MplsLdp.MplsLdpConfig.Discovery()
            self.discovery.parent = self
            self.dual_stack = MplsLdp.MplsLdpConfig.DualStack()
            self.dual_stack.parent = self
            self.global_cfg = MplsLdp.MplsLdpConfig.GlobalCfg()
            self.global_cfg.parent = self
            self.graceful_restart = MplsLdp.MplsLdpConfig.GracefulRestart()
            self.graceful_restart.parent = self
            self.interfaces = MplsLdp.MplsLdpConfig.Interfaces()
            self.interfaces.parent = self
            self.label_cfg = MplsLdp.MplsLdpConfig.LabelCfg()
            self.label_cfg.parent = self
            self.logging = MplsLdp.MplsLdpConfig.Logging()
            self.logging.parent = self
            self.nbr_table = MplsLdp.MplsLdpConfig.NbrTable()
            self.nbr_table.parent = self
            self.passwords = MplsLdp.MplsLdpConfig.Passwords()
            self.passwords.parent = self
            self.routing = MplsLdp.MplsLdpConfig.Routing()
            self.routing.parent = self
            self.session = MplsLdp.MplsLdpConfig.Session()
            self.session.parent = self


        class GlobalCfg(object):
            """
            This contains hold all MPLS LDP Configuration with Global
            scope. These values affect the entire LSR unless
            overiddden by a parameter with a more localized scope.
            
            .. attribute:: admin_status
            
            	This leaf controls the administrative status of LDP for this LSR. If set to disable, then all LDP activity will be disabled and all LDP sessions with peers will terminate. The LDP configuration will remain intact.  When the admin status is set back to 'enable', then LDP will resume operations and attempt to establish new sessions with the peers
            	**type**\:   :py:class:`AdminStatusEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.AdminStatusEnum>`
            
            .. attribute:: dcsp_val
            
            	This sets the 6\-bit Differentiated Services Code Point (DSCP) value in the TCP packets for LDP messages being sent from the LSR
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: disable_delay
            
            	This choice causes IGP sync up immediately upon session up
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: disable_delay_proc
            
            	This choice causes IGP sync up immediately upon session up
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: disable_quick_start
            
            	When set to true, disable LDP discovery's quick start mode for this LSR
            	**type**\:  bool
            
            .. attribute:: enable_nsr
            
            	This leaf controls whether Non\-Stop\-Routing should be enabled to include MPLS LDP
            	**type**\:  bool
            
            .. attribute:: high_priority
            
            	This sets the priority within the LSR for TCP packets for LDP messages being sent from the LSR. They are given a higher transmission priorty and will avoid being queued behind lower priority messages
            	**type**\:  bool
            
            .. attribute:: init_sess_thresh
            
            	When attempting to establish a session with a given Peer, the given LDP Entity should send out the YANG notification, 'init\-sess\-thresh\-ex', when the number of Session Initialization messages sent exceeds this threshold.  The notification is used to notify an operator when this Entity and its Peer are possibly engaged in an endless sequence of messages as each NAKs the other's  Initialization messages with Error Notification messages.  Setting this threshold which triggers the notification is one way to notify the operator.  The notification should be generated each time this threshold is exceeded and for every subsequent Initialization message which is NAK'd with an Error Notification message after this threshold is exceeded.  A value of 0 (zero) for this object indicates that the threshold is infinity, thus the YANG notification will never be generated
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: loop_detection
            
            	This leaf enables or disables Loop Detection globally for the LSR
            	**type**\:  bool
            
            .. attribute:: per_af
            
            	This container holds the global per address family configuration
            	**type**\:   :py:class:`PerAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.PerAf>`
            
            .. attribute:: protocol
            
            	This leaf defines the protocol to be used. The default is LDP
            	**type**\:   :py:class:`ProtocolEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.ProtocolEnum>`
            
            .. attribute:: router_id
            
            	Configuration for LDP Router ID (LDP ID)
            	**type**\: list of    :py:class:`RouterId <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.RouterId>`
            
            .. attribute:: seconds
            
            	Time in seconds to delay IGP sync after session comes up
            	**type**\:  int
            
            	**range:** 5..300
            
            	**units**\: second
            
            .. attribute:: seconds_delay_proc
            
            	Time in seconds to delay IGP sync after session comes up
            	**type**\:  int
            
            	**range:** 5..300
            
            	**units**\: second
            
            .. attribute:: session
            
            	Configure session parameters. Session parameters effect the session between LDP peers once the session has been established
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Session>`
            
            .. attribute:: shutdown
            
            	Writing this leaf tears down all LDP sessions, withdraws all outgoing labels from the forwarding plane, and frees all local labels that have been allocated
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.admin_status = None
                self.dcsp_val = None
                self.disable_delay = None
                self.disable_delay_proc = None
                self.disable_quick_start = None
                self.enable_nsr = None
                self.high_priority = None
                self.init_sess_thresh = None
                self.loop_detection = None
                self.per_af = MplsLdp.MplsLdpConfig.GlobalCfg.PerAf()
                self.per_af.parent = self
                self.protocol = None
                self.router_id = YList()
                self.router_id.parent = self
                self.router_id.name = 'router_id'
                self.seconds = None
                self.seconds_delay_proc = None
                self.session = MplsLdp.MplsLdpConfig.GlobalCfg.Session()
                self.session.parent = self
                self.shutdown = None

            class AdminStatusEnum(Enum):
                """
                AdminStatusEnum

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

                enable = 1

                disable = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.AdminStatusEnum']


            class ProtocolEnum(Enum):
                """
                ProtocolEnum

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

                ldp = 1

                tdp = 2

                both = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.ProtocolEnum']



            class RouterId(object):
                """
                Configuration for LDP Router ID (LDP ID)
                
                .. attribute:: vrf_name  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: force
                
                	Force the router to use the specified identifier as the router ID more quickly
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: lsr_id_if
                
                	This defines the interface to use for the LDP LSR identifier address for all sessions. The IP address of this interface will be used as the identifier
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: lsr_id_ip
                
                	This is the IP address to be used as the LDP LSR ID for all sessions
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.force = None
                    self.lsr_id_if = None
                    self.lsr_id_ip = None

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg/Cisco-IOS-XE-mpls-ldp:router-id[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.force is not None:
                        return True

                    if self.lsr_id_if is not None:
                        return True

                    if self.lsr_id_ip is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.RouterId']['meta_info']


            class Session(object):
                """
                Configure session parameters. Session parameters effect
                the session between LDP peers once the session has been
                established.
                
                .. attribute:: backoff_init
                
                	Initial session backoff time (seconds). The LDP backoff mechanism prevents two incompatibly configured label switch routers (LSRs) from engaging in an unthrottled sequence of session setup failures.  For example, an incompatibility arises when two neighboring routers attempt to perform LC\-ATM (label\-controlled ATM) but the two are using different ranges of VPI/VCI values for labels.  If a session setup attempt fails due to an incompatibility, each LSR delays its next attempt (that is, backs off), increasing the delay exponentially with each successive failure until the maximum backoff delay is reached.  The default settings correspond to the lowest settings for initial and maximum backoff values defined by the LDP protocol specification. You should change the settings from the default values only if such settings result in undesirable behavior
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 15
                
                .. attribute:: backoff_max
                
                	The maximum session backoff time (seconds) The LDP backoff mechanism prevents two incompatibly configured label switch routers (LSRs) from engaging in an unthrottled sequence of session setup failures.  For example, an incompatibility arises when two neighboring routers attempt to perform LC\-ATM (label\-controlled ATM) but the two are using different ranges of VPI/VCI values for labels.  If a session setup attempt fails due to an incompatibility, each LSR delays its next attempt (that is, backs off), increasing the delay exponentially with each successive failure until the maximum backoff delay is reached.  The default settings correspond to the lowest settings for initial and maximum backoff values defined by the LDP protocol specification. You should change the settings from the default values only if such settings result in undesirable behavior
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: seconds
                
                	**default value**\: 15
                
                .. attribute:: downstream_on_demand
                
                	This container holds config for Downstream on Demand. For it to be enabled, the Downstream on demand feature has to be configured on both peers of the session. If only one peer in the session has downstream\-on\-demand feature configured, then the session does not use downstream\-on\-demand mode. If, after, a label request is sent, and no remote label is received from the peer, the router will periodically resend the label request. After the peer advertises a label after receiving the label request, it will automatically readvertise the label if any label attribute changes subsequently
                	**type**\: list of    :py:class:`DownstreamOnDemand <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand>`
                
                .. attribute:: infinite
                
                	If set to true, the session is held indefinitely in the absence of LDP messages from the peer
                	**type**\:  bool
                
                .. attribute:: protection
                
                	Configure Session Protection parameters
                	**type**\:   :py:class:`Protection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection>`
                
                .. attribute:: seconds
                
                	Number from 15 to 2147483, that defines the time, in seconds, an LDP session is maintained in the absence of LDP messages from the session peer
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.backoff_init = None
                    self.backoff_max = None
                    self.downstream_on_demand = YList()
                    self.downstream_on_demand.parent = self
                    self.downstream_on_demand.name = 'downstream_on_demand'
                    self.infinite = None
                    self.protection = MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection()
                    self.protection.parent = self
                    self.seconds = None


                class DownstreamOnDemand(object):
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
                    
                    .. attribute:: vrf_name  <key>
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\:  str
                    
                    .. attribute:: enabled
                    
                    	Enable Downstream on Demand for this LSR. In this mode a label is not advertised to a peer, unless the peer explicitly requests it. At the same time, since the peer does not automatically advertise labels, the label request is sent whenever the next\-hop points out to a peer that no remote label has been assigned
                    	**type**\:  bool
                    
                    .. attribute:: filter
                    
                    	This filter contains a list of peer IDs that are configured for downstream\-on\-demand mode. When the filter is changed or configured, the list of established neighbors is traversed. If a session's downstream\-on\-demand configuration has changed, the session is reset in order that the new down\-stream\-on\-demand mode can be configured. The reason for resetting the session is to ensure that the labels are properly advertised between the peers. When a new session is established, the ACL is verified to determine whether the session should negotiate for downstream\-on\-demand mode. If the filter string is configured and the corresponding filter does not exist or is empty, then downstream\-on\-demand mode is not configured for any neighbor. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.enabled = None
                        self.filter = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg/Cisco-IOS-XE-mpls-ldp:session/Cisco-IOS-XE-mpls-ldp:downstream-on-demand[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.enabled is not None:
                            return True

                        if self.filter is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session.DownstreamOnDemand']['meta_info']


                class Protection(object):
                    """
                    Configure Session Protection parameters
                    
                    .. attribute:: enable_prot
                    
                    	This is set true to enable session protection
                    	**type**\:  bool
                    
                    .. attribute:: inf
                    
                    	This sessiom holdup duration is infinite
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: peer_filter
                    
                    	This is an optional filter to restrict session protection. If the string is null or unconfigured then session protection applied to all peers. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\:  str
                    
                    .. attribute:: seconds
                    
                    	This is the sessiom holdup duration in seconds
                    	**type**\:  int
                    
                    	**range:** 30..2147483
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.enable_prot = None
                        self.inf = None
                        self.peer_filter = None
                        self.seconds = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg/Cisco-IOS-XE-mpls-ldp:session/Cisco-IOS-XE-mpls-ldp:protection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable_prot is not None:
                            return True

                        if self.inf is not None:
                            return True

                        if self.peer_filter is not None:
                            return True

                        if self.seconds is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session.Protection']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg/Cisco-IOS-XE-mpls-ldp:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.backoff_init is not None:
                        return True

                    if self.backoff_max is not None:
                        return True

                    if self.downstream_on_demand is not None:
                        for child_ref in self.downstream_on_demand:
                            if child_ref._has_data():
                                return True

                    if self.infinite is not None:
                        return True

                    if self.protection is not None and self.protection._has_data():
                        return True

                    if self.seconds is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.Session']['meta_info']


            class PerAf(object):
                """
                This container holds the global per address family
                configuration.
                
                .. attribute:: af_cfg
                
                	This container holds the global per address family configuration
                	**type**\: list of    :py:class:`AfCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.af_cfg = YList()
                    self.af_cfg.parent = self
                    self.af_cfg.name = 'af_cfg'


                class AfCfg(object):
                    """
                    This container holds the global per address family
                    configuration.
                    
                    .. attribute:: vrf_name  <key>
                    
                    	This contains the VRF Name, where 'default' is used for the default vrf
                    	**type**\:  str
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                    
                    .. attribute:: default_route
                    
                    	When set true, this enables MPLS forwarding for the ip default route
                    	**type**\:  bool
                    
                    .. attribute:: implicit
                    
                    	Do not advertise an explicit address in LDP discovery hello messages or advertise a default address. Use the default address for LDP transport
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface
                    
                    	Advertise this interface's address as the explicit address in LDP discovery hello messages and use it for LDP transport
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: ipaddr
                    
                    	Advertise this address as the explicit address in LDP discovery hello messages and use it for LDP transport
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.vrf_name = None
                        self.af_name = None
                        self.default_route = None
                        self.implicit = None
                        self.interface = None
                        self.ipaddr = None

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')
                        if self.af_name is None:
                            raise YPYModelError('Key property af_name is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg/Cisco-IOS-XE-mpls-ldp:per-af/Cisco-IOS-XE-mpls-ldp:af-cfg[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:af-name = ' + str(self.af_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.default_route is not None:
                            return True

                        if self.implicit is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.ipaddr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.PerAf.AfCfg']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg/Cisco-IOS-XE-mpls-ldp:per-af'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af_cfg is not None:
                        for child_ref in self.af_cfg:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg.PerAf']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:global-cfg'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.admin_status is not None:
                    return True

                if self.dcsp_val is not None:
                    return True

                if self.disable_delay is not None:
                    return True

                if self.disable_delay_proc is not None:
                    return True

                if self.disable_quick_start is not None:
                    return True

                if self.enable_nsr is not None:
                    return True

                if self.high_priority is not None:
                    return True

                if self.init_sess_thresh is not None:
                    return True

                if self.loop_detection is not None:
                    return True

                if self.per_af is not None and self.per_af._has_data():
                    return True

                if self.protocol is not None:
                    return True

                if self.router_id is not None:
                    for child_ref in self.router_id:
                        if child_ref._has_data():
                            return True

                if self.seconds is not None:
                    return True

                if self.seconds_delay_proc is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.shutdown is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.GlobalCfg']['meta_info']


        class NbrTable(object):
            """
            This container holds the list of neighbor configuration
            parameters.
            
            .. attribute:: nbr_cfg
            
            	This entry holds the configuration of a single neighbor identified by the IP address of that neighbor
            	**type**\: list of    :py:class:`NbrCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable.NbrCfg>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.nbr_cfg = YList()
                self.nbr_cfg.parent = self
                self.nbr_cfg.name = 'nbr_cfg'


            class NbrCfg(object):
                """
                This entry holds the configuration of a single neighbor
                identified by the IP address of that neighbor.
                
                .. attribute:: nbr_vrf  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: nbr_ip  <key>
                
                	The IP address for the LDP neighbor. This may be IPv4 or IPv6
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: admin_status
                
                	The administrative status of this neighbor. If this object is changed from 'enable' to 'disable' and this entity has already attempted to establish contact with a neighbor, a 'tear\-down' for that session is issued and the session and all information related to that session ceases to exist).  When the admin status is set back to 'enable', then this Entity will attempt to establish a new session with the neighbor
                	**type**\:   :py:class:`AdminStatusEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.AdminStatusEnum>`
                
                .. attribute:: implicit_withdraw
                
                	Enable LDP implicit withdraw label for this peer
                	**type**\:  bool
                
                .. attribute:: label_binding_filter
                
                	Accept only labels matching this filter. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                .. attribute:: label_protocol
                
                	This leaf defines the protocol to be used. The default is LDP
                	**type**\:   :py:class:`LabelProtocolEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.LabelProtocolEnum>`
                
                .. attribute:: password
                
                	Enables password authentication and stores the password using a cryptographic hash
                	**type**\:  str
                
                .. attribute:: targeted
                
                	Establish or delete a targeted session
                	**type**\:  bool
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.nbr_vrf = None
                    self.nbr_ip = None
                    self.admin_status = None
                    self.implicit_withdraw = None
                    self.label_binding_filter = None
                    self.label_protocol = None
                    self.password = None
                    self.targeted = None

                class AdminStatusEnum(Enum):
                    """
                    AdminStatusEnum

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

                    enable = 1

                    disable = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.AdminStatusEnum']


                class LabelProtocolEnum(Enum):
                    """
                    LabelProtocolEnum

                    This leaf defines the protocol to be used. The default

                    is LDP.

                    .. data:: ldp = 1

                    	This LSR should use the LDP tagging protocol.

                    .. data:: tdp = 2

                    	This LSR should use the TDP tagging protocol.

                    """

                    ldp = 1

                    tdp = 2


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.NbrTable.NbrCfg.LabelProtocolEnum']


                @property
                def _common_path(self):
                    if self.nbr_vrf is None:
                        raise YPYModelError('Key property nbr_vrf is None')
                    if self.nbr_ip is None:
                        raise YPYModelError('Key property nbr_ip is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:nbr-table/Cisco-IOS-XE-mpls-ldp:nbr-cfg[Cisco-IOS-XE-mpls-ldp:nbr-vrf = ' + str(self.nbr_vrf) + '][Cisco-IOS-XE-mpls-ldp:nbr-ip = ' + str(self.nbr_ip) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nbr_vrf is not None:
                        return True

                    if self.nbr_ip is not None:
                        return True

                    if self.admin_status is not None:
                        return True

                    if self.implicit_withdraw is not None:
                        return True

                    if self.label_binding_filter is not None:
                        return True

                    if self.label_protocol is not None:
                        return True

                    if self.password is not None:
                        return True

                    if self.targeted is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.NbrTable.NbrCfg']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:nbr-table'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.nbr_cfg is not None:
                    for child_ref in self.nbr_cfg:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.NbrTable']['meta_info']


        class Passwords(object):
            """
            This holds the MPLS LDP password configuration for use
            with LDP neighbors.
            
            .. attribute:: password
            
            	This holds the MPLS LDP password configuration for use with a single LDP neighbor or group of LDP neighbors
            	**type**\: list of    :py:class:`Password <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Passwords.Password>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.password = YList()
                self.password.parent = self
                self.password.name = 'password'


            class Password(object):
                """
                This holds the MPLS LDP password configuration for use
                with a single LDP neighbor or group of LDP neighbors.
                
                .. attribute:: nbr_vrf  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: nbr_id  <key>
                
                	This leaf holds the neighbor id for this password. This id may be an lsr\-id, an ip\-address, or a filter describing a group of neighbors
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                
                ----
                	**type**\:  str
                
                
                ----
                .. attribute:: password_num  <key>
                
                	This is a user\-assigned unique number identifying a password for this neighbor or group of neighbors. Multiple passwords may be assigned to a neighbor. If that is the case, each password is tried starting with the lowest number to the highest until a passsword matches or the list is exhausted
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: clear_pass
                
                	This is a clear\-text (non\-encrypted password to be used with the neighbor
                	**type**\:  str
                
                .. attribute:: encrypt_pass
                
                	This is an encrypted password to be used with the neighbor
                	**type**\:  str
                
                .. attribute:: keychain_pass
                
                	This is a keychain identifier, which identifies an separately configured keychain to be used with the neighbor neighbor
                	**type**\:  str
                
                .. attribute:: pass_required
                
                	This leaf is set true if the password is required and false if the password is not required
                	**type**\:  bool
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.nbr_vrf = None
                    self.nbr_id = None
                    self.password_num = None
                    self.clear_pass = None
                    self.encrypt_pass = None
                    self.keychain_pass = None
                    self.pass_required = None

                @property
                def _common_path(self):
                    if self.nbr_vrf is None:
                        raise YPYModelError('Key property nbr_vrf is None')
                    if self.nbr_id is None:
                        raise YPYModelError('Key property nbr_id is None')
                    if self.password_num is None:
                        raise YPYModelError('Key property password_num is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:passwords/Cisco-IOS-XE-mpls-ldp:password[Cisco-IOS-XE-mpls-ldp:nbr-vrf = ' + str(self.nbr_vrf) + '][Cisco-IOS-XE-mpls-ldp:nbr-id = ' + str(self.nbr_id) + '][Cisco-IOS-XE-mpls-ldp:password-num = ' + str(self.password_num) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nbr_vrf is not None:
                        return True

                    if self.nbr_id is not None:
                        return True

                    if self.password_num is not None:
                        return True

                    if self.clear_pass is not None:
                        return True

                    if self.encrypt_pass is not None:
                        return True

                    if self.keychain_pass is not None:
                        return True

                    if self.pass_required is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Passwords.Password']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:passwords'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.password is not None:
                    for child_ref in self.password:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.Passwords']['meta_info']


        class Session(object):
            """
            Configure session parameters
            
            .. attribute:: backoff
            
            	Initial session backoff time (seconds)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**default value**\: 15
            
            .. attribute:: infinite
            
            	Ignore LDP session holdtime
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: seconds
            
            	Session holdtime in seconds
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.backoff = None
                self.infinite = None
                self.seconds = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:session'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.backoff is not None:
                    return True

                if self.infinite is not None:
                    return True

                if self.seconds is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.Session']['meta_info']


        class LabelCfg(object):
            """
            This container holds the label allocation and
            advertisement configuration for the LDP Label Information
            Base. These control what prefixes may be allocated and
            advertised to peers.
            
            .. attribute:: label_af_cfg
            
            	This is an allocation filter and advertisement filters for LDP labels in this address family
            	**type**\: list of    :py:class:`LabelAfCfg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.label_af_cfg = YList()
                self.label_af_cfg.parent = self
                self.label_af_cfg.name = 'label_af_cfg'


            class LabelAfCfg(object):
                """
                This is an allocation filter and advertisement filters
                for LDP labels in this address family.
                
                .. attribute:: vrf_name  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: af_name  <key>
                
                	Address Family name
                	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                
                .. attribute:: advt_filter
                
                	MPLS LDP Label advertisement filter restrictions
                	**type**\: list of    :py:class:`AdvtFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter>`
                
                .. attribute:: host_route_enable
                
                	True if this LSR should allocate host\-routes only
                	**type**\:  bool
                
                .. attribute:: prefix_filter
                
                	This contains the filter name for this label's prefix. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None
                    self.af_name = None
                    self.advt_filter = YList()
                    self.advt_filter.parent = self
                    self.advt_filter.name = 'advt_filter'
                    self.host_route_enable = None
                    self.prefix_filter = None


                class AdvtFilter(object):
                    """
                    MPLS LDP Label advertisement filter restrictions.
                    
                    .. attribute:: prefix_filter  <key>
                    
                    	This contains the filter name for this label's prefix.  The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: peer_filter  <key>
                    
                    	This contains the filter name for this label's Peer. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\:  str
                    
                    	**length:** 0..64
                    
                    .. attribute:: interface  <key>
                    
                    	This is an optional interface that may be used to restrict the scope of the label advertisement
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: adv_label_cfg
                    
                    	This leaf controls what type of label is advertised for matching prefixes to the matching peers
                    	**type**\:   :py:class:`AdvLabelTypeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AdvLabelTypeEnum>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.prefix_filter = None
                        self.peer_filter = None
                        self.interface = None
                        self.adv_label_cfg = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.prefix_filter is None:
                            raise YPYModelError('Key property prefix_filter is None')
                        if self.peer_filter is None:
                            raise YPYModelError('Key property peer_filter is None')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:advt-filter[Cisco-IOS-XE-mpls-ldp:prefix-filter = ' + str(self.prefix_filter) + '][Cisco-IOS-XE-mpls-ldp:peer-filter = ' + str(self.peer_filter) + '][Cisco-IOS-XE-mpls-ldp:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.prefix_filter is not None:
                            return True

                        if self.peer_filter is not None:
                            return True

                        if self.interface is not None:
                            return True

                        if self.adv_label_cfg is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg.AdvtFilter']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')
                    if self.af_name is None:
                        raise YPYModelError('Key property af_name is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:label-cfg/Cisco-IOS-XE-mpls-ldp:label-af-cfg[Cisco-IOS-XE-mpls-ldp:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-mpls-ldp:af-name = ' + str(self.af_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    if self.af_name is not None:
                        return True

                    if self.advt_filter is not None:
                        for child_ref in self.advt_filter:
                            if child_ref._has_data():
                                return True

                    if self.host_route_enable is not None:
                        return True

                    if self.prefix_filter is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.LabelCfg.LabelAfCfg']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:label-cfg'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.label_af_cfg is not None:
                    for child_ref in self.label_af_cfg:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.LabelCfg']['meta_info']


        class Discovery(object):
            """
            LDP discovery
            
            .. attribute:: instance_tlv
            
            	Set this leaf to true to disable transmit and receive processing for Type\-Length\-Value (TLV) in the discovery messages
            	**type**\:  bool
            
            .. attribute:: int_trans_addrs
            
            	This list contains the per\-interface transport addresses, which overide the global and default values
            	**type**\:   :py:class:`IntTransAddrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs>`
            
            .. attribute:: link_hello
            
            	This container holds the parameters for the non\-targeted link hello
            	**type**\:   :py:class:`LinkHello <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.LinkHello>`
            
            .. attribute:: targeted_hello
            
            	This container holds the parameters for the targeted link hello
            	**type**\:   :py:class:`TargetedHello <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.TargetedHello>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.instance_tlv = None
                self.int_trans_addrs = MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs()
                self.int_trans_addrs.parent = self
                self.link_hello = MplsLdp.MplsLdpConfig.Discovery.LinkHello()
                self.link_hello.parent = self
                self.targeted_hello = MplsLdp.MplsLdpConfig.Discovery.TargetedHello()
                self.targeted_hello.parent = self


            class LinkHello(object):
                """
                This container holds the parameters for the non\-targeted
                link hello.
                
                .. attribute:: holdtime
                
                	LDP discovery link hello holdtime in seconds
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: interval
                
                	LDP discovery link hello interval in seconds
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.holdtime = None
                    self.interval = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:link-hello'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.holdtime is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Discovery.LinkHello']['meta_info']


            class TargetedHello(object):
                """
                This container holds the parameters for the targeted
                link hello.
                
                .. attribute:: accept
                
                	Enables router to respond to requests for targeted hello messages
                	**type**\:   :py:class:`Accept <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept>`
                
                .. attribute:: enable
                
                	Set to true if targeted hello messages may be accepted
                	**type**\:  bool
                
                .. attribute:: holdtime
                
                	LDP discovery targeted hello holdtime in seconds
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: interval
                
                	LDP discovery targeted hello interval in seconds
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.accept = MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept()
                    self.accept.parent = self
                    self.enable = None
                    self.holdtime = None
                    self.interval = None


                class Accept(object):
                    """
                    Enables router to respond to requests for targeted
                    hello messages
                    
                    .. attribute:: enable
                    
                    	Set to true if targeted hello messages may be accepted
                    	**type**\:  bool
                    
                    .. attribute:: src_filter
                    
                    	Only respond to requests for targeted hello messages from sources matching this filter. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.src_filter = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:targeted-hello/Cisco-IOS-XE-mpls-ldp:accept'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.src_filter is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.Discovery.TargetedHello.Accept']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:targeted-hello'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.accept is not None and self.accept._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.holdtime is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Discovery.TargetedHello']['meta_info']


            class IntTransAddrs(object):
                """
                This list contains the per\-interface transport
                addresses, which overide the global and default
                values.
                
                .. attribute:: int_trans_addr
                
                	This entry contains the per\-interface transport addresses, which overide the global and default values
                	**type**\: list of    :py:class:`IntTransAddr <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.int_trans_addr = YList()
                    self.int_trans_addr.parent = self
                    self.int_trans_addr.name = 'int_trans_addr'


                class IntTransAddr(object):
                    """
                    This entry contains the per\-interface transport
                    addresses, which overide the global and default
                    values.
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                    
                    .. attribute:: int_name  <key>
                    
                    	The Interface Name
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: trans_int
                    
                    	Advertise this interface's address as the address in LDP discovery hello messages and use it for LDP transport
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: trans_ip
                    
                    	Advertise this address as the address in LDP discovery hello messages and use it for LDP transport
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.int_name = None
                        self.trans_int = None
                        self.trans_ip = None

                    @property
                    def _common_path(self):
                        if self.af_name is None:
                            raise YPYModelError('Key property af_name is None')
                        if self.int_name is None:
                            raise YPYModelError('Key property int_name is None')

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:int-trans-addrs/Cisco-IOS-XE-mpls-ldp:int-trans-addr[Cisco-IOS-XE-mpls-ldp:af-name = ' + str(self.af_name) + '][Cisco-IOS-XE-mpls-ldp:int-name = ' + str(self.int_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.int_name is not None:
                            return True

                        if self.trans_int is not None:
                            return True

                        if self.trans_ip is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs.IntTransAddr']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:discovery/Cisco-IOS-XE-mpls-ldp:int-trans-addrs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.int_trans_addr is not None:
                        for child_ref in self.int_trans_addr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Discovery.IntTransAddrs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:discovery'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.instance_tlv is not None:
                    return True

                if self.int_trans_addrs is not None and self.int_trans_addrs._has_data():
                    return True

                if self.link_hello is not None and self.link_hello._has_data():
                    return True

                if self.targeted_hello is not None and self.targeted_hello._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.Discovery']['meta_info']


        class GracefulRestart(object):
            """
            Configure LDP Graceful Restart
            
            .. attribute:: forwarding_holding
            
            	Specifies the amount of time the MPLS LDP forwarding state must be preserved after the control plane restarts
            	**type**\:  int
            
            	**range:** 5..300
            
            	**units**\: seconds
            
            .. attribute:: helper
            
            	This contains the filter name for peers for which this LSR will act as a graceful\-restart helper
            	**type**\: list of    :py:class:`Helper <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.GracefulRestart.Helper>`
            
            .. attribute:: is_graceful_restartable
            
            	Enable graceful restartable
            	**type**\:  bool
            
            .. attribute:: max_recovery
            
            	Amount of time (in seconds) that the router should hold stale label\-FEC bindings after an LDP session has been reestablished
            	**type**\:  int
            
            	**range:** 5..300
            
            	**units**\: seconds
            
            .. attribute:: nbr_liveness
            
            	Amount of time (in seconds) that the router must wait for an LDP session to be reestablished
            	**type**\:  int
            
            	**range:** 5..300
            
            	**units**\: seconds
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.forwarding_holding = None
                self.helper = YList()
                self.helper.parent = self
                self.helper.name = 'helper'
                self.is_graceful_restartable = None
                self.max_recovery = None
                self.nbr_liveness = None


            class Helper(object):
                """
                This contains the filter name for peers for which this
                LSR will act as a graceful\-restart helper.
                
                .. attribute:: helper_vrf  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: helper_filter  <key>
                
                	This contains the filter name for peers for which this LSR will act as a graceful\-restart helper. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
                	**type**\:  str
                
                	**length:** 0..64
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.helper_vrf = None
                    self.helper_filter = None

                @property
                def _common_path(self):
                    if self.helper_vrf is None:
                        raise YPYModelError('Key property helper_vrf is None')
                    if self.helper_filter is None:
                        raise YPYModelError('Key property helper_filter is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:graceful-restart/Cisco-IOS-XE-mpls-ldp:helper[Cisco-IOS-XE-mpls-ldp:helper-vrf = ' + str(self.helper_vrf) + '][Cisco-IOS-XE-mpls-ldp:helper-filter = ' + str(self.helper_filter) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.helper_vrf is not None:
                        return True

                    if self.helper_filter is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.GracefulRestart.Helper']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:graceful-restart'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.forwarding_holding is not None:
                    return True

                if self.helper is not None:
                    for child_ref in self.helper:
                        if child_ref._has_data():
                            return True

                if self.is_graceful_restartable is not None:
                    return True

                if self.max_recovery is not None:
                    return True

                if self.nbr_liveness is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.GracefulRestart']['meta_info']


        class Logging(object):
            """
            Enable LDP logging
            
            .. attribute:: adjacency
            
            	Enable logging of adjacency messages
            	**type**\:  bool
            
            .. attribute:: graceful_restart
            
            	Enable logging of graceful\-restart messages
            	**type**\:  bool
            
            .. attribute:: neighbor
            
            	Enable logging of neighbor messages
            	**type**\:  bool
            
            .. attribute:: nsr
            
            	Enable logging of nsr messages
            	**type**\:  bool
            
            .. attribute:: password
            
            	Enable logging of password messages
            	**type**\:   :py:class:`Password <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging.Password>`
            
            .. attribute:: session_protection
            
            	Enable logging of session\-protection messages
            	**type**\:  bool
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.adjacency = None
                self.graceful_restart = None
                self.neighbor = None
                self.nsr = None
                self.password = MplsLdp.MplsLdpConfig.Logging.Password()
                self.password.parent = self
                self.session_protection = None


            class Password(object):
                """
                Enable logging of password messages.
                
                .. attribute:: config_msg
                
                	Log MPLS LDP password configuration changes
                	**type**\:   :py:class:`ConfigMsg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg>`
                
                .. attribute:: rollover_msg
                
                	Log MPLS LDP password rollover messages
                	**type**\:   :py:class:`RolloverMsg <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg>`
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.config_msg = MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg()
                    self.config_msg.parent = self
                    self.rollover_msg = MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg()
                    self.rollover_msg.parent = self


                class ConfigMsg(object):
                    """
                    Log MPLS LDP password configuration changes.
                    
                    .. attribute:: enable
                    
                    	Log MPLS LDP password configuration changes
                    	**type**\:  bool
                    
                    .. attribute:: rate_limit
                    
                    	This is the number of messages per minute to limit the logging. A value of 0 indicates no limits on the number of logged messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.rate_limit = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:logging/Cisco-IOS-XE-mpls-ldp:password/Cisco-IOS-XE-mpls-ldp:config-msg'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.rate_limit is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.Logging.Password.ConfigMsg']['meta_info']


                class RolloverMsg(object):
                    """
                    Log MPLS LDP password rollover messages.
                    
                    .. attribute:: enable
                    
                    	Log MPLS LDP password rollover messages
                    	**type**\:  bool
                    
                    .. attribute:: rate_limit
                    
                    	This is the number of messages per minute to limit the logging. A value of 0 indicates no limits on the number of logged messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.rate_limit = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:logging/Cisco-IOS-XE-mpls-ldp:password/Cisco-IOS-XE-mpls-ldp:rollover-msg'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.rate_limit is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.Logging.Password.RolloverMsg']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:logging/Cisco-IOS-XE-mpls-ldp:password'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.config_msg is not None and self.config_msg._has_data():
                        return True

                    if self.rollover_msg is not None and self.rollover_msg._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Logging.Password']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:logging'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.adjacency is not None:
                    return True

                if self.graceful_restart is not None:
                    return True

                if self.neighbor is not None:
                    return True

                if self.nsr is not None:
                    return True

                if self.password is not None and self.password._has_data():
                    return True

                if self.session_protection is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.Logging']['meta_info']


        class Interfaces(object):
            """
            MPLS LDP Interface configuration commands.
            
            .. attribute:: interface
            
            	MPLS LDP Interface configuration commands. Where a corresponding global configuration command exists, the interface level command will take precedence when configured
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
                """
                MPLS LDP Interface configuration commands. Where a
                corresponding global configuration command exists, the
                interface level command will take precedence when
                configured.
                
                .. attribute:: vrf  <key>
                
                	This contains the VRF Name, where 'default' is used for the default vrf
                	**type**\:  str
                
                .. attribute:: interface  <key>
                
                	The Interface Name
                	**type**\:  str
                
                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs>`
                
                .. attribute:: disable_delay
                
                	This choice causes IGP sync up immediately upon session up
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: disable_quick_start_int
                
                	When set to true, disable LDP discovery's quick start mode for this interface
                	**type**\:  bool
                
                .. attribute:: link_hello_hold
                
                	LDP discovery link hello holdtime in seconds for this interface. This value overides the global setting
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                	**default value**\: 15
                
                .. attribute:: link_hello_int
                
                	LDP discovery link hello interval in seconds for this interface. This value overides the global setting
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                	**default value**\: 5
                
                .. attribute:: seconds
                
                	Time in seconds to delay IGP sync after session comes up
                	**type**\:  int
                
                	**range:** 5..300
                
                	**units**\: second
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.vrf = None
                    self.interface = None
                    self.afs = MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs()
                    self.afs.parent = self
                    self.disable_delay = None
                    self.disable_quick_start_int = None
                    self.link_hello_hold = None
                    self.link_hello_int = None
                    self.seconds = None


                class Afs(object):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	MPLS LDP Operational data for this Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.af = YList()
                        self.af.parent = self
                        self.af.name = 'af'


                    class Af(object):
                        """
                        MPLS LDP Operational data for this Address Family.
                        
                        .. attribute:: af_name  <key>
                        
                        	Address Family name
                        	**type**\:   :py:class:`AfEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.AfEnum>`
                        
                        .. attribute:: autoconfig_disable
                        
                        	True if LDP autoconfig is explicitly disabled on this interface
                        	**type**\:  bool
                        
                        .. attribute:: bgp_redist
                        
                        	MPLS LDP configuration for protocol redistribution. By default, redistribution of BGP routes is disabled. It can be enabled for all BGP routes or for a specific AS. Also it can be redistributed to all LDP peers or to a filtered group of peers
                        	**type**\:   :py:class:`BgpRedist <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist>`
                        
                        .. attribute:: enable
                        
                        	This is set true to enable LDP on this interface
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'mpls-ldp-ios-xe-oper'
                        _revision = '2017-02-07'

                        def __init__(self):
                            self.parent = None
                            self.af_name = None
                            self.autoconfig_disable = None
                            self.bgp_redist = MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist()
                            self.bgp_redist.parent = self
                            self.enable = None


                        class BgpRedist(object):
                            """
                            MPLS LDP configuration for protocol
                            redistribution. By default, redistribution of BGP
                            routes is disabled. It can be enabled for all
                            BGP routes or for a specific AS. Also it can be
                            redistributed to all LDP peers or to a filtered
                            group of peers.
                            
                            .. attribute:: advertise_to
                            
                            	Filter of neighbors to receive BGP route redistributions from LDP. If the list is empty or unset, all LDP neighbors will receive redistributions
                            	**type**\:  str
                            
                            .. attribute:: as_xx
                            
                            	First half of BGP AS number in XX.YY format.  Mandatory Must be a non\-zero value if second half is zero
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: as_yy
                            
                            	Second half of BGP AS number in XX.YY format. Mandatory Must be a non\-zero value if first half is zero
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: enable
                            
                            	This is set true to allow LDP to redistribute BGP routes
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'mpls-ldp-ios-xe-oper'
                            _revision = '2017-02-07'

                            def __init__(self):
                                self.parent = None
                                self.advertise_to = None
                                self.as_xx = None
                                self.as_yy = None
                                self.enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:bgp-redist'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.advertise_to is not None:
                                    return True

                                if self.as_xx is not None:
                                    return True

                                if self.as_yy is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                                return meta._meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af.BgpRedist']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.af_name is None:
                                raise YPYModelError('Key property af_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:af[Cisco-IOS-XE-mpls-ldp:af-name = ' + str(self.af_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.autoconfig_disable is not None:
                                return True

                            if self.bgp_redist is not None and self.bgp_redist._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                            return meta._meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs.Af']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-mpls-ldp:afs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.af is not None:
                            for child_ref in self.af:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface.Afs']['meta_info']

                @property
                def _common_path(self):
                    if self.vrf is None:
                        raise YPYModelError('Key property vrf is None')
                    if self.interface is None:
                        raise YPYModelError('Key property interface is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:interfaces/Cisco-IOS-XE-mpls-ldp:interface[Cisco-IOS-XE-mpls-ldp:vrf = ' + str(self.vrf) + '][Cisco-IOS-XE-mpls-ldp:interface = ' + str(self.interface) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf is not None:
                        return True

                    if self.interface is not None:
                        return True

                    if self.afs is not None and self.afs._has_data():
                        return True

                    if self.disable_delay is not None:
                        return True

                    if self.disable_quick_start_int is not None:
                        return True

                    if self.link_hello_hold is not None:
                        return True

                    if self.link_hello_int is not None:
                        return True

                    if self.seconds is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.Interfaces']['meta_info']


        class Routing(object):
            """
            This containter provides the MPLS LDP config for routing
            protocols from which it can obtain addresses to
            associate with labels.
            
            .. attribute:: routing_inst
            
            	This entry provides the MPLS LDP config for this routing instance
            	**type**\: list of    :py:class:`RoutingInst <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Routing.RoutingInst>`
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.routing_inst = YList()
                self.routing_inst.parent = self
                self.routing_inst.name = 'routing_inst'


            class RoutingInst(object):
                """
                This entry provides the MPLS LDP config for this
                routing instance.
                
                .. attribute:: routing_inst_name  <key>
                
                	Name of the routing instance for which this MPLS LDP configuration applies
                	**type**\:  str
                
                .. attribute:: area_id
                
                	This leaf restricts the LDP Autoconfiguration feature to enable LDP on interfaces belonging to an OSPF process for a specific area. If no area is specified, then this applies to all interfaces associated with the. If an area ID is specified, then only interfaces associated with that OSPF area are automatically enabled with LDP. Any interface\-specific ldp configuration will overide this setting for that interface
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: autoconfig_enable
                
                	This leaf enables or disables LDP for all interfaces covered by this routing instance subject to the autoconfig\-scope
                	**type**\:  bool
                
                .. attribute:: level_id
                
                	This leaf restricts the LDP Autoconfiguration feature to enable LDP on interfaces belonging to an ISIS process for a specific level. If no level is specified, then this applies to all interfaces associated with the. If a level is specified, then only interfaces associated with that ISIS level are automatically enabled with LDP. Any interface\-specific ldp configuration will overide this setting for that interface
                	**type**\:   :py:class:`LevelIdEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.MplsLdp.MplsLdpConfig.Routing.RoutingInst.LevelIdEnum>`
                
                .. attribute:: sync
                
                	When set to true this enables LDP IGP synchronization. Without syncrhonization, packet loss can occur because the actions of the IGP and LDP are not synchronized
                	**type**\:  bool
                
                

                """

                _prefix = 'mpls-ldp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.routing_inst_name = None
                    self.area_id = None
                    self.autoconfig_enable = None
                    self.level_id = None
                    self.sync = None

                class LevelIdEnum(Enum):
                    """
                    LevelIdEnum

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

                    level_1 = 1

                    level_2 = 2

                    level_1_2 = 3


                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                        return meta._meta_table['MplsLdp.MplsLdpConfig.Routing.RoutingInst.LevelIdEnum']


                @property
                def _common_path(self):
                    if self.routing_inst_name is None:
                        raise YPYModelError('Key property routing_inst_name is None')

                    return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:routing/Cisco-IOS-XE-mpls-ldp:routing-inst[Cisco-IOS-XE-mpls-ldp:routing-inst-name = ' + str(self.routing_inst_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.routing_inst_name is not None:
                        return True

                    if self.area_id is not None:
                        return True

                    if self.autoconfig_enable is not None:
                        return True

                    if self.level_id is not None:
                        return True

                    if self.sync is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                    return meta._meta_table['MplsLdp.MplsLdpConfig.Routing.RoutingInst']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:routing'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.routing_inst is not None:
                    for child_ref in self.routing_inst:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.Routing']['meta_info']


        class DualStack(object):
            """
            This container holds the configuration of dual IPv4 and
            IPv6 stack peers.
            
            .. attribute:: max_wait
            
            	Wait time in seconds (0 indicates no preference)
            	**type**\:  int
            
            	**range:** 0..60
            
            .. attribute:: prefer_ipv4_peers
            
            	This contains the filter name for peers where IPv4 connections are preferred over IPv6 connections. The filter type is device specific and could be an ACL, a prefix list, or other mechanism
            	**type**\:  str
            
            

            """

            _prefix = 'mpls-ldp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.max_wait = None
                self.prefer_ipv4_peers = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config/Cisco-IOS-XE-mpls-ldp:dual-stack'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.max_wait is not None:
                    return True

                if self.prefer_ipv4_peers is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
                return meta._meta_table['MplsLdp.MplsLdpConfig.DualStack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp/Cisco-IOS-XE-mpls-ldp:mpls-ldp-config'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.discovery is not None and self.discovery._has_data():
                return True

            if self.dual_stack is not None and self.dual_stack._has_data():
                return True

            if self.global_cfg is not None and self.global_cfg._has_data():
                return True

            if self.graceful_restart is not None and self.graceful_restart._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.label_cfg is not None and self.label_cfg._has_data():
                return True

            if self.logging is not None and self.logging._has_data():
                return True

            if self.nbr_table is not None and self.nbr_table._has_data():
                return True

            if self.passwords is not None and self.passwords._has_data():
                return True

            if self.routing is not None and self.routing._has_data():
                return True

            if self.session is not None and self.session._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['MplsLdp.MplsLdpConfig']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-mpls-ldp:mpls-ldp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.mpls_ldp_config is not None and self.mpls_ldp_config._has_data():
            return True

        if self.mpls_ldp_state is not None and self.mpls_ldp_state._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['MplsLdp']['meta_info']


class ClearMsgCountersRpc(object):
    """
    This RPC clears the LDP message counters for either a single
    neighbor or for all neighbors.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearMsgCountersRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearMsgCountersRpc.Output>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.input = ClearMsgCountersRpc.Input()
        self.input.parent = self
        self.output = ClearMsgCountersRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: all
        
        	Clear information for all neighbors
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: nbr_ip
        
        	LSR ID of the neighbor
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: vrf_name
        
        	This contains the VRF Name, where 'default' is used for the default vrf
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.all = None
            self.nbr_ip = None
            self.vrf_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:clear-msg-counters/Cisco-IOS-XE-mpls-ldp:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.all is not None:
                return True

            if self.nbr_ip is not None:
                return True

            if self.vrf_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['ClearMsgCountersRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: status
        
        	Return status will be 'OK' on success or an explanation string on failure
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.status = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:clear-msg-counters/Cisco-IOS-XE-mpls-ldp:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['ClearMsgCountersRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-mpls-ldp:clear-msg-counters'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['ClearMsgCountersRpc']['meta_info']


class RestartNeighborRpc(object):
    """
    This RPC restarts a single LDP session or all LDP sessions,
    but does not restart the LDP process itself, if the device
    supports that capability.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RestartNeighborRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.RestartNeighborRpc.Output>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.input = RestartNeighborRpc.Input()
        self.input.parent = self
        self.output = RestartNeighborRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: all
        
        	Restart sessions for all neighbors
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: nbr_ip
        
        	LSR ID of the neighbor
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: vrf_name
        
        	This contains the VRF Name, where 'default' is used for the default vrf
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.all = None
            self.nbr_ip = None
            self.vrf_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:restart-neighbor/Cisco-IOS-XE-mpls-ldp:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.all is not None:
                return True

            if self.nbr_ip is not None:
                return True

            if self.vrf_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['RestartNeighborRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: status
        
        	Return status will be 'OK' on success or an explanation string on failure
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.status = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:restart-neighbor/Cisco-IOS-XE-mpls-ldp:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['RestartNeighborRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-mpls-ldp:restart-neighbor'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RestartNeighborRpc']['meta_info']


class ClearForwardingRpc(object):
    """
    This command resets LDP installed forwarding state for all
    prefixes or a given prefix. It is useful when installed 
    LDP forwarding state needs to be reprogrammed in LSD and
    MPLS forwarding.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearForwardingRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_ldp.ClearForwardingRpc.Output>`
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.input = ClearForwardingRpc.Input()
        self.input.parent = self
        self.output = ClearForwardingRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: all
        
        	This case is used to clear the forwarding entries for all prefixes
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: prefix_ip
        
        	This case provides the IP prefix for the forwarding entry whose data should be cleared
        	**type**\: one of the below types:
        
        	**type**\:  str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        
        ----
        	**type**\:  str
        
        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        
        ----
        .. attribute:: vrf_name
        
        	This contains the VRF Name, where 'default' is used for the default vrf
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.all = None
            self.prefix_ip = None
            self.vrf_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:clear-forwarding/Cisco-IOS-XE-mpls-ldp:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.all is not None:
                return True

            if self.prefix_ip is not None:
                return True

            if self.vrf_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['ClearForwardingRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: status
        
        	Return status will be 'OK' on success or an explanatory string on failure
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-ldp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.status = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-mpls-ldp:clear-forwarding/Cisco-IOS-XE-mpls-ldp:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.status is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
            return meta._meta_table['ClearForwardingRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-mpls-ldp:clear-forwarding'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['ClearForwardingRpc']['meta_info']


class NsrPeerSyncErrSyncPrepIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, synch prep.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrSyncPrepIdentity']['meta_info']


class NsrSyncNackRsnPEndSockNotSyncedIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed because the P end sock was not synced.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnPEndSockNotSyncedIdentity']['meta_info']


class LabelTypeMplsIdentity(LabelTypeIdentity):
    """
    The is an MPLS Label.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        LabelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LabelTypeMplsIdentity']['meta_info']


class RoutePathLblOwnerLdpIdentity(RoutePathLblOwnerIdentity):
    """
    Path outgoing label owned by LDP.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathLblOwnerIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathLblOwnerLdpIdentity']['meta_info']


class LabelTypeUnLabeledIdentity(LabelTypeIdentity):
    """
    This is unlabeled
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        LabelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LabelTypeUnLabeledIdentity']['meta_info']


class NsrPeerSyncErrNoneIdentity(NsrPeerSyncErrIdentity):
    """
    No error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrNoneIdentity']['meta_info']


class NsrSyncNackRsnErrRxUnexpOpenIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to an unexpected open.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrRxUnexpOpenIdentity']['meta_info']


class DownNbrReasonNaIdentity(DownNbrReasonIdentity):
    """
    Not applicable, the neighbor is up..
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        DownNbrReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['DownNbrReasonNaIdentity']['meta_info']


class DownNbrReasonDiscHelloIdentity(DownNbrReasonIdentity):
    """
    The local discovery hello timer expired..
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        DownNbrReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['DownNbrReasonDiscHelloIdentity']['meta_info']


class NsrPeerSyncErrLdpPeerIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, ldp peer
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrLdpPeerIdentity']['meta_info']


class RoutePathIpNoFlagIdentity(RoutePathTypeIdentity):
    """
    A primary path with no special flag/attribute
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathIpNoFlagIdentity']['meta_info']


class NsrPeerSyncErrTcpPeerIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, tcp peer
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrTcpPeerIdentity']['meta_info']


class LdpNsrPeerSyncStOperIdentity(NsrPeerSyncStateIdentity):
    """
    LDP NSR peer synchronization is operational.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LdpNsrPeerSyncStOperIdentity']['meta_info']


class LdpNsrPeerSyncStPrepIdentity(NsrPeerSyncStateIdentity):
    """
    LDP NSR peer synchronization is prep.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LdpNsrPeerSyncStPrepIdentity']['meta_info']


class NsrSyncNackRsnErrDhcAddIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed with a error creating the directed hello control
    infrastructure.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrDhcAddIdentity']['meta_info']


class LabelTypeUnknownIdentity(LabelTypeIdentity):
    """
    The label is unknown.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        LabelTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LabelTypeUnknownIdentity']['meta_info']


class RoutePathIpBackupRemoteIdentity(RoutePathTypeIdentity):
    """
    A non\-primary remote LFA FRR (pure) backup path
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathIpBackupRemoteIdentity']['meta_info']


class IgpSyncDownReasonNoHelloAdjIdentity(IgpSyncDownReasonIdentity):
    """
    No hello adjacency.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IgpSyncDownReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonNoHelloAdjIdentity']['meta_info']


class NsrSyncNackRsnErrAdjAddIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to an error adding the adjacency.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrAdjAddIdentity']['meta_info']


class RoutePathLblOwnerNoneIdentity(RoutePathLblOwnerIdentity):
    """
    No label and no owner.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathLblOwnerIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathLblOwnerNoneIdentity']['meta_info']


class IgpSyncDownReasonNaIdentity(IgpSyncDownReasonIdentity):
    """
    Not Applicable.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IgpSyncDownReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonNaIdentity']['meta_info']


class IgpSyncDownReasonNoPeerSessIdentity(IgpSyncDownReasonIdentity):
    """
    No peer session.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IgpSyncDownReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonNoPeerSessIdentity']['meta_info']


class RoutePathLblOwnerBgpIdentity(RoutePathLblOwnerIdentity):
    """
    Path outgoing label owned by BGP.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathLblOwnerIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathLblOwnerBgpIdentity']['meta_info']


class IgpSyncDownReasonPeerUpdateNotReceivedIdentity(IgpSyncDownReasonIdentity):
    """
    Initial update from peer not received yet.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IgpSyncDownReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonPeerUpdateNotReceivedIdentity']['meta_info']


class NsrSyncNackRsnMissingElemIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to a Missing Element.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnMissingElemIdentity']['meta_info']


class NsrSyncNackRsnNoPEndSockIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed because there was no P end socket.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnNoPEndSockIdentity']['meta_info']


class NsrSyncNackRsnNoCtxIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed with a no context error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnNoCtxIdentity']['meta_info']


class LdpNsrPeerSyncStReadyIdentity(NsrPeerSyncStateIdentity):
    """
    LDP NSR peer synchronization is ready.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LdpNsrPeerSyncStReadyIdentity']['meta_info']


class RoutePathIpBackupIdentity(RoutePathTypeIdentity):
    """
    A non\-primary local LFA FRR (pure) backup path
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathIpBackupIdentity']['meta_info']


class NsrPeerSyncErrAppFailIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, app fail
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrAppFailIdentity']['meta_info']


class NsrPeerSyncErrLdpSyncNackIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, received sync nack.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrLdpSyncNackIdentity']['meta_info']


class NsrSyncNackRsnErrAddrBindIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed to bind address.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrAddrBindIdentity']['meta_info']


class LdpNsrPeerSyncStAppWaitIdentity(NsrPeerSyncStateIdentity):
    """
    LDP NSR peer synchronization is app wait.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LdpNsrPeerSyncStAppWaitIdentity']['meta_info']


class LdpNsrPeerSyncStWaitIdentity(NsrPeerSyncStateIdentity):
    """
    LDP NSR peer synchronization is wait.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LdpNsrPeerSyncStWaitIdentity']['meta_info']


class NsrSyncNackRsnErrAppNotFoundIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to app not found.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrAppNotFoundIdentity']['meta_info']


class NsrSyncNackRsnErrRxNotifIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed with a received notification error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrRxNotifIdentity']['meta_info']


class DownNbrReasonNbrHoldIdentity(DownNbrReasonIdentity):
    """
    The neighbor sent error, hold time expired..
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        DownNbrReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['DownNbrReasonNbrHoldIdentity']['meta_info']


class NsrSyncNackRsnErrRxBadPieIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed, received a bad PIE.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrRxBadPieIdentity']['meta_info']


class NsrSyncNackRsnNoneIdentity(NsrSyncNackRsnIdentity):
    """
    None
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnNoneIdentity']['meta_info']


class NsrPeerSyncErrTcpGblIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, tcp gbl
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrTcpGblIdentity']['meta_info']


class RoutePathLblOwnerStaticIdentity(RoutePathLblOwnerIdentity):
    """
    Path outgoing label statically configured.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathLblOwnerIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathLblOwnerStaticIdentity']['meta_info']


class NsrSyncNackRsnTblIdMismatchIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed with a table ID mismatch.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnTblIdMismatchIdentity']['meta_info']


class NsrSyncNackRsnPpExistsIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed with because pp already exists.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnPpExistsIdentity']['meta_info']


class IgpSyncDownReasonInternalIdentity(IgpSyncDownReasonIdentity):
    """
    Internal reason.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IgpSyncDownReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonInternalIdentity']['meta_info']


class IccpTypeMlacpIdentity(IccpTypeIdentity):
    """
    MLACP Multi\-chassic Link Aggregation Control Protocol.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IccpTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IccpTypeMlacpIdentity']['meta_info']


class NsrSyncNackRsnEnomemIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to an out of memory error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnEnomemIdentity']['meta_info']


class IgpSyncDownReasonPeerUpdateNotDoneIdentity(IgpSyncDownReasonIdentity):
    """
    Initial update to peer not done yet.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IgpSyncDownReasonIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IgpSyncDownReasonPeerUpdateNotDoneIdentity']['meta_info']


class RoutePathIpBgpBackupIdentity(RoutePathTypeIdentity):
    """
    A non\-primary BGP backup path
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathIpBgpBackupIdentity']['meta_info']


class NsrPeerSyncErrLdpGblIdentity(NsrPeerSyncErrIdentity):
    """
    LDP Peer Sync failed, ldp gbl
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncErrIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrPeerSyncErrLdpGblIdentity']['meta_info']


class LdpNsrPeerSyncStNoneIdentity(NsrPeerSyncStateIdentity):
    """
    LDP NSR peer synchronization none.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrPeerSyncStateIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['LdpNsrPeerSyncStNoneIdentity']['meta_info']


class IcpmTypeIccpIdentity(IcpmTypeIdentity):
    """
    ICCP Interchassis Communication Protocol.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        IcpmTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['IcpmTypeIccpIdentity']['meta_info']


class NsrStatusDisabledIdentity(NsrStatusIdentity):
    """
    NSR is not enabled.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrStatusDisabledIdentity']['meta_info']


class NsrStatusReadyIdentity(NsrStatusIdentity):
    """
    Device is NSR Ready.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrStatusReadyIdentity']['meta_info']


class NsrSyncNackRsnErrPpCreateIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed creating the pp.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrPpCreateIdentity']['meta_info']


class NsrSyncNackRsnErrTpCreateIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed creating the tp.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrTpCreateIdentity']['meta_info']


class NsrSyncNackRsnErrUnexpPeerDownIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to unexpected peer down.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrUnexpPeerDownIdentity']['meta_info']


class RoutePathIpProtectedIdentity(RoutePathTypeIdentity):
    """
    A primary path with LFA FRR protection
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        RoutePathTypeIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['RoutePathIpProtectedIdentity']['meta_info']


class NsrSyncNackRsnErrAppInvalidIdentity(NsrSyncNackRsnIdentity):
    """
    NSR failed due to an app invalid error.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrSyncNackRsnIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrSyncNackRsnErrAppInvalidIdentity']['meta_info']


class NsrStatusNotReadyIdentity(NsrStatusIdentity):
    """
    Device is not NSR Ready.
    
    

    """

    _prefix = 'mpls-ldp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        NsrStatusIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_mpls_ldp as meta
        return meta._meta_table['NsrStatusNotReadyIdentity']['meta_info']


