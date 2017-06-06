""" Cisco_IOS_XR_telemetry_model_driven_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR telemetry\-model\-driven package operational data.

This module contains definitions
for the following management objects\:
  telemetry\-model\-driven\: Telemetry operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MdtEncodingEnumEnum(Enum):
    """
    MdtEncodingEnumEnum

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

    not_set = 0

    gpb = 2

    self_describing_gpb = 3

    json = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
        return meta._meta_table['MdtEncodingEnumEnum']


class MdtInternalPathStatusEnum(Enum):
    """
    MdtInternalPathStatusEnum

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

    active = 0

    internal_err = 1

    plugin_active = 2

    plugin_not_initialized = 3

    plugin_invalid_cadence = 4

    plugin_err = 5

    filter_err = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
        return meta._meta_table['MdtInternalPathStatusEnum']


class MdtIpEnum(Enum):
    """
    MdtIpEnum

    IP Type

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
        return meta._meta_table['MdtIpEnum']


class MdtTransportEnumEnum(Enum):
    """
    MdtTransportEnumEnum

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

    not_set = 0

    grpc = 1

    tcp = 2

    udp = 3

    dialin = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
        return meta._meta_table['MdtTransportEnumEnum']



class TelemetryModelDriven(object):
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
    _revision = '2016-07-14'

    def __init__(self):
        self.destinations = TelemetryModelDriven.Destinations()
        self.destinations.parent = self
        self.sensor_groups = TelemetryModelDriven.SensorGroups()
        self.sensor_groups.parent = self
        self.subscriptions = TelemetryModelDriven.Subscriptions()
        self.subscriptions.parent = self


    class Destinations(object):
        """
        Telemetry Destinations
        
        .. attribute:: destination
        
        	Telemetry Destination
        	**type**\: list of    :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2016-07-14'

        def __init__(self):
            self.parent = None
            self.destination = YList()
            self.destination.parent = self
            self.destination.name = 'destination'


        class Destination(object):
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
            	**type**\: list of    :py:class:`Destination_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_>`
            
            .. attribute:: id
            
            	Destination Group name
            	**type**\:  str
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2016-07-14'

            def __init__(self):
                self.parent = None
                self.destination_id = None
                self.configured = None
                self.destination = YList()
                self.destination.parent = self
                self.destination.name = 'destination'
                self.id = None


            class Destination_(object):
                """
                list of destinations defined in this group
                
                .. attribute:: collection_group
                
                	List of collection groups for this destination group
                	**type**\: list of    :py:class:`CollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup>`
                
                .. attribute:: destination
                
                	Destination
                	**type**\:   :py:class:`Destination__ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.Destination__>`
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2016-07-14'

                def __init__(self):
                    self.parent = None
                    self.collection_group = YList()
                    self.collection_group.parent = self
                    self.collection_group.name = 'collection_group'
                    self.destination = TelemetryModelDriven.Destinations.Destination.Destination_.Destination__()
                    self.destination.parent = self


                class Destination__(object):
                    """
                    Destination
                    
                    .. attribute:: dest_ip_address
                    
                    	Destination IP Address
                    	**type**\:   :py:class:`DestIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress>`
                    
                    .. attribute:: dest_port
                    
                    	Destination Port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: encoding
                    
                    	Destination group encoding
                    	**type**\:   :py:class:`MdtEncodingEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnumEnum>`
                    
                    .. attribute:: id
                    
                    	Destination Id
                    	**type**\:  str
                    
                    .. attribute:: last_collection_time
                    
                    	Timestamp of the last collection
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: state
                    
                    	State of streaming on this destination
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
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
                    	**type**\:   :py:class:`MdtTransportEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtTransportEnumEnum>`
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2016-07-14'

                    def __init__(self):
                        self.parent = None
                        self.dest_ip_address = TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress()
                        self.dest_ip_address.parent = self
                        self.dest_port = None
                        self.encoding = None
                        self.id = None
                        self.last_collection_time = None
                        self.state = None
                        self.sub_id = YLeafList()
                        self.sub_id.parent = self
                        self.sub_id.name = 'sub_id'
                        self.sub_id_str = None
                        self.tls = None
                        self.tls_host = None
                        self.total_num_of_bytes_sent = None
                        self.total_num_of_packets_sent = None
                        self.transport = None


                    class DestIpAddress(object):
                        """
                        Destination IP Address
                        
                        .. attribute:: ip_type
                        
                        	IPType
                        	**type**\:   :py:class:`MdtIpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtIpEnum>`
                        
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
                        _revision = '2016-07-14'

                        def __init__(self):
                            self.parent = None
                            self.ip_type = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:dest-ip-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.ip_type is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                            return meta._meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.Destination__.DestIpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:destination'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.dest_ip_address is not None and self.dest_ip_address._has_data():
                            return True

                        if self.dest_port is not None:
                            return True

                        if self.encoding is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.last_collection_time is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.sub_id is not None:
                            for child in self.sub_id:
                                if child is not None:
                                    return True

                        if self.sub_id_str is not None:
                            return True

                        if self.tls is not None:
                            return True

                        if self.tls_host is not None:
                            return True

                        if self.total_num_of_bytes_sent is not None:
                            return True

                        if self.total_num_of_packets_sent is not None:
                            return True

                        if self.transport is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                        return meta._meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.Destination__']['meta_info']


                class CollectionGroup(object):
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
                    	**type**\: list of    :py:class:`CollectionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath>`
                    
                    .. attribute:: encoding
                    
                    	Destination group encoding
                    	**type**\:   :py:class:`MdtEncodingEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnumEnum>`
                    
                    .. attribute:: id
                    
                    	Collection Group id
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: internal_collection_group
                    
                    	Array of information for sysdb paths within collection group
                    	**type**\: list of    :py:class:`InternalCollectionGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup>`
                    
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
                    _revision = '2016-07-14'

                    def __init__(self):
                        self.parent = None
                        self.avg_total_time = None
                        self.cadence = None
                        self.collection_path = YList()
                        self.collection_path.parent = self
                        self.collection_path.name = 'collection_path'
                        self.encoding = None
                        self.id = None
                        self.internal_collection_group = YList()
                        self.internal_collection_group.parent = self
                        self.internal_collection_group.name = 'internal_collection_group'
                        self.last_collection_end_time = None
                        self.last_collection_start_time = None
                        self.max_collection_time = None
                        self.max_total_time = None
                        self.min_collection_time = None
                        self.min_total_time = None
                        self.total_collections = None
                        self.total_not_ready = None
                        self.total_other_errors = None
                        self.total_send_drops = None
                        self.total_send_errors = None


                    class CollectionPath(object):
                        """
                        Array of information for sensor paths within
                        collection group
                        
                        .. attribute:: path
                        
                        	Sensor Path
                        	**type**\:  str
                        
                        .. attribute:: state
                        
                        	State, if sensor path is resolved or not
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: status_str
                        
                        	Error str, if there are any errors resolving the sensor path
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2016-07-14'

                        def __init__(self):
                            self.parent = None
                            self.path = None
                            self.state = None
                            self.status_str = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:collection-path'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.path is not None:
                                return True

                            if self.state is not None:
                                return True

                            if self.status_str is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                            return meta._meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.CollectionPath']['meta_info']


                    class InternalCollectionGroup(object):
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
                        	**type**\:   :py:class:`MdtInternalPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtInternalPathStatusEnum>`
                        
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
                        _revision = '2016-07-14'

                        def __init__(self):
                            self.parent = None
                            self.avg_collection_time = None
                            self.cadence = None
                            self.collection_method = None
                            self.max_collection_time = None
                            self.min_collection_time = None
                            self.path = None
                            self.status = None
                            self.total_collections = None
                            self.total_collections_missed = None
                            self.total_datalist_count = None
                            self.total_datalist_errors = None
                            self.total_encode_errors = None
                            self.total_encode_notready = None
                            self.total_finddata_count = None
                            self.total_finddata_errors = None
                            self.total_get_bulk_count = None
                            self.total_get_bulk_errors = None
                            self.total_get_count = None
                            self.total_get_errors = None
                            self.total_item_count = None
                            self.total_list_count = None
                            self.total_list_errors = None
                            self.total_send_bytes_dropped = None
                            self.total_send_drops = None
                            self.total_send_errors = None
                            self.total_send_packets = None
                            self.total_sent_bytes = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:internal-collection-group'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.avg_collection_time is not None:
                                return True

                            if self.cadence is not None:
                                return True

                            if self.collection_method is not None:
                                return True

                            if self.max_collection_time is not None:
                                return True

                            if self.min_collection_time is not None:
                                return True

                            if self.path is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.total_collections is not None:
                                return True

                            if self.total_collections_missed is not None:
                                return True

                            if self.total_datalist_count is not None:
                                return True

                            if self.total_datalist_errors is not None:
                                return True

                            if self.total_encode_errors is not None:
                                return True

                            if self.total_encode_notready is not None:
                                return True

                            if self.total_finddata_count is not None:
                                return True

                            if self.total_finddata_errors is not None:
                                return True

                            if self.total_get_bulk_count is not None:
                                return True

                            if self.total_get_bulk_errors is not None:
                                return True

                            if self.total_get_count is not None:
                                return True

                            if self.total_get_errors is not None:
                                return True

                            if self.total_item_count is not None:
                                return True

                            if self.total_list_count is not None:
                                return True

                            if self.total_list_errors is not None:
                                return True

                            if self.total_send_bytes_dropped is not None:
                                return True

                            if self.total_send_drops is not None:
                                return True

                            if self.total_send_errors is not None:
                                return True

                            if self.total_send_packets is not None:
                                return True

                            if self.total_sent_bytes is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                            return meta._meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup.InternalCollectionGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:collection-group'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg_total_time is not None:
                            return True

                        if self.cadence is not None:
                            return True

                        if self.collection_path is not None:
                            for child_ref in self.collection_path:
                                if child_ref._has_data():
                                    return True

                        if self.encoding is not None:
                            return True

                        if self.id is not None:
                            return True

                        if self.internal_collection_group is not None:
                            for child_ref in self.internal_collection_group:
                                if child_ref._has_data():
                                    return True

                        if self.last_collection_end_time is not None:
                            return True

                        if self.last_collection_start_time is not None:
                            return True

                        if self.max_collection_time is not None:
                            return True

                        if self.max_total_time is not None:
                            return True

                        if self.min_collection_time is not None:
                            return True

                        if self.min_total_time is not None:
                            return True

                        if self.total_collections is not None:
                            return True

                        if self.total_not_ready is not None:
                            return True

                        if self.total_other_errors is not None:
                            return True

                        if self.total_send_drops is not None:
                            return True

                        if self.total_send_errors is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                        return meta._meta_table['TelemetryModelDriven.Destinations.Destination.Destination_.CollectionGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:destination'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.collection_group is not None:
                        for child_ref in self.collection_group:
                            if child_ref._has_data():
                                return True

                    if self.destination is not None and self.destination._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                    return meta._meta_table['TelemetryModelDriven.Destinations.Destination.Destination_']['meta_info']

            @property
            def _common_path(self):
                if self.destination_id is None:
                    raise YPYModelError('Key property destination_id is None')

                return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-oper:destinations/Cisco-IOS-XR-telemetry-model-driven-oper:destination[Cisco-IOS-XR-telemetry-model-driven-oper:destination-id = ' + str(self.destination_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.destination_id is not None:
                    return True

                if self.configured is not None:
                    return True

                if self.destination is not None:
                    for child_ref in self.destination:
                        if child_ref._has_data():
                            return True

                if self.id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                return meta._meta_table['TelemetryModelDriven.Destinations.Destination']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-oper:destinations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.destination is not None:
                for child_ref in self.destination:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
            return meta._meta_table['TelemetryModelDriven.Destinations']['meta_info']


    class Subscriptions(object):
        """
        Telemetry Subscriptions
        
        .. attribute:: subscription
        
        	Telemetry Subscription
        	**type**\: list of    :py:class:`Subscription <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2016-07-14'

        def __init__(self):
            self.parent = None
            self.subscription = YList()
            self.subscription.parent = self
            self.subscription.name = 'subscription'


        class Subscription(object):
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
            	**type**\:   :py:class:`Subscription_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_>`
            
            .. attribute:: total_num_of_bytes_sent
            
            	Total number of bytes sent for this subscription
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: total_num_of_packets_sent
            
            	Total number of packets sent for this subscription
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'telemetry-model-driven-oper'
            _revision = '2016-07-14'

            def __init__(self):
                self.parent = None
                self.subscription_id = None
                self.collection_group = YList()
                self.collection_group.parent = self
                self.collection_group.name = 'collection_group'
                self.subscription = TelemetryModelDriven.Subscriptions.Subscription.Subscription_()
                self.subscription.parent = self
                self.total_num_of_bytes_sent = None
                self.total_num_of_packets_sent = None


            class Subscription_(object):
                """
                Subscription
                
                .. attribute:: destination_grp
                
                	Array of destinations within a subscription
                	**type**\: list of    :py:class:`DestinationGrp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp>`
                
                .. attribute:: id
                
                	Collection Subscription name
                	**type**\:  str
                
                .. attribute:: sensor_profile
                
                	List of sensor groups within a subscription
                	**type**\: list of    :py:class:`SensorProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile>`
                
                .. attribute:: state
                
                	Subscription state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2016-07-14'

                def __init__(self):
                    self.parent = None
                    self.destination_grp = YList()
                    self.destination_grp.parent = self
                    self.destination_grp.name = 'destination_grp'
                    self.id = None
                    self.sensor_profile = YList()
                    self.sensor_profile.parent = self
                    self.sensor_profile.name = 'sensor_profile'
                    self.state = None


                class SensorProfile(object):
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
                    	**type**\:   :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup>`
                    
                    .. attribute:: suppress_redundant
                    
                    	Suppress Redundant
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2016-07-14'

                    def __init__(self):
                        self.parent = None
                        self.heartbeat_interval = None
                        self.sample_interval = None
                        self.sensor_group = TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup()
                        self.sensor_group.parent = self
                        self.suppress_redundant = None


                    class SensorGroup(object):
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
                        	**type**\: list of    :py:class:`SensorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath>`
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2016-07-14'

                        def __init__(self):
                            self.parent = None
                            self.configured = None
                            self.id = None
                            self.sensor_path = YList()
                            self.sensor_path.parent = self
                            self.sensor_path.name = 'sensor_path'


                        class SensorPath(object):
                            """
                            Array of information for sensor paths within
                            sensor group
                            
                            .. attribute:: path
                            
                            	Sensor Path
                            	**type**\:  str
                            
                            .. attribute:: state
                            
                            	State, if sensor path is resolved or not
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: status_str
                            
                            	Error str, if there are any errors resolving the sensor path
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'telemetry-model-driven-oper'
                            _revision = '2016-07-14'

                            def __init__(self):
                                self.parent = None
                                self.path = None
                                self.state = None
                                self.status_str = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-path'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.path is not None:
                                    return True

                                if self.state is not None:
                                    return True

                                if self.status_str is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                                return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup.SensorPath']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-group'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.configured is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.sensor_path is not None:
                                for child_ref in self.sensor_path:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                            return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile.SensorGroup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-profile'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.heartbeat_interval is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sensor_group is not None and self.sensor_group._has_data():
                            return True

                        if self.suppress_redundant is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                        return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.SensorProfile']['meta_info']


                class DestinationGrp(object):
                    """
                    Array of destinations within a subscription
                    
                    .. attribute:: configured
                    
                    	Set if this is configured destination group
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination
                    
                    	list of destinations defined in this group
                    	**type**\: list of    :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination>`
                    
                    .. attribute:: id
                    
                    	Destination Group name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2016-07-14'

                    def __init__(self):
                        self.parent = None
                        self.configured = None
                        self.destination = YList()
                        self.destination.parent = self
                        self.destination.name = 'destination'
                        self.id = None


                    class Destination(object):
                        """
                        list of destinations defined in this group
                        
                        .. attribute:: dest_ip_address
                        
                        	Destination IP Address
                        	**type**\:   :py:class:`DestIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress>`
                        
                        .. attribute:: dest_port
                        
                        	Destination Port number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: encoding
                        
                        	Destination group encoding
                        	**type**\:   :py:class:`MdtEncodingEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnumEnum>`
                        
                        .. attribute:: id
                        
                        	Destination Id
                        	**type**\:  str
                        
                        .. attribute:: last_collection_time
                        
                        	Timestamp of the last collection
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: state
                        
                        	State of streaming on this destination
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
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
                        	**type**\:   :py:class:`MdtTransportEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtTransportEnumEnum>`
                        
                        

                        """

                        _prefix = 'telemetry-model-driven-oper'
                        _revision = '2016-07-14'

                        def __init__(self):
                            self.parent = None
                            self.dest_ip_address = TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress()
                            self.dest_ip_address.parent = self
                            self.dest_port = None
                            self.encoding = None
                            self.id = None
                            self.last_collection_time = None
                            self.state = None
                            self.sub_id = YLeafList()
                            self.sub_id.parent = self
                            self.sub_id.name = 'sub_id'
                            self.sub_id_str = None
                            self.tls = None
                            self.tls_host = None
                            self.total_num_of_bytes_sent = None
                            self.total_num_of_packets_sent = None
                            self.transport = None


                        class DestIpAddress(object):
                            """
                            Destination IP Address
                            
                            .. attribute:: ip_type
                            
                            	IPType
                            	**type**\:   :py:class:`MdtIpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtIpEnum>`
                            
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
                            _revision = '2016-07-14'

                            def __init__(self):
                                self.parent = None
                                self.ip_type = None
                                self.ipv4_address = None
                                self.ipv6_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:dest-ip-address'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.ip_type is not None:
                                    return True

                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                                return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination.DestIpAddress']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:destination'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.dest_ip_address is not None and self.dest_ip_address._has_data():
                                return True

                            if self.dest_port is not None:
                                return True

                            if self.encoding is not None:
                                return True

                            if self.id is not None:
                                return True

                            if self.last_collection_time is not None:
                                return True

                            if self.state is not None:
                                return True

                            if self.sub_id is not None:
                                for child in self.sub_id:
                                    if child is not None:
                                        return True

                            if self.sub_id_str is not None:
                                return True

                            if self.tls is not None:
                                return True

                            if self.tls_host is not None:
                                return True

                            if self.total_num_of_bytes_sent is not None:
                                return True

                            if self.total_num_of_packets_sent is not None:
                                return True

                            if self.transport is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                            return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp.Destination']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:destination-grp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.configured is not None:
                            return True

                        if self.destination is not None:
                            for child_ref in self.destination:
                                if child_ref._has_data():
                                    return True

                        if self.id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                        return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_.DestinationGrp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:subscription'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.destination_grp is not None:
                        for child_ref in self.destination_grp:
                            if child_ref._has_data():
                                return True

                    if self.id is not None:
                        return True

                    if self.sensor_profile is not None:
                        for child_ref in self.sensor_profile:
                            if child_ref._has_data():
                                return True

                    if self.state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                    return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.Subscription_']['meta_info']


            class CollectionGroup(object):
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
                	**type**\:   :py:class:`MdtEncodingEnumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtEncodingEnumEnum>`
                
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
                _revision = '2016-07-14'

                def __init__(self):
                    self.parent = None
                    self.avg_total_time = None
                    self.cadence = None
                    self.collection_path = YList()
                    self.collection_path.parent = self
                    self.collection_path.name = 'collection_path'
                    self.encoding = None
                    self.id = None
                    self.internal_collection_group = YList()
                    self.internal_collection_group.parent = self
                    self.internal_collection_group.name = 'internal_collection_group'
                    self.last_collection_end_time = None
                    self.last_collection_start_time = None
                    self.max_collection_time = None
                    self.max_total_time = None
                    self.min_collection_time = None
                    self.min_total_time = None
                    self.total_collections = None
                    self.total_not_ready = None
                    self.total_other_errors = None
                    self.total_send_drops = None
                    self.total_send_errors = None


                class CollectionPath(object):
                    """
                    Array of information for sensor paths within
                    collection group
                    
                    .. attribute:: path
                    
                    	Sensor Path
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	State, if sensor path is resolved or not
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: status_str
                    
                    	Error str, if there are any errors resolving the sensor path
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'telemetry-model-driven-oper'
                    _revision = '2016-07-14'

                    def __init__(self):
                        self.parent = None
                        self.path = None
                        self.state = None
                        self.status_str = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:collection-path'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.path is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.status_str is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                        return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.CollectionPath']['meta_info']


                class InternalCollectionGroup(object):
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
                    	**type**\:   :py:class:`MdtInternalPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.MdtInternalPathStatusEnum>`
                    
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
                    _revision = '2016-07-14'

                    def __init__(self):
                        self.parent = None
                        self.avg_collection_time = None
                        self.cadence = None
                        self.collection_method = None
                        self.max_collection_time = None
                        self.min_collection_time = None
                        self.path = None
                        self.status = None
                        self.total_collections = None
                        self.total_collections_missed = None
                        self.total_datalist_count = None
                        self.total_datalist_errors = None
                        self.total_encode_errors = None
                        self.total_encode_notready = None
                        self.total_finddata_count = None
                        self.total_finddata_errors = None
                        self.total_get_bulk_count = None
                        self.total_get_bulk_errors = None
                        self.total_get_count = None
                        self.total_get_errors = None
                        self.total_item_count = None
                        self.total_list_count = None
                        self.total_list_errors = None
                        self.total_send_bytes_dropped = None
                        self.total_send_drops = None
                        self.total_send_errors = None
                        self.total_send_packets = None
                        self.total_sent_bytes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:internal-collection-group'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.avg_collection_time is not None:
                            return True

                        if self.cadence is not None:
                            return True

                        if self.collection_method is not None:
                            return True

                        if self.max_collection_time is not None:
                            return True

                        if self.min_collection_time is not None:
                            return True

                        if self.path is not None:
                            return True

                        if self.status is not None:
                            return True

                        if self.total_collections is not None:
                            return True

                        if self.total_collections_missed is not None:
                            return True

                        if self.total_datalist_count is not None:
                            return True

                        if self.total_datalist_errors is not None:
                            return True

                        if self.total_encode_errors is not None:
                            return True

                        if self.total_encode_notready is not None:
                            return True

                        if self.total_finddata_count is not None:
                            return True

                        if self.total_finddata_errors is not None:
                            return True

                        if self.total_get_bulk_count is not None:
                            return True

                        if self.total_get_bulk_errors is not None:
                            return True

                        if self.total_get_count is not None:
                            return True

                        if self.total_get_errors is not None:
                            return True

                        if self.total_item_count is not None:
                            return True

                        if self.total_list_count is not None:
                            return True

                        if self.total_list_errors is not None:
                            return True

                        if self.total_send_bytes_dropped is not None:
                            return True

                        if self.total_send_drops is not None:
                            return True

                        if self.total_send_errors is not None:
                            return True

                        if self.total_send_packets is not None:
                            return True

                        if self.total_sent_bytes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                        return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup.InternalCollectionGroup']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:collection-group'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.avg_total_time is not None:
                        return True

                    if self.cadence is not None:
                        return True

                    if self.collection_path is not None:
                        for child_ref in self.collection_path:
                            if child_ref._has_data():
                                return True

                    if self.encoding is not None:
                        return True

                    if self.id is not None:
                        return True

                    if self.internal_collection_group is not None:
                        for child_ref in self.internal_collection_group:
                            if child_ref._has_data():
                                return True

                    if self.last_collection_end_time is not None:
                        return True

                    if self.last_collection_start_time is not None:
                        return True

                    if self.max_collection_time is not None:
                        return True

                    if self.max_total_time is not None:
                        return True

                    if self.min_collection_time is not None:
                        return True

                    if self.min_total_time is not None:
                        return True

                    if self.total_collections is not None:
                        return True

                    if self.total_not_ready is not None:
                        return True

                    if self.total_other_errors is not None:
                        return True

                    if self.total_send_drops is not None:
                        return True

                    if self.total_send_errors is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                    return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription.CollectionGroup']['meta_info']

            @property
            def _common_path(self):
                if self.subscription_id is None:
                    raise YPYModelError('Key property subscription_id is None')

                return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-oper:subscriptions/Cisco-IOS-XR-telemetry-model-driven-oper:subscription[Cisco-IOS-XR-telemetry-model-driven-oper:subscription-id = ' + str(self.subscription_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.subscription_id is not None:
                    return True

                if self.collection_group is not None:
                    for child_ref in self.collection_group:
                        if child_ref._has_data():
                            return True

                if self.subscription is not None and self.subscription._has_data():
                    return True

                if self.total_num_of_bytes_sent is not None:
                    return True

                if self.total_num_of_packets_sent is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                return meta._meta_table['TelemetryModelDriven.Subscriptions.Subscription']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-oper:subscriptions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.subscription is not None:
                for child_ref in self.subscription:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
            return meta._meta_table['TelemetryModelDriven.Subscriptions']['meta_info']


    class SensorGroups(object):
        """
        Telemetry Sensor Groups
        
        .. attribute:: sensor_group
        
        	Telemetry Sensor Groups
        	**type**\: list of    :py:class:`SensorGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_telemetry_model_driven_oper.TelemetryModelDriven.SensorGroups.SensorGroup>`
        
        

        """

        _prefix = 'telemetry-model-driven-oper'
        _revision = '2016-07-14'

        def __init__(self):
            self.parent = None
            self.sensor_group = YList()
            self.sensor_group.parent = self
            self.sensor_group.name = 'sensor_group'


        class SensorGroup(object):
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
            _revision = '2016-07-14'

            def __init__(self):
                self.parent = None
                self.sensor_group_id = None
                self.configured = None
                self.id = None
                self.sensor_path = YList()
                self.sensor_path.parent = self
                self.sensor_path.name = 'sensor_path'


            class SensorPath(object):
                """
                Array of information for sensor paths within
                sensor group
                
                .. attribute:: path
                
                	Sensor Path
                	**type**\:  str
                
                .. attribute:: state
                
                	State, if sensor path is resolved or not
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: status_str
                
                	Error str, if there are any errors resolving the sensor path
                	**type**\:  str
                
                

                """

                _prefix = 'telemetry-model-driven-oper'
                _revision = '2016-07-14'

                def __init__(self):
                    self.parent = None
                    self.path = None
                    self.state = None
                    self.status_str = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-path'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.path is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.status_str is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                    return meta._meta_table['TelemetryModelDriven.SensorGroups.SensorGroup.SensorPath']['meta_info']

            @property
            def _common_path(self):
                if self.sensor_group_id is None:
                    raise YPYModelError('Key property sensor_group_id is None')

                return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-groups/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-group[Cisco-IOS-XR-telemetry-model-driven-oper:sensor-group-id = ' + str(self.sensor_group_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sensor_group_id is not None:
                    return True

                if self.configured is not None:
                    return True

                if self.id is not None:
                    return True

                if self.sensor_path is not None:
                    for child_ref in self.sensor_path:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
                return meta._meta_table['TelemetryModelDriven.SensorGroups.SensorGroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven/Cisco-IOS-XR-telemetry-model-driven-oper:sensor-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.sensor_group is not None:
                for child_ref in self.sensor_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
            return meta._meta_table['TelemetryModelDriven.SensorGroups']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-telemetry-model-driven-oper:telemetry-model-driven'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.destinations is not None and self.destinations._has_data():
            return True

        if self.sensor_groups is not None and self.sensor_groups._has_data():
            return True

        if self.subscriptions is not None and self.subscriptions._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_telemetry_model_driven_oper as meta
        return meta._meta_table['TelemetryModelDriven']['meta_info']


