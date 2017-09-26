""" Cisco_IOS_XR_infra_statsd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package operational data.

This module contains definitions
for the following management objects\:
  infra\-statistics\: Statistics Infrastructure

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InfraStatistics(Entity):
    """
    Statistics Infrastructure
    
    .. attribute:: interfaces
    
    	List of interfaces
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces>`
    
    

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
        self._child_container_classes = {"interfaces" : ("interfaces", InfraStatistics.Interfaces)}
        self._child_list_classes = {}

        self.interfaces = InfraStatistics.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-statsd-oper:infra-statistics"


    class Interfaces(Entity):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Statistics of an interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-statsd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(InfraStatistics.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "infra-statistics"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", InfraStatistics.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-oper:infra-statistics/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(InfraStatistics.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Statistics of an interface
            
            .. attribute:: interface_name  <key>
            
            	Name of the interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: cache
            
            	Cached stats data of interfaces
            	**type**\:   :py:class:`Cache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache>`
            
            .. attribute:: data_rate
            
            	Datarate information
            	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.DataRate>`
            
            .. attribute:: generic_counters
            
            	Generic set of interface counters
            	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.GenericCounters>`
            
            .. attribute:: interfaces_mib_counters
            
            	Set of interface counters as displayed by the InterfacesMIB
            	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.InterfacesMibCounters>`
            
            .. attribute:: latest
            
            	Latest stats data of interfaces
            	**type**\:   :py:class:`Latest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest>`
            
            .. attribute:: protocols
            
            	List of protocols
            	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols>`
            
            .. attribute:: total
            
            	Total stats data of interfaces
            	**type**\:   :py:class:`Total <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total>`
            
            

            """

            _prefix = 'infra-statsd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(InfraStatistics.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"cache" : ("cache", InfraStatistics.Interfaces.Interface.Cache), "data-rate" : ("data_rate", InfraStatistics.Interfaces.Interface.DataRate), "generic-counters" : ("generic_counters", InfraStatistics.Interfaces.Interface.GenericCounters), "interfaces-mib-counters" : ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.InterfacesMibCounters), "latest" : ("latest", InfraStatistics.Interfaces.Interface.Latest), "protocols" : ("protocols", InfraStatistics.Interfaces.Interface.Protocols), "total" : ("total", InfraStatistics.Interfaces.Interface.Total)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.cache = InfraStatistics.Interfaces.Interface.Cache()
                self.cache.parent = self
                self._children_name_map["cache"] = "cache"
                self._children_yang_names.add("cache")

                self.data_rate = InfraStatistics.Interfaces.Interface.DataRate()
                self.data_rate.parent = self
                self._children_name_map["data_rate"] = "data-rate"
                self._children_yang_names.add("data-rate")

                self.generic_counters = InfraStatistics.Interfaces.Interface.GenericCounters()
                self.generic_counters.parent = self
                self._children_name_map["generic_counters"] = "generic-counters"
                self._children_yang_names.add("generic-counters")

                self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.InterfacesMibCounters()
                self.interfaces_mib_counters.parent = self
                self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                self._children_yang_names.add("interfaces-mib-counters")

                self.latest = InfraStatistics.Interfaces.Interface.Latest()
                self.latest.parent = self
                self._children_name_map["latest"] = "latest"
                self._children_yang_names.add("latest")

                self.protocols = InfraStatistics.Interfaces.Interface.Protocols()
                self.protocols.parent = self
                self._children_name_map["protocols"] = "protocols"
                self._children_yang_names.add("protocols")

                self.total = InfraStatistics.Interfaces.Interface.Total()
                self.total.parent = self
                self._children_name_map["total"] = "total"
                self._children_yang_names.add("total")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-statsd-oper:infra-statistics/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(InfraStatistics.Interfaces.Interface, ['interface_name'], name, value)


            class Cache(Entity):
                """
                Cached stats data of interfaces
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.GenericCounters>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters>`
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Cache, self).__init__()

                    self.yang_name = "cache"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"data-rate" : ("data_rate", InfraStatistics.Interfaces.Interface.Cache.DataRate), "generic-counters" : ("generic_counters", InfraStatistics.Interfaces.Interface.Cache.GenericCounters), "interfaces-mib-counters" : ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters), "protocols" : ("protocols", InfraStatistics.Interfaces.Interface.Cache.Protocols)}
                    self._child_list_classes = {}

                    self.data_rate = InfraStatistics.Interfaces.Interface.Cache.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"
                    self._children_yang_names.add("data-rate")

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Cache.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._children_yang_names.add("generic-counters")

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    self._children_yang_names.add("interfaces-mib-counters")

                    self.protocols = InfraStatistics.Interfaces.Interface.Cache.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._children_yang_names.add("protocols")
                    self._segment_path = lambda: "cache"


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_load = YLeaf(YType.uint8, "input-load")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.load_interval = YLeaf(YType.uint32, "load-interval")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_load = YLeaf(YType.uint8, "output-load")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                        self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                        self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                        self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                        self.reliability = YLeaf(YType.uint8, "reliability")
                        self._segment_path = lambda: "data-rate"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.DataRate, ['bandwidth', 'input_data_rate', 'input_load', 'input_packet_rate', 'load_interval', 'output_data_rate', 'output_load', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'reliability'], name, value)


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                        self._segment_path = lambda: "generic-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.GenericCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                        self._segment_path = lambda: "interfaces-mib-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Cache.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "cache"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"protocol" : ("protocol", InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol)}

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  <key>
                        
                        	Name of the protocol
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.protocol_name = YLeaf(YType.str, "protocol-name")

                            self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                            self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                            self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                            self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                            self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                            self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                            self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                            self.packets_received = YLeaf(YType.uint64, "packets-received")

                            self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                            self.protocol = YLeaf(YType.uint32, "protocol")
                            self._segment_path = lambda: "protocol" + "[protocol-name='" + self.protocol_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol, ['protocol_name', 'bytes_received', 'bytes_sent', 'input_data_rate', 'input_packet_rate', 'last_data_time', 'output_data_rate', 'output_packet_rate', 'packets_received', 'packets_sent', 'protocol'], name, value)


            class DataRate(Entity):
                """
                Datarate information
                
                .. attribute:: bandwidth
                
                	Bandwidth (in kbps)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: kbit/s
                
                .. attribute:: input_data_rate
                
                	Input data rate in 1000's of bps
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: input_load
                
                	Input load as fraction of 255
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: input_packet_rate
                
                	Input packets per second
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: load_interval
                
                	Number of 30\-sec intervals less one
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_data_rate
                
                	Output data rate in 1000's of bps
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: bit/s
                
                .. attribute:: output_load
                
                	Output load as fraction of 255
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: output_packet_rate
                
                	Output packets per second
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: packet/s
                
                .. attribute:: peak_input_data_rate
                
                	Peak input data rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_input_packet_rate
                
                	Peak input packet rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_data_rate
                
                	Peak output data rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: peak_output_packet_rate
                
                	Peak output packet rate
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: reliability
                
                	Reliability coefficient
                	**type**\:  int
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                    self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                    self.input_load = YLeaf(YType.uint8, "input-load")

                    self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                    self.load_interval = YLeaf(YType.uint32, "load-interval")

                    self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                    self.output_load = YLeaf(YType.uint8, "output-load")

                    self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                    self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                    self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                    self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                    self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                    self.reliability = YLeaf(YType.uint8, "reliability")
                    self._segment_path = lambda: "data-rate"

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.DataRate, ['bandwidth', 'input_data_rate', 'input_load', 'input_packet_rate', 'load_interval', 'output_data_rate', 'output_load', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'reliability'], name, value)


            class GenericCounters(Entity):
                """
                Generic set of interface counters
                
                .. attribute:: applique
                
                	Applique
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: availability_flag
                
                	Availability bit mask
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: broadcast_packets_received
                
                	Broadcast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_sent
                
                	Broadcast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_received
                
                	Bytes received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: bytes_sent
                
                	Bytes sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: carrier_transitions
                
                	Carrier transitions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: crc_errors
                
                	Input CRC errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: framing_errors_received
                
                	Framing\-errors received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: giant_packets_received
                
                	Received giant packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_aborts
                
                	Input aborts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_drops
                
                	Total input drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_errors
                
                	Total input errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_ignored_packets
                
                	Input ignored packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_overruns
                
                	Input overruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_queue_drops
                
                	Input queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_data_time
                
                	Time when counters were last written (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_discontinuity_time
                
                	SysUpTime when counters were last reset (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: multicast_packets_received
                
                	Multicast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: multicast_packets_sent
                
                	Multicast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_buffer_failures
                
                	Output buffer failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffers_swapped_out
                
                	Output buffers swapped out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_drops
                
                	Total output drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_errors
                
                	Total output errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_queue_drops
                
                	Output queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_underruns
                
                	Output underruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_received
                
                	Packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_sent
                
                	Packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: parity_packets_received
                
                	Received parity packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resets
                
                	Number of board resets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: runt_packets_received
                
                	Received runt packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_since_last_clear_counters
                
                	Number of seconds since last clear counters
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_received
                
                	Seconds since packet received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_sent
                
                	Seconds since packet sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: throttled_packets_received
                
                	Received throttled packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_protocol_packets_received
                
                	Unknown protocol packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.GenericCounters, self).__init__()

                    self.yang_name = "generic-counters"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.applique = YLeaf(YType.uint32, "applique")

                    self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                    self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                    self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                    self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                    self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                    self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                    self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                    self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                    self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                    self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                    self.input_drops = YLeaf(YType.uint32, "input-drops")

                    self.input_errors = YLeaf(YType.uint32, "input-errors")

                    self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                    self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                    self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                    self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                    self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                    self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                    self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                    self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                    self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                    self.output_drops = YLeaf(YType.uint32, "output-drops")

                    self.output_errors = YLeaf(YType.uint32, "output-errors")

                    self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                    self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                    self.packets_received = YLeaf(YType.uint64, "packets-received")

                    self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                    self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                    self.resets = YLeaf(YType.uint32, "resets")

                    self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                    self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                    self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                    self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                    self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                    self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                    self._segment_path = lambda: "generic-counters"

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.GenericCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


            class InterfacesMibCounters(Entity):
                """
                Set of interface counters as displayed by the
                InterfacesMIB
                
                .. attribute:: applique
                
                	Applique
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: availability_flag
                
                	Availability bit mask
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: broadcast_packets_received
                
                	Broadcast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: broadcast_packets_sent
                
                	Broadcast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_received
                
                	Bytes received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: bytes_sent
                
                	Bytes sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: carrier_transitions
                
                	Carrier transitions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: crc_errors
                
                	Input CRC errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: framing_errors_received
                
                	Framing\-errors received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: giant_packets_received
                
                	Received giant packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_aborts
                
                	Input aborts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_drops
                
                	Total input drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_errors
                
                	Total input errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_ignored_packets
                
                	Input ignored packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_overruns
                
                	Input overruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: input_queue_drops
                
                	Input queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_data_time
                
                	Time when counters were last written (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_discontinuity_time
                
                	SysUpTime when counters were last reset (in seconds)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: multicast_packets_received
                
                	Multicast packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: multicast_packets_sent
                
                	Multicast packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: output_buffer_failures
                
                	Output buffer failures
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_buffers_swapped_out
                
                	Output buffers swapped out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_drops
                
                	Total output drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_errors
                
                	Total output errors
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_queue_drops
                
                	Output queue drops
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: output_underruns
                
                	Output underruns
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_received
                
                	Packets received
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_sent
                
                	Packets sent
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: parity_packets_received
                
                	Received parity packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: resets
                
                	Number of board resets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: runt_packets_received
                
                	Received runt packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: seconds_since_last_clear_counters
                
                	Number of seconds since last clear counters
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_received
                
                	Seconds since packet received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: seconds_since_packet_sent
                
                	Seconds since packet sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: throttled_packets_received
                
                	Received throttled packets
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_protocol_packets_received
                
                	Unknown protocol packets received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, self).__init__()

                    self.yang_name = "interfaces-mib-counters"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.applique = YLeaf(YType.uint32, "applique")

                    self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                    self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                    self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                    self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                    self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                    self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                    self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                    self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                    self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                    self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                    self.input_drops = YLeaf(YType.uint32, "input-drops")

                    self.input_errors = YLeaf(YType.uint32, "input-errors")

                    self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                    self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                    self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                    self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                    self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                    self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                    self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                    self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                    self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                    self.output_drops = YLeaf(YType.uint32, "output-drops")

                    self.output_errors = YLeaf(YType.uint32, "output-errors")

                    self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                    self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                    self.packets_received = YLeaf(YType.uint64, "packets-received")

                    self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                    self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                    self.resets = YLeaf(YType.uint32, "resets")

                    self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                    self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                    self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                    self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                    self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                    self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                    self._segment_path = lambda: "interfaces-mib-counters"

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.InterfacesMibCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


            class Latest(Entity):
                """
                Latest stats data of interfaces
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.GenericCounters>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters>`
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Latest, self).__init__()

                    self.yang_name = "latest"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"data-rate" : ("data_rate", InfraStatistics.Interfaces.Interface.Latest.DataRate), "generic-counters" : ("generic_counters", InfraStatistics.Interfaces.Interface.Latest.GenericCounters), "interfaces-mib-counters" : ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters), "protocols" : ("protocols", InfraStatistics.Interfaces.Interface.Latest.Protocols)}
                    self._child_list_classes = {}

                    self.data_rate = InfraStatistics.Interfaces.Interface.Latest.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"
                    self._children_yang_names.add("data-rate")

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Latest.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._children_yang_names.add("generic-counters")

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    self._children_yang_names.add("interfaces-mib-counters")

                    self.protocols = InfraStatistics.Interfaces.Interface.Latest.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._children_yang_names.add("protocols")
                    self._segment_path = lambda: "latest"


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_load = YLeaf(YType.uint8, "input-load")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.load_interval = YLeaf(YType.uint32, "load-interval")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_load = YLeaf(YType.uint8, "output-load")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                        self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                        self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                        self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                        self.reliability = YLeaf(YType.uint8, "reliability")
                        self._segment_path = lambda: "data-rate"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.DataRate, ['bandwidth', 'input_data_rate', 'input_load', 'input_packet_rate', 'load_interval', 'output_data_rate', 'output_load', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'reliability'], name, value)


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                        self._segment_path = lambda: "generic-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.GenericCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                        self._segment_path = lambda: "interfaces-mib-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Latest.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "latest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"protocol" : ("protocol", InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol)}

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  <key>
                        
                        	Name of the protocol
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.protocol_name = YLeaf(YType.str, "protocol-name")

                            self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                            self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                            self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                            self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                            self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                            self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                            self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                            self.packets_received = YLeaf(YType.uint64, "packets-received")

                            self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                            self.protocol = YLeaf(YType.uint32, "protocol")
                            self._segment_path = lambda: "protocol" + "[protocol-name='" + self.protocol_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol, ['protocol_name', 'bytes_received', 'bytes_sent', 'input_data_rate', 'input_packet_rate', 'last_data_time', 'output_data_rate', 'output_packet_rate', 'packets_received', 'packets_sent', 'protocol'], name, value)


            class Protocols(Entity):
                """
                List of protocols
                
                .. attribute:: protocol
                
                	Interface counters per protocol
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols.Protocol>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Protocols, self).__init__()

                    self.yang_name = "protocols"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"protocol" : ("protocol", InfraStatistics.Interfaces.Interface.Protocols.Protocol)}

                    self.protocol = YList(self)
                    self._segment_path = lambda: "protocols"

                def __setattr__(self, name, value):
                    self._perform_setattr(InfraStatistics.Interfaces.Interface.Protocols, [], name, value)


                class Protocol(Entity):
                    """
                    Interface counters per protocol
                    
                    .. attribute:: protocol_name  <key>
                    
                    	Name of the protocol
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: protocol
                    
                    	Protocol number
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Protocols.Protocol, self).__init__()

                        self.yang_name = "protocol"
                        self.yang_parent_name = "protocols"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.protocol_name = YLeaf(YType.str, "protocol-name")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.protocol = YLeaf(YType.uint32, "protocol")
                        self._segment_path = lambda: "protocol" + "[protocol-name='" + self.protocol_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Protocols.Protocol, ['protocol_name', 'bytes_received', 'bytes_sent', 'input_data_rate', 'input_packet_rate', 'last_data_time', 'output_data_rate', 'output_packet_rate', 'packets_received', 'packets_sent', 'protocol'], name, value)


            class Total(Entity):
                """
                Total stats data of interfaces
                
                .. attribute:: data_rate
                
                	Datarate information
                	**type**\:   :py:class:`DataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.DataRate>`
                
                .. attribute:: generic_counters
                
                	Generic set of interface counters
                	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.GenericCounters>`
                
                .. attribute:: interfaces_mib_counters
                
                	Set of interface counters as displayed by the InterfacesMIB
                	**type**\:   :py:class:`InterfacesMibCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters>`
                
                .. attribute:: protocols
                
                	List of protocols
                	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(InfraStatistics.Interfaces.Interface.Total, self).__init__()

                    self.yang_name = "total"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"data-rate" : ("data_rate", InfraStatistics.Interfaces.Interface.Total.DataRate), "generic-counters" : ("generic_counters", InfraStatistics.Interfaces.Interface.Total.GenericCounters), "interfaces-mib-counters" : ("interfaces_mib_counters", InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters), "protocols" : ("protocols", InfraStatistics.Interfaces.Interface.Total.Protocols)}
                    self._child_list_classes = {}

                    self.data_rate = InfraStatistics.Interfaces.Interface.Total.DataRate()
                    self.data_rate.parent = self
                    self._children_name_map["data_rate"] = "data-rate"
                    self._children_yang_names.add("data-rate")

                    self.generic_counters = InfraStatistics.Interfaces.Interface.Total.GenericCounters()
                    self.generic_counters.parent = self
                    self._children_name_map["generic_counters"] = "generic-counters"
                    self._children_yang_names.add("generic-counters")

                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self._children_name_map["interfaces_mib_counters"] = "interfaces-mib-counters"
                    self._children_yang_names.add("interfaces-mib-counters")

                    self.protocols = InfraStatistics.Interfaces.Interface.Total.Protocols()
                    self.protocols.parent = self
                    self._children_name_map["protocols"] = "protocols"
                    self._children_yang_names.add("protocols")
                    self._segment_path = lambda: "total"


                class DataRate(Entity):
                    """
                    Datarate information
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth (in kbps)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: input_load
                    
                    	Input load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: input_packet_rate
                    
                    	Input packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: load_interval
                    
                    	Number of 30\-sec intervals less one
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in 1000's of bps
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: bit/s
                    
                    .. attribute:: output_load
                    
                    	Output load as fraction of 255
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: output_packet_rate
                    
                    	Output packets per second
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: packet/s
                    
                    .. attribute:: peak_input_data_rate
                    
                    	Peak input data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_input_packet_rate
                    
                    	Peak input packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_data_rate
                    
                    	Peak output data rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: peak_output_packet_rate
                    
                    	Peak output packet rate
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reliability
                    
                    	Reliability coefficient
                    	**type**\:  int
                    
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
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                        self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                        self.input_load = YLeaf(YType.uint8, "input-load")

                        self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                        self.load_interval = YLeaf(YType.uint32, "load-interval")

                        self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                        self.output_load = YLeaf(YType.uint8, "output-load")

                        self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                        self.peak_input_data_rate = YLeaf(YType.uint64, "peak-input-data-rate")

                        self.peak_input_packet_rate = YLeaf(YType.uint64, "peak-input-packet-rate")

                        self.peak_output_data_rate = YLeaf(YType.uint64, "peak-output-data-rate")

                        self.peak_output_packet_rate = YLeaf(YType.uint64, "peak-output-packet-rate")

                        self.reliability = YLeaf(YType.uint8, "reliability")
                        self._segment_path = lambda: "data-rate"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.DataRate, ['bandwidth', 'input_data_rate', 'input_load', 'input_packet_rate', 'load_interval', 'output_data_rate', 'output_load', 'output_packet_rate', 'peak_input_data_rate', 'peak_input_packet_rate', 'peak_output_data_rate', 'peak_output_packet_rate', 'reliability'], name, value)


                class GenericCounters(Entity):
                    """
                    Generic set of interface counters
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.GenericCounters, self).__init__()

                        self.yang_name = "generic-counters"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                        self._segment_path = lambda: "generic-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.GenericCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


                class InterfacesMibCounters(Entity):
                    """
                    Set of interface counters as displayed by the
                    InterfacesMIB
                    
                    .. attribute:: applique
                    
                    	Applique
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: availability_flag
                    
                    	Availability bit mask
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: broadcast_packets_received
                    
                    	Broadcast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: broadcast_packets_sent
                    
                    	Broadcast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bytes_received
                    
                    	Bytes received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_sent
                    
                    	Bytes sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: carrier_transitions
                    
                    	Carrier transitions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: crc_errors
                    
                    	Input CRC errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: framing_errors_received
                    
                    	Framing\-errors received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giant_packets_received
                    
                    	Received giant packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_aborts
                    
                    	Input aborts
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_drops
                    
                    	Total input drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_errors
                    
                    	Total input errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_ignored_packets
                    
                    	Input ignored packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_overruns
                    
                    	Input overruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue_drops
                    
                    	Input queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_data_time
                    
                    	Time when counters were last written (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_discontinuity_time
                    
                    	SysUpTime when counters were last reset (in seconds)
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: multicast_packets_received
                    
                    	Multicast packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multicast_packets_sent
                    
                    	Multicast packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_buffer_failures
                    
                    	Output buffer failures
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_buffers_swapped_out
                    
                    	Output buffers swapped out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_drops
                    
                    	Total output drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_errors
                    
                    	Total output errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_queue_drops
                    
                    	Output queue drops
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_underruns
                    
                    	Output underruns
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received
                    
                    	Packets received
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: packets_sent
                    
                    	Packets sent
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: parity_packets_received
                    
                    	Received parity packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resets
                    
                    	Number of board resets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: runt_packets_received
                    
                    	Received runt packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: seconds_since_last_clear_counters
                    
                    	Number of seconds since last clear counters
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_received
                    
                    	Seconds since packet received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: seconds_since_packet_sent
                    
                    	Seconds since packet sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: throttled_packets_received
                    
                    	Received throttled packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unknown_protocol_packets_received
                    
                    	Unknown protocol packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, self).__init__()

                        self.yang_name = "interfaces-mib-counters"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.applique = YLeaf(YType.uint32, "applique")

                        self.availability_flag = YLeaf(YType.uint32, "availability-flag")

                        self.broadcast_packets_received = YLeaf(YType.uint64, "broadcast-packets-received")

                        self.broadcast_packets_sent = YLeaf(YType.uint64, "broadcast-packets-sent")

                        self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                        self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                        self.carrier_transitions = YLeaf(YType.uint32, "carrier-transitions")

                        self.crc_errors = YLeaf(YType.uint32, "crc-errors")

                        self.framing_errors_received = YLeaf(YType.uint32, "framing-errors-received")

                        self.giant_packets_received = YLeaf(YType.uint32, "giant-packets-received")

                        self.input_aborts = YLeaf(YType.uint32, "input-aborts")

                        self.input_drops = YLeaf(YType.uint32, "input-drops")

                        self.input_errors = YLeaf(YType.uint32, "input-errors")

                        self.input_ignored_packets = YLeaf(YType.uint32, "input-ignored-packets")

                        self.input_overruns = YLeaf(YType.uint32, "input-overruns")

                        self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                        self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                        self.last_discontinuity_time = YLeaf(YType.uint32, "last-discontinuity-time")

                        self.multicast_packets_received = YLeaf(YType.uint64, "multicast-packets-received")

                        self.multicast_packets_sent = YLeaf(YType.uint64, "multicast-packets-sent")

                        self.output_buffer_failures = YLeaf(YType.uint32, "output-buffer-failures")

                        self.output_buffers_swapped_out = YLeaf(YType.uint32, "output-buffers-swapped-out")

                        self.output_drops = YLeaf(YType.uint32, "output-drops")

                        self.output_errors = YLeaf(YType.uint32, "output-errors")

                        self.output_queue_drops = YLeaf(YType.uint32, "output-queue-drops")

                        self.output_underruns = YLeaf(YType.uint32, "output-underruns")

                        self.packets_received = YLeaf(YType.uint64, "packets-received")

                        self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                        self.parity_packets_received = YLeaf(YType.uint32, "parity-packets-received")

                        self.resets = YLeaf(YType.uint32, "resets")

                        self.runt_packets_received = YLeaf(YType.uint32, "runt-packets-received")

                        self.seconds_since_last_clear_counters = YLeaf(YType.uint32, "seconds-since-last-clear-counters")

                        self.seconds_since_packet_received = YLeaf(YType.uint32, "seconds-since-packet-received")

                        self.seconds_since_packet_sent = YLeaf(YType.uint32, "seconds-since-packet-sent")

                        self.throttled_packets_received = YLeaf(YType.uint32, "throttled-packets-received")

                        self.unknown_protocol_packets_received = YLeaf(YType.uint32, "unknown-protocol-packets-received")
                        self._segment_path = lambda: "interfaces-mib-counters"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters, ['applique', 'availability_flag', 'broadcast_packets_received', 'broadcast_packets_sent', 'bytes_received', 'bytes_sent', 'carrier_transitions', 'crc_errors', 'framing_errors_received', 'giant_packets_received', 'input_aborts', 'input_drops', 'input_errors', 'input_ignored_packets', 'input_overruns', 'input_queue_drops', 'last_data_time', 'last_discontinuity_time', 'multicast_packets_received', 'multicast_packets_sent', 'output_buffer_failures', 'output_buffers_swapped_out', 'output_drops', 'output_errors', 'output_queue_drops', 'output_underruns', 'packets_received', 'packets_sent', 'parity_packets_received', 'resets', 'runt_packets_received', 'seconds_since_last_clear_counters', 'seconds_since_packet_received', 'seconds_since_packet_sent', 'throttled_packets_received', 'unknown_protocol_packets_received'], name, value)


                class Protocols(Entity):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(InfraStatistics.Interfaces.Interface.Total.Protocols, self).__init__()

                        self.yang_name = "protocols"
                        self.yang_parent_name = "total"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"protocol" : ("protocol", InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol)}

                        self.protocol = YList(self)
                        self._segment_path = lambda: "protocols"

                    def __setattr__(self, name, value):
                        self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.Protocols, [], name, value)


                    class Protocol(Entity):
                        """
                        Interface counters per protocol
                        
                        .. attribute:: protocol_name  <key>
                        
                        	Name of the protocol
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: bytes_received
                        
                        	Bytes received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: bytes_sent
                        
                        	Bytes sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: input_data_rate
                        
                        	Input data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: input_packet_rate
                        
                        	Input packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: last_data_time
                        
                        	Time when counters were last written (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: output_data_rate
                        
                        	Output data rate in 1000's of bps
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: bit/s
                        
                        .. attribute:: output_packet_rate
                        
                        	Output packets per second
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: packet/s
                        
                        .. attribute:: packets_received
                        
                        	Packets received
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packets_sent
                        
                        	Packets sent
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: protocol
                        
                        	Protocol number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-statsd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, self).__init__()

                            self.yang_name = "protocol"
                            self.yang_parent_name = "protocols"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.protocol_name = YLeaf(YType.str, "protocol-name")

                            self.bytes_received = YLeaf(YType.uint64, "bytes-received")

                            self.bytes_sent = YLeaf(YType.uint64, "bytes-sent")

                            self.input_data_rate = YLeaf(YType.uint64, "input-data-rate")

                            self.input_packet_rate = YLeaf(YType.uint64, "input-packet-rate")

                            self.last_data_time = YLeaf(YType.uint32, "last-data-time")

                            self.output_data_rate = YLeaf(YType.uint64, "output-data-rate")

                            self.output_packet_rate = YLeaf(YType.uint64, "output-packet-rate")

                            self.packets_received = YLeaf(YType.uint64, "packets-received")

                            self.packets_sent = YLeaf(YType.uint64, "packets-sent")

                            self.protocol = YLeaf(YType.uint32, "protocol")
                            self._segment_path = lambda: "protocol" + "[protocol-name='" + self.protocol_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol, ['protocol_name', 'bytes_received', 'bytes_sent', 'input_data_rate', 'input_packet_rate', 'last_data_time', 'output_data_rate', 'output_packet_rate', 'packets_received', 'packets_sent', 'protocol'], name, value)

    def clone_ptr(self):
        self._top_entity = InfraStatistics()
        return self._top_entity

