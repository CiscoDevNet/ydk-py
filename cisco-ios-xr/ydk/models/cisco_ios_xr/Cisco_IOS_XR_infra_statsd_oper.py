""" Cisco_IOS_XR_infra_statsd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package operational data.

This module contains definitions
for the following management objects\:
  infra\-statistics\: Statistics Infrastructure

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class InfraStatistics(Entity):
    """
    Statistics Infrastructure
    
    .. attribute:: interfaces
    
    	List of interfaces
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces>`
    
    

    """

    _prefix = 'infra-statsd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(InfraStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "infra-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-infra-statsd-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("interfaces", ("interfaces", InfraStatistics.Interfaces))])
        self._leafs = OrderedDict()

        self.interfaces = InfraStatistics.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-statsd-oper:infra-statistics"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(InfraStatistics, [], name, value)


    class Interfaces(Entity):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Statistics of an interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-statsd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(InfraStatistics.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "infra-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", InfraStatistics.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-oper:infra-statistics/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(InfraStatistics.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Statistics of an interface
            
            .. attribute:: interface_name  (key)
            
            	Name of the interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: cache
            
            	Cached stats data of interfaces
            	**type**\:  :py:class:`Cache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache>`
            
            .. attribute:: latest
            
            	Latest stats data of interfaces
            	**type**\:  :py:class:`Latest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest>`
            
            .. attribute:: total
            
            	Total stats data of interfaces
            	**type**\:  :py:class:`Total <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total>`
            
            .. attribute:: protocols
            
            	List of protocols
            	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols>`
            
            .. attribute:: interfaces_mib_counters
            
            	Set of interface counters as displayed by the InterfacesMIB
            	**type**\:  :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.InterfacesMibCounters>`
            
            .. attribute:: data_rate
            
            	Datarate information
            	**type**\:  :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.DataRate>`
            
            .. attribute:: generic_counters
            
            	Generic set of interface counters
            	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.GenericCounters>`
            
            

            """

            _prefix = 'infra-statsd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(InfraStatistics.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("cache", ("cache", InfraStatistics.Interfaces.Interface.Cache)), ("latest", ("latest", InfraStatistics.Interfaces.Interface.Latest)), ("total", ("total", InfraStatistics.Interfaces.Interface.Total)), ("protocols", ("protocols", InfraStatistics.Interfaces.Interface.Protocols)), ("interfaces-mib-counters", ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.InterfacesMibCounters)), ("data-rate", ("data_rate", InfraStatistics.Interfaces.Interface.DataRate)), ("generic-counters", ("generic_counters", InfraStatistics.Interfaces.Interface.GenericCounters))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.cache = InfraStatistics.Interfaces.Interface.Cache()
                self.cache.parent = self
                self._children_name_map["cache"] = "cache"

                self.latest = InfraStatistics.Interfaces.Interface.Latest()
                self.latest.parent = self
                self._children_name_map["latest"] = "latest"

                self.total = InfraStatistics.Interfaces.Interface.Total()
                self.total.parent = self
                self._children_name_map["total"] = "total"

                self.protocols = InfraStatistics.Interfaces.Interface.Protocols()
                self.protocols.parent = self
                self._children_name_map["protocols"] = "protocols"

                self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.InterfacesMibCounters()
                self.interfaces_mib_counters.parent = self
                self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"

                self.data_rate = InfraStatistics.Interfaces.Interface.DataRate()
                self.data_rate.parent = self
                self._children_name_map["data_rate"] = "data-rate"

                self.generic_counters = InfraStatistics.Interfaces.Interface.GenericCounters()
                self.generic_counters.parent = self
                self._children_name_map["generic_counters"] = "generic-counters"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-oper:infra-statistics/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(InfraStatistics.Interfaces.Interface, ['interface_name'], name, value)


            class Cache(Entity):
                """
                Cached stats data of interfaces
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:  :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters>`
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:  :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.GenericCounters>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Cache, self).__init__()

                    self.yang_name = "cache"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("protocols", ("protocols", InfraStatistics.Interfaces.Interface.Cache.Protocols)), ("interfaces-mib-counters", ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters)), ("data-rate", ("data_rate", InfraStatistics.Interfaces.Interface.Cache.DataRate)), ("generic-counters", ("generic_counters", InfraStatistics.Interfaces.Interface.Cache.GenericCounters))])
                    self._leafs = OrderedDict()

                    self.protocols = InfraStatistics.Interfaces.Interface.Cache.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"

                    self.data_rate = InfraStatistics.Interfaces.Interface.Cache.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Cache.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._segment_path = lambda: "cache"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache, [], name, value)


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("protocol", ("protocol", InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol))])
                        self._leafs = OrderedDict()

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  (key)
                        
                        	Name of the protocol
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['protocol_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('protocol_name', (YLeaf(YType.str, 'protocol-name'), ['str'])),
                                ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                                ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                                ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                                ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                                ('protocol', (YLeaf(YType.uint32, 'protocol'), ['int'])),
                                ('last_data_time', (YLeaf(YType.uint64, 'last-data-time'), ['int'])),
                                ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                                ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                                ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                                ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                            ])
                            self.protocol_name = None
                            self.bytes_received = None
                            self.packets_received = None
                            self.bytes_sent = None
                            self.packets_sent = None
                            self.protocol = None
                            self.last_data_time = None
                            self.input_data_rate = None
                            self.input_packet_rate = None
                            self.output_data_rate = None
                            self.output_packet_rate = None
                            self._segment_path = lambda: "protocol" + "[protocol-name='" + str(self.protocol_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, ['protocol_name', 'bytes_received', 'packets_received', 'bytes_sent', 'packets_sent', 'protocol', 'last_data_time', 'input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate'], name, value)


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "interfaces-mib-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.DataRate, self).__init__()

                        self.yang_name = "data-rate"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                            ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                            ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                            ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                            ('peak_input_data_rate', (YLeaf(YType.uint64, 'peak-input-data-rate'), ['int'])),
                            ('peak_input_packet_rate', (YLeaf(YType.uint64, 'peak-input-packet-rate'), ['int'])),
                            ('peak_output_data_rate', (YLeaf(YType.uint64, 'peak-output-data-rate'), ['int'])),
                            ('peak_output_packet_rate', (YLeaf(YType.uint64, 'peak-output-packet-rate'), ['int'])),
                            ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                            ('load_interval', (YLeaf(YType.uint32, 'load-interval'), ['int'])),
                            ('output_load', (YLeaf(YType.uint8, 'output-load'), ['int'])),
                            ('input_load', (YLeaf(YType.uint8, 'input-load'), ['int'])),
                            ('reliability', (YLeaf(YType.uint8, 'reliability'), ['int'])),
                        ])
                        self.input_data_rate = None
                        self.input_packet_rate = None
                        self.output_data_rate = None
                        self.output_packet_rate = None
                        self.peak_input_data_rate = None
                        self.peak_input_packet_rate = None
                        self.peak_output_data_rate = None
                        self.peak_output_packet_rate = None
                        self.bandwidth = None
                        self.load_interval = None
                        self.output_load = None
                        self.input_load = None
                        self.reliability = None
                        self._segment_path = lambda: "data-rate"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.DataRate, ['input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'bandwidth', 'load_interval', 'output_load', 'input_load', 'reliability'], name, value)


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "generic-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


            class Latest(Entity):
                """
                Latest stats data of interfaces
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:  :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters>`
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:  :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.GenericCounters>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Latest, self).__init__()

                    self.yang_name = "latest"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("protocols", ("protocols", InfraStatistics.Interfaces.Interface.Latest.Protocols)), ("interfaces-mib-counters", ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters)), ("data-rate", ("data_rate", InfraStatistics.Interfaces.Interface.Latest.DataRate)), ("generic-counters", ("generic_counters", InfraStatistics.Interfaces.Interface.Latest.GenericCounters))])
                    self._leafs = OrderedDict()

                    self.protocols = InfraStatistics.Interfaces.Interface.Latest.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"

                    self.data_rate = InfraStatistics.Interfaces.Interface.Latest.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Latest.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._segment_path = lambda: "latest"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest, [], name, value)


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("protocol", ("protocol", InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol))])
                        self._leafs = OrderedDict()

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  (key)
                        
                        	Name of the protocol
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['protocol_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('protocol_name', (YLeaf(YType.str, 'protocol-name'), ['str'])),
                                ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                                ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                                ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                                ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                                ('protocol', (YLeaf(YType.uint32, 'protocol'), ['int'])),
                                ('last_data_time', (YLeaf(YType.uint64, 'last-data-time'), ['int'])),
                                ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                                ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                                ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                                ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                            ])
                            self.protocol_name = None
                            self.bytes_received = None
                            self.packets_received = None
                            self.bytes_sent = None
                            self.packets_sent = None
                            self.protocol = None
                            self.last_data_time = None
                            self.input_data_rate = None
                            self.input_packet_rate = None
                            self.output_data_rate = None
                            self.output_packet_rate = None
                            self._segment_path = lambda: "protocol" + "[protocol-name='" + str(self.protocol_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, ['protocol_name', 'bytes_received', 'packets_received', 'bytes_sent', 'packets_sent', 'protocol', 'last_data_time', 'input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate'], name, value)


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "interfaces-mib-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.DataRate, self).__init__()

                        self.yang_name = "data-rate"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                            ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                            ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                            ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                            ('peak_input_data_rate', (YLeaf(YType.uint64, 'peak-input-data-rate'), ['int'])),
                            ('peak_input_packet_rate', (YLeaf(YType.uint64, 'peak-input-packet-rate'), ['int'])),
                            ('peak_output_data_rate', (YLeaf(YType.uint64, 'peak-output-data-rate'), ['int'])),
                            ('peak_output_packet_rate', (YLeaf(YType.uint64, 'peak-output-packet-rate'), ['int'])),
                            ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                            ('load_interval', (YLeaf(YType.uint32, 'load-interval'), ['int'])),
                            ('output_load', (YLeaf(YType.uint8, 'output-load'), ['int'])),
                            ('input_load', (YLeaf(YType.uint8, 'input-load'), ['int'])),
                            ('reliability', (YLeaf(YType.uint8, 'reliability'), ['int'])),
                        ])
                        self.input_data_rate = None
                        self.input_packet_rate = None
                        self.output_data_rate = None
                        self.output_packet_rate = None
                        self.peak_input_data_rate = None
                        self.peak_input_packet_rate = None
                        self.peak_output_data_rate = None
                        self.peak_output_packet_rate = None
                        self.bandwidth = None
                        self.load_interval = None
                        self.output_load = None
                        self.input_load = None
                        self.reliability = None
                        self._segment_path = lambda: "data-rate"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.DataRate, ['input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'bandwidth', 'load_interval', 'output_load', 'input_load', 'reliability'], name, value)


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "generic-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


            class Total(Entity):
                """
                Total stats data of interfaces
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:  :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:  :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters>`
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:  :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.GenericCounters>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Total, self).__init__()

                    self.yang_name = "total"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("protocols", ("protocols", InfraStatistics.Interfaces.Interface.Total.Protocols)), ("interfaces-mib-counters", ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters)), ("data-rate", ("data_rate", InfraStatistics.Interfaces.Interface.Total.DataRate)), ("generic-counters", ("generic_counters", InfraStatistics.Interfaces.Interface.Total.GenericCounters))])
                    self._leafs = OrderedDict()

                    self.protocols = InfraStatistics.Interfaces.Interface.Total.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"

                    self.data_rate = InfraStatistics.Interfaces.Interface.Total.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Total.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._segment_path = lambda: "total"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.Total, [], name, value)


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("protocol", ("protocol", InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol))])
                        self._leafs = OrderedDict()

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  (key)
                        
                        	Name of the protocol
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['protocol_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('protocol_name', (YLeaf(YType.str, 'protocol-name'), ['str'])),
                                ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                                ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                                ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                                ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                                ('protocol', (YLeaf(YType.uint32, 'protocol'), ['int'])),
                                ('last_data_time', (YLeaf(YType.uint64, 'last-data-time'), ['int'])),
                                ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                                ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                                ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                                ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                            ])
                            self.protocol_name = None
                            self.bytes_received = None
                            self.packets_received = None
                            self.bytes_sent = None
                            self.packets_sent = None
                            self.protocol = None
                            self.last_data_time = None
                            self.input_data_rate = None
                            self.input_packet_rate = None
                            self.output_data_rate = None
                            self.output_packet_rate = None
                            self._segment_path = lambda: "protocol" + "[protocol-name='" + str(self.protocol_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, ['protocol_name', 'bytes_received', 'packets_received', 'bytes_sent', 'packets_sent', 'protocol', 'last_data_time', 'input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate'], name, value)


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "interfaces-mib-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.DataRate, self).__init__()

                        self.yang_name = "data-rate"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                            ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                            ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                            ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                            ('peak_input_data_rate', (YLeaf(YType.uint64, 'peak-input-data-rate'), ['int'])),
                            ('peak_input_packet_rate', (YLeaf(YType.uint64, 'peak-input-packet-rate'), ['int'])),
                            ('peak_output_data_rate', (YLeaf(YType.uint64, 'peak-output-data-rate'), ['int'])),
                            ('peak_output_packet_rate', (YLeaf(YType.uint64, 'peak-output-packet-rate'), ['int'])),
                            ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                            ('load_interval', (YLeaf(YType.uint32, 'load-interval'), ['int'])),
                            ('output_load', (YLeaf(YType.uint8, 'output-load'), ['int'])),
                            ('input_load', (YLeaf(YType.uint8, 'input-load'), ['int'])),
                            ('reliability', (YLeaf(YType.uint8, 'reliability'), ['int'])),
                        ])
                        self.input_data_rate = None
                        self.input_packet_rate = None
                        self.output_data_rate = None
                        self.output_packet_rate = None
                        self.peak_input_data_rate = None
                        self.peak_input_packet_rate = None
                        self.peak_output_data_rate = None
                        self.peak_output_packet_rate = None
                        self.bandwidth = None
                        self.load_interval = None
                        self.output_load = None
                        self.input_load = None
                        self.reliability = None
                        self._segment_path = lambda: "data-rate"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.DataRate, ['input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'bandwidth', 'load_interval', 'output_load', 'input_load', 'reliability'], name, value)


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                            ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                            ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                            ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                            ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                            ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                            ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                            ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                            ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                            ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                            ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                            ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                            ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                            ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                            ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                            ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                            ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                            ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                            ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                            ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                            ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                            ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                            ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                            ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                            ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                            ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                            ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                            ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                            ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                            ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                            ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                        ])
                        self.packets_received = None
                        self.bytes_received = None
                        self.packets_sent = None
                        self.bytes_sent = None
                        self.multicast_packets_received = None
                        self.broadcast_packets_received = None
                        self.multicast_packets_sent = None
                        self.broadcast_packets_sent = None
                        self.output_drops = None
                        self.output_queue_drops = None
                        self.input_drops = None
                        self.input_queue_drops = None
                        self.runt_packets_received = None
                        self.giant_packets_received = None
                        self.throttled_packets_received = None
                        self.parity_packets_received = None
                        self.unknown_protocol_packets_received = None
                        self.input_errors = None
                        self.crc_errors = None
                        self.input_overruns = None
                        self.framing_errors_received = None
                        self.input_ignored_packets = None
                        self.input_aborts = None
                        self.output_errors = None
                        self.output_underruns = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.applique = None
                        self.resets = None
                        self.carrier_transitions = None
                        self.availability_flag = None
                        self.last_data_time = None
                        self.seconds_since_last_clear_counters = None
                        self.last_discontinuity_time = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self._segment_path = lambda: "generic-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.GenericCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


            class Protocols(Entity):
                """
                List of protocols
                
                .. attribute:: protocol
                
                	Interface counters per protocol
                	**type**\: list of  		 :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols.Protocol>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Protocols, self).__init__()

                    self.yang_name = "protocols"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("protocol", ("protocol", InfraStatistics.Interfaces.Interface.Protocols.Protocol))])
                    self._leafs = OrderedDict()

                    self.protocol = YList(self)
                    self._segment_path = lambda: "protocols"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.Protocols, [], name, value)


                class Protocol(Entity):
                    """
                    Interface counters per protocol
                    
                    .. attribute:: protocol_name  (key)
                    
                    	Name of the protocol
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: protocol
                    
                    	Protocol number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: second
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Protocols.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "protocols"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['protocol_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('protocol_name', (YLeaf(YType.str, 'protocol-name'), ['str'])),
                            ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                            ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                            ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                            ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                            ('protocol', (YLeaf(YType.uint32, 'protocol'), ['int'])),
                            ('last_data_time', (YLeaf(YType.uint64, 'last-data-time'), ['int'])),
                            ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                            ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                            ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                            ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                        ])
                        self.protocol_name = None
                        self.bytes_received = None
                        self.packets_received = None
                        self.bytes_sent = None
                        self.packets_sent = None
                        self.protocol = None
                        self.last_data_time = None
                        self.input_data_rate = None
                        self.input_packet_rate = None
                        self.output_data_rate = None
                        self.output_packet_rate = None
                        self._segment_path = lambda: "protocol" + "[protocol-name='" + str(self.protocol_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Protocols.Protocol, ['protocol_name', 'bytes_received', 'packets_received', 'bytes_sent', 'packets_sent', 'protocol', 'last_data_time', 'input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate'], name, value)


            class InterfacesMibCounters(Entity):
                """
                Set of interface counters as displayed by the
                InterfacesMIB
                
                .. attribute:: packets_received
                
                	Packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_received
                
                	Bytes received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets_sent
                
                	Packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_sent
                
                	Bytes sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: multicast_packets_received
                
                	Multicast packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_received
                
                	Broadcast packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: multicast_packets_sent
                
                	Multicast packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_sent
                
                	Broadcast packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_drops
                
                	Total output drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_queue_drops
                
                	Output queue drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_drops
                
                	Total input drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_queue_drops
                
                	Input queue drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: runt_packets_received
                
                	Received runt packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: giant_packets_received
                
                	Received giant packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_packets_received
                
                	Received throttled packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: parity_packets_received
                
                	Received parity packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_protocol_packets_received
                
                	Unknown protocol packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_errors
                
                	Total input errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: crc_errors
                
                	Input CRC errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_overruns
                
                	Input overruns
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: framing_errors_received
                
                	Framing\-errors received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_ignored_packets
                
                	Input ignored packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_aborts
                
                	Input aborts
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_errors
                
                	Total output errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_underruns
                
                	Output underruns
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffer_failures
                
                	Output buffer failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffers_swapped_out
                
                	Output buffers swapped out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: applique
                
                	Applique
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: resets
                
                	Number of board resets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: carrier_transitions
                
                	Carrier transitions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: availability_flag
                
                	Availability bit mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_data_time
                
                	Time when counters were last written (in seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_last_clear_counters
                
                	Number of seconds since last clear counters
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_discontinuity_time
                
                	SysUpTime when counters were last reset (in seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_received
                
                	Seconds since packet received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_sent
                
                	Seconds since packet sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, self).__init__()

                    self.yang_name = "interfaces-mib-counters"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                        ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                        ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                        ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                        ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                        ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                        ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                        ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                        ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                        ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                        ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                        ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                        ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                        ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                        ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                        ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                        ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                        ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                        ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                        ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                        ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                        ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                        ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                        ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                        ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                        ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                        ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                        ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                        ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                        ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                        ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                        ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                        ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                        ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                        ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                        ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                    ])
                    self.packets_received = None
                    self.bytes_received = None
                    self.packets_sent = None
                    self.bytes_sent = None
                    self.multicast_packets_received = None
                    self.broadcast_packets_received = None
                    self.multicast_packets_sent = None
                    self.broadcast_packets_sent = None
                    self.output_drops = None
                    self.output_queue_drops = None
                    self.input_drops = None
                    self.input_queue_drops = None
                    self.runt_packets_received = None
                    self.giant_packets_received = None
                    self.throttled_packets_received = None
                    self.parity_packets_received = None
                    self.unknown_protocol_packets_received = None
                    self.input_errors = None
                    self.crc_errors = None
                    self.input_overruns = None
                    self.framing_errors_received = None
                    self.input_ignored_packets = None
                    self.input_aborts = None
                    self.output_errors = None
                    self.output_underruns = None
                    self.output_buffer_failures = None
                    self.output_buffers_swapped_out = None
                    self.applique = None
                    self.resets = None
                    self.carrier_transitions = None
                    self.availability_flag = None
                    self.last_data_time = None
                    self.seconds_since_last_clear_counters = None
                    self.last_discontinuity_time = None
                    self.seconds_since_packet_received = None
                    self.seconds_since_packet_sent = None
                    self._segment_path = lambda: "interfaces-mib-counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)


            class DataRate(Entity):
                """
                Datarate information
                
                .. attribute:: input_data_rate
                
                	Input data rate in 1000's of bps
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: input_packet_rate
                
                	Input packets per second
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: output_data_rate
                
                	Output data rate in 1000's of bps
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: output_packet_rate
                
                	Output packets per second
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: peak_input_data_rate
                
                	Peak input data rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_packet_rate
                
                	Peak input packet rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_data_rate
                
                	Peak output data rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_packet_rate
                
                	Peak output packet rate
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bandwidth
                
                	Bandwidth (in kbps)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: kbit/s
                
                .. attribute:: load_interval
                
                	Number of 30\-sec intervals less one
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_load
                
                	Output load as fraction of 255
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: input_load
                
                	Input load as fraction of 255
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: reliability
                
                	Reliability coefficient
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.DataRate, self).__init__()

                    self.yang_name = "data-rate"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('input_data_rate', (YLeaf(YType.uint64, 'input-data-rate'), ['int'])),
                        ('input_packet_rate', (YLeaf(YType.uint64, 'input-packet-rate'), ['int'])),
                        ('output_data_rate', (YLeaf(YType.uint64, 'output-data-rate'), ['int'])),
                        ('output_packet_rate', (YLeaf(YType.uint64, 'output-packet-rate'), ['int'])),
                        ('peak_input_data_rate', (YLeaf(YType.uint64, 'peak-input-data-rate'), ['int'])),
                        ('peak_input_packet_rate', (YLeaf(YType.uint64, 'peak-input-packet-rate'), ['int'])),
                        ('peak_output_data_rate', (YLeaf(YType.uint64, 'peak-output-data-rate'), ['int'])),
                        ('peak_output_packet_rate', (YLeaf(YType.uint64, 'peak-output-packet-rate'), ['int'])),
                        ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                        ('load_interval', (YLeaf(YType.uint32, 'load-interval'), ['int'])),
                        ('output_load', (YLeaf(YType.uint8, 'output-load'), ['int'])),
                        ('input_load', (YLeaf(YType.uint8, 'input-load'), ['int'])),
                        ('reliability', (YLeaf(YType.uint8, 'reliability'), ['int'])),
                    ])
                    self.input_data_rate = None
                    self.input_packet_rate = None
                    self.output_data_rate = None
                    self.output_packet_rate = None
                    self.peak_input_data_rate = None
                    self.peak_input_packet_rate = None
                    self.peak_output_data_rate = None
                    self.peak_output_packet_rate = None
                    self.bandwidth = None
                    self.load_interval = None
                    self.output_load = None
                    self.input_load = None
                    self.reliability = None
                    self._segment_path = lambda: "data-rate"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.DataRate, ['input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'bandwidth', 'load_interval', 'output_load', 'input_load', 'reliability'], name, value)


            class GenericCounters(Entity):
                """
                Generic set of interface counters
                
                .. attribute:: packets_received
                
                	Packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_received
                
                	Bytes received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: packets_sent
                
                	Packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_sent
                
                	Bytes sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: multicast_packets_received
                
                	Multicast packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_received
                
                	Broadcast packets received
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: multicast_packets_sent
                
                	Multicast packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_sent
                
                	Broadcast packets sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_drops
                
                	Total output drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_queue_drops
                
                	Output queue drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_drops
                
                	Total input drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_queue_drops
                
                	Input queue drops
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: runt_packets_received
                
                	Received runt packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: giant_packets_received
                
                	Received giant packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_packets_received
                
                	Received throttled packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: parity_packets_received
                
                	Received parity packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_protocol_packets_received
                
                	Unknown protocol packets received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_errors
                
                	Total input errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: crc_errors
                
                	Input CRC errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_overruns
                
                	Input overruns
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: framing_errors_received
                
                	Framing\-errors received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_ignored_packets
                
                	Input ignored packets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_aborts
                
                	Input aborts
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_errors
                
                	Total output errors
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_underruns
                
                	Output underruns
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffer_failures
                
                	Output buffer failures
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffers_swapped_out
                
                	Output buffers swapped out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: applique
                
                	Applique
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: resets
                
                	Number of board resets
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: carrier_transitions
                
                	Carrier transitions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: availability_flag
                
                	Availability bit mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_data_time
                
                	Time when counters were last written (in seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_last_clear_counters
                
                	Number of seconds since last clear counters
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_discontinuity_time
                
                	SysUpTime when counters were last reset (in seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_received
                
                	Seconds since packet received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_sent
                
                	Seconds since packet sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.GenericCounters, self).__init__()

                    self.yang_name = "generic-counters"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('packets_received', (YLeaf(YType.uint64, 'packets-received'), ['int'])),
                        ('bytes_received', (YLeaf(YType.uint64, 'bytes-received'), ['int'])),
                        ('packets_sent', (YLeaf(YType.uint64, 'packets-sent'), ['int'])),
                        ('bytes_sent', (YLeaf(YType.uint64, 'bytes-sent'), ['int'])),
                        ('multicast_packets_received', (YLeaf(YType.uint64, 'multicast-packets-received'), ['int'])),
                        ('broadcast_packets_received', (YLeaf(YType.uint64, 'broadcast-packets-received'), ['int'])),
                        ('multicast_packets_sent', (YLeaf(YType.uint64, 'multicast-packets-sent'), ['int'])),
                        ('broadcast_packets_sent', (YLeaf(YType.uint64, 'broadcast-packets-sent'), ['int'])),
                        ('output_drops', (YLeaf(YType.uint32, 'output-drops'), ['int'])),
                        ('output_queue_drops', (YLeaf(YType.uint32, 'output-queue-drops'), ['int'])),
                        ('input_drops', (YLeaf(YType.uint32, 'input-drops'), ['int'])),
                        ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                        ('runt_packets_received', (YLeaf(YType.uint32, 'runt-packets-received'), ['int'])),
                        ('giant_packets_received', (YLeaf(YType.uint32, 'giant-packets-received'), ['int'])),
                        ('throttled_packets_received', (YLeaf(YType.uint32, 'throttled-packets-received'), ['int'])),
                        ('parity_packets_received', (YLeaf(YType.uint32, 'parity-packets-received'), ['int'])),
                        ('unknown_protocol_packets_received', (YLeaf(YType.uint32, 'unknown-protocol-packets-received'), ['int'])),
                        ('input_errors', (YLeaf(YType.uint32, 'input-errors'), ['int'])),
                        ('crc_errors', (YLeaf(YType.uint32, 'crc-errors'), ['int'])),
                        ('input_overruns', (YLeaf(YType.uint32, 'input-overruns'), ['int'])),
                        ('framing_errors_received', (YLeaf(YType.uint32, 'framing-errors-received'), ['int'])),
                        ('input_ignored_packets', (YLeaf(YType.uint32, 'input-ignored-packets'), ['int'])),
                        ('input_aborts', (YLeaf(YType.uint32, 'input-aborts'), ['int'])),
                        ('output_errors', (YLeaf(YType.uint32, 'output-errors'), ['int'])),
                        ('output_underruns', (YLeaf(YType.uint32, 'output-underruns'), ['int'])),
                        ('output_buffer_failures', (YLeaf(YType.uint32, 'output-buffer-failures'), ['int'])),
                        ('output_buffers_swapped_out', (YLeaf(YType.uint32, 'output-buffers-swapped-out'), ['int'])),
                        ('applique', (YLeaf(YType.uint32, 'applique'), ['int'])),
                        ('resets', (YLeaf(YType.uint32, 'resets'), ['int'])),
                        ('carrier_transitions', (YLeaf(YType.uint32, 'carrier-transitions'), ['int'])),
                        ('availability_flag', (YLeaf(YType.uint32, 'availability-flag'), ['int'])),
                        ('last_data_time', (YLeaf(YType.uint32, 'last-data-time'), ['int'])),
                        ('seconds_since_last_clear_counters', (YLeaf(YType.uint32, 'seconds-since-last-clear-counters'), ['int'])),
                        ('last_discontinuity_time', (YLeaf(YType.uint32, 'last-discontinuity-time'), ['int'])),
                        ('seconds_since_packet_received', (YLeaf(YType.uint32, 'seconds-since-packet-received'), ['int'])),
                        ('seconds_since_packet_sent', (YLeaf(YType.uint32, 'seconds-since-packet-sent'), ['int'])),
                    ])
                    self.packets_received = None
                    self.bytes_received = None
                    self.packets_sent = None
                    self.bytes_sent = None
                    self.multicast_packets_received = None
                    self.broadcast_packets_received = None
                    self.multicast_packets_sent = None
                    self.broadcast_packets_sent = None
                    self.output_drops = None
                    self.output_queue_drops = None
                    self.input_drops = None
                    self.input_queue_drops = None
                    self.runt_packets_received = None
                    self.giant_packets_received = None
                    self.throttled_packets_received = None
                    self.parity_packets_received = None
                    self.unknown_protocol_packets_received = None
                    self.input_errors = None
                    self.crc_errors = None
                    self.input_overruns = None
                    self.framing_errors_received = None
                    self.input_ignored_packets = None
                    self.input_aborts = None
                    self.output_errors = None
                    self.output_underruns = None
                    self.output_buffer_failures = None
                    self.output_buffers_swapped_out = None
                    self.applique = None
                    self.resets = None
                    self.carrier_transitions = None
                    self.availability_flag = None
                    self.last_data_time = None
                    self.seconds_since_last_clear_counters = None
                    self.last_discontinuity_time = None
                    self.seconds_since_packet_received = None
                    self.seconds_since_packet_sent = None
                    self._segment_path = lambda: "generic-counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.GenericCounters, ['packets_received', 'bytes_received', 'packets_sent', 'bytes_sent', 'multicast_packets_received', 'broadcast_packets_received', 'multicast_packets_sent', 'broadcast_packets_sent', 'output_drops', 'output_queue_drops', 'input_drops', 'input_queue_drops', 'runt_packets_received', 'giant_packets_received', 'throttled_packets_received', 'parity_packets_received', 'unknown_protocol_packets_received', 'input_errors', 'crc_errors', 'input_overruns', 'framing_errors_received', 'input_ignored_packets', 'input_aborts', 'output_errors', 'output_underruns', 'output_buffer_failures', 'output_buffers_swapped_out', 'applique', 'resets', 'carrier_transitions', 'availability_flag', 'last_data_time', 'seconds_since_last_clear_counters', 'last_discontinuity_time', 'seconds_since_packet_received', 'seconds_since_packet_sent'], name, value)

    def clone_ptr(self):
        self._top_entity = InfraStatistics()
        return self._top_entity

