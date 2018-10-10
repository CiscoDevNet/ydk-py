""" Cisco_IOS_XR_manageability_object_tracking_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package operational data.

This module contains definitions
for the following management objects\:
  object\-tracking\: Object Tracking operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Track(Enum):
    """
    Track (Enum Class)

    Track

    .. data:: interface_type = 1

    	Line protocol type

    .. data:: route_type = 2

    	Route type

    .. data:: bool_and_type = 3

    	Boolean and type

    .. data:: bool_or_type = 4

    	Boolean or type

    .. data:: ipsla_type = 5

    	Ipsla track type

    .. data:: undefined_type = 6

    	type undefined

    .. data:: threshold_weight = 7

    	type threshold weight

    .. data:: threshold_percentage = 8

    	type threshold percentage

    .. data:: bfd_type = 9

    	type bfd rtr

    """

    interface_type = Enum.YLeaf(1, "interface-type")

    route_type = Enum.YLeaf(2, "route-type")

    bool_and_type = Enum.YLeaf(3, "bool-and-type")

    bool_or_type = Enum.YLeaf(4, "bool-or-type")

    ipsla_type = Enum.YLeaf(5, "ipsla-type")

    undefined_type = Enum.YLeaf(6, "undefined-type")

    threshold_weight = Enum.YLeaf(7, "threshold-weight")

    threshold_percentage = Enum.YLeaf(8, "threshold-percentage")

    bfd_type = Enum.YLeaf(9, "bfd-type")



class ObjectTracking(Entity):
    """
    Object Tracking operational data
    
    .. attribute:: track_type_interface
    
    	Object Tracking Type interface info
    	**type**\:  :py:class:`TrackTypeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface>`
    
    .. attribute:: track_briefs
    
    	Object Tracking Track table brief
    	**type**\:  :py:class:`TrackBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs>`
    
    .. attribute:: track_type_rtr_reachability
    
    	Object Tracking Type RTR Reachability info
    	**type**\:  :py:class:`TrackTypeRtrReachability <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability>`
    
    .. attribute:: track_type_rtr_reachability_brief
    
    	Object Tracking Type RTR Reachability brief info
    	**type**\:  :py:class:`TrackTypeRtrReachabilityBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief>`
    
    .. attribute:: tracks
    
    	Object Tracking Track table
    	**type**\:  :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks>`
    
    .. attribute:: track_type_ipv4_route_brief
    
    	Object Tracking Type Ipv4 Route brief info
    	**type**\:  :py:class:`TrackTypeIpv4RouteBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief>`
    
    .. attribute:: track_type_ipv4_route
    
    	Object Tracking Type IPV4 route info
    	**type**\:  :py:class:`TrackTypeIpv4Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route>`
    
    .. attribute:: track_type_interface_brief
    
    	Object Tracking Type Interface brief info
    	**type**\:  :py:class:`TrackTypeInterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief>`
    
    

    """

    _prefix = 'manageability-object-tracking-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ObjectTracking, self).__init__()
        self._top_entity = None

        self.yang_name = "object-tracking"
        self.yang_parent_name = "Cisco-IOS-XR-manageability-object-tracking-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("track-type-interface", ("track_type_interface", ObjectTracking.TrackTypeInterface)), ("track-briefs", ("track_briefs", ObjectTracking.TrackBriefs)), ("track-type-rtr-reachability", ("track_type_rtr_reachability", ObjectTracking.TrackTypeRtrReachability)), ("track-type-rtr-reachability-brief", ("track_type_rtr_reachability_brief", ObjectTracking.TrackTypeRtrReachabilityBrief)), ("tracks", ("tracks", ObjectTracking.Tracks)), ("track-type-ipv4-route-brief", ("track_type_ipv4_route_brief", ObjectTracking.TrackTypeIpv4RouteBrief)), ("track-type-ipv4-route", ("track_type_ipv4_route", ObjectTracking.TrackTypeIpv4Route)), ("track-type-interface-brief", ("track_type_interface_brief", ObjectTracking.TrackTypeInterfaceBrief))])
        self._leafs = OrderedDict()

        self.track_type_interface = ObjectTracking.TrackTypeInterface()
        self.track_type_interface.parent = self
        self._children_name_map["track_type_interface"] = "track-type-interface"

        self.track_briefs = ObjectTracking.TrackBriefs()
        self.track_briefs.parent = self
        self._children_name_map["track_briefs"] = "track-briefs"

        self.track_type_rtr_reachability = ObjectTracking.TrackTypeRtrReachability()
        self.track_type_rtr_reachability.parent = self
        self._children_name_map["track_type_rtr_reachability"] = "track-type-rtr-reachability"

        self.track_type_rtr_reachability_brief = ObjectTracking.TrackTypeRtrReachabilityBrief()
        self.track_type_rtr_reachability_brief.parent = self
        self._children_name_map["track_type_rtr_reachability_brief"] = "track-type-rtr-reachability-brief"

        self.tracks = ObjectTracking.Tracks()
        self.tracks.parent = self
        self._children_name_map["tracks"] = "tracks"

        self.track_type_ipv4_route_brief = ObjectTracking.TrackTypeIpv4RouteBrief()
        self.track_type_ipv4_route_brief.parent = self
        self._children_name_map["track_type_ipv4_route_brief"] = "track-type-ipv4-route-brief"

        self.track_type_ipv4_route = ObjectTracking.TrackTypeIpv4Route()
        self.track_type_ipv4_route.parent = self
        self._children_name_map["track_type_ipv4_route"] = "track-type-ipv4-route"

        self.track_type_interface_brief = ObjectTracking.TrackTypeInterfaceBrief()
        self.track_type_interface_brief.parent = self
        self._children_name_map["track_type_interface_brief"] = "track-type-interface-brief"
        self._segment_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ObjectTracking, [], name, value)


    class TrackTypeInterface(Entity):
        """
        Object Tracking Type interface info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of  		 :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeInterface, self).__init__()

            self.yang_name = "track-type-interface"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-info", ("track_info", ObjectTracking.TrackTypeInterface.TrackInfo))])
            self._leafs = OrderedDict()

            self.track_info = YList(self)
            self._segment_path = lambda: "track-type-interface"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeInterface, [], name, value)


        class TrackInfo(Entity):
            """
            track info
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo>`
            
            .. attribute:: bool_tracks
            
            	boolean objects
            	**type**\:  :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks>`
            
            .. attribute:: threshold_tracks
            
            	Threshold objects
            	**type**\:  :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks>`
            
            .. attribute:: tracking_interaces
            
            	Tracking Interfaces
            	**type**\:  :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces>`
            
            .. attribute:: delayed
            
            	Is the state change delay counter in progress
            	**type**\:  :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.Delayed>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\: str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            .. attribute:: track_state
            
            	Track state
            	**type**\: bool
            
            .. attribute:: state_change_counter
            
            	State Change Counter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: seconds_last_change
            
            	Seconds Last Change
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: threshold_up
            
            	User specified threshold upper limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_down
            
            	User specified threshold lower limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeInterface.TrackInfo, self).__init__()

                self.yang_name = "track-info"
                self.yang_parent_name = "track-type-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo)), ("bool-tracks", ("bool_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks)), ("threshold-tracks", ("threshold_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks)), ("tracking-interaces", ("tracking_interaces", ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces)), ("delayed", ("delayed", ObjectTracking.TrackTypeInterface.TrackInfo.Delayed))])
                self._leafs = OrderedDict([
                    ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ('state_change_counter', (YLeaf(YType.uint32, 'state-change-counter'), ['int'])),
                    ('seconds_last_change', (YLeaf(YType.uint64, 'seconds-last-change'), ['int'])),
                    ('threshold_up', (YLeaf(YType.uint32, 'threshold-up'), ['int'])),
                    ('threshold_down', (YLeaf(YType.uint32, 'threshold-down'), ['int'])),
                ])
                self.tracke_name = None
                self.type = None
                self.track_state = None
                self.state_change_counter = None
                self.seconds_last_change = None
                self.threshold_up = None
                self.threshold_down = None

                self.track_type_info = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"

                self.bool_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self._children_name_map["bool_tracks"] = "bool-tracks"

                self.threshold_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self._children_name_map["threshold_tracks"] = "threshold-tracks"

                self.tracking_interaces = ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self._children_name_map["tracking_interaces"] = "tracking-interaces"

                self.delayed = ObjectTracking.TrackTypeInterface.TrackInfo.Delayed()
                self.delayed.parent = self
                self._children_name_map["delayed"] = "delayed"
                self._segment_path = lambda: "track-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo, ['tracke_name', 'type', 'track_state', 'state_change_counter', 'seconds_last_change', 'threshold_up', 'threshold_down'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks))])
                    self._leafs = OrderedDict([
                        ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ])
                    self.discriminant = None

                    self.interface_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"

                    self.route_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"

                    self.ipsla_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                    self.bfd_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__init__()

                        self.yang_name = "interface-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks, self).__init__()

                        self.yang_name = "route-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None
                        self.next_hop = None
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks, self).__init__()

                        self.yang_name = "ipsla-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                            ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                            ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                        ])
                        self.ipsla_op_id = None
                        self.rtt = None
                        self.return_code = None
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks, self).__init__()

                        self.yang_name = "bfd-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.destination_address = None
                        self.rate = None
                        self.debounce_count = None
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


            class BoolTracks(Entity):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of  		 :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks, self).__init__()

                    self.yang_name = "bool-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bool-track-info", ("bool_track_info", ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo))])
                    self._leafs = OrderedDict()

                    self.bool_track_info = YList(self)
                    self._segment_path = lambda: "bool-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks, [], name, value)


                class BoolTrackInfo(Entity):
                    """
                    bool track info
                    
                    .. attribute:: object_name
                    
                    	Object Name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state
                    	**type**\: bool
                    
                    .. attribute:: with_not
                    
                    	Track object with Not
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                        self.yang_name = "bool-track-info"
                        self.yang_parent_name = "bool-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                            ('with_not', (YLeaf(YType.boolean, 'with-not'), ['bool'])),
                        ])
                        self.object_name = None
                        self.track_state = None
                        self.with_not = None
                        self._segment_path = lambda: "bool-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/bool-tracks/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


            class ThresholdTracks(Entity):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of  		 :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks, self).__init__()

                    self.yang_name = "threshold-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("threshold-track-info", ("threshold_track_info", ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo))])
                    self._leafs = OrderedDict()

                    self.threshold_track_info = YList(self)
                    self._segment_path = lambda: "threshold-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks, [], name, value)


                class ThresholdTrackInfo(Entity):
                    """
                    threshold track info
                    
                    .. attribute:: object_name
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state. True means track is up; False means track is down
                    	**type**\: bool
                    
                    .. attribute:: weight
                    
                    	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__init__()

                        self.yang_name = "threshold-track-info"
                        self.yang_parent_name = "threshold-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                        ])
                        self.object_name = None
                        self.track_state = None
                        self.weight = None
                        self._segment_path = lambda: "threshold-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/threshold-tracks/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


            class TrackingInteraces(Entity):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of  		 :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces, self).__init__()

                    self.yang_name = "tracking-interaces"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracking-info", ("interface_tracking_info", ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo))])
                    self._leafs = OrderedDict()

                    self.interface_tracking_info = YList(self)
                    self._segment_path = lambda: "tracking-interaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces, [], name, value)


                class InterfaceTrackingInfo(Entity):
                    """
                    interface tracking info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__init__()

                        self.yang_name = "interface-tracking-info"
                        self.yang_parent_name = "tracking-interaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracking-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/tracking-interaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


            class Delayed(Entity):
                """
                Is the state change delay counter in progress
                
                .. attribute:: time_remaining
                
                	The time remaining in seconds for the counter to trigger state change
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: track_state
                
                	State the track will transition to. Track state. True means track is up; False means track is down
                	**type**\: bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.Delayed, self).__init__()

                    self.yang_name = "delayed"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                        ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ])
                    self.time_remaining = None
                    self.track_state = None
                    self._segment_path = lambda: "delayed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


    class TrackBriefs(Entity):
        """
        Object Tracking Track table brief
        
        .. attribute:: track_brief
        
        	Track name \- maximum 32 characters
        	**type**\: list of  		 :py:class:`TrackBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackBriefs, self).__init__()

            self.yang_name = "track-briefs"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-brief", ("track_brief", ObjectTracking.TrackBriefs.TrackBrief))])
            self._leafs = OrderedDict()

            self.track_brief = YList(self)
            self._segment_path = lambda: "track-briefs"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackBriefs, [], name, value)


        class TrackBrief(Entity):
            """
            Track name \- maximum 32 characters
            
            .. attribute:: track_name  (key)
            
            	Track name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: track_info_brief
            
            	track info brief
            	**type**\: list of  		 :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackBriefs.TrackBrief, self).__init__()

                self.yang_name = "track-brief"
                self.yang_parent_name = "track-briefs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['track_name']
                self._child_classes = OrderedDict([("track-info-brief", ("track_info_brief", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief))])
                self._leafs = OrderedDict([
                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                ])
                self.track_name = None

                self.track_info_brief = YList(self)
                self._segment_path = lambda: "track-brief" + "[track-name='" + str(self.track_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-briefs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief, ['track_name'], name, value)


            class TrackInfoBrief(Entity):
                """
                track info brief
                
                .. attribute:: track_type_info
                
                	Track type information
                	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo>`
                
                .. attribute:: tracke_name
                
                	Track Name
                	**type**\: str
                
                	**length:** 0..33
                
                .. attribute:: type
                
                	Track type
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: track_state
                
                	Track state
                	**type**\: bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief, self).__init__()

                    self.yang_name = "track-info-brief"
                    self.yang_parent_name = "track-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo))])
                    self._leafs = OrderedDict([
                        ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                        ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ])
                    self.tracke_name = None
                    self.type = None
                    self.track_state = None

                    self.track_type_info = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self._children_name_map["track_type_info"] = "track-type-info"
                    self._segment_path = lambda: "track-info-brief"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief, ['tracke_name', 'type', 'track_state'], name, value)


                class TrackTypeInfo(Entity):
                    """
                    Track type information
                    
                    .. attribute:: interface_tracks
                    
                    	track type interface info
                    	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                    
                    .. attribute:: route_tracks
                    
                    	track type route info
                    	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                    
                    .. attribute:: ipsla_tracks
                    
                    	track type rtr info
                    	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                    
                    .. attribute:: bfd_tracks
                    
                    	track type bfdrtr info
                    	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                    
                    .. attribute:: discriminant
                    
                    	discriminant
                    	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                        self.yang_name = "track-type-info"
                        self.yang_parent_name = "track-info-brief"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks))])
                        self._leafs = OrderedDict([
                            ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                        ])
                        self.discriminant = None

                        self.interface_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                        self.interface_tracks.parent = self
                        self._children_name_map["interface_tracks"] = "interface-tracks"

                        self.route_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                        self.route_tracks.parent = self
                        self._children_name_map["route_tracks"] = "route-tracks"

                        self.ipsla_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                        self.ipsla_tracks.parent = self
                        self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                        self.bfd_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                        self.bfd_tracks.parent = self
                        self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        self._segment_path = lambda: "track-type-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                    class InterfaceTracks(Entity):
                        """
                        track type interface info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__init__()

                            self.yang_name = "interface-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self._segment_path = lambda: "interface-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                    class RouteTracks(Entity):
                        """
                        track type route info
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf
                        
                        	VRF Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        .. attribute:: next_hop
                        
                        	Next Hop
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__init__()

                            self.yang_name = "route-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self.vrf = None
                            self.next_hop = None
                            self._segment_path = lambda: "route-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                    class IpslaTracks(Entity):
                        """
                        track type rtr info
                        
                        .. attribute:: ipsla_op_id
                        
                        	Op Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Latest RTT
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: return_code
                        
                        	Latest Return Code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__init__()

                            self.yang_name = "ipsla-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                                ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                                ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                            ])
                            self.ipsla_op_id = None
                            self.rtt = None
                            self.return_code = None
                            self._segment_path = lambda: "ipsla-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                    class BfdTracks(Entity):
                        """
                        track type bfdrtr info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        .. attribute:: destination_address
                        
                        	Destination Address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rate
                        
                        	Rate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: debounce_count
                        
                        	Debounce Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__init__()

                            self.yang_name = "bfd-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                            ])
                            self.interface_name = None
                            self.destination_address = None
                            self.rate = None
                            self.debounce_count = None
                            self._segment_path = lambda: "bfd-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


    class TrackTypeRtrReachability(Entity):
        """
        Object Tracking Type RTR Reachability info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of  		 :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeRtrReachability, self).__init__()

            self.yang_name = "track-type-rtr-reachability"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-info", ("track_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo))])
            self._leafs = OrderedDict()

            self.track_info = YList(self)
            self._segment_path = lambda: "track-type-rtr-reachability"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeRtrReachability, [], name, value)


        class TrackInfo(Entity):
            """
            track info
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo>`
            
            .. attribute:: bool_tracks
            
            	boolean objects
            	**type**\:  :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks>`
            
            .. attribute:: threshold_tracks
            
            	Threshold objects
            	**type**\:  :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks>`
            
            .. attribute:: tracking_interaces
            
            	Tracking Interfaces
            	**type**\:  :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces>`
            
            .. attribute:: delayed
            
            	Is the state change delay counter in progress
            	**type**\:  :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\: str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            .. attribute:: track_state
            
            	Track state
            	**type**\: bool
            
            .. attribute:: state_change_counter
            
            	State Change Counter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: seconds_last_change
            
            	Seconds Last Change
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: threshold_up
            
            	User specified threshold upper limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_down
            
            	User specified threshold lower limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo, self).__init__()

                self.yang_name = "track-info"
                self.yang_parent_name = "track-type-rtr-reachability"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo)), ("bool-tracks", ("bool_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks)), ("threshold-tracks", ("threshold_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks)), ("tracking-interaces", ("tracking_interaces", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces)), ("delayed", ("delayed", ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed))])
                self._leafs = OrderedDict([
                    ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ('state_change_counter', (YLeaf(YType.uint32, 'state-change-counter'), ['int'])),
                    ('seconds_last_change', (YLeaf(YType.uint64, 'seconds-last-change'), ['int'])),
                    ('threshold_up', (YLeaf(YType.uint32, 'threshold-up'), ['int'])),
                    ('threshold_down', (YLeaf(YType.uint32, 'threshold-down'), ['int'])),
                ])
                self.tracke_name = None
                self.type = None
                self.track_state = None
                self.state_change_counter = None
                self.seconds_last_change = None
                self.threshold_up = None
                self.threshold_down = None

                self.track_type_info = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"

                self.bool_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self._children_name_map["bool_tracks"] = "bool-tracks"

                self.threshold_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self._children_name_map["threshold_tracks"] = "threshold-tracks"

                self.tracking_interaces = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self._children_name_map["tracking_interaces"] = "tracking-interaces"

                self.delayed = ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed()
                self.delayed.parent = self
                self._children_name_map["delayed"] = "delayed"
                self._segment_path = lambda: "track-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo, ['tracke_name', 'type', 'track_state', 'state_change_counter', 'seconds_last_change', 'threshold_up', 'threshold_down'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks))])
                    self._leafs = OrderedDict([
                        ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ])
                    self.discriminant = None

                    self.interface_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"

                    self.route_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"

                    self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                    self.bfd_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__init__()

                        self.yang_name = "interface-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks, self).__init__()

                        self.yang_name = "route-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None
                        self.next_hop = None
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks, self).__init__()

                        self.yang_name = "ipsla-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                            ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                            ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                        ])
                        self.ipsla_op_id = None
                        self.rtt = None
                        self.return_code = None
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks, self).__init__()

                        self.yang_name = "bfd-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.destination_address = None
                        self.rate = None
                        self.debounce_count = None
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


            class BoolTracks(Entity):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of  		 :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks, self).__init__()

                    self.yang_name = "bool-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bool-track-info", ("bool_track_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo))])
                    self._leafs = OrderedDict()

                    self.bool_track_info = YList(self)
                    self._segment_path = lambda: "bool-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks, [], name, value)


                class BoolTrackInfo(Entity):
                    """
                    bool track info
                    
                    .. attribute:: object_name
                    
                    	Object Name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state
                    	**type**\: bool
                    
                    .. attribute:: with_not
                    
                    	Track object with Not
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                        self.yang_name = "bool-track-info"
                        self.yang_parent_name = "bool-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                            ('with_not', (YLeaf(YType.boolean, 'with-not'), ['bool'])),
                        ])
                        self.object_name = None
                        self.track_state = None
                        self.with_not = None
                        self._segment_path = lambda: "bool-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/bool-tracks/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


            class ThresholdTracks(Entity):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of  		 :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks, self).__init__()

                    self.yang_name = "threshold-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("threshold-track-info", ("threshold_track_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo))])
                    self._leafs = OrderedDict()

                    self.threshold_track_info = YList(self)
                    self._segment_path = lambda: "threshold-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks, [], name, value)


                class ThresholdTrackInfo(Entity):
                    """
                    threshold track info
                    
                    .. attribute:: object_name
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state. True means track is up; False means track is down
                    	**type**\: bool
                    
                    .. attribute:: weight
                    
                    	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__init__()

                        self.yang_name = "threshold-track-info"
                        self.yang_parent_name = "threshold-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                        ])
                        self.object_name = None
                        self.track_state = None
                        self.weight = None
                        self._segment_path = lambda: "threshold-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/threshold-tracks/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


            class TrackingInteraces(Entity):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of  		 :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces, self).__init__()

                    self.yang_name = "tracking-interaces"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracking-info", ("interface_tracking_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo))])
                    self._leafs = OrderedDict()

                    self.interface_tracking_info = YList(self)
                    self._segment_path = lambda: "tracking-interaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces, [], name, value)


                class InterfaceTrackingInfo(Entity):
                    """
                    interface tracking info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__init__()

                        self.yang_name = "interface-tracking-info"
                        self.yang_parent_name = "tracking-interaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracking-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/tracking-interaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


            class Delayed(Entity):
                """
                Is the state change delay counter in progress
                
                .. attribute:: time_remaining
                
                	The time remaining in seconds for the counter to trigger state change
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: track_state
                
                	State the track will transition to. Track state. True means track is up; False means track is down
                	**type**\: bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed, self).__init__()

                    self.yang_name = "delayed"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                        ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ])
                    self.time_remaining = None
                    self.track_state = None
                    self._segment_path = lambda: "delayed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


    class TrackTypeRtrReachabilityBrief(Entity):
        """
        Object Tracking Type RTR Reachability brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of  		 :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeRtrReachabilityBrief, self).__init__()

            self.yang_name = "track-type-rtr-reachability-brief"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-info-brief", ("track_info_brief", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief))])
            self._leafs = OrderedDict()

            self.track_info_brief = YList(self)
            self._segment_path = lambda: "track-type-rtr-reachability-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief, [], name, value)


        class TrackInfoBrief(Entity):
            """
            track info brief
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\: str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            .. attribute:: track_state
            
            	Track state
            	**type**\: bool
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief, self).__init__()

                self.yang_name = "track-info-brief"
                self.yang_parent_name = "track-type-rtr-reachability-brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo))])
                self._leafs = OrderedDict([
                    ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                ])
                self.tracke_name = None
                self.type = None
                self.track_state = None

                self.track_type_info = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._segment_path = lambda: "track-info-brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief, ['tracke_name', 'type', 'track_state'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks))])
                    self._leafs = OrderedDict([
                        ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ])
                    self.discriminant = None

                    self.interface_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"

                    self.route_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"

                    self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                    self.bfd_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__init__()

                        self.yang_name = "interface-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__init__()

                        self.yang_name = "route-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None
                        self.next_hop = None
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__init__()

                        self.yang_name = "ipsla-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                            ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                            ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                        ])
                        self.ipsla_op_id = None
                        self.rtt = None
                        self.return_code = None
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__init__()

                        self.yang_name = "bfd-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.destination_address = None
                        self.rate = None
                        self.debounce_count = None
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


    class Tracks(Entity):
        """
        Object Tracking Track table
        
        .. attribute:: track
        
        	Track name \- maximum 32 characters
        	**type**\: list of  		 :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.Tracks, self).__init__()

            self.yang_name = "tracks"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track", ("track", ObjectTracking.Tracks.Track))])
            self._leafs = OrderedDict()

            self.track = YList(self)
            self._segment_path = lambda: "tracks"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.Tracks, [], name, value)


        class Track(Entity):
            """
            Track name \- maximum 32 characters
            
            .. attribute:: track_name  (key)
            
            	Track name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: track_info
            
            	track info
            	**type**\: list of  		 :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.Tracks.Track, self).__init__()

                self.yang_name = "track"
                self.yang_parent_name = "tracks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['track_name']
                self._child_classes = OrderedDict([("track-info", ("track_info", ObjectTracking.Tracks.Track.TrackInfo))])
                self._leafs = OrderedDict([
                    ('track_name', (YLeaf(YType.str, 'track-name'), ['str'])),
                ])
                self.track_name = None

                self.track_info = YList(self)
                self._segment_path = lambda: "track" + "[track-name='" + str(self.track_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/tracks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.Tracks.Track, ['track_name'], name, value)


            class TrackInfo(Entity):
                """
                track info
                
                .. attribute:: track_type_info
                
                	Track type information
                	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo>`
                
                .. attribute:: bool_tracks
                
                	boolean objects
                	**type**\:  :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.BoolTracks>`
                
                .. attribute:: threshold_tracks
                
                	Threshold objects
                	**type**\:  :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks>`
                
                .. attribute:: tracking_interaces
                
                	Tracking Interfaces
                	**type**\:  :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces>`
                
                .. attribute:: delayed
                
                	Is the state change delay counter in progress
                	**type**\:  :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.Delayed>`
                
                .. attribute:: tracke_name
                
                	Track Name
                	**type**\: str
                
                	**length:** 0..33
                
                .. attribute:: type
                
                	Track type
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: track_state
                
                	Track state
                	**type**\: bool
                
                .. attribute:: state_change_counter
                
                	State Change Counter
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_last_change
                
                	Seconds Last Change
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                .. attribute:: threshold_up
                
                	User specified threshold upper limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: threshold_down
                
                	User specified threshold lower limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.Tracks.Track.TrackInfo, self).__init__()

                    self.yang_name = "track-info"
                    self.yang_parent_name = "track"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo)), ("bool-tracks", ("bool_tracks", ObjectTracking.Tracks.Track.TrackInfo.BoolTracks)), ("threshold-tracks", ("threshold_tracks", ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks)), ("tracking-interaces", ("tracking_interaces", ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces)), ("delayed", ("delayed", ObjectTracking.Tracks.Track.TrackInfo.Delayed))])
                    self._leafs = OrderedDict([
                        ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                        ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                        ('state_change_counter', (YLeaf(YType.uint32, 'state-change-counter'), ['int'])),
                        ('seconds_last_change', (YLeaf(YType.uint64, 'seconds-last-change'), ['int'])),
                        ('threshold_up', (YLeaf(YType.uint32, 'threshold-up'), ['int'])),
                        ('threshold_down', (YLeaf(YType.uint32, 'threshold-down'), ['int'])),
                    ])
                    self.tracke_name = None
                    self.type = None
                    self.track_state = None
                    self.state_change_counter = None
                    self.seconds_last_change = None
                    self.threshold_up = None
                    self.threshold_down = None

                    self.track_type_info = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self._children_name_map["track_type_info"] = "track-type-info"

                    self.bool_tracks = ObjectTracking.Tracks.Track.TrackInfo.BoolTracks()
                    self.bool_tracks.parent = self
                    self._children_name_map["bool_tracks"] = "bool-tracks"

                    self.threshold_tracks = ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks()
                    self.threshold_tracks.parent = self
                    self._children_name_map["threshold_tracks"] = "threshold-tracks"

                    self.tracking_interaces = ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces()
                    self.tracking_interaces.parent = self
                    self._children_name_map["tracking_interaces"] = "tracking-interaces"

                    self.delayed = ObjectTracking.Tracks.Track.TrackInfo.Delayed()
                    self.delayed.parent = self
                    self._children_name_map["delayed"] = "delayed"
                    self._segment_path = lambda: "track-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo, ['tracke_name', 'type', 'track_state', 'state_change_counter', 'seconds_last_change', 'threshold_up', 'threshold_down'], name, value)


                class TrackTypeInfo(Entity):
                    """
                    Track type information
                    
                    .. attribute:: interface_tracks
                    
                    	track type interface info
                    	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                    
                    .. attribute:: route_tracks
                    
                    	track type route info
                    	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks>`
                    
                    .. attribute:: ipsla_tracks
                    
                    	track type rtr info
                    	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks>`
                    
                    .. attribute:: bfd_tracks
                    
                    	track type bfdrtr info
                    	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks>`
                    
                    .. attribute:: discriminant
                    
                    	discriminant
                    	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo, self).__init__()

                        self.yang_name = "track-type-info"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks))])
                        self._leafs = OrderedDict([
                            ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                        ])
                        self.discriminant = None

                        self.interface_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks()
                        self.interface_tracks.parent = self
                        self._children_name_map["interface_tracks"] = "interface-tracks"

                        self.route_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks()
                        self.route_tracks.parent = self
                        self._children_name_map["route_tracks"] = "route-tracks"

                        self.ipsla_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks()
                        self.ipsla_tracks.parent = self
                        self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                        self.bfd_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks()
                        self.bfd_tracks.parent = self
                        self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        self._segment_path = lambda: "track-type-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                    class InterfaceTracks(Entity):
                        """
                        track type interface info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__init__()

                            self.yang_name = "interface-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self._segment_path = lambda: "interface-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                    class RouteTracks(Entity):
                        """
                        track type route info
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf
                        
                        	VRF Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        .. attribute:: next_hop
                        
                        	Next Hop
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks, self).__init__()

                            self.yang_name = "route-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                            ])
                            self.prefix = None
                            self.prefix_length = None
                            self.vrf = None
                            self.next_hop = None
                            self._segment_path = lambda: "route-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                    class IpslaTracks(Entity):
                        """
                        track type rtr info
                        
                        .. attribute:: ipsla_op_id
                        
                        	Op Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Latest RTT
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: return_code
                        
                        	Latest Return Code
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks, self).__init__()

                            self.yang_name = "ipsla-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                                ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                                ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                            ])
                            self.ipsla_op_id = None
                            self.rtt = None
                            self.return_code = None
                            self._segment_path = lambda: "ipsla-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                    class BfdTracks(Entity):
                        """
                        track type bfdrtr info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        .. attribute:: destination_address
                        
                        	Destination Address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rate
                        
                        	Rate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: debounce_count
                        
                        	Debounce Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks, self).__init__()

                            self.yang_name = "bfd-tracks"
                            self.yang_parent_name = "track-type-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                                ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                                ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                            ])
                            self.interface_name = None
                            self.destination_address = None
                            self.rate = None
                            self.debounce_count = None
                            self._segment_path = lambda: "bfd-tracks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


                class BoolTracks(Entity):
                    """
                    boolean objects
                    
                    .. attribute:: bool_track_info
                    
                    	bool track info
                    	**type**\: list of  		 :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks, self).__init__()

                        self.yang_name = "bool-tracks"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("bool-track-info", ("bool_track_info", ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo))])
                        self._leafs = OrderedDict()

                        self.bool_track_info = YList(self)
                        self._segment_path = lambda: "bool-tracks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks, [], name, value)


                    class BoolTrackInfo(Entity):
                        """
                        bool track info
                        
                        .. attribute:: object_name
                        
                        	Object Name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: track_state
                        
                        	Track state
                        	**type**\: bool
                        
                        .. attribute:: with_not
                        
                        	Track object with Not
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                            self.yang_name = "bool-track-info"
                            self.yang_parent_name = "bool-tracks"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                                ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                                ('with_not', (YLeaf(YType.boolean, 'with-not'), ['bool'])),
                            ])
                            self.object_name = None
                            self.track_state = None
                            self.with_not = None
                            self._segment_path = lambda: "bool-track-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


                class ThresholdTracks(Entity):
                    """
                    Threshold objects
                    
                    .. attribute:: threshold_track_info
                    
                    	threshold track info
                    	**type**\: list of  		 :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks, self).__init__()

                        self.yang_name = "threshold-tracks"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("threshold-track-info", ("threshold_track_info", ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo))])
                        self._leafs = OrderedDict()

                        self.threshold_track_info = YList(self)
                        self._segment_path = lambda: "threshold-tracks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks, [], name, value)


                    class ThresholdTrackInfo(Entity):
                        """
                        threshold track info
                        
                        .. attribute:: object_name
                        
                        	Object name
                        	**type**\: str
                        
                        	**length:** 0..33
                        
                        .. attribute:: track_state
                        
                        	Track state. True means track is up; False means track is down
                        	**type**\: bool
                        
                        .. attribute:: weight
                        
                        	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: percentage
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__init__()

                            self.yang_name = "threshold-track-info"
                            self.yang_parent_name = "threshold-tracks"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                                ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                                ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                            ])
                            self.object_name = None
                            self.track_state = None
                            self.weight = None
                            self._segment_path = lambda: "threshold-track-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


                class TrackingInteraces(Entity):
                    """
                    Tracking Interfaces
                    
                    .. attribute:: interface_tracking_info
                    
                    	interface tracking info
                    	**type**\: list of  		 :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces, self).__init__()

                        self.yang_name = "tracking-interaces"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-tracking-info", ("interface_tracking_info", ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo))])
                        self._leafs = OrderedDict()

                        self.interface_tracking_info = YList(self)
                        self._segment_path = lambda: "tracking-interaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces, [], name, value)


                    class InterfaceTrackingInfo(Entity):
                        """
                        interface tracking info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**length:** 0..120
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__init__()

                            self.yang_name = "interface-tracking-info"
                            self.yang_parent_name = "tracking-interaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self._segment_path = lambda: "interface-tracking-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


                class Delayed(Entity):
                    """
                    Is the state change delay counter in progress
                    
                    .. attribute:: time_remaining
                    
                    	The time remaining in seconds for the counter to trigger state change
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: track_state
                    
                    	State the track will transition to. Track state. True means track is up; False means track is down
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.Delayed, self).__init__()

                        self.yang_name = "delayed"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                        ])
                        self.time_remaining = None
                        self.track_state = None
                        self._segment_path = lambda: "delayed"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


    class TrackTypeIpv4RouteBrief(Entity):
        """
        Object Tracking Type Ipv4 Route brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of  		 :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeIpv4RouteBrief, self).__init__()

            self.yang_name = "track-type-ipv4-route-brief"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-info-brief", ("track_info_brief", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief))])
            self._leafs = OrderedDict()

            self.track_info_brief = YList(self)
            self._segment_path = lambda: "track-type-ipv4-route-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief, [], name, value)


        class TrackInfoBrief(Entity):
            """
            track info brief
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\: str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            .. attribute:: track_state
            
            	Track state
            	**type**\: bool
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief, self).__init__()

                self.yang_name = "track-info-brief"
                self.yang_parent_name = "track-type-ipv4-route-brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo))])
                self._leafs = OrderedDict([
                    ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                ])
                self.tracke_name = None
                self.type = None
                self.track_state = None

                self.track_type_info = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._segment_path = lambda: "track-info-brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief, ['tracke_name', 'type', 'track_state'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks))])
                    self._leafs = OrderedDict([
                        ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ])
                    self.discriminant = None

                    self.interface_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"

                    self.route_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"

                    self.ipsla_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                    self.bfd_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__init__()

                        self.yang_name = "interface-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__init__()

                        self.yang_name = "route-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None
                        self.next_hop = None
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__init__()

                        self.yang_name = "ipsla-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                            ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                            ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                        ])
                        self.ipsla_op_id = None
                        self.rtt = None
                        self.return_code = None
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__init__()

                        self.yang_name = "bfd-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.destination_address = None
                        self.rate = None
                        self.debounce_count = None
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


    class TrackTypeIpv4Route(Entity):
        """
        Object Tracking Type IPV4 route info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of  		 :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeIpv4Route, self).__init__()

            self.yang_name = "track-type-ipv4-route"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-info", ("track_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo))])
            self._leafs = OrderedDict()

            self.track_info = YList(self)
            self._segment_path = lambda: "track-type-ipv4-route"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeIpv4Route, [], name, value)


        class TrackInfo(Entity):
            """
            track info
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo>`
            
            .. attribute:: bool_tracks
            
            	boolean objects
            	**type**\:  :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks>`
            
            .. attribute:: threshold_tracks
            
            	Threshold objects
            	**type**\:  :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks>`
            
            .. attribute:: tracking_interaces
            
            	Tracking Interfaces
            	**type**\:  :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces>`
            
            .. attribute:: delayed
            
            	Is the state change delay counter in progress
            	**type**\:  :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\: str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            .. attribute:: track_state
            
            	Track state
            	**type**\: bool
            
            .. attribute:: state_change_counter
            
            	State Change Counter
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: seconds_last_change
            
            	Seconds Last Change
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: threshold_up
            
            	User specified threshold upper limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_down
            
            	User specified threshold lower limit
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo, self).__init__()

                self.yang_name = "track-info"
                self.yang_parent_name = "track-type-ipv4-route"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo)), ("bool-tracks", ("bool_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks)), ("threshold-tracks", ("threshold_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks)), ("tracking-interaces", ("tracking_interaces", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces)), ("delayed", ("delayed", ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed))])
                self._leafs = OrderedDict([
                    ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ('state_change_counter', (YLeaf(YType.uint32, 'state-change-counter'), ['int'])),
                    ('seconds_last_change', (YLeaf(YType.uint64, 'seconds-last-change'), ['int'])),
                    ('threshold_up', (YLeaf(YType.uint32, 'threshold-up'), ['int'])),
                    ('threshold_down', (YLeaf(YType.uint32, 'threshold-down'), ['int'])),
                ])
                self.tracke_name = None
                self.type = None
                self.track_state = None
                self.state_change_counter = None
                self.seconds_last_change = None
                self.threshold_up = None
                self.threshold_down = None

                self.track_type_info = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"

                self.bool_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self._children_name_map["bool_tracks"] = "bool-tracks"

                self.threshold_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self._children_name_map["threshold_tracks"] = "threshold-tracks"

                self.tracking_interaces = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self._children_name_map["tracking_interaces"] = "tracking-interaces"

                self.delayed = ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed()
                self.delayed.parent = self
                self._children_name_map["delayed"] = "delayed"
                self._segment_path = lambda: "track-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo, ['tracke_name', 'type', 'track_state', 'state_change_counter', 'seconds_last_change', 'threshold_up', 'threshold_down'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks))])
                    self._leafs = OrderedDict([
                        ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ])
                    self.discriminant = None

                    self.interface_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"

                    self.route_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"

                    self.ipsla_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                    self.bfd_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__init__()

                        self.yang_name = "interface-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks, self).__init__()

                        self.yang_name = "route-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None
                        self.next_hop = None
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks, self).__init__()

                        self.yang_name = "ipsla-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                            ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                            ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                        ])
                        self.ipsla_op_id = None
                        self.rtt = None
                        self.return_code = None
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks, self).__init__()

                        self.yang_name = "bfd-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.destination_address = None
                        self.rate = None
                        self.debounce_count = None
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)


            class BoolTracks(Entity):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of  		 :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks, self).__init__()

                    self.yang_name = "bool-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bool-track-info", ("bool_track_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo))])
                    self._leafs = OrderedDict()

                    self.bool_track_info = YList(self)
                    self._segment_path = lambda: "bool-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks, [], name, value)


                class BoolTrackInfo(Entity):
                    """
                    bool track info
                    
                    .. attribute:: object_name
                    
                    	Object Name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state
                    	**type**\: bool
                    
                    .. attribute:: with_not
                    
                    	Track object with Not
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                        self.yang_name = "bool-track-info"
                        self.yang_parent_name = "bool-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                            ('with_not', (YLeaf(YType.boolean, 'with-not'), ['bool'])),
                        ])
                        self.object_name = None
                        self.track_state = None
                        self.with_not = None
                        self._segment_path = lambda: "bool-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/bool-tracks/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


            class ThresholdTracks(Entity):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of  		 :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks, self).__init__()

                    self.yang_name = "threshold-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("threshold-track-info", ("threshold_track_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo))])
                    self._leafs = OrderedDict()

                    self.threshold_track_info = YList(self)
                    self._segment_path = lambda: "threshold-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks, [], name, value)


                class ThresholdTrackInfo(Entity):
                    """
                    threshold track info
                    
                    .. attribute:: object_name
                    
                    	Object name
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state. True means track is up; False means track is down
                    	**type**\: bool
                    
                    .. attribute:: weight
                    
                    	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: percentage
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__init__()

                        self.yang_name = "threshold-track-info"
                        self.yang_parent_name = "threshold-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('object_name', (YLeaf(YType.str, 'object-name'), ['str'])),
                            ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                            ('weight', (YLeaf(YType.uint32, 'weight'), ['int'])),
                        ])
                        self.object_name = None
                        self.track_state = None
                        self.weight = None
                        self._segment_path = lambda: "threshold-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/threshold-tracks/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


            class TrackingInteraces(Entity):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of  		 :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces, self).__init__()

                    self.yang_name = "tracking-interaces"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracking-info", ("interface_tracking_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo))])
                    self._leafs = OrderedDict()

                    self.interface_tracking_info = YList(self)
                    self._segment_path = lambda: "tracking-interaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces, [], name, value)


                class InterfaceTrackingInfo(Entity):
                    """
                    interface tracking info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__init__()

                        self.yang_name = "interface-tracking-info"
                        self.yang_parent_name = "tracking-interaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracking-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/tracking-interaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


            class Delayed(Entity):
                """
                Is the state change delay counter in progress
                
                .. attribute:: time_remaining
                
                	The time remaining in seconds for the counter to trigger state change
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: track_state
                
                	State the track will transition to. Track state. True means track is up; False means track is down
                	**type**\: bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed, self).__init__()

                    self.yang_name = "delayed"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                        ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                    ])
                    self.time_remaining = None
                    self.track_state = None
                    self._segment_path = lambda: "delayed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


    class TrackTypeInterfaceBrief(Entity):
        """
        Object Tracking Type Interface brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of  		 :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeInterfaceBrief, self).__init__()

            self.yang_name = "track-type-interface-brief"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("track-info-brief", ("track_info_brief", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief))])
            self._leafs = OrderedDict()

            self.track_info_brief = YList(self)
            self._segment_path = lambda: "track-type-interface-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief, [], name, value)


        class TrackInfoBrief(Entity):
            """
            track info brief
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:  :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\: str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            .. attribute:: track_state
            
            	Track state
            	**type**\: bool
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief, self).__init__()

                self.yang_name = "track-info-brief"
                self.yang_parent_name = "track-type-interface-brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("track-type-info", ("track_type_info", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo))])
                self._leafs = OrderedDict([
                    ('tracke_name', (YLeaf(YType.str, 'tracke-name'), ['str'])),
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ('track_state', (YLeaf(YType.boolean, 'track-state'), ['bool'])),
                ])
                self.tracke_name = None
                self.type = None
                self.track_state = None

                self.track_type_info = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._segment_path = lambda: "track-info-brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief, ['tracke_name', 'type', 'track_state'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:  :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:  :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:  :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:  :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:  :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-tracks", ("interface_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks)), ("route-tracks", ("route_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)), ("ipsla-tracks", ("ipsla_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks)), ("bfd-tracks", ("bfd_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks))])
                    self._leafs = OrderedDict([
                        ('discriminant', (YLeaf(YType.enumeration, 'discriminant'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper', 'Track', '')])),
                    ])
                    self.discriminant = None

                    self.interface_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"

                    self.route_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"

                    self.ipsla_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"

                    self.bfd_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__init__()

                        self.yang_name = "interface-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__init__()

                        self.yang_name = "route-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('prefix', (YLeaf(YType.uint32, 'prefix'), ['int'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('next_hop', (YLeaf(YType.str, 'next-hop'), ['str'])),
                        ])
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None
                        self.next_hop = None
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['prefix', 'prefix_length', 'vrf', 'next_hop'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__init__()

                        self.yang_name = "ipsla-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ipsla_op_id', (YLeaf(YType.uint32, 'ipsla-op-id'), ['int'])),
                            ('rtt', (YLeaf(YType.uint32, 'rtt'), ['int'])),
                            ('return_code', (YLeaf(YType.uint32, 'return-code'), ['int'])),
                        ])
                        self.ipsla_op_id = None
                        self.rtt = None
                        self.return_code = None
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'rtt', 'return_code'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**length:** 0..120
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__init__()

                        self.yang_name = "bfd-tracks"
                        self.yang_parent_name = "track-type-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('destination_address', (YLeaf(YType.uint32, 'destination-address'), ['int'])),
                            ('rate', (YLeaf(YType.uint32, 'rate'), ['int'])),
                            ('debounce_count', (YLeaf(YType.uint32, 'debounce-count'), ['int'])),
                        ])
                        self.interface_name = None
                        self.destination_address = None
                        self.rate = None
                        self.debounce_count = None
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['interface_name', 'destination_address', 'rate', 'debounce_count'], name, value)

    def clone_ptr(self):
        self._top_entity = ObjectTracking()
        return self._top_entity

