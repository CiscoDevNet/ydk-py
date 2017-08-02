""" Cisco_IOS_XR_manageability_object_tracking_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package operational data.

This module contains definitions
for the following management objects\:
  object\-tracking\: Object Tracking operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.track_info = YList(self)

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
                        super(ObjectTracking.TrackTypeInterface, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackTypeInterface, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("seconds_last_change",
                                "state_change_counter",
                                "threshold_down",
                                "threshold_up",
                                "track_state",
                                "tracke_name",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackTypeInterface.TrackInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackTypeInterface.TrackInfo, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminant") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix


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

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("next_hop",
                                        "prefix",
                                        "prefix_length",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.next_hop.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.next_hop.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "next-hop"):
                            self.next_hop = value
                            self.next_hop.value_namespace = name_space
                            self.next_hop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix


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

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipsla_op_id",
                                        "return_code",
                                        "rtt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipsla_op_id.is_set or
                            self.return_code.is_set or
                            self.rtt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipsla_op_id.yfilter != YFilter.not_set or
                            self.return_code.yfilter != YFilter.not_set or
                            self.rtt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipsla-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                        if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.return_code.get_name_leafdata())
                        if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rtt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipsla-op-id"):
                            self.ipsla_op_id = value
                            self.ipsla_op_id.value_namespace = name_space
                            self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "return-code"):
                            self.return_code = value
                            self.return_code.value_namespace = name_space
                            self.return_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "rtt"):
                            self.rtt = value
                            self.rtt.value_namespace = name_space
                            self.rtt.value_namespace_prefix = name_space_prefix


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

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debounce_count",
                                        "destination_address",
                                        "interface_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debounce_count.is_set or
                            self.destination_address.is_set or
                            self.interface_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debounce_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debounce_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debounce-count"):
                            self.debounce_count = value
                            self.debounce_count.value_namespace = name_space
                            self.debounce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.discriminant.is_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                        (self.route_tracks is not None and self.route_tracks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminant.yfilter != YFilter.not_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                        (self.route_tracks is not None and self.route_tracks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-type-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminant.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bfd-tracks"):
                        if (self.bfd_tracks is None):
                            self.bfd_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks()
                            self.bfd_tracks.parent = self
                            self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        return self.bfd_tracks

                    if (child_yang_name == "interface-tracks"):
                        if (self.interface_tracks is None):
                            self.interface_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks()
                            self.interface_tracks.parent = self
                            self._children_name_map["interface_tracks"] = "interface-tracks"
                        return self.interface_tracks

                    if (child_yang_name == "ipsla-tracks"):
                        if (self.ipsla_tracks is None):
                            self.ipsla_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks()
                            self.ipsla_tracks.parent = self
                            self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        return self.ipsla_tracks

                    if (child_yang_name == "route-tracks"):
                        if (self.route_tracks is None):
                            self.route_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks()
                            self.route_tracks.parent = self
                            self._children_name_map["route_tracks"] = "route-tracks"
                        return self.route_tracks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminant"):
                        self.discriminant = value
                        self.discriminant.value_namespace = name_space
                        self.discriminant.value_namespace_prefix = name_space_prefix


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

                    self.bool_track_info = YList(self)

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
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks, self).__setattr__(name, value)


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

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.with_not = YLeaf(YType.boolean, "with-not")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "track_state",
                                        "with_not") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.track_state.is_set or
                            self.with_not.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set or
                            self.with_not.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bool-track-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/bool-tracks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())
                        if (self.with_not.is_set or self.with_not.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.with_not.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "track-state" or name == "with-not"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "with-not"):
                            self.with_not = value
                            self.with_not.value_namespace = name_space
                            self.with_not.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bool_track_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bool_track_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bool-tracks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bool-track-info"):
                        for c in self.bool_track_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bool_track_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bool-track-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.threshold_track_info = YList(self)

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
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks, self).__setattr__(name, value)


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

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.weight = YLeaf(YType.uint32, "weight")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "track_state",
                                        "weight") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.track_state.is_set or
                            self.weight.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set or
                            self.weight.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-track-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/threshold-tracks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())
                        if (self.weight.is_set or self.weight.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.weight.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "track-state" or name == "weight"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "weight"):
                            self.weight = value
                            self.weight.value_namespace = name_space
                            self.weight.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.threshold_track_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.threshold_track_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-tracks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "threshold-track-info"):
                        for c in self.threshold_track_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.threshold_track_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "threshold-track-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.interface_tracking_info = YList(self)

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
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracking-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/tracking-interaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_tracking_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_tracking_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tracking-interaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-tracking-info"):
                        for c in self.interface_tracking_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_tracking_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-tracking-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    self.track_state = YLeaf(YType.boolean, "track-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("time_remaining",
                                    "track_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeInterface.TrackInfo.Delayed, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeInterface.TrackInfo.Delayed, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.time_remaining.is_set or
                        self.track_state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.time_remaining.yfilter != YFilter.not_set or
                        self.track_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "delayed" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_remaining.get_name_leafdata())
                    if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.track_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "time-remaining" or name == "track-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "time-remaining"):
                        self.time_remaining = value
                        self.time_remaining.value_namespace = name_space
                        self.time_remaining.value_namespace_prefix = name_space_prefix
                    if(value_path == "track-state"):
                        self.track_state = value
                        self.track_state.value_namespace = name_space
                        self.track_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.seconds_last_change.is_set or
                    self.state_change_counter.is_set or
                    self.threshold_down.is_set or
                    self.threshold_up.is_set or
                    self.track_state.is_set or
                    self.tracke_name.is_set or
                    self.type.is_set or
                    (self.bool_tracks is not None and self.bool_tracks.has_data()) or
                    (self.delayed is not None and self.delayed.has_data()) or
                    (self.threshold_tracks is not None and self.threshold_tracks.has_data()) or
                    (self.track_type_info is not None and self.track_type_info.has_data()) or
                    (self.tracking_interaces is not None and self.tracking_interaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.seconds_last_change.yfilter != YFilter.not_set or
                    self.state_change_counter.yfilter != YFilter.not_set or
                    self.threshold_down.yfilter != YFilter.not_set or
                    self.threshold_up.yfilter != YFilter.not_set or
                    self.track_state.yfilter != YFilter.not_set or
                    self.tracke_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.bool_tracks is not None and self.bool_tracks.has_operation()) or
                    (self.delayed is not None and self.delayed.has_operation()) or
                    (self.threshold_tracks is not None and self.threshold_tracks.has_operation()) or
                    (self.track_type_info is not None and self.track_type_info.has_operation()) or
                    (self.tracking_interaces is not None and self.tracking_interaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.seconds_last_change.is_set or self.seconds_last_change.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.seconds_last_change.get_name_leafdata())
                if (self.state_change_counter.is_set or self.state_change_counter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state_change_counter.get_name_leafdata())
                if (self.threshold_down.is_set or self.threshold_down.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold_down.get_name_leafdata())
                if (self.threshold_up.is_set or self.threshold_up.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold_up.get_name_leafdata())
                if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_state.get_name_leafdata())
                if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tracke_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bool-tracks"):
                    if (self.bool_tracks is None):
                        self.bool_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks()
                        self.bool_tracks.parent = self
                        self._children_name_map["bool_tracks"] = "bool-tracks"
                    return self.bool_tracks

                if (child_yang_name == "delayed"):
                    if (self.delayed is None):
                        self.delayed = ObjectTracking.TrackTypeInterface.TrackInfo.Delayed()
                        self.delayed.parent = self
                        self._children_name_map["delayed"] = "delayed"
                    return self.delayed

                if (child_yang_name == "threshold-tracks"):
                    if (self.threshold_tracks is None):
                        self.threshold_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks()
                        self.threshold_tracks.parent = self
                        self._children_name_map["threshold_tracks"] = "threshold-tracks"
                    return self.threshold_tracks

                if (child_yang_name == "track-type-info"):
                    if (self.track_type_info is None):
                        self.track_type_info = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo()
                        self.track_type_info.parent = self
                        self._children_name_map["track_type_info"] = "track-type-info"
                    return self.track_type_info

                if (child_yang_name == "tracking-interaces"):
                    if (self.tracking_interaces is None):
                        self.tracking_interaces = ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces()
                        self.tracking_interaces.parent = self
                        self._children_name_map["tracking_interaces"] = "tracking-interaces"
                    return self.tracking_interaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bool-tracks" or name == "delayed" or name == "threshold-tracks" or name == "track-type-info" or name == "tracking-interaces" or name == "seconds-last-change" or name == "state-change-counter" or name == "threshold-down" or name == "threshold-up" or name == "track-state" or name == "tracke-name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "seconds-last-change"):
                    self.seconds_last_change = value
                    self.seconds_last_change.value_namespace = name_space
                    self.seconds_last_change.value_namespace_prefix = name_space_prefix
                if(value_path == "state-change-counter"):
                    self.state_change_counter = value
                    self.state_change_counter.value_namespace = name_space
                    self.state_change_counter.value_namespace_prefix = name_space_prefix
                if(value_path == "threshold-down"):
                    self.threshold_down = value
                    self.threshold_down.value_namespace = name_space
                    self.threshold_down.value_namespace_prefix = name_space_prefix
                if(value_path == "threshold-up"):
                    self.threshold_up = value
                    self.threshold_up.value_namespace = name_space
                    self.threshold_up.value_namespace_prefix = name_space_prefix
                if(value_path == "track-state"):
                    self.track_state = value
                    self.track_state.value_namespace = name_space
                    self.track_state.value_namespace_prefix = name_space_prefix
                if(value_path == "tracke-name"):
                    self.tracke_name = value
                    self.tracke_name.value_namespace = name_space
                    self.tracke_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-type-interface" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-info"):
                for c in self.track_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackTypeInterface.TrackInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track_brief = YList(self)

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
                        super(ObjectTracking.TrackBriefs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackBriefs, self).__setattr__(name, value)


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

                self.track_name = YLeaf(YType.str, "track-name")

                self.track_info_brief = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("track_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackBriefs.TrackBrief, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackBriefs.TrackBrief, self).__setattr__(name, value)


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

                    self.track_state = YLeaf(YType.boolean, "track-state")

                    self.tracke_name = YLeaf(YType.str, "tracke-name")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.track_type_info = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self._children_name_map["track_type_info"] = "track-type-info"
                    self._children_yang_names.add("track-type-info")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("track_state",
                                    "tracke_name",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("discriminant") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)


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

                            self.interface_name = YLeaf(YType.str, "interface-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix


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

                            self.next_hop = YLeaf(YType.str, "next-hop")

                            self.prefix = YLeaf(YType.uint32, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.vrf = YLeaf(YType.str, "vrf")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("next_hop",
                                            "prefix",
                                            "prefix_length",
                                            "vrf") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.next_hop.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set or
                                self.vrf.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.next_hop.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.vrf.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "route-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "next-hop"):
                                self.next_hop = value
                                self.next_hop.value_namespace = name_space
                                self.next_hop.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf"):
                                self.vrf = value
                                self.vrf.value_namespace = name_space
                                self.vrf.value_namespace_prefix = name_space_prefix


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

                            self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                            self.return_code = YLeaf(YType.uint32, "return-code")

                            self.rtt = YLeaf(YType.uint32, "rtt")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipsla_op_id",
                                            "return_code",
                                            "rtt") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ipsla_op_id.is_set or
                                self.return_code.is_set or
                                self.rtt.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipsla_op_id.yfilter != YFilter.not_set or
                                self.return_code.yfilter != YFilter.not_set or
                                self.rtt.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipsla-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                            if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.return_code.get_name_leafdata())
                            if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rtt.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipsla-op-id"):
                                self.ipsla_op_id = value
                                self.ipsla_op_id.value_namespace = name_space
                                self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "return-code"):
                                self.return_code = value
                                self.return_code.value_namespace = name_space
                                self.return_code.value_namespace_prefix = name_space_prefix
                            if(value_path == "rtt"):
                                self.rtt = value
                                self.rtt.value_namespace = name_space
                                self.rtt.value_namespace_prefix = name_space_prefix


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

                            self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                            self.destination_address = YLeaf(YType.uint32, "destination-address")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.rate = YLeaf(YType.uint32, "rate")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("debounce_count",
                                            "destination_address",
                                            "interface_name",
                                            "rate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.debounce_count.is_set or
                                self.destination_address.is_set or
                                self.interface_name.is_set or
                                self.rate.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.debounce_count.yfilter != YFilter.not_set or
                                self.destination_address.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.rate.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bfd-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.debounce_count.get_name_leafdata())
                            if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "debounce-count"):
                                self.debounce_count = value
                                self.debounce_count.value_namespace = name_space
                                self.debounce_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate"):
                                self.rate = value
                                self.rate.value_namespace = name_space
                                self.rate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.discriminant.is_set or
                            (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                            (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                            (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                            (self.route_tracks is not None and self.route_tracks.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.discriminant.yfilter != YFilter.not_set or
                            (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                            (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                            (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                            (self.route_tracks is not None and self.route_tracks.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "track-type-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discriminant.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "bfd-tracks"):
                            if (self.bfd_tracks is None):
                                self.bfd_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                                self.bfd_tracks.parent = self
                                self._children_name_map["bfd_tracks"] = "bfd-tracks"
                            return self.bfd_tracks

                        if (child_yang_name == "interface-tracks"):
                            if (self.interface_tracks is None):
                                self.interface_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                                self.interface_tracks.parent = self
                                self._children_name_map["interface_tracks"] = "interface-tracks"
                            return self.interface_tracks

                        if (child_yang_name == "ipsla-tracks"):
                            if (self.ipsla_tracks is None):
                                self.ipsla_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                                self.ipsla_tracks.parent = self
                                self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                            return self.ipsla_tracks

                        if (child_yang_name == "route-tracks"):
                            if (self.route_tracks is None):
                                self.route_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                                self.route_tracks.parent = self
                                self._children_name_map["route_tracks"] = "route-tracks"
                            return self.route_tracks

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "discriminant"):
                            self.discriminant = value
                            self.discriminant.value_namespace = name_space
                            self.discriminant.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.track_state.is_set or
                        self.tracke_name.is_set or
                        self.type.is_set or
                        (self.track_type_info is not None and self.track_type_info.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.track_state.yfilter != YFilter.not_set or
                        self.tracke_name.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        (self.track_type_info is not None and self.track_type_info.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-info-brief" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.track_state.get_name_leafdata())
                    if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracke_name.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "track-type-info"):
                        if (self.track_type_info is None):
                            self.track_type_info = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo()
                            self.track_type_info.parent = self
                            self._children_name_map["track_type_info"] = "track-type-info"
                        return self.track_type_info

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "track-type-info" or name == "track-state" or name == "tracke-name" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "track-state"):
                        self.track_state = value
                        self.track_state.value_namespace = name_space
                        self.track_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracke-name"):
                        self.tracke_name = value
                        self.tracke_name.value_namespace = name_space
                        self.tracke_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.track_info_brief:
                    if (c.has_data()):
                        return True
                return self.track_name.is_set

            def has_operation(self):
                for c in self.track_info_brief:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.track_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-brief" + "[track-name='" + self.track_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-briefs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-info-brief"):
                    for c in self.track_info_brief:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.track_info_brief.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-info-brief" or name == "track-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "track-name"):
                    self.track_name = value
                    self.track_name.value_namespace = name_space
                    self.track_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_brief:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_brief:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-briefs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-brief"):
                for c in self.track_brief:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackBriefs.TrackBrief()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_brief.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-brief"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track_info = YList(self)

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
                        super(ObjectTracking.TrackTypeRtrReachability, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackTypeRtrReachability, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("seconds_last_change",
                                "state_change_counter",
                                "threshold_down",
                                "threshold_up",
                                "track_state",
                                "tracke_name",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackTypeRtrReachability.TrackInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackTypeRtrReachability.TrackInfo, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminant") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix


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

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("next_hop",
                                        "prefix",
                                        "prefix_length",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.next_hop.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.next_hop.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "next-hop"):
                            self.next_hop = value
                            self.next_hop.value_namespace = name_space
                            self.next_hop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix


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

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipsla_op_id",
                                        "return_code",
                                        "rtt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipsla_op_id.is_set or
                            self.return_code.is_set or
                            self.rtt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipsla_op_id.yfilter != YFilter.not_set or
                            self.return_code.yfilter != YFilter.not_set or
                            self.rtt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipsla-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                        if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.return_code.get_name_leafdata())
                        if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rtt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipsla-op-id"):
                            self.ipsla_op_id = value
                            self.ipsla_op_id.value_namespace = name_space
                            self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "return-code"):
                            self.return_code = value
                            self.return_code.value_namespace = name_space
                            self.return_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "rtt"):
                            self.rtt = value
                            self.rtt.value_namespace = name_space
                            self.rtt.value_namespace_prefix = name_space_prefix


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

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debounce_count",
                                        "destination_address",
                                        "interface_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debounce_count.is_set or
                            self.destination_address.is_set or
                            self.interface_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debounce_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debounce_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debounce-count"):
                            self.debounce_count = value
                            self.debounce_count.value_namespace = name_space
                            self.debounce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.discriminant.is_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                        (self.route_tracks is not None and self.route_tracks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminant.yfilter != YFilter.not_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                        (self.route_tracks is not None and self.route_tracks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-type-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminant.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bfd-tracks"):
                        if (self.bfd_tracks is None):
                            self.bfd_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks()
                            self.bfd_tracks.parent = self
                            self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        return self.bfd_tracks

                    if (child_yang_name == "interface-tracks"):
                        if (self.interface_tracks is None):
                            self.interface_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks()
                            self.interface_tracks.parent = self
                            self._children_name_map["interface_tracks"] = "interface-tracks"
                        return self.interface_tracks

                    if (child_yang_name == "ipsla-tracks"):
                        if (self.ipsla_tracks is None):
                            self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks()
                            self.ipsla_tracks.parent = self
                            self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        return self.ipsla_tracks

                    if (child_yang_name == "route-tracks"):
                        if (self.route_tracks is None):
                            self.route_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks()
                            self.route_tracks.parent = self
                            self._children_name_map["route_tracks"] = "route-tracks"
                        return self.route_tracks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminant"):
                        self.discriminant = value
                        self.discriminant.value_namespace = name_space
                        self.discriminant.value_namespace_prefix = name_space_prefix


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

                    self.bool_track_info = YList(self)

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
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks, self).__setattr__(name, value)


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

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.with_not = YLeaf(YType.boolean, "with-not")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "track_state",
                                        "with_not") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.track_state.is_set or
                            self.with_not.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set or
                            self.with_not.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bool-track-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/bool-tracks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())
                        if (self.with_not.is_set or self.with_not.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.with_not.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "track-state" or name == "with-not"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "with-not"):
                            self.with_not = value
                            self.with_not.value_namespace = name_space
                            self.with_not.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bool_track_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bool_track_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bool-tracks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bool-track-info"):
                        for c in self.bool_track_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bool_track_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bool-track-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.threshold_track_info = YList(self)

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
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks, self).__setattr__(name, value)


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

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.weight = YLeaf(YType.uint32, "weight")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "track_state",
                                        "weight") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.track_state.is_set or
                            self.weight.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set or
                            self.weight.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-track-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/threshold-tracks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())
                        if (self.weight.is_set or self.weight.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.weight.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "track-state" or name == "weight"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "weight"):
                            self.weight = value
                            self.weight.value_namespace = name_space
                            self.weight.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.threshold_track_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.threshold_track_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-tracks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "threshold-track-info"):
                        for c in self.threshold_track_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.threshold_track_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "threshold-track-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.interface_tracking_info = YList(self)

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
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracking-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/tracking-interaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_tracking_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_tracking_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tracking-interaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-tracking-info"):
                        for c in self.interface_tracking_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_tracking_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-tracking-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    self.track_state = YLeaf(YType.boolean, "track-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("time_remaining",
                                    "track_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.time_remaining.is_set or
                        self.track_state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.time_remaining.yfilter != YFilter.not_set or
                        self.track_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "delayed" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_remaining.get_name_leafdata())
                    if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.track_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "time-remaining" or name == "track-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "time-remaining"):
                        self.time_remaining = value
                        self.time_remaining.value_namespace = name_space
                        self.time_remaining.value_namespace_prefix = name_space_prefix
                    if(value_path == "track-state"):
                        self.track_state = value
                        self.track_state.value_namespace = name_space
                        self.track_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.seconds_last_change.is_set or
                    self.state_change_counter.is_set or
                    self.threshold_down.is_set or
                    self.threshold_up.is_set or
                    self.track_state.is_set or
                    self.tracke_name.is_set or
                    self.type.is_set or
                    (self.bool_tracks is not None and self.bool_tracks.has_data()) or
                    (self.delayed is not None and self.delayed.has_data()) or
                    (self.threshold_tracks is not None and self.threshold_tracks.has_data()) or
                    (self.track_type_info is not None and self.track_type_info.has_data()) or
                    (self.tracking_interaces is not None and self.tracking_interaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.seconds_last_change.yfilter != YFilter.not_set or
                    self.state_change_counter.yfilter != YFilter.not_set or
                    self.threshold_down.yfilter != YFilter.not_set or
                    self.threshold_up.yfilter != YFilter.not_set or
                    self.track_state.yfilter != YFilter.not_set or
                    self.tracke_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.bool_tracks is not None and self.bool_tracks.has_operation()) or
                    (self.delayed is not None and self.delayed.has_operation()) or
                    (self.threshold_tracks is not None and self.threshold_tracks.has_operation()) or
                    (self.track_type_info is not None and self.track_type_info.has_operation()) or
                    (self.tracking_interaces is not None and self.tracking_interaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.seconds_last_change.is_set or self.seconds_last_change.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.seconds_last_change.get_name_leafdata())
                if (self.state_change_counter.is_set or self.state_change_counter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state_change_counter.get_name_leafdata())
                if (self.threshold_down.is_set or self.threshold_down.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold_down.get_name_leafdata())
                if (self.threshold_up.is_set or self.threshold_up.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold_up.get_name_leafdata())
                if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_state.get_name_leafdata())
                if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tracke_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bool-tracks"):
                    if (self.bool_tracks is None):
                        self.bool_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks()
                        self.bool_tracks.parent = self
                        self._children_name_map["bool_tracks"] = "bool-tracks"
                    return self.bool_tracks

                if (child_yang_name == "delayed"):
                    if (self.delayed is None):
                        self.delayed = ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed()
                        self.delayed.parent = self
                        self._children_name_map["delayed"] = "delayed"
                    return self.delayed

                if (child_yang_name == "threshold-tracks"):
                    if (self.threshold_tracks is None):
                        self.threshold_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks()
                        self.threshold_tracks.parent = self
                        self._children_name_map["threshold_tracks"] = "threshold-tracks"
                    return self.threshold_tracks

                if (child_yang_name == "track-type-info"):
                    if (self.track_type_info is None):
                        self.track_type_info = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo()
                        self.track_type_info.parent = self
                        self._children_name_map["track_type_info"] = "track-type-info"
                    return self.track_type_info

                if (child_yang_name == "tracking-interaces"):
                    if (self.tracking_interaces is None):
                        self.tracking_interaces = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces()
                        self.tracking_interaces.parent = self
                        self._children_name_map["tracking_interaces"] = "tracking-interaces"
                    return self.tracking_interaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bool-tracks" or name == "delayed" or name == "threshold-tracks" or name == "track-type-info" or name == "tracking-interaces" or name == "seconds-last-change" or name == "state-change-counter" or name == "threshold-down" or name == "threshold-up" or name == "track-state" or name == "tracke-name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "seconds-last-change"):
                    self.seconds_last_change = value
                    self.seconds_last_change.value_namespace = name_space
                    self.seconds_last_change.value_namespace_prefix = name_space_prefix
                if(value_path == "state-change-counter"):
                    self.state_change_counter = value
                    self.state_change_counter.value_namespace = name_space
                    self.state_change_counter.value_namespace_prefix = name_space_prefix
                if(value_path == "threshold-down"):
                    self.threshold_down = value
                    self.threshold_down.value_namespace = name_space
                    self.threshold_down.value_namespace_prefix = name_space_prefix
                if(value_path == "threshold-up"):
                    self.threshold_up = value
                    self.threshold_up.value_namespace = name_space
                    self.threshold_up.value_namespace_prefix = name_space_prefix
                if(value_path == "track-state"):
                    self.track_state = value
                    self.track_state.value_namespace = name_space
                    self.track_state.value_namespace_prefix = name_space_prefix
                if(value_path == "tracke-name"):
                    self.tracke_name = value
                    self.tracke_name.value_namespace = name_space
                    self.tracke_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-type-rtr-reachability" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-info"):
                for c in self.track_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackTypeRtrReachability.TrackInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track_info_brief = YList(self)

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
                        super(ObjectTracking.TrackTypeRtrReachabilityBrief, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackTypeRtrReachabilityBrief, self).__setattr__(name, value)


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

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.track_type_info = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("track_state",
                                "tracke_name",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminant") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix


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

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("next_hop",
                                        "prefix",
                                        "prefix_length",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.next_hop.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.next_hop.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "next-hop"):
                            self.next_hop = value
                            self.next_hop.value_namespace = name_space
                            self.next_hop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix


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

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipsla_op_id",
                                        "return_code",
                                        "rtt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipsla_op_id.is_set or
                            self.return_code.is_set or
                            self.rtt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipsla_op_id.yfilter != YFilter.not_set or
                            self.return_code.yfilter != YFilter.not_set or
                            self.rtt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipsla-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                        if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.return_code.get_name_leafdata())
                        if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rtt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipsla-op-id"):
                            self.ipsla_op_id = value
                            self.ipsla_op_id.value_namespace = name_space
                            self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "return-code"):
                            self.return_code = value
                            self.return_code.value_namespace = name_space
                            self.return_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "rtt"):
                            self.rtt = value
                            self.rtt.value_namespace = name_space
                            self.rtt.value_namespace_prefix = name_space_prefix


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

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debounce_count",
                                        "destination_address",
                                        "interface_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debounce_count.is_set or
                            self.destination_address.is_set or
                            self.interface_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debounce_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debounce_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debounce-count"):
                            self.debounce_count = value
                            self.debounce_count.value_namespace = name_space
                            self.debounce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.discriminant.is_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                        (self.route_tracks is not None and self.route_tracks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminant.yfilter != YFilter.not_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                        (self.route_tracks is not None and self.route_tracks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-type-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/track-info-brief/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminant.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bfd-tracks"):
                        if (self.bfd_tracks is None):
                            self.bfd_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                            self.bfd_tracks.parent = self
                            self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        return self.bfd_tracks

                    if (child_yang_name == "interface-tracks"):
                        if (self.interface_tracks is None):
                            self.interface_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                            self.interface_tracks.parent = self
                            self._children_name_map["interface_tracks"] = "interface-tracks"
                        return self.interface_tracks

                    if (child_yang_name == "ipsla-tracks"):
                        if (self.ipsla_tracks is None):
                            self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                            self.ipsla_tracks.parent = self
                            self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        return self.ipsla_tracks

                    if (child_yang_name == "route-tracks"):
                        if (self.route_tracks is None):
                            self.route_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                            self.route_tracks.parent = self
                            self._children_name_map["route_tracks"] = "route-tracks"
                        return self.route_tracks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminant"):
                        self.discriminant = value
                        self.discriminant.value_namespace = name_space
                        self.discriminant.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.track_state.is_set or
                    self.tracke_name.is_set or
                    self.type.is_set or
                    (self.track_type_info is not None and self.track_type_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.track_state.yfilter != YFilter.not_set or
                    self.tracke_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.track_type_info is not None and self.track_type_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-info-brief" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-rtr-reachability-brief/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_state.get_name_leafdata())
                if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tracke_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-type-info"):
                    if (self.track_type_info is None):
                        self.track_type_info = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo()
                        self.track_type_info.parent = self
                        self._children_name_map["track_type_info"] = "track-type-info"
                    return self.track_type_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-type-info" or name == "track-state" or name == "tracke-name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "track-state"):
                    self.track_state = value
                    self.track_state.value_namespace = name_space
                    self.track_state.value_namespace_prefix = name_space_prefix
                if(value_path == "tracke-name"):
                    self.tracke_name = value
                    self.tracke_name.value_namespace = name_space
                    self.tracke_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_info_brief:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_info_brief:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-type-rtr-reachability-brief" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-info-brief"):
                for c in self.track_info_brief:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_info_brief.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-info-brief"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track = YList(self)

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
                        super(ObjectTracking.Tracks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.Tracks, self).__setattr__(name, value)


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

                self.track_name = YLeaf(YType.str, "track-name")

                self.track_info = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("track_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.Tracks.Track, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.Tracks.Track, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("seconds_last_change",
                                    "state_change_counter",
                                    "threshold_down",
                                    "threshold_up",
                                    "track_state",
                                    "tracke_name",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.Tracks.Track.TrackInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.Tracks.Track.TrackInfo, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("discriminant") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)


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

                            self.interface_name = YLeaf(YType.str, "interface-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix


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

                            self.next_hop = YLeaf(YType.str, "next-hop")

                            self.prefix = YLeaf(YType.uint32, "prefix")

                            self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                            self.vrf = YLeaf(YType.str, "vrf")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("next_hop",
                                            "prefix",
                                            "prefix_length",
                                            "vrf") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.next_hop.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set or
                                self.vrf.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.next_hop.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.vrf.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "route-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "next-hop"):
                                self.next_hop = value
                                self.next_hop.value_namespace = name_space
                                self.next_hop.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf"):
                                self.vrf = value
                                self.vrf.value_namespace = name_space
                                self.vrf.value_namespace_prefix = name_space_prefix


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

                            self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                            self.return_code = YLeaf(YType.uint32, "return-code")

                            self.rtt = YLeaf(YType.uint32, "rtt")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipsla_op_id",
                                            "return_code",
                                            "rtt") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ipsla_op_id.is_set or
                                self.return_code.is_set or
                                self.rtt.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipsla_op_id.yfilter != YFilter.not_set or
                                self.return_code.yfilter != YFilter.not_set or
                                self.rtt.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipsla-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                            if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.return_code.get_name_leafdata())
                            if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rtt.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipsla-op-id"):
                                self.ipsla_op_id = value
                                self.ipsla_op_id.value_namespace = name_space
                                self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "return-code"):
                                self.return_code = value
                                self.return_code.value_namespace = name_space
                                self.return_code.value_namespace_prefix = name_space_prefix
                            if(value_path == "rtt"):
                                self.rtt = value
                                self.rtt.value_namespace = name_space
                                self.rtt.value_namespace_prefix = name_space_prefix


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

                            self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                            self.destination_address = YLeaf(YType.uint32, "destination-address")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.rate = YLeaf(YType.uint32, "rate")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("debounce_count",
                                            "destination_address",
                                            "interface_name",
                                            "rate") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.debounce_count.is_set or
                                self.destination_address.is_set or
                                self.interface_name.is_set or
                                self.rate.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.debounce_count.yfilter != YFilter.not_set or
                                self.destination_address.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.rate.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bfd-tracks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.debounce_count.get_name_leafdata())
                            if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_address.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.rate.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "debounce-count"):
                                self.debounce_count = value
                                self.debounce_count.value_namespace = name_space
                                self.debounce_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "destination-address"):
                                self.destination_address = value
                                self.destination_address.value_namespace = name_space
                                self.destination_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "rate"):
                                self.rate = value
                                self.rate.value_namespace = name_space
                                self.rate.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.discriminant.is_set or
                            (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                            (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                            (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                            (self.route_tracks is not None and self.route_tracks.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.discriminant.yfilter != YFilter.not_set or
                            (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                            (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                            (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                            (self.route_tracks is not None and self.route_tracks.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "track-type-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discriminant.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "bfd-tracks"):
                            if (self.bfd_tracks is None):
                                self.bfd_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks()
                                self.bfd_tracks.parent = self
                                self._children_name_map["bfd_tracks"] = "bfd-tracks"
                            return self.bfd_tracks

                        if (child_yang_name == "interface-tracks"):
                            if (self.interface_tracks is None):
                                self.interface_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks()
                                self.interface_tracks.parent = self
                                self._children_name_map["interface_tracks"] = "interface-tracks"
                            return self.interface_tracks

                        if (child_yang_name == "ipsla-tracks"):
                            if (self.ipsla_tracks is None):
                                self.ipsla_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks()
                                self.ipsla_tracks.parent = self
                                self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                            return self.ipsla_tracks

                        if (child_yang_name == "route-tracks"):
                            if (self.route_tracks is None):
                                self.route_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks()
                                self.route_tracks.parent = self
                                self._children_name_map["route_tracks"] = "route-tracks"
                            return self.route_tracks

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "discriminant"):
                            self.discriminant = value
                            self.discriminant.value_namespace = name_space
                            self.discriminant.value_namespace_prefix = name_space_prefix


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

                        self.bool_track_info = YList(self)

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
                                    super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks, self).__setattr__(name, value)


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

                            self.object_name = YLeaf(YType.str, "object-name")

                            self.track_state = YLeaf(YType.boolean, "track-state")

                            self.with_not = YLeaf(YType.boolean, "with-not")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("object_name",
                                            "track_state",
                                            "with_not") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.object_name.is_set or
                                self.track_state.is_set or
                                self.with_not.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.object_name.yfilter != YFilter.not_set or
                                self.track_state.yfilter != YFilter.not_set or
                                self.with_not.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bool-track-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.object_name.get_name_leafdata())
                            if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.track_state.get_name_leafdata())
                            if (self.with_not.is_set or self.with_not.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.with_not.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "object-name" or name == "track-state" or name == "with-not"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "object-name"):
                                self.object_name = value
                                self.object_name.value_namespace = name_space
                                self.object_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "track-state"):
                                self.track_state = value
                                self.track_state.value_namespace = name_space
                                self.track_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "with-not"):
                                self.with_not = value
                                self.with_not.value_namespace = name_space
                                self.with_not.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.bool_track_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.bool_track_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bool-tracks" + path_buffer

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

                        if (child_yang_name == "bool-track-info"):
                            for c in self.bool_track_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.bool_track_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bool-track-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.threshold_track_info = YList(self)

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
                                    super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks, self).__setattr__(name, value)


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

                            self.object_name = YLeaf(YType.str, "object-name")

                            self.track_state = YLeaf(YType.boolean, "track-state")

                            self.weight = YLeaf(YType.uint32, "weight")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("object_name",
                                            "track_state",
                                            "weight") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.object_name.is_set or
                                self.track_state.is_set or
                                self.weight.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.object_name.yfilter != YFilter.not_set or
                                self.track_state.yfilter != YFilter.not_set or
                                self.weight.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "threshold-track-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.object_name.get_name_leafdata())
                            if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.track_state.get_name_leafdata())
                            if (self.weight.is_set or self.weight.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.weight.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "object-name" or name == "track-state" or name == "weight"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "object-name"):
                                self.object_name = value
                                self.object_name.value_namespace = name_space
                                self.object_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "track-state"):
                                self.track_state = value
                                self.track_state.value_namespace = name_space
                                self.track_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "weight"):
                                self.weight = value
                                self.weight.value_namespace = name_space
                                self.weight.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.threshold_track_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.threshold_track_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-tracks" + path_buffer

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

                        if (child_yang_name == "threshold-track-info"):
                            for c in self.threshold_track_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.threshold_track_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "threshold-track-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.interface_tracking_info = YList(self)

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
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces, self).__setattr__(name, value)


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

                            self.interface_name = YLeaf(YType.str, "interface-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-tracking-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.interface_tracking_info:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.interface_tracking_info:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tracking-interaces" + path_buffer

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

                        if (child_yang_name == "interface-tracking-info"):
                            for c in self.interface_tracking_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface_tracking_info.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-tracking-info"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("time_remaining",
                                        "track_state") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.Tracks.Track.TrackInfo.Delayed, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.Tracks.Track.TrackInfo.Delayed, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.time_remaining.is_set or
                            self.track_state.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.time_remaining.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "delayed" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_remaining.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "time-remaining" or name == "track-state"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "time-remaining"):
                            self.time_remaining = value
                            self.time_remaining.value_namespace = name_space
                            self.time_remaining.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.seconds_last_change.is_set or
                        self.state_change_counter.is_set or
                        self.threshold_down.is_set or
                        self.threshold_up.is_set or
                        self.track_state.is_set or
                        self.tracke_name.is_set or
                        self.type.is_set or
                        (self.bool_tracks is not None and self.bool_tracks.has_data()) or
                        (self.delayed is not None and self.delayed.has_data()) or
                        (self.threshold_tracks is not None and self.threshold_tracks.has_data()) or
                        (self.track_type_info is not None and self.track_type_info.has_data()) or
                        (self.tracking_interaces is not None and self.tracking_interaces.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.seconds_last_change.yfilter != YFilter.not_set or
                        self.state_change_counter.yfilter != YFilter.not_set or
                        self.threshold_down.yfilter != YFilter.not_set or
                        self.threshold_up.yfilter != YFilter.not_set or
                        self.track_state.yfilter != YFilter.not_set or
                        self.tracke_name.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        (self.bool_tracks is not None and self.bool_tracks.has_operation()) or
                        (self.delayed is not None and self.delayed.has_operation()) or
                        (self.threshold_tracks is not None and self.threshold_tracks.has_operation()) or
                        (self.track_type_info is not None and self.track_type_info.has_operation()) or
                        (self.tracking_interaces is not None and self.tracking_interaces.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.seconds_last_change.is_set or self.seconds_last_change.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.seconds_last_change.get_name_leafdata())
                    if (self.state_change_counter.is_set or self.state_change_counter.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_change_counter.get_name_leafdata())
                    if (self.threshold_down.is_set or self.threshold_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.threshold_down.get_name_leafdata())
                    if (self.threshold_up.is_set or self.threshold_up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.threshold_up.get_name_leafdata())
                    if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.track_state.get_name_leafdata())
                    if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tracke_name.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bool-tracks"):
                        if (self.bool_tracks is None):
                            self.bool_tracks = ObjectTracking.Tracks.Track.TrackInfo.BoolTracks()
                            self.bool_tracks.parent = self
                            self._children_name_map["bool_tracks"] = "bool-tracks"
                        return self.bool_tracks

                    if (child_yang_name == "delayed"):
                        if (self.delayed is None):
                            self.delayed = ObjectTracking.Tracks.Track.TrackInfo.Delayed()
                            self.delayed.parent = self
                            self._children_name_map["delayed"] = "delayed"
                        return self.delayed

                    if (child_yang_name == "threshold-tracks"):
                        if (self.threshold_tracks is None):
                            self.threshold_tracks = ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks()
                            self.threshold_tracks.parent = self
                            self._children_name_map["threshold_tracks"] = "threshold-tracks"
                        return self.threshold_tracks

                    if (child_yang_name == "track-type-info"):
                        if (self.track_type_info is None):
                            self.track_type_info = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo()
                            self.track_type_info.parent = self
                            self._children_name_map["track_type_info"] = "track-type-info"
                        return self.track_type_info

                    if (child_yang_name == "tracking-interaces"):
                        if (self.tracking_interaces is None):
                            self.tracking_interaces = ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces()
                            self.tracking_interaces.parent = self
                            self._children_name_map["tracking_interaces"] = "tracking-interaces"
                        return self.tracking_interaces

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bool-tracks" or name == "delayed" or name == "threshold-tracks" or name == "track-type-info" or name == "tracking-interaces" or name == "seconds-last-change" or name == "state-change-counter" or name == "threshold-down" or name == "threshold-up" or name == "track-state" or name == "tracke-name" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "seconds-last-change"):
                        self.seconds_last_change = value
                        self.seconds_last_change.value_namespace = name_space
                        self.seconds_last_change.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-change-counter"):
                        self.state_change_counter = value
                        self.state_change_counter.value_namespace = name_space
                        self.state_change_counter.value_namespace_prefix = name_space_prefix
                    if(value_path == "threshold-down"):
                        self.threshold_down = value
                        self.threshold_down.value_namespace = name_space
                        self.threshold_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "threshold-up"):
                        self.threshold_up = value
                        self.threshold_up.value_namespace = name_space
                        self.threshold_up.value_namespace_prefix = name_space_prefix
                    if(value_path == "track-state"):
                        self.track_state = value
                        self.track_state.value_namespace = name_space
                        self.track_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "tracke-name"):
                        self.tracke_name = value
                        self.tracke_name.value_namespace = name_space
                        self.tracke_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.track_info:
                    if (c.has_data()):
                        return True
                return self.track_name.is_set

            def has_operation(self):
                for c in self.track_info:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.track_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track" + "[track-name='" + self.track_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/tracks/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.track_name.is_set or self.track_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-info"):
                    for c in self.track_info:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ObjectTracking.Tracks.Track.TrackInfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.track_info.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-info" or name == "track-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "track-name"):
                    self.track_name = value
                    self.track_name.value_namespace = name_space
                    self.track_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tracks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track"):
                for c in self.track:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.Tracks.Track()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track_info_brief = YList(self)

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
                        super(ObjectTracking.TrackTypeIpv4RouteBrief, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackTypeIpv4RouteBrief, self).__setattr__(name, value)


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

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.track_type_info = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("track_state",
                                "tracke_name",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminant") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix


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

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("next_hop",
                                        "prefix",
                                        "prefix_length",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.next_hop.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.next_hop.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "next-hop"):
                            self.next_hop = value
                            self.next_hop.value_namespace = name_space
                            self.next_hop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix


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

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipsla_op_id",
                                        "return_code",
                                        "rtt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipsla_op_id.is_set or
                            self.return_code.is_set or
                            self.rtt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipsla_op_id.yfilter != YFilter.not_set or
                            self.return_code.yfilter != YFilter.not_set or
                            self.rtt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipsla-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                        if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.return_code.get_name_leafdata())
                        if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rtt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipsla-op-id"):
                            self.ipsla_op_id = value
                            self.ipsla_op_id.value_namespace = name_space
                            self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "return-code"):
                            self.return_code = value
                            self.return_code.value_namespace = name_space
                            self.return_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "rtt"):
                            self.rtt = value
                            self.rtt.value_namespace = name_space
                            self.rtt.value_namespace_prefix = name_space_prefix


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

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debounce_count",
                                        "destination_address",
                                        "interface_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debounce_count.is_set or
                            self.destination_address.is_set or
                            self.interface_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debounce_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debounce_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debounce-count"):
                            self.debounce_count = value
                            self.debounce_count.value_namespace = name_space
                            self.debounce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.discriminant.is_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                        (self.route_tracks is not None and self.route_tracks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminant.yfilter != YFilter.not_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                        (self.route_tracks is not None and self.route_tracks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-type-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/track-info-brief/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminant.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bfd-tracks"):
                        if (self.bfd_tracks is None):
                            self.bfd_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                            self.bfd_tracks.parent = self
                            self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        return self.bfd_tracks

                    if (child_yang_name == "interface-tracks"):
                        if (self.interface_tracks is None):
                            self.interface_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                            self.interface_tracks.parent = self
                            self._children_name_map["interface_tracks"] = "interface-tracks"
                        return self.interface_tracks

                    if (child_yang_name == "ipsla-tracks"):
                        if (self.ipsla_tracks is None):
                            self.ipsla_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                            self.ipsla_tracks.parent = self
                            self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        return self.ipsla_tracks

                    if (child_yang_name == "route-tracks"):
                        if (self.route_tracks is None):
                            self.route_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                            self.route_tracks.parent = self
                            self._children_name_map["route_tracks"] = "route-tracks"
                        return self.route_tracks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminant"):
                        self.discriminant = value
                        self.discriminant.value_namespace = name_space
                        self.discriminant.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.track_state.is_set or
                    self.tracke_name.is_set or
                    self.type.is_set or
                    (self.track_type_info is not None and self.track_type_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.track_state.yfilter != YFilter.not_set or
                    self.tracke_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.track_type_info is not None and self.track_type_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-info-brief" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route-brief/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_state.get_name_leafdata())
                if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tracke_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-type-info"):
                    if (self.track_type_info is None):
                        self.track_type_info = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo()
                        self.track_type_info.parent = self
                        self._children_name_map["track_type_info"] = "track-type-info"
                    return self.track_type_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-type-info" or name == "track-state" or name == "tracke-name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "track-state"):
                    self.track_state = value
                    self.track_state.value_namespace = name_space
                    self.track_state.value_namespace_prefix = name_space_prefix
                if(value_path == "tracke-name"):
                    self.tracke_name = value
                    self.tracke_name.value_namespace = name_space
                    self.tracke_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_info_brief:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_info_brief:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-type-ipv4-route-brief" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-info-brief"):
                for c in self.track_info_brief:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_info_brief.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-info-brief"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track_info = YList(self)

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
                        super(ObjectTracking.TrackTypeIpv4Route, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackTypeIpv4Route, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("seconds_last_change",
                                "state_change_counter",
                                "threshold_down",
                                "threshold_up",
                                "track_state",
                                "tracke_name",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackTypeIpv4Route.TrackInfo, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackTypeIpv4Route.TrackInfo, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminant") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix


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

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("next_hop",
                                        "prefix",
                                        "prefix_length",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.next_hop.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.next_hop.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "next-hop"):
                            self.next_hop = value
                            self.next_hop.value_namespace = name_space
                            self.next_hop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix


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

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipsla_op_id",
                                        "return_code",
                                        "rtt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipsla_op_id.is_set or
                            self.return_code.is_set or
                            self.rtt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipsla_op_id.yfilter != YFilter.not_set or
                            self.return_code.yfilter != YFilter.not_set or
                            self.rtt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipsla-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                        if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.return_code.get_name_leafdata())
                        if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rtt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipsla-op-id"):
                            self.ipsla_op_id = value
                            self.ipsla_op_id.value_namespace = name_space
                            self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "return-code"):
                            self.return_code = value
                            self.return_code.value_namespace = name_space
                            self.return_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "rtt"):
                            self.rtt = value
                            self.rtt.value_namespace = name_space
                            self.rtt.value_namespace_prefix = name_space_prefix


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

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debounce_count",
                                        "destination_address",
                                        "interface_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debounce_count.is_set or
                            self.destination_address.is_set or
                            self.interface_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debounce_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debounce_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debounce-count"):
                            self.debounce_count = value
                            self.debounce_count.value_namespace = name_space
                            self.debounce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.discriminant.is_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                        (self.route_tracks is not None and self.route_tracks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminant.yfilter != YFilter.not_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                        (self.route_tracks is not None and self.route_tracks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-type-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminant.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bfd-tracks"):
                        if (self.bfd_tracks is None):
                            self.bfd_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks()
                            self.bfd_tracks.parent = self
                            self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        return self.bfd_tracks

                    if (child_yang_name == "interface-tracks"):
                        if (self.interface_tracks is None):
                            self.interface_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks()
                            self.interface_tracks.parent = self
                            self._children_name_map["interface_tracks"] = "interface-tracks"
                        return self.interface_tracks

                    if (child_yang_name == "ipsla-tracks"):
                        if (self.ipsla_tracks is None):
                            self.ipsla_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks()
                            self.ipsla_tracks.parent = self
                            self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        return self.ipsla_tracks

                    if (child_yang_name == "route-tracks"):
                        if (self.route_tracks is None):
                            self.route_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks()
                            self.route_tracks.parent = self
                            self._children_name_map["route_tracks"] = "route-tracks"
                        return self.route_tracks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminant"):
                        self.discriminant = value
                        self.discriminant.value_namespace = name_space
                        self.discriminant.value_namespace_prefix = name_space_prefix


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

                    self.bool_track_info = YList(self)

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
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks, self).__setattr__(name, value)


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

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.with_not = YLeaf(YType.boolean, "with-not")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "track_state",
                                        "with_not") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.track_state.is_set or
                            self.with_not.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set or
                            self.with_not.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bool-track-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/bool-tracks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())
                        if (self.with_not.is_set or self.with_not.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.with_not.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "track-state" or name == "with-not"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "with-not"):
                            self.with_not = value
                            self.with_not.value_namespace = name_space
                            self.with_not.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bool_track_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bool_track_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bool-tracks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bool-track-info"):
                        for c in self.bool_track_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bool_track_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bool-track-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.threshold_track_info = YList(self)

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
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks, self).__setattr__(name, value)


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

                        self.object_name = YLeaf(YType.str, "object-name")

                        self.track_state = YLeaf(YType.boolean, "track-state")

                        self.weight = YLeaf(YType.uint32, "weight")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("object_name",
                                        "track_state",
                                        "weight") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.object_name.is_set or
                            self.track_state.is_set or
                            self.weight.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.object_name.yfilter != YFilter.not_set or
                            self.track_state.yfilter != YFilter.not_set or
                            self.weight.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "threshold-track-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/threshold-tracks/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.object_name.is_set or self.object_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.object_name.get_name_leafdata())
                        if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.track_state.get_name_leafdata())
                        if (self.weight.is_set or self.weight.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.weight.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "object-name" or name == "track-state" or name == "weight"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "object-name"):
                            self.object_name = value
                            self.object_name.value_namespace = name_space
                            self.object_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "track-state"):
                            self.track_state = value
                            self.track_state.value_namespace = name_space
                            self.track_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "weight"):
                            self.weight = value
                            self.weight.value_namespace = name_space
                            self.weight.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.threshold_track_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.threshold_track_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-tracks" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "threshold-track-info"):
                        for c in self.threshold_track_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.threshold_track_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "threshold-track-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.interface_tracking_info = YList(self)

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
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracking-info" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/tracking-interaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_tracking_info:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_tracking_info:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tracking-interaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface-tracking-info"):
                        for c in self.interface_tracking_info:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_tracking_info.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-tracking-info"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    self.track_state = YLeaf(YType.boolean, "track-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("time_remaining",
                                    "track_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.time_remaining.is_set or
                        self.track_state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.time_remaining.yfilter != YFilter.not_set or
                        self.track_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "delayed" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/track-info/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_remaining.get_name_leafdata())
                    if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.track_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "time-remaining" or name == "track-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "time-remaining"):
                        self.time_remaining = value
                        self.time_remaining.value_namespace = name_space
                        self.time_remaining.value_namespace_prefix = name_space_prefix
                    if(value_path == "track-state"):
                        self.track_state = value
                        self.track_state.value_namespace = name_space
                        self.track_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.seconds_last_change.is_set or
                    self.state_change_counter.is_set or
                    self.threshold_down.is_set or
                    self.threshold_up.is_set or
                    self.track_state.is_set or
                    self.tracke_name.is_set or
                    self.type.is_set or
                    (self.bool_tracks is not None and self.bool_tracks.has_data()) or
                    (self.delayed is not None and self.delayed.has_data()) or
                    (self.threshold_tracks is not None and self.threshold_tracks.has_data()) or
                    (self.track_type_info is not None and self.track_type_info.has_data()) or
                    (self.tracking_interaces is not None and self.tracking_interaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.seconds_last_change.yfilter != YFilter.not_set or
                    self.state_change_counter.yfilter != YFilter.not_set or
                    self.threshold_down.yfilter != YFilter.not_set or
                    self.threshold_up.yfilter != YFilter.not_set or
                    self.track_state.yfilter != YFilter.not_set or
                    self.tracke_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.bool_tracks is not None and self.bool_tracks.has_operation()) or
                    (self.delayed is not None and self.delayed.has_operation()) or
                    (self.threshold_tracks is not None and self.threshold_tracks.has_operation()) or
                    (self.track_type_info is not None and self.track_type_info.has_operation()) or
                    (self.tracking_interaces is not None and self.tracking_interaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-info" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-ipv4-route/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.seconds_last_change.is_set or self.seconds_last_change.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.seconds_last_change.get_name_leafdata())
                if (self.state_change_counter.is_set or self.state_change_counter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state_change_counter.get_name_leafdata())
                if (self.threshold_down.is_set or self.threshold_down.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold_down.get_name_leafdata())
                if (self.threshold_up.is_set or self.threshold_up.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold_up.get_name_leafdata())
                if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_state.get_name_leafdata())
                if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tracke_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bool-tracks"):
                    if (self.bool_tracks is None):
                        self.bool_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks()
                        self.bool_tracks.parent = self
                        self._children_name_map["bool_tracks"] = "bool-tracks"
                    return self.bool_tracks

                if (child_yang_name == "delayed"):
                    if (self.delayed is None):
                        self.delayed = ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed()
                        self.delayed.parent = self
                        self._children_name_map["delayed"] = "delayed"
                    return self.delayed

                if (child_yang_name == "threshold-tracks"):
                    if (self.threshold_tracks is None):
                        self.threshold_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks()
                        self.threshold_tracks.parent = self
                        self._children_name_map["threshold_tracks"] = "threshold-tracks"
                    return self.threshold_tracks

                if (child_yang_name == "track-type-info"):
                    if (self.track_type_info is None):
                        self.track_type_info = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo()
                        self.track_type_info.parent = self
                        self._children_name_map["track_type_info"] = "track-type-info"
                    return self.track_type_info

                if (child_yang_name == "tracking-interaces"):
                    if (self.tracking_interaces is None):
                        self.tracking_interaces = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces()
                        self.tracking_interaces.parent = self
                        self._children_name_map["tracking_interaces"] = "tracking-interaces"
                    return self.tracking_interaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bool-tracks" or name == "delayed" or name == "threshold-tracks" or name == "track-type-info" or name == "tracking-interaces" or name == "seconds-last-change" or name == "state-change-counter" or name == "threshold-down" or name == "threshold-up" or name == "track-state" or name == "tracke-name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "seconds-last-change"):
                    self.seconds_last_change = value
                    self.seconds_last_change.value_namespace = name_space
                    self.seconds_last_change.value_namespace_prefix = name_space_prefix
                if(value_path == "state-change-counter"):
                    self.state_change_counter = value
                    self.state_change_counter.value_namespace = name_space
                    self.state_change_counter.value_namespace_prefix = name_space_prefix
                if(value_path == "threshold-down"):
                    self.threshold_down = value
                    self.threshold_down.value_namespace = name_space
                    self.threshold_down.value_namespace_prefix = name_space_prefix
                if(value_path == "threshold-up"):
                    self.threshold_up = value
                    self.threshold_up.value_namespace = name_space
                    self.threshold_up.value_namespace_prefix = name_space_prefix
                if(value_path == "track-state"):
                    self.track_state = value
                    self.track_state.value_namespace = name_space
                    self.track_state.value_namespace_prefix = name_space_prefix
                if(value_path == "tracke-name"):
                    self.tracke_name = value
                    self.tracke_name.value_namespace = name_space
                    self.tracke_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_info:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_info:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-type-ipv4-route" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-info"):
                for c in self.track_info:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackTypeIpv4Route.TrackInfo()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_info.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-info"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.track_info_brief = YList(self)

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
                        super(ObjectTracking.TrackTypeInterfaceBrief, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ObjectTracking.TrackTypeInterfaceBrief, self).__setattr__(name, value)


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

                self.track_state = YLeaf(YType.boolean, "track-state")

                self.tracke_name = YLeaf(YType.str, "tracke-name")

                self.type = YLeaf(YType.enumeration, "type")

                self.track_type_info = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self._children_name_map["track_type_info"] = "track-type-info"
                self._children_yang_names.add("track-type-info")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("track_state",
                                "tracke_name",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("discriminant") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface_name.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix


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

                        self.next_hop = YLeaf(YType.str, "next-hop")

                        self.prefix = YLeaf(YType.uint32, "prefix")

                        self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                        self.vrf = YLeaf(YType.str, "vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("next_hop",
                                        "prefix",
                                        "prefix_length",
                                        "vrf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.next_hop.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.vrf.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.next_hop.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "route-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.next_hop.is_set or self.next_hop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.next_hop.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "prefix" or name == "prefix-length" or name == "vrf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "next-hop"):
                            self.next_hop = value
                            self.next_hop.value_namespace = name_space
                            self.next_hop.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix


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

                        self.ipsla_op_id = YLeaf(YType.uint32, "ipsla-op-id")

                        self.return_code = YLeaf(YType.uint32, "return-code")

                        self.rtt = YLeaf(YType.uint32, "rtt")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ipsla_op_id",
                                        "return_code",
                                        "rtt") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.ipsla_op_id.is_set or
                            self.return_code.is_set or
                            self.rtt.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ipsla_op_id.yfilter != YFilter.not_set or
                            self.return_code.yfilter != YFilter.not_set or
                            self.rtt.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipsla-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ipsla_op_id.is_set or self.ipsla_op_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipsla_op_id.get_name_leafdata())
                        if (self.return_code.is_set or self.return_code.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.return_code.get_name_leafdata())
                        if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rtt.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipsla-op-id" or name == "return-code" or name == "rtt"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ipsla-op-id"):
                            self.ipsla_op_id = value
                            self.ipsla_op_id.value_namespace = name_space
                            self.ipsla_op_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "return-code"):
                            self.return_code = value
                            self.return_code.value_namespace = name_space
                            self.return_code.value_namespace_prefix = name_space_prefix
                        if(value_path == "rtt"):
                            self.rtt = value
                            self.rtt.value_namespace = name_space
                            self.rtt.value_namespace_prefix = name_space_prefix


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

                        self.debounce_count = YLeaf(YType.uint32, "debounce-count")

                        self.destination_address = YLeaf(YType.uint32, "destination-address")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.rate = YLeaf(YType.uint32, "rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debounce_count",
                                        "destination_address",
                                        "interface_name",
                                        "rate") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debounce_count.is_set or
                            self.destination_address.is_set or
                            self.interface_name.is_set or
                            self.rate.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debounce_count.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.rate.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bfd-tracks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/track-type-info/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debounce_count.is_set or self.debounce_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debounce_count.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.rate.is_set or self.rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rate.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debounce-count" or name == "destination-address" or name == "interface-name" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debounce-count"):
                            self.debounce_count = value
                            self.debounce_count.value_namespace = name_space
                            self.debounce_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "rate"):
                            self.rate = value
                            self.rate.value_namespace = name_space
                            self.rate.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.discriminant.is_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_data()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_data()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_data()) or
                        (self.route_tracks is not None and self.route_tracks.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.discriminant.yfilter != YFilter.not_set or
                        (self.bfd_tracks is not None and self.bfd_tracks.has_operation()) or
                        (self.interface_tracks is not None and self.interface_tracks.has_operation()) or
                        (self.ipsla_tracks is not None and self.ipsla_tracks.has_operation()) or
                        (self.route_tracks is not None and self.route_tracks.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "track-type-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/track-info-brief/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.discriminant.is_set or self.discriminant.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.discriminant.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bfd-tracks"):
                        if (self.bfd_tracks is None):
                            self.bfd_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                            self.bfd_tracks.parent = self
                            self._children_name_map["bfd_tracks"] = "bfd-tracks"
                        return self.bfd_tracks

                    if (child_yang_name == "interface-tracks"):
                        if (self.interface_tracks is None):
                            self.interface_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                            self.interface_tracks.parent = self
                            self._children_name_map["interface_tracks"] = "interface-tracks"
                        return self.interface_tracks

                    if (child_yang_name == "ipsla-tracks"):
                        if (self.ipsla_tracks is None):
                            self.ipsla_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                            self.ipsla_tracks.parent = self
                            self._children_name_map["ipsla_tracks"] = "ipsla-tracks"
                        return self.ipsla_tracks

                    if (child_yang_name == "route-tracks"):
                        if (self.route_tracks is None):
                            self.route_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                            self.route_tracks.parent = self
                            self._children_name_map["route_tracks"] = "route-tracks"
                        return self.route_tracks

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bfd-tracks" or name == "interface-tracks" or name == "ipsla-tracks" or name == "route-tracks" or name == "discriminant"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "discriminant"):
                        self.discriminant = value
                        self.discriminant.value_namespace = name_space
                        self.discriminant.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.track_state.is_set or
                    self.tracke_name.is_set or
                    self.type.is_set or
                    (self.track_type_info is not None and self.track_type_info.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.track_state.yfilter != YFilter.not_set or
                    self.tracke_name.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    (self.track_type_info is not None and self.track_type_info.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "track-info-brief" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/track-type-interface-brief/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.track_state.is_set or self.track_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.track_state.get_name_leafdata())
                if (self.tracke_name.is_set or self.tracke_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tracke_name.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "track-type-info"):
                    if (self.track_type_info is None):
                        self.track_type_info = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo()
                        self.track_type_info.parent = self
                        self._children_name_map["track_type_info"] = "track-type-info"
                    return self.track_type_info

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "track-type-info" or name == "track-state" or name == "tracke-name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "track-state"):
                    self.track_state = value
                    self.track_state.value_namespace = name_space
                    self.track_state.value_namespace_prefix = name_space_prefix
                if(value_path == "tracke-name"):
                    self.tracke_name = value
                    self.tracke_name.value_namespace = name_space
                    self.tracke_name.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.track_info_brief:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.track_info_brief:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "track-type-interface-brief" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "track-info-brief"):
                for c in self.track_info_brief:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.track_info_brief.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "track-info-brief"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.track_briefs is not None and self.track_briefs.has_data()) or
            (self.track_type_interface is not None and self.track_type_interface.has_data()) or
            (self.track_type_interface_brief is not None and self.track_type_interface_brief.has_data()) or
            (self.track_type_ipv4_route is not None and self.track_type_ipv4_route.has_data()) or
            (self.track_type_ipv4_route_brief is not None and self.track_type_ipv4_route_brief.has_data()) or
            (self.track_type_rtr_reachability is not None and self.track_type_rtr_reachability.has_data()) or
            (self.track_type_rtr_reachability_brief is not None and self.track_type_rtr_reachability_brief.has_data()) or
            (self.tracks is not None and self.tracks.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.track_briefs is not None and self.track_briefs.has_operation()) or
            (self.track_type_interface is not None and self.track_type_interface.has_operation()) or
            (self.track_type_interface_brief is not None and self.track_type_interface_brief.has_operation()) or
            (self.track_type_ipv4_route is not None and self.track_type_ipv4_route.has_operation()) or
            (self.track_type_ipv4_route_brief is not None and self.track_type_ipv4_route_brief.has_operation()) or
            (self.track_type_rtr_reachability is not None and self.track_type_rtr_reachability.has_operation()) or
            (self.track_type_rtr_reachability_brief is not None and self.track_type_rtr_reachability_brief.has_operation()) or
            (self.tracks is not None and self.tracks.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking" + path_buffer

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

        if (child_yang_name == "track-briefs"):
            if (self.track_briefs is None):
                self.track_briefs = ObjectTracking.TrackBriefs()
                self.track_briefs.parent = self
                self._children_name_map["track_briefs"] = "track-briefs"
            return self.track_briefs

        if (child_yang_name == "track-type-interface"):
            if (self.track_type_interface is None):
                self.track_type_interface = ObjectTracking.TrackTypeInterface()
                self.track_type_interface.parent = self
                self._children_name_map["track_type_interface"] = "track-type-interface"
            return self.track_type_interface

        if (child_yang_name == "track-type-interface-brief"):
            if (self.track_type_interface_brief is None):
                self.track_type_interface_brief = ObjectTracking.TrackTypeInterfaceBrief()
                self.track_type_interface_brief.parent = self
                self._children_name_map["track_type_interface_brief"] = "track-type-interface-brief"
            return self.track_type_interface_brief

        if (child_yang_name == "track-type-ipv4-route"):
            if (self.track_type_ipv4_route is None):
                self.track_type_ipv4_route = ObjectTracking.TrackTypeIpv4Route()
                self.track_type_ipv4_route.parent = self
                self._children_name_map["track_type_ipv4_route"] = "track-type-ipv4-route"
            return self.track_type_ipv4_route

        if (child_yang_name == "track-type-ipv4-route-brief"):
            if (self.track_type_ipv4_route_brief is None):
                self.track_type_ipv4_route_brief = ObjectTracking.TrackTypeIpv4RouteBrief()
                self.track_type_ipv4_route_brief.parent = self
                self._children_name_map["track_type_ipv4_route_brief"] = "track-type-ipv4-route-brief"
            return self.track_type_ipv4_route_brief

        if (child_yang_name == "track-type-rtr-reachability"):
            if (self.track_type_rtr_reachability is None):
                self.track_type_rtr_reachability = ObjectTracking.TrackTypeRtrReachability()
                self.track_type_rtr_reachability.parent = self
                self._children_name_map["track_type_rtr_reachability"] = "track-type-rtr-reachability"
            return self.track_type_rtr_reachability

        if (child_yang_name == "track-type-rtr-reachability-brief"):
            if (self.track_type_rtr_reachability_brief is None):
                self.track_type_rtr_reachability_brief = ObjectTracking.TrackTypeRtrReachabilityBrief()
                self.track_type_rtr_reachability_brief.parent = self
                self._children_name_map["track_type_rtr_reachability_brief"] = "track-type-rtr-reachability-brief"
            return self.track_type_rtr_reachability_brief

        if (child_yang_name == "tracks"):
            if (self.tracks is None):
                self.tracks = ObjectTracking.Tracks()
                self.tracks.parent = self
                self._children_name_map["tracks"] = "tracks"
            return self.tracks

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "track-briefs" or name == "track-type-interface" or name == "track-type-interface-brief" or name == "track-type-ipv4-route" or name == "track-type-ipv4-route-brief" or name == "track-type-rtr-reachability" or name == "track-type-rtr-reachability-brief" or name == "tracks"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ObjectTracking()
        return self._top_entity

