""" Cisco_IOS_XR_telemetry_model_driven_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package operational data.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Telemetry operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

    """

    active = Enum.YLeaf(0, "active")

    internal_err = Enum.YLeaf(1, "internal-err")

    plugin_active = Enum.YLeaf(2, "plugin-active")

    plugin_not_initialized = Enum.YLeaf(3, "plugin-not-initialized")

    plugin_invalid_cadence = Enum.YLeaf(4, "plugin-invalid-cadence")

    plugin_err = Enum.YLeaf(5, "plugin-err")

    filter_err = Enum.YLeaf(6, "filter-err")


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

            self.destination = YList(self)

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
                        super(TelemetryModelDriven.Destinations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetryModelDriven.Destinations, self).__setattr__(name, value)


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

                self.destination_id = YLeaf(YType.str, "destination-id")

                self.configured = YLeaf(YType.uint32, "configured")

                self.id = YLeaf(YType.str, "id")

                self.destination = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("destination_id",
                                "configured",
                                "id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetryModelDriven.Destinations.Destination, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetryModelDriven.Destinations.Destination, self).__setattr__(name, value)


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

                    self.destination = TelemetryModelDriven.Destinations.Destination.Destination.Destination()
                    self.destination.parent = self
                    self._children_name_map["destination"] = "destination"
                    self._children_yang_names.add("destination")

                    self.collection_group = YList(self)

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
                                super(TelemetryModelDriven.Destinations.Destination.Destination, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.Destinations.Destination.Destination, self).__setattr__(name, value)


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dest_port",
                                        "dscp",
                                        "encoding",
                                        "id",
                                        "last_collection_time",
                                        "state",
                                        "sub_id",
                                        "sub_id_str",
                                        "tls",
                                        "tls_host",
                                        "total_num_of_bytes_sent",
                                        "total_num_of_packets_sent",
                                        "transport",
                                        "udp_mtu",
                                        "vrf",
                                        "vrf_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Destinations.Destination.Destination.Destination, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Destinations.Destination.Destination.Destination, self).__setattr__(name, value)


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

                            self.ip_type = YLeaf(YType.enumeration, "ip-type")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ip_type",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ip_type.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ip_type.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dest-ip-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ip_type.is_set or self.ip_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_type.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ip-type" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ip-type"):
                                self.ip_type = value
                                self.ip_type.value_namespace = name_space
                                self.ip_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for leaf in self.sub_id.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.dest_port.is_set or
                            self.dscp.is_set or
                            self.encoding.is_set or
                            self.id.is_set or
                            self.last_collection_time.is_set or
                            self.state.is_set or
                            self.sub_id_str.is_set or
                            self.tls.is_set or
                            self.tls_host.is_set or
                            self.total_num_of_bytes_sent.is_set or
                            self.total_num_of_packets_sent.is_set or
                            self.transport.is_set or
                            self.udp_mtu.is_set or
                            self.vrf.is_set or
                            self.vrf_id.is_set or
                            (self.dest_ip_address is not None and self.dest_ip_address.has_data()))

                    def has_operation(self):
                        for leaf in self.sub_id.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dest_port.yfilter != YFilter.not_set or
                            self.dscp.yfilter != YFilter.not_set or
                            self.encoding.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.last_collection_time.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.sub_id.yfilter != YFilter.not_set or
                            self.sub_id_str.yfilter != YFilter.not_set or
                            self.tls.yfilter != YFilter.not_set or
                            self.tls_host.yfilter != YFilter.not_set or
                            self.total_num_of_bytes_sent.yfilter != YFilter.not_set or
                            self.total_num_of_packets_sent.yfilter != YFilter.not_set or
                            self.transport.yfilter != YFilter.not_set or
                            self.udp_mtu.yfilter != YFilter.not_set or
                            self.vrf.yfilter != YFilter.not_set or
                            self.vrf_id.yfilter != YFilter.not_set or
                            (self.dest_ip_address is not None and self.dest_ip_address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dest_port.is_set or self.dest_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dest_port.get_name_leafdata())
                        if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dscp.get_name_leafdata())
                        if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encoding.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.last_collection_time.is_set or self.last_collection_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_collection_time.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.sub_id_str.is_set or self.sub_id_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sub_id_str.get_name_leafdata())
                        if (self.tls.is_set or self.tls.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tls.get_name_leafdata())
                        if (self.tls_host.is_set or self.tls_host.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tls_host.get_name_leafdata())
                        if (self.total_num_of_bytes_sent.is_set or self.total_num_of_bytes_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_num_of_bytes_sent.get_name_leafdata())
                        if (self.total_num_of_packets_sent.is_set or self.total_num_of_packets_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_num_of_packets_sent.get_name_leafdata())
                        if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transport.get_name_leafdata())
                        if (self.udp_mtu.is_set or self.udp_mtu.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_mtu.get_name_leafdata())
                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf.get_name_leafdata())
                        if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_id.get_name_leafdata())

                        leaf_name_data.extend(self.sub_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "dest-ip-address"):
                            if (self.dest_ip_address is None):
                                self.dest_ip_address = TelemetryModelDriven.Destinations.Destination.Destination.Destination.DestIpAddress()
                                self.dest_ip_address.parent = self
                                self._children_name_map["dest_ip_address"] = "dest-ip-address"
                            return self.dest_ip_address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dest-ip-address" or name == "dest-port" or name == "dscp" or name == "encoding" or name == "id" or name == "last-collection-time" or name == "state" or name == "sub-id" or name == "sub-id-str" or name == "tls" or name == "tls-host" or name == "total-num-of-bytes-sent" or name == "total-num-of-packets-sent" or name == "transport" or name == "udp-mtu" or name == "vrf" or name == "vrf-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dest-port"):
                            self.dest_port = value
                            self.dest_port.value_namespace = name_space
                            self.dest_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "dscp"):
                            self.dscp = value
                            self.dscp.value_namespace = name_space
                            self.dscp.value_namespace_prefix = name_space_prefix
                        if(value_path == "encoding"):
                            self.encoding = value
                            self.encoding.value_namespace = name_space
                            self.encoding.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-collection-time"):
                            self.last_collection_time = value
                            self.last_collection_time.value_namespace = name_space
                            self.last_collection_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "sub-id"):
                            self.sub_id.append(value)
                        if(value_path == "sub-id-str"):
                            self.sub_id_str = value
                            self.sub_id_str.value_namespace = name_space
                            self.sub_id_str.value_namespace_prefix = name_space_prefix
                        if(value_path == "tls"):
                            self.tls = value
                            self.tls.value_namespace = name_space
                            self.tls.value_namespace_prefix = name_space_prefix
                        if(value_path == "tls-host"):
                            self.tls_host = value
                            self.tls_host.value_namespace = name_space
                            self.tls_host.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-num-of-bytes-sent"):
                            self.total_num_of_bytes_sent = value
                            self.total_num_of_bytes_sent.value_namespace = name_space
                            self.total_num_of_bytes_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-num-of-packets-sent"):
                            self.total_num_of_packets_sent = value
                            self.total_num_of_packets_sent.value_namespace = name_space
                            self.total_num_of_packets_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "transport"):
                            self.transport = value
                            self.transport.value_namespace = name_space
                            self.transport.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-mtu"):
                            self.udp_mtu = value
                            self.udp_mtu.value_namespace = name_space
                            self.udp_mtu.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf"):
                            self.vrf = value
                            self.vrf.value_namespace = name_space
                            self.vrf.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-id"):
                            self.vrf_id = value
                            self.vrf_id.value_namespace = name_space
                            self.vrf_id.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg_total_time",
                                        "cadence",
                                        "encoding",
                                        "id",
                                        "last_collection_end_time",
                                        "last_collection_start_time",
                                        "max_collection_time",
                                        "max_total_time",
                                        "min_collection_time",
                                        "min_total_time",
                                        "total_collections",
                                        "total_not_ready",
                                        "total_on_data_instances",
                                        "total_other_errors",
                                        "total_send_drops",
                                        "total_send_errors") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup, self).__setattr__(name, value)


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

                            self.path = YLeaf(YType.str, "path")

                            self.state = YLeaf(YType.boolean, "state")

                            self.status_str = YLeaf(YType.str, "status-str")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("path",
                                            "state",
                                            "status_str") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.path.is_set or
                                self.state.is_set or
                                self.status_str.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.path.yfilter != YFilter.not_set or
                                self.state.yfilter != YFilter.not_set or
                                self.status_str.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "collection-path" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path.get_name_leafdata())
                            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.state.get_name_leafdata())
                            if (self.status_str.is_set or self.status_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status_str.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "path" or name == "state" or name == "status-str"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "path"):
                                self.path = value
                                self.path.value_namespace = name_space
                                self.path.value_namespace_prefix = name_space_prefix
                            if(value_path == "state"):
                                self.state = value
                                self.state.value_namespace = name_space
                                self.state.value_namespace_prefix = name_space_prefix
                            if(value_path == "status-str"):
                                self.status_str = value
                                self.status_str.value_namespace = name_space
                                self.status_str.value_namespace_prefix = name_space_prefix


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("avg_collection_time",
                                            "cadence",
                                            "collection_method",
                                            "max_collection_time",
                                            "min_collection_time",
                                            "path",
                                            "status",
                                            "total_collections",
                                            "total_collections_missed",
                                            "total_datalist_count",
                                            "total_datalist_errors",
                                            "total_encode_errors",
                                            "total_encode_notready",
                                            "total_finddata_count",
                                            "total_finddata_errors",
                                            "total_get_bulk_count",
                                            "total_get_bulk_errors",
                                            "total_get_count",
                                            "total_get_errors",
                                            "total_item_count",
                                            "total_list_count",
                                            "total_list_errors",
                                            "total_send_bytes_dropped",
                                            "total_send_drops",
                                            "total_send_errors",
                                            "total_send_packets",
                                            "total_sent_bytes") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.avg_collection_time.is_set or
                                self.cadence.is_set or
                                self.collection_method.is_set or
                                self.max_collection_time.is_set or
                                self.min_collection_time.is_set or
                                self.path.is_set or
                                self.status.is_set or
                                self.total_collections.is_set or
                                self.total_collections_missed.is_set or
                                self.total_datalist_count.is_set or
                                self.total_datalist_errors.is_set or
                                self.total_encode_errors.is_set or
                                self.total_encode_notready.is_set or
                                self.total_finddata_count.is_set or
                                self.total_finddata_errors.is_set or
                                self.total_get_bulk_count.is_set or
                                self.total_get_bulk_errors.is_set or
                                self.total_get_count.is_set or
                                self.total_get_errors.is_set or
                                self.total_item_count.is_set or
                                self.total_list_count.is_set or
                                self.total_list_errors.is_set or
                                self.total_send_bytes_dropped.is_set or
                                self.total_send_drops.is_set or
                                self.total_send_errors.is_set or
                                self.total_send_packets.is_set or
                                self.total_sent_bytes.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.avg_collection_time.yfilter != YFilter.not_set or
                                self.cadence.yfilter != YFilter.not_set or
                                self.collection_method.yfilter != YFilter.not_set or
                                self.max_collection_time.yfilter != YFilter.not_set or
                                self.min_collection_time.yfilter != YFilter.not_set or
                                self.path.yfilter != YFilter.not_set or
                                self.status.yfilter != YFilter.not_set or
                                self.total_collections.yfilter != YFilter.not_set or
                                self.total_collections_missed.yfilter != YFilter.not_set or
                                self.total_datalist_count.yfilter != YFilter.not_set or
                                self.total_datalist_errors.yfilter != YFilter.not_set or
                                self.total_encode_errors.yfilter != YFilter.not_set or
                                self.total_encode_notready.yfilter != YFilter.not_set or
                                self.total_finddata_count.yfilter != YFilter.not_set or
                                self.total_finddata_errors.yfilter != YFilter.not_set or
                                self.total_get_bulk_count.yfilter != YFilter.not_set or
                                self.total_get_bulk_errors.yfilter != YFilter.not_set or
                                self.total_get_count.yfilter != YFilter.not_set or
                                self.total_get_errors.yfilter != YFilter.not_set or
                                self.total_item_count.yfilter != YFilter.not_set or
                                self.total_list_count.yfilter != YFilter.not_set or
                                self.total_list_errors.yfilter != YFilter.not_set or
                                self.total_send_bytes_dropped.yfilter != YFilter.not_set or
                                self.total_send_drops.yfilter != YFilter.not_set or
                                self.total_send_errors.yfilter != YFilter.not_set or
                                self.total_send_packets.yfilter != YFilter.not_set or
                                self.total_sent_bytes.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "internal-collection-group" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.avg_collection_time.is_set or self.avg_collection_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.avg_collection_time.get_name_leafdata())
                            if (self.cadence.is_set or self.cadence.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.cadence.get_name_leafdata())
                            if (self.collection_method.is_set or self.collection_method.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.collection_method.get_name_leafdata())
                            if (self.max_collection_time.is_set or self.max_collection_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_collection_time.get_name_leafdata())
                            if (self.min_collection_time.is_set or self.min_collection_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.min_collection_time.get_name_leafdata())
                            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path.get_name_leafdata())
                            if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status.get_name_leafdata())
                            if (self.total_collections.is_set or self.total_collections.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_collections.get_name_leafdata())
                            if (self.total_collections_missed.is_set or self.total_collections_missed.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_collections_missed.get_name_leafdata())
                            if (self.total_datalist_count.is_set or self.total_datalist_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_datalist_count.get_name_leafdata())
                            if (self.total_datalist_errors.is_set or self.total_datalist_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_datalist_errors.get_name_leafdata())
                            if (self.total_encode_errors.is_set or self.total_encode_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_encode_errors.get_name_leafdata())
                            if (self.total_encode_notready.is_set or self.total_encode_notready.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_encode_notready.get_name_leafdata())
                            if (self.total_finddata_count.is_set or self.total_finddata_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_finddata_count.get_name_leafdata())
                            if (self.total_finddata_errors.is_set or self.total_finddata_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_finddata_errors.get_name_leafdata())
                            if (self.total_get_bulk_count.is_set or self.total_get_bulk_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_get_bulk_count.get_name_leafdata())
                            if (self.total_get_bulk_errors.is_set or self.total_get_bulk_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_get_bulk_errors.get_name_leafdata())
                            if (self.total_get_count.is_set or self.total_get_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_get_count.get_name_leafdata())
                            if (self.total_get_errors.is_set or self.total_get_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_get_errors.get_name_leafdata())
                            if (self.total_item_count.is_set or self.total_item_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_item_count.get_name_leafdata())
                            if (self.total_list_count.is_set or self.total_list_count.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_list_count.get_name_leafdata())
                            if (self.total_list_errors.is_set or self.total_list_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_list_errors.get_name_leafdata())
                            if (self.total_send_bytes_dropped.is_set or self.total_send_bytes_dropped.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_send_bytes_dropped.get_name_leafdata())
                            if (self.total_send_drops.is_set or self.total_send_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_send_drops.get_name_leafdata())
                            if (self.total_send_errors.is_set or self.total_send_errors.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_send_errors.get_name_leafdata())
                            if (self.total_send_packets.is_set or self.total_send_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_send_packets.get_name_leafdata())
                            if (self.total_sent_bytes.is_set or self.total_sent_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_sent_bytes.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "avg-collection-time" or name == "cadence" or name == "collection-method" or name == "max-collection-time" or name == "min-collection-time" or name == "path" or name == "status" or name == "total-collections" or name == "total-collections-missed" or name == "total-datalist-count" or name == "total-datalist-errors" or name == "total-encode-errors" or name == "total-encode-notready" or name == "total-finddata-count" or name == "total-finddata-errors" or name == "total-get-bulk-count" or name == "total-get-bulk-errors" or name == "total-get-count" or name == "total-get-errors" or name == "total-item-count" or name == "total-list-count" or name == "total-list-errors" or name == "total-send-bytes-dropped" or name == "total-send-drops" or name == "total-send-errors" or name == "total-send-packets" or name == "total-sent-bytes"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "avg-collection-time"):
                                self.avg_collection_time = value
                                self.avg_collection_time.value_namespace = name_space
                                self.avg_collection_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "cadence"):
                                self.cadence = value
                                self.cadence.value_namespace = name_space
                                self.cadence.value_namespace_prefix = name_space_prefix
                            if(value_path == "collection-method"):
                                self.collection_method = value
                                self.collection_method.value_namespace = name_space
                                self.collection_method.value_namespace_prefix = name_space_prefix
                            if(value_path == "max-collection-time"):
                                self.max_collection_time = value
                                self.max_collection_time.value_namespace = name_space
                                self.max_collection_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "min-collection-time"):
                                self.min_collection_time = value
                                self.min_collection_time.value_namespace = name_space
                                self.min_collection_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "path"):
                                self.path = value
                                self.path.value_namespace = name_space
                                self.path.value_namespace_prefix = name_space_prefix
                            if(value_path == "status"):
                                self.status = value
                                self.status.value_namespace = name_space
                                self.status.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-collections"):
                                self.total_collections = value
                                self.total_collections.value_namespace = name_space
                                self.total_collections.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-collections-missed"):
                                self.total_collections_missed = value
                                self.total_collections_missed.value_namespace = name_space
                                self.total_collections_missed.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-datalist-count"):
                                self.total_datalist_count = value
                                self.total_datalist_count.value_namespace = name_space
                                self.total_datalist_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-datalist-errors"):
                                self.total_datalist_errors = value
                                self.total_datalist_errors.value_namespace = name_space
                                self.total_datalist_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-encode-errors"):
                                self.total_encode_errors = value
                                self.total_encode_errors.value_namespace = name_space
                                self.total_encode_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-encode-notready"):
                                self.total_encode_notready = value
                                self.total_encode_notready.value_namespace = name_space
                                self.total_encode_notready.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-finddata-count"):
                                self.total_finddata_count = value
                                self.total_finddata_count.value_namespace = name_space
                                self.total_finddata_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-finddata-errors"):
                                self.total_finddata_errors = value
                                self.total_finddata_errors.value_namespace = name_space
                                self.total_finddata_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-get-bulk-count"):
                                self.total_get_bulk_count = value
                                self.total_get_bulk_count.value_namespace = name_space
                                self.total_get_bulk_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-get-bulk-errors"):
                                self.total_get_bulk_errors = value
                                self.total_get_bulk_errors.value_namespace = name_space
                                self.total_get_bulk_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-get-count"):
                                self.total_get_count = value
                                self.total_get_count.value_namespace = name_space
                                self.total_get_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-get-errors"):
                                self.total_get_errors = value
                                self.total_get_errors.value_namespace = name_space
                                self.total_get_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-item-count"):
                                self.total_item_count = value
                                self.total_item_count.value_namespace = name_space
                                self.total_item_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-list-count"):
                                self.total_list_count = value
                                self.total_list_count.value_namespace = name_space
                                self.total_list_count.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-list-errors"):
                                self.total_list_errors = value
                                self.total_list_errors.value_namespace = name_space
                                self.total_list_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-send-bytes-dropped"):
                                self.total_send_bytes_dropped = value
                                self.total_send_bytes_dropped.value_namespace = name_space
                                self.total_send_bytes_dropped.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-send-drops"):
                                self.total_send_drops = value
                                self.total_send_drops.value_namespace = name_space
                                self.total_send_drops.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-send-errors"):
                                self.total_send_errors = value
                                self.total_send_errors.value_namespace = name_space
                                self.total_send_errors.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-send-packets"):
                                self.total_send_packets = value
                                self.total_send_packets.value_namespace = name_space
                                self.total_send_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-sent-bytes"):
                                self.total_sent_bytes = value
                                self.total_sent_bytes.value_namespace = name_space
                                self.total_sent_bytes.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.collection_path:
                            if (c.has_data()):
                                return True
                        for c in self.internal_collection_group:
                            if (c.has_data()):
                                return True
                        return (
                            self.avg_total_time.is_set or
                            self.cadence.is_set or
                            self.encoding.is_set or
                            self.id.is_set or
                            self.last_collection_end_time.is_set or
                            self.last_collection_start_time.is_set or
                            self.max_collection_time.is_set or
                            self.max_total_time.is_set or
                            self.min_collection_time.is_set or
                            self.min_total_time.is_set or
                            self.total_collections.is_set or
                            self.total_not_ready.is_set or
                            self.total_on_data_instances.is_set or
                            self.total_other_errors.is_set or
                            self.total_send_drops.is_set or
                            self.total_send_errors.is_set)

                    def has_operation(self):
                        for c in self.collection_path:
                            if (c.has_operation()):
                                return True
                        for c in self.internal_collection_group:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg_total_time.yfilter != YFilter.not_set or
                            self.cadence.yfilter != YFilter.not_set or
                            self.encoding.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.last_collection_end_time.yfilter != YFilter.not_set or
                            self.last_collection_start_time.yfilter != YFilter.not_set or
                            self.max_collection_time.yfilter != YFilter.not_set or
                            self.max_total_time.yfilter != YFilter.not_set or
                            self.min_collection_time.yfilter != YFilter.not_set or
                            self.min_total_time.yfilter != YFilter.not_set or
                            self.total_collections.yfilter != YFilter.not_set or
                            self.total_not_ready.yfilter != YFilter.not_set or
                            self.total_on_data_instances.yfilter != YFilter.not_set or
                            self.total_other_errors.yfilter != YFilter.not_set or
                            self.total_send_drops.yfilter != YFilter.not_set or
                            self.total_send_errors.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "collection-group" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg_total_time.is_set or self.avg_total_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg_total_time.get_name_leafdata())
                        if (self.cadence.is_set or self.cadence.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cadence.get_name_leafdata())
                        if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.encoding.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.last_collection_end_time.is_set or self.last_collection_end_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_collection_end_time.get_name_leafdata())
                        if (self.last_collection_start_time.is_set or self.last_collection_start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_collection_start_time.get_name_leafdata())
                        if (self.max_collection_time.is_set or self.max_collection_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_collection_time.get_name_leafdata())
                        if (self.max_total_time.is_set or self.max_total_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_total_time.get_name_leafdata())
                        if (self.min_collection_time.is_set or self.min_collection_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_collection_time.get_name_leafdata())
                        if (self.min_total_time.is_set or self.min_total_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_total_time.get_name_leafdata())
                        if (self.total_collections.is_set or self.total_collections.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_collections.get_name_leafdata())
                        if (self.total_not_ready.is_set or self.total_not_ready.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_not_ready.get_name_leafdata())
                        if (self.total_on_data_instances.is_set or self.total_on_data_instances.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_on_data_instances.get_name_leafdata())
                        if (self.total_other_errors.is_set or self.total_other_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_other_errors.get_name_leafdata())
                        if (self.total_send_drops.is_set or self.total_send_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_send_drops.get_name_leafdata())
                        if (self.total_send_errors.is_set or self.total_send_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_send_errors.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "collection-path"):
                            for c in self.collection_path:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.CollectionPath()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.collection_path.append(c)
                            return c

                        if (child_yang_name == "internal-collection-group"):
                            for c in self.internal_collection_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup.InternalCollectionGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.internal_collection_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "collection-path" or name == "internal-collection-group" or name == "avg-total-time" or name == "cadence" or name == "encoding" or name == "id" or name == "last-collection-end-time" or name == "last-collection-start-time" or name == "max-collection-time" or name == "max-total-time" or name == "min-collection-time" or name == "min-total-time" or name == "total-collections" or name == "total-not-ready" or name == "total-on-data-instances" or name == "total-other-errors" or name == "total-send-drops" or name == "total-send-errors"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg-total-time"):
                            self.avg_total_time = value
                            self.avg_total_time.value_namespace = name_space
                            self.avg_total_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "cadence"):
                            self.cadence = value
                            self.cadence.value_namespace = name_space
                            self.cadence.value_namespace_prefix = name_space_prefix
                        if(value_path == "encoding"):
                            self.encoding = value
                            self.encoding.value_namespace = name_space
                            self.encoding.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-collection-end-time"):
                            self.last_collection_end_time = value
                            self.last_collection_end_time.value_namespace = name_space
                            self.last_collection_end_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-collection-start-time"):
                            self.last_collection_start_time = value
                            self.last_collection_start_time.value_namespace = name_space
                            self.last_collection_start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-collection-time"):
                            self.max_collection_time = value
                            self.max_collection_time.value_namespace = name_space
                            self.max_collection_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-total-time"):
                            self.max_total_time = value
                            self.max_total_time.value_namespace = name_space
                            self.max_total_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "min-collection-time"):
                            self.min_collection_time = value
                            self.min_collection_time.value_namespace = name_space
                            self.min_collection_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "min-total-time"):
                            self.min_total_time = value
                            self.min_total_time.value_namespace = name_space
                            self.min_total_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-collections"):
                            self.total_collections = value
                            self.total_collections.value_namespace = name_space
                            self.total_collections.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-not-ready"):
                            self.total_not_ready = value
                            self.total_not_ready.value_namespace = name_space
                            self.total_not_ready.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-on-data-instances"):
                            self.total_on_data_instances = value
                            self.total_on_data_instances.value_namespace = name_space
                            self.total_on_data_instances.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-other-errors"):
                            self.total_other_errors = value
                            self.total_other_errors.value_namespace = name_space
                            self.total_other_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-send-drops"):
                            self.total_send_drops = value
                            self.total_send_drops.value_namespace = name_space
                            self.total_send_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-send-errors"):
                            self.total_send_errors = value
                            self.total_send_errors.value_namespace = name_space
                            self.total_send_errors.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.collection_group:
                        if (c.has_data()):
                            return True
                    return (self.destination is not None and self.destination.has_data())

                def has_operation(self):
                    for c in self.collection_group:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.destination is not None and self.destination.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "destination" + path_buffer

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

                    if (child_yang_name == "collection-group"):
                        for c in self.collection_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.Destinations.Destination.Destination.CollectionGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.collection_group.append(c)
                        return c

                    if (child_yang_name == "destination"):
                        if (self.destination is None):
                            self.destination = TelemetryModelDriven.Destinations.Destination.Destination.Destination()
                            self.destination.parent = self
                            self._children_name_map["destination"] = "destination"
                        return self.destination

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "collection-group" or name == "destination"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                for c in self.destination:
                    if (c.has_data()):
                        return True
                return (
                    self.destination_id.is_set or
                    self.configured.is_set or
                    self.id.is_set)

            def has_operation(self):
                for c in self.destination:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination_id.yfilter != YFilter.not_set or
                    self.configured.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "destination" + "[destination-id='" + self.destination_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/destinations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination_id.is_set or self.destination_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination_id.get_name_leafdata())
                if (self.configured.is_set or self.configured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configured.get_name_leafdata())
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "destination"):
                    for c in self.destination:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = TelemetryModelDriven.Destinations.Destination.Destination()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.destination.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination" or name == "destination-id" or name == "configured" or name == "id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination-id"):
                    self.destination_id = value
                    self.destination_id.value_namespace = name_space
                    self.destination_id.value_namespace_prefix = name_space_prefix
                if(value_path == "configured"):
                    self.configured = value
                    self.configured.value_namespace = name_space
                    self.configured.value_namespace_prefix = name_space_prefix
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.destination:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.destination:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "destinations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "destination"):
                for c in self.destination:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TelemetryModelDriven.Destinations.Destination()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.destination.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.subscription = YList(self)

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
                        super(TelemetryModelDriven.Subscriptions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetryModelDriven.Subscriptions, self).__setattr__(name, value)


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

                self.subscription_id = YLeaf(YType.str, "subscription-id")

                self.subscription = TelemetryModelDriven.Subscriptions.Subscription.Subscription()
                self.subscription.parent = self
                self._children_name_map["subscription"] = "subscription"
                self._children_yang_names.add("subscription")

                self.collection_group = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("subscription_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetryModelDriven.Subscriptions.Subscription, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetryModelDriven.Subscriptions.Subscription, self).__setattr__(name, value)


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

                    self.id = YLeaf(YType.str, "id")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.source_interface = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface()
                    self.source_interface.parent = self
                    self._children_name_map["source_interface"] = "source-interface"
                    self._children_yang_names.add("source-interface")

                    self.destination_grp = YList(self)
                    self.sensor_profile = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription, self).__setattr__(name, value)


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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        self.state = YLeaf(YType.boolean, "state")

                        self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "ipv4_address",
                                        "ipv6_address",
                                        "state",
                                        "vrf_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.ipv4_address.is_set or
                            self.ipv6_address.is_set or
                            self.state.is_set or
                            self.vrf_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.ipv4_address.yfilter != YFilter.not_set or
                            self.ipv6_address.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.vrf_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "source-interface" + path_buffer

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
                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "ipv4-address" or name == "ipv6-address" or name == "state" or name == "vrf-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-address"):
                            self.ipv4_address = value
                            self.ipv4_address.value_namespace = name_space
                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-address"):
                            self.ipv6_address = value
                            self.ipv6_address.value_namespace = name_space
                            self.ipv6_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-id"):
                            self.vrf_id = value
                            self.vrf_id.value_namespace = name_space
                            self.vrf_id.value_namespace_prefix = name_space_prefix


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

                        self.heartbeat_interval = YLeaf(YType.uint32, "heartbeat-interval")

                        self.sample_interval = YLeaf(YType.uint32, "sample-interval")

                        self.suppress_redundant = YLeaf(YType.boolean, "suppress-redundant")

                        self.sensor_group = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup()
                        self.sensor_group.parent = self
                        self._children_name_map["sensor_group"] = "sensor-group"
                        self._children_yang_names.add("sensor-group")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("heartbeat_interval",
                                        "sample_interval",
                                        "suppress_redundant") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile, self).__setattr__(name, value)


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

                            self.configured = YLeaf(YType.uint32, "configured")

                            self.id = YLeaf(YType.str, "id")

                            self.sensor_path = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("configured",
                                            "id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup, self).__setattr__(name, value)


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

                                self.path = YLeaf(YType.str, "path")

                                self.state = YLeaf(YType.boolean, "state")

                                self.status_str = YLeaf(YType.str, "status-str")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("path",
                                                "state",
                                                "status_str") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.path.is_set or
                                    self.state.is_set or
                                    self.status_str.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.path.yfilter != YFilter.not_set or
                                    self.state.yfilter != YFilter.not_set or
                                    self.status_str.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sensor-path" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path.get_name_leafdata())
                                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.state.get_name_leafdata())
                                if (self.status_str.is_set or self.status_str.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status_str.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "path" or name == "state" or name == "status-str"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "path"):
                                    self.path = value
                                    self.path.value_namespace = name_space
                                    self.path.value_namespace_prefix = name_space_prefix
                                if(value_path == "state"):
                                    self.state = value
                                    self.state.value_namespace = name_space
                                    self.state.value_namespace_prefix = name_space_prefix
                                if(value_path == "status-str"):
                                    self.status_str = value
                                    self.status_str.value_namespace = name_space
                                    self.status_str.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sensor_path:
                                if (c.has_data()):
                                    return True
                            return (
                                self.configured.is_set or
                                self.id.is_set)

                        def has_operation(self):
                            for c in self.sensor_path:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.configured.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sensor-group" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.configured.is_set or self.configured.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.configured.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sensor-path"):
                                for c in self.sensor_path:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup.SensorPath()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sensor_path.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sensor-path" or name == "configured" or name == "id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "configured"):
                                self.configured = value
                                self.configured.value_namespace = name_space
                                self.configured.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.heartbeat_interval.is_set or
                            self.sample_interval.is_set or
                            self.suppress_redundant.is_set or
                            (self.sensor_group is not None and self.sensor_group.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.heartbeat_interval.yfilter != YFilter.not_set or
                            self.sample_interval.yfilter != YFilter.not_set or
                            self.suppress_redundant.yfilter != YFilter.not_set or
                            (self.sensor_group is not None and self.sensor_group.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sensor-profile" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.heartbeat_interval.is_set or self.heartbeat_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.heartbeat_interval.get_name_leafdata())
                        if (self.sample_interval.is_set or self.sample_interval.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sample_interval.get_name_leafdata())
                        if (self.suppress_redundant.is_set or self.suppress_redundant.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.suppress_redundant.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sensor-group"):
                            if (self.sensor_group is None):
                                self.sensor_group = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile.SensorGroup()
                                self.sensor_group.parent = self
                                self._children_name_map["sensor_group"] = "sensor-group"
                            return self.sensor_group

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sensor-group" or name == "heartbeat-interval" or name == "sample-interval" or name == "suppress-redundant"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "heartbeat-interval"):
                            self.heartbeat_interval = value
                            self.heartbeat_interval.value_namespace = name_space
                            self.heartbeat_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "sample-interval"):
                            self.sample_interval = value
                            self.sample_interval.value_namespace = name_space
                            self.sample_interval.value_namespace_prefix = name_space_prefix
                        if(value_path == "suppress-redundant"):
                            self.suppress_redundant = value
                            self.suppress_redundant.value_namespace = name_space
                            self.suppress_redundant.value_namespace_prefix = name_space_prefix


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

                        self.configured = YLeaf(YType.uint32, "configured")

                        self.id = YLeaf(YType.str, "id")

                        self.destination = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("configured",
                                        "id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp, self).__setattr__(name, value)


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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("dest_port",
                                            "dscp",
                                            "encoding",
                                            "id",
                                            "last_collection_time",
                                            "state",
                                            "sub_id",
                                            "sub_id_str",
                                            "tls",
                                            "tls_host",
                                            "total_num_of_bytes_sent",
                                            "total_num_of_packets_sent",
                                            "transport",
                                            "udp_mtu",
                                            "vrf",
                                            "vrf_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination, self).__setattr__(name, value)


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

                                self.ip_type = YLeaf(YType.enumeration, "ip-type")

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ip_type",
                                                "ipv4_address",
                                                "ipv6_address") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ip_type.is_set or
                                    self.ipv4_address.is_set or
                                    self.ipv6_address.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ip_type.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dest-ip-address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ip_type.is_set or self.ip_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_type.get_name_leafdata())
                                if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ip-type" or name == "ipv4-address" or name == "ipv6-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ip-type"):
                                    self.ip_type = value
                                    self.ip_type.value_namespace = name_space
                                    self.ip_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for leaf in self.sub_id.getYLeafs():
                                if (leaf.yfilter != YFilter.not_set):
                                    return True
                            return (
                                self.dest_port.is_set or
                                self.dscp.is_set or
                                self.encoding.is_set or
                                self.id.is_set or
                                self.last_collection_time.is_set or
                                self.state.is_set or
                                self.sub_id_str.is_set or
                                self.tls.is_set or
                                self.tls_host.is_set or
                                self.total_num_of_bytes_sent.is_set or
                                self.total_num_of_packets_sent.is_set or
                                self.transport.is_set or
                                self.udp_mtu.is_set or
                                self.vrf.is_set or
                                self.vrf_id.is_set or
                                (self.dest_ip_address is not None and self.dest_ip_address.has_data()))

                        def has_operation(self):
                            for leaf in self.sub_id.getYLeafs():
                                if (leaf.is_set):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.dest_port.yfilter != YFilter.not_set or
                                self.dscp.yfilter != YFilter.not_set or
                                self.encoding.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set or
                                self.last_collection_time.yfilter != YFilter.not_set or
                                self.state.yfilter != YFilter.not_set or
                                self.sub_id.yfilter != YFilter.not_set or
                                self.sub_id_str.yfilter != YFilter.not_set or
                                self.tls.yfilter != YFilter.not_set or
                                self.tls_host.yfilter != YFilter.not_set or
                                self.total_num_of_bytes_sent.yfilter != YFilter.not_set or
                                self.total_num_of_packets_sent.yfilter != YFilter.not_set or
                                self.transport.yfilter != YFilter.not_set or
                                self.udp_mtu.yfilter != YFilter.not_set or
                                self.vrf.yfilter != YFilter.not_set or
                                self.vrf_id.yfilter != YFilter.not_set or
                                (self.dest_ip_address is not None and self.dest_ip_address.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.dest_port.is_set or self.dest_port.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dest_port.get_name_leafdata())
                            if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.dscp.get_name_leafdata())
                            if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encoding.get_name_leafdata())
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())
                            if (self.last_collection_time.is_set or self.last_collection_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.last_collection_time.get_name_leafdata())
                            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.state.get_name_leafdata())
                            if (self.sub_id_str.is_set or self.sub_id_str.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sub_id_str.get_name_leafdata())
                            if (self.tls.is_set or self.tls.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tls.get_name_leafdata())
                            if (self.tls_host.is_set or self.tls_host.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tls_host.get_name_leafdata())
                            if (self.total_num_of_bytes_sent.is_set or self.total_num_of_bytes_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_num_of_bytes_sent.get_name_leafdata())
                            if (self.total_num_of_packets_sent.is_set or self.total_num_of_packets_sent.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.total_num_of_packets_sent.get_name_leafdata())
                            if (self.transport.is_set or self.transport.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transport.get_name_leafdata())
                            if (self.udp_mtu.is_set or self.udp_mtu.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.udp_mtu.get_name_leafdata())
                            if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf.get_name_leafdata())
                            if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_id.get_name_leafdata())

                            leaf_name_data.extend(self.sub_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "dest-ip-address"):
                                if (self.dest_ip_address is None):
                                    self.dest_ip_address = TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination.DestIpAddress()
                                    self.dest_ip_address.parent = self
                                    self._children_name_map["dest_ip_address"] = "dest-ip-address"
                                return self.dest_ip_address

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "dest-ip-address" or name == "dest-port" or name == "dscp" or name == "encoding" or name == "id" or name == "last-collection-time" or name == "state" or name == "sub-id" or name == "sub-id-str" or name == "tls" or name == "tls-host" or name == "total-num-of-bytes-sent" or name == "total-num-of-packets-sent" or name == "transport" or name == "udp-mtu" or name == "vrf" or name == "vrf-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "dest-port"):
                                self.dest_port = value
                                self.dest_port.value_namespace = name_space
                                self.dest_port.value_namespace_prefix = name_space_prefix
                            if(value_path == "dscp"):
                                self.dscp = value
                                self.dscp.value_namespace = name_space
                                self.dscp.value_namespace_prefix = name_space_prefix
                            if(value_path == "encoding"):
                                self.encoding = value
                                self.encoding.value_namespace = name_space
                                self.encoding.value_namespace_prefix = name_space_prefix
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix
                            if(value_path == "last-collection-time"):
                                self.last_collection_time = value
                                self.last_collection_time.value_namespace = name_space
                                self.last_collection_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "state"):
                                self.state = value
                                self.state.value_namespace = name_space
                                self.state.value_namespace_prefix = name_space_prefix
                            if(value_path == "sub-id"):
                                self.sub_id.append(value)
                            if(value_path == "sub-id-str"):
                                self.sub_id_str = value
                                self.sub_id_str.value_namespace = name_space
                                self.sub_id_str.value_namespace_prefix = name_space_prefix
                            if(value_path == "tls"):
                                self.tls = value
                                self.tls.value_namespace = name_space
                                self.tls.value_namespace_prefix = name_space_prefix
                            if(value_path == "tls-host"):
                                self.tls_host = value
                                self.tls_host.value_namespace = name_space
                                self.tls_host.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-num-of-bytes-sent"):
                                self.total_num_of_bytes_sent = value
                                self.total_num_of_bytes_sent.value_namespace = name_space
                                self.total_num_of_bytes_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "total-num-of-packets-sent"):
                                self.total_num_of_packets_sent = value
                                self.total_num_of_packets_sent.value_namespace = name_space
                                self.total_num_of_packets_sent.value_namespace_prefix = name_space_prefix
                            if(value_path == "transport"):
                                self.transport = value
                                self.transport.value_namespace = name_space
                                self.transport.value_namespace_prefix = name_space_prefix
                            if(value_path == "udp-mtu"):
                                self.udp_mtu = value
                                self.udp_mtu.value_namespace = name_space
                                self.udp_mtu.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf"):
                                self.vrf = value
                                self.vrf.value_namespace = name_space
                                self.vrf.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-id"):
                                self.vrf_id = value
                                self.vrf_id.value_namespace = name_space
                                self.vrf_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.destination:
                            if (c.has_data()):
                                return True
                        return (
                            self.configured.is_set or
                            self.id.is_set)

                    def has_operation(self):
                        for c in self.destination:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.configured.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-grp" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.configured.is_set or self.configured.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.configured.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "destination"):
                            for c in self.destination:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp.Destination()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.destination.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination" or name == "configured" or name == "id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "configured"):
                            self.configured = value
                            self.configured.value_namespace = name_space
                            self.configured.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.destination_grp:
                        if (c.has_data()):
                            return True
                    for c in self.sensor_profile:
                        if (c.has_data()):
                            return True
                    return (
                        self.id.is_set or
                        self.state.is_set or
                        (self.source_interface is not None and self.source_interface.has_data()))

                def has_operation(self):
                    for c in self.destination_grp:
                        if (c.has_operation()):
                            return True
                    for c in self.sensor_profile:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        (self.source_interface is not None and self.source_interface.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscription" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "destination-grp"):
                        for c in self.destination_grp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.Subscriptions.Subscription.Subscription.DestinationGrp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination_grp.append(c)
                        return c

                    if (child_yang_name == "sensor-profile"):
                        for c in self.sensor_profile:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SensorProfile()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.sensor_profile.append(c)
                        return c

                    if (child_yang_name == "source-interface"):
                        if (self.source_interface is None):
                            self.source_interface = TelemetryModelDriven.Subscriptions.Subscription.Subscription.SourceInterface()
                            self.source_interface.parent = self
                            self._children_name_map["source_interface"] = "source-interface"
                        return self.source_interface

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-grp" or name == "sensor-profile" or name == "source-interface" or name == "id" or name == "state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("avg_total_time",
                                    "cadence",
                                    "encoding",
                                    "id",
                                    "last_collection_end_time",
                                    "last_collection_start_time",
                                    "max_collection_time",
                                    "max_total_time",
                                    "min_collection_time",
                                    "min_total_time",
                                    "total_collections",
                                    "total_not_ready",
                                    "total_on_data_instances",
                                    "total_other_errors",
                                    "total_send_drops",
                                    "total_send_errors") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup, self).__setattr__(name, value)


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

                        self.path = YLeaf(YType.str, "path")

                        self.state = YLeaf(YType.boolean, "state")

                        self.status_str = YLeaf(YType.str, "status-str")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("path",
                                        "state",
                                        "status_str") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.path.is_set or
                            self.state.is_set or
                            self.status_str.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.path.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.status_str.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "collection-path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.status_str.is_set or self.status_str.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status_str.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "path" or name == "state" or name == "status-str"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "path"):
                            self.path = value
                            self.path.value_namespace = name_space
                            self.path.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "status-str"):
                            self.status_str = value
                            self.status_str.value_namespace = name_space
                            self.status_str.value_namespace_prefix = name_space_prefix


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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("avg_collection_time",
                                        "cadence",
                                        "collection_method",
                                        "max_collection_time",
                                        "min_collection_time",
                                        "path",
                                        "status",
                                        "total_collections",
                                        "total_collections_missed",
                                        "total_datalist_count",
                                        "total_datalist_errors",
                                        "total_encode_errors",
                                        "total_encode_notready",
                                        "total_finddata_count",
                                        "total_finddata_errors",
                                        "total_get_bulk_count",
                                        "total_get_bulk_errors",
                                        "total_get_count",
                                        "total_get_errors",
                                        "total_item_count",
                                        "total_list_count",
                                        "total_list_errors",
                                        "total_send_bytes_dropped",
                                        "total_send_drops",
                                        "total_send_errors",
                                        "total_send_packets",
                                        "total_sent_bytes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.avg_collection_time.is_set or
                            self.cadence.is_set or
                            self.collection_method.is_set or
                            self.max_collection_time.is_set or
                            self.min_collection_time.is_set or
                            self.path.is_set or
                            self.status.is_set or
                            self.total_collections.is_set or
                            self.total_collections_missed.is_set or
                            self.total_datalist_count.is_set or
                            self.total_datalist_errors.is_set or
                            self.total_encode_errors.is_set or
                            self.total_encode_notready.is_set or
                            self.total_finddata_count.is_set or
                            self.total_finddata_errors.is_set or
                            self.total_get_bulk_count.is_set or
                            self.total_get_bulk_errors.is_set or
                            self.total_get_count.is_set or
                            self.total_get_errors.is_set or
                            self.total_item_count.is_set or
                            self.total_list_count.is_set or
                            self.total_list_errors.is_set or
                            self.total_send_bytes_dropped.is_set or
                            self.total_send_drops.is_set or
                            self.total_send_errors.is_set or
                            self.total_send_packets.is_set or
                            self.total_sent_bytes.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.avg_collection_time.yfilter != YFilter.not_set or
                            self.cadence.yfilter != YFilter.not_set or
                            self.collection_method.yfilter != YFilter.not_set or
                            self.max_collection_time.yfilter != YFilter.not_set or
                            self.min_collection_time.yfilter != YFilter.not_set or
                            self.path.yfilter != YFilter.not_set or
                            self.status.yfilter != YFilter.not_set or
                            self.total_collections.yfilter != YFilter.not_set or
                            self.total_collections_missed.yfilter != YFilter.not_set or
                            self.total_datalist_count.yfilter != YFilter.not_set or
                            self.total_datalist_errors.yfilter != YFilter.not_set or
                            self.total_encode_errors.yfilter != YFilter.not_set or
                            self.total_encode_notready.yfilter != YFilter.not_set or
                            self.total_finddata_count.yfilter != YFilter.not_set or
                            self.total_finddata_errors.yfilter != YFilter.not_set or
                            self.total_get_bulk_count.yfilter != YFilter.not_set or
                            self.total_get_bulk_errors.yfilter != YFilter.not_set or
                            self.total_get_count.yfilter != YFilter.not_set or
                            self.total_get_errors.yfilter != YFilter.not_set or
                            self.total_item_count.yfilter != YFilter.not_set or
                            self.total_list_count.yfilter != YFilter.not_set or
                            self.total_list_errors.yfilter != YFilter.not_set or
                            self.total_send_bytes_dropped.yfilter != YFilter.not_set or
                            self.total_send_drops.yfilter != YFilter.not_set or
                            self.total_send_errors.yfilter != YFilter.not_set or
                            self.total_send_packets.yfilter != YFilter.not_set or
                            self.total_sent_bytes.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "internal-collection-group" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.avg_collection_time.is_set or self.avg_collection_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg_collection_time.get_name_leafdata())
                        if (self.cadence.is_set or self.cadence.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cadence.get_name_leafdata())
                        if (self.collection_method.is_set or self.collection_method.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.collection_method.get_name_leafdata())
                        if (self.max_collection_time.is_set or self.max_collection_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_collection_time.get_name_leafdata())
                        if (self.min_collection_time.is_set or self.min_collection_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min_collection_time.get_name_leafdata())
                        if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path.get_name_leafdata())
                        if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.status.get_name_leafdata())
                        if (self.total_collections.is_set or self.total_collections.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_collections.get_name_leafdata())
                        if (self.total_collections_missed.is_set or self.total_collections_missed.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_collections_missed.get_name_leafdata())
                        if (self.total_datalist_count.is_set or self.total_datalist_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_datalist_count.get_name_leafdata())
                        if (self.total_datalist_errors.is_set or self.total_datalist_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_datalist_errors.get_name_leafdata())
                        if (self.total_encode_errors.is_set or self.total_encode_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_encode_errors.get_name_leafdata())
                        if (self.total_encode_notready.is_set or self.total_encode_notready.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_encode_notready.get_name_leafdata())
                        if (self.total_finddata_count.is_set or self.total_finddata_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_finddata_count.get_name_leafdata())
                        if (self.total_finddata_errors.is_set or self.total_finddata_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_finddata_errors.get_name_leafdata())
                        if (self.total_get_bulk_count.is_set or self.total_get_bulk_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_get_bulk_count.get_name_leafdata())
                        if (self.total_get_bulk_errors.is_set or self.total_get_bulk_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_get_bulk_errors.get_name_leafdata())
                        if (self.total_get_count.is_set or self.total_get_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_get_count.get_name_leafdata())
                        if (self.total_get_errors.is_set or self.total_get_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_get_errors.get_name_leafdata())
                        if (self.total_item_count.is_set or self.total_item_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_item_count.get_name_leafdata())
                        if (self.total_list_count.is_set or self.total_list_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_list_count.get_name_leafdata())
                        if (self.total_list_errors.is_set or self.total_list_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_list_errors.get_name_leafdata())
                        if (self.total_send_bytes_dropped.is_set or self.total_send_bytes_dropped.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_send_bytes_dropped.get_name_leafdata())
                        if (self.total_send_drops.is_set or self.total_send_drops.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_send_drops.get_name_leafdata())
                        if (self.total_send_errors.is_set or self.total_send_errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_send_errors.get_name_leafdata())
                        if (self.total_send_packets.is_set or self.total_send_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_send_packets.get_name_leafdata())
                        if (self.total_sent_bytes.is_set or self.total_sent_bytes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_sent_bytes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "avg-collection-time" or name == "cadence" or name == "collection-method" or name == "max-collection-time" or name == "min-collection-time" or name == "path" or name == "status" or name == "total-collections" or name == "total-collections-missed" or name == "total-datalist-count" or name == "total-datalist-errors" or name == "total-encode-errors" or name == "total-encode-notready" or name == "total-finddata-count" or name == "total-finddata-errors" or name == "total-get-bulk-count" or name == "total-get-bulk-errors" or name == "total-get-count" or name == "total-get-errors" or name == "total-item-count" or name == "total-list-count" or name == "total-list-errors" or name == "total-send-bytes-dropped" or name == "total-send-drops" or name == "total-send-errors" or name == "total-send-packets" or name == "total-sent-bytes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "avg-collection-time"):
                            self.avg_collection_time = value
                            self.avg_collection_time.value_namespace = name_space
                            self.avg_collection_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "cadence"):
                            self.cadence = value
                            self.cadence.value_namespace = name_space
                            self.cadence.value_namespace_prefix = name_space_prefix
                        if(value_path == "collection-method"):
                            self.collection_method = value
                            self.collection_method.value_namespace = name_space
                            self.collection_method.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-collection-time"):
                            self.max_collection_time = value
                            self.max_collection_time.value_namespace = name_space
                            self.max_collection_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "min-collection-time"):
                            self.min_collection_time = value
                            self.min_collection_time.value_namespace = name_space
                            self.min_collection_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "path"):
                            self.path = value
                            self.path.value_namespace = name_space
                            self.path.value_namespace_prefix = name_space_prefix
                        if(value_path == "status"):
                            self.status = value
                            self.status.value_namespace = name_space
                            self.status.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-collections"):
                            self.total_collections = value
                            self.total_collections.value_namespace = name_space
                            self.total_collections.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-collections-missed"):
                            self.total_collections_missed = value
                            self.total_collections_missed.value_namespace = name_space
                            self.total_collections_missed.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-datalist-count"):
                            self.total_datalist_count = value
                            self.total_datalist_count.value_namespace = name_space
                            self.total_datalist_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-datalist-errors"):
                            self.total_datalist_errors = value
                            self.total_datalist_errors.value_namespace = name_space
                            self.total_datalist_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-encode-errors"):
                            self.total_encode_errors = value
                            self.total_encode_errors.value_namespace = name_space
                            self.total_encode_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-encode-notready"):
                            self.total_encode_notready = value
                            self.total_encode_notready.value_namespace = name_space
                            self.total_encode_notready.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-finddata-count"):
                            self.total_finddata_count = value
                            self.total_finddata_count.value_namespace = name_space
                            self.total_finddata_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-finddata-errors"):
                            self.total_finddata_errors = value
                            self.total_finddata_errors.value_namespace = name_space
                            self.total_finddata_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-get-bulk-count"):
                            self.total_get_bulk_count = value
                            self.total_get_bulk_count.value_namespace = name_space
                            self.total_get_bulk_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-get-bulk-errors"):
                            self.total_get_bulk_errors = value
                            self.total_get_bulk_errors.value_namespace = name_space
                            self.total_get_bulk_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-get-count"):
                            self.total_get_count = value
                            self.total_get_count.value_namespace = name_space
                            self.total_get_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-get-errors"):
                            self.total_get_errors = value
                            self.total_get_errors.value_namespace = name_space
                            self.total_get_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-item-count"):
                            self.total_item_count = value
                            self.total_item_count.value_namespace = name_space
                            self.total_item_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-list-count"):
                            self.total_list_count = value
                            self.total_list_count.value_namespace = name_space
                            self.total_list_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-list-errors"):
                            self.total_list_errors = value
                            self.total_list_errors.value_namespace = name_space
                            self.total_list_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-send-bytes-dropped"):
                            self.total_send_bytes_dropped = value
                            self.total_send_bytes_dropped.value_namespace = name_space
                            self.total_send_bytes_dropped.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-send-drops"):
                            self.total_send_drops = value
                            self.total_send_drops.value_namespace = name_space
                            self.total_send_drops.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-send-errors"):
                            self.total_send_errors = value
                            self.total_send_errors.value_namespace = name_space
                            self.total_send_errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-send-packets"):
                            self.total_send_packets = value
                            self.total_send_packets.value_namespace = name_space
                            self.total_send_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-sent-bytes"):
                            self.total_sent_bytes = value
                            self.total_sent_bytes.value_namespace = name_space
                            self.total_sent_bytes.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.collection_path:
                        if (c.has_data()):
                            return True
                    for c in self.internal_collection_group:
                        if (c.has_data()):
                            return True
                    return (
                        self.avg_total_time.is_set or
                        self.cadence.is_set or
                        self.encoding.is_set or
                        self.id.is_set or
                        self.last_collection_end_time.is_set or
                        self.last_collection_start_time.is_set or
                        self.max_collection_time.is_set or
                        self.max_total_time.is_set or
                        self.min_collection_time.is_set or
                        self.min_total_time.is_set or
                        self.total_collections.is_set or
                        self.total_not_ready.is_set or
                        self.total_on_data_instances.is_set or
                        self.total_other_errors.is_set or
                        self.total_send_drops.is_set or
                        self.total_send_errors.is_set)

                def has_operation(self):
                    for c in self.collection_path:
                        if (c.has_operation()):
                            return True
                    for c in self.internal_collection_group:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.avg_total_time.yfilter != YFilter.not_set or
                        self.cadence.yfilter != YFilter.not_set or
                        self.encoding.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.last_collection_end_time.yfilter != YFilter.not_set or
                        self.last_collection_start_time.yfilter != YFilter.not_set or
                        self.max_collection_time.yfilter != YFilter.not_set or
                        self.max_total_time.yfilter != YFilter.not_set or
                        self.min_collection_time.yfilter != YFilter.not_set or
                        self.min_total_time.yfilter != YFilter.not_set or
                        self.total_collections.yfilter != YFilter.not_set or
                        self.total_not_ready.yfilter != YFilter.not_set or
                        self.total_on_data_instances.yfilter != YFilter.not_set or
                        self.total_other_errors.yfilter != YFilter.not_set or
                        self.total_send_drops.yfilter != YFilter.not_set or
                        self.total_send_errors.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "collection-group" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.avg_total_time.is_set or self.avg_total_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.avg_total_time.get_name_leafdata())
                    if (self.cadence.is_set or self.cadence.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cadence.get_name_leafdata())
                    if (self.encoding.is_set or self.encoding.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.encoding.get_name_leafdata())
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.last_collection_end_time.is_set or self.last_collection_end_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_collection_end_time.get_name_leafdata())
                    if (self.last_collection_start_time.is_set or self.last_collection_start_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_collection_start_time.get_name_leafdata())
                    if (self.max_collection_time.is_set or self.max_collection_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_collection_time.get_name_leafdata())
                    if (self.max_total_time.is_set or self.max_total_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_total_time.get_name_leafdata())
                    if (self.min_collection_time.is_set or self.min_collection_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_collection_time.get_name_leafdata())
                    if (self.min_total_time.is_set or self.min_total_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.min_total_time.get_name_leafdata())
                    if (self.total_collections.is_set or self.total_collections.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_collections.get_name_leafdata())
                    if (self.total_not_ready.is_set or self.total_not_ready.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_not_ready.get_name_leafdata())
                    if (self.total_on_data_instances.is_set or self.total_on_data_instances.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_on_data_instances.get_name_leafdata())
                    if (self.total_other_errors.is_set or self.total_other_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_other_errors.get_name_leafdata())
                    if (self.total_send_drops.is_set or self.total_send_drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_send_drops.get_name_leafdata())
                    if (self.total_send_errors.is_set or self.total_send_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_send_errors.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "collection-path"):
                        for c in self.collection_path:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.collection_path.append(c)
                        return c

                    if (child_yang_name == "internal-collection-group"):
                        for c in self.internal_collection_group:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.internal_collection_group.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "collection-path" or name == "internal-collection-group" or name == "avg-total-time" or name == "cadence" or name == "encoding" or name == "id" or name == "last-collection-end-time" or name == "last-collection-start-time" or name == "max-collection-time" or name == "max-total-time" or name == "min-collection-time" or name == "min-total-time" or name == "total-collections" or name == "total-not-ready" or name == "total-on-data-instances" or name == "total-other-errors" or name == "total-send-drops" or name == "total-send-errors"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "avg-total-time"):
                        self.avg_total_time = value
                        self.avg_total_time.value_namespace = name_space
                        self.avg_total_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "cadence"):
                        self.cadence = value
                        self.cadence.value_namespace = name_space
                        self.cadence.value_namespace_prefix = name_space_prefix
                    if(value_path == "encoding"):
                        self.encoding = value
                        self.encoding.value_namespace = name_space
                        self.encoding.value_namespace_prefix = name_space_prefix
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-collection-end-time"):
                        self.last_collection_end_time = value
                        self.last_collection_end_time.value_namespace = name_space
                        self.last_collection_end_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-collection-start-time"):
                        self.last_collection_start_time = value
                        self.last_collection_start_time.value_namespace = name_space
                        self.last_collection_start_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-collection-time"):
                        self.max_collection_time = value
                        self.max_collection_time.value_namespace = name_space
                        self.max_collection_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-total-time"):
                        self.max_total_time = value
                        self.max_total_time.value_namespace = name_space
                        self.max_total_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-collection-time"):
                        self.min_collection_time = value
                        self.min_collection_time.value_namespace = name_space
                        self.min_collection_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "min-total-time"):
                        self.min_total_time = value
                        self.min_total_time.value_namespace = name_space
                        self.min_total_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-collections"):
                        self.total_collections = value
                        self.total_collections.value_namespace = name_space
                        self.total_collections.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-not-ready"):
                        self.total_not_ready = value
                        self.total_not_ready.value_namespace = name_space
                        self.total_not_ready.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-on-data-instances"):
                        self.total_on_data_instances = value
                        self.total_on_data_instances.value_namespace = name_space
                        self.total_on_data_instances.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-other-errors"):
                        self.total_other_errors = value
                        self.total_other_errors.value_namespace = name_space
                        self.total_other_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-send-drops"):
                        self.total_send_drops = value
                        self.total_send_drops.value_namespace = name_space
                        self.total_send_drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-send-errors"):
                        self.total_send_errors = value
                        self.total_send_errors.value_namespace = name_space
                        self.total_send_errors.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.collection_group:
                    if (c.has_data()):
                        return True
                return (
                    self.subscription_id.is_set or
                    (self.subscription is not None and self.subscription.has_data()))

            def has_operation(self):
                for c in self.collection_group:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.subscription_id.yfilter != YFilter.not_set or
                    (self.subscription is not None and self.subscription.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "subscription" + "[subscription-id='" + self.subscription_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/subscriptions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.subscription_id.is_set or self.subscription_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.subscription_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "collection-group"):
                    for c in self.collection_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.collection_group.append(c)
                    return c

                if (child_yang_name == "subscription"):
                    if (self.subscription is None):
                        self.subscription = TelemetryModelDriven.Subscriptions.Subscription.Subscription()
                        self.subscription.parent = self
                        self._children_name_map["subscription"] = "subscription"
                    return self.subscription

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "collection-group" or name == "subscription" or name == "subscription-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "subscription-id"):
                    self.subscription_id = value
                    self.subscription_id.value_namespace = name_space
                    self.subscription_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.subscription:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.subscription:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "subscriptions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "subscription"):
                for c in self.subscription:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TelemetryModelDriven.Subscriptions.Subscription()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.subscription.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "subscription"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.sensor_group = YList(self)

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
                        super(TelemetryModelDriven.SensorGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TelemetryModelDriven.SensorGroups, self).__setattr__(name, value)


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

                self.sensor_group_id = YLeaf(YType.str, "sensor-group-id")

                self.configured = YLeaf(YType.uint32, "configured")

                self.id = YLeaf(YType.str, "id")

                self.sensor_path = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("sensor_group_id",
                                "configured",
                                "id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TelemetryModelDriven.SensorGroups.SensorGroup, self).__setattr__(name, value)


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

                    self.path = YLeaf(YType.str, "path")

                    self.state = YLeaf(YType.boolean, "state")

                    self.status_str = YLeaf(YType.str, "status-str")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("path",
                                    "state",
                                    "status_str") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.path.is_set or
                        self.state.is_set or
                        self.status_str.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.path.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.status_str.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sensor-path" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.status_str.is_set or self.status_str.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.status_str.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "path" or name == "state" or name == "status-str"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "path"):
                        self.path = value
                        self.path.value_namespace = name_space
                        self.path.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "status-str"):
                        self.status_str = value
                        self.status_str.value_namespace = name_space
                        self.status_str.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.sensor_path:
                    if (c.has_data()):
                        return True
                return (
                    self.sensor_group_id.is_set or
                    self.configured.is_set or
                    self.id.is_set)

            def has_operation(self):
                for c in self.sensor_path:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.sensor_group_id.yfilter != YFilter.not_set or
                    self.configured.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "sensor-group" + "[sensor-group-id='" + self.sensor_group_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/sensor-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.sensor_group_id.is_set or self.sensor_group_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sensor_group_id.get_name_leafdata())
                if (self.configured.is_set or self.configured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.configured.get_name_leafdata())
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sensor-path"):
                    for c in self.sensor_path:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.sensor_path.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sensor-path" or name == "sensor-group-id" or name == "configured" or name == "id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "sensor-group-id"):
                    self.sensor_group_id = value
                    self.sensor_group_id.value_namespace = name_space
                    self.sensor_group_id.value_namespace_prefix = name_space_prefix
                if(value_path == "configured"):
                    self.configured = value
                    self.configured.value_namespace = name_space
                    self.configured.value_namespace_prefix = name_space_prefix
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.sensor_group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.sensor_group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sensor-groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "sensor-group"):
                for c in self.sensor_group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TelemetryModelDriven.SensorGroups.SensorGroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.sensor_group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "sensor-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.destinations is not None and self.destinations.has_data()) or
            (self.sensor_groups is not None and self.sensor_groups.has_data()) or
            (self.subscriptions is not None and self.subscriptions.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.destinations is not None and self.destinations.has_operation()) or
            (self.sensor_groups is not None and self.sensor_groups.has_operation()) or
            (self.subscriptions is not None and self.subscriptions.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven" + path_buffer

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

        if (child_yang_name == "destinations"):
            if (self.destinations is None):
                self.destinations = TelemetryModelDriven.Destinations()
                self.destinations.parent = self
                self._children_name_map["destinations"] = "destinations"
            return self.destinations

        if (child_yang_name == "sensor-groups"):
            if (self.sensor_groups is None):
                self.sensor_groups = TelemetryModelDriven.SensorGroups()
                self.sensor_groups.parent = self
                self._children_name_map["sensor_groups"] = "sensor-groups"
            return self.sensor_groups

        if (child_yang_name == "subscriptions"):
            if (self.subscriptions is None):
                self.subscriptions = TelemetryModelDriven.Subscriptions()
                self.subscriptions.parent = self
                self._children_name_map["subscriptions"] = "subscriptions"
            return self.subscriptions

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "destinations" or name == "sensor-groups" or name == "subscriptions"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TelemetryModelDriven()
        return self._top_entity

