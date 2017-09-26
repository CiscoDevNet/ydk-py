""" Cisco_IOS_XR_manageability_object_tracking_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package operational data.

This module contains definitions
for the following management objects\:
  object\-tracking\: Object Tracking operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Track(Enum):
    """
    Track

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
    
    .. attribute:: track_briefs
    
    	Object Tracking Track table brief
    	**type**\:   :py:class:`TrackBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs>`
    
    .. attribute:: track_type_interface
    
    	Object Tracking Type interface info
    	**type**\:   :py:class:`TrackTypeInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface>`
    
    .. attribute:: track_type_interface_brief
    
    	Object Tracking Type Interface brief info
    	**type**\:   :py:class:`TrackTypeInterfaceBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief>`
    
    .. attribute:: track_type_ipv4_route
    
    	Object Tracking Type IPV4 route info
    	**type**\:   :py:class:`TrackTypeIpv4Route <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route>`
    
    .. attribute:: track_type_ipv4_route_brief
    
    	Object Tracking Type Ipv4 Route brief info
    	**type**\:   :py:class:`TrackTypeIpv4RouteBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief>`
    
    .. attribute:: track_type_rtr_reachability
    
    	Object Tracking Type RTR Reachability info
    	**type**\:   :py:class:`TrackTypeRtrReachability <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability>`
    
    .. attribute:: track_type_rtr_reachability_brief
    
    	Object Tracking Type RTR Reachability brief info
    	**type**\:   :py:class:`TrackTypeRtrReachabilityBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief>`
    
    .. attribute:: tracks
    
    	Object Tracking Track table
    	**type**\:   :py:class:`Tracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks>`
    
    

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
        self._child_container_classes = {"track-briefs" : ("track_briefs", ObjectTracking.TrackBriefs), "track-type-interface" : ("track_type_interface", ObjectTracking.TrackTypeInterface), "track-type-interface-brief" : ("track_type_interface_brief", ObjectTracking.TrackTypeInterfaceBrief), "track-type-ipv4-route" : ("track_type_ipv4_route", ObjectTracking.TrackTypeIpv4Route), "track-type-ipv4-route-brief" : ("track_type_ipv4_route_brief", ObjectTracking.TrackTypeIpv4RouteBrief), "track-type-rtr-reachability" : ("track_type_rtr_reachability", ObjectTracking.TrackTypeRtrReachability), "track-type-rtr-reachability-brief" : ("track_type_rtr_reachability_brief", ObjectTracking.TrackTypeRtrReachabilityBrief), "tracks" : ("tracks", ObjectTracking.Tracks)}
        self._child_list_classes = {}

        self.track_briefs = ObjectTracking.TrackBriefs()
        self.track_briefs.parent = self
        self._children_name_map["track_briefs"] = "track-briefs"
        self._children_yang_names.add("track-briefs")

        self.track_type_interface = ObjectTracking.TrackTypeInterface()
        self.track_type_interface.parent = self
        self._children_name_map["track_type_interface"] = "track-type-interface"
        self._children_yang_names.add("track-type-interface")

        self.track_type_interface_brief = ObjectTracking.TrackTypeInterfaceBrief()
        self.track_type_interface_brief.parent = self
        self._children_name_map["track_type_interface_brief"] = "track-type-interface-brief"
        self._children_yang_names.add("track-type-interface-brief")

        self.track_type_ipv4_route = ObjectTracking.TrackTypeIpv4Route()
        self.track_type_ipv4_route.parent = self
        self._children_name_map["track_type_ipv4_route"] = "track-type-ipv4-route"
        self._children_yang_names.add("track-type-ipv4-route")

        self.track_type_ipv4_route_brief = ObjectTracking.TrackTypeIpv4RouteBrief()
        self.track_type_ipv4_route_brief.parent = self
        self._children_name_map["track_type_ipv4_route_brief"] = "track-type-ipv4-route-brief"
        self._children_yang_names.add("track-type-ipv4-route-brief")

        self.track_type_rtr_reachability = ObjectTracking.TrackTypeRtrReachability()
        self.track_type_rtr_reachability.parent = self
        self._children_name_map["track_type_rtr_reachability"] = "track-type-rtr-reachability"
        self._children_yang_names.add("track-type-rtr-reachability")

        self.track_type_rtr_reachability_brief = ObjectTracking.TrackTypeRtrReachabilityBrief()
        self.track_type_rtr_reachability_brief.parent = self
        self._children_name_map["track_type_rtr_reachability_brief"] = "track-type-rtr-reachability-brief"
        self._children_yang_names.add("track-type-rtr-reachability-brief")

        self.tracks = ObjectTracking.Tracks()
        self.tracks.parent = self
        self._children_name_map["tracks"] = "tracks"
        self._children_yang_names.add("tracks")
        self._segment_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking"


    class TrackBriefs(Entity):
        """
        Object Tracking Track table brief
        
        .. attribute:: track_brief
        
        	Track name \- maximum 32 characters
        	**type**\: list of    :py:class:`TrackBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackBriefs, self).__init__()

            self.yang_name = "track-briefs"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-brief" : ("track_brief", ObjectTracking.TrackBriefs.TrackBrief)}

            self.track_brief = YList(self)
            self._segment_path = lambda: "track-briefs"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackBriefs, [], name, value)


        class TrackBrief(Entity):
            """
            Track name \- maximum 32 characters
            
            .. attribute:: track_name  <key>
            
            	Track name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: track_info_brief
            
            	track info brief
            	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackBriefs.TrackBrief, self).__init__()

                self.yang_name = "track-brief"
                self.yang_parent_name = "track-briefs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"track-info-brief" : ("track_info_brief", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief)}

                self.track_name = YLeaf(YType.str, "track-name")

                self.track_info_brief = YList(self)
                self._segment_path = lambda: "track-brief" + "[track-name='" + self.track_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-briefs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief, ['track_name'], name, value)


            class TrackInfoBrief(Entity):
                """
                track info brief
                
                .. attribute:: track_state
                
                	Track state
                	**type**\:  bool
                
                .. attribute:: track_type_info
                
                	Track type information
                	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo>`
                
                .. attribute:: tracke_name
                
                	Track Name
                	**type**\:  str
                
                	**length:** 0..33
                
                .. attribute:: type
                
                	Track type
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief, self).__init__()

                    self.yang_name = "track-info-brief"
                    self.yang_parent_name = "track-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"track-type-info" : ("track_type_info", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo)}
                    self._child_list_classes = {}

                    self.track_state = YLeaf(YType.boolean, "track-state")

                    self.tracke_name = YLeaf(YType.str, "tracke-name")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.track_type_info = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self._children_name_map["track_type_info"] = "track-type-info"
                    self._children_yang_names.add("track-type-info")
                    self._segment_path = lambda: "track-info-brief"

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief, ['track_state', 'tracke_name', 'type'], name, value)


                class TrackTypeInfo(Entity):
                    """
                    Track type information
                    
                    .. attribute:: bfd_tracks
                    
                    	track type bfdrtr info
                    	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                    
                    .. attribute:: discriminant
                    
                    	discriminant
                    	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                    
                    .. attribute:: interface_tracks
                    
                    	track type interface info
                    	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                    
                    .. attribute:: ipsla_tracks
                    
                    	track type rtr info
                    	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                    
                    .. attribute:: route_tracks
                    
                    	track type route info
                    	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                        self.yang_name = "track-type-info"
                        self.yang_parent_name = "track-info-brief"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)}
                        self._child_list_classes = {}

                        self.discriminant = YLeaf(YType.enumeration, "discriminant")

                        self.bfd_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                        self.bfd_tracks.parent = self
                        self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        self._children_yang_names.add("bfd-tracks")

                        self.interface_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                        self.interface_tracks.parent = self
                        self._children_name_map["interface_tracks"] = "interface-tracks"
                        self._children_yang_names.add("interface-tracks")

                        self.ipsla_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                        self.ipsla_tracks.parent = self
                        self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        self._children_yang_names.add("ipsla-tracks")

                        self.route_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                        self.route_tracks.parent = self
                        self._children_name_map["route_tracks"] = "route-tracks"
                        self._children_yang_names.add("route-tracks")
                        self._segment_path = lambda: "track-type-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                    class BfdTracks(Entity):
                        """
                        track type bfdrtr info
                        
                        .. attribute:: debounce_count
                        
                        	Debounce Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destination_address
                        
                        	Destination Address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**length:** 0..120
                        
                        .. attribute:: rate
                        
                        	Rate
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                            self.destination_address = YLeaf(YType.uint32, "destination-address")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.rate = YLeaf(YType.uint32, "rate")
                            self._segment_path = lambda: "bfd-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                    class InterfaceTracks(Entity):
                        """
                        track type interface info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "interface-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                    class IpslaTracks(Entity):
                        """
                        track type rtr info
                        
                        .. attribute:: ipsla_op_id
                        
                        	Op Id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: return_code
                        
                        	Latest Return Code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Latest RTT
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                            self.return_code = YLeaf(YType.uint32, "return-code")

                            self.rtt = YLeaf(YType.uint32, "rtt")
                            self._segment_path = lambda: "ipsla-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                    class RouteTracks(Entity):
                        """
                        track type route info
                        
                        .. attribute:: next_hop
                        
                        	Next Hop
                        	**type**\:  str
                        
                        	**length:** 0..120
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf
                        
                        	VRF Name
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.next_hop = YLeaf(YType.str, "next-hop")

                            self.prefix = YLeaf(YType.uint32, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.vrf = YLeaf(YType.str, "vrf")
                            self._segment_path = lambda: "route-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


    class TrackTypeInterface(Entity):
        """
        Object Tracking Type interface info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeInterface, self).__init__()

            self.yang_name = "track-type-interface"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-info" : ("track_info", ObjectTracking.TrackTypeInterface.TrackInfo)}

            self.track_info = YList(self)
            self._segment_path = lambda: "track-type-interface"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeInterface, [], name, value)


        class TrackInfo(Entity):
            """
            track info
            
            .. attribute:: bool_tracks
            
            	boolean objects
            	**type**\:   :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks>`
            
            .. attribute:: delayed
            
            	Is the state change delay counter in progress
            	**type**\:   :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.Delayed>`
            
            .. attribute:: seconds_last_change
            
            	Seconds Last Change
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: state_change_counter
            
            	State Change Counter
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_down
            
            	User specified threshold lower limit
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_tracks
            
            	Threshold objects
            	**type**\:   :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks>`
            
            .. attribute:: threshold_up
            
            	User specified threshold upper limit
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: track_state
            
            	Track state
            	**type**\:  bool
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\:  str
            
            	**length:** 0..33
            
            .. attribute:: tracking_interaces
            
            	Tracking Interfaces
            	**type**\:   :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces>`
            
            .. attribute:: type
            
            	Track type
            	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeInterface.TrackInfo, self).__init__()

                self.yang_name = "track-info"
                self.yang_parent_name = "track-type-interface"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bool-tracks" : ("bool_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks), "delayed" : ("delayed", ObjectTracking.TrackTypeInterface.TrackInfo.Delayed), "threshold-tracks" : ("threshold_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks), "track-type-info" : ("track_type_info", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo), "tracking-interaces" : ("tracking_interaces", ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces)}
                self._child_list_classes = {}

                self.seconds_last_change = YLeaf(YType.uint64, "seconds-last-change")

                self.state_change_counter = YLeaf(YType.uint32, "state-change-counter")

                self.threshold_down = YLeaf(YType.uint32, "threshold-down")

                self.threshold_up = YLeaf(YType.uint32, "threshold-up")

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.bool_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self._children_name_map["bool_tracks"] = "bool-tracks"
                self._children_yang_names.add("bool-tracks")

                self.delayed = ObjectTracking.TrackTypeInterface.TrackInfo.Delayed()
                self.delayed.parent = self
                self._children_name_map["delayed"] = "delayed"
                self._children_yang_names.add("delayed")

                self.threshold_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self._children_name_map["threshold_tracks"] = "threshold-tracks"
                self._children_yang_names.add("threshold-tracks")

                self.track_type_info = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")

                self.tracking_interaces = ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self._children_name_map["tracking_interaces"] = "tracking-interaces"
                self._children_yang_names.add("tracking-interaces")
                self._segment_path = lambda: "track-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo, ['seconds_last_change', 'state_change_counter', 'threshold_down', 'threshold_up', 'track_state', 'tracke_name', 'type'], name, value)


            class BoolTracks(Entity):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks, self).__init__()

                    self.yang_name = "bool-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"bool-track-info" : ("bool_track_info", ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo)}

                    self.bool_track_info = YList(self)
                    self._segment_path = lambda: "bool-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks, [], name, value)


                class BoolTrackInfo(Entity):
                    """
                    bool track info
                    
                    .. attribute:: object_name
                    
                    	Object Name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state
                    	**type**\:  bool
                    
                    .. attribute:: with_not
                    
                    	Track object with Not
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                        self.yang_name = "bool-track-info"
                        self.yang_parent_name = "bool-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.with_not = YLeaf(YType.boolean, "with-not")
                        self._segment_path = lambda: "bool-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/bool-tracks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


            class Delayed(Entity):
                """
                Is the state change delay counter in progress
                
                .. attribute:: time_remaining
                
                	The time remaining in seconds for the counter to trigger state change
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: track_state
                
                	State the track will transition to. Track state. True means track is up; False means track is down
                	**type**\:  bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.Delayed, self).__init__()

                    self.yang_name = "delayed"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    self.track_state = YLeaf(YType.boolean, "track-state")
                    self._segment_path = lambda: "delayed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


            class ThresholdTracks(Entity):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks, self).__init__()

                    self.yang_name = "threshold-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"threshold-track-info" : ("threshold_track_info", ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo)}

                    self.threshold_track_info = YList(self)
                    self._segment_path = lambda: "threshold-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks, [], name, value)


                class ThresholdTrackInfo(Entity):
                    """
                    threshold track info
                    
                    .. attribute:: object_name
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state. True means track is up; False means track is down
                    	**type**\:  bool
                    
                    .. attribute:: weight
                    
                    	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.weight = YLeaf(YType.uint32, "weight")
                        self._segment_path = lambda: "threshold-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/threshold-tracks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks)}
                    self._child_list_classes = {}

                    self.discriminant = YLeaf(YType.enumeration, "discriminant")

                    self.bfd_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._children_yang_names.add("bfd-tracks")

                    self.interface_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"
                    self._children_yang_names.add("interface-tracks")

                    self.ipsla_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                    self._children_yang_names.add("ipsla-tracks")

                    self.route_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"
                    self._children_yang_names.add("route-tracks")
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


            class TrackingInteraces(Entity):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces, self).__init__()

                    self.yang_name = "tracking-interaces"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-tracking-info" : ("interface_tracking_info", ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo)}

                    self.interface_tracking_info = YList(self)
                    self._segment_path = lambda: "tracking-interaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces, [], name, value)


                class InterfaceTrackingInfo(Entity):
                    """
                    interface tracking info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracking-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/tracking-interaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


    class TrackTypeInterfaceBrief(Entity):
        """
        Object Tracking Type Interface brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeInterfaceBrief, self).__init__()

            self.yang_name = "track-type-interface-brief"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-info-brief" : ("track_info_brief", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief)}

            self.track_info_brief = YList(self)
            self._segment_path = lambda: "track-type-interface-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief, [], name, value)


        class TrackInfoBrief(Entity):
            """
            track info brief
            
            .. attribute:: track_state
            
            	Track state
            	**type**\:  bool
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\:  str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief, self).__init__()

                self.yang_name = "track-info-brief"
                self.yang_parent_name = "track-type-interface-brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"track-type-info" : ("track_type_info", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo)}
                self._child_list_classes = {}

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.track_type_info = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")
                self._segment_path = lambda: "track-info-brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief, ['track_state', 'tracke_name', 'type'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)}
                    self._child_list_classes = {}

                    self.discriminant = YLeaf(YType.enumeration, "discriminant")

                    self.bfd_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._children_yang_names.add("bfd-tracks")

                    self.interface_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"
                    self._children_yang_names.add("interface-tracks")

                    self.ipsla_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                    self._children_yang_names.add("ipsla-tracks")

                    self.route_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"
                    self._children_yang_names.add("route-tracks")
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


    class TrackTypeIpv4Route(Entity):
        """
        Object Tracking Type IPV4 route info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeIpv4Route, self).__init__()

            self.yang_name = "track-type-ipv4-route"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-info" : ("track_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo)}

            self.track_info = YList(self)
            self._segment_path = lambda: "track-type-ipv4-route"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeIpv4Route, [], name, value)


        class TrackInfo(Entity):
            """
            track info
            
            .. attribute:: bool_tracks
            
            	boolean objects
            	**type**\:   :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks>`
            
            .. attribute:: delayed
            
            	Is the state change delay counter in progress
            	**type**\:   :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed>`
            
            .. attribute:: seconds_last_change
            
            	Seconds Last Change
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: state_change_counter
            
            	State Change Counter
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_down
            
            	User specified threshold lower limit
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_tracks
            
            	Threshold objects
            	**type**\:   :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks>`
            
            .. attribute:: threshold_up
            
            	User specified threshold upper limit
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: track_state
            
            	Track state
            	**type**\:  bool
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\:  str
            
            	**length:** 0..33
            
            .. attribute:: tracking_interaces
            
            	Tracking Interfaces
            	**type**\:   :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces>`
            
            .. attribute:: type
            
            	Track type
            	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo, self).__init__()

                self.yang_name = "track-info"
                self.yang_parent_name = "track-type-ipv4-route"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bool-tracks" : ("bool_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks), "delayed" : ("delayed", ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed), "threshold-tracks" : ("threshold_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks), "track-type-info" : ("track_type_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo), "tracking-interaces" : ("tracking_interaces", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces)}
                self._child_list_classes = {}

                self.seconds_last_change = YLeaf(YType.uint64, "seconds-last-change")

                self.state_change_counter = YLeaf(YType.uint32, "state-change-counter")

                self.threshold_down = YLeaf(YType.uint32, "threshold-down")

                self.threshold_up = YLeaf(YType.uint32, "threshold-up")

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.bool_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self._children_name_map["bool_tracks"] = "bool-tracks"
                self._children_yang_names.add("bool-tracks")

                self.delayed = ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed()
                self.delayed.parent = self
                self._children_name_map["delayed"] = "delayed"
                self._children_yang_names.add("delayed")

                self.threshold_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self._children_name_map["threshold_tracks"] = "threshold-tracks"
                self._children_yang_names.add("threshold-tracks")

                self.track_type_info = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")

                self.tracking_interaces = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self._children_name_map["tracking_interaces"] = "tracking-interaces"
                self._children_yang_names.add("tracking-interaces")
                self._segment_path = lambda: "track-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo, ['seconds_last_change', 'state_change_counter', 'threshold_down', 'threshold_up', 'track_state', 'tracke_name', 'type'], name, value)


            class BoolTracks(Entity):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks, self).__init__()

                    self.yang_name = "bool-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"bool-track-info" : ("bool_track_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo)}

                    self.bool_track_info = YList(self)
                    self._segment_path = lambda: "bool-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks, [], name, value)


                class BoolTrackInfo(Entity):
                    """
                    bool track info
                    
                    .. attribute:: object_name
                    
                    	Object Name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state
                    	**type**\:  bool
                    
                    .. attribute:: with_not
                    
                    	Track object with Not
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                        self.yang_name = "bool-track-info"
                        self.yang_parent_name = "bool-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.with_not = YLeaf(YType.boolean, "with-not")
                        self._segment_path = lambda: "bool-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/bool-tracks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


            class Delayed(Entity):
                """
                Is the state change delay counter in progress
                
                .. attribute:: time_remaining
                
                	The time remaining in seconds for the counter to trigger state change
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: track_state
                
                	State the track will transition to. Track state. True means track is up; False means track is down
                	**type**\:  bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed, self).__init__()

                    self.yang_name = "delayed"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    self.track_state = YLeaf(YType.boolean, "track-state")
                    self._segment_path = lambda: "delayed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


            class ThresholdTracks(Entity):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks, self).__init__()

                    self.yang_name = "threshold-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"threshold-track-info" : ("threshold_track_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo)}

                    self.threshold_track_info = YList(self)
                    self._segment_path = lambda: "threshold-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks, [], name, value)


                class ThresholdTrackInfo(Entity):
                    """
                    threshold track info
                    
                    .. attribute:: object_name
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state. True means track is up; False means track is down
                    	**type**\:  bool
                    
                    .. attribute:: weight
                    
                    	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.weight = YLeaf(YType.uint32, "weight")
                        self._segment_path = lambda: "threshold-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/threshold-tracks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks)}
                    self._child_list_classes = {}

                    self.discriminant = YLeaf(YType.enumeration, "discriminant")

                    self.bfd_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._children_yang_names.add("bfd-tracks")

                    self.interface_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"
                    self._children_yang_names.add("interface-tracks")

                    self.ipsla_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                    self._children_yang_names.add("ipsla-tracks")

                    self.route_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"
                    self._children_yang_names.add("route-tracks")
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


            class TrackingInteraces(Entity):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces, self).__init__()

                    self.yang_name = "tracking-interaces"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-tracking-info" : ("interface_tracking_info", ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo)}

                    self.interface_tracking_info = YList(self)
                    self._segment_path = lambda: "tracking-interaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces, [], name, value)


                class InterfaceTrackingInfo(Entity):
                    """
                    interface tracking info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracking-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/tracking-interaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


    class TrackTypeIpv4RouteBrief(Entity):
        """
        Object Tracking Type Ipv4 Route brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeIpv4RouteBrief, self).__init__()

            self.yang_name = "track-type-ipv4-route-brief"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-info-brief" : ("track_info_brief", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief)}

            self.track_info_brief = YList(self)
            self._segment_path = lambda: "track-type-ipv4-route-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief, [], name, value)


        class TrackInfoBrief(Entity):
            """
            track info brief
            
            .. attribute:: track_state
            
            	Track state
            	**type**\:  bool
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\:  str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief, self).__init__()

                self.yang_name = "track-info-brief"
                self.yang_parent_name = "track-type-ipv4-route-brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"track-type-info" : ("track_type_info", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo)}
                self._child_list_classes = {}

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.track_type_info = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")
                self._segment_path = lambda: "track-info-brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief, ['track_state', 'tracke_name', 'type'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)}
                    self._child_list_classes = {}

                    self.discriminant = YLeaf(YType.enumeration, "discriminant")

                    self.bfd_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._children_yang_names.add("bfd-tracks")

                    self.interface_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"
                    self._children_yang_names.add("interface-tracks")

                    self.ipsla_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                    self._children_yang_names.add("ipsla-tracks")

                    self.route_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"
                    self._children_yang_names.add("route-tracks")
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


    class TrackTypeRtrReachability(Entity):
        """
        Object Tracking Type RTR Reachability info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeRtrReachability, self).__init__()

            self.yang_name = "track-type-rtr-reachability"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-info" : ("track_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo)}

            self.track_info = YList(self)
            self._segment_path = lambda: "track-type-rtr-reachability"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeRtrReachability, [], name, value)


        class TrackInfo(Entity):
            """
            track info
            
            .. attribute:: bool_tracks
            
            	boolean objects
            	**type**\:   :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks>`
            
            .. attribute:: delayed
            
            	Is the state change delay counter in progress
            	**type**\:   :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed>`
            
            .. attribute:: seconds_last_change
            
            	Seconds Last Change
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: second
            
            .. attribute:: state_change_counter
            
            	State Change Counter
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_down
            
            	User specified threshold lower limit
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: threshold_tracks
            
            	Threshold objects
            	**type**\:   :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks>`
            
            .. attribute:: threshold_up
            
            	User specified threshold upper limit
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: track_state
            
            	Track state
            	**type**\:  bool
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\:  str
            
            	**length:** 0..33
            
            .. attribute:: tracking_interaces
            
            	Tracking Interfaces
            	**type**\:   :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces>`
            
            .. attribute:: type
            
            	Track type
            	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo, self).__init__()

                self.yang_name = "track-info"
                self.yang_parent_name = "track-type-rtr-reachability"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bool-tracks" : ("bool_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks), "delayed" : ("delayed", ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed), "threshold-tracks" : ("threshold_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks), "track-type-info" : ("track_type_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo), "tracking-interaces" : ("tracking_interaces", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces)}
                self._child_list_classes = {}

                self.seconds_last_change = YLeaf(YType.uint64, "seconds-last-change")

                self.state_change_counter = YLeaf(YType.uint32, "state-change-counter")

                self.threshold_down = YLeaf(YType.uint32, "threshold-down")

                self.threshold_up = YLeaf(YType.uint32, "threshold-up")

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.bool_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self._children_name_map["bool_tracks"] = "bool-tracks"
                self._children_yang_names.add("bool-tracks")

                self.delayed = ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed()
                self.delayed.parent = self
                self._children_name_map["delayed"] = "delayed"
                self._children_yang_names.add("delayed")

                self.threshold_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self._children_name_map["threshold_tracks"] = "threshold-tracks"
                self._children_yang_names.add("threshold-tracks")

                self.track_type_info = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")

                self.tracking_interaces = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self._children_name_map["tracking_interaces"] = "tracking-interaces"
                self._children_yang_names.add("tracking-interaces")
                self._segment_path = lambda: "track-info"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo, ['seconds_last_change', 'state_change_counter', 'threshold_down', 'threshold_up', 'track_state', 'tracke_name', 'type'], name, value)


            class BoolTracks(Entity):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks, self).__init__()

                    self.yang_name = "bool-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"bool-track-info" : ("bool_track_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo)}

                    self.bool_track_info = YList(self)
                    self._segment_path = lambda: "bool-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks, [], name, value)


                class BoolTrackInfo(Entity):
                    """
                    bool track info
                    
                    .. attribute:: object_name
                    
                    	Object Name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state
                    	**type**\:  bool
                    
                    .. attribute:: with_not
                    
                    	Track object with Not
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                        self.yang_name = "bool-track-info"
                        self.yang_parent_name = "bool-tracks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.with_not = YLeaf(YType.boolean, "with-not")
                        self._segment_path = lambda: "bool-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/bool-tracks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


            class Delayed(Entity):
                """
                Is the state change delay counter in progress
                
                .. attribute:: time_remaining
                
                	The time remaining in seconds for the counter to trigger state change
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: track_state
                
                	State the track will transition to. Track state. True means track is up; False means track is down
                	**type**\:  bool
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed, self).__init__()

                    self.yang_name = "delayed"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    self.track_state = YLeaf(YType.boolean, "track-state")
                    self._segment_path = lambda: "delayed"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


            class ThresholdTracks(Entity):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks, self).__init__()

                    self.yang_name = "threshold-tracks"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"threshold-track-info" : ("threshold_track_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo)}

                    self.threshold_track_info = YList(self)
                    self._segment_path = lambda: "threshold-tracks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks, [], name, value)


                class ThresholdTrackInfo(Entity):
                    """
                    threshold track info
                    
                    .. attribute:: object_name
                    
                    	Object name
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    .. attribute:: track_state
                    
                    	Track state. True means track is up; False means track is down
                    	**type**\:  bool
                    
                    .. attribute:: weight
                    
                    	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.weight = YLeaf(YType.uint32, "weight")
                        self._segment_path = lambda: "threshold-track-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/threshold-tracks/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks)}
                    self._child_list_classes = {}

                    self.discriminant = YLeaf(YType.enumeration, "discriminant")

                    self.bfd_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._children_yang_names.add("bfd-tracks")

                    self.interface_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"
                    self._children_yang_names.add("interface-tracks")

                    self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                    self._children_yang_names.add("ipsla-tracks")

                    self.route_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"
                    self._children_yang_names.add("route-tracks")
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


            class TrackingInteraces(Entity):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces, self).__init__()

                    self.yang_name = "tracking-interaces"
                    self.yang_parent_name = "track-info"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-tracking-info" : ("interface_tracking_info", ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo)}

                    self.interface_tracking_info = YList(self)
                    self._segment_path = lambda: "tracking-interaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces, [], name, value)


                class InterfaceTrackingInfo(Entity):
                    """
                    interface tracking info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracking-info"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/tracking-interaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)


    class TrackTypeRtrReachabilityBrief(Entity):
        """
        Object Tracking Type RTR Reachability brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.TrackTypeRtrReachabilityBrief, self).__init__()

            self.yang_name = "track-type-rtr-reachability-brief"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track-info-brief" : ("track_info_brief", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief)}

            self.track_info_brief = YList(self)
            self._segment_path = lambda: "track-type-rtr-reachability-brief"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief, [], name, value)


        class TrackInfoBrief(Entity):
            """
            track info brief
            
            .. attribute:: track_state
            
            	Track state
            	**type**\:  bool
            
            .. attribute:: track_type_info
            
            	Track type information
            	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo>`
            
            .. attribute:: tracke_name
            
            	Track Name
            	**type**\:  str
            
            	**length:** 0..33
            
            .. attribute:: type
            
            	Track type
            	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief, self).__init__()

                self.yang_name = "track-info-brief"
                self.yang_parent_name = "track-type-rtr-reachability-brief"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"track-type-info" : ("track_type_info", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo)}
                self._child_list_classes = {}

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.track_type_info = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")
                self._segment_path = lambda: "track-info-brief"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief, ['track_state', 'tracke_name', 'type'], name, value)


            class TrackTypeInfo(Entity):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                .. attribute:: interface_tracks
                
                	track type interface info
                	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks>`
                
                .. attribute:: ipsla_tracks
                
                	track type rtr info
                	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks>`
                
                .. attribute:: route_tracks
                
                	track type route info
                	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo, self).__init__()

                    self.yang_name = "track-type-info"
                    self.yang_parent_name = "track-info-brief"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks)}
                    self._child_list_classes = {}

                    self.discriminant = YLeaf(YType.enumeration, "discriminant")

                    self.bfd_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self._children_name_map["bfd_tracks"] = "bfd-tracks"
                    self._children_yang_names.add("bfd-tracks")

                    self.interface_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self._children_name_map["interface_tracks"] = "interface-tracks"
                    self._children_yang_names.add("interface-tracks")

                    self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                    self._children_yang_names.add("ipsla-tracks")

                    self.route_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self
                    self._children_name_map["route_tracks"] = "route-tracks"
                    self._children_yang_names.add("route-tracks")
                    self._segment_path = lambda: "track-type-info"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo, ['discriminant'], name, value)


                class BfdTracks(Entity):
                    """
                    track type bfdrtr info
                    
                    .. attribute:: debounce_count
                    
                    	Debounce Count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_address
                    
                    	Destination Address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: rate
                    
                    	Rate
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")
                        self._segment_path = lambda: "bfd-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                class InterfaceTracks(Entity):
                    """
                    track type interface info
                    
                    .. attribute:: interface_name
                    
                    	Interface Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")
                        self._segment_path = lambda: "interface-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                class IpslaTracks(Entity):
                    """
                    track type rtr info
                    
                    .. attribute:: ipsla_op_id
                    
                    	Op Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: return_code
                    
                    	Latest Return Code
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtt
                    
                    	Latest RTT
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")
                        self._segment_path = lambda: "ipsla-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                class RouteTracks(Entity):
                    """
                    track type route info
                    
                    .. attribute:: next_hop
                    
                    	Next Hop
                    	**type**\:  str
                    
                    	**length:** 0..120
                    
                    .. attribute:: prefix
                    
                    	Prefix
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prefix_length
                    
                    	Prefix Length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	VRF Name
                    	**type**\:  str
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")
                        self._segment_path = lambda: "route-tracks"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


    class Tracks(Entity):
        """
        Object Tracking Track table
        
        .. attribute:: track
        
        	Track name \- maximum 32 characters
        	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ObjectTracking.Tracks, self).__init__()

            self.yang_name = "tracks"
            self.yang_parent_name = "object-tracking"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"track" : ("track", ObjectTracking.Tracks.Track)}

            self.track = YList(self)
            self._segment_path = lambda: "tracks"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ObjectTracking.Tracks, [], name, value)


        class Track(Entity):
            """
            Track name \- maximum 32 characters
            
            .. attribute:: track_name  <key>
            
            	Track name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: track_info
            
            	track info
            	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ObjectTracking.Tracks.Track, self).__init__()

                self.yang_name = "track"
                self.yang_parent_name = "tracks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"track-info" : ("track_info", ObjectTracking.Tracks.Track.TrackInfo)}

                self.track_name = YLeaf(YType.str, "track-name")

                self.track_info = YList(self)
                self._segment_path = lambda: "track" + "[track-name='" + self.track_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/tracks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ObjectTracking.Tracks.Track, ['track_name'], name, value)


            class TrackInfo(Entity):
                """
                track info
                
                .. attribute:: bool_tracks
                
                	boolean objects
                	**type**\:   :py:class:`BoolTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.BoolTracks>`
                
                .. attribute:: delayed
                
                	Is the state change delay counter in progress
                	**type**\:   :py:class:`Delayed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.Delayed>`
                
                .. attribute:: seconds_last_change
                
                	Seconds Last Change
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: second
                
                .. attribute:: state_change_counter
                
                	State Change Counter
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: threshold_down
                
                	User specified threshold lower limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: threshold_tracks
                
                	Threshold objects
                	**type**\:   :py:class:`ThresholdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks>`
                
                .. attribute:: threshold_up
                
                	User specified threshold upper limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: track_state
                
                	Track state
                	**type**\:  bool
                
                .. attribute:: track_type_info
                
                	Track type information
                	**type**\:   :py:class:`TrackTypeInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo>`
                
                .. attribute:: tracke_name
                
                	Track Name
                	**type**\:  str
                
                	**length:** 0..33
                
                .. attribute:: tracking_interaces
                
                	Tracking Interfaces
                	**type**\:   :py:class:`TrackingInteraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces>`
                
                .. attribute:: type
                
                	Track type
                	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ObjectTracking.Tracks.Track.TrackInfo, self).__init__()

                    self.yang_name = "track-info"
                    self.yang_parent_name = "track"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"bool-tracks" : ("bool_tracks", ObjectTracking.Tracks.Track.TrackInfo.BoolTracks), "delayed" : ("delayed", ObjectTracking.Tracks.Track.TrackInfo.Delayed), "threshold-tracks" : ("threshold_tracks", ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks), "track-type-info" : ("track_type_info", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo), "tracking-interaces" : ("tracking_interaces", ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces)}
                    self._child_list_classes = {}

                    self.seconds_last_change = YLeaf(YType.uint64, "seconds-last-change")

                    self.state_change_counter = YLeaf(YType.uint32, "state-change-counter")

                    self.threshold_down = YLeaf(YType.uint32, "threshold-down")

                    self.threshold_up = YLeaf(YType.uint32, "threshold-up")

                    self.track_state = YLeaf(YType.boolean, "track-state")

                    self.tracke_name = YLeaf(YType.str, "tracke-name")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.bool_tracks = ObjectTracking.Tracks.Track.TrackInfo.BoolTracks()
                    self.bool_tracks.parent = self
                    self._children_name_map["bool_tracks"] = "bool-tracks"
                    self._children_yang_names.add("bool-tracks")

                    self.delayed = ObjectTracking.Tracks.Track.TrackInfo.Delayed()
                    self.delayed.parent = self
                    self._children_name_map["delayed"] = "delayed"
                    self._children_yang_names.add("delayed")

                    self.threshold_tracks = ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks()
                    self.threshold_tracks.parent = self
                    self._children_name_map["threshold_tracks"] = "threshold-tracks"
                    self._children_yang_names.add("threshold-tracks")

                    self.track_type_info = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self._children_name_map["track_type_info"] = "track-type-info"
                    self._children_yang_names.add("track-type-info")

                    self.tracking_interaces = ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces()
                    self.tracking_interaces.parent = self
                    self._children_name_map["tracking_interaces"] = "tracking-interaces"
                    self._children_yang_names.add("tracking-interaces")
                    self._segment_path = lambda: "track-info"

                def __setattr__(self, name, value):
                    self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo, ['seconds_last_change', 'state_change_counter', 'threshold_down', 'threshold_up', 'track_state', 'tracke_name', 'type'], name, value)


                class BoolTracks(Entity):
                    """
                    boolean objects
                    
                    .. attribute:: bool_track_info
                    
                    	bool track info
                    	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks, self).__init__()

                        self.yang_name = "bool-tracks"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"bool-track-info" : ("bool_track_info", ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo)}

                        self.bool_track_info = YList(self)
                        self._segment_path = lambda: "bool-tracks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks, [], name, value)


                    class BoolTrackInfo(Entity):
                        """
                        bool track info
                        
                        .. attribute:: object_name
                        
                        	Object Name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: track_state
                        
                        	Track state
                        	**type**\:  bool
                        
                        .. attribute:: with_not
                        
                        	Track object with Not
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'manageability-object-tracking-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo, self).__init__()

                            self.yang_name = "bool-track-info"
                            self.yang_parent_name = "bool-tracks"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.object_name = YLeaf(YType.str, "object-name")

                            self.track_state = YLeaf(YType.boolean, "track-state")

                            self.with_not = YLeaf(YType.boolean, "with-not")
                            self._segment_path = lambda: "bool-track-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo, ['object_name', 'track_state', 'with_not'], name, value)


                class Delayed(Entity):
                    """
                    Is the state change delay counter in progress
                    
                    .. attribute:: time_remaining
                    
                    	The time remaining in seconds for the counter to trigger state change
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: track_state
                    
                    	State the track will transition to. Track state. True means track is up; False means track is down
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.Delayed, self).__init__()

                        self.yang_name = "delayed"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                        self.track_state = YLeaf(YType.boolean, "track-state")
                        self._segment_path = lambda: "delayed"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.Delayed, ['time_remaining', 'track_state'], name, value)


                class ThresholdTracks(Entity):
                    """
                    Threshold objects
                    
                    .. attribute:: threshold_track_info
                    
                    	threshold track info
                    	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks, self).__init__()

                        self.yang_name = "threshold-tracks"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"threshold-track-info" : ("threshold_track_info", ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo)}

                        self.threshold_track_info = YList(self)
                        self._segment_path = lambda: "threshold-tracks"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks, [], name, value)


                    class ThresholdTrackInfo(Entity):
                        """
                        threshold track info
                        
                        .. attribute:: object_name
                        
                        	Object name
                        	**type**\:  str
                        
                        	**length:** 0..33
                        
                        .. attribute:: track_state
                        
                        	Track state. True means track is up; False means track is down
                        	**type**\:  bool
                        
                        .. attribute:: weight
                        
                        	Weight is the number assigned to a track object . In case of a type threshold weight( i.e. weighted sum list), weight is asigned by User at the time of configuration. In case of a type threshold percentage (i.e. percentage based list), weight is internally computed by (1/N)x100, where N is the number of objects in the list
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.object_name = YLeaf(YType.str, "object-name")

                            self.track_state = YLeaf(YType.boolean, "track-state")

                            self.weight = YLeaf(YType.uint32, "weight")
                            self._segment_path = lambda: "threshold-track-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo, ['object_name', 'track_state', 'weight'], name, value)


                class TrackTypeInfo(Entity):
                    """
                    Track type information
                    
                    .. attribute:: bfd_tracks
                    
                    	track type bfdrtr info
                    	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks>`
                    
                    .. attribute:: discriminant
                    
                    	discriminant
                    	**type**\:   :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.Track>`
                    
                    .. attribute:: interface_tracks
                    
                    	track type interface info
                    	**type**\:   :py:class:`InterfaceTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks>`
                    
                    .. attribute:: ipsla_tracks
                    
                    	track type rtr info
                    	**type**\:   :py:class:`IpslaTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks>`
                    
                    .. attribute:: route_tracks
                    
                    	track type route info
                    	**type**\:   :py:class:`RouteTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo, self).__init__()

                        self.yang_name = "track-type-info"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"bfd-tracks" : ("bfd_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks), "interface-tracks" : ("interface_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks), "ipsla-tracks" : ("ipsla_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks), "route-tracks" : ("route_tracks", ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks)}
                        self._child_list_classes = {}

                        self.discriminant = YLeaf(YType.enumeration, "discriminant")

                        self.bfd_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks()
                        self.bfd_tracks.parent = self
                        self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        self._children_yang_names.add("bfd-tracks")

                        self.interface_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks()
                        self.interface_tracks.parent = self
                        self._children_name_map["interface_tracks"] = "interface-tracks"
                        self._children_yang_names.add("interface-tracks")

                        self.ipsla_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks()
                        self.ipsla_tracks.parent = self
                        self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        self._children_yang_names.add("ipsla-tracks")

                        self.route_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks()
                        self.route_tracks.parent = self
                        self._children_name_map["route_tracks"] = "route-tracks"
                        self._children_yang_names.add("route-tracks")
                        self._segment_path = lambda: "track-type-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo, ['discriminant'], name, value)


                    class BfdTracks(Entity):
                        """
                        track type bfdrtr info
                        
                        .. attribute:: debounce_count
                        
                        	Debounce Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destination_address
                        
                        	Destination Address
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**length:** 0..120
                        
                        .. attribute:: rate
                        
                        	Rate
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                            self.destination_address = YLeaf(YType.uint32, "destination-address")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.rate = YLeaf(YType.uint32, "rate")
                            self._segment_path = lambda: "bfd-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks, ['debounce_count', 'destination_address', 'interface_name', 'rate'], name, value)


                    class InterfaceTracks(Entity):
                        """
                        track type interface info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "interface-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks, ['interface_name'], name, value)


                    class IpslaTracks(Entity):
                        """
                        track type rtr info
                        
                        .. attribute:: ipsla_op_id
                        
                        	Op Id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: return_code
                        
                        	Latest Return Code
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rtt
                        
                        	Latest RTT
                        	**type**\:  int
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                            self.return_code = YLeaf(YType.uint32, "return-code")

                            self.rtt = YLeaf(YType.uint32, "rtt")
                            self._segment_path = lambda: "ipsla-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks, ['ipsla_op_id', 'return_code', 'rtt'], name, value)


                    class RouteTracks(Entity):
                        """
                        track type route info
                        
                        .. attribute:: next_hop
                        
                        	Next Hop
                        	**type**\:  str
                        
                        	**length:** 0..120
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: prefix_length
                        
                        	Prefix Length
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf
                        
                        	VRF Name
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.next_hop = YLeaf(YType.str, "next-hop")

                            self.prefix = YLeaf(YType.uint32, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.vrf = YLeaf(YType.str, "vrf")
                            self._segment_path = lambda: "route-tracks"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks, ['next_hop', 'prefix', 'prefix_length', 'vrf'], name, value)


                class TrackingInteraces(Entity):
                    """
                    Tracking Interfaces
                    
                    .. attribute:: interface_tracking_info
                    
                    	interface tracking info
                    	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces, self).__init__()

                        self.yang_name = "tracking-interaces"
                        self.yang_parent_name = "track-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface-tracking-info" : ("interface_tracking_info", ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo)}

                        self.interface_tracking_info = YList(self)
                        self._segment_path = lambda: "tracking-interaces"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces, [], name, value)


                    class InterfaceTrackingInfo(Entity):
                        """
                        interface tracking info
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
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
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")
                            self._segment_path = lambda: "interface-tracking-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, ['interface_name'], name, value)

    def clone_ptr(self):
        self._top_entity = ObjectTracking()
        return self._top_entity

