""" Cisco_IOS_XR_ip_ntp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package operational data.

This module contains definitions
for the following management objects\:
  ntp\: NTP operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ClockUpdateNode(Enum):
    """
    ClockUpdateNode

    Mode of Clock Update

    .. data:: clk_never_updated = 0

    	 clock is never updated

    .. data:: clk_updated = 1

    	 clock is updated

    .. data:: clk_no_update_info = 2

    	 clock has no update info

    """

    clk_never_updated = Enum.YLeaf(0, "clk-never-updated")

    clk_updated = Enum.YLeaf(1, "clk-updated")

    clk_no_update_info = Enum.YLeaf(2, "clk-no-update-info")


class NtpLeap(Enum):
    """
    NtpLeap

    Type of leap

    .. data:: ntp_leap_no_warning = 0

    	Normal, no leap second warning

    .. data:: ntp_leap_addse_cond = 1

    	Last minute of day has 61 seconds

    .. data:: ntp_leap_delse_cond = 2

    	Last minute of day has 59 seconds

    .. data:: ntp_leap_not_in_sync = 3

    	Overload, clock is free running

    """

    ntp_leap_no_warning = Enum.YLeaf(0, "ntp-leap-no-warning")

    ntp_leap_addse_cond = Enum.YLeaf(1, "ntp-leap-addse-cond")

    ntp_leap_delse_cond = Enum.YLeaf(2, "ntp-leap-delse-cond")

    ntp_leap_not_in_sync = Enum.YLeaf(3, "ntp-leap-not-in-sync")


class NtpLoopFilterState(Enum):
    """
    NtpLoopFilterState

    Loop filter state

    .. data:: ntp_loop_flt_n_set = 0

    	 never set

    .. data:: ntp_loop_flt_f_set = 1

    	 drift set from file

    .. data:: ntp_loop_flt_spik = 2

    	 spike

    .. data:: ntp_loop_flt_freq = 3

    	 drift being measured

    .. data:: ntp_loop_flt_sync = 4

    	 normal controlled loop

    .. data:: ntp_loop_flt_unkn = 5

    	 unknown

    """

    ntp_loop_flt_n_set = Enum.YLeaf(0, "ntp-loop-flt-n-set")

    ntp_loop_flt_f_set = Enum.YLeaf(1, "ntp-loop-flt-f-set")

    ntp_loop_flt_spik = Enum.YLeaf(2, "ntp-loop-flt-spik")

    ntp_loop_flt_freq = Enum.YLeaf(3, "ntp-loop-flt-freq")

    ntp_loop_flt_sync = Enum.YLeaf(4, "ntp-loop-flt-sync")

    ntp_loop_flt_unkn = Enum.YLeaf(5, "ntp-loop-flt-unkn")


class NtpMode(Enum):
    """
    NtpMode

    Type of mode

    .. data:: ntp_mode_unspec = 0

    	Unspecified probably old NTP version

    .. data:: ntp_mode_symetric_active = 1

    	Symmetric active

    .. data:: ntp_mode_symetric_passive = 2

    	Symmetric passive

    .. data:: ntp_mode_client = 3

    	Client mode

    .. data:: ntp_mode_server = 4

    	Server mode

    .. data:: ntp_mode_xcast_server = 5

    	Broadcast mode

    .. data:: ntp_mode_control = 6

    	Control mode packet

    .. data:: ntp_mode_private = 7

    	Implementation defined function

    .. data:: ntp_mode_xcast_client = 8

    	A broadcast client mode

    """

    ntp_mode_unspec = Enum.YLeaf(0, "ntp-mode-unspec")

    ntp_mode_symetric_active = Enum.YLeaf(1, "ntp-mode-symetric-active")

    ntp_mode_symetric_passive = Enum.YLeaf(2, "ntp-mode-symetric-passive")

    ntp_mode_client = Enum.YLeaf(3, "ntp-mode-client")

    ntp_mode_server = Enum.YLeaf(4, "ntp-mode-server")

    ntp_mode_xcast_server = Enum.YLeaf(5, "ntp-mode-xcast-server")

    ntp_mode_control = Enum.YLeaf(6, "ntp-mode-control")

    ntp_mode_private = Enum.YLeaf(7, "ntp-mode-private")

    ntp_mode_xcast_client = Enum.YLeaf(8, "ntp-mode-xcast-client")


class NtpPeerStatus(Enum):
    """
    NtpPeerStatus

    Type of peer status

    .. data:: ntp_ctl_pst_sel_reject = 0

    	   reject

    .. data:: ntp_ctl_pst_sel_sane = 1

    	 x falsetick

    .. data:: ntp_ctl_pst_sel_correct = 2

    	 . excess 

    .. data:: ntp_ctl_pst_sel_selcand = 3

    	 - outlyer

    .. data:: ntp_ctl_pst_sel_sync_cand = 4

    	 + candidate

    .. data:: ntp_ctl_pst_sel_distsys_peer = 5

    	 # selected

    .. data:: ntp_ctl_pst_sel_sys_peer = 6

    	 * sys peer

    .. data:: ntp_ctl_pst_sel_pps = 7

    	 o pps peer

    """

    ntp_ctl_pst_sel_reject = Enum.YLeaf(0, "ntp-ctl-pst-sel-reject")

    ntp_ctl_pst_sel_sane = Enum.YLeaf(1, "ntp-ctl-pst-sel-sane")

    ntp_ctl_pst_sel_correct = Enum.YLeaf(2, "ntp-ctl-pst-sel-correct")

    ntp_ctl_pst_sel_selcand = Enum.YLeaf(3, "ntp-ctl-pst-sel-selcand")

    ntp_ctl_pst_sel_sync_cand = Enum.YLeaf(4, "ntp-ctl-pst-sel-sync-cand")

    ntp_ctl_pst_sel_distsys_peer = Enum.YLeaf(5, "ntp-ctl-pst-sel-distsys-peer")

    ntp_ctl_pst_sel_sys_peer = Enum.YLeaf(6, "ntp-ctl-pst-sel-sys-peer")

    ntp_ctl_pst_sel_pps = Enum.YLeaf(7, "ntp-ctl-pst-sel-pps")



class Ntp(Entity):
    """
    NTP operational data
    
    .. attribute:: nodes
    
    	Node\-specific NTP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes>`
    
    

    """

    _prefix = 'ip-ntp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ntp, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-ntp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", Ntp.Nodes)}
        self._child_list_classes = {}

        self.nodes = Ntp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-ntp-oper:ntp"


    class Nodes(Entity):
        """
        Node\-specific NTP operational data
        
        .. attribute:: node
        
        	NTP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-ntp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ntp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Ntp.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-oper:ntp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Nodes, [], name, value)


        class Node(Entity):
            """
            NTP operational data for a particular node
            
            .. attribute:: node  <key>
            
            	The node identifier
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: associations
            
            	NTP Associations information
            	**type**\:   :py:class:`Associations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations>`
            
            .. attribute:: associations_detail
            
            	NTP Associations Detail information
            	**type**\:   :py:class:`AssociationsDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail>`
            
            .. attribute:: status
            
            	Status of NTP peer(s)
            	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status>`
            
            

            """

            _prefix = 'ip-ntp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ntp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"associations" : ("associations", Ntp.Nodes.Node.Associations), "associations-detail" : ("associations_detail", Ntp.Nodes.Node.AssociationsDetail), "status" : ("status", Ntp.Nodes.Node.Status)}
                self._child_list_classes = {}

                self.node = YLeaf(YType.str, "node")

                self.associations = Ntp.Nodes.Node.Associations()
                self.associations.parent = self
                self._children_name_map["associations"] = "associations"
                self._children_yang_names.add("associations")

                self.associations_detail = Ntp.Nodes.Node.AssociationsDetail()
                self.associations_detail.parent = self
                self._children_name_map["associations_detail"] = "associations-detail"
                self._children_yang_names.add("associations-detail")

                self.status = Ntp.Nodes.Node.Status()
                self.status.parent = self
                self._children_name_map["status"] = "status"
                self._children_yang_names.add("status")
                self._segment_path = lambda: "node" + "[node='" + self.node.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-oper:ntp/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Nodes.Node, ['node'], name, value)


            class Associations(Entity):
                """
                NTP Associations information
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\:  bool
                
                .. attribute:: peer_summary_info
                
                	Peer info
                	**type**\: list of    :py:class:`PeerSummaryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations.PeerSummaryInfo>`
                
                .. attribute:: sys_leap
                
                	Leap
                	**type**\:   :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.Nodes.Node.Associations, self).__init__()

                    self.yang_name = "associations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"peer-summary-info" : ("peer_summary_info", Ntp.Nodes.Node.Associations.PeerSummaryInfo)}

                    self.is_ntp_enabled = YLeaf(YType.boolean, "is-ntp-enabled")

                    self.sys_leap = YLeaf(YType.enumeration, "sys-leap")

                    self.peer_summary_info = YList(self)
                    self._segment_path = lambda: "associations"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Nodes.Node.Associations, ['is_ntp_enabled', 'sys_leap'], name, value)


                class PeerSummaryInfo(Entity):
                    """
                    Peer info
                    
                    .. attribute:: peer_info_common
                    
                    	Common peer info
                    	**type**\:   :py:class:`PeerInfoCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon>`
                    
                    .. attribute:: time_since
                    
                    	Time since last frame received (\-1=none)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.Nodes.Node.Associations.PeerSummaryInfo, self).__init__()

                        self.yang_name = "peer-summary-info"
                        self.yang_parent_name = "associations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"peer-info-common" : ("peer_info_common", Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon)}
                        self._child_list_classes = {}

                        self.time_since = YLeaf(YType.int32, "time-since")

                        self.peer_info_common = Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self._children_name_map["peer_info_common"] = "peer-info-common"
                        self._children_yang_names.add("peer-info-common")
                        self._segment_path = lambda: "peer-summary-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Nodes.Node.Associations.PeerSummaryInfo, ['time_since'], name, value)


                    class PeerInfoCommon(Entity):
                        """
                        Common peer info
                        
                        .. attribute:: address
                        
                        	Peer Address
                        	**type**\:  str
                        
                        .. attribute:: delay
                        
                        	Peer delay
                        	**type**\:  str
                        
                        .. attribute:: dispersion
                        
                        	Peer dispersion
                        	**type**\:  str
                        
                        .. attribute:: host_mode
                        
                        	Association mode with this peer
                        	**type**\:   :py:class:`NtpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpMode>`
                        
                        .. attribute:: host_poll
                        
                        	Host poll
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_configured
                        
                        	Is configured
                        	**type**\:  bool
                        
                        .. attribute:: is_sys_peer
                        
                        	Indicates whether this is syspeer
                        	**type**\:  bool
                        
                        .. attribute:: offset
                        
                        	Peer offset
                        	**type**\:  str
                        
                        .. attribute:: reachability
                        
                        	Reachability
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: reference_id
                        
                        	Peer reference ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: status
                        
                        	Peer status
                        	**type**\:   :py:class:`NtpPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpPeerStatus>`
                        
                        .. attribute:: stratum
                        
                        	Peer stratum
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon, self).__init__()

                            self.yang_name = "peer-info-common"
                            self.yang_parent_name = "peer-summary-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.delay = YLeaf(YType.str, "delay")

                            self.dispersion = YLeaf(YType.str, "dispersion")

                            self.host_mode = YLeaf(YType.enumeration, "host-mode")

                            self.host_poll = YLeaf(YType.uint8, "host-poll")

                            self.is_configured = YLeaf(YType.boolean, "is-configured")

                            self.is_sys_peer = YLeaf(YType.boolean, "is-sys-peer")

                            self.offset = YLeaf(YType.str, "offset")

                            self.reachability = YLeaf(YType.uint8, "reachability")

                            self.reference_id = YLeaf(YType.str, "reference-id")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.stratum = YLeaf(YType.uint8, "stratum")
                            self._segment_path = lambda: "peer-info-common"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon, ['address', 'delay', 'dispersion', 'host_mode', 'host_poll', 'is_configured', 'is_sys_peer', 'offset', 'reachability', 'reference_id', 'status', 'stratum'], name, value)


            class AssociationsDetail(Entity):
                """
                NTP Associations Detail information
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\:  bool
                
                .. attribute:: peer_detail_info
                
                	Peer info
                	**type**\: list of    :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo>`
                
                .. attribute:: sys_leap
                
                	Leap
                	**type**\:   :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.Nodes.Node.AssociationsDetail, self).__init__()

                    self.yang_name = "associations-detail"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"peer-detail-info" : ("peer_detail_info", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo)}

                    self.is_ntp_enabled = YLeaf(YType.boolean, "is-ntp-enabled")

                    self.sys_leap = YLeaf(YType.enumeration, "sys-leap")

                    self.peer_detail_info = YList(self)
                    self._segment_path = lambda: "associations-detail"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail, ['is_ntp_enabled', 'sys_leap'], name, value)


                class PeerDetailInfo(Entity):
                    """
                    Peer info
                    
                    .. attribute:: filter_detail
                    
                    	Filter Details
                    	**type**\: list of    :py:class:`FilterDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail>`
                    
                    .. attribute:: filter_index
                    
                    	Index into filter shift register
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_authenticated
                    
                    	Is authenticated
                    	**type**\:  bool
                    
                    .. attribute:: is_ref_clock
                    
                    	Is refclock
                    	**type**\:  bool
                    
                    .. attribute:: leap
                    
                    	Leap
                    	**type**\:   :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                    
                    .. attribute:: originate_time
                    
                    	Originate timestamp
                    	**type**\:   :py:class:`OriginateTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime>`
                    
                    .. attribute:: peer_info_common
                    
                    	Common peer info
                    	**type**\:   :py:class:`PeerInfoCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon>`
                    
                    .. attribute:: peer_mode
                    
                    	Peer's association mode
                    	**type**\:   :py:class:`NtpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpMode>`
                    
                    .. attribute:: poll_interval
                    
                    	Peer poll interval
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: precision
                    
                    	Precision
                    	**type**\:  int
                    
                    	**range:** \-128..127
                    
                    .. attribute:: receive_time
                    
                    	Receive timestamp
                    	**type**\:   :py:class:`ReceiveTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime>`
                    
                    .. attribute:: ref_time
                    
                    	Reference time
                    	**type**\:   :py:class:`RefTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime>`
                    
                    .. attribute:: root_delay
                    
                    	Root delay
                    	**type**\:  str
                    
                    .. attribute:: root_dispersion
                    
                    	Root dispersion
                    	**type**\:  str
                    
                    .. attribute:: synch_distance
                    
                    	Synch distance
                    	**type**\:  str
                    
                    .. attribute:: transmit_time
                    
                    	Transmit timestamp
                    	**type**\:   :py:class:`TransmitTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime>`
                    
                    .. attribute:: version
                    
                    	NTP version
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo, self).__init__()

                        self.yang_name = "peer-detail-info"
                        self.yang_parent_name = "associations-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"originate-time" : ("originate_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime), "peer-info-common" : ("peer_info_common", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon), "receive-time" : ("receive_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime), "ref-time" : ("ref_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime), "transmit-time" : ("transmit_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime)}
                        self._child_list_classes = {"filter-detail" : ("filter_detail", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail)}

                        self.filter_index = YLeaf(YType.uint32, "filter-index")

                        self.is_authenticated = YLeaf(YType.boolean, "is-authenticated")

                        self.is_ref_clock = YLeaf(YType.boolean, "is-ref-clock")

                        self.leap = YLeaf(YType.enumeration, "leap")

                        self.peer_mode = YLeaf(YType.enumeration, "peer-mode")

                        self.poll_interval = YLeaf(YType.uint8, "poll-interval")

                        self.precision = YLeaf(YType.int8, "precision")

                        self.root_delay = YLeaf(YType.str, "root-delay")

                        self.root_dispersion = YLeaf(YType.str, "root-dispersion")

                        self.synch_distance = YLeaf(YType.str, "synch-distance")

                        self.version = YLeaf(YType.uint8, "version")

                        self.originate_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime()
                        self.originate_time.parent = self
                        self._children_name_map["originate_time"] = "originate-time"
                        self._children_yang_names.add("originate-time")

                        self.peer_info_common = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self._children_name_map["peer_info_common"] = "peer-info-common"
                        self._children_yang_names.add("peer-info-common")

                        self.receive_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime()
                        self.receive_time.parent = self
                        self._children_name_map["receive_time"] = "receive-time"
                        self._children_yang_names.add("receive-time")

                        self.ref_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime()
                        self.ref_time.parent = self
                        self._children_name_map["ref_time"] = "ref-time"
                        self._children_yang_names.add("ref-time")

                        self.transmit_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime()
                        self.transmit_time.parent = self
                        self._children_name_map["transmit_time"] = "transmit-time"
                        self._children_yang_names.add("transmit-time")

                        self.filter_detail = YList(self)
                        self._segment_path = lambda: "peer-detail-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo, ['filter_index', 'is_authenticated', 'is_ref_clock', 'leap', 'peer_mode', 'poll_interval', 'precision', 'root_delay', 'root_dispersion', 'synch_distance', 'version'], name, value)


                    class FilterDetail(Entity):
                        """
                        Filter Details
                        
                        .. attribute:: filter_delay
                        
                        	filter delay
                        	**type**\:  str
                        
                        .. attribute:: filter_disp
                        
                        	filter disp
                        	**type**\:  str
                        
                        .. attribute:: filter_offset
                        
                        	filter offset
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail, self).__init__()

                            self.yang_name = "filter-detail"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.filter_delay = YLeaf(YType.str, "filter-delay")

                            self.filter_disp = YLeaf(YType.str, "filter-disp")

                            self.filter_offset = YLeaf(YType.str, "filter-offset")
                            self._segment_path = lambda: "filter-detail"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail, ['filter_delay', 'filter_disp', 'filter_offset'], name, value)


                    class OriginateTime(Entity):
                        """
                        Originate timestamp
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime, self).__init__()

                            self.yang_name = "originate-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"frac-secs" : ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs), "sec" : ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec)}
                            self._child_list_classes = {}

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")
                            self._segment_path = lambda: "originate-time"


                        class FracSecs(Entity):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "originate-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.frac = YLeaf(YType.uint32, "frac")
                                self._segment_path = lambda: "frac-secs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs, ['frac'], name, value)


                        class Sec(Entity):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "originate-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.int = YLeaf(YType.uint32, "int")
                                self._segment_path = lambda: "sec"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec, ['int'], name, value)


                    class PeerInfoCommon(Entity):
                        """
                        Common peer info
                        
                        .. attribute:: address
                        
                        	Peer Address
                        	**type**\:  str
                        
                        .. attribute:: delay
                        
                        	Peer delay
                        	**type**\:  str
                        
                        .. attribute:: dispersion
                        
                        	Peer dispersion
                        	**type**\:  str
                        
                        .. attribute:: host_mode
                        
                        	Association mode with this peer
                        	**type**\:   :py:class:`NtpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpMode>`
                        
                        .. attribute:: host_poll
                        
                        	Host poll
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_configured
                        
                        	Is configured
                        	**type**\:  bool
                        
                        .. attribute:: is_sys_peer
                        
                        	Indicates whether this is syspeer
                        	**type**\:  bool
                        
                        .. attribute:: offset
                        
                        	Peer offset
                        	**type**\:  str
                        
                        .. attribute:: reachability
                        
                        	Reachability
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: reference_id
                        
                        	Peer reference ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: status
                        
                        	Peer status
                        	**type**\:   :py:class:`NtpPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpPeerStatus>`
                        
                        .. attribute:: stratum
                        
                        	Peer stratum
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon, self).__init__()

                            self.yang_name = "peer-info-common"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.delay = YLeaf(YType.str, "delay")

                            self.dispersion = YLeaf(YType.str, "dispersion")

                            self.host_mode = YLeaf(YType.enumeration, "host-mode")

                            self.host_poll = YLeaf(YType.uint8, "host-poll")

                            self.is_configured = YLeaf(YType.boolean, "is-configured")

                            self.is_sys_peer = YLeaf(YType.boolean, "is-sys-peer")

                            self.offset = YLeaf(YType.str, "offset")

                            self.reachability = YLeaf(YType.uint8, "reachability")

                            self.reference_id = YLeaf(YType.str, "reference-id")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.stratum = YLeaf(YType.uint8, "stratum")
                            self._segment_path = lambda: "peer-info-common"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon, ['address', 'delay', 'dispersion', 'host_mode', 'host_poll', 'is_configured', 'is_sys_peer', 'offset', 'reachability', 'reference_id', 'status', 'stratum'], name, value)


                    class ReceiveTime(Entity):
                        """
                        Receive timestamp
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime, self).__init__()

                            self.yang_name = "receive-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"frac-secs" : ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs), "sec" : ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec)}
                            self._child_list_classes = {}

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")
                            self._segment_path = lambda: "receive-time"


                        class FracSecs(Entity):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "receive-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.frac = YLeaf(YType.uint32, "frac")
                                self._segment_path = lambda: "frac-secs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs, ['frac'], name, value)


                        class Sec(Entity):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "receive-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.int = YLeaf(YType.uint32, "int")
                                self._segment_path = lambda: "sec"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec, ['int'], name, value)


                    class RefTime(Entity):
                        """
                        Reference time
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime, self).__init__()

                            self.yang_name = "ref-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"frac-secs" : ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs), "sec" : ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec)}
                            self._child_list_classes = {}

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")
                            self._segment_path = lambda: "ref-time"


                        class FracSecs(Entity):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "ref-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.frac = YLeaf(YType.uint32, "frac")
                                self._segment_path = lambda: "frac-secs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs, ['frac'], name, value)


                        class Sec(Entity):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "ref-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.int = YLeaf(YType.uint32, "int")
                                self._segment_path = lambda: "sec"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec, ['int'], name, value)


                    class TransmitTime(Entity):
                        """
                        Transmit timestamp
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs>`
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:   :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec>`
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime, self).__init__()

                            self.yang_name = "transmit-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"frac-secs" : ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs), "sec" : ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec)}
                            self._child_list_classes = {}

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")
                            self._segment_path = lambda: "transmit-time"


                        class FracSecs(Entity):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "transmit-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.frac = YLeaf(YType.uint32, "frac")
                                self._segment_path = lambda: "frac-secs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs, ['frac'], name, value)


                        class Sec(Entity):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "transmit-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.int = YLeaf(YType.uint32, "int")
                                self._segment_path = lambda: "sec"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec, ['int'], name, value)


            class Status(Entity):
                """
                Status of NTP peer(s)
                
                .. attribute:: clock_period
                
                	Clock period in nanosecs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: nanosecond
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\:  bool
                
                .. attribute:: is_updated
                
                	Is clock updated
                	**type**\:   :py:class:`ClockUpdateNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.ClockUpdateNode>`
                
                .. attribute:: last_update
                
                	Last Update
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: loop_filter_state
                
                	Loop Filter State
                	**type**\:   :py:class:`NtpLoopFilterState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLoopFilterState>`
                
                .. attribute:: poll_interval
                
                	Peer poll interval
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: sys_dispersion
                
                	Peer dispersion
                	**type**\:  str
                
                .. attribute:: sys_drift
                
                	System Drift
                	**type**\:   :py:class:`SysDrift <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift>`
                
                .. attribute:: sys_leap
                
                	leap
                	**type**\:   :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                
                .. attribute:: sys_offset
                
                	Clock offset
                	**type**\:  str
                
                .. attribute:: sys_precision
                
                	Precision
                	**type**\:  int
                
                	**range:** \-128..127
                
                .. attribute:: sys_ref_id
                
                	Reference clock ID
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: sys_ref_time
                
                	Reference time
                	**type**\:   :py:class:`SysRefTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime>`
                
                .. attribute:: sys_root_delay
                
                	Root delay
                	**type**\:  str
                
                .. attribute:: sys_root_dispersion
                
                	Root dispersion
                	**type**\:  str
                
                .. attribute:: sys_stratum
                
                	Stratum
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ntp.Nodes.Node.Status, self).__init__()

                    self.yang_name = "status"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"sys-drift" : ("sys_drift", Ntp.Nodes.Node.Status.SysDrift), "sys-ref-time" : ("sys_ref_time", Ntp.Nodes.Node.Status.SysRefTime)}
                    self._child_list_classes = {}

                    self.clock_period = YLeaf(YType.uint32, "clock-period")

                    self.is_ntp_enabled = YLeaf(YType.boolean, "is-ntp-enabled")

                    self.is_updated = YLeaf(YType.enumeration, "is-updated")

                    self.last_update = YLeaf(YType.int32, "last-update")

                    self.loop_filter_state = YLeaf(YType.enumeration, "loop-filter-state")

                    self.poll_interval = YLeaf(YType.uint8, "poll-interval")

                    self.sys_dispersion = YLeaf(YType.str, "sys-dispersion")

                    self.sys_leap = YLeaf(YType.enumeration, "sys-leap")

                    self.sys_offset = YLeaf(YType.str, "sys-offset")

                    self.sys_precision = YLeaf(YType.int8, "sys-precision")

                    self.sys_ref_id = YLeaf(YType.str, "sys-ref-id")

                    self.sys_root_delay = YLeaf(YType.str, "sys-root-delay")

                    self.sys_root_dispersion = YLeaf(YType.str, "sys-root-dispersion")

                    self.sys_stratum = YLeaf(YType.uint8, "sys-stratum")

                    self.sys_drift = Ntp.Nodes.Node.Status.SysDrift()
                    self.sys_drift.parent = self
                    self._children_name_map["sys_drift"] = "sys-drift"
                    self._children_yang_names.add("sys-drift")

                    self.sys_ref_time = Ntp.Nodes.Node.Status.SysRefTime()
                    self.sys_ref_time.parent = self
                    self._children_name_map["sys_ref_time"] = "sys-ref-time"
                    self._children_yang_names.add("sys-ref-time")
                    self._segment_path = lambda: "status"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Nodes.Node.Status, ['clock_period', 'is_ntp_enabled', 'is_updated', 'last_update', 'loop_filter_state', 'poll_interval', 'sys_dispersion', 'sys_leap', 'sys_offset', 'sys_precision', 'sys_ref_id', 'sys_root_delay', 'sys_root_dispersion', 'sys_stratum'], name, value)


                class SysDrift(Entity):
                    """
                    System Drift
                    
                    .. attribute:: frac_secs
                    
                    	Fractional part in 64\-bit NTP timestamp
                    	**type**\:   :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift.FracSecs>`
                    
                    .. attribute:: sec
                    
                    	Second part in 64\-bit NTP timestamp
                    	**type**\:   :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift.Sec>`
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.Nodes.Node.Status.SysDrift, self).__init__()

                        self.yang_name = "sys-drift"
                        self.yang_parent_name = "status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"frac-secs" : ("frac_secs", Ntp.Nodes.Node.Status.SysDrift.FracSecs), "sec" : ("sec", Ntp.Nodes.Node.Status.SysDrift.Sec)}
                        self._child_list_classes = {}

                        self.frac_secs = Ntp.Nodes.Node.Status.SysDrift.FracSecs()
                        self.frac_secs.parent = self
                        self._children_name_map["frac_secs"] = "frac-secs"
                        self._children_yang_names.add("frac-secs")

                        self.sec = Ntp.Nodes.Node.Status.SysDrift.Sec()
                        self.sec.parent = self
                        self._children_name_map["sec"] = "sec"
                        self._children_yang_names.add("sec")
                        self._segment_path = lambda: "sys-drift"


                    class FracSecs(Entity):
                        """
                        Fractional part in 64\-bit NTP timestamp
                        
                        .. attribute:: frac
                        
                        	Fractional format in NTP reference code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.Status.SysDrift.FracSecs, self).__init__()

                            self.yang_name = "frac-secs"
                            self.yang_parent_name = "sys-drift"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.frac = YLeaf(YType.uint32, "frac")
                            self._segment_path = lambda: "frac-secs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysDrift.FracSecs, ['frac'], name, value)


                    class Sec(Entity):
                        """
                        Second part in 64\-bit NTP timestamp
                        
                        .. attribute:: int
                        
                        	Integer format in NTP reference code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.Status.SysDrift.Sec, self).__init__()

                            self.yang_name = "sec"
                            self.yang_parent_name = "sys-drift"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.int = YLeaf(YType.uint32, "int")
                            self._segment_path = lambda: "sec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysDrift.Sec, ['int'], name, value)


                class SysRefTime(Entity):
                    """
                    Reference time
                    
                    .. attribute:: frac_secs
                    
                    	Fractional part in 64\-bit NTP timestamp
                    	**type**\:   :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime.FracSecs>`
                    
                    .. attribute:: sec
                    
                    	Second part in 64\-bit NTP timestamp
                    	**type**\:   :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime.Sec>`
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ntp.Nodes.Node.Status.SysRefTime, self).__init__()

                        self.yang_name = "sys-ref-time"
                        self.yang_parent_name = "status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"frac-secs" : ("frac_secs", Ntp.Nodes.Node.Status.SysRefTime.FracSecs), "sec" : ("sec", Ntp.Nodes.Node.Status.SysRefTime.Sec)}
                        self._child_list_classes = {}

                        self.frac_secs = Ntp.Nodes.Node.Status.SysRefTime.FracSecs()
                        self.frac_secs.parent = self
                        self._children_name_map["frac_secs"] = "frac-secs"
                        self._children_yang_names.add("frac-secs")

                        self.sec = Ntp.Nodes.Node.Status.SysRefTime.Sec()
                        self.sec.parent = self
                        self._children_name_map["sec"] = "sec"
                        self._children_yang_names.add("sec")
                        self._segment_path = lambda: "sys-ref-time"


                    class FracSecs(Entity):
                        """
                        Fractional part in 64\-bit NTP timestamp
                        
                        .. attribute:: frac
                        
                        	Fractional format in NTP reference code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.Status.SysRefTime.FracSecs, self).__init__()

                            self.yang_name = "frac-secs"
                            self.yang_parent_name = "sys-ref-time"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.frac = YLeaf(YType.uint32, "frac")
                            self._segment_path = lambda: "frac-secs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysRefTime.FracSecs, ['frac'], name, value)


                    class Sec(Entity):
                        """
                        Second part in 64\-bit NTP timestamp
                        
                        .. attribute:: int
                        
                        	Integer format in NTP reference code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ntp.Nodes.Node.Status.SysRefTime.Sec, self).__init__()

                            self.yang_name = "sec"
                            self.yang_parent_name = "sys-ref-time"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.int = YLeaf(YType.uint32, "int")
                            self._segment_path = lambda: "sec"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysRefTime.Sec, ['int'], name, value)

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

