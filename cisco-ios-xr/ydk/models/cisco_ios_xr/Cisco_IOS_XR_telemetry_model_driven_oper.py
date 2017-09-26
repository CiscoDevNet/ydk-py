""" Cisco_IOS_XR_telemetry_model_driven_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package operational data.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Telemetry operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MdtDestStateEnum(Enum):
    """
    MdtDestStateEnum

    Destination state

    .. data:: dest_not_active = 0

    	NA

    .. data:: dest_active = 1

    	Active

    .. data:: dest_asking_pause = 2

    	AskingPause

    .. data:: dest_paused = 3

    	Paused

    .. data:: dest_resuming = 4

    	Resuming

    .. data:: dest_channel_not_found = 5

    	ChannelNotFound

    """

    dest_not_active = Enum.YLeaf(0, "dest-not-active")

    dest_active = Enum.YLeaf(1, "dest-active")

    dest_asking_pause = Enum.YLeaf(2, "dest-asking-pause")

    dest_paused = Enum.YLeaf(3, "dest-paused")

    dest_resuming = Enum.YLeaf(4, "dest-resuming")

    dest_channel_not_found = Enum.YLeaf(5, "dest-channel-not-found")


class MdtEncodingEnum(Enum):
    """
    MdtEncodingEnum

    MDT Encoding

    .. data:: not_set = 0

    	ENCODING NOT SET

    .. data:: gpb = 2

    	GPB

    .. data:: self_describing_gpb = 3

    	SELF DESCRIBING GPB

    .. data:: json = 4

    	JSON

    """

    not_set = Enum.YLeaf(0, "not-set")

    gpb = Enum.YLeaf(2, "gpb")

    self_describing_gpb = Enum.YLeaf(3, "self-describing-gpb")

    json = Enum.YLeaf(4, "json")


class MdtInternalPathStatus(Enum):
    """
    MdtInternalPathStatus

    Internal Subscription Path Status

    .. data:: active = 0

    	Active

    .. data:: internal_err = 1

    	Internal Error

    .. data:: plugin_active = 2

    	Plugin Active

    .. data:: plugin_not_initialized = 3

    	Plugin Not Initialized

    .. data:: plugin_invalid_cadence = 4

    	Plugin Unsupported Cadence

    .. data:: plugin_err = 5

    	Plugin Subscription Error

    .. data:: filter_err = 6

    	Filter Error

    .. data:: paused = 7

    	Paused

    .. data:: event_ing_active = 8

    	Eventing Active

    .. data:: event_ing_not_active = 9

    	Eventing Not Active

    .. data:: event_ing_err = 10

    	Eventing Error

    """

    active = Enum.YLeaf(0, "active")

    internal_err = Enum.YLeaf(1, "internal-err")

    plugin_active = Enum.YLeaf(2, "plugin-active")

    plugin_not_initialized = Enum.YLeaf(3, "plugin-not-initialized")

    plugin_invalid_cadence = Enum.YLeaf(4, "plugin-invalid-cadence")

    plugin_err = Enum.YLeaf(5, "plugin-err")

    filter_err = Enum.YLeaf(6, "filter-err")

    paused = Enum.YLeaf(7, "paused")

    event_ing_active = Enum.YLeaf(8, "event-ing-active")

    event_ing_not_active = Enum.YLeaf(9, "event-ing-not-active")

    event_ing_err = Enum.YLeaf(10, "event-ing-err")


class MdtIp(Enum):
    """
    MdtIp

    IP Type

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class MdtSourceQosMarking(Enum):
    """
    MdtSourceQosMarking

    DSCP source qos value for subscription

    .. data:: dscp_default = 0

    	0

    .. data:: dscp_cs1 = 8

    	8

    .. data:: dscp_af11 = 10

    	10

    .. data:: dscp_af12 = 12

    	12

    .. data:: dscp_af13 = 14

    	14

    .. data:: dscp_cs2 = 16

    	16

    .. data:: dscp_af21 = 18

    	18

    .. data:: dscp_af22 = 20

    	20

    .. data:: dscp_af23 = 22

    	22

    .. data:: dscp_cs3 = 24

    	24

    .. data:: dscp_af31 = 26

    	26

    .. data:: dscp_af32 = 28

    	28

    .. data:: dscp_af33 = 30

    	30

    .. data:: dscp_cs4 = 32

    	32

    .. data:: dscp_af41 = 34

    	34

    .. data:: dscp_af42 = 36

    	36

    .. data:: dscp_af43 = 38

    	38

    .. data:: dscp_cs5 = 40

    	40

    .. data:: dscp_ef = 46

    	46

    .. data:: dscp_cs6 = 48

    	48

    .. data:: dscp_cs7 = 56

    	56

    """

    dscp_default = Enum.YLeaf(0, "dscp-default")

    dscp_cs1 = Enum.YLeaf(8, "dscp-cs1")

    dscp_af11 = Enum.YLeaf(10, "dscp-af11")

    dscp_af12 = Enum.YLeaf(12, "dscp-af12")

    dscp_af13 = Enum.YLeaf(14, "dscp-af13")

    dscp_cs2 = Enum.YLeaf(16, "dscp-cs2")

    dscp_af21 = Enum.YLeaf(18, "dscp-af21")

    dscp_af22 = Enum.YLeaf(20, "dscp-af22")

    dscp_af23 = Enum.YLeaf(22, "dscp-af23")

    dscp_cs3 = Enum.YLeaf(24, "dscp-cs3")

    dscp_af31 = Enum.YLeaf(26, "dscp-af31")

    dscp_af32 = Enum.YLeaf(28, "dscp-af32")

    dscp_af33 = Enum.YLeaf(30, "dscp-af33")

    dscp_cs4 = Enum.YLeaf(32, "dscp-cs4")

    dscp_af41 = Enum.YLeaf(34, "dscp-af41")

    dscp_af42 = Enum.YLeaf(36, "dscp-af42")

    dscp_af43 = Enum.YLeaf(38, "dscp-af43")

    dscp_cs5 = Enum.YLeaf(40, "dscp-cs5")

    dscp_ef = Enum.YLeaf(46, "dscp-ef")

    dscp_cs6 = Enum.YLeaf(48, "dscp-cs6")

    dscp_cs7 = Enum.YLeaf(56, "dscp-cs7")


