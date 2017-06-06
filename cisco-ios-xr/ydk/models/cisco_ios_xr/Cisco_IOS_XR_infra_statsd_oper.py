""" Cisco_IOS_XR_infra_statsd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-statsd package operational data.

This module contains definitions
for the following management objects\:
  infra\-statistics\: Statistics Infrastructure

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class InfraStatistics(object):
    """
    Statistics Infrastructure
    
    .. attribute:: interfaces
    
    	List of interfaces
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces>`
    
    

    """

    _prefix = 'infra-statsd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.interfaces = InfraStatistics.Interfaces()
        self.interfaces.parent = self


    class Interfaces(object):
        """
        List of interfaces
        
        .. attribute:: interface
        
        	Statistics of an interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-statsd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Statistics of an interface
            
            .. attribute:: interface_name  <key>
            
            	Name of the interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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
                self.parent = None
                self.interface_name = None
                self.cache = InfraStatistics.Interfaces.Interface.Cache()
                self.cache.parent = self
                self.data_rate = InfraStatistics.Interfaces.Interface.DataRate()
                self.data_rate.parent = self
                self.generic_counters = InfraStatistics.Interfaces.Interface.GenericCounters()
                self.generic_counters.parent = self
                self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.InterfacesMibCounters()
                self.interfaces_mib_counters.parent = self
                self.latest = InfraStatistics.Interfaces.Interface.Latest()
                self.latest.parent = self
                self.protocols = InfraStatistics.Interfaces.Interface.Protocols()
                self.protocols.parent = self
                self.total = InfraStatistics.Interfaces.Interface.Total()
                self.total.parent = self


            class Cache(object):
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
                    self.parent = None
                    self.data_rate = InfraStatistics.Interfaces.Interface.Cache.DataRate()
                    self.data_rate.parent = self
                    self.generic_counters = InfraStatistics.Interfaces.Interface.Cache.GenericCounters()
                    self.generic_counters.parent = self
                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self.protocols = InfraStatistics.Interfaces.Interface.Cache.Protocols()
                    self.protocols.parent = self


                class Protocols(object):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.protocol = YList()
                        self.protocol.parent = self
                        self.protocol.name = 'protocol'


                    class Protocol(object):
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
                            self.parent = None
                            self.protocol_name = None
                            self.bytes_received = None
                            self.bytes_sent = None
                            self.input_data_rate = None
                            self.input_packet_rate = None
                            self.last_data_time = None
                            self.output_data_rate = None
                            self.output_packet_rate = None
                            self.packets_received = None
                            self.packets_sent = None
                            self.protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.protocol_name is None:
                                raise YPYModelError('Key property protocol_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocol[Cisco-IOS-XR-infra-statsd-oper:protocol-name = ' + str(self.protocol_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.protocol_name is not None:
                                return True

                            if self.bytes_received is not None:
                                return True

                            if self.bytes_sent is not None:
                                return True

                            if self.input_data_rate is not None:
                                return True

                            if self.input_packet_rate is not None:
                                return True

                            if self.last_data_time is not None:
                                return True

                            if self.output_data_rate is not None:
                                return True

                            if self.output_packet_rate is not None:
                                return True

                            if self.packets_received is not None:
                                return True

                            if self.packets_sent is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                            return meta._meta_table['InfraStatistics.Interfaces.Interface.Cache.Protocols.Protocol']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocols'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.protocol is not None:
                            for child_ref in self.protocol:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Cache.Protocols']['meta_info']


                class InterfacesMibCounters(object):
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
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:interfaces-mib-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Cache.InterfacesMibCounters']['meta_info']


                class DataRate(object):
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
                        self.parent = None
                        self.bandwidth = None
                        self.input_data_rate = None
                        self.input_load = None
                        self.input_packet_rate = None
                        self.load_interval = None
                        self.output_data_rate = None
                        self.output_load = None
                        self.output_packet_rate = None
                        self.peak_input_data_rate = None
                        self.peak_input_packet_rate = None
                        self.peak_output_data_rate = None
                        self.peak_output_packet_rate = None
                        self.reliability = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:data-rate'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bandwidth is not None:
                            return True

                        if self.input_data_rate is not None:
                            return True

                        if self.input_load is not None:
                            return True

                        if self.input_packet_rate is not None:
                            return True

                        if self.load_interval is not None:
                            return True

                        if self.output_data_rate is not None:
                            return True

                        if self.output_load is not None:
                            return True

                        if self.output_packet_rate is not None:
                            return True

                        if self.peak_input_data_rate is not None:
                            return True

                        if self.peak_input_packet_rate is not None:
                            return True

                        if self.peak_output_data_rate is not None:
                            return True

                        if self.peak_output_packet_rate is not None:
                            return True

                        if self.reliability is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Cache.DataRate']['meta_info']


                class GenericCounters(object):
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
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:generic-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Cache.GenericCounters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:cache'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.data_rate is not None and self.data_rate._has_data():
                        return True

                    if self.generic_counters is not None and self.generic_counters._has_data():
                        return True

                    if self.interfaces_mib_counters is not None and self.interfaces_mib_counters._has_data():
                        return True

                    if self.protocols is not None and self.protocols._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.Cache']['meta_info']


            class Latest(object):
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
                    self.parent = None
                    self.data_rate = InfraStatistics.Interfaces.Interface.Latest.DataRate()
                    self.data_rate.parent = self
                    self.generic_counters = InfraStatistics.Interfaces.Interface.Latest.GenericCounters()
                    self.generic_counters.parent = self
                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self.protocols = InfraStatistics.Interfaces.Interface.Latest.Protocols()
                    self.protocols.parent = self


                class Protocols(object):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.protocol = YList()
                        self.protocol.parent = self
                        self.protocol.name = 'protocol'


                    class Protocol(object):
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
                            self.parent = None
                            self.protocol_name = None
                            self.bytes_received = None
                            self.bytes_sent = None
                            self.input_data_rate = None
                            self.input_packet_rate = None
                            self.last_data_time = None
                            self.output_data_rate = None
                            self.output_packet_rate = None
                            self.packets_received = None
                            self.packets_sent = None
                            self.protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.protocol_name is None:
                                raise YPYModelError('Key property protocol_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocol[Cisco-IOS-XR-infra-statsd-oper:protocol-name = ' + str(self.protocol_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.protocol_name is not None:
                                return True

                            if self.bytes_received is not None:
                                return True

                            if self.bytes_sent is not None:
                                return True

                            if self.input_data_rate is not None:
                                return True

                            if self.input_packet_rate is not None:
                                return True

                            if self.last_data_time is not None:
                                return True

                            if self.output_data_rate is not None:
                                return True

                            if self.output_packet_rate is not None:
                                return True

                            if self.packets_received is not None:
                                return True

                            if self.packets_sent is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                            return meta._meta_table['InfraStatistics.Interfaces.Interface.Latest.Protocols.Protocol']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocols'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.protocol is not None:
                            for child_ref in self.protocol:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Latest.Protocols']['meta_info']


                class InterfacesMibCounters(object):
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
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:interfaces-mib-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Latest.InterfacesMibCounters']['meta_info']


                class DataRate(object):
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
                        self.parent = None
                        self.bandwidth = None
                        self.input_data_rate = None
                        self.input_load = None
                        self.input_packet_rate = None
                        self.load_interval = None
                        self.output_data_rate = None
                        self.output_load = None
                        self.output_packet_rate = None
                        self.peak_input_data_rate = None
                        self.peak_input_packet_rate = None
                        self.peak_output_data_rate = None
                        self.peak_output_packet_rate = None
                        self.reliability = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:data-rate'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bandwidth is not None:
                            return True

                        if self.input_data_rate is not None:
                            return True

                        if self.input_load is not None:
                            return True

                        if self.input_packet_rate is not None:
                            return True

                        if self.load_interval is not None:
                            return True

                        if self.output_data_rate is not None:
                            return True

                        if self.output_load is not None:
                            return True

                        if self.output_packet_rate is not None:
                            return True

                        if self.peak_input_data_rate is not None:
                            return True

                        if self.peak_input_packet_rate is not None:
                            return True

                        if self.peak_output_data_rate is not None:
                            return True

                        if self.peak_output_packet_rate is not None:
                            return True

                        if self.reliability is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Latest.DataRate']['meta_info']


                class GenericCounters(object):
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
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:generic-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Latest.GenericCounters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:latest'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.data_rate is not None and self.data_rate._has_data():
                        return True

                    if self.generic_counters is not None and self.generic_counters._has_data():
                        return True

                    if self.interfaces_mib_counters is not None and self.interfaces_mib_counters._has_data():
                        return True

                    if self.protocols is not None and self.protocols._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.Latest']['meta_info']


            class Total(object):
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
                    self.parent = None
                    self.data_rate = InfraStatistics.Interfaces.Interface.Total.DataRate()
                    self.data_rate.parent = self
                    self.generic_counters = InfraStatistics.Interfaces.Interface.Total.GenericCounters()
                    self.generic_counters.parent = self
                    self.interfaces_mib_counters = InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters()
                    self.interfaces_mib_counters.parent = self
                    self.protocols = InfraStatistics.Interfaces.Interface.Total.Protocols()
                    self.protocols.parent = self


                class Protocols(object):
                    """
                    List of protocols
                    
                    .. attribute:: protocol
                    
                    	Interface counters per protocol
                    	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol>`
                    
                    

                    """

                    _prefix = 'infra-statsd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.protocol = YList()
                        self.protocol.parent = self
                        self.protocol.name = 'protocol'


                    class Protocol(object):
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
                            self.parent = None
                            self.protocol_name = None
                            self.bytes_received = None
                            self.bytes_sent = None
                            self.input_data_rate = None
                            self.input_packet_rate = None
                            self.last_data_time = None
                            self.output_data_rate = None
                            self.output_packet_rate = None
                            self.packets_received = None
                            self.packets_sent = None
                            self.protocol = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.protocol_name is None:
                                raise YPYModelError('Key property protocol_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocol[Cisco-IOS-XR-infra-statsd-oper:protocol-name = ' + str(self.protocol_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.protocol_name is not None:
                                return True

                            if self.bytes_received is not None:
                                return True

                            if self.bytes_sent is not None:
                                return True

                            if self.input_data_rate is not None:
                                return True

                            if self.input_packet_rate is not None:
                                return True

                            if self.last_data_time is not None:
                                return True

                            if self.output_data_rate is not None:
                                return True

                            if self.output_packet_rate is not None:
                                return True

                            if self.packets_received is not None:
                                return True

                            if self.packets_sent is not None:
                                return True

                            if self.protocol is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                            return meta._meta_table['InfraStatistics.Interfaces.Interface.Total.Protocols.Protocol']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocols'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.protocol is not None:
                            for child_ref in self.protocol:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Total.Protocols']['meta_info']


                class InterfacesMibCounters(object):
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
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:interfaces-mib-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Total.InterfacesMibCounters']['meta_info']


                class DataRate(object):
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
                        self.parent = None
                        self.bandwidth = None
                        self.input_data_rate = None
                        self.input_load = None
                        self.input_packet_rate = None
                        self.load_interval = None
                        self.output_data_rate = None
                        self.output_load = None
                        self.output_packet_rate = None
                        self.peak_input_data_rate = None
                        self.peak_input_packet_rate = None
                        self.peak_output_data_rate = None
                        self.peak_output_packet_rate = None
                        self.reliability = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:data-rate'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bandwidth is not None:
                            return True

                        if self.input_data_rate is not None:
                            return True

                        if self.input_load is not None:
                            return True

                        if self.input_packet_rate is not None:
                            return True

                        if self.load_interval is not None:
                            return True

                        if self.output_data_rate is not None:
                            return True

                        if self.output_load is not None:
                            return True

                        if self.output_packet_rate is not None:
                            return True

                        if self.peak_input_data_rate is not None:
                            return True

                        if self.peak_input_packet_rate is not None:
                            return True

                        if self.peak_output_data_rate is not None:
                            return True

                        if self.peak_output_packet_rate is not None:
                            return True

                        if self.reliability is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Total.DataRate']['meta_info']


                class GenericCounters(object):
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
                        self.parent = None
                        self.applique = None
                        self.availability_flag = None
                        self.broadcast_packets_received = None
                        self.broadcast_packets_sent = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.carrier_transitions = None
                        self.crc_errors = None
                        self.framing_errors_received = None
                        self.giant_packets_received = None
                        self.input_aborts = None
                        self.input_drops = None
                        self.input_errors = None
                        self.input_ignored_packets = None
                        self.input_overruns = None
                        self.input_queue_drops = None
                        self.last_data_time = None
                        self.last_discontinuity_time = None
                        self.multicast_packets_received = None
                        self.multicast_packets_sent = None
                        self.output_buffer_failures = None
                        self.output_buffers_swapped_out = None
                        self.output_drops = None
                        self.output_errors = None
                        self.output_queue_drops = None
                        self.output_underruns = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.parity_packets_received = None
                        self.resets = None
                        self.runt_packets_received = None
                        self.seconds_since_last_clear_counters = None
                        self.seconds_since_packet_received = None
                        self.seconds_since_packet_sent = None
                        self.throttled_packets_received = None
                        self.unknown_protocol_packets_received = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:generic-counters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.applique is not None:
                            return True

                        if self.availability_flag is not None:
                            return True

                        if self.broadcast_packets_received is not None:
                            return True

                        if self.broadcast_packets_sent is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.carrier_transitions is not None:
                            return True

                        if self.crc_errors is not None:
                            return True

                        if self.framing_errors_received is not None:
                            return True

                        if self.giant_packets_received is not None:
                            return True

                        if self.input_aborts is not None:
                            return True

                        if self.input_drops is not None:
                            return True

                        if self.input_errors is not None:
                            return True

                        if self.input_ignored_packets is not None:
                            return True

                        if self.input_overruns is not None:
                            return True

                        if self.input_queue_drops is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.last_discontinuity_time is not None:
                            return True

                        if self.multicast_packets_received is not None:
                            return True

                        if self.multicast_packets_sent is not None:
                            return True

                        if self.output_buffer_failures is not None:
                            return True

                        if self.output_buffers_swapped_out is not None:
                            return True

                        if self.output_drops is not None:
                            return True

                        if self.output_errors is not None:
                            return True

                        if self.output_queue_drops is not None:
                            return True

                        if self.output_underruns is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.parity_packets_received is not None:
                            return True

                        if self.resets is not None:
                            return True

                        if self.runt_packets_received is not None:
                            return True

                        if self.seconds_since_last_clear_counters is not None:
                            return True

                        if self.seconds_since_packet_received is not None:
                            return True

                        if self.seconds_since_packet_sent is not None:
                            return True

                        if self.throttled_packets_received is not None:
                            return True

                        if self.unknown_protocol_packets_received is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Total.GenericCounters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:total'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.data_rate is not None and self.data_rate._has_data():
                        return True

                    if self.generic_counters is not None and self.generic_counters._has_data():
                        return True

                    if self.interfaces_mib_counters is not None and self.interfaces_mib_counters._has_data():
                        return True

                    if self.protocols is not None and self.protocols._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.Total']['meta_info']


            class Protocols(object):
                """
                List of protocols
                
                .. attribute:: protocol
                
                	Interface counters per protocol
                	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_oper.InfraStatistics.Interfaces.Interface.Protocols.Protocol>`
                
                

                """

                _prefix = 'infra-statsd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.protocol = YList()
                    self.protocol.parent = self
                    self.protocol.name = 'protocol'


                class Protocol(object):
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
                        self.parent = None
                        self.protocol_name = None
                        self.bytes_received = None
                        self.bytes_sent = None
                        self.input_data_rate = None
                        self.input_packet_rate = None
                        self.last_data_time = None
                        self.output_data_rate = None
                        self.output_packet_rate = None
                        self.packets_received = None
                        self.packets_sent = None
                        self.protocol = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.protocol_name is None:
                            raise YPYModelError('Key property protocol_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocol[Cisco-IOS-XR-infra-statsd-oper:protocol-name = ' + str(self.protocol_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.protocol_name is not None:
                            return True

                        if self.bytes_received is not None:
                            return True

                        if self.bytes_sent is not None:
                            return True

                        if self.input_data_rate is not None:
                            return True

                        if self.input_packet_rate is not None:
                            return True

                        if self.last_data_time is not None:
                            return True

                        if self.output_data_rate is not None:
                            return True

                        if self.output_packet_rate is not None:
                            return True

                        if self.packets_received is not None:
                            return True

                        if self.packets_sent is not None:
                            return True

                        if self.protocol is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                        return meta._meta_table['InfraStatistics.Interfaces.Interface.Protocols.Protocol']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:protocols'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.protocol is not None:
                        for child_ref in self.protocol:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.Protocols']['meta_info']


            class InterfacesMibCounters(object):
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
                    self.parent = None
                    self.applique = None
                    self.availability_flag = None
                    self.broadcast_packets_received = None
                    self.broadcast_packets_sent = None
                    self.bytes_received = None
                    self.bytes_sent = None
                    self.carrier_transitions = None
                    self.crc_errors = None
                    self.framing_errors_received = None
                    self.giant_packets_received = None
                    self.input_aborts = None
                    self.input_drops = None
                    self.input_errors = None
                    self.input_ignored_packets = None
                    self.input_overruns = None
                    self.input_queue_drops = None
                    self.last_data_time = None
                    self.last_discontinuity_time = None
                    self.multicast_packets_received = None
                    self.multicast_packets_sent = None
                    self.output_buffer_failures = None
                    self.output_buffers_swapped_out = None
                    self.output_drops = None
                    self.output_errors = None
                    self.output_queue_drops = None
                    self.output_underruns = None
                    self.packets_received = None
                    self.packets_sent = None
                    self.parity_packets_received = None
                    self.resets = None
                    self.runt_packets_received = None
                    self.seconds_since_last_clear_counters = None
                    self.seconds_since_packet_received = None
                    self.seconds_since_packet_sent = None
                    self.throttled_packets_received = None
                    self.unknown_protocol_packets_received = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:interfaces-mib-counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.applique is not None:
                        return True

                    if self.availability_flag is not None:
                        return True

                    if self.broadcast_packets_received is not None:
                        return True

                    if self.broadcast_packets_sent is not None:
                        return True

                    if self.bytes_received is not None:
                        return True

                    if self.bytes_sent is not None:
                        return True

                    if self.carrier_transitions is not None:
                        return True

                    if self.crc_errors is not None:
                        return True

                    if self.framing_errors_received is not None:
                        return True

                    if self.giant_packets_received is not None:
                        return True

                    if self.input_aborts is not None:
                        return True

                    if self.input_drops is not None:
                        return True

                    if self.input_errors is not None:
                        return True

                    if self.input_ignored_packets is not None:
                        return True

                    if self.input_overruns is not None:
                        return True

                    if self.input_queue_drops is not None:
                        return True

                    if self.last_data_time is not None:
                        return True

                    if self.last_discontinuity_time is not None:
                        return True

                    if self.multicast_packets_received is not None:
                        return True

                    if self.multicast_packets_sent is not None:
                        return True

                    if self.output_buffer_failures is not None:
                        return True

                    if self.output_buffers_swapped_out is not None:
                        return True

                    if self.output_drops is not None:
                        return True

                    if self.output_errors is not None:
                        return True

                    if self.output_queue_drops is not None:
                        return True

                    if self.output_underruns is not None:
                        return True

                    if self.packets_received is not None:
                        return True

                    if self.packets_sent is not None:
                        return True

                    if self.parity_packets_received is not None:
                        return True

                    if self.resets is not None:
                        return True

                    if self.runt_packets_received is not None:
                        return True

                    if self.seconds_since_last_clear_counters is not None:
                        return True

                    if self.seconds_since_packet_received is not None:
                        return True

                    if self.seconds_since_packet_sent is not None:
                        return True

                    if self.throttled_packets_received is not None:
                        return True

                    if self.unknown_protocol_packets_received is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.InterfacesMibCounters']['meta_info']


            class DataRate(object):
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
                    self.parent = None
                    self.bandwidth = None
                    self.input_data_rate = None
                    self.input_load = None
                    self.input_packet_rate = None
                    self.load_interval = None
                    self.output_data_rate = None
                    self.output_load = None
                    self.output_packet_rate = None
                    self.peak_input_data_rate = None
                    self.peak_input_packet_rate = None
                    self.peak_output_data_rate = None
                    self.peak_output_packet_rate = None
                    self.reliability = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:data-rate'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bandwidth is not None:
                        return True

                    if self.input_data_rate is not None:
                        return True

                    if self.input_load is not None:
                        return True

                    if self.input_packet_rate is not None:
                        return True

                    if self.load_interval is not None:
                        return True

                    if self.output_data_rate is not None:
                        return True

                    if self.output_load is not None:
                        return True

                    if self.output_packet_rate is not None:
                        return True

                    if self.peak_input_data_rate is not None:
                        return True

                    if self.peak_input_packet_rate is not None:
                        return True

                    if self.peak_output_data_rate is not None:
                        return True

                    if self.peak_output_packet_rate is not None:
                        return True

                    if self.reliability is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.DataRate']['meta_info']


            class GenericCounters(object):
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
                    self.parent = None
                    self.applique = None
                    self.availability_flag = None
                    self.broadcast_packets_received = None
                    self.broadcast_packets_sent = None
                    self.bytes_received = None
                    self.bytes_sent = None
                    self.carrier_transitions = None
                    self.crc_errors = None
                    self.framing_errors_received = None
                    self.giant_packets_received = None
                    self.input_aborts = None
                    self.input_drops = None
                    self.input_errors = None
                    self.input_ignored_packets = None
                    self.input_overruns = None
                    self.input_queue_drops = None
                    self.last_data_time = None
                    self.last_discontinuity_time = None
                    self.multicast_packets_received = None
                    self.multicast_packets_sent = None
                    self.output_buffer_failures = None
                    self.output_buffers_swapped_out = None
                    self.output_drops = None
                    self.output_errors = None
                    self.output_queue_drops = None
                    self.output_underruns = None
                    self.packets_received = None
                    self.packets_sent = None
                    self.parity_packets_received = None
                    self.resets = None
                    self.runt_packets_received = None
                    self.seconds_since_last_clear_counters = None
                    self.seconds_since_packet_received = None
                    self.seconds_since_packet_sent = None
                    self.throttled_packets_received = None
                    self.unknown_protocol_packets_received = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-statsd-oper:generic-counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.applique is not None:
                        return True

                    if self.availability_flag is not None:
                        return True

                    if self.broadcast_packets_received is not None:
                        return True

                    if self.broadcast_packets_sent is not None:
                        return True

                    if self.bytes_received is not None:
                        return True

                    if self.bytes_sent is not None:
                        return True

                    if self.carrier_transitions is not None:
                        return True

                    if self.crc_errors is not None:
                        return True

                    if self.framing_errors_received is not None:
                        return True

                    if self.giant_packets_received is not None:
                        return True

                    if self.input_aborts is not None:
                        return True

                    if self.input_drops is not None:
                        return True

                    if self.input_errors is not None:
                        return True

                    if self.input_ignored_packets is not None:
                        return True

                    if self.input_overruns is not None:
                        return True

                    if self.input_queue_drops is not None:
                        return True

                    if self.last_data_time is not None:
                        return True

                    if self.last_discontinuity_time is not None:
                        return True

                    if self.multicast_packets_received is not None:
                        return True

                    if self.multicast_packets_sent is not None:
                        return True

                    if self.output_buffer_failures is not None:
                        return True

                    if self.output_buffers_swapped_out is not None:
                        return True

                    if self.output_drops is not None:
                        return True

                    if self.output_errors is not None:
                        return True

                    if self.output_queue_drops is not None:
                        return True

                    if self.output_underruns is not None:
                        return True

                    if self.packets_received is not None:
                        return True

                    if self.packets_sent is not None:
                        return True

                    if self.parity_packets_received is not None:
                        return True

                    if self.resets is not None:
                        return True

                    if self.runt_packets_received is not None:
                        return True

                    if self.seconds_since_last_clear_counters is not None:
                        return True

                    if self.seconds_since_packet_received is not None:
                        return True

                    if self.seconds_since_packet_sent is not None:
                        return True

                    if self.throttled_packets_received is not None:
                        return True

                    if self.unknown_protocol_packets_received is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                    return meta._meta_table['InfraStatistics.Interfaces.Interface.GenericCounters']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-infra-statsd-oper:infra-statistics/Cisco-IOS-XR-infra-statsd-oper:interfaces/Cisco-IOS-XR-infra-statsd-oper:interface[Cisco-IOS-XR-infra-statsd-oper:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.cache is not None and self.cache._has_data():
                    return True

                if self.data_rate is not None and self.data_rate._has_data():
                    return True

                if self.generic_counters is not None and self.generic_counters._has_data():
                    return True

                if self.interfaces_mib_counters is not None and self.interfaces_mib_counters._has_data():
                    return True

                if self.latest is not None and self.latest._has_data():
                    return True

                if self.protocols is not None and self.protocols._has_data():
                    return True

                if self.total is not None and self.total._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
                return meta._meta_table['InfraStatistics.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-statsd-oper:infra-statistics/Cisco-IOS-XR-infra-statsd-oper:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
            return meta._meta_table['InfraStatistics.Interfaces']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-statsd-oper:infra-statistics'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.interfaces is not None and self.interfaces._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_statsd_oper as meta
        return meta._meta_table['InfraStatistics']['meta_info']


