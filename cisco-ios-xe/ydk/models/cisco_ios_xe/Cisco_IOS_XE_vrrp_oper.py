""" Cisco_IOS_XE_vrrp_oper 

This module contains a collection of YANG
definitions for VRRP operational data.
Copyright (c) 2017\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MasterReason(Enum):
    """
    MasterReason (Enum Class)

    Indicates why this router became master of the VRRP group

    .. data:: reason_not_master = 0

    	Router is not in master state

    .. data:: reason_priority = 1

    	Won the Master election due to higher priority

    .. data:: reason_preempt = 2

    	Preempted a lower priority Master router

    .. data:: reason_master_no_response = 3

    	Master router stopped responding

    """

    reason_not_master = Enum.YLeaf(0, "reason-not-master")

    reason_priority = Enum.YLeaf(1, "reason-priority")

    reason_preempt = Enum.YLeaf(2, "reason-preempt")

    reason_master_no_response = Enum.YLeaf(3, "reason-master-no-response")


class OmpStateUpdown(Enum):
    """
    OmpStateUpdown (Enum Class)

    Indicates the state of the Overlay Management Protocol tracking

    .. data:: omp_up = 0

    	Indicates OMP track is up

    .. data:: omp_down = 1

    	Indicates OMP track is down

    """

    omp_up = Enum.YLeaf(0, "omp-up")

    omp_down = Enum.YLeaf(1, "omp-down")


class ProtoVersion(Enum):
    """
    ProtoVersion (Enum Class)

    VRRP protocol version

    .. data:: vrrp_v3 = 1

    """

    vrrp_v3 = Enum.YLeaf(1, "vrrp-v3")


class TrackState(Enum):
    """
    TrackState (Enum Class)

    Indicates whether the track is resolved

    .. data:: vrrp_track_state_resolved = 0

    	Track is resolved

    .. data:: vrrp_track_state_unresolved = 1

    	Track is unresolved

    """

    vrrp_track_state_resolved = Enum.YLeaf(0, "vrrp-track-state-resolved")

    vrrp_track_state_unresolved = Enum.YLeaf(1, "vrrp-track-state-unresolved")


class VrrpProtoState(Enum):
    """
    VrrpProtoState (Enum Class)

    VRRP group state

    .. data:: proto_state_init = 1

    	Indicates that the virtual router group is waiting for a startup event

    .. data:: proto_state_backup = 2

    	Indicates that the virtual router is monitoring the availability of a master

    .. data:: proto_state_master = 3

    	Indicates that the virtual router is forwarding packets for IP addresses that are associated with this router

    .. data:: proto_state_recover = 4

    	Indicates that the virtual router is under recovery

    """

    proto_state_init = Enum.YLeaf(1, "proto-state-init")

    proto_state_backup = Enum.YLeaf(2, "proto-state-backup")

    proto_state_master = Enum.YLeaf(3, "proto-state-master")

    proto_state_recover = Enum.YLeaf(4, "proto-state-recover")



class VrrpOperData(Entity):
    """
    VRRP operational data
    
    .. attribute:: vrrp_oper_state
    
    	VRRP operational state
    	**type**\: list of  		 :py:class:`VrrpOperState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.VrrpOperData.VrrpOperState>`
    
    

    """

    _prefix = 'vrrp-ios-xe-oper'
    _revision = '2017-12-01'

    def __init__(self):
        super(VrrpOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "vrrp-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-vrrp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("vrrp-oper-state", ("vrrp_oper_state", VrrpOperData.VrrpOperState))])
        self._leafs = OrderedDict()

        self.vrrp_oper_state = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-vrrp-oper:vrrp-oper-data"

    def __setattr__(self, name, value):
        self._perform_setattr(VrrpOperData, [], name, value)


    class VrrpOperState(Entity):
        """
        VRRP operational state
        
        .. attribute:: if_number  (key)
        
        	IfIndex for the interface on which VRRP group is hosted
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: group_id  (key)
        
        	VRRP group number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: addr_type  (key)
        
        	Address family of VRRP group. IPv4 or IPv6 are the two valid values
        	**type**\:  :py:class:`AddrType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_common_types.AddrType>`
        
        .. attribute:: version
        
        	VRRP version
        	**type**\:  :py:class:`ProtoVersion <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.ProtoVersion>`
        
        .. attribute:: virtual_ip
        
        	Primary Virtual IP address for the VRRP group
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: if_name
        
        	Name for the interface on which VRRP group is hosted
        	**type**\: str
        
        .. attribute:: vrrp_state
        
        	VRRP group state
        	**type**\:  :py:class:`VrrpProtoState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.VrrpProtoState>`
        
        .. attribute:: virtual_mac
        
        	Virtual MAC address for the VRRP group
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: master_ip
        
        	IP address of the Master router for the VRRP group
        	**type**\: union of the below types:
        
        		**type**\: str
        
        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        		**type**\: str
        
        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
        
        .. attribute:: is_owner
        
        	Whether the router owns the VRRP Primary virtual IP address. When Interface IP address and VRRP Primary virtual IP address are the same for this router, its priority is bumped up to 255
        	**type**\: bool
        
        .. attribute:: priority
        
        	Specifies the priority value used for VRRP master election process. Valid values are 0 to 255. 0 is used by a current master router to gracefully retire from the vrrp group. 255 indicates the master router also owns the VRRP virtual IP address
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: advertisement_timer
        
        	Time interval between hello packets sent by the master router in milliseconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: master_down_timer
        
        	Time after which a backup router declares the current master to be down in milliseconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: skew_time
        
        	Time to skew Master Down Interval in milliseconds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: preempt
        
        	Controls whether a higher priority virtual router will preempt a lower priority master
        	**type**\: bool
        
        .. attribute:: master_transitions
        
        	Number of master transitions that have happened in the VRRP group
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: new_master_reason
        
        	Indicates why this router became master of the VRRP group
        	**type**\:  :py:class:`MasterReason <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.MasterReason>`
        
        .. attribute:: last_state_change_time
        
        	Time when state of the VRRP group last changed
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: adv_interval_errors
        
        	Total number of VRRP packets that arrived with advertisement interval different to the configured value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ip_ttl_errors
        
        	Total number of VRRP packets received by the virtual router with IPv4 TTL (for VRRP over IPv4) or IPv6 Hop Limit (for VRRP over IPv6) not equal to 255
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: rcvd_pri_zero_pak
        
        	Total number of VRRP packets received with priority 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sent_pri_zero_pak
        
        	Total number of VRRP packets sent with priority 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: rcvd_invalid_type_pak
        
        	Total number of VRRP packets received with invalid Type field
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: addr_list_errors
        
        	Total number of VRRP packets received with address not matching the address list locally configured on the router
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: pak_len_errors
        
        	Total number of VRRP packets received with length less that VRRP header length
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: discontinuity_time
        
        	Indicates the last time when a discontinuity happened in gathering statistics
        	**type**\: str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: advertisement_sent
        
        	Total number of VRRP packets sent
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: advertisement_rcvd
        
        	Total number of VRRP packets received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: track_list
        
        	Status of list of tracking objects in the group
        	**type**\: list of  		 :py:class:`TrackList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.VrrpOperData.VrrpOperState.TrackList>`
        
        .. attribute:: omp_state
        
        	Indicates the state of the Overlay Management protocol tracking
        	**type**\:  :py:class:`OmpStateUpdown <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.OmpStateUpdown>`
        
        

        """

        _prefix = 'vrrp-ios-xe-oper'
        _revision = '2017-12-01'

        def __init__(self):
            super(VrrpOperData.VrrpOperState, self).__init__()

            self.yang_name = "vrrp-oper-state"
            self.yang_parent_name = "vrrp-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['if_number','group_id','addr_type']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("track-list", ("track_list", VrrpOperData.VrrpOperState.TrackList))])
            self._leafs = OrderedDict([
                ('if_number', YLeaf(YType.uint32, 'if-number')),
                ('group_id', YLeaf(YType.uint32, 'group-id')),
                ('addr_type', YLeaf(YType.enumeration, 'addr-type')),
                ('version', YLeaf(YType.enumeration, 'version')),
                ('virtual_ip', YLeaf(YType.str, 'virtual-ip')),
                ('if_name', YLeaf(YType.str, 'if-name')),
                ('vrrp_state', YLeaf(YType.enumeration, 'vrrp-state')),
                ('virtual_mac', YLeaf(YType.str, 'virtual-mac')),
                ('master_ip', YLeaf(YType.str, 'master-ip')),
                ('is_owner', YLeaf(YType.boolean, 'is-owner')),
                ('priority', YLeaf(YType.uint32, 'priority')),
                ('advertisement_timer', YLeaf(YType.uint32, 'advertisement-timer')),
                ('master_down_timer', YLeaf(YType.uint32, 'master-down-timer')),
                ('skew_time', YLeaf(YType.uint32, 'skew-time')),
                ('preempt', YLeaf(YType.boolean, 'preempt')),
                ('master_transitions', YLeaf(YType.uint32, 'master-transitions')),
                ('new_master_reason', YLeaf(YType.enumeration, 'new-master-reason')),
                ('last_state_change_time', YLeaf(YType.str, 'last-state-change-time')),
                ('adv_interval_errors', YLeaf(YType.uint32, 'adv-interval-errors')),
                ('ip_ttl_errors', YLeaf(YType.uint32, 'ip-ttl-errors')),
                ('rcvd_pri_zero_pak', YLeaf(YType.uint32, 'rcvd-pri-zero-pak')),
                ('sent_pri_zero_pak', YLeaf(YType.uint32, 'sent-pri-zero-pak')),
                ('rcvd_invalid_type_pak', YLeaf(YType.uint32, 'rcvd-invalid-type-pak')),
                ('addr_list_errors', YLeaf(YType.uint32, 'addr-list-errors')),
                ('pak_len_errors', YLeaf(YType.uint32, 'pak-len-errors')),
                ('discontinuity_time', YLeaf(YType.str, 'discontinuity-time')),
                ('advertisement_sent', YLeaf(YType.uint32, 'advertisement-sent')),
                ('advertisement_rcvd', YLeaf(YType.uint32, 'advertisement-rcvd')),
                ('omp_state', YLeaf(YType.enumeration, 'omp-state')),
            ])
            self.if_number = None
            self.group_id = None
            self.addr_type = None
            self.version = None
            self.virtual_ip = None
            self.if_name = None
            self.vrrp_state = None
            self.virtual_mac = None
            self.master_ip = None
            self.is_owner = None
            self.priority = None
            self.advertisement_timer = None
            self.master_down_timer = None
            self.skew_time = None
            self.preempt = None
            self.master_transitions = None
            self.new_master_reason = None
            self.last_state_change_time = None
            self.adv_interval_errors = None
            self.ip_ttl_errors = None
            self.rcvd_pri_zero_pak = None
            self.sent_pri_zero_pak = None
            self.rcvd_invalid_type_pak = None
            self.addr_list_errors = None
            self.pak_len_errors = None
            self.discontinuity_time = None
            self.advertisement_sent = None
            self.advertisement_rcvd = None
            self.omp_state = None

            self.track_list = YList(self)
            self._segment_path = lambda: "vrrp-oper-state" + "[if-number='" + str(self.if_number) + "']" + "[group-id='" + str(self.group_id) + "']" + "[addr-type='" + str(self.addr_type) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-vrrp-oper:vrrp-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(VrrpOperData.VrrpOperState, ['if_number', 'group_id', 'addr_type', 'version', 'virtual_ip', 'if_name', 'vrrp_state', 'virtual_mac', 'master_ip', 'is_owner', 'priority', 'advertisement_timer', 'master_down_timer', 'skew_time', 'preempt', 'master_transitions', 'new_master_reason', 'last_state_change_time', 'adv_interval_errors', 'ip_ttl_errors', 'rcvd_pri_zero_pak', 'sent_pri_zero_pak', 'rcvd_invalid_type_pak', 'addr_list_errors', 'pak_len_errors', 'discontinuity_time', 'advertisement_sent', 'advertisement_rcvd', 'omp_state'], name, value)


        class TrackList(Entity):
            """
            Status of list of tracking objects in the group
            
            .. attribute:: track_name
            
            	Name of the tracking object
            	**type**\: str
            
            .. attribute:: track_obj_state
            
            	State of the tracking object
            	**type**\:  :py:class:`TrackState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_vrrp_oper.TrackState>`
            
            

            """

            _prefix = 'vrrp-ios-xe-oper'
            _revision = '2017-12-01'

            def __init__(self):
                super(VrrpOperData.VrrpOperState.TrackList, self).__init__()

                self.yang_name = "track-list"
                self.yang_parent_name = "vrrp-oper-state"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('track_name', YLeaf(YType.str, 'track-name')),
                    ('track_obj_state', YLeaf(YType.enumeration, 'track-obj-state')),
                ])
                self.track_name = None
                self.track_obj_state = None
                self._segment_path = lambda: "track-list"

            def __setattr__(self, name, value):
                self._perform_setattr(VrrpOperData.VrrpOperState.TrackList, ['track_name', 'track_obj_state'], name, value)

    def clone_ptr(self):
        self._top_entity = VrrpOperData()
        return self._top_entity