class MdtSubsStateEnum(Enum):
    """
    MdtSubsStateEnum

    Subscription State

    .. data:: not_active = 0

    	NA

    .. data:: active = 1

    	Active

    .. data:: paused = 2

    	Paused

    """

    not_active = Enum.YLeaf(0, "not-active")

    active = Enum.YLeaf(1, "active")

    paused = Enum.YLeaf(2, "paused")


class MdtTransportEnum(Enum):
    """
    MdtTransportEnum

    MDT Transport

    .. data:: not_set = 0

    	PROTOCOL NOT SET

    .. data:: grpc = 1

    	GRPC

    .. data:: tcp = 2

    	TCP

    .. data:: udp = 3

    	UDP

    .. data:: dialin = 6

    	DIALIN

    """

    not_set = Enum.YLeaf(0, "not-set")

    grpc = Enum.YLeaf(1, "grpc")

    tcp = Enum.YLeaf(2, "tcp")

    udp = Enum.YLeaf(3, "udp")

    dialin = Enum.YLeaf(6, "dialin")



class TelemetryModelDriven(Entity):
    """
    Telemetry operational data
    
    .. attribute:: destinations
    
    	Telemetry Destinations
    	**type**\:   :py:class:`Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations>`
    
    .. attribute:: sensor_groups
    
    	Telemetry Sensor Groups
    	**type**\:   :py:class:`SensorGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups>`
    
    .. attribute:: subscriptions
    
    	Telemetry Subscriptions
    	**type**\:   :py:class:`Subscriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions>`
    
    

    """

    _prefix = 'telemetry-model-driven-oper'
    _revision = '2017-05-05'

    def __init__(self):
        super(TelemetryModelDriven, self).__init__()
        self._top_entity = None

        self.yang_name = "telemetry-model-driven"
        self.yang_parent_name = "Cisco-IOS-XR-telemetry-model-driven-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"destinations" : ("destinations", TelemetryModelDriven.Destinations), "sensor-groups" : ("sensor_groups", TelemetryModelDriven.SensorGroups), "subscriptions" : ("subscriptions", TelemetryModelDriven.Subscriptions)}
        self._child_list_classes = {}

        self.destinations = TelemetryModelDriven.Destinations()
        self.destinations.parent = self
        self._children_name_map["destinations"] = "destinations"
        self._children_yang_names.add("destinations")

        self.sensor_groups = TelemetryModelDriven.SensorGroups()
        self.sensor_groups.parent = self
        self._children_name_map["sensor_groups"] = "sensor-groups"
        self._children_yang_names.add("sensor-groups")

        self.subscriptions = TelemetryModelDriven.Subscriptions()
        self.subscriptions.parent = self
        self._children_name_map["subscriptions"] = "subscriptions"
        self._children_yang_names.add("subscriptions")
        self._segment_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven"


    class Destinations(Entity):
        """
        Telemetry Destinations
        
        .. attribute:: destination
        
        	Telemetry Destination
        	**type**\: list of    :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(TelemetryModelDriven.Destinations, self).__init__()

            self.yang_name = "destinations"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"destination" : ("destination", TelemetryModelDriven.Destinations.Destination)}

            self.destination = YList(self)
            self._segment_path = lambda: "destinations"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Destinations, [], name, value)


        class Destination(Entity):
            """
            Telemetry Destination
            
            .. attribute:: destination_id  <key>
            
            	Id of the destination
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: configured
            
            	Set if this is configured destination group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: destination
            
            	list of destinations defined in this group
            	**type**\: list of    :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination>`
            
            .. attribute:: id
            
            	Destination Group name
            	**type**\:  str
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(TelemetryModelDriven.Destinations.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "destinations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"destination" : ("destination", TelemetryModelDriven.Destinations.Destination.Destination)}

                self.destination_id = YLeaf(YType.str, "destination-id")

                self.configured = YLeaf(YType.uint32, "configured")

                self.id = YLeaf(YType.str, "id")

                self.destination = YList(self)
                self._segment_path = lambda: "destination" + "[destination-id='" + self.destination_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/destinations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.Destinations.Destination, ['destination_id', 'configured', 'id'], name, value)


            class Destination(Entity):
                """
                list of destinations defined in this group
                
                .. attribute:: collection_group
                
                	List of collection groups for this destination group
                	**type**\: list of    :py:class:`CollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup>`
                
                .. attribute:: destination
                
                	Destination
                	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination.Destination>`
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(TelemetryModelDriven.Destinations.Destination.Destination, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "destination"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"destination" : ("destination", TelemetryModelDriven.Destinations.Destination.Destination.Destination)}
                    self._child_list_classes = {"collection-group" : ("collection_group", TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup)}

                    self.destination = TelemetryModelDriven.Destinations.Destination.Destination.Destination()
                    self.destination.parent = self
                    self._children_name_map["destination"] = "destination"
                    self._children_yang_names.add("destination")

                    self.collection_group = YList(self)
                    self._segment_path = lambda: "destination"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination, [], name, value)


                class CollectionGroup(Entity):
                    """
                    List of collection groups for this destination
                    group
                    
                    .. attribute:: avg_total_time
                    
                    	Average time for all processing (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cadence
                    
                    	Period of the collections (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: collection_path
                    
                    	Array of information for sensor paths within collection group
                    	**type**\: list of    :py:class:`CollectionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath>`
                    
                    .. attribute:: encoding
                    
                    	Destination group encoding
                    	**type**\:   :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                    
                    .. attribute:: id
                    
                    	Collection Group id
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: internal_collection_group
                    
                    	Array of information for sysdb paths within collection group
                    	**type**\: list of    :py:class:`InternalCollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup>`
                    
                    .. attribute:: last_collection_end_time
                    
                    	Timestamp of the end of last collection
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_collection_start_time
                    
                    	Timestamp of the start of last collection
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_collection_time
                    
                    	Maximum time for a collection (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_total_time
                    
                    	Maximum time for all processing (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_collection_time
                    
                    	Minimum time for a collection (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_total_time
                    
                    	Minimum time for all processing (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_collections
                    
                    	Completed collections count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_not_ready
                    
                    	Total number skipped (not ready)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_on_data_instances
                    
                    	Total number of no data instances
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_other_errors
                    
                    	Total number of errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_send_drops
                    
                    	Total number of send drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_send_errors
                    
                    	Total number of send errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup, self).__init__()

                        self.yang_name = "collection-group"
                        self.yang_parent_name = "destination"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"collection-path" : ("collection_path", TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath), "internal-collection-group" : ("internal_collection_group", TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup)}

                        self.avg_total_time = YLeaf(YType.uint32, "avg-total-time")

                        self.cadence = YLeaf(YType.uint32, "cadence")

                        self.encoding = YLeaf(YType.enumeration, "encoding")

                        self.id = YLeaf(YType.uint64, "id")

                        self.last_collection_end_time = YLeaf(YType.uint64, "last-collection-end-time")

                        self.last_collection_start_time = YLeaf(YType.uint64, "last-collection-start-time")

                        self.max_collection_time = YLeaf(YType.uint32, "max-collection-time")

                        self.max_total_time = YLeaf(YType.uint32, "max-total-time")

                        self.min_collection_time = YLeaf(YType.uint32, "min-collection-time")

                        self.min_total_time = YLeaf(YType.uint32, "min-total-time")

                        self.total_collections = YLeaf(YType.uint32, "total-collections")

                        self.total_not_ready = YLeaf(YType.uint32, "total-not-ready")

                        self.total_on_data_instances = YLeaf(YType.uint32, "total-on-data-instances")

                        self.total_other_errors = YLeaf(YType.uint32, "total-other-errors")

                        self.total_send_drops = YLeaf(YType.uint32, "total-send-drops")

                        self.total_send_errors = YLeaf(YType.uint32, "total-send-errors")

                        self.collection_path = YList(self)
                        self.internal_collection_group = YList(self)
                        self._segment_path = lambda: "collection-group"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup, ['avg_total_time', 'cadence', 'encoding', 'id', 'last_collection_end_time', 'last_collection_start_time', 'max_collection_time', 'max_total_time', 'min_collection_time', 'min_total_time', 'total_collections', 'total_not_ready', 'total_on_data_instances', 'total_other_errors', 'total_send_drops', 'total_send_errors'], name, value)


                    class CollectionPath(Entity):
                        """
                        Array of information for sensor paths within
                        collection group
                        
                        .. attribute:: path
                        
                        	Sensor Path
                        	**type**\:  str
                        
                        .. attribute:: state
                        
                        	State, if sensor path is resolved or not
                        	**type**\:  bool
                        
                        .. attribute:: status_str
                        
                        	Error str, if there are any errors resolving the sensor path
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath, self).__init__()

                            self.yang_name = "collection-path"
                            self.yang_parent_name = "collection-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.path = YLeaf(YType.str, "path")

                            self.state = YLeaf(YType.boolean, "state")

                            self.status_str = YLeaf(YType.str, "status-str")
                            self._segment_path = lambda: "collection-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath, ['path', 'state', 'status_str'], name, value)


                    class InternalCollectionGroup(Entity):
                        """
                        Array of information for sysdb paths within
                        collection group
                        
                        .. attribute:: avg_collection_time
                        
                        	Average time for a collection (ms)
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: cadence
                        
                        	Period of the collections (ms)
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: collection_method
                        
                        	Collection method in use
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: max_collection_time
                        
                        	Maximum time for a collection (ms)
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: min_collection_time
                        
                        	Minimum time for a collection (ms)
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: path
                        
                        	Sysdb Path
                        	**type**\:  str
                        
                        .. attribute:: status
                        
                        	Status of collection path
                        	**type**\:   :py:class:`MdtInternalPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtInternalPathStatus>`
                        
                        .. attribute:: total_collections
                        
                        	Completed collections count
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_collections_missed
                        
                        	Total number of collections missed
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_datalist_count
                        
                        	Total number of datalists
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_datalist_errors
                        
                        	Total number of datalist errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_encode_errors
                        
                        	Total number of encode errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_encode_notready
                        
                        	Total number of encode deferred
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_finddata_count
                        
                        	Total number of finddata
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_finddata_errors
                        
                        	Total number of finddata errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_bulk_count
                        
                        	Total number of get bulk
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_bulk_errors
                        
                        	Total number of get bulk errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_count
                        
                        	Total number of gets
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_errors
                        
                        	Total number of get errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_item_count
                        
                        	Total number of items retrived from sysdb
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_list_count
                        
                        	Total number of lists
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_list_errors
                        
                        	Total number of list errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_send_bytes_dropped
                        
                        	Total number of send bytes dropped
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: total_send_drops
                        
                        	Total number of send channel full
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_send_errors
                        
                        	Total number of send errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_send_packets
                        
                        	Total number of packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_sent_bytes
                        
                        	Total number of bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup, self).__init__()

                            self.yang_name = "internal-collection-group"
                            self.yang_parent_name = "collection-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.avg_collection_time = YLeaf(YType.uint64, "avg-collection-time")

                            self.cadence = YLeaf(YType.uint64, "cadence")

                            self.collection_method = YLeaf(YType.uint64, "collection-method")

                            self.max_collection_time = YLeaf(YType.uint64, "max-collection-time")

                            self.min_collection_time = YLeaf(YType.uint64, "min-collection-time")

                            self.path = YLeaf(YType.str, "path")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.total_collections = YLeaf(YType.uint64, "total-collections")

                            self.total_collections_missed = YLeaf(YType.uint64, "total-collections-missed")

                            self.total_datalist_count = YLeaf(YType.uint64, "total-datalist-count")

                            self.total_datalist_errors = YLeaf(YType.uint64, "total-datalist-errors")

                            self.total_encode_errors = YLeaf(YType.uint64, "total-encode-errors")

                            self.total_encode_notready = YLeaf(YType.uint64, "total-encode-notready")

                            self.total_finddata_count = YLeaf(YType.uint64, "total-finddata-count")

                            self.total_finddata_errors = YLeaf(YType.uint64, "total-finddata-errors")

                            self.total_get_bulk_count = YLeaf(YType.uint64, "total-get-bulk-count")

                            self.total_get_bulk_errors = YLeaf(YType.uint64, "total-get-bulk-errors")

                            self.total_get_count = YLeaf(YType.uint64, "total-get-count")

                            self.total_get_errors = YLeaf(YType.uint64, "total-get-errors")

                            self.total_item_count = YLeaf(YType.uint64, "total-item-count")

                            self.total_list_count = YLeaf(YType.uint64, "total-list-count")

                            self.total_list_errors = YLeaf(YType.uint64, "total-list-errors")

                            self.total_send_bytes_dropped = YLeaf(YType.uint64, "total-send-bytes-dropped")

                            self.total_send_drops = YLeaf(YType.uint64, "total-send-drops")

                            self.total_send_errors = YLeaf(YType.uint64, "total-send-errors")

                            self.total_send_packets = YLeaf(YType.uint64, "total-send-packets")

                            self.total_sent_bytes = YLeaf(YType.uint64, "total-sent-bytes")
                            self._segment_path = lambda: "internal-collection-group"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup, ['avg_collection_time', 'cadence', 'collection_method', 'max_collection_time', 'min_collection_time', 'path', 'status', 'total_collections', 'total_collections_missed', 'total_datalist_count', 'total_datalist_errors', 'total_encode_errors', 'total_encode_notready', 'total_finddata_count', 'total_finddata_errors', 'total_get_bulk_count', 'total_get_bulk_errors', 'total_get_count', 'total_get_errors', 'total_item_count', 'total_list_count', 'total_list_errors', 'total_send_bytes_dropped', 'total_send_drops', 'total_send_errors', 'total_send_packets', 'total_sent_bytes'], name, value)


                class Destination(Entity):
                    """
                    Destination
                    
                    .. attribute:: dest_ip_address
                    
                    	Destination IP Address
                    	**type**\:   :py:class:`DestIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress>`
                    
                    .. attribute:: dest_port
                    
                    	Destination Port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: dscp
                    
                    	DSCP setting for this destination
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: encoding
                    
                    	Destination group encoding
                    	**type**\:   :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                    
                    .. attribute:: id
                    
                    	Destination Id
                    	**type**\:  str
                    
                    .. attribute:: last_collection_time
                    
                    	Timestamp of the last collection
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: state
                    
                    	State of streaming on this destination
                    	**type**\:   :py:class:`MdtDestStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtDestStateEnum>`
                    
                    .. attribute:: sub_id
                    
                    	Sub Id
                    	**type**\:  list of int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: sub_id_str
                    
                    	Sub Idstr
                    	**type**\:  str
                    
                    .. attribute:: tls
                    
                    	TLS connection to this destination
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tls_host
                    
                    	TLS Hostname of this destination
                    	**type**\:  str
                    
                    .. attribute:: total_num_of_bytes_sent
                    
                    	Total number of bytes sent for this destination
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: total_num_of_packets_sent
                    
                    	Total number of packets sent for this destination
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: transport
                    
                    	Destination group transport
                    	**type**\:   :py:class:`MdtTransportEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtTransportEnum>`
                    
                    .. attribute:: udp_mtu
                    
                    	UDP MTU if this destination is UDP
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf
                    
                    	Destination group vrf
                    	**type**\:  str
                    
                    .. attribute:: vrf_id
                    
                    	Destination group vrf id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Destinations.Destination.Destination.Destination, self).__init__()

                        self.yang_name = "destination"
                        self.yang_parent_name = "destination"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"dest-ip-address" : ("dest_ip_address", TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress)}
                        self._child_list_classes = {}

                        self.dest_port = YLeaf(YType.uint16, "dest-port")

                        self.dscp = YLeaf(YType.uint32, "dscp")

                        self.encoding = YLeaf(YType.enumeration, "encoding")

                        self.id = YLeaf(YType.str, "id")

                        self.last_collection_time = YLeaf(YType.uint64, "last-collection-time")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.sub_id = YLeafList(YType.uint64, "sub-id")

                        self.sub_id_str = YLeaf(YType.str, "sub-id-str")

                        self.tls = YLeaf(YType.uint32, "tls")

                        self.tls_host = YLeaf(YType.str, "tls-host")

                        self.total_num_of_bytes_sent = YLeaf(YType.uint64, "total-num-of-bytes-sent")

                        self.total_num_of_packets_sent = YLeaf(YType.uint64, "total-num-of-packets-sent")

                        self.transport = YLeaf(YType.enumeration, "transport")

                        self.udp_mtu = YLeaf(YType.uint32, "udp-mtu")

                        self.vrf = YLeaf(YType.str, "vrf")

                        self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                        self.dest_ip_address = TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress()
                        self.dest_ip_address.parent = self
                        self._children_name_map["dest_ip_address"] = "dest-ip-address"
                        self._children_yang_names.add("dest-ip-address")
                        self._segment_path = lambda: "destination"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination.Destination, ['dest_port', 'dscp', 'encoding', 'id', 'last_collection_time', 'state', 'sub_id', 'sub_id_str', 'tls', 'tls_host', 'total_num_of_bytes_sent', 'total_num_of_packets_sent', 'transport', 'udp_mtu', 'vrf', 'vrf_id'], name, value)


                    class DestIpAddress(Entity):
                        """
                        Destination IP Address
                        
                        .. attribute:: ip_type
                        
                        	IPType
                        	**type**\:   :py:class:`MdtIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtIp>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPV4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPV6 Address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress, self).__init__()

                            self.yang_name = "dest-ip-address"
                            self.yang_parent_name = "destination"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ip_type = YLeaf(YType.enumeration, "ip-type")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                            self._segment_path = lambda: "dest-ip-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress, ['ip_type', 'ipv4_address', 'ipv6_address'], name, value)


    class SensorGroups(Entity):
        """
        Telemetry Sensor Groups
        
        .. attribute:: sensor_group
        
        	Telemetry Sensor Groups
        	**type**\: list of    :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(TelemetryModelDriven.SensorGroups, self).__init__()

            self.yang_name = "sensor-groups"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"sensor-group" : ("sensor_group", TelemetryModelDriven.SensorGroups.SensorGroup)}

            self.sensor_group = YList(self)
            self._segment_path = lambda: "sensor-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.SensorGroups, [], name, value)


        class SensorGroup(Entity):
            """
            Telemetry Sensor Groups
            
            .. attribute:: sensor_group_id  <key>
            
            	Id of the sensor group
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: configured
            
            	Set if this is configured sensor group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: id
            
            	Sensor Group name
            	**type**\:  str
            
            .. attribute:: sensor_path
            
            	Array of information for sensor paths within sensor group
            	**type**\: list of    :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath>`
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__init__()

                self.yang_name = "sensor-group"
                self.yang_parent_name = "sensor-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"sensor-path" : ("sensor_path", TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath)}

                self.sensor_group_id = YLeaf(YType.str, "sensor-group-id")

                self.configured = YLeaf(YType.uint32, "configured")

                self.id = YLeaf(YType.str, "id")

                self.sensor_path = YList(self)
                self._segment_path = lambda: "sensor-group" + "[sensor-group-id='" + self.sensor_group_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/sensor-groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup, ['sensor_group_id', 'configured', 'id'], name, value)


            class SensorPath(Entity):
                """
                Array of information for sensor paths within
                sensor group
                
                .. attribute:: path
                
                	Sensor Path
                	**type**\:  str
                
                .. attribute:: state
                
                	State, if sensor path is resolved or not
                	**type**\:  bool
                
                .. attribute:: status_str
                
                	Error str, if there are any errors resolving the sensor path
                	**type**\:  str
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath, self).__init__()

                    self.yang_name = "sensor-path"
                    self.yang_parent_name = "sensor-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.path = YLeaf(YType.str, "path")

                    self.state = YLeaf(YType.boolean, "state")

                    self.status_str = YLeaf(YType.str, "status-str")
                    self._segment_path = lambda: "sensor-path"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath, ['path', 'state', 'status_str'], name, value)


    class Subscriptions(Entity):
        """
        Telemetry Subscriptions
        
        .. attribute:: subscription
        
        	Telemetry Subscription
        	**type**\: list of    :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-05-05'

        def __init__(self):
            super(TelemetryModelDriven.Subscriptions, self).__init__()

            self.yang_name = "subscriptions"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"subscription" : ("subscription", TelemetryModelDriven.Subscriptions.Subscription)}

            self.subscription = YList(self)
            self._segment_path = lambda: "subscriptions"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Subscriptions, [], name, value)


        class Subscription(Entity):
            """
            Telemetry Subscription
            
            .. attribute:: subscription_id  <key>
            
            	Id of the subscription
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: collection_group
            
            	List of collection groups active for this subscription
            	**type**\: list of    :py:class:`CollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup>`
            
            .. attribute:: subscription
            
            	Subscription
            	**type**\:   :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription>`
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2017-05-05'

            def __init__(self):
                super(TelemetryModelDriven.Subscriptions.Subscription, self).__init__()

                self.yang_name = "subscription"
                self.yang_parent_name = "subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"subscription" : ("subscription", TelemetryModelDriven.Subscriptions.Subscription.Subscription)}
                self._child_list_classes = {"collection-group" : ("collection_group", TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup)}

                self.subscription_id = YLeaf(YType.str, "subscription-id")

                self.subscription = TelemetryModelDriven.Subscriptions.Subscription.Subscription()
                self.subscription.parent = self
                self._children_name_map["subscription"] = "subscription"
                self._children_yang_names.add("subscription")

                self.collection_group = YList(self)
                self._segment_path = lambda: "subscription" + "[subscription-id='" + self.subscription_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/subscriptions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription, ['subscription_id'], name, value)


            class CollectionGroup(Entity):
                """
                List of collection groups active for this
                subscription
                
                .. attribute:: avg_total_time
                
                	Average time for all processing (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cadence
                
                	Period of the collections (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: collection_path
                
                	Array of information for sensor paths within collection group
                	**type**\: list of    :py:class:`CollectionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath>`
                
                .. attribute:: encoding
                
                	Destination group encoding
                	**type**\:   :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                
                .. attribute:: id
                
                	Collection Group id
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: internal_collection_group
                
                	Array of information for sysdb paths within collection group
                	**type**\: list of    :py:class:`InternalCollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup>`
                
                .. attribute:: last_collection_end_time
                
                	Timestamp of the end of last collection
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: last_collection_start_time
                
                	Timestamp of the start of last collection
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: max_collection_time
                
                	Maximum time for a collection (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_total_time
                
                	Maximum time for all processing (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_collection_time
                
                	Minimum time for a collection (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_total_time
                
                	Minimum time for all processing (ms)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_collections
                
                	Completed collections count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_not_ready
                
                	Total number skipped (not ready)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_on_data_instances
                
                	Total number of no data instances
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_other_errors
                
                	Total number of errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_send_drops
                
                	Total number of send drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_send_errors
                
                	Total number of send errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup, self).__init__()

                    self.yang_name = "collection-group"
                    self.yang_parent_name = "subscription"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"collection-path" : ("collection_path", TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath), "internal-collection-group" : ("internal_collection_group", TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup)}

                    self.avg_total_time = YLeaf(YType.uint32, "avg-total-time")

                    self.cadence = YLeaf(YType.uint32, "cadence")

                    self.encoding = YLeaf(YType.enumeration, "encoding")

                    self.id = YLeaf(YType.uint64, "id")

                    self.last_collection_end_time = YLeaf(YType.uint64, "last-collection-end-time")

                    self.last_collection_start_time = YLeaf(YType.uint64, "last-collection-start-time")

                    self.max_collection_time = YLeaf(YType.uint32, "max-collection-time")

                    self.max_total_time = YLeaf(YType.uint32, "max-total-time")

                    self.min_collection_time = YLeaf(YType.uint32, "min-collection-time")

                    self.min_total_time = YLeaf(YType.uint32, "min-total-time")

                    self.total_collections = YLeaf(YType.uint32, "total-collections")

                    self.total_not_ready = YLeaf(YType.uint32, "total-not-ready")

                    self.total_on_data_instances = YLeaf(YType.uint32, "total-on-data-instances")

                    self.total_other_errors = YLeaf(YType.uint32, "total-other-errors")

                    self.total_send_drops = YLeaf(YType.uint32, "total-send-drops")

                    self.total_send_errors = YLeaf(YType.uint32, "total-send-errors")

                    self.collection_path = YList(self)
                    self.internal_collection_group = YList(self)
                    self._segment_path = lambda: "collection-group"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup, ['avg_total_time', 'cadence', 'encoding', 'id', 'last_collection_end_time', 'last_collection_start_time', 'max_collection_time', 'max_total_time', 'min_collection_time', 'min_total_time', 'total_collections', 'total_not_ready', 'total_on_data_instances', 'total_other_errors', 'total_send_drops', 'total_send_errors'], name, value)


                class CollectionPath(Entity):
                    """
                    Array of information for sensor paths within
                    collection group
                    
                    .. attribute:: path
                    
                    	Sensor Path
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	State, if sensor path is resolved or not
                    	**type**\:  bool
                    
                    .. attribute:: status_str
                    
                    	Error str, if there are any errors resolving the sensor path
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath, self).__init__()

                        self.yang_name = "collection-path"
                        self.yang_parent_name = "collection-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.path = YLeaf(YType.str, "path")

                        self.state = YLeaf(YType.boolean, "state")

                        self.status_str = YLeaf(YType.str, "status-str")
                        self._segment_path = lambda: "collection-path"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath, ['path', 'state', 'status_str'], name, value)


                class InternalCollectionGroup(Entity):
                    """
                    Array of information for sysdb paths within
                    collection group
                    
                    .. attribute:: avg_collection_time
                    
                    	Average time for a collection (ms)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: cadence
                    
                    	Period of the collections (ms)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: collection_method
                    
                    	Collection method in use
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_collection_time
                    
                    	Maximum time for a collection (ms)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: min_collection_time
                    
                    	Minimum time for a collection (ms)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: path
                    
                    	Sysdb Path
                    	**type**\:  str
                    
                    .. attribute:: status
                    
                    	Status of collection path
                    	**type**\:   :py:class:`MdtInternalPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtInternalPathStatus>`
                    
                    .. attribute:: total_collections
                    
                    	Completed collections count
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_collections_missed
                    
                    	Total number of collections missed
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_datalist_count
                    
                    	Total number of datalists
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_datalist_errors
                    
                    	Total number of datalist errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_encode_errors
                    
                    	Total number of encode errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_encode_notready
                    
                    	Total number of encode deferred
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_finddata_count
                    
                    	Total number of finddata
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_finddata_errors
                    
                    	Total number of finddata errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_bulk_count
                    
                    	Total number of get bulk
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_bulk_errors
                    
                    	Total number of get bulk errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_count
                    
                    	Total number of gets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_errors
                    
                    	Total number of get errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_item_count
                    
                    	Total number of items retrived from sysdb
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_list_count
                    
                    	Total number of lists
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_list_errors
                    
                    	Total number of list errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_send_bytes_dropped
                    
                    	Total number of send bytes dropped
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: total_send_drops
                    
                    	Total number of send channel full
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_send_errors
                    
                    	Total number of send errors
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_send_packets
                    
                    	Total number of packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_sent_bytes
                    
                    	Total number of bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup, self).__init__()

                        self.yang_name = "internal-collection-group"
                        self.yang_parent_name = "collection-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.avg_collection_time = YLeaf(YType.uint64, "avg-collection-time")

                        self.cadence = YLeaf(YType.uint64, "cadence")

                        self.collection_method = YLeaf(YType.uint64, "collection-method")

                        self.max_collection_time = YLeaf(YType.uint64, "max-collection-time")

                        self.min_collection_time = YLeaf(YType.uint64, "min-collection-time")

                        self.path = YLeaf(YType.str, "path")

                        self.status = YLeaf(YType.enumeration, "status")

                        self.total_collections = YLeaf(YType.uint64, "total-collections")

                        self.total_collections_missed = YLeaf(YType.uint64, "total-collections-missed")

                        self.total_datalist_count = YLeaf(YType.uint64, "total-datalist-count")

                        self.total_datalist_errors = YLeaf(YType.uint64, "total-datalist-errors")

                        self.total_encode_errors = YLeaf(YType.uint64, "total-encode-errors")

                        self.total_encode_notready = YLeaf(YType.uint64, "total-encode-notready")

                        self.total_finddata_count = YLeaf(YType.uint64, "total-finddata-count")

                        self.total_finddata_errors = YLeaf(YType.uint64, "total-finddata-errors")

                        self.total_get_bulk_count = YLeaf(YType.uint64, "total-get-bulk-count")

                        self.total_get_bulk_errors = YLeaf(YType.uint64, "total-get-bulk-errors")

                        self.total_get_count = YLeaf(YType.uint64, "total-get-count")

                        self.total_get_errors = YLeaf(YType.uint64, "total-get-errors")

                        self.total_item_count = YLeaf(YType.uint64, "total-item-count")

                        self.total_list_count = YLeaf(YType.uint64, "total-list-count")

                        self.total_list_errors = YLeaf(YType.uint64, "total-list-errors")

                        self.total_send_bytes_dropped = YLeaf(YType.uint64, "total-send-bytes-dropped")

                        self.total_send_drops = YLeaf(YType.uint64, "total-send-drops")

                        self.total_send_errors = YLeaf(YType.uint64, "total-send-errors")

                        self.total_send_packets = YLeaf(YType.uint64, "total-send-packets")

                        self.total_sent_bytes = YLeaf(YType.uint64, "total-sent-bytes")
                        self._segment_path = lambda: "internal-collection-group"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup, ['avg_collection_time', 'cadence', 'collection_method', 'max_collection_time', 'min_collection_time', 'path', 'status', 'total_collections', 'total_collections_missed', 'total_datalist_count', 'total_datalist_errors', 'total_encode_errors', 'total_encode_notready', 'total_finddata_count', 'total_finddata_errors', 'total_get_bulk_count', 'total_get_bulk_errors', 'total_get_count', 'total_get_errors', 'total_item_count', 'total_list_count', 'total_list_errors', 'total_send_bytes_dropped', 'total_send_drops', 'total_send_errors', 'total_send_packets', 'total_sent_bytes'], name, value)


            class Subscription(Entity):
                """
                Subscription
                
                .. attribute:: destination_grp
                
                	Array of destinations within a subscription
                	**type**\: list of    :py:class:`DestinationGrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp>`
                
                .. attribute:: id
                
                	Collection Subscription name
                	**type**\:  str
                
                .. attribute:: sensor_profile
                
                	List of sensor groups within a subscription
                	**type**\: list of    :py:class:`SensorProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile>`
                
                .. attribute:: source_interface
                
                	configured source interface
                	**type**\:   :py:class:`SourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface>`
                
                .. attribute:: source_qos_marking
                
                	DSCP
                	**type**\:   :py:class:`MdtSourceQosMarking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtSourceQosMarking>`
                
                .. attribute:: state
                
                	Subscription state
                	**type**\:   :py:class:`MdtSubsStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtSubsStateEnum>`
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-05-05'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription, self).__init__()

                    self.yang_name = "subscription"
                    self.yang_parent_name = "subscription"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"source-interface" : ("source_interface", TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface)}
                    self._child_list_classes = {"destination-grp" : ("destination_grp", TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp), "sensor-profile" : ("sensor_profile", TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile)}

                    self.id = YLeaf(YType.str, "id")

                    self.source_qos_marking = YLeaf(YType.enumeration, "source-qos-marking")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.source_interface = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface()
                    self.source_interface.parent = self
                    self._children_name_map["source_interface"] = "source-interface"
                    self._children_yang_names.add("source-interface")

                    self.destination_grp = YList(self)
                    self.sensor_profile = YList(self)
                    self._segment_path = lambda: "subscription"

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription, ['id', 'source_qos_marking', 'state'], name, value)


                class DestinationGrp(Entity):
                    """
                    Array of destinations within a subscription
                    
                    .. attribute:: configured
                    
                    	Set if this is configured destination group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination
                    
                    	list of destinations defined in this group
                    	**type**\: list of    :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination>`
                    
                    .. attribute:: id
                    
                    	Destination Group name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp, self).__init__()

                        self.yang_name = "destination-grp"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"destination" : ("destination", TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination)}

                        self.configured = YLeaf(YType.uint32, "configured")

                        self.id = YLeaf(YType.str, "id")

                        self.destination = YList(self)
                        self._segment_path = lambda: "destination-grp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp, ['configured', 'id'], name, value)


                    class Destination(Entity):
                        """
                        list of destinations defined in this group
                        
                        .. attribute:: dest_ip_address
                        
                        	Destination IP Address
                        	**type**\:   :py:class:`DestIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress>`
                        
                        .. attribute:: dest_port
                        
                        	Destination Port number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: dscp
                        
                        	DSCP setting for this destination
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: encoding
                        
                        	Destination group encoding
                        	**type**\:   :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                        
                        .. attribute:: id
                        
                        	Destination Id
                        	**type**\:  str
                        
                        .. attribute:: last_collection_time
                        
                        	Timestamp of the last collection
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: state
                        
                        	State of streaming on this destination
                        	**type**\:   :py:class:`MdtDestStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtDestStateEnum>`
                        
                        .. attribute:: sub_id
                        
                        	Sub Id
                        	**type**\:  list of int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sub_id_str
                        
                        	Sub Idstr
                        	**type**\:  str
                        
                        .. attribute:: tls
                        
                        	TLS connection to this destination
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tls_host
                        
                        	TLS Hostname of this destination
                        	**type**\:  str
                        
                        .. attribute:: total_num_of_bytes_sent
                        
                        	Total number of bytes sent for this destination
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: total_num_of_packets_sent
                        
                        	Total number of packets sent for this destination
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: transport
                        
                        	Destination group transport
                        	**type**\:   :py:class:`MdtTransportEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtTransportEnum>`
                        
                        .. attribute:: udp_mtu
                        
                        	UDP MTU if this destination is UDP
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf
                        
                        	Destination group vrf
                        	**type**\:  str
                        
                        .. attribute:: vrf_id
                        
                        	Destination group vrf id
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination, self).__init__()

                            self.yang_name = "destination"
                            self.yang_parent_name = "destination-grp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"dest-ip-address" : ("dest_ip_address", TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress)}
                            self._child_list_classes = {}

                            self.dest_port = YLeaf(YType.uint16, "dest-port")

                            self.dscp = YLeaf(YType.uint32, "dscp")

                            self.encoding = YLeaf(YType.enumeration, "encoding")

                            self.id = YLeaf(YType.str, "id")

                            self.last_collection_time = YLeaf(YType.uint64, "last-collection-time")

                            self.state = YLeaf(YType.enumeration, "state")

                            self.sub_id = YLeafList(YType.uint64, "sub-id")

                            self.sub_id_str = YLeaf(YType.str, "sub-id-str")

                            self.tls = YLeaf(YType.uint32, "tls")

                            self.tls_host = YLeaf(YType.str, "tls-host")

                            self.total_num_of_bytes_sent = YLeaf(YType.uint64, "total-num-of-bytes-sent")

                            self.total_num_of_packets_sent = YLeaf(YType.uint64, "total-num-of-packets-sent")

                            self.transport = YLeaf(YType.enumeration, "transport")

                            self.udp_mtu = YLeaf(YType.uint32, "udp-mtu")

                            self.vrf = YLeaf(YType.str, "vrf")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.dest_ip_address = TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress()
                            self.dest_ip_address.parent = self
                            self._children_name_map["dest_ip_address"] = "dest-ip-address"
                            self._children_yang_names.add("dest-ip-address")
                            self._segment_path = lambda: "destination"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination, ['dest_port', 'dscp', 'encoding', 'id', 'last_collection_time', 'state', 'sub_id', 'sub_id_str', 'tls', 'tls_host', 'total_num_of_bytes_sent', 'total_num_of_packets_sent', 'transport', 'udp_mtu', 'vrf', 'vrf_id'], name, value)


                        class DestIpAddress(Entity):
                            """
                            Destination IP Address
                            
                            .. attribute:: ip_type
                            
                            	IPType
                            	**type**\:   :py:class:`MdtIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtIp>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPV4 Address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPV6 Address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'telemetry-model-driven-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress, self).__init__()

                                self.yang_name = "dest-ip-address"
                                self.yang_parent_name = "destination"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ip_type = YLeaf(YType.enumeration, "ip-type")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")
                                self._segment_path = lambda: "dest-ip-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress, ['ip_type', 'ipv4_address', 'ipv6_address'], name, value)


                class SensorProfile(Entity):
                    """
                    List of sensor groups within a subscription
                    
                    .. attribute:: heartbeat_interval
                    
                    	Heartbeat interval for the sensor group (s)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sample_interval
                    
                    	Sample interval for the sensor group (ms)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sensor_group
                    
                    	sensor group
                    	**type**\:   :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup>`
                    
                    .. attribute:: suppress_redundant
                    
                    	Suppress Redundant
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile, self).__init__()

                        self.yang_name = "sensor-profile"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"sensor-group" : ("sensor_group", TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup)}
                        self._child_list_classes = {}

                        self.heartbeat_interval = YLeaf(YType.uint32, "heartbeat-interval")

                        self.sample_interval = YLeaf(YType.uint32, "sample-interval")

                        self.suppress_redundant = YLeaf(YType.boolean, "suppress-redundant")

                        self.sensor_group = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup()
                        self.sensor_group.parent = self
                        self._children_name_map["sensor_group"] = "sensor-group"
                        self._children_yang_names.add("sensor-group")
                        self._segment_path = lambda: "sensor-profile"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile, ['heartbeat_interval', 'sample_interval', 'suppress_redundant'], name, value)


                    class SensorGroup(Entity):
                        """
                        sensor group
                        
                        .. attribute:: configured
                        
                        	Set if this is configured sensor group
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: id
                        
                        	Sensor Group name
                        	**type**\:  str
                        
                        .. attribute:: sensor_path
                        
                        	Array of information for sensor paths within sensor group
                        	**type**\: list of    :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath>`
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-05-05'

                        def __init__(self):
                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup, self).__init__()

                            self.yang_name = "sensor-group"
                            self.yang_parent_name = "sensor-profile"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sensor-path" : ("sensor_path", TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath)}

                            self.configured = YLeaf(YType.uint32, "configured")

                            self.id = YLeaf(YType.str, "id")

                            self.sensor_path = YList(self)
                            self._segment_path = lambda: "sensor-group"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup, ['configured', 'id'], name, value)


                        class SensorPath(Entity):
                            """
                            Array of information for sensor paths within
                            sensor group
                            
                            .. attribute:: path
                            
                            	Sensor Path
                            	**type**\:  str
                            
                            .. attribute:: state
                            
                            	State, if sensor path is resolved or not
                            	**type**\:  bool
                            
                            .. attribute:: status_str
                            
                            	Error str, if there are any errors resolving the sensor path
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'telemetry-model-driven-oper'
                            _revision = '2017-05-05'

                            def __init__(self):
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath, self).__init__()

                                self.yang_name = "sensor-path"
                                self.yang_parent_name = "sensor-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.path = YLeaf(YType.str, "path")

                                self.state = YLeaf(YType.boolean, "state")

                                self.status_str = YLeaf(YType.str, "status-str")
                                self._segment_path = lambda: "sensor-path"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath, ['path', 'state', 'status_str'], name, value)


                class SourceInterface(Entity):
                    """
                    configured source interface
                    
                    .. attribute:: interface_name
                    
                    	Source Interface Name
                    	**type**\:  str
                    
                    .. attribute:: ipv4_address
                    
                    	IPV4 Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6 Address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: state
                    
                    	interface state
                    	**type**\:  bool
                    
                    .. attribute:: vrf_id
                    
                    	Src Vrf Id
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-05-05'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface, self).__init__()

                        self.yang_name = "source-interface"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        self.state = YLeaf(YType.boolean, "state")

                        self.vrf_id = YLeaf(YType.uint32, "vrf-id")
                        self._segment_path = lambda: "source-interface"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface, ['interface_name', 'ipv4_address', 'ipv6_address', 'state', 'vrf_id'], name, value)

    def clone_ptr(self):
        self._top_entity = TelemetryModelDriven()
        return self._top_entity

