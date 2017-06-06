""" Cisco_IOS_XR_manageability_object_tracking_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-object\-tracking package operational data.

This module contains definitions
for the following management objects\:
  object\-tracking\: Object Tracking operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class TrackEnum(Enum):
    """
    TrackEnum

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

    interface_type = 1

    route_type = 2

    bool_and_type = 3

    bool_or_type = 4

    ipsla_type = 5

    undefined_type = 6

    threshold_weight = 7

    threshold_percentage = 8

    bfd_type = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
        return meta._meta_table['TrackEnum']



class ObjectTracking(object):
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
        self.track_briefs = ObjectTracking.TrackBriefs()
        self.track_briefs.parent = self
        self.track_type_interface = ObjectTracking.TrackTypeInterface()
        self.track_type_interface.parent = self
        self.track_type_interface_brief = ObjectTracking.TrackTypeInterfaceBrief()
        self.track_type_interface_brief.parent = self
        self.track_type_ipv4_route = ObjectTracking.TrackTypeIpv4Route()
        self.track_type_ipv4_route.parent = self
        self.track_type_ipv4_route_brief = ObjectTracking.TrackTypeIpv4RouteBrief()
        self.track_type_ipv4_route_brief.parent = self
        self.track_type_rtr_reachability = ObjectTracking.TrackTypeRtrReachability()
        self.track_type_rtr_reachability.parent = self
        self.track_type_rtr_reachability_brief = ObjectTracking.TrackTypeRtrReachabilityBrief()
        self.track_type_rtr_reachability_brief.parent = self
        self.tracks = ObjectTracking.Tracks()
        self.tracks.parent = self


    class TrackTypeInterface(object):
        """
        Object Tracking Type interface info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_info = YList()
            self.track_info.parent = self
            self.track_info.name = 'track_info'


        class TrackInfo(object):
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
            	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bool_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self.delayed = ObjectTracking.TrackTypeInterface.TrackInfo.Delayed()
                self.delayed.parent = self
                self.seconds_last_change = None
                self.state_change_counter = None
                self.threshold_down = None
                self.threshold_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self.threshold_up = None
                self.track_state = None
                self.track_type_info = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self.tracke_name = None
                self.tracking_interaces = ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self.type = None


            class TrackTypeInfo(object):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
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
                    self.parent = None
                    self.bfd_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self.discriminant = None
                    self.interface_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self.ipsla_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self.route_tracks = ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self


                class InterfaceTracks(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info']


                class RouteTracks(object):
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
                        self.parent = None
                        self.next_hop = None
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info']


                class IpslaTracks(object):
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
                        self.parent = None
                        self.ipsla_op_id = None
                        self.return_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipsla_op_id is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info']


                class BfdTracks(object):
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
                        self.parent = None
                        self.debounce_count = None
                        self.destination_address = None
                        self.interface_name = None
                        self.rate = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.debounce_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                        return True

                    if self.discriminant is not None:
                        return True

                    if self.interface_tracks is not None and self.interface_tracks._has_data():
                        return True

                    if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                        return True

                    if self.route_tracks is not None and self.route_tracks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackTypeInfo']['meta_info']


            class BoolTracks(object):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bool_track_info = YList()
                    self.bool_track_info.parent = self
                    self.bool_track_info.name = 'bool_track_info'


                class BoolTrackInfo(object):
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
                        self.parent = None
                        self.object_name = None
                        self.track_state = None
                        self.with_not = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks/Cisco-IOS-XR-manageability-object-tracking-oper:bool-track-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        if self.with_not is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bool_track_info is not None:
                        for child_ref in self.bool_track_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.BoolTracks']['meta_info']


            class ThresholdTracks(object):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.threshold_track_info = YList()
                    self.threshold_track_info.parent = self
                    self.threshold_track_info.name = 'threshold_track_info'


                class ThresholdTrackInfo(object):
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
                        self.parent = None
                        self.object_name = None
                        self.track_state = None
                        self.weight = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-track-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        if self.weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.threshold_track_info is not None:
                        for child_ref in self.threshold_track_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.ThresholdTracks']['meta_info']


            class TrackingInteraces(object):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_tracking_info = YList()
                    self.interface_tracking_info.parent = self
                    self.interface_tracking_info.name = 'interface_tracking_info'


                class InterfaceTrackingInfo(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracking-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_tracking_info is not None:
                        for child_ref in self.interface_tracking_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.TrackingInteraces']['meta_info']


            class Delayed(object):
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
                    self.parent = None
                    self.time_remaining = None
                    self.track_state = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:delayed'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.time_remaining is not None:
                        return True

                    if self.track_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo.Delayed']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface/Cisco-IOS-XR-manageability-object-tracking-oper:track-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bool_tracks is not None and self.bool_tracks._has_data():
                    return True

                if self.delayed is not None and self.delayed._has_data():
                    return True

                if self.seconds_last_change is not None:
                    return True

                if self.state_change_counter is not None:
                    return True

                if self.threshold_down is not None:
                    return True

                if self.threshold_tracks is not None and self.threshold_tracks._has_data():
                    return True

                if self.threshold_up is not None:
                    return True

                if self.track_state is not None:
                    return True

                if self.track_type_info is not None and self.track_type_info._has_data():
                    return True

                if self.tracke_name is not None:
                    return True

                if self.tracking_interaces is not None and self.tracking_interaces._has_data():
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackTypeInterface.TrackInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_info is not None:
                for child_ref in self.track_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackTypeInterface']['meta_info']


    class TrackBriefs(object):
        """
        Object Tracking Track table brief
        
        .. attribute:: track_brief
        
        	Track name \- maximum 32 characters
        	**type**\: list of    :py:class:`TrackBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_brief = YList()
            self.track_brief.parent = self
            self.track_brief.name = 'track_brief'


        class TrackBrief(object):
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
                self.parent = None
                self.track_name = None
                self.track_info_brief = YList()
                self.track_info_brief.parent = self
                self.track_info_brief.name = 'track_info_brief'


            class TrackInfoBrief(object):
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
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.track_state = None
                    self.track_type_info = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self.tracke_name = None
                    self.type = None


                class TrackTypeInfo(object):
                    """
                    Track type information
                    
                    .. attribute:: bfd_tracks
                    
                    	track type bfdrtr info
                    	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                    
                    .. attribute:: discriminant
                    
                    	discriminant
                    	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                    
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
                        self.parent = None
                        self.bfd_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                        self.bfd_tracks.parent = self
                        self.discriminant = None
                        self.interface_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                        self.interface_tracks.parent = self
                        self.ipsla_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                        self.ipsla_tracks.parent = self
                        self.route_tracks = ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                        self.route_tracks.parent = self


                    class InterfaceTracks(object):
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
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info']


                    class RouteTracks(object):
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
                            self.parent = None
                            self.next_hop = None
                            self.prefix = None
                            self.prefix_length = None
                            self.vrf = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.next_hop is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.vrf is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info']


                    class IpslaTracks(object):
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
                            self.parent = None
                            self.ipsla_op_id = None
                            self.return_code = None
                            self.rtt = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipsla_op_id is not None:
                                return True

                            if self.return_code is not None:
                                return True

                            if self.rtt is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info']


                    class BfdTracks(object):
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
                            self.parent = None
                            self.debounce_count = None
                            self.destination_address = None
                            self.interface_name = None
                            self.rate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.debounce_count is not None:
                                return True

                            if self.destination_address is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                            return True

                        if self.discriminant is not None:
                            return True

                        if self.interface_tracks is not None and self.interface_tracks._has_data():
                            return True

                        if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                            return True

                        if self.route_tracks is not None and self.route_tracks._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.track_state is not None:
                        return True

                    if self.track_type_info is not None and self.track_type_info._has_data():
                        return True

                    if self.tracke_name is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief.TrackInfoBrief']['meta_info']

            @property
            def _common_path(self):
                if self.track_name is None:
                    raise YPYModelError('Key property track_name is None')

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-briefs/Cisco-IOS-XR-manageability-object-tracking-oper:track-brief[Cisco-IOS-XR-manageability-object-tracking-oper:track-name = ' + str(self.track_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_name is not None:
                    return True

                if self.track_info_brief is not None:
                    for child_ref in self.track_info_brief:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackBriefs.TrackBrief']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-briefs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_brief is not None:
                for child_ref in self.track_brief:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackBriefs']['meta_info']


    class TrackTypeRtrReachability(object):
        """
        Object Tracking Type RTR Reachability info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_info = YList()
            self.track_info.parent = self
            self.track_info.name = 'track_info'


        class TrackInfo(object):
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
            	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bool_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self.delayed = ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed()
                self.delayed.parent = self
                self.seconds_last_change = None
                self.state_change_counter = None
                self.threshold_down = None
                self.threshold_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self.threshold_up = None
                self.track_state = None
                self.track_type_info = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self.tracke_name = None
                self.tracking_interaces = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self.type = None


            class TrackTypeInfo(object):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
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
                    self.parent = None
                    self.bfd_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self.discriminant = None
                    self.interface_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self.route_tracks = ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self


                class InterfaceTracks(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info']


                class RouteTracks(object):
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
                        self.parent = None
                        self.next_hop = None
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info']


                class IpslaTracks(object):
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
                        self.parent = None
                        self.ipsla_op_id = None
                        self.return_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipsla_op_id is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info']


                class BfdTracks(object):
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
                        self.parent = None
                        self.debounce_count = None
                        self.destination_address = None
                        self.interface_name = None
                        self.rate = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.debounce_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                        return True

                    if self.discriminant is not None:
                        return True

                    if self.interface_tracks is not None and self.interface_tracks._has_data():
                        return True

                    if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                        return True

                    if self.route_tracks is not None and self.route_tracks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackTypeInfo']['meta_info']


            class BoolTracks(object):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bool_track_info = YList()
                    self.bool_track_info.parent = self
                    self.bool_track_info.name = 'bool_track_info'


                class BoolTrackInfo(object):
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
                        self.parent = None
                        self.object_name = None
                        self.track_state = None
                        self.with_not = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks/Cisco-IOS-XR-manageability-object-tracking-oper:bool-track-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        if self.with_not is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bool_track_info is not None:
                        for child_ref in self.bool_track_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.BoolTracks']['meta_info']


            class ThresholdTracks(object):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.threshold_track_info = YList()
                    self.threshold_track_info.parent = self
                    self.threshold_track_info.name = 'threshold_track_info'


                class ThresholdTrackInfo(object):
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
                        self.parent = None
                        self.object_name = None
                        self.track_state = None
                        self.weight = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-track-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        if self.weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.threshold_track_info is not None:
                        for child_ref in self.threshold_track_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.ThresholdTracks']['meta_info']


            class TrackingInteraces(object):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_tracking_info = YList()
                    self.interface_tracking_info.parent = self
                    self.interface_tracking_info.name = 'interface_tracking_info'


                class InterfaceTrackingInfo(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracking-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_tracking_info is not None:
                        for child_ref in self.interface_tracking_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.TrackingInteraces']['meta_info']


            class Delayed(object):
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
                    self.parent = None
                    self.time_remaining = None
                    self.track_state = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:delayed'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.time_remaining is not None:
                        return True

                    if self.track_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo.Delayed']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability/Cisco-IOS-XR-manageability-object-tracking-oper:track-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bool_tracks is not None and self.bool_tracks._has_data():
                    return True

                if self.delayed is not None and self.delayed._has_data():
                    return True

                if self.seconds_last_change is not None:
                    return True

                if self.state_change_counter is not None:
                    return True

                if self.threshold_down is not None:
                    return True

                if self.threshold_tracks is not None and self.threshold_tracks._has_data():
                    return True

                if self.threshold_up is not None:
                    return True

                if self.track_state is not None:
                    return True

                if self.track_type_info is not None and self.track_type_info._has_data():
                    return True

                if self.tracke_name is not None:
                    return True

                if self.tracking_interaces is not None and self.tracking_interaces._has_data():
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackTypeRtrReachability.TrackInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_info is not None:
                for child_ref in self.track_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackTypeRtrReachability']['meta_info']


    class TrackTypeRtrReachabilityBrief(object):
        """
        Object Tracking Type RTR Reachability brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_info_brief = YList()
            self.track_info_brief.parent = self
            self.track_info_brief.name = 'track_info_brief'


        class TrackInfoBrief(object):
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
            	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.track_state = None
                self.track_type_info = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self.tracke_name = None
                self.type = None


            class TrackTypeInfo(object):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
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
                    self.parent = None
                    self.bfd_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self.discriminant = None
                    self.interface_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self.ipsla_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self.route_tracks = ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self


                class InterfaceTracks(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info']


                class RouteTracks(object):
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
                        self.parent = None
                        self.next_hop = None
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info']


                class IpslaTracks(object):
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
                        self.parent = None
                        self.ipsla_op_id = None
                        self.return_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipsla_op_id is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info']


                class BfdTracks(object):
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
                        self.parent = None
                        self.debounce_count = None
                        self.destination_address = None
                        self.interface_name = None
                        self.rate = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.debounce_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                        return True

                    if self.discriminant is not None:
                        return True

                    if self.interface_tracks is not None and self.interface_tracks._has_data():
                        return True

                    if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                        return True

                    if self.route_tracks is not None and self.route_tracks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_state is not None:
                    return True

                if self.track_type_info is not None and self.track_type_info._has_data():
                    return True

                if self.tracke_name is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief.TrackInfoBrief']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-rtr-reachability-brief'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_info_brief is not None:
                for child_ref in self.track_info_brief:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackTypeRtrReachabilityBrief']['meta_info']


    class Tracks(object):
        """
        Object Tracking Track table
        
        .. attribute:: track
        
        	Track name \- maximum 32 characters
        	**type**\: list of    :py:class:`Track <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track = YList()
            self.track.parent = self
            self.track.name = 'track'


        class Track(object):
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
                self.parent = None
                self.track_name = None
                self.track_info = YList()
                self.track_info.parent = self
                self.track_info.name = 'track_info'


            class TrackInfo(object):
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
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bool_tracks = ObjectTracking.Tracks.Track.TrackInfo.BoolTracks()
                    self.bool_tracks.parent = self
                    self.delayed = ObjectTracking.Tracks.Track.TrackInfo.Delayed()
                    self.delayed.parent = self
                    self.seconds_last_change = None
                    self.state_change_counter = None
                    self.threshold_down = None
                    self.threshold_tracks = ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks()
                    self.threshold_tracks.parent = self
                    self.threshold_up = None
                    self.track_state = None
                    self.track_type_info = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo()
                    self.track_type_info.parent = self
                    self.tracke_name = None
                    self.tracking_interaces = ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces()
                    self.tracking_interaces.parent = self
                    self.type = None


                class TrackTypeInfo(object):
                    """
                    Track type information
                    
                    .. attribute:: bfd_tracks
                    
                    	track type bfdrtr info
                    	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks>`
                    
                    .. attribute:: discriminant
                    
                    	discriminant
                    	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                    
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
                        self.parent = None
                        self.bfd_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks()
                        self.bfd_tracks.parent = self
                        self.discriminant = None
                        self.interface_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks()
                        self.interface_tracks.parent = self
                        self.ipsla_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks()
                        self.ipsla_tracks.parent = self
                        self.route_tracks = ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks()
                        self.route_tracks.parent = self


                    class InterfaceTracks(object):
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
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info']


                    class RouteTracks(object):
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
                            self.parent = None
                            self.next_hop = None
                            self.prefix = None
                            self.prefix_length = None
                            self.vrf = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.next_hop is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.vrf is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info']


                    class IpslaTracks(object):
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
                            self.parent = None
                            self.ipsla_op_id = None
                            self.return_code = None
                            self.rtt = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ipsla_op_id is not None:
                                return True

                            if self.return_code is not None:
                                return True

                            if self.rtt is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info']


                    class BfdTracks(object):
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
                            self.parent = None
                            self.debounce_count = None
                            self.destination_address = None
                            self.interface_name = None
                            self.rate = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.debounce_count is not None:
                                return True

                            if self.destination_address is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.rate is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                            return True

                        if self.discriminant is not None:
                            return True

                        if self.interface_tracks is not None and self.interface_tracks._has_data():
                            return True

                        if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                            return True

                        if self.route_tracks is not None and self.route_tracks._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackTypeInfo']['meta_info']


                class BoolTracks(object):
                    """
                    boolean objects
                    
                    .. attribute:: bool_track_info
                    
                    	bool track info
                    	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bool_track_info = YList()
                        self.bool_track_info.parent = self
                        self.bool_track_info.name = 'bool_track_info'


                    class BoolTrackInfo(object):
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
                            self.parent = None
                            self.object_name = None
                            self.track_state = None
                            self.with_not = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:bool-track-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.object_name is not None:
                                return True

                            if self.track_state is not None:
                                return True

                            if self.with_not is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bool_track_info is not None:
                            for child_ref in self.bool_track_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.BoolTracks']['meta_info']


                class ThresholdTracks(object):
                    """
                    Threshold objects
                    
                    .. attribute:: threshold_track_info
                    
                    	threshold track info
                    	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.threshold_track_info = YList()
                        self.threshold_track_info.parent = self
                        self.threshold_track_info.name = 'threshold_track_info'


                    class ThresholdTrackInfo(object):
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
                            self.parent = None
                            self.object_name = None
                            self.track_state = None
                            self.weight = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-track-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.object_name is not None:
                                return True

                            if self.track_state is not None:
                                return True

                            if self.weight is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.threshold_track_info is not None:
                            for child_ref in self.threshold_track_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.ThresholdTracks']['meta_info']


                class TrackingInteraces(object):
                    """
                    Tracking Interfaces
                    
                    .. attribute:: interface_tracking_info
                    
                    	interface tracking info
                    	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                    
                    

                    """

                    _prefix = 'manageability-object-tracking-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_tracking_info = YList()
                        self.interface_tracking_info.parent = self
                        self.interface_tracking_info.name = 'interface_tracking_info'


                    class InterfaceTrackingInfo(object):
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
                            self.parent = None
                            self.interface_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracking-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                            return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_tracking_info is not None:
                            for child_ref in self.interface_tracking_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.TrackingInteraces']['meta_info']


                class Delayed(object):
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
                        self.parent = None
                        self.time_remaining = None
                        self.track_state = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:delayed'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.time_remaining is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo.Delayed']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-object-tracking-oper:track-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bool_tracks is not None and self.bool_tracks._has_data():
                        return True

                    if self.delayed is not None and self.delayed._has_data():
                        return True

                    if self.seconds_last_change is not None:
                        return True

                    if self.state_change_counter is not None:
                        return True

                    if self.threshold_down is not None:
                        return True

                    if self.threshold_tracks is not None and self.threshold_tracks._has_data():
                        return True

                    if self.threshold_up is not None:
                        return True

                    if self.track_state is not None:
                        return True

                    if self.track_type_info is not None and self.track_type_info._has_data():
                        return True

                    if self.tracke_name is not None:
                        return True

                    if self.tracking_interaces is not None and self.tracking_interaces._has_data():
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.Tracks.Track.TrackInfo']['meta_info']

            @property
            def _common_path(self):
                if self.track_name is None:
                    raise YPYModelError('Key property track_name is None')

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:tracks/Cisco-IOS-XR-manageability-object-tracking-oper:track[Cisco-IOS-XR-manageability-object-tracking-oper:track-name = ' + str(self.track_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_name is not None:
                    return True

                if self.track_info is not None:
                    for child_ref in self.track_info:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.Tracks.Track']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:tracks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track is not None:
                for child_ref in self.track:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.Tracks']['meta_info']


    class TrackTypeIpv4RouteBrief(object):
        """
        Object Tracking Type Ipv4 Route brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_info_brief = YList()
            self.track_info_brief.parent = self
            self.track_info_brief.name = 'track_info_brief'


        class TrackInfoBrief(object):
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
            	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.track_state = None
                self.track_type_info = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self.tracke_name = None
                self.type = None


            class TrackTypeInfo(object):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
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
                    self.parent = None
                    self.bfd_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self.discriminant = None
                    self.interface_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self.ipsla_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self.route_tracks = ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self


                class InterfaceTracks(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info']


                class RouteTracks(object):
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
                        self.parent = None
                        self.next_hop = None
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info']


                class IpslaTracks(object):
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
                        self.parent = None
                        self.ipsla_op_id = None
                        self.return_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipsla_op_id is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info']


                class BfdTracks(object):
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
                        self.parent = None
                        self.debounce_count = None
                        self.destination_address = None
                        self.interface_name = None
                        self.rate = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.debounce_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                        return True

                    if self.discriminant is not None:
                        return True

                    if self.interface_tracks is not None and self.interface_tracks._has_data():
                        return True

                    if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                        return True

                    if self.route_tracks is not None and self.route_tracks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_state is not None:
                    return True

                if self.track_type_info is not None and self.track_type_info._has_data():
                    return True

                if self.tracke_name is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief.TrackInfoBrief']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route-brief'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_info_brief is not None:
                for child_ref in self.track_info_brief:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackTypeIpv4RouteBrief']['meta_info']


    class TrackTypeIpv4Route(object):
        """
        Object Tracking Type IPV4 route info
        
        .. attribute:: track_info
        
        	track info
        	**type**\: list of    :py:class:`TrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_info = YList()
            self.track_info.parent = self
            self.track_info.name = 'track_info'


        class TrackInfo(object):
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
            	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bool_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks()
                self.bool_tracks.parent = self
                self.delayed = ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed()
                self.delayed.parent = self
                self.seconds_last_change = None
                self.state_change_counter = None
                self.threshold_down = None
                self.threshold_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks()
                self.threshold_tracks.parent = self
                self.threshold_up = None
                self.track_state = None
                self.track_type_info = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo()
                self.track_type_info.parent = self
                self.tracke_name = None
                self.tracking_interaces = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces()
                self.tracking_interaces.parent = self
                self.type = None


            class TrackTypeInfo(object):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
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
                    self.parent = None
                    self.bfd_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self.discriminant = None
                    self.interface_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self.ipsla_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self.route_tracks = ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self


                class InterfaceTracks(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.InterfaceTracks']['meta_info']


                class RouteTracks(object):
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
                        self.parent = None
                        self.next_hop = None
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.RouteTracks']['meta_info']


                class IpslaTracks(object):
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
                        self.parent = None
                        self.ipsla_op_id = None
                        self.return_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipsla_op_id is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.IpslaTracks']['meta_info']


                class BfdTracks(object):
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
                        self.parent = None
                        self.debounce_count = None
                        self.destination_address = None
                        self.interface_name = None
                        self.rate = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.debounce_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo.BfdTracks']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                        return True

                    if self.discriminant is not None:
                        return True

                    if self.interface_tracks is not None and self.interface_tracks._has_data():
                        return True

                    if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                        return True

                    if self.route_tracks is not None and self.route_tracks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackTypeInfo']['meta_info']


            class BoolTracks(object):
                """
                boolean objects
                
                .. attribute:: bool_track_info
                
                	bool track info
                	**type**\: list of    :py:class:`BoolTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bool_track_info = YList()
                    self.bool_track_info.parent = self
                    self.bool_track_info.name = 'bool_track_info'


                class BoolTrackInfo(object):
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
                        self.parent = None
                        self.object_name = None
                        self.track_state = None
                        self.with_not = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks/Cisco-IOS-XR-manageability-object-tracking-oper:bool-track-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        if self.with_not is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks.BoolTrackInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:bool-tracks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bool_track_info is not None:
                        for child_ref in self.bool_track_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.BoolTracks']['meta_info']


            class ThresholdTracks(object):
                """
                Threshold objects
                
                .. attribute:: threshold_track_info
                
                	threshold track info
                	**type**\: list of    :py:class:`ThresholdTrackInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.threshold_track_info = YList()
                    self.threshold_track_info.parent = self
                    self.threshold_track_info.name = 'threshold_track_info'


                class ThresholdTrackInfo(object):
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
                        self.parent = None
                        self.object_name = None
                        self.track_state = None
                        self.weight = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-track-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.object_name is not None:
                            return True

                        if self.track_state is not None:
                            return True

                        if self.weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks.ThresholdTrackInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:threshold-tracks'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.threshold_track_info is not None:
                        for child_ref in self.threshold_track_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.ThresholdTracks']['meta_info']


            class TrackingInteraces(object):
                """
                Tracking Interfaces
                
                .. attribute:: interface_tracking_info
                
                	interface tracking info
                	**type**\: list of    :py:class:`InterfaceTrackingInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo>`
                
                

                """

                _prefix = 'manageability-object-tracking-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_tracking_info = YList()
                    self.interface_tracking_info.parent = self
                    self.interface_tracking_info.name = 'interface_tracking_info'


                class InterfaceTrackingInfo(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracking-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces.InterfaceTrackingInfo']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:tracking-interaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_tracking_info is not None:
                        for child_ref in self.interface_tracking_info:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.TrackingInteraces']['meta_info']


            class Delayed(object):
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
                    self.parent = None
                    self.time_remaining = None
                    self.track_state = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info/Cisco-IOS-XR-manageability-object-tracking-oper:delayed'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.time_remaining is not None:
                        return True

                    if self.track_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo.Delayed']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route/Cisco-IOS-XR-manageability-object-tracking-oper:track-info'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bool_tracks is not None and self.bool_tracks._has_data():
                    return True

                if self.delayed is not None and self.delayed._has_data():
                    return True

                if self.seconds_last_change is not None:
                    return True

                if self.state_change_counter is not None:
                    return True

                if self.threshold_down is not None:
                    return True

                if self.threshold_tracks is not None and self.threshold_tracks._has_data():
                    return True

                if self.threshold_up is not None:
                    return True

                if self.track_state is not None:
                    return True

                if self.track_type_info is not None and self.track_type_info._has_data():
                    return True

                if self.tracke_name is not None:
                    return True

                if self.tracking_interaces is not None and self.tracking_interaces._has_data():
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackTypeIpv4Route.TrackInfo']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-ipv4-route'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_info is not None:
                for child_ref in self.track_info:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackTypeIpv4Route']['meta_info']


    class TrackTypeInterfaceBrief(object):
        """
        Object Tracking Type Interface brief info
        
        .. attribute:: track_info_brief
        
        	track info brief
        	**type**\: list of    :py:class:`TrackInfoBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief>`
        
        

        """

        _prefix = 'manageability-object-tracking-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.track_info_brief = YList()
            self.track_info_brief.parent = self
            self.track_info_brief.name = 'track_info_brief'


        class TrackInfoBrief(object):
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
            	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
            
            

            """

            _prefix = 'manageability-object-tracking-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.track_state = None
                self.track_type_info = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo()
                self.track_type_info.parent = self
                self.tracke_name = None
                self.type = None


            class TrackTypeInfo(object):
                """
                Track type information
                
                .. attribute:: bfd_tracks
                
                	track type bfdrtr info
                	**type**\:   :py:class:`BfdTracks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks>`
                
                .. attribute:: discriminant
                
                	discriminant
                	**type**\:   :py:class:`TrackEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_oper.TrackEnum>`
                
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
                    self.parent = None
                    self.bfd_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks()
                    self.bfd_tracks.parent = self
                    self.discriminant = None
                    self.interface_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks()
                    self.interface_tracks.parent = self
                    self.ipsla_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks()
                    self.ipsla_tracks.parent = self
                    self.route_tracks = ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks()
                    self.route_tracks.parent = self


                class InterfaceTracks(object):
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
                        self.parent = None
                        self.interface_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:interface-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.InterfaceTracks']['meta_info']


                class RouteTracks(object):
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
                        self.parent = None
                        self.next_hop = None
                        self.prefix = None
                        self.prefix_length = None
                        self.vrf = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:route-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.next_hop is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.vrf is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.RouteTracks']['meta_info']


                class IpslaTracks(object):
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
                        self.parent = None
                        self.ipsla_op_id = None
                        self.return_code = None
                        self.rtt = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:ipsla-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ipsla_op_id is not None:
                            return True

                        if self.return_code is not None:
                            return True

                        if self.rtt is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.IpslaTracks']['meta_info']


                class BfdTracks(object):
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
                        self.parent = None
                        self.debounce_count = None
                        self.destination_address = None
                        self.interface_name = None
                        self.rate = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info/Cisco-IOS-XR-manageability-object-tracking-oper:bfd-tracks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.debounce_count is not None:
                            return True

                        if self.destination_address is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.rate is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                        return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo.BfdTracks']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bfd_tracks is not None and self.bfd_tracks._has_data():
                        return True

                    if self.discriminant is not None:
                        return True

                    if self.interface_tracks is not None and self.interface_tracks._has_data():
                        return True

                    if self.ipsla_tracks is not None and self.ipsla_tracks._has_data():
                        return True

                    if self.route_tracks is not None and self.route_tracks._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                    return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief.TrackTypeInfo']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief/Cisco-IOS-XR-manageability-object-tracking-oper:track-info-brief'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.track_state is not None:
                    return True

                if self.track_type_info is not None and self.track_type_info._has_data():
                    return True

                if self.tracke_name is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
                return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief.TrackInfoBrief']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking/Cisco-IOS-XR-manageability-object-tracking-oper:track-type-interface-brief'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.track_info_brief is not None:
                for child_ref in self.track_info_brief:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
            return meta._meta_table['ObjectTracking.TrackTypeInterfaceBrief']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-manageability-object-tracking-oper:object-tracking'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.track_briefs is not None and self.track_briefs._has_data():
            return True

        if self.track_type_interface is not None and self.track_type_interface._has_data():
            return True

        if self.track_type_interface_brief is not None and self.track_type_interface_brief._has_data():
            return True

        if self.track_type_ipv4_route is not None and self.track_type_ipv4_route._has_data():
            return True

        if self.track_type_ipv4_route_brief is not None and self.track_type_ipv4_route_brief._has_data():
            return True

        if self.track_type_rtr_reachability is not None and self.track_type_rtr_reachability._has_data():
            return True

        if self.track_type_rtr_reachability_brief is not None and self.track_type_rtr_reachability_brief._has_data():
            return True

        if self.tracks is not None and self.tracks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_object_tracking_oper as meta
        return meta._meta_table['ObjectTracking']['meta_info']


