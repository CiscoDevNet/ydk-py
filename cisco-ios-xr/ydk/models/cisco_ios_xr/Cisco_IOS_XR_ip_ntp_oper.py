""" Cisco_IOS_XR_ip_ntp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-ntp package operational data.

This module contains definitions
for the following management objects\:
  ntp\: NTP operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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



class ClockUpdateNode(Enum):
    """
    ClockUpdateNode (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['ClockUpdateNode']


class NtpLeap(Enum):
    """
    NtpLeap (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpLeap']


class NtpLoopFilterState(Enum):
    """
    NtpLoopFilterState (Enum Class)

    Loop filter state

    .. data:: ntp_loop_flt_n_set = 1

    	 never set

    .. data:: ntp_loop_flt_f_set = 2

    	 drift set from file

    .. data:: ntp_loop_flt_spik = 3

    	 spike

    .. data:: ntp_loop_flt_freq = 4

    	 drift being measured

    .. data:: ntp_loop_flt_sync = 5

    	 normal controlled loop

    .. data:: ntp_loop_flt_unkn = 6

    	 unknown

    """

    ntp_loop_flt_n_set = Enum.YLeaf(1, "ntp-loop-flt-n-set")

    ntp_loop_flt_f_set = Enum.YLeaf(2, "ntp-loop-flt-f-set")

    ntp_loop_flt_spik = Enum.YLeaf(3, "ntp-loop-flt-spik")

    ntp_loop_flt_freq = Enum.YLeaf(4, "ntp-loop-flt-freq")

    ntp_loop_flt_sync = Enum.YLeaf(5, "ntp-loop-flt-sync")

    ntp_loop_flt_unkn = Enum.YLeaf(6, "ntp-loop-flt-unkn")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpLoopFilterState']


class NtpMode(Enum):
    """
    NtpMode (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpMode']


class NtpPeerStatus(Enum):
    """
    NtpPeerStatus (Enum Class)

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['NtpPeerStatus']



class Ntp(_Entity_):
    """
    NTP operational data
    
    .. attribute:: nodes
    
    	Node\-specific NTP operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ip-ntp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ntp, self).__init__()
        self._top_entity = None

        self.yang_name = "ntp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-ntp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Ntp.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Ntp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-ntp-oper:ntp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ntp, [], name, value)


    class Nodes(_Entity_):
        """
        Node\-specific NTP operational data
        
        .. attribute:: node
        
        	NTP operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ip-ntp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ntp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "ntp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Ntp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-oper:ntp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ntp.Nodes, [], name, value)


        class Node(_Entity_):
            """
            NTP operational data for a particular node
            
            .. attribute:: node  (key)
            
            	The node identifier
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: associations_detail
            
            	NTP Associations Detail information
            	**type**\:  :py:class:`AssociationsDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail>`
            
            	**config**\: False
            
            .. attribute:: status
            
            	Status of NTP peer(s)
            	**type**\:  :py:class:`Status <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status>`
            
            	**config**\: False
            
            .. attribute:: associations
            
            	NTP Associations information
            	**type**\:  :py:class:`Associations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations>`
            
            	**config**\: False
            
            

            """

            _prefix = 'ip-ntp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ntp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("associations-detail", ("associations_detail", Ntp.Nodes.Node.AssociationsDetail)), ("status", ("status", Ntp.Nodes.Node.Status)), ("associations", ("associations", Ntp.Nodes.Node.Associations))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.associations_detail = Ntp.Nodes.Node.AssociationsDetail()
                self.associations_detail.parent = self
                self._children_name_map["associations_detail"] = "associations-detail"

                self.status = Ntp.Nodes.Node.Status()
                self.status.parent = self
                self._children_name_map["status"] = "status"

                self.associations = Ntp.Nodes.Node.Associations()
                self.associations.parent = self
                self._children_name_map["associations"] = "associations"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-ntp-oper:ntp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ntp.Nodes.Node, ['node'], name, value)


            class AssociationsDetail(_Entity_):
                """
                NTP Associations Detail information
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sys_leap
                
                	Leap
                	**type**\:  :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                
                	**config**\: False
                
                .. attribute:: peer_detail_info
                
                	Peer info
                	**type**\: list of  		 :py:class:`PeerDetailInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ntp.Nodes.Node.AssociationsDetail, self).__init__()

                    self.yang_name = "associations-detail"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer-detail-info", ("peer_detail_info", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo))])
                    self._leafs = OrderedDict([
                        ('is_ntp_enabled', (YLeaf(YType.boolean, 'is-ntp-enabled'), ['bool'])),
                        ('sys_leap', (YLeaf(YType.enumeration, 'sys-leap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpLeap', '')])),
                    ])
                    self.is_ntp_enabled = None
                    self.sys_leap = None

                    self.peer_detail_info = YList(self)
                    self._segment_path = lambda: "associations-detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail, ['is_ntp_enabled', 'sys_leap'], name, value)


                class PeerDetailInfo(_Entity_):
                    """
                    Peer info
                    
                    .. attribute:: peer_info_common
                    
                    	Common peer info
                    	**type**\:  :py:class:`PeerInfoCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon>`
                    
                    	**config**\: False
                    
                    .. attribute:: ref_time
                    
                    	Reference time
                    	**type**\:  :py:class:`RefTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime>`
                    
                    	**config**\: False
                    
                    .. attribute:: originate_time
                    
                    	Originate timestamp
                    	**type**\:  :py:class:`OriginateTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime>`
                    
                    	**config**\: False
                    
                    .. attribute:: receive_time
                    
                    	Receive timestamp
                    	**type**\:  :py:class:`ReceiveTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime>`
                    
                    	**config**\: False
                    
                    .. attribute:: transmit_time
                    
                    	Transmit timestamp
                    	**type**\:  :py:class:`TransmitTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime>`
                    
                    	**config**\: False
                    
                    .. attribute:: leap
                    
                    	Leap
                    	**type**\:  :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                    
                    	**config**\: False
                    
                    .. attribute:: peer_mode
                    
                    	Peer's association mode
                    	**type**\:  :py:class:`NtpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpMode>`
                    
                    	**config**\: False
                    
                    .. attribute:: poll_interval
                    
                    	Peer poll interval
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: is_ref_clock
                    
                    	Is refclock
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_authenticated
                    
                    	Is authenticated
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: root_delay
                    
                    	Root delay
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: root_dispersion
                    
                    	Root dispersion
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: synch_distance
                    
                    	Synch distance
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: precision
                    
                    	Precision
                    	**type**\: int
                    
                    	**range:** \-128..127
                    
                    	**config**\: False
                    
                    .. attribute:: version
                    
                    	NTP version
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: filter_index
                    
                    	Index into filter shift register
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: cast_flags
                    
                    	Cast Flags
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: filter_detail
                    
                    	Filter Details
                    	**type**\: list of  		 :py:class:`FilterDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo, self).__init__()

                        self.yang_name = "peer-detail-info"
                        self.yang_parent_name = "associations-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("peer-info-common", ("peer_info_common", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon)), ("ref-time", ("ref_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime)), ("originate-time", ("originate_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime)), ("receive-time", ("receive_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime)), ("transmit-time", ("transmit_time", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime)), ("filter-detail", ("filter_detail", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail))])
                        self._leafs = OrderedDict([
                            ('leap', (YLeaf(YType.enumeration, 'leap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpLeap', '')])),
                            ('peer_mode', (YLeaf(YType.enumeration, 'peer-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpMode', '')])),
                            ('poll_interval', (YLeaf(YType.uint8, 'poll-interval'), ['int'])),
                            ('is_ref_clock', (YLeaf(YType.boolean, 'is-ref-clock'), ['bool'])),
                            ('is_authenticated', (YLeaf(YType.boolean, 'is-authenticated'), ['bool'])),
                            ('root_delay', (YLeaf(YType.str, 'root-delay'), ['str'])),
                            ('root_dispersion', (YLeaf(YType.str, 'root-dispersion'), ['str'])),
                            ('synch_distance', (YLeaf(YType.str, 'synch-distance'), ['str'])),
                            ('precision', (YLeaf(YType.int8, 'precision'), ['int'])),
                            ('version', (YLeaf(YType.uint8, 'version'), ['int'])),
                            ('filter_index', (YLeaf(YType.uint32, 'filter-index'), ['int'])),
                            ('cast_flags', (YLeaf(YType.uint8, 'cast-flags'), ['int'])),
                        ])
                        self.leap = None
                        self.peer_mode = None
                        self.poll_interval = None
                        self.is_ref_clock = None
                        self.is_authenticated = None
                        self.root_delay = None
                        self.root_dispersion = None
                        self.synch_distance = None
                        self.precision = None
                        self.version = None
                        self.filter_index = None
                        self.cast_flags = None

                        self.peer_info_common = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self._children_name_map["peer_info_common"] = "peer-info-common"

                        self.ref_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime()
                        self.ref_time.parent = self
                        self._children_name_map["ref_time"] = "ref-time"

                        self.originate_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime()
                        self.originate_time.parent = self
                        self._children_name_map["originate_time"] = "originate-time"

                        self.receive_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime()
                        self.receive_time.parent = self
                        self._children_name_map["receive_time"] = "receive-time"

                        self.transmit_time = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime()
                        self.transmit_time.parent = self
                        self._children_name_map["transmit_time"] = "transmit-time"

                        self.filter_detail = YList(self)
                        self._segment_path = lambda: "peer-detail-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo, ['leap', 'peer_mode', 'poll_interval', 'is_ref_clock', 'is_authenticated', 'root_delay', 'root_dispersion', 'synch_distance', 'precision', 'version', 'filter_index', 'cast_flags'], name, value)


                    class PeerInfoCommon(_Entity_):
                        """
                        Common peer info
                        
                        .. attribute:: host_mode
                        
                        	Association mode with this peer
                        	**type**\:  :py:class:`NtpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpMode>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_configured
                        
                        	Is configured
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: address
                        
                        	Peer Address
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: reference_id
                        
                        	Peer reference ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: host_poll
                        
                        	Host poll
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: reachability
                        
                        	Reachability
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: stratum
                        
                        	Peer stratum
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: status
                        
                        	Peer status
                        	**type**\:  :py:class:`NtpPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpPeerStatus>`
                        
                        	**config**\: False
                        
                        .. attribute:: delay
                        
                        	Peer delay
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: offset
                        
                        	Peer offset
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: dispersion
                        
                        	Peer dispersion
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: is_sys_peer
                        
                        	Indicates whether this is syspeer
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon, self).__init__()

                            self.yang_name = "peer-info-common"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('host_mode', (YLeaf(YType.enumeration, 'host-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpMode', '')])),
                                ('is_configured', (YLeaf(YType.boolean, 'is-configured'), ['bool'])),
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('reference_id', (YLeaf(YType.str, 'reference-id'), ['str'])),
                                ('host_poll', (YLeaf(YType.uint8, 'host-poll'), ['int'])),
                                ('reachability', (YLeaf(YType.uint8, 'reachability'), ['int'])),
                                ('stratum', (YLeaf(YType.uint8, 'stratum'), ['int'])),
                                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpPeerStatus', '')])),
                                ('delay', (YLeaf(YType.str, 'delay'), ['str'])),
                                ('offset', (YLeaf(YType.str, 'offset'), ['str'])),
                                ('dispersion', (YLeaf(YType.str, 'dispersion'), ['str'])),
                                ('is_sys_peer', (YLeaf(YType.boolean, 'is-sys-peer'), ['bool'])),
                            ])
                            self.host_mode = None
                            self.is_configured = None
                            self.address = None
                            self.reference_id = None
                            self.host_poll = None
                            self.reachability = None
                            self.stratum = None
                            self.status = None
                            self.delay = None
                            self.offset = None
                            self.dispersion = None
                            self.is_sys_peer = None
                            self._segment_path = lambda: "peer-info-common"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon, ['host_mode', 'is_configured', 'address', 'reference_id', 'host_poll', 'reachability', 'stratum', 'status', 'delay', 'offset', 'dispersion', 'is_sys_peer'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.PeerInfoCommon']['meta_info']


                    class RefTime(_Entity_):
                        """
                        Reference time
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec>`
                        
                        	**config**\: False
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime, self).__init__()

                            self.yang_name = "ref-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sec", ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec)), ("frac-secs", ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs))])
                            self._leafs = OrderedDict()

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._segment_path = lambda: "ref-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime, [], name, value)


                        class Sec(_Entity_):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "ref-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('int', (YLeaf(YType.uint32, 'int'), ['int'])),
                                ])
                                self.int = None
                                self._segment_path = lambda: "sec"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec, ['int'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.Sec']['meta_info']


                        class FracSecs(_Entity_):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "ref-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('frac', (YLeaf(YType.uint32, 'frac'), ['int'])),
                                ])
                                self.frac = None
                                self._segment_path = lambda: "frac-secs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs, ['frac'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime.FracSecs']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.RefTime']['meta_info']


                    class OriginateTime(_Entity_):
                        """
                        Originate timestamp
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec>`
                        
                        	**config**\: False
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime, self).__init__()

                            self.yang_name = "originate-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sec", ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec)), ("frac-secs", ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs))])
                            self._leafs = OrderedDict()

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._segment_path = lambda: "originate-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime, [], name, value)


                        class Sec(_Entity_):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "originate-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('int', (YLeaf(YType.uint32, 'int'), ['int'])),
                                ])
                                self.int = None
                                self._segment_path = lambda: "sec"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec, ['int'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.Sec']['meta_info']


                        class FracSecs(_Entity_):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "originate-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('frac', (YLeaf(YType.uint32, 'frac'), ['int'])),
                                ])
                                self.frac = None
                                self._segment_path = lambda: "frac-secs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs, ['frac'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime.FracSecs']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.OriginateTime']['meta_info']


                    class ReceiveTime(_Entity_):
                        """
                        Receive timestamp
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec>`
                        
                        	**config**\: False
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime, self).__init__()

                            self.yang_name = "receive-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sec", ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec)), ("frac-secs", ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs))])
                            self._leafs = OrderedDict()

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._segment_path = lambda: "receive-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime, [], name, value)


                        class Sec(_Entity_):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "receive-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('int', (YLeaf(YType.uint32, 'int'), ['int'])),
                                ])
                                self.int = None
                                self._segment_path = lambda: "sec"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec, ['int'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.Sec']['meta_info']


                        class FracSecs(_Entity_):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "receive-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('frac', (YLeaf(YType.uint32, 'frac'), ['int'])),
                                ])
                                self.frac = None
                                self._segment_path = lambda: "frac-secs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs, ['frac'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime.FracSecs']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.ReceiveTime']['meta_info']


                    class TransmitTime(_Entity_):
                        """
                        Transmit timestamp
                        
                        .. attribute:: sec
                        
                        	Second part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec>`
                        
                        	**config**\: False
                        
                        .. attribute:: frac_secs
                        
                        	Fractional part in 64\-bit NTP timestamp
                        	**type**\:  :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime, self).__init__()

                            self.yang_name = "transmit-time"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sec", ("sec", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec)), ("frac-secs", ("frac_secs", Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs))])
                            self._leafs = OrderedDict()

                            self.sec = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec()
                            self.sec.parent = self
                            self._children_name_map["sec"] = "sec"

                            self.frac_secs = Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs()
                            self.frac_secs.parent = self
                            self._children_name_map["frac_secs"] = "frac-secs"
                            self._segment_path = lambda: "transmit-time"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime, [], name, value)


                        class Sec(_Entity_):
                            """
                            Second part in 64\-bit NTP timestamp
                            
                            .. attribute:: int
                            
                            	Integer format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec, self).__init__()

                                self.yang_name = "sec"
                                self.yang_parent_name = "transmit-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('int', (YLeaf(YType.uint32, 'int'), ['int'])),
                                ])
                                self.int = None
                                self._segment_path = lambda: "sec"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec, ['int'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.Sec']['meta_info']


                        class FracSecs(_Entity_):
                            """
                            Fractional part in 64\-bit NTP timestamp
                            
                            .. attribute:: frac
                            
                            	Fractional format in NTP reference code
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'ip-ntp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs, self).__init__()

                                self.yang_name = "frac-secs"
                                self.yang_parent_name = "transmit-time"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('frac', (YLeaf(YType.uint32, 'frac'), ['int'])),
                                ])
                                self.frac = None
                                self._segment_path = lambda: "frac-secs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs, ['frac'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                                return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime.FracSecs']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.TransmitTime']['meta_info']


                    class FilterDetail(_Entity_):
                        """
                        Filter Details
                        
                        .. attribute:: filter_delay
                        
                        	filter delay
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: filter_offset
                        
                        	filter offset
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: filter_disp
                        
                        	filter disp
                        	**type**\: str
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail, self).__init__()

                            self.yang_name = "filter-detail"
                            self.yang_parent_name = "peer-detail-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('filter_delay', (YLeaf(YType.str, 'filter-delay'), ['str'])),
                                ('filter_offset', (YLeaf(YType.str, 'filter-offset'), ['str'])),
                                ('filter_disp', (YLeaf(YType.str, 'filter-disp'), ['str'])),
                            ])
                            self.filter_delay = None
                            self.filter_offset = None
                            self.filter_disp = None
                            self._segment_path = lambda: "filter-detail"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail, ['filter_delay', 'filter_offset', 'filter_disp'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo.FilterDetail']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail.PeerDetailInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                    return meta._meta_table['Ntp.Nodes.Node.AssociationsDetail']['meta_info']


            class Status(_Entity_):
                """
                Status of NTP peer(s)
                
                .. attribute:: sys_ref_time
                
                	Reference time
                	**type**\:  :py:class:`SysRefTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime>`
                
                	**config**\: False
                
                .. attribute:: sys_drift
                
                	System Drift
                	**type**\:  :py:class:`SysDrift <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift>`
                
                	**config**\: False
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sys_dispersion
                
                	Peer dispersion
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sys_offset
                
                	Clock offset
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: clock_period
                
                	Clock period in nanosecs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                	**units**\: nanosecond
                
                .. attribute:: sys_leap
                
                	leap
                	**type**\:  :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                
                	**config**\: False
                
                .. attribute:: sys_precision
                
                	Precision
                	**type**\: int
                
                	**range:** \-128..127
                
                	**config**\: False
                
                .. attribute:: sys_stratum
                
                	Stratum
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: sys_ref_id
                
                	Reference clock ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                	**config**\: False
                
                .. attribute:: sys_root_delay
                
                	Root delay
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: sys_root_dispersion
                
                	Root dispersion
                	**type**\: str
                
                	**config**\: False
                
                .. attribute:: loop_filter_state
                
                	Loop Filter State
                	**type**\:  :py:class:`NtpLoopFilterState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLoopFilterState>`
                
                	**config**\: False
                
                .. attribute:: poll_interval
                
                	Peer poll interval
                	**type**\: int
                
                	**range:** 0..255
                
                	**config**\: False
                
                .. attribute:: is_updated
                
                	Is clock updated
                	**type**\:  :py:class:`ClockUpdateNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.ClockUpdateNode>`
                
                	**config**\: False
                
                .. attribute:: last_update
                
                	Last Update
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                	**config**\: False
                
                .. attribute:: is_auth_enabled
                
                	Is NTP Authenticate enabled
                	**type**\: bool
                
                	**config**\: False
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ntp.Nodes.Node.Status, self).__init__()

                    self.yang_name = "status"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sys-ref-time", ("sys_ref_time", Ntp.Nodes.Node.Status.SysRefTime)), ("sys-drift", ("sys_drift", Ntp.Nodes.Node.Status.SysDrift))])
                    self._leafs = OrderedDict([
                        ('is_ntp_enabled', (YLeaf(YType.boolean, 'is-ntp-enabled'), ['bool'])),
                        ('sys_dispersion', (YLeaf(YType.str, 'sys-dispersion'), ['str'])),
                        ('sys_offset', (YLeaf(YType.str, 'sys-offset'), ['str'])),
                        ('clock_period', (YLeaf(YType.uint32, 'clock-period'), ['int'])),
                        ('sys_leap', (YLeaf(YType.enumeration, 'sys-leap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpLeap', '')])),
                        ('sys_precision', (YLeaf(YType.int8, 'sys-precision'), ['int'])),
                        ('sys_stratum', (YLeaf(YType.uint8, 'sys-stratum'), ['int'])),
                        ('sys_ref_id', (YLeaf(YType.str, 'sys-ref-id'), ['str'])),
                        ('sys_root_delay', (YLeaf(YType.str, 'sys-root-delay'), ['str'])),
                        ('sys_root_dispersion', (YLeaf(YType.str, 'sys-root-dispersion'), ['str'])),
                        ('loop_filter_state', (YLeaf(YType.enumeration, 'loop-filter-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpLoopFilterState', '')])),
                        ('poll_interval', (YLeaf(YType.uint8, 'poll-interval'), ['int'])),
                        ('is_updated', (YLeaf(YType.enumeration, 'is-updated'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'ClockUpdateNode', '')])),
                        ('last_update', (YLeaf(YType.int32, 'last-update'), ['int'])),
                        ('is_auth_enabled', (YLeaf(YType.boolean, 'is-auth-enabled'), ['bool'])),
                    ])
                    self.is_ntp_enabled = None
                    self.sys_dispersion = None
                    self.sys_offset = None
                    self.clock_period = None
                    self.sys_leap = None
                    self.sys_precision = None
                    self.sys_stratum = None
                    self.sys_ref_id = None
                    self.sys_root_delay = None
                    self.sys_root_dispersion = None
                    self.loop_filter_state = None
                    self.poll_interval = None
                    self.is_updated = None
                    self.last_update = None
                    self.is_auth_enabled = None

                    self.sys_ref_time = Ntp.Nodes.Node.Status.SysRefTime()
                    self.sys_ref_time.parent = self
                    self._children_name_map["sys_ref_time"] = "sys-ref-time"

                    self.sys_drift = Ntp.Nodes.Node.Status.SysDrift()
                    self.sys_drift.parent = self
                    self._children_name_map["sys_drift"] = "sys-drift"
                    self._segment_path = lambda: "status"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Nodes.Node.Status, ['is_ntp_enabled', 'sys_dispersion', 'sys_offset', 'clock_period', 'sys_leap', 'sys_precision', 'sys_stratum', 'sys_ref_id', 'sys_root_delay', 'sys_root_dispersion', 'loop_filter_state', 'poll_interval', 'is_updated', 'last_update', 'is_auth_enabled'], name, value)


                class SysRefTime(_Entity_):
                    """
                    Reference time
                    
                    .. attribute:: sec
                    
                    	Second part in 64\-bit NTP timestamp
                    	**type**\:  :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime.Sec>`
                    
                    	**config**\: False
                    
                    .. attribute:: frac_secs
                    
                    	Fractional part in 64\-bit NTP timestamp
                    	**type**\:  :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysRefTime.FracSecs>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ntp.Nodes.Node.Status.SysRefTime, self).__init__()

                        self.yang_name = "sys-ref-time"
                        self.yang_parent_name = "status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sec", ("sec", Ntp.Nodes.Node.Status.SysRefTime.Sec)), ("frac-secs", ("frac_secs", Ntp.Nodes.Node.Status.SysRefTime.FracSecs))])
                        self._leafs = OrderedDict()

                        self.sec = Ntp.Nodes.Node.Status.SysRefTime.Sec()
                        self.sec.parent = self
                        self._children_name_map["sec"] = "sec"

                        self.frac_secs = Ntp.Nodes.Node.Status.SysRefTime.FracSecs()
                        self.frac_secs.parent = self
                        self._children_name_map["frac_secs"] = "frac-secs"
                        self._segment_path = lambda: "sys-ref-time"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Nodes.Node.Status.SysRefTime, [], name, value)


                    class Sec(_Entity_):
                        """
                        Second part in 64\-bit NTP timestamp
                        
                        .. attribute:: int
                        
                        	Integer format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.Status.SysRefTime.Sec, self).__init__()

                            self.yang_name = "sec"
                            self.yang_parent_name = "sys-ref-time"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('int', (YLeaf(YType.uint32, 'int'), ['int'])),
                            ])
                            self.int = None
                            self._segment_path = lambda: "sec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysRefTime.Sec, ['int'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysRefTime.Sec']['meta_info']


                    class FracSecs(_Entity_):
                        """
                        Fractional part in 64\-bit NTP timestamp
                        
                        .. attribute:: frac
                        
                        	Fractional format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.Status.SysRefTime.FracSecs, self).__init__()

                            self.yang_name = "frac-secs"
                            self.yang_parent_name = "sys-ref-time"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('frac', (YLeaf(YType.uint32, 'frac'), ['int'])),
                            ])
                            self.frac = None
                            self._segment_path = lambda: "frac-secs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysRefTime.FracSecs, ['frac'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysRefTime.FracSecs']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.Status.SysRefTime']['meta_info']


                class SysDrift(_Entity_):
                    """
                    System Drift
                    
                    .. attribute:: sec
                    
                    	Second part in 64\-bit NTP timestamp
                    	**type**\:  :py:class:`Sec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift.Sec>`
                    
                    	**config**\: False
                    
                    .. attribute:: frac_secs
                    
                    	Fractional part in 64\-bit NTP timestamp
                    	**type**\:  :py:class:`FracSecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Status.SysDrift.FracSecs>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ntp.Nodes.Node.Status.SysDrift, self).__init__()

                        self.yang_name = "sys-drift"
                        self.yang_parent_name = "status"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sec", ("sec", Ntp.Nodes.Node.Status.SysDrift.Sec)), ("frac-secs", ("frac_secs", Ntp.Nodes.Node.Status.SysDrift.FracSecs))])
                        self._leafs = OrderedDict()

                        self.sec = Ntp.Nodes.Node.Status.SysDrift.Sec()
                        self.sec.parent = self
                        self._children_name_map["sec"] = "sec"

                        self.frac_secs = Ntp.Nodes.Node.Status.SysDrift.FracSecs()
                        self.frac_secs.parent = self
                        self._children_name_map["frac_secs"] = "frac-secs"
                        self._segment_path = lambda: "sys-drift"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Nodes.Node.Status.SysDrift, [], name, value)


                    class Sec(_Entity_):
                        """
                        Second part in 64\-bit NTP timestamp
                        
                        .. attribute:: int
                        
                        	Integer format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.Status.SysDrift.Sec, self).__init__()

                            self.yang_name = "sec"
                            self.yang_parent_name = "sys-drift"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('int', (YLeaf(YType.uint32, 'int'), ['int'])),
                            ])
                            self.int = None
                            self._segment_path = lambda: "sec"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysDrift.Sec, ['int'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysDrift.Sec']['meta_info']


                    class FracSecs(_Entity_):
                        """
                        Fractional part in 64\-bit NTP timestamp
                        
                        .. attribute:: frac
                        
                        	Fractional format in NTP reference code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.Status.SysDrift.FracSecs, self).__init__()

                            self.yang_name = "frac-secs"
                            self.yang_parent_name = "sys-drift"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('frac', (YLeaf(YType.uint32, 'frac'), ['int'])),
                            ])
                            self.frac = None
                            self._segment_path = lambda: "frac-secs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Status.SysDrift.FracSecs, ['frac'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Status.SysDrift.FracSecs']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.Status.SysDrift']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                    return meta._meta_table['Ntp.Nodes.Node.Status']['meta_info']


            class Associations(_Entity_):
                """
                NTP Associations information
                
                .. attribute:: is_ntp_enabled
                
                	Is NTP enabled
                	**type**\: bool
                
                	**config**\: False
                
                .. attribute:: sys_leap
                
                	Leap
                	**type**\:  :py:class:`NtpLeap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpLeap>`
                
                	**config**\: False
                
                .. attribute:: peer_summary_info
                
                	Peer info
                	**type**\: list of  		 :py:class:`PeerSummaryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations.PeerSummaryInfo>`
                
                	**config**\: False
                
                

                """

                _prefix = 'ip-ntp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ntp.Nodes.Node.Associations, self).__init__()

                    self.yang_name = "associations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("peer-summary-info", ("peer_summary_info", Ntp.Nodes.Node.Associations.PeerSummaryInfo))])
                    self._leafs = OrderedDict([
                        ('is_ntp_enabled', (YLeaf(YType.boolean, 'is-ntp-enabled'), ['bool'])),
                        ('sys_leap', (YLeaf(YType.enumeration, 'sys-leap'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpLeap', '')])),
                    ])
                    self.is_ntp_enabled = None
                    self.sys_leap = None

                    self.peer_summary_info = YList(self)
                    self._segment_path = lambda: "associations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ntp.Nodes.Node.Associations, ['is_ntp_enabled', 'sys_leap'], name, value)


                class PeerSummaryInfo(_Entity_):
                    """
                    Peer info
                    
                    .. attribute:: peer_info_common
                    
                    	Common peer info
                    	**type**\:  :py:class:`PeerInfoCommon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon>`
                    
                    	**config**\: False
                    
                    .. attribute:: time_since
                    
                    	Time since last frame received (\-1=none)
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'ip-ntp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Ntp.Nodes.Node.Associations.PeerSummaryInfo, self).__init__()

                        self.yang_name = "peer-summary-info"
                        self.yang_parent_name = "associations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("peer-info-common", ("peer_info_common", Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon))])
                        self._leafs = OrderedDict([
                            ('time_since', (YLeaf(YType.int32, 'time-since'), ['int'])),
                        ])
                        self.time_since = None

                        self.peer_info_common = Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon()
                        self.peer_info_common.parent = self
                        self._children_name_map["peer_info_common"] = "peer-info-common"
                        self._segment_path = lambda: "peer-summary-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ntp.Nodes.Node.Associations.PeerSummaryInfo, ['time_since'], name, value)


                    class PeerInfoCommon(_Entity_):
                        """
                        Common peer info
                        
                        .. attribute:: host_mode
                        
                        	Association mode with this peer
                        	**type**\:  :py:class:`NtpMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpMode>`
                        
                        	**config**\: False
                        
                        .. attribute:: is_configured
                        
                        	Is configured
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: address
                        
                        	Peer Address
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: reference_id
                        
                        	Peer reference ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: host_poll
                        
                        	Host poll
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: reachability
                        
                        	Reachability
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: stratum
                        
                        	Peer stratum
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: status
                        
                        	Peer status
                        	**type**\:  :py:class:`NtpPeerStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper.NtpPeerStatus>`
                        
                        	**config**\: False
                        
                        .. attribute:: delay
                        
                        	Peer delay
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: offset
                        
                        	Peer offset
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: dispersion
                        
                        	Peer dispersion
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: is_sys_peer
                        
                        	Indicates whether this is syspeer
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'ip-ntp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon, self).__init__()

                            self.yang_name = "peer-info-common"
                            self.yang_parent_name = "peer-summary-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('host_mode', (YLeaf(YType.enumeration, 'host-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpMode', '')])),
                                ('is_configured', (YLeaf(YType.boolean, 'is-configured'), ['bool'])),
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('reference_id', (YLeaf(YType.str, 'reference-id'), ['str'])),
                                ('host_poll', (YLeaf(YType.uint8, 'host-poll'), ['int'])),
                                ('reachability', (YLeaf(YType.uint8, 'reachability'), ['int'])),
                                ('stratum', (YLeaf(YType.uint8, 'stratum'), ['int'])),
                                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_oper', 'NtpPeerStatus', '')])),
                                ('delay', (YLeaf(YType.str, 'delay'), ['str'])),
                                ('offset', (YLeaf(YType.str, 'offset'), ['str'])),
                                ('dispersion', (YLeaf(YType.str, 'dispersion'), ['str'])),
                                ('is_sys_peer', (YLeaf(YType.boolean, 'is-sys-peer'), ['bool'])),
                            ])
                            self.host_mode = None
                            self.is_configured = None
                            self.address = None
                            self.reference_id = None
                            self.host_poll = None
                            self.reachability = None
                            self.stratum = None
                            self.status = None
                            self.delay = None
                            self.offset = None
                            self.dispersion = None
                            self.is_sys_peer = None
                            self._segment_path = lambda: "peer-info-common"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon, ['host_mode', 'is_configured', 'address', 'reference_id', 'host_poll', 'reachability', 'stratum', 'status', 'delay', 'offset', 'dispersion', 'is_sys_peer'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                            return meta._meta_table['Ntp.Nodes.Node.Associations.PeerSummaryInfo.PeerInfoCommon']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                        return meta._meta_table['Ntp.Nodes.Node.Associations.PeerSummaryInfo']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                    return meta._meta_table['Ntp.Nodes.Node.Associations']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
                return meta._meta_table['Ntp.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
            return meta._meta_table['Ntp.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ntp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_ntp_oper as meta
        return meta._meta_table['Ntp']['meta_info']


