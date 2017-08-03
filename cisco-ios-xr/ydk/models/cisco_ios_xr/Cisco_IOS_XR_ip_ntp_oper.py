""" Cisco_IOS_XR_ip_ntp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package operational data.

This module contains definitions
for the following management objects\:
  ntp\: NTP operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.nodes = Ntp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


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

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ntp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ntp.Nodes, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ntp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ntp.Nodes.Node, self).__setattr__(name, value)


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

                    self.is_ntp_enabled = YLeaf(YType.boolean, "is-ntp-enabled")

                    self.sys_leap = YLeaf(YType.enumeration, "sys-leap")

                    self.peer_detail_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("is_ntp_enabled",
                                    "sys_leap") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.Nodes.Node.AssociationsDetail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.Nodes.Node.AssociationsDetail, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("filter_index",
                                        "is_authenticated",
                                        "is_ref_clock",
                                        "leap",
                                        "peer_mode",
                                        "poll_interval",
                                        "precision",
                                        "root_delay",
                                        "root_dispersion",
                                        "synch_distance",
                                        "version") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address",
                                            "delay",
                                            "dispersion",
                                            "host_mode",
                                            "host_poll",
                                            "is_configured",
                                            "is_sys_peer",
                                            "offset",
                                            "reachability",
                                            "reference_id",
                                            "status",
                                            "stratum") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.delay.is_set or
                                self.dispersion.is_set or
                                self.host_mode.is_set or
                                self.host_poll.is_set or
                                self.is_configured.is_set or
                                self.is_sys_peer.is_set or
                                self.offset.is_set or
                                self.reachability.is_set or
                                self.reference_id.is_set or
                                self.status.is_set or
                                self.stratum.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set or
                                self.dispersion.yfilter != YFilter.not_set or
                                self.host_mode.yfilter != YFilter.not_set or
                                self.host_poll.yfilter != YFilter.not_set or
                                self.is_configured.yfilter != YFilter.not_set or
                                self.is_sys_peer.yfilter != YFilter.not_set or
                                self.offset.yfilter != YFilter.not_set or
                                self.reachability.yfilter != YFilter.not_set or
                                self.reference_id.yfilter != YFilter.not_set or
                                self.status.yfilter != YFilter.not_set or
                                self.stratum.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-info-common" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())
                            if (self.dispersion.is_set or self.dispersion.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dispersion.get_name_leafdata())
                            if (self.host_mode.is_set or self.host_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_mode.get_name_leafdata())
                            if (self.host_poll.is_set or self.host_poll.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_poll.get_name_leafdata())
                            if (self.is_configured.is_set or self.is_configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_configured.get_name_leafdata())
                            if (self.is_sys_peer.is_set or self.is_sys_peer.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_sys_peer.get_name_leafdata())
                            if (self.offset.is_set or self.offset.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.offset.get_name_leafdata())
                            if (self.reachability.is_set or self.reachability.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reachability.get_name_leafdata())
                            if (self.reference_id.is_set or self.reference_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reference_id.get_name_leafdata())
                            if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status.get_name_leafdata())
                            if (self.stratum.is_set or self.stratum.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stratum.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "delay" or name == "dispersion" or name == "host-mode" or name == "host-poll" or name == "is-configured" or name == "is-sys-peer" or name == "offset" or name == "reachability" or name == "reference-id" or name == "status" or name == "stratum"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix
                            if(value_path == "dispersion"):
                                self.dispersion = value
                                self.dispersion.value_namespace = name_space
                                self.dispersion.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-mode"):
                                self.host_mode = value
                                self.host_mode.value_namespace = name_space
                                self.host_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-poll"):
                                self.host_poll = value
                                self.host_poll.value_namespace = name_space
                                self.host_poll.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-configured"):
                                self.is_configured = value
                                self.is_configured.value_namespace = name_space
                                self.is_configured.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-sys-peer"):
                                self.is_sys_peer = value
                                self.is_sys_peer.value_namespace = name_space
                                self.is_sys_peer.value_namespace_prefix = name_space_prefix
                            if(value_path == "offset"):
                                self.offset = value
                                self.offset.value_namespace = name_space
                                self.offset.value_namespace_prefix = name_space_prefix
                            if(value_path == "reachability"):
                                self.reachability = value
                                self.reachability.value_namespace = name_space
                                self.reachability.value_namespace_prefix = name_space_prefix
                            if(value_path == "reference-id"):
                                self.reference_id = value
                                self.reference_id.value_namespace = name_space
                                self.reference_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "status"):
                                self.status = value
                                self.status.value_namespace = name_space
                                self.status.value_namespace_prefix = name_space_prefix
                            if(value_path == "stratum"):
                                self.stratum = value
                                self.stratum.value_namespace = name_space
                                self.stratum.value_namespace_prefix = name_space_prefix


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

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")


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

                                self.int = YLeaf(YType.uint32, "int")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("int") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec, self).__setattr__(name, value)

                            def has_data(self):
                                return self.int.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.int.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sec" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.int.is_set or self.int.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.int.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "int"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "int"):
                                    self.int = value
                                    self.int.value_namespace = name_space
                                    self.int.value_namespace_prefix = name_space_prefix


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

                                self.frac = YLeaf(YType.uint32, "frac")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("frac") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs, self).__setattr__(name, value)

                            def has_data(self):
                                return self.frac.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.frac.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "frac-secs" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.frac.is_set or self.frac.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.frac.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "frac"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "frac"):
                                    self.frac = value
                                    self.frac.value_namespace = name_space
                                    self.frac.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.frac_secs is not None and self.frac_secs.has_data()) or
                                (self.sec is not None and self.sec.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.frac_secs is not None and self.frac_secs.has_operation()) or
                                (self.sec is not None and self.sec.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ref-time" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "frac-secs"):
                                if (self.frac_secs is None):
                                    self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs()
                                    self.frac_secs.parent = self
                                    self._children_name_map["frac_secs"] = "frac-secs"
                                return self.frac_secs

                            if (child_yang_name == "sec"):
                                if (self.sec is None):
                                    self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec()
                                    self.sec.parent = self
                                    self._children_name_map["sec"] = "sec"
                                return self.sec

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "frac-secs" or name == "sec"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")


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

                                self.int = YLeaf(YType.uint32, "int")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("int") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec, self).__setattr__(name, value)

                            def has_data(self):
                                return self.int.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.int.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sec" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.int.is_set or self.int.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.int.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "int"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "int"):
                                    self.int = value
                                    self.int.value_namespace = name_space
                                    self.int.value_namespace_prefix = name_space_prefix


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

                                self.frac = YLeaf(YType.uint32, "frac")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("frac") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs, self).__setattr__(name, value)

                            def has_data(self):
                                return self.frac.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.frac.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "frac-secs" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.frac.is_set or self.frac.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.frac.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "frac"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "frac"):
                                    self.frac = value
                                    self.frac.value_namespace = name_space
                                    self.frac.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.frac_secs is not None and self.frac_secs.has_data()) or
                                (self.sec is not None and self.sec.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.frac_secs is not None and self.frac_secs.has_operation()) or
                                (self.sec is not None and self.sec.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "originate-time" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "frac-secs"):
                                if (self.frac_secs is None):
                                    self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs()
                                    self.frac_secs.parent = self
                                    self._children_name_map["frac_secs"] = "frac-secs"
                                return self.frac_secs

                            if (child_yang_name == "sec"):
                                if (self.sec is None):
                                    self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec()
                                    self.sec.parent = self
                                    self._children_name_map["sec"] = "sec"
                                return self.sec

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "frac-secs" or name == "sec"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")


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

                                self.int = YLeaf(YType.uint32, "int")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("int") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec, self).__setattr__(name, value)

                            def has_data(self):
                                return self.int.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.int.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sec" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.int.is_set or self.int.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.int.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "int"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "int"):
                                    self.int = value
                                    self.int.value_namespace = name_space
                                    self.int.value_namespace_prefix = name_space_prefix


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

                                self.frac = YLeaf(YType.uint32, "frac")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("frac") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs, self).__setattr__(name, value)

                            def has_data(self):
                                return self.frac.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.frac.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "frac-secs" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.frac.is_set or self.frac.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.frac.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "frac"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "frac"):
                                    self.frac = value
                                    self.frac.value_namespace = name_space
                                    self.frac.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.frac_secs is not None and self.frac_secs.has_data()) or
                                (self.sec is not None and self.sec.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.frac_secs is not None and self.frac_secs.has_operation()) or
                                (self.sec is not None and self.sec.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "receive-time" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "frac-secs"):
                                if (self.frac_secs is None):
                                    self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs()
                                    self.frac_secs.parent = self
                                    self._children_name_map["frac_secs"] = "frac-secs"
                                return self.frac_secs

                            if (child_yang_name == "sec"):
                                if (self.sec is None):
                                    self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec()
                                    self.sec.parent = self
                                    self._children_name_map["sec"] = "sec"
                                return self.sec

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "frac-secs" or name == "sec"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._children_yang_names.add("frac-secs")

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"
                            self._children_yang_names.add("sec")


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

                                self.int = YLeaf(YType.uint32, "int")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("int") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec, self).__setattr__(name, value)

                            def has_data(self):
                                return self.int.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.int.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sec" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.int.is_set or self.int.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.int.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "int"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "int"):
                                    self.int = value
                                    self.int.value_namespace = name_space
                                    self.int.value_namespace_prefix = name_space_prefix


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

                                self.frac = YLeaf(YType.uint32, "frac")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("frac") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs, self).__setattr__(name, value)

                            def has_data(self):
                                return self.frac.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.frac.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "frac-secs" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.frac.is_set or self.frac.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.frac.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "frac"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "frac"):
                                    self.frac = value
                                    self.frac.value_namespace = name_space
                                    self.frac.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.frac_secs is not None and self.frac_secs.has_data()) or
                                (self.sec is not None and self.sec.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.frac_secs is not None and self.frac_secs.has_operation()) or
                                (self.sec is not None and self.sec.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "transmit-time" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "frac-secs"):
                                if (self.frac_secs is None):
                                    self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs()
                                    self.frac_secs.parent = self
                                    self._children_name_map["frac_secs"] = "frac-secs"
                                return self.frac_secs

                            if (child_yang_name == "sec"):
                                if (self.sec is None):
                                    self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec()
                                    self.sec.parent = self
                                    self._children_name_map["sec"] = "sec"
                                return self.sec

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "frac-secs" or name == "sec"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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

                            self.filter_delay = YLeaf(YType.str, "filter-delay")

                            self.filter_disp = YLeaf(YType.str, "filter-disp")

                            self.filter_offset = YLeaf(YType.str, "filter-offset")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("filter_delay",
                                            "filter_disp",
                                            "filter_offset") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.filter_delay.is_set or
                                self.filter_disp.is_set or
                                self.filter_offset.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.filter_delay.yfilter != YFilter.not_set or
                                self.filter_disp.yfilter != YFilter.not_set or
                                self.filter_offset.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "filter-detail" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.filter_delay.is_set or self.filter_delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.filter_delay.get_name_leafdata())
                            if (self.filter_disp.is_set or self.filter_disp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.filter_disp.get_name_leafdata())
                            if (self.filter_offset.is_set or self.filter_offset.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.filter_offset.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "filter-delay" or name == "filter-disp" or name == "filter-offset"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "filter-delay"):
                                self.filter_delay = value
                                self.filter_delay.value_namespace = name_space
                                self.filter_delay.value_namespace_prefix = name_space_prefix
                            if(value_path == "filter-disp"):
                                self.filter_disp = value
                                self.filter_disp.value_namespace = name_space
                                self.filter_disp.value_namespace_prefix = name_space_prefix
                            if(value_path == "filter-offset"):
                                self.filter_offset = value
                                self.filter_offset.value_namespace = name_space
                                self.filter_offset.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.filter_detail:
                            if (c.has_data()):
                                return True
                        return (
                            self.filter_index.is_set or
                            self.is_authenticated.is_set or
                            self.is_ref_clock.is_set or
                            self.leap.is_set or
                            self.peer_mode.is_set or
                            self.poll_interval.is_set or
                            self.precision.is_set or
                            self.root_delay.is_set or
                            self.root_dispersion.is_set or
                            self.synch_distance.is_set or
                            self.version.is_set or
                            (self.originate_time is not None and self.originate_time.has_data()) or
                            (self.peer_info_common is not None and self.peer_info_common.has_data()) or
                            (self.receive_time is not None and self.receive_time.has_data()) or
                            (self.ref_time is not None and self.ref_time.has_data()) or
                            (self.transmit_time is not None and self.transmit_time.has_data()))

                    def has_operation(self):
                        for c in self.filter_detail:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.filter_index.yfilter != YFilter.not_set or
                            self.is_authenticated.yfilter != YFilter.not_set or
                            self.is_ref_clock.yfilter != YFilter.not_set or
                            self.leap.yfilter != YFilter.not_set or
                            self.peer_mode.yfilter != YFilter.not_set or
                            self.poll_interval.yfilter != YFilter.not_set or
                            self.precision.yfilter != YFilter.not_set or
                            self.root_delay.yfilter != YFilter.not_set or
                            self.root_dispersion.yfilter != YFilter.not_set or
                            self.synch_distance.yfilter != YFilter.not_set or
                            self.version.yfilter != YFilter.not_set or
                            (self.originate_time is not None and self.originate_time.has_operation()) or
                            (self.peer_info_common is not None and self.peer_info_common.has_operation()) or
                            (self.receive_time is not None and self.receive_time.has_operation()) or
                            (self.ref_time is not None and self.ref_time.has_operation()) or
                            (self.transmit_time is not None and self.transmit_time.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer-detail-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.filter_index.is_set or self.filter_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.filter_index.get_name_leafdata())
                        if (self.is_authenticated.is_set or self.is_authenticated.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_authenticated.get_name_leafdata())
                        if (self.is_ref_clock.is_set or self.is_ref_clock.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_ref_clock.get_name_leafdata())
                        if (self.leap.is_set or self.leap.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.leap.get_name_leafdata())
                        if (self.peer_mode.is_set or self.peer_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_mode.get_name_leafdata())
                        if (self.poll_interval.is_set or self.poll_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.poll_interval.get_name_leafdata())
                        if (self.precision.is_set or self.precision.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.precision.get_name_leafdata())
                        if (self.root_delay.is_set or self.root_delay.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.root_delay.get_name_leafdata())
                        if (self.root_dispersion.is_set or self.root_dispersion.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.root_dispersion.get_name_leafdata())
                        if (self.synch_distance.is_set or self.synch_distance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.synch_distance.get_name_leafdata())
                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.version.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "filter-detail"):
                            for c in self.filter_detail:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.filter_detail.append(c)
                            return c

                        if (child_yang_name == "originate-time"):
                            if (self.originate_time is None):
                                self.originate_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime()
                                self.originate_time.parent = self
                                self._children_name_map["originate_time"] = "originate-time"
                            return self.originate_time

                        if (child_yang_name == "peer-info-common"):
                            if (self.peer_info_common is None):
                                self.peer_info_common = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon()
                                self.peer_info_common.parent = self
                                self._children_name_map["peer_info_common"] = "peer-info-common"
                            return self.peer_info_common

                        if (child_yang_name == "receive-time"):
                            if (self.receive_time is None):
                                self.receive_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime()
                                self.receive_time.parent = self
                                self._children_name_map["receive_time"] = "receive-time"
                            return self.receive_time

                        if (child_yang_name == "ref-time"):
                            if (self.ref_time is None):
                                self.ref_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime()
                                self.ref_time.parent = self
                                self._children_name_map["ref_time"] = "ref-time"
                            return self.ref_time

                        if (child_yang_name == "transmit-time"):
                            if (self.transmit_time is None):
                                self.transmit_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime()
                                self.transmit_time.parent = self
                                self._children_name_map["transmit_time"] = "transmit-time"
                            return self.transmit_time

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "filter-detail" or name == "originate-time" or name == "peer-info-common" or name == "receive-time" or name == "ref-time" or name == "transmit-time" or name == "filter-index" or name == "is-authenticated" or name == "is-ref-clock" or name == "leap" or name == "peer-mode" or name == "poll-interval" or name == "precision" or name == "root-delay" or name == "root-dispersion" or name == "synch-distance" or name == "version"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "filter-index"):
                            self.filter_index = value
                            self.filter_index.value_namespace = name_space
                            self.filter_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-authenticated"):
                            self.is_authenticated = value
                            self.is_authenticated.value_namespace = name_space
                            self.is_authenticated.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-ref-clock"):
                            self.is_ref_clock = value
                            self.is_ref_clock.value_namespace = name_space
                            self.is_ref_clock.value_namespace_prefix = name_space_prefix
                        if(value_path == "leap"):
                            self.leap = value
                            self.leap.value_namespace = name_space
                            self.leap.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-mode"):
                            self.peer_mode = value
                            self.peer_mode.value_namespace = name_space
                            self.peer_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "poll-interval"):
                            self.poll_interval = value
                            self.poll_interval.value_namespace = name_space
                            self.poll_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "precision"):
                            self.precision = value
                            self.precision.value_namespace = name_space
                            self.precision.value_namespace_prefix = name_space_prefix
                        if(value_path == "root-delay"):
                            self.root_delay = value
                            self.root_delay.value_namespace = name_space
                            self.root_delay.value_namespace_prefix = name_space_prefix
                        if(value_path == "root-dispersion"):
                            self.root_dispersion = value
                            self.root_dispersion.value_namespace = name_space
                            self.root_dispersion.value_namespace_prefix = name_space_prefix
                        if(value_path == "synch-distance"):
                            self.synch_distance = value
                            self.synch_distance.value_namespace = name_space
                            self.synch_distance.value_namespace_prefix = name_space_prefix
                        if(value_path == "version"):
                            self.version = value
                            self.version.value_namespace = name_space
                            self.version.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.peer_detail_info:
                        if (c.has_data()):
                            return True
                    return (
                        self.is_ntp_enabled.is_set or
                        self.sys_leap.is_set)

                def has_operation(self):
                    for c in self.peer_detail_info:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.is_ntp_enabled.yfilter != YFilter.not_set or
                        self.sys_leap.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "associations-detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.is_ntp_enabled.is_set or self.is_ntp_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_ntp_enabled.get_name_leafdata())
                    if (self.sys_leap.is_set or self.sys_leap.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_leap.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "peer-detail-info"):
                        for c in self.peer_detail_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.peer_detail_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-detail-info" or name == "is-ntp-enabled" or name == "sys-leap"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "is-ntp-enabled"):
                        self.is_ntp_enabled = value
                        self.is_ntp_enabled.value_namespace = name_space
                        self.is_ntp_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-leap"):
                        self.sys_leap = value
                        self.sys_leap.value_namespace = name_space
                        self.sys_leap.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("clock_period",
                                    "is_ntp_enabled",
                                    "is_updated",
                                    "last_update",
                                    "loop_filter_state",
                                    "poll_interval",
                                    "sys_dispersion",
                                    "sys_leap",
                                    "sys_offset",
                                    "sys_precision",
                                    "sys_ref_id",
                                    "sys_root_delay",
                                    "sys_root_dispersion",
                                    "sys_stratum") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.Nodes.Node.Status, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.Nodes.Node.Status, self).__setattr__(name, value)


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

                        self.frac_secs = Ntp.Nodes.Node.Status.SysRefTime.FracSecs()
                        self.frac_secs.parent = self
                        self._children_name_map["frac_secs"] = "frac-secs"
                        self._children_yang_names.add("frac-secs")

                        self.sec = Ntp.Nodes.Node.Status.SysRefTime.Sec()
                        self.sec.parent = self
                        self._children_name_map["sec"] = "sec"
                        self._children_yang_names.add("sec")


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

                            self.int = YLeaf(YType.uint32, "int")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("int") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.Status.SysRefTime.Sec, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.Status.SysRefTime.Sec, self).__setattr__(name, value)

                        def has_data(self):
                            return self.int.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.int.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.int.is_set or self.int.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.int.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "int"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "int"):
                                self.int = value
                                self.int.value_namespace = name_space
                                self.int.value_namespace_prefix = name_space_prefix


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

                            self.frac = YLeaf(YType.uint32, "frac")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("frac") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.Status.SysRefTime.FracSecs, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.Status.SysRefTime.FracSecs, self).__setattr__(name, value)

                        def has_data(self):
                            return self.frac.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.frac.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "frac-secs" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.frac.is_set or self.frac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.frac.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "frac"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "frac"):
                                self.frac = value
                                self.frac.value_namespace = name_space
                                self.frac.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.frac_secs is not None and self.frac_secs.has_data()) or
                            (self.sec is not None and self.sec.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.frac_secs is not None and self.frac_secs.has_operation()) or
                            (self.sec is not None and self.sec.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sys-ref-time" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "frac-secs"):
                            if (self.frac_secs is None):
                                self.frac_secs = Ntp.Nodes.Node.Status.SysRefTime.FracSecs()
                                self.frac_secs.parent = self
                                self._children_name_map["frac_secs"] = "frac-secs"
                            return self.frac_secs

                        if (child_yang_name == "sec"):
                            if (self.sec is None):
                                self.sec = Ntp.Nodes.Node.Status.SysRefTime.Sec()
                                self.sec.parent = self
                                self._children_name_map["sec"] = "sec"
                            return self.sec

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "frac-secs" or name == "sec"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.frac_secs = Ntp.Nodes.Node.Status.SysDrift.FracSecs()
                        self.frac_secs.parent = self
                        self._children_name_map["frac_secs"] = "frac-secs"
                        self._children_yang_names.add("frac-secs")

                        self.sec = Ntp.Nodes.Node.Status.SysDrift.Sec()
                        self.sec.parent = self
                        self._children_name_map["sec"] = "sec"
                        self._children_yang_names.add("sec")


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

                            self.int = YLeaf(YType.uint32, "int")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("int") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.Status.SysDrift.Sec, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.Status.SysDrift.Sec, self).__setattr__(name, value)

                        def has_data(self):
                            return self.int.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.int.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sec" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.int.is_set or self.int.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.int.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "int"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "int"):
                                self.int = value
                                self.int.value_namespace = name_space
                                self.int.value_namespace_prefix = name_space_prefix


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

                            self.frac = YLeaf(YType.uint32, "frac")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("frac") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.Status.SysDrift.FracSecs, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.Status.SysDrift.FracSecs, self).__setattr__(name, value)

                        def has_data(self):
                            return self.frac.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.frac.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "frac-secs" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.frac.is_set or self.frac.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.frac.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "frac"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "frac"):
                                self.frac = value
                                self.frac.value_namespace = name_space
                                self.frac.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.frac_secs is not None and self.frac_secs.has_data()) or
                            (self.sec is not None and self.sec.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.frac_secs is not None and self.frac_secs.has_operation()) or
                            (self.sec is not None and self.sec.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sys-drift" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "frac-secs"):
                            if (self.frac_secs is None):
                                self.frac_secs = Ntp.Nodes.Node.Status.SysDrift.FracSecs()
                                self.frac_secs.parent = self
                                self._children_name_map["frac_secs"] = "frac-secs"
                            return self.frac_secs

                        if (child_yang_name == "sec"):
                            if (self.sec is None):
                                self.sec = Ntp.Nodes.Node.Status.SysDrift.Sec()
                                self.sec.parent = self
                                self._children_name_map["sec"] = "sec"
                            return self.sec

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "frac-secs" or name == "sec"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.clock_period.is_set or
                        self.is_ntp_enabled.is_set or
                        self.is_updated.is_set or
                        self.last_update.is_set or
                        self.loop_filter_state.is_set or
                        self.poll_interval.is_set or
                        self.sys_dispersion.is_set or
                        self.sys_leap.is_set or
                        self.sys_offset.is_set or
                        self.sys_precision.is_set or
                        self.sys_ref_id.is_set or
                        self.sys_root_delay.is_set or
                        self.sys_root_dispersion.is_set or
                        self.sys_stratum.is_set or
                        (self.sys_drift is not None and self.sys_drift.has_data()) or
                        (self.sys_ref_time is not None and self.sys_ref_time.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.clock_period.yfilter != YFilter.not_set or
                        self.is_ntp_enabled.yfilter != YFilter.not_set or
                        self.is_updated.yfilter != YFilter.not_set or
                        self.last_update.yfilter != YFilter.not_set or
                        self.loop_filter_state.yfilter != YFilter.not_set or
                        self.poll_interval.yfilter != YFilter.not_set or
                        self.sys_dispersion.yfilter != YFilter.not_set or
                        self.sys_leap.yfilter != YFilter.not_set or
                        self.sys_offset.yfilter != YFilter.not_set or
                        self.sys_precision.yfilter != YFilter.not_set or
                        self.sys_ref_id.yfilter != YFilter.not_set or
                        self.sys_root_delay.yfilter != YFilter.not_set or
                        self.sys_root_dispersion.yfilter != YFilter.not_set or
                        self.sys_stratum.yfilter != YFilter.not_set or
                        (self.sys_drift is not None and self.sys_drift.has_operation()) or
                        (self.sys_ref_time is not None and self.sys_ref_time.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "status" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.clock_period.is_set or self.clock_period.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.clock_period.get_name_leafdata())
                    if (self.is_ntp_enabled.is_set or self.is_ntp_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_ntp_enabled.get_name_leafdata())
                    if (self.is_updated.is_set or self.is_updated.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_updated.get_name_leafdata())
                    if (self.last_update.is_set or self.last_update.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_update.get_name_leafdata())
                    if (self.loop_filter_state.is_set or self.loop_filter_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loop_filter_state.get_name_leafdata())
                    if (self.poll_interval.is_set or self.poll_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.poll_interval.get_name_leafdata())
                    if (self.sys_dispersion.is_set or self.sys_dispersion.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_dispersion.get_name_leafdata())
                    if (self.sys_leap.is_set or self.sys_leap.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_leap.get_name_leafdata())
                    if (self.sys_offset.is_set or self.sys_offset.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_offset.get_name_leafdata())
                    if (self.sys_precision.is_set or self.sys_precision.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_precision.get_name_leafdata())
                    if (self.sys_ref_id.is_set or self.sys_ref_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_ref_id.get_name_leafdata())
                    if (self.sys_root_delay.is_set or self.sys_root_delay.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_root_delay.get_name_leafdata())
                    if (self.sys_root_dispersion.is_set or self.sys_root_dispersion.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_root_dispersion.get_name_leafdata())
                    if (self.sys_stratum.is_set or self.sys_stratum.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_stratum.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "sys-drift"):
                        if (self.sys_drift is None):
                            self.sys_drift = Ntp.Nodes.Node.Status.SysDrift()
                            self.sys_drift.parent = self
                            self._children_name_map["sys_drift"] = "sys-drift"
                        return self.sys_drift

                    if (child_yang_name == "sys-ref-time"):
                        if (self.sys_ref_time is None):
                            self.sys_ref_time = Ntp.Nodes.Node.Status.SysRefTime()
                            self.sys_ref_time.parent = self
                            self._children_name_map["sys_ref_time"] = "sys-ref-time"
                        return self.sys_ref_time

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sys-drift" or name == "sys-ref-time" or name == "clock-period" or name == "is-ntp-enabled" or name == "is-updated" or name == "last-update" or name == "loop-filter-state" or name == "poll-interval" or name == "sys-dispersion" or name == "sys-leap" or name == "sys-offset" or name == "sys-precision" or name == "sys-ref-id" or name == "sys-root-delay" or name == "sys-root-dispersion" or name == "sys-stratum"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "clock-period"):
                        self.clock_period = value
                        self.clock_period.value_namespace = name_space
                        self.clock_period.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-ntp-enabled"):
                        self.is_ntp_enabled = value
                        self.is_ntp_enabled.value_namespace = name_space
                        self.is_ntp_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-updated"):
                        self.is_updated = value
                        self.is_updated.value_namespace = name_space
                        self.is_updated.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-update"):
                        self.last_update = value
                        self.last_update.value_namespace = name_space
                        self.last_update.value_namespace_prefix = name_space_prefix
                    if(value_path == "loop-filter-state"):
                        self.loop_filter_state = value
                        self.loop_filter_state.value_namespace = name_space
                        self.loop_filter_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "poll-interval"):
                        self.poll_interval = value
                        self.poll_interval.value_namespace = name_space
                        self.poll_interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-dispersion"):
                        self.sys_dispersion = value
                        self.sys_dispersion.value_namespace = name_space
                        self.sys_dispersion.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-leap"):
                        self.sys_leap = value
                        self.sys_leap.value_namespace = name_space
                        self.sys_leap.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-offset"):
                        self.sys_offset = value
                        self.sys_offset.value_namespace = name_space
                        self.sys_offset.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-precision"):
                        self.sys_precision = value
                        self.sys_precision.value_namespace = name_space
                        self.sys_precision.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-ref-id"):
                        self.sys_ref_id = value
                        self.sys_ref_id.value_namespace = name_space
                        self.sys_ref_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-root-delay"):
                        self.sys_root_delay = value
                        self.sys_root_delay.value_namespace = name_space
                        self.sys_root_delay.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-root-dispersion"):
                        self.sys_root_dispersion = value
                        self.sys_root_dispersion.value_namespace = name_space
                        self.sys_root_dispersion.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-stratum"):
                        self.sys_stratum = value
                        self.sys_stratum.value_namespace = name_space
                        self.sys_stratum.value_namespace_prefix = name_space_prefix


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

                    self.is_ntp_enabled = YLeaf(YType.boolean, "is-ntp-enabled")

                    self.sys_leap = YLeaf(YType.enumeration, "sys-leap")

                    self.peer_summary_info = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("is_ntp_enabled",
                                    "sys_leap") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ntp.Nodes.Node.Associations, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ntp.Nodes.Node.Associations, self).__setattr__(name, value)


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

                        self.time_since = YLeaf(YType.int32, "time-since")

                        self.peer_info_common = Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self._children_name_map["peer_info_common"] = "peer-info-common"
                        self._children_yang_names.add("peer-info-common")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("time_since") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ntp.Nodes.Node.Associations.PeerSummaryInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ntp.Nodes.Node.Associations.PeerSummaryInfo, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address",
                                            "delay",
                                            "dispersion",
                                            "host_mode",
                                            "host_poll",
                                            "is_configured",
                                            "is_sys_peer",
                                            "offset",
                                            "reachability",
                                            "reference_id",
                                            "status",
                                            "stratum") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address.is_set or
                                self.delay.is_set or
                                self.dispersion.is_set or
                                self.host_mode.is_set or
                                self.host_poll.is_set or
                                self.is_configured.is_set or
                                self.is_sys_peer.is_set or
                                self.offset.is_set or
                                self.reachability.is_set or
                                self.reference_id.is_set or
                                self.status.is_set or
                                self.stratum.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address.yfilter != YFilter.not_set or
                                self.delay.yfilter != YFilter.not_set or
                                self.dispersion.yfilter != YFilter.not_set or
                                self.host_mode.yfilter != YFilter.not_set or
                                self.host_poll.yfilter != YFilter.not_set or
                                self.is_configured.yfilter != YFilter.not_set or
                                self.is_sys_peer.yfilter != YFilter.not_set or
                                self.offset.yfilter != YFilter.not_set or
                                self.reachability.yfilter != YFilter.not_set or
                                self.reference_id.yfilter != YFilter.not_set or
                                self.status.yfilter != YFilter.not_set or
                                self.stratum.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peer-info-common" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address.get_name_leafdata())
                            if (self.delay.is_set or self.delay.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delay.get_name_leafdata())
                            if (self.dispersion.is_set or self.dispersion.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dispersion.get_name_leafdata())
                            if (self.host_mode.is_set or self.host_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_mode.get_name_leafdata())
                            if (self.host_poll.is_set or self.host_poll.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.host_poll.get_name_leafdata())
                            if (self.is_configured.is_set or self.is_configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_configured.get_name_leafdata())
                            if (self.is_sys_peer.is_set or self.is_sys_peer.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_sys_peer.get_name_leafdata())
                            if (self.offset.is_set or self.offset.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.offset.get_name_leafdata())
                            if (self.reachability.is_set or self.reachability.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reachability.get_name_leafdata())
                            if (self.reference_id.is_set or self.reference_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reference_id.get_name_leafdata())
                            if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status.get_name_leafdata())
                            if (self.stratum.is_set or self.stratum.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.stratum.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address" or name == "delay" or name == "dispersion" or name == "host-mode" or name == "host-poll" or name == "is-configured" or name == "is-sys-peer" or name == "offset" or name == "reachability" or name == "reference-id" or name == "status" or name == "stratum"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address"):
                                self.address = value
                                self.address.value_namespace = name_space
                                self.address.value_namespace_prefix = name_space_prefix
                            if(value_path == "delay"):
                                self.delay = value
                                self.delay.value_namespace = name_space
                                self.delay.value_namespace_prefix = name_space_prefix
                            if(value_path == "dispersion"):
                                self.dispersion = value
                                self.dispersion.value_namespace = name_space
                                self.dispersion.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-mode"):
                                self.host_mode = value
                                self.host_mode.value_namespace = name_space
                                self.host_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "host-poll"):
                                self.host_poll = value
                                self.host_poll.value_namespace = name_space
                                self.host_poll.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-configured"):
                                self.is_configured = value
                                self.is_configured.value_namespace = name_space
                                self.is_configured.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-sys-peer"):
                                self.is_sys_peer = value
                                self.is_sys_peer.value_namespace = name_space
                                self.is_sys_peer.value_namespace_prefix = name_space_prefix
                            if(value_path == "offset"):
                                self.offset = value
                                self.offset.value_namespace = name_space
                                self.offset.value_namespace_prefix = name_space_prefix
                            if(value_path == "reachability"):
                                self.reachability = value
                                self.reachability.value_namespace = name_space
                                self.reachability.value_namespace_prefix = name_space_prefix
                            if(value_path == "reference-id"):
                                self.reference_id = value
                                self.reference_id.value_namespace = name_space
                                self.reference_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "status"):
                                self.status = value
                                self.status.value_namespace = name_space
                                self.status.value_namespace_prefix = name_space_prefix
                            if(value_path == "stratum"):
                                self.stratum = value
                                self.stratum.value_namespace = name_space
                                self.stratum.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.time_since.is_set or
                            (self.peer_info_common is not None and self.peer_info_common.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.time_since.yfilter != YFilter.not_set or
                            (self.peer_info_common is not None and self.peer_info_common.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "peer-summary-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.time_since.is_set or self.time_since.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_since.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "peer-info-common"):
                            if (self.peer_info_common is None):
                                self.peer_info_common = Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon()
                                self.peer_info_common.parent = self
                                self._children_name_map["peer_info_common"] = "peer-info-common"
                            return self.peer_info_common

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer-info-common" or name == "time-since"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "time-since"):
                            self.time_since = value
                            self.time_since.value_namespace = name_space
                            self.time_since.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.peer_summary_info:
                        if (c.has_data()):
                            return True
                    return (
                        self.is_ntp_enabled.is_set or
                        self.sys_leap.is_set)

                def has_operation(self):
                    for c in self.peer_summary_info:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.is_ntp_enabled.yfilter != YFilter.not_set or
                        self.sys_leap.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "associations" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.is_ntp_enabled.is_set or self.is_ntp_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_ntp_enabled.get_name_leafdata())
                    if (self.sys_leap.is_set or self.sys_leap.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sys_leap.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "peer-summary-info"):
                        for c in self.peer_summary_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ntp.Nodes.Node.Associations.PeerSummaryInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.peer_summary_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "peer-summary-info" or name == "is-ntp-enabled" or name == "sys-leap"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "is-ntp-enabled"):
                        self.is_ntp_enabled = value
                        self.is_ntp_enabled.value_namespace = name_space
                        self.is_ntp_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "sys-leap"):
                        self.sys_leap = value
                        self.sys_leap.value_namespace = name_space
                        self.sys_leap.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node.is_set or
                    (self.associations is not None and self.associations.has_data()) or
                    (self.associations_detail is not None and self.associations_detail.has_data()) or
                    (self.status is not None and self.status.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node.yfilter != YFilter.not_set or
                    (self.associations is not None and self.associations.has_operation()) or
                    (self.associations_detail is not None and self.associations_detail.has_operation()) or
                    (self.status is not None and self.status.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node='" + self.node.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-ntp-oper:ntp/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "associations"):
                    if (self.associations is None):
                        self.associations = Ntp.Nodes.Node.Associations()
                        self.associations.parent = self
                        self._children_name_map["associations"] = "associations"
                    return self.associations

                if (child_yang_name == "associations-detail"):
                    if (self.associations_detail is None):
                        self.associations_detail = Ntp.Nodes.Node.AssociationsDetail()
                        self.associations_detail.parent = self
                        self._children_name_map["associations_detail"] = "associations-detail"
                    return self.associations_detail

                if (child_yang_name == "status"):
                    if (self.status is None):
                        self.status = Ntp.Nodes.Node.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                    return self.status

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "associations" or name == "associations-detail" or name == "status" or name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node"):
                    self.node = value
                    self.node.value_namespace = name_space
                    self.node.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-ntp-oper:ntp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ntp.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-ntp-oper:ntp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Ntp.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

