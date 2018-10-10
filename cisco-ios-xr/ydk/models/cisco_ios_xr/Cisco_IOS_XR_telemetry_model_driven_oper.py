""" Cisco_IOS_XR_telemetry_model_driven_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package operational data.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Telemetry operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MdtDestStateEnum(Enum):
    """
    MdtDestStateEnum (Enum Class)

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
    MdtEncodingEnum (Enum Class)

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
    MdtInternalPathStatus (Enum Class)

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
    MdtIp (Enum Class)

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
    MdtSourceQosMarking (Enum Class)

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
    MdtSubsStateEnum (Enum Class)

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
    MdtTransportEnum (Enum Class)

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
    	**type**\:  :py:class:`Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations>`
    
    .. attribute:: subscriptions
    
    	Telemetry Subscriptions
    	**type**\:  :py:class:`Subscriptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions>`
    
    .. attribute:: sensor_groups
    
    	Telemetry Sensor Groups
    	**type**\:  :py:class:`SensorGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups>`
    
    .. attribute:: summary
    
    	Telemetry Summary info
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Summary>`
    
    

    """

    _prefix = 'telemetry-model-driven-oper'
    _revision = '2017-09-27'

    def __init__(self):
        super(TelemetryModelDriven, self).__init__()
        self._top_entity = None

        self.yang_name = "telemetry-model-driven"
        self.yang_parent_name = "Cisco-IOS-XR-telemetry-model-driven-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("destinations", ("destinations", TelemetryModelDriven.Destinations)), ("subscriptions", ("subscriptions", TelemetryModelDriven.Subscriptions)), ("sensor-groups", ("sensor_groups", TelemetryModelDriven.SensorGroups)), ("summary", ("summary", TelemetryModelDriven.Summary))])
        self._leafs = OrderedDict()

        self.destinations = TelemetryModelDriven.Destinations()
        self.destinations.parent = self
        self._children_name_map["destinations"] = "destinations"

        self.subscriptions = TelemetryModelDriven.Subscriptions()
        self.subscriptions.parent = self
        self._children_name_map["subscriptions"] = "subscriptions"

        self.sensor_groups = TelemetryModelDriven.SensorGroups()
        self.sensor_groups.parent = self
        self._children_name_map["sensor_groups"] = "sensor-groups"

        self.summary = TelemetryModelDriven.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._segment_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TelemetryModelDriven, [], name, value)


    class Destinations(Entity):
        """
        Telemetry Destinations
        
        .. attribute:: destination
        
        	Telemetry Destination
        	**type**\: list of  		 :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-09-27'

        def __init__(self):
            super(TelemetryModelDriven.Destinations, self).__init__()

            self.yang_name = "destinations"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("destination", ("destination", TelemetryModelDriven.Destinations.Destination))])
            self._leafs = OrderedDict()

            self.destination = YList(self)
            self._segment_path = lambda: "destinations"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Destinations, [], name, value)


        class Destination(Entity):
            """
            Telemetry Destination
            
            .. attribute:: destination_id  (key)
            
            	Id of the destination
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: id
            
            	Destination Group name
            	**type**\: str
            
            .. attribute:: configured
            
            	Set if this is configured destination group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: destination
            
            	list of destinations defined in this group
            	**type**\: list of  		 :py:class:`Destination_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_>`
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2017-09-27'

            def __init__(self):
                super(TelemetryModelDriven.Destinations.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "destinations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['destination_id']
                self._child_classes = OrderedDict([("destination", ("destination", TelemetryModelDriven.Destinations.Destination.Destination_))])
                self._leafs = OrderedDict([
                    ('destination_id', (YLeaf(YType.str, 'destination-id'), ['str'])),
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ('configured', (YLeaf(YType.uint32, 'configured'), ['int'])),
                ])
                self.destination_id = None
                self.id = None
                self.configured = None

                self.destination = YList(self)
                self._segment_path = lambda: "destination" + "[destination-id='" + str(self.destination_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/destinations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.Destinations.Destination, ['destination_id', u'id', u'configured'], name, value)


            class Destination_(Entity):
                """
                list of destinations defined in this group
                
                .. attribute:: destination
                
                	Destination
                	**type**\:  :py:class:`Destination_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.Destination_>`
                
                .. attribute:: collection_group
                
                	List of collection groups for this destination group
                	**type**\: list of  		 :py:class:`CollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup>`
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-09-27'

                def __init__(self):
                    super(TelemetryModelDriven.Destinations.Destination.Destination_, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "destination"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("destination", ("destination", TelemetryModelDriven.Destinations.Destination.Destination_.Destination_)), ("collection-group", ("collection_group", TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup))])
                    self._leafs = OrderedDict()

                    self.destination = TelemetryModelDriven.Destinations.Destination.Destination_.Destination_()
                    self.destination.parent = self
                    self._children_name_map["destination"] = "destination"

                    self.collection_group = YList(self)
                    self._segment_path = lambda: "destination"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination_, [], name, value)


                class Destination_(Entity):
                    """
                    Destination
                    
                    .. attribute:: dest_ip_address
                    
                    	Destination IP Address
                    	**type**\:  :py:class:`DestIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.Destination_.DestIpAddress>`
                    
                    .. attribute:: id
                    
                    	Destination Id
                    	**type**\: str
                    
                    .. attribute:: sub_id_str
                    
                    	Sub Idstr
                    	**type**\: str
                    
                    .. attribute:: dest_port
                    
                    	Destination Port number
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: encoding
                    
                    	Destination group encoding
                    	**type**\:  :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                    
                    .. attribute:: transport
                    
                    	Destination group transport
                    	**type**\:  :py:class:`MdtTransportEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtTransportEnum>`
                    
                    .. attribute:: vrf
                    
                    	Destination group vrf
                    	**type**\: str
                    
                    .. attribute:: vrf_id
                    
                    	Destination group vrf id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	State of streaming on this destination
                    	**type**\:  :py:class:`MdtDestStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtDestStateEnum>`
                    
                    .. attribute:: udp_mtu
                    
                    	UDP MTU if this destination is UDP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tls
                    
                    	TLS connection to this destination
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tls_host
                    
                    	TLS Hostname of this destination
                    	**type**\: str
                    
                    .. attribute:: total_num_of_packets_sent
                    
                    	Total number of packets sent for this destination
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_num_of_bytes_sent
                    
                    	Total number of bytes sent for this destination
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: last_collection_time
                    
                    	Timestamp of the last collection
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dscp
                    
                    	DSCP setting for this destination
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sub_id
                    
                    	Sub Id
                    	**type**\: list of int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Destinations.Destination.Destination_.Destination_, self).__init__()

                        self.yang_name = "destination"
                        self.yang_parent_name = "destination"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("dest-ip-address", ("dest_ip_address", TelemetryModelDriven.Destinations.Destination.Destination_.Destination_.DestIpAddress))])
                        self._leafs = OrderedDict([
                            ('id', (YLeaf(YType.str, 'id'), ['str'])),
                            ('sub_id_str', (YLeaf(YType.str, 'sub-id-str'), ['str'])),
                            ('dest_port', (YLeaf(YType.uint16, 'dest-port'), ['int'])),
                            ('encoding', (YLeaf(YType.enumeration, 'encoding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnum', '')])),
                            ('transport', (YLeaf(YType.enumeration, 'transport'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtTransportEnum', '')])),
                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtDestStateEnum', '')])),
                            ('udp_mtu', (YLeaf(YType.uint32, 'udp-mtu'), ['int'])),
                            ('tls', (YLeaf(YType.uint32, 'tls'), ['int'])),
                            ('tls_host', (YLeaf(YType.str, 'tls-host'), ['str'])),
                            ('total_num_of_packets_sent', (YLeaf(YType.uint64, 'total-num-of-packets-sent'), ['int'])),
                            ('total_num_of_bytes_sent', (YLeaf(YType.uint64, 'total-num-of-bytes-sent'), ['int'])),
                            ('last_collection_time', (YLeaf(YType.uint64, 'last-collection-time'), ['int'])),
                            ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
                            ('sub_id', (YLeafList(YType.uint64, 'sub-id'), ['int'])),
                        ])
                        self.id = None
                        self.sub_id_str = None
                        self.dest_port = None
                        self.encoding = None
                        self.transport = None
                        self.vrf = None
                        self.vrf_id = None
                        self.state = None
                        self.udp_mtu = None
                        self.tls = None
                        self.tls_host = None
                        self.total_num_of_packets_sent = None
                        self.total_num_of_bytes_sent = None
                        self.last_collection_time = None
                        self.dscp = None
                        self.sub_id = []

                        self.dest_ip_address = TelemetryModelDriven.Destinations.Destination.Destination_.Destination_.DestIpAddress()
                        self.dest_ip_address.parent = self
                        self._children_name_map["dest_ip_address"] = "dest-ip-address"
                        self._segment_path = lambda: "destination"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination_.Destination_, [u'id', u'sub_id_str', u'dest_port', u'encoding', u'transport', u'vrf', u'vrf_id', u'state', u'udp_mtu', u'tls', u'tls_host', u'total_num_of_packets_sent', u'total_num_of_bytes_sent', u'last_collection_time', u'dscp', u'sub_id'], name, value)


                    class DestIpAddress(Entity):
                        """
                        Destination IP Address
                        
                        .. attribute:: ip_type
                        
                        	IPType
                        	**type**\:  :py:class:`MdtIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtIp>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPV4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPV6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-09-27'

                        def __init__(self):
                            super(TelemetryModelDriven.Destinations.Destination.Destination_.Destination_.DestIpAddress, self).__init__()

                            self.yang_name = "dest-ip-address"
                            self.yang_parent_name = "destination"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ip_type', (YLeaf(YType.enumeration, 'ip-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtIp', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.ip_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "dest-ip-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination_.Destination_.DestIpAddress, [u'ip_type', u'ipv4_address', u'ipv6_address'], name, value)


                class CollectionGroup(Entity):
                    """
                    List of collection groups for this destination
                    group
                    
                    .. attribute:: id
                    
                    	Collection Group id
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: cadence
                    
                    	Period of the collections (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_collections
                    
                    	Completed collections count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: encoding
                    
                    	Destination group encoding
                    	**type**\:  :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                    
                    .. attribute:: last_collection_start_time
                    
                    	Timestamp of the start of last collection
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_collection_end_time
                    
                    	Timestamp of the end of last collection
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_collection_time
                    
                    	Maximum time for a collection (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_collection_time
                    
                    	Minimum time for a collection (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_total_time
                    
                    	Minimum time for all processing (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_total_time
                    
                    	Maximum time for all processing (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: avg_total_time
                    
                    	Average time for all processing (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_other_errors
                    
                    	Total number of errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_on_data_instances
                    
                    	Total number of no data instances
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_not_ready
                    
                    	Total number skipped (not ready)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_send_errors
                    
                    	Total number of send errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_send_drops
                    
                    	Total number of send drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: strict_timer
                    
                    	Set if strict timer is ON
                    	**type**\: bool
                    
                    .. attribute:: collection_path
                    
                    	Array of information for sensor paths within collection group
                    	**type**\: list of  		 :py:class:`CollectionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath>`
                    
                    .. attribute:: internal_collection_group
                    
                    	Array of information for sysdb paths within collection group
                    	**type**\: list of  		 :py:class:`InternalCollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup>`
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup, self).__init__()

                        self.yang_name = "collection-group"
                        self.yang_parent_name = "destination"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("collection-path", ("collection_path", TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath)), ("internal-collection-group", ("internal_collection_group", TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup))])
                        self._leafs = OrderedDict([
                            ('id', (YLeaf(YType.uint64, 'id'), ['int'])),
                            ('cadence', (YLeaf(YType.uint32, 'cadence'), ['int'])),
                            ('total_collections', (YLeaf(YType.uint32, 'total-collections'), ['int'])),
                            ('encoding', (YLeaf(YType.enumeration, 'encoding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnum', '')])),
                            ('last_collection_start_time', (YLeaf(YType.uint64, 'last-collection-start-time'), ['int'])),
                            ('last_collection_end_time', (YLeaf(YType.uint64, 'last-collection-end-time'), ['int'])),
                            ('max_collection_time', (YLeaf(YType.uint32, 'max-collection-time'), ['int'])),
                            ('min_collection_time', (YLeaf(YType.uint32, 'min-collection-time'), ['int'])),
                            ('min_total_time', (YLeaf(YType.uint32, 'min-total-time'), ['int'])),
                            ('max_total_time', (YLeaf(YType.uint32, 'max-total-time'), ['int'])),
                            ('avg_total_time', (YLeaf(YType.uint32, 'avg-total-time'), ['int'])),
                            ('total_other_errors', (YLeaf(YType.uint32, 'total-other-errors'), ['int'])),
                            ('total_on_data_instances', (YLeaf(YType.uint32, 'total-on-data-instances'), ['int'])),
                            ('total_not_ready', (YLeaf(YType.uint32, 'total-not-ready'), ['int'])),
                            ('total_send_errors', (YLeaf(YType.uint32, 'total-send-errors'), ['int'])),
                            ('total_send_drops', (YLeaf(YType.uint32, 'total-send-drops'), ['int'])),
                            ('strict_timer', (YLeaf(YType.boolean, 'strict-timer'), ['bool'])),
                        ])
                        self.id = None
                        self.cadence = None
                        self.total_collections = None
                        self.encoding = None
                        self.last_collection_start_time = None
                        self.last_collection_end_time = None
                        self.max_collection_time = None
                        self.min_collection_time = None
                        self.min_total_time = None
                        self.max_total_time = None
                        self.avg_total_time = None
                        self.total_other_errors = None
                        self.total_on_data_instances = None
                        self.total_not_ready = None
                        self.total_send_errors = None
                        self.total_send_drops = None
                        self.strict_timer = None

                        self.collection_path = YList(self)
                        self.internal_collection_group = YList(self)
                        self._segment_path = lambda: "collection-group"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup, [u'id', u'cadence', u'total_collections', u'encoding', u'last_collection_start_time', u'last_collection_end_time', u'max_collection_time', u'min_collection_time', u'min_total_time', u'max_total_time', u'avg_total_time', u'total_other_errors', u'total_on_data_instances', u'total_not_ready', u'total_send_errors', u'total_send_drops', u'strict_timer'], name, value)


                    class CollectionPath(Entity):
                        """
                        Array of information for sensor paths within
                        collection group
                        
                        .. attribute:: path
                        
                        	Sensor Path
                        	**type**\: str
                        
                        .. attribute:: state
                        
                        	State, if sensor path is resolved or not
                        	**type**\: bool
                        
                        .. attribute:: status_str
                        
                        	Error str, if there are any errors resolving the sensor path
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-09-27'

                        def __init__(self):
                            super(TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath, self).__init__()

                            self.yang_name = "collection-path"
                            self.yang_parent_name = "collection-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                ('state', (YLeaf(YType.boolean, 'state'), ['bool'])),
                                ('status_str', (YLeaf(YType.str, 'status-str'), ['str'])),
                            ])
                            self.path = None
                            self.state = None
                            self.status_str = None
                            self._segment_path = lambda: "collection-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath, [u'path', u'state', u'status_str'], name, value)


                    class InternalCollectionGroup(Entity):
                        """
                        Array of information for sysdb paths within
                        collection group
                        
                        .. attribute:: path
                        
                        	Sysdb Path
                        	**type**\: str
                        
                        .. attribute:: cadence
                        
                        	Period of the collections (ms)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_count
                        
                        	Total number of gets
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_list_count
                        
                        	Total number of lists
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_datalist_count
                        
                        	Total number of datalists
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_finddata_count
                        
                        	Total number of finddata
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_bulk_count
                        
                        	Total number of get bulk
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_item_count
                        
                        	Total number of items retrived from sysdb
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_errors
                        
                        	Total number of get errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_list_errors
                        
                        	Total number of list errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_datalist_errors
                        
                        	Total number of datalist errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_finddata_errors
                        
                        	Total number of finddata errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_get_bulk_errors
                        
                        	Total number of get bulk errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_encode_errors
                        
                        	Total number of encode errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_encode_notready
                        
                        	Total number of encode deferred
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_send_errors
                        
                        	Total number of send errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_send_drops
                        
                        	Total number of send channel full
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_sent_bytes
                        
                        	Total number of bytes sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: total_send_packets
                        
                        	Total number of packets sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_send_bytes_dropped
                        
                        	Total number of send bytes dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: total_collections
                        
                        	Completed collections count
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_collections_missed
                        
                        	Total number of collections missed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: max_collection_time
                        
                        	Maximum time for a collection (ms)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: min_collection_time
                        
                        	Minimum time for a collection (ms)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: avg_collection_time
                        
                        	Average time for a collection (ms)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: collection_method
                        
                        	Collection method in use
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: status
                        
                        	Status of collection path
                        	**type**\:  :py:class:`MdtInternalPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtInternalPathStatus>`
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-09-27'

                        def __init__(self):
                            super(TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup, self).__init__()

                            self.yang_name = "internal-collection-group"
                            self.yang_parent_name = "collection-group"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                ('cadence', (YLeaf(YType.uint64, 'cadence'), ['int'])),
                                ('total_get_count', (YLeaf(YType.uint64, 'total-get-count'), ['int'])),
                                ('total_list_count', (YLeaf(YType.uint64, 'total-list-count'), ['int'])),
                                ('total_datalist_count', (YLeaf(YType.uint64, 'total-datalist-count'), ['int'])),
                                ('total_finddata_count', (YLeaf(YType.uint64, 'total-finddata-count'), ['int'])),
                                ('total_get_bulk_count', (YLeaf(YType.uint64, 'total-get-bulk-count'), ['int'])),
                                ('total_item_count', (YLeaf(YType.uint64, 'total-item-count'), ['int'])),
                                ('total_get_errors', (YLeaf(YType.uint64, 'total-get-errors'), ['int'])),
                                ('total_list_errors', (YLeaf(YType.uint64, 'total-list-errors'), ['int'])),
                                ('total_datalist_errors', (YLeaf(YType.uint64, 'total-datalist-errors'), ['int'])),
                                ('total_finddata_errors', (YLeaf(YType.uint64, 'total-finddata-errors'), ['int'])),
                                ('total_get_bulk_errors', (YLeaf(YType.uint64, 'total-get-bulk-errors'), ['int'])),
                                ('total_encode_errors', (YLeaf(YType.uint64, 'total-encode-errors'), ['int'])),
                                ('total_encode_notready', (YLeaf(YType.uint64, 'total-encode-notready'), ['int'])),
                                ('total_send_errors', (YLeaf(YType.uint64, 'total-send-errors'), ['int'])),
                                ('total_send_drops', (YLeaf(YType.uint64, 'total-send-drops'), ['int'])),
                                ('total_sent_bytes', (YLeaf(YType.uint64, 'total-sent-bytes'), ['int'])),
                                ('total_send_packets', (YLeaf(YType.uint64, 'total-send-packets'), ['int'])),
                                ('total_send_bytes_dropped', (YLeaf(YType.uint64, 'total-send-bytes-dropped'), ['int'])),
                                ('total_collections', (YLeaf(YType.uint64, 'total-collections'), ['int'])),
                                ('total_collections_missed', (YLeaf(YType.uint64, 'total-collections-missed'), ['int'])),
                                ('max_collection_time', (YLeaf(YType.uint64, 'max-collection-time'), ['int'])),
                                ('min_collection_time', (YLeaf(YType.uint64, 'min-collection-time'), ['int'])),
                                ('avg_collection_time', (YLeaf(YType.uint64, 'avg-collection-time'), ['int'])),
                                ('collection_method', (YLeaf(YType.uint64, 'collection-method'), ['int'])),
                                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtInternalPathStatus', '')])),
                            ])
                            self.path = None
                            self.cadence = None
                            self.total_get_count = None
                            self.total_list_count = None
                            self.total_datalist_count = None
                            self.total_finddata_count = None
                            self.total_get_bulk_count = None
                            self.total_item_count = None
                            self.total_get_errors = None
                            self.total_list_errors = None
                            self.total_datalist_errors = None
                            self.total_finddata_errors = None
                            self.total_get_bulk_errors = None
                            self.total_encode_errors = None
                            self.total_encode_notready = None
                            self.total_send_errors = None
                            self.total_send_drops = None
                            self.total_sent_bytes = None
                            self.total_send_packets = None
                            self.total_send_bytes_dropped = None
                            self.total_collections = None
                            self.total_collections_missed = None
                            self.max_collection_time = None
                            self.min_collection_time = None
                            self.avg_collection_time = None
                            self.collection_method = None
                            self.status = None
                            self._segment_path = lambda: "internal-collection-group"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup, [u'path', u'cadence', u'total_get_count', u'total_list_count', u'total_datalist_count', u'total_finddata_count', u'total_get_bulk_count', u'total_item_count', u'total_get_errors', u'total_list_errors', u'total_datalist_errors', u'total_finddata_errors', u'total_get_bulk_errors', u'total_encode_errors', u'total_encode_notready', u'total_send_errors', u'total_send_drops', u'total_sent_bytes', u'total_send_packets', u'total_send_bytes_dropped', u'total_collections', u'total_collections_missed', u'max_collection_time', u'min_collection_time', u'avg_collection_time', u'collection_method', u'status'], name, value)


    class Subscriptions(Entity):
        """
        Telemetry Subscriptions
        
        .. attribute:: subscription
        
        	Telemetry Subscription
        	**type**\: list of  		 :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-09-27'

        def __init__(self):
            super(TelemetryModelDriven.Subscriptions, self).__init__()

            self.yang_name = "subscriptions"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("subscription", ("subscription", TelemetryModelDriven.Subscriptions.Subscription))])
            self._leafs = OrderedDict()

            self.subscription = YList(self)
            self._segment_path = lambda: "subscriptions"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Subscriptions, [], name, value)


        class Subscription(Entity):
            """
            Telemetry Subscription
            
            .. attribute:: subscription_id  (key)
            
            	Id of the subscription
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: subscription
            
            	Subscription
            	**type**\:  :py:class:`Subscription_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_>`
            
            .. attribute:: collection_group
            
            	List of collection groups active for this subscription
            	**type**\: list of  		 :py:class:`CollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup>`
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2017-09-27'

            def __init__(self):
                super(TelemetryModelDriven.Subscriptions.Subscription, self).__init__()

                self.yang_name = "subscription"
                self.yang_parent_name = "subscriptions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['subscription_id']
                self._child_classes = OrderedDict([("subscription", ("subscription", TelemetryModelDriven.Subscriptions.Subscription.Subscription_)), ("collection-group", ("collection_group", TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup))])
                self._leafs = OrderedDict([
                    ('subscription_id', (YLeaf(YType.str, 'subscription-id'), ['str'])),
                ])
                self.subscription_id = None

                self.subscription = TelemetryModelDriven.Subscriptions.Subscription.Subscription_()
                self.subscription.parent = self
                self._children_name_map["subscription"] = "subscription"

                self.collection_group = YList(self)
                self._segment_path = lambda: "subscription" + "[subscription-id='" + str(self.subscription_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/subscriptions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription, ['subscription_id'], name, value)


            class Subscription_(Entity):
                """
                Subscription
                
                .. attribute:: source_interface
                
                	configured source interface
                	**type**\:  :py:class:`SourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SourceInterface>`
                
                .. attribute:: id
                
                	Collection Subscription name
                	**type**\: str
                
                .. attribute:: state
                
                	Subscription state
                	**type**\:  :py:class:`MdtSubsStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtSubsStateEnum>`
                
                .. attribute:: source_qos_marking
                
                	DSCP
                	**type**\:  :py:class:`MdtSourceQosMarking <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtSourceQosMarking>`
                
                .. attribute:: sensor_profile
                
                	List of sensor groups within a subscription
                	**type**\: list of  		 :py:class:`SensorProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile>`
                
                .. attribute:: destination_grp
                
                	Array of destinations within a subscription
                	**type**\: list of  		 :py:class:`DestinationGrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp>`
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-09-27'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_, self).__init__()

                    self.yang_name = "subscription"
                    self.yang_parent_name = "subscription"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("source-interface", ("source_interface", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SourceInterface)), ("sensor-profile", ("sensor_profile", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile)), ("destination-grp", ("destination_grp", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp))])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.str, 'id'), ['str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtSubsStateEnum', '')])),
                        ('source_qos_marking', (YLeaf(YType.enumeration, 'source-qos-marking'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtSourceQosMarking', '')])),
                    ])
                    self.id = None
                    self.state = None
                    self.source_qos_marking = None

                    self.source_interface = TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SourceInterface()
                    self.source_interface.parent = self
                    self._children_name_map["source_interface"] = "source-interface"

                    self.sensor_profile = YList(self)
                    self.destination_grp = YList(self)
                    self._segment_path = lambda: "subscription"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_, [u'id', u'state', u'source_qos_marking'], name, value)


                class SourceInterface(Entity):
                    """
                    configured source interface
                    
                    .. attribute:: interface_name
                    
                    	Source Interface Name
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	interface state
                    	**type**\: bool
                    
                    .. attribute:: ipv4_address
                    
                    	IPV4 Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_address
                    
                    	IPV6 Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: vrf_id
                    
                    	Src Vrf Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SourceInterface, self).__init__()

                        self.yang_name = "source-interface"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('state', (YLeaf(YType.boolean, 'state'), ['bool'])),
                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                        ])
                        self.interface_name = None
                        self.state = None
                        self.ipv4_address = None
                        self.ipv6_address = None
                        self.vrf_id = None
                        self._segment_path = lambda: "source-interface"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SourceInterface, [u'interface_name', u'state', u'ipv4_address', u'ipv6_address', u'vrf_id'], name, value)


                class SensorProfile(Entity):
                    """
                    List of sensor groups within a subscription
                    
                    .. attribute:: sensor_group
                    
                    	sensor group
                    	**type**\:  :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup>`
                    
                    .. attribute:: sample_interval
                    
                    	Sample interval for the sensor group (ms)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: heartbeat_interval
                    
                    	Heartbeat interval for the sensor group (s)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: suppress_redundant
                    
                    	Suppress Redundant
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile, self).__init__()

                        self.yang_name = "sensor-profile"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sensor-group", ("sensor_group", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup))])
                        self._leafs = OrderedDict([
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('heartbeat_interval', (YLeaf(YType.uint32, 'heartbeat-interval'), ['int'])),
                            ('suppress_redundant', (YLeaf(YType.boolean, 'suppress-redundant'), ['bool'])),
                        ])
                        self.sample_interval = None
                        self.heartbeat_interval = None
                        self.suppress_redundant = None

                        self.sensor_group = TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup()
                        self.sensor_group.parent = self
                        self._children_name_map["sensor_group"] = "sensor-group"
                        self._segment_path = lambda: "sensor-profile"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile, [u'sample_interval', u'heartbeat_interval', u'suppress_redundant'], name, value)


                    class SensorGroup(Entity):
                        """
                        sensor group
                        
                        .. attribute:: id
                        
                        	Sensor Group name
                        	**type**\: str
                        
                        .. attribute:: configured
                        
                        	Set if this is configured sensor group
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sensor_path
                        
                        	Array of information for sensor paths within sensor group
                        	**type**\: list of  		 :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath>`
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-09-27'

                        def __init__(self):
                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup, self).__init__()

                            self.yang_name = "sensor-group"
                            self.yang_parent_name = "sensor-profile"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sensor-path", ("sensor_path", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath))])
                            self._leafs = OrderedDict([
                                ('id', (YLeaf(YType.str, 'id'), ['str'])),
                                ('configured', (YLeaf(YType.uint32, 'configured'), ['int'])),
                            ])
                            self.id = None
                            self.configured = None

                            self.sensor_path = YList(self)
                            self._segment_path = lambda: "sensor-group"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup, [u'id', u'configured'], name, value)


                        class SensorPath(Entity):
                            """
                            Array of information for sensor paths within
                            sensor group
                            
                            .. attribute:: path
                            
                            	Sensor Path
                            	**type**\: str
                            
                            .. attribute:: state
                            
                            	State, if sensor path is resolved or not
                            	**type**\: bool
                            
                            .. attribute:: status_str
                            
                            	Error str, if there are any errors resolving the sensor path
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'telemetry-model-driven-oper'
                            _revision = '2017-09-27'

                            def __init__(self):
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath, self).__init__()

                                self.yang_name = "sensor-path"
                                self.yang_parent_name = "sensor-group"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path', (YLeaf(YType.str, 'path'), ['str'])),
                                    ('state', (YLeaf(YType.boolean, 'state'), ['bool'])),
                                    ('status_str', (YLeaf(YType.str, 'status-str'), ['str'])),
                                ])
                                self.path = None
                                self.state = None
                                self.status_str = None
                                self._segment_path = lambda: "sensor-path"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath, [u'path', u'state', u'status_str'], name, value)


                class DestinationGrp(Entity):
                    """
                    Array of destinations within a subscription
                    
                    .. attribute:: id
                    
                    	Destination Group name
                    	**type**\: str
                    
                    .. attribute:: configured
                    
                    	Set if this is configured destination group
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination
                    
                    	list of destinations defined in this group
                    	**type**\: list of  		 :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination>`
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp, self).__init__()

                        self.yang_name = "destination-grp"
                        self.yang_parent_name = "subscription"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("destination", ("destination", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination))])
                        self._leafs = OrderedDict([
                            ('id', (YLeaf(YType.str, 'id'), ['str'])),
                            ('configured', (YLeaf(YType.uint32, 'configured'), ['int'])),
                        ])
                        self.id = None
                        self.configured = None

                        self.destination = YList(self)
                        self._segment_path = lambda: "destination-grp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp, [u'id', u'configured'], name, value)


                    class Destination(Entity):
                        """
                        list of destinations defined in this group
                        
                        .. attribute:: dest_ip_address
                        
                        	Destination IP Address
                        	**type**\:  :py:class:`DestIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress>`
                        
                        .. attribute:: id
                        
                        	Destination Id
                        	**type**\: str
                        
                        .. attribute:: sub_id_str
                        
                        	Sub Idstr
                        	**type**\: str
                        
                        .. attribute:: dest_port
                        
                        	Destination Port number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: encoding
                        
                        	Destination group encoding
                        	**type**\:  :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                        
                        .. attribute:: transport
                        
                        	Destination group transport
                        	**type**\:  :py:class:`MdtTransportEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtTransportEnum>`
                        
                        .. attribute:: vrf
                        
                        	Destination group vrf
                        	**type**\: str
                        
                        .. attribute:: vrf_id
                        
                        	Destination group vrf id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state
                        
                        	State of streaming on this destination
                        	**type**\:  :py:class:`MdtDestStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtDestStateEnum>`
                        
                        .. attribute:: udp_mtu
                        
                        	UDP MTU if this destination is UDP
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tls
                        
                        	TLS connection to this destination
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tls_host
                        
                        	TLS Hostname of this destination
                        	**type**\: str
                        
                        .. attribute:: total_num_of_packets_sent
                        
                        	Total number of packets sent for this destination
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_num_of_bytes_sent
                        
                        	Total number of bytes sent for this destination
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: last_collection_time
                        
                        	Timestamp of the last collection
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dscp
                        
                        	DSCP setting for this destination
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sub_id
                        
                        	Sub Id
                        	**type**\: list of int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2017-09-27'

                        def __init__(self):
                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination, self).__init__()

                            self.yang_name = "destination"
                            self.yang_parent_name = "destination-grp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("dest-ip-address", ("dest_ip_address", TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress))])
                            self._leafs = OrderedDict([
                                ('id', (YLeaf(YType.str, 'id'), ['str'])),
                                ('sub_id_str', (YLeaf(YType.str, 'sub-id-str'), ['str'])),
                                ('dest_port', (YLeaf(YType.uint16, 'dest-port'), ['int'])),
                                ('encoding', (YLeaf(YType.enumeration, 'encoding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnum', '')])),
                                ('transport', (YLeaf(YType.enumeration, 'transport'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtTransportEnum', '')])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtDestStateEnum', '')])),
                                ('udp_mtu', (YLeaf(YType.uint32, 'udp-mtu'), ['int'])),
                                ('tls', (YLeaf(YType.uint32, 'tls'), ['int'])),
                                ('tls_host', (YLeaf(YType.str, 'tls-host'), ['str'])),
                                ('total_num_of_packets_sent', (YLeaf(YType.uint64, 'total-num-of-packets-sent'), ['int'])),
                                ('total_num_of_bytes_sent', (YLeaf(YType.uint64, 'total-num-of-bytes-sent'), ['int'])),
                                ('last_collection_time', (YLeaf(YType.uint64, 'last-collection-time'), ['int'])),
                                ('dscp', (YLeaf(YType.uint32, 'dscp'), ['int'])),
                                ('sub_id', (YLeafList(YType.uint64, 'sub-id'), ['int'])),
                            ])
                            self.id = None
                            self.sub_id_str = None
                            self.dest_port = None
                            self.encoding = None
                            self.transport = None
                            self.vrf = None
                            self.vrf_id = None
                            self.state = None
                            self.udp_mtu = None
                            self.tls = None
                            self.tls_host = None
                            self.total_num_of_packets_sent = None
                            self.total_num_of_bytes_sent = None
                            self.last_collection_time = None
                            self.dscp = None
                            self.sub_id = []

                            self.dest_ip_address = TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress()
                            self.dest_ip_address.parent = self
                            self._children_name_map["dest_ip_address"] = "dest-ip-address"
                            self._segment_path = lambda: "destination"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination, [u'id', u'sub_id_str', u'dest_port', u'encoding', u'transport', u'vrf', u'vrf_id', u'state', u'udp_mtu', u'tls', u'tls_host', u'total_num_of_packets_sent', u'total_num_of_bytes_sent', u'last_collection_time', u'dscp', u'sub_id'], name, value)


                        class DestIpAddress(Entity):
                            """
                            Destination IP Address
                            
                            .. attribute:: ip_type
                            
                            	IPType
                            	**type**\:  :py:class:`MdtIp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtIp>`
                            
                            .. attribute:: ipv4_address
                            
                            	IPV4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_address
                            
                            	IPV6 Address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'telemetry-model-driven-oper'
                            _revision = '2017-09-27'

                            def __init__(self):
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress, self).__init__()

                                self.yang_name = "dest-ip-address"
                                self.yang_parent_name = "destination"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ip_type', (YLeaf(YType.enumeration, 'ip-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtIp', '')])),
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ])
                                self.ip_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self._segment_path = lambda: "dest-ip-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress, [u'ip_type', u'ipv4_address', u'ipv6_address'], name, value)


            class CollectionGroup(Entity):
                """
                List of collection groups active for this
                subscription
                
                .. attribute:: id
                
                	Collection Group id
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: cadence
                
                	Period of the collections (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_collections
                
                	Completed collections count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: encoding
                
                	Destination group encoding
                	**type**\:  :py:class:`MdtEncodingEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnum>`
                
                .. attribute:: last_collection_start_time
                
                	Timestamp of the start of last collection
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: last_collection_end_time
                
                	Timestamp of the end of last collection
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: max_collection_time
                
                	Maximum time for a collection (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_collection_time
                
                	Minimum time for a collection (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: min_total_time
                
                	Minimum time for all processing (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_total_time
                
                	Maximum time for all processing (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: avg_total_time
                
                	Average time for all processing (ms)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_other_errors
                
                	Total number of errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_on_data_instances
                
                	Total number of no data instances
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_not_ready
                
                	Total number skipped (not ready)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_send_errors
                
                	Total number of send errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_send_drops
                
                	Total number of send drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: strict_timer
                
                	Set if strict timer is ON
                	**type**\: bool
                
                .. attribute:: collection_path
                
                	Array of information for sensor paths within collection group
                	**type**\: list of  		 :py:class:`CollectionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath>`
                
                .. attribute:: internal_collection_group
                
                	Array of information for sysdb paths within collection group
                	**type**\: list of  		 :py:class:`InternalCollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup>`
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-09-27'

                def __init__(self):
                    super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup, self).__init__()

                    self.yang_name = "collection-group"
                    self.yang_parent_name = "subscription"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("collection-path", ("collection_path", TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath)), ("internal-collection-group", ("internal_collection_group", TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup))])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.uint64, 'id'), ['int'])),
                        ('cadence', (YLeaf(YType.uint32, 'cadence'), ['int'])),
                        ('total_collections', (YLeaf(YType.uint32, 'total-collections'), ['int'])),
                        ('encoding', (YLeaf(YType.enumeration, 'encoding'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtEncodingEnum', '')])),
                        ('last_collection_start_time', (YLeaf(YType.uint64, 'last-collection-start-time'), ['int'])),
                        ('last_collection_end_time', (YLeaf(YType.uint64, 'last-collection-end-time'), ['int'])),
                        ('max_collection_time', (YLeaf(YType.uint32, 'max-collection-time'), ['int'])),
                        ('min_collection_time', (YLeaf(YType.uint32, 'min-collection-time'), ['int'])),
                        ('min_total_time', (YLeaf(YType.uint32, 'min-total-time'), ['int'])),
                        ('max_total_time', (YLeaf(YType.uint32, 'max-total-time'), ['int'])),
                        ('avg_total_time', (YLeaf(YType.uint32, 'avg-total-time'), ['int'])),
                        ('total_other_errors', (YLeaf(YType.uint32, 'total-other-errors'), ['int'])),
                        ('total_on_data_instances', (YLeaf(YType.uint32, 'total-on-data-instances'), ['int'])),
                        ('total_not_ready', (YLeaf(YType.uint32, 'total-not-ready'), ['int'])),
                        ('total_send_errors', (YLeaf(YType.uint32, 'total-send-errors'), ['int'])),
                        ('total_send_drops', (YLeaf(YType.uint32, 'total-send-drops'), ['int'])),
                        ('strict_timer', (YLeaf(YType.boolean, 'strict-timer'), ['bool'])),
                    ])
                    self.id = None
                    self.cadence = None
                    self.total_collections = None
                    self.encoding = None
                    self.last_collection_start_time = None
                    self.last_collection_end_time = None
                    self.max_collection_time = None
                    self.min_collection_time = None
                    self.min_total_time = None
                    self.max_total_time = None
                    self.avg_total_time = None
                    self.total_other_errors = None
                    self.total_on_data_instances = None
                    self.total_not_ready = None
                    self.total_send_errors = None
                    self.total_send_drops = None
                    self.strict_timer = None

                    self.collection_path = YList(self)
                    self.internal_collection_group = YList(self)
                    self._segment_path = lambda: "collection-group"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup, [u'id', u'cadence', u'total_collections', u'encoding', u'last_collection_start_time', u'last_collection_end_time', u'max_collection_time', u'min_collection_time', u'min_total_time', u'max_total_time', u'avg_total_time', u'total_other_errors', u'total_on_data_instances', u'total_not_ready', u'total_send_errors', u'total_send_drops', u'strict_timer'], name, value)


                class CollectionPath(Entity):
                    """
                    Array of information for sensor paths within
                    collection group
                    
                    .. attribute:: path
                    
                    	Sensor Path
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	State, if sensor path is resolved or not
                    	**type**\: bool
                    
                    .. attribute:: status_str
                    
                    	Error str, if there are any errors resolving the sensor path
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath, self).__init__()

                        self.yang_name = "collection-path"
                        self.yang_parent_name = "collection-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('path', (YLeaf(YType.str, 'path'), ['str'])),
                            ('state', (YLeaf(YType.boolean, 'state'), ['bool'])),
                            ('status_str', (YLeaf(YType.str, 'status-str'), ['str'])),
                        ])
                        self.path = None
                        self.state = None
                        self.status_str = None
                        self._segment_path = lambda: "collection-path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath, [u'path', u'state', u'status_str'], name, value)


                class InternalCollectionGroup(Entity):
                    """
                    Array of information for sysdb paths within
                    collection group
                    
                    .. attribute:: path
                    
                    	Sysdb Path
                    	**type**\: str
                    
                    .. attribute:: cadence
                    
                    	Period of the collections (ms)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_count
                    
                    	Total number of gets
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_list_count
                    
                    	Total number of lists
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_datalist_count
                    
                    	Total number of datalists
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_finddata_count
                    
                    	Total number of finddata
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_bulk_count
                    
                    	Total number of get bulk
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_item_count
                    
                    	Total number of items retrived from sysdb
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_errors
                    
                    	Total number of get errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_list_errors
                    
                    	Total number of list errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_datalist_errors
                    
                    	Total number of datalist errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_finddata_errors
                    
                    	Total number of finddata errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_get_bulk_errors
                    
                    	Total number of get bulk errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_encode_errors
                    
                    	Total number of encode errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_encode_notready
                    
                    	Total number of encode deferred
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_send_errors
                    
                    	Total number of send errors
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_send_drops
                    
                    	Total number of send channel full
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_sent_bytes
                    
                    	Total number of bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: total_send_packets
                    
                    	Total number of packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_send_bytes_dropped
                    
                    	Total number of send bytes dropped
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: total_collections
                    
                    	Completed collections count
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_collections_missed
                    
                    	Total number of collections missed
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: max_collection_time
                    
                    	Maximum time for a collection (ms)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: min_collection_time
                    
                    	Minimum time for a collection (ms)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: avg_collection_time
                    
                    	Average time for a collection (ms)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: collection_method
                    
                    	Collection method in use
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: status
                    
                    	Status of collection path
                    	**type**\:  :py:class:`MdtInternalPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtInternalPathStatus>`
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2017-09-27'

                    def __init__(self):
                        super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup, self).__init__()

                        self.yang_name = "internal-collection-group"
                        self.yang_parent_name = "collection-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('path', (YLeaf(YType.str, 'path'), ['str'])),
                            ('cadence', (YLeaf(YType.uint64, 'cadence'), ['int'])),
                            ('total_get_count', (YLeaf(YType.uint64, 'total-get-count'), ['int'])),
                            ('total_list_count', (YLeaf(YType.uint64, 'total-list-count'), ['int'])),
                            ('total_datalist_count', (YLeaf(YType.uint64, 'total-datalist-count'), ['int'])),
                            ('total_finddata_count', (YLeaf(YType.uint64, 'total-finddata-count'), ['int'])),
                            ('total_get_bulk_count', (YLeaf(YType.uint64, 'total-get-bulk-count'), ['int'])),
                            ('total_item_count', (YLeaf(YType.uint64, 'total-item-count'), ['int'])),
                            ('total_get_errors', (YLeaf(YType.uint64, 'total-get-errors'), ['int'])),
                            ('total_list_errors', (YLeaf(YType.uint64, 'total-list-errors'), ['int'])),
                            ('total_datalist_errors', (YLeaf(YType.uint64, 'total-datalist-errors'), ['int'])),
                            ('total_finddata_errors', (YLeaf(YType.uint64, 'total-finddata-errors'), ['int'])),
                            ('total_get_bulk_errors', (YLeaf(YType.uint64, 'total-get-bulk-errors'), ['int'])),
                            ('total_encode_errors', (YLeaf(YType.uint64, 'total-encode-errors'), ['int'])),
                            ('total_encode_notready', (YLeaf(YType.uint64, 'total-encode-notready'), ['int'])),
                            ('total_send_errors', (YLeaf(YType.uint64, 'total-send-errors'), ['int'])),
                            ('total_send_drops', (YLeaf(YType.uint64, 'total-send-drops'), ['int'])),
                            ('total_sent_bytes', (YLeaf(YType.uint64, 'total-sent-bytes'), ['int'])),
                            ('total_send_packets', (YLeaf(YType.uint64, 'total-send-packets'), ['int'])),
                            ('total_send_bytes_dropped', (YLeaf(YType.uint64, 'total-send-bytes-dropped'), ['int'])),
                            ('total_collections', (YLeaf(YType.uint64, 'total-collections'), ['int'])),
                            ('total_collections_missed', (YLeaf(YType.uint64, 'total-collections-missed'), ['int'])),
                            ('max_collection_time', (YLeaf(YType.uint64, 'max-collection-time'), ['int'])),
                            ('min_collection_time', (YLeaf(YType.uint64, 'min-collection-time'), ['int'])),
                            ('avg_collection_time', (YLeaf(YType.uint64, 'avg-collection-time'), ['int'])),
                            ('collection_method', (YLeaf(YType.uint64, 'collection-method'), ['int'])),
                            ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper', 'MdtInternalPathStatus', '')])),
                        ])
                        self.path = None
                        self.cadence = None
                        self.total_get_count = None
                        self.total_list_count = None
                        self.total_datalist_count = None
                        self.total_finddata_count = None
                        self.total_get_bulk_count = None
                        self.total_item_count = None
                        self.total_get_errors = None
                        self.total_list_errors = None
                        self.total_datalist_errors = None
                        self.total_finddata_errors = None
                        self.total_get_bulk_errors = None
                        self.total_encode_errors = None
                        self.total_encode_notready = None
                        self.total_send_errors = None
                        self.total_send_drops = None
                        self.total_sent_bytes = None
                        self.total_send_packets = None
                        self.total_send_bytes_dropped = None
                        self.total_collections = None
                        self.total_collections_missed = None
                        self.max_collection_time = None
                        self.min_collection_time = None
                        self.avg_collection_time = None
                        self.collection_method = None
                        self.status = None
                        self._segment_path = lambda: "internal-collection-group"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup, [u'path', u'cadence', u'total_get_count', u'total_list_count', u'total_datalist_count', u'total_finddata_count', u'total_get_bulk_count', u'total_item_count', u'total_get_errors', u'total_list_errors', u'total_datalist_errors', u'total_finddata_errors', u'total_get_bulk_errors', u'total_encode_errors', u'total_encode_notready', u'total_send_errors', u'total_send_drops', u'total_sent_bytes', u'total_send_packets', u'total_send_bytes_dropped', u'total_collections', u'total_collections_missed', u'max_collection_time', u'min_collection_time', u'avg_collection_time', u'collection_method', u'status'], name, value)


    class SensorGroups(Entity):
        """
        Telemetry Sensor Groups
        
        .. attribute:: sensor_group
        
        	Telemetry Sensor Groups
        	**type**\: list of  		 :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-09-27'

        def __init__(self):
            super(TelemetryModelDriven.SensorGroups, self).__init__()

            self.yang_name = "sensor-groups"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("sensor-group", ("sensor_group", TelemetryModelDriven.SensorGroups.SensorGroup))])
            self._leafs = OrderedDict()

            self.sensor_group = YList(self)
            self._segment_path = lambda: "sensor-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.SensorGroups, [], name, value)


        class SensorGroup(Entity):
            """
            Telemetry Sensor Groups
            
            .. attribute:: sensor_group_id  (key)
            
            	Id of the sensor group
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: id
            
            	Sensor Group name
            	**type**\: str
            
            .. attribute:: configured
            
            	Set if this is configured sensor group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sensor_path
            
            	Array of information for sensor paths within sensor group
            	**type**\: list of  		 :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath>`
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2017-09-27'

            def __init__(self):
                super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__init__()

                self.yang_name = "sensor-group"
                self.yang_parent_name = "sensor-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sensor_group_id']
                self._child_classes = OrderedDict([("sensor-path", ("sensor_path", TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath))])
                self._leafs = OrderedDict([
                    ('sensor_group_id', (YLeaf(YType.str, 'sensor-group-id'), ['str'])),
                    ('id', (YLeaf(YType.str, 'id'), ['str'])),
                    ('configured', (YLeaf(YType.uint32, 'configured'), ['int'])),
                ])
                self.sensor_group_id = None
                self.id = None
                self.configured = None

                self.sensor_path = YList(self)
                self._segment_path = lambda: "sensor-group" + "[sensor-group-id='" + str(self.sensor_group_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/sensor-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup, ['sensor_group_id', u'id', u'configured'], name, value)


            class SensorPath(Entity):
                """
                Array of information for sensor paths within
                sensor group
                
                .. attribute:: path
                
                	Sensor Path
                	**type**\: str
                
                .. attribute:: state
                
                	State, if sensor path is resolved or not
                	**type**\: bool
                
                .. attribute:: status_str
                
                	Error str, if there are any errors resolving the sensor path
                	**type**\: str
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2017-09-27'

                def __init__(self):
                    super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath, self).__init__()

                    self.yang_name = "sensor-path"
                    self.yang_parent_name = "sensor-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('path', (YLeaf(YType.str, 'path'), ['str'])),
                        ('state', (YLeaf(YType.boolean, 'state'), ['bool'])),
                        ('status_str', (YLeaf(YType.str, 'status-str'), ['str'])),
                    ])
                    self.path = None
                    self.state = None
                    self.status_str = None
                    self._segment_path = lambda: "sensor-path"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath, [u'path', u'state', u'status_str'], name, value)


    class Summary(Entity):
        """
        Telemetry Summary info
        
        .. attribute:: num_of_subscriptions
        
        	Number of Subscriptions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_active_subscriptions
        
        	Number of Active Subscriptions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_paused_subscriptions
        
        	Number of Paused Subscriptions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_destination_groups
        
        	Number of Destination Groups
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_destinations
        
        	Number of Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_tcp_dialouts
        
        	Number of Tcp Dialout Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_udp_dialouts
        
        	Number of Udp Dialout Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_grpc_tls_dialouts
        
        	Number of GRPC TLS Dialout Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_grpc_non_tls_dialouts
        
        	Number of GRPC Non\-TLS Dialout Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_dialins
        
        	Number of Dialin Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_active_destinations
        
        	Number of Active Destinations
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_connected_sessions
        
        	Number of Connected Sessions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_connecting_sessions
        
        	Number of Connecting Sessions
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_sensor_groups
        
        	Number of Sensor Groups
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_unique_sensor_paths
        
        	Number of Unique Sensor Paths
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_sensor_paths
        
        	Number of Sensor Paths
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_not_resolved_sensor_paths
        
        	Number of not resolved sensor paths
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: num_of_active_sensor_paths
        
        	Number of Active Sensor Paths
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_sensor_paths
        
        	Maximum Sensor Paths allowed
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_containers_per_path
        
        	Max containers allowed per Sensor Path
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2017-09-27'

        def __init__(self):
            super(TelemetryModelDriven.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "telemetry-model-driven"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('num_of_subscriptions', (YLeaf(YType.uint32, 'num-of-subscriptions'), ['int'])),
                ('num_of_active_subscriptions', (YLeaf(YType.uint32, 'num-of-active-subscriptions'), ['int'])),
                ('num_of_paused_subscriptions', (YLeaf(YType.uint32, 'num-of-paused-subscriptions'), ['int'])),
                ('num_of_destination_groups', (YLeaf(YType.uint32, 'num-of-destination-groups'), ['int'])),
                ('num_of_destinations', (YLeaf(YType.uint32, 'num-of-destinations'), ['int'])),
                ('num_of_tcp_dialouts', (YLeaf(YType.uint32, 'num-of-tcp-dialouts'), ['int'])),
                ('num_of_udp_dialouts', (YLeaf(YType.uint32, 'num-of-udp-dialouts'), ['int'])),
                ('num_of_grpc_tls_dialouts', (YLeaf(YType.uint32, 'num-of-grpc-tls-dialouts'), ['int'])),
                ('num_of_grpc_non_tls_dialouts', (YLeaf(YType.uint32, 'num-of-grpc-non-tls-dialouts'), ['int'])),
                ('num_of_dialins', (YLeaf(YType.uint32, 'num-of-dialins'), ['int'])),
                ('num_of_active_destinations', (YLeaf(YType.uint32, 'num-of-active-destinations'), ['int'])),
                ('num_of_connected_sessions', (YLeaf(YType.uint32, 'num-of-connected-sessions'), ['int'])),
                ('num_of_connecting_sessions', (YLeaf(YType.uint32, 'num-of-connecting-sessions'), ['int'])),
                ('num_of_sensor_groups', (YLeaf(YType.uint32, 'num-of-sensor-groups'), ['int'])),
                ('num_of_unique_sensor_paths', (YLeaf(YType.uint32, 'num-of-unique-sensor-paths'), ['int'])),
                ('num_of_sensor_paths', (YLeaf(YType.uint32, 'num-of-sensor-paths'), ['int'])),
                ('num_of_not_resolved_sensor_paths', (YLeaf(YType.uint32, 'num-of-not-resolved-sensor-paths'), ['int'])),
                ('num_of_active_sensor_paths', (YLeaf(YType.uint32, 'num-of-active-sensor-paths'), ['int'])),
                ('max_sensor_paths', (YLeaf(YType.uint32, 'max-sensor-paths'), ['int'])),
                ('max_containers_per_path', (YLeaf(YType.uint32, 'max-containers-per-path'), ['int'])),
            ])
            self.num_of_subscriptions = None
            self.num_of_active_subscriptions = None
            self.num_of_paused_subscriptions = None
            self.num_of_destination_groups = None
            self.num_of_destinations = None
            self.num_of_tcp_dialouts = None
            self.num_of_udp_dialouts = None
            self.num_of_grpc_tls_dialouts = None
            self.num_of_grpc_non_tls_dialouts = None
            self.num_of_dialins = None
            self.num_of_active_destinations = None
            self.num_of_connected_sessions = None
            self.num_of_connecting_sessions = None
            self.num_of_sensor_groups = None
            self.num_of_unique_sensor_paths = None
            self.num_of_sensor_paths = None
            self.num_of_not_resolved_sensor_paths = None
            self.num_of_active_sensor_paths = None
            self.max_sensor_paths = None
            self.max_containers_per_path = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TelemetryModelDriven.Summary, [u'num_of_subscriptions', u'num_of_active_subscriptions', u'num_of_paused_subscriptions', u'num_of_destination_groups', u'num_of_destinations', u'num_of_tcp_dialouts', u'num_of_udp_dialouts', u'num_of_grpc_tls_dialouts', u'num_of_grpc_non_tls_dialouts', u'num_of_dialins', u'num_of_active_destinations', u'num_of_connected_sessions', u'num_of_connecting_sessions', u'num_of_sensor_groups', u'num_of_unique_sensor_paths', u'num_of_sensor_paths', u'num_of_not_resolved_sensor_paths', u'num_of_active_sensor_paths', u'max_sensor_paths', u'max_containers_per_path'], name, value)

    def clone_ptr(self):
        self._top_entity = TelemetryModelDriven()
        return self._top_entity

