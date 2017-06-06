""" Cisco_IOS_XE_flow_monitor_oper 

This module contains a collection of YANG definitions for Flexible NetFlow Operational dataCopyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class FlowMonitors(object):
    """
    All of the flow monitors
    
    .. attribute:: flow_monitor
    
    	A flow monitor
    	**type**\: list of    :py:class:`FlowMonitor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor>`
    
    

    """

    _prefix = 'flow-monitor-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.flow_monitor = YList()
        self.flow_monitor.parent = self
        self.flow_monitor.name = 'flow_monitor'


    class FlowMonitor(object):
        """
        A flow monitor
        
        .. attribute:: name  <key>
        
        	Name of the flow monitor
        	**type**\:  str
        
        .. attribute:: flows
        
        	All the flows for this flow monitor
        	**type**\:   :py:class:`Flows <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows>`
        
        .. attribute:: time_collected
        
        	Time the flow monitor data was collected in seconds
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'flow-monitor-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.name = None
            self.flows = FlowMonitors.FlowMonitor.Flows()
            self.flows.parent = self
            self.time_collected = None


        class Flows(object):
            """
            All the flows for this flow monitor
            
            .. attribute:: flow
            
            	A flow
            	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows.Flow>`
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.flow = YList()
                self.flow.parent = self
                self.flow.name = 'flow'


            class Flow(object):
                """
                A flow
                
                .. attribute:: source_address  <key>
                
                	Source address of the flow
                	**type**\:  str
                
                .. attribute:: destination_address  <key>
                
                	Destination address of the flow
                	**type**\:  str
                
                .. attribute:: interface_input  <key>
                
                	Input interface of the flow
                	**type**\:  str
                
                .. attribute:: is_multicast  <key>
                
                	Multicast flow
                	**type**\:  str
                
                .. attribute:: vrf_id_input  <key>
                
                	Vrf id input
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: source_port  <key>
                
                	The source port number
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: destination_port  <key>
                
                	The destination port number
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: ip_tos  <key>
                
                	ip\-tos value
                	**type**\:  str
                
                .. attribute:: ip_protocol  <key>
                
                	IP protocol number
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: bytes
                
                	Number of bytes passed through
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: interface_output
                
                	Output interface of the flow
                	**type**\:  str
                
                .. attribute:: packets
                
                	Number of packets passed through
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                

                """

                _prefix = 'flow-monitor-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.source_address = None
                    self.destination_address = None
                    self.interface_input = None
                    self.is_multicast = None
                    self.vrf_id_input = None
                    self.source_port = None
                    self.destination_port = None
                    self.ip_tos = None
                    self.ip_protocol = None
                    self.bytes = None
                    self.interface_output = None
                    self.packets = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.source_address is None:
                        raise YPYModelError('Key property source_address is None')
                    if self.destination_address is None:
                        raise YPYModelError('Key property destination_address is None')
                    if self.interface_input is None:
                        raise YPYModelError('Key property interface_input is None')
                    if self.is_multicast is None:
                        raise YPYModelError('Key property is_multicast is None')
                    if self.vrf_id_input is None:
                        raise YPYModelError('Key property vrf_id_input is None')
                    if self.source_port is None:
                        raise YPYModelError('Key property source_port is None')
                    if self.destination_port is None:
                        raise YPYModelError('Key property destination_port is None')
                    if self.ip_tos is None:
                        raise YPYModelError('Key property ip_tos is None')
                    if self.ip_protocol is None:
                        raise YPYModelError('Key property ip_protocol is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-flow-monitor-oper:flow[Cisco-IOS-XE-flow-monitor-oper:source-address = ' + str(self.source_address) + '][Cisco-IOS-XE-flow-monitor-oper:destination-address = ' + str(self.destination_address) + '][Cisco-IOS-XE-flow-monitor-oper:interface-input = ' + str(self.interface_input) + '][Cisco-IOS-XE-flow-monitor-oper:is-multicast = ' + str(self.is_multicast) + '][Cisco-IOS-XE-flow-monitor-oper:vrf-id-input = ' + str(self.vrf_id_input) + '][Cisco-IOS-XE-flow-monitor-oper:source-port = ' + str(self.source_port) + '][Cisco-IOS-XE-flow-monitor-oper:destination-port = ' + str(self.destination_port) + '][Cisco-IOS-XE-flow-monitor-oper:ip-tos = ' + str(self.ip_tos) + '][Cisco-IOS-XE-flow-monitor-oper:ip-protocol = ' + str(self.ip_protocol) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.source_address is not None:
                        return True

                    if self.destination_address is not None:
                        return True

                    if self.interface_input is not None:
                        return True

                    if self.is_multicast is not None:
                        return True

                    if self.vrf_id_input is not None:
                        return True

                    if self.source_port is not None:
                        return True

                    if self.destination_port is not None:
                        return True

                    if self.ip_tos is not None:
                        return True

                    if self.ip_protocol is not None:
                        return True

                    if self.bytes is not None:
                        return True

                    if self.interface_output is not None:
                        return True

                    if self.packets is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_flow_monitor_oper as meta
                    return meta._meta_table['FlowMonitors.FlowMonitor.Flows.Flow']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-flow-monitor-oper:flows'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.flow is not None:
                    for child_ref in self.flow:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_flow_monitor_oper as meta
                return meta._meta_table['FlowMonitors.FlowMonitor.Flows']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/Cisco-IOS-XE-flow-monitor-oper:flow-monitors/Cisco-IOS-XE-flow-monitor-oper:flow-monitor[Cisco-IOS-XE-flow-monitor-oper:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.flows is not None and self.flows._has_data():
                return True

            if self.time_collected is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_flow_monitor_oper as meta
            return meta._meta_table['FlowMonitors.FlowMonitor']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-flow-monitor-oper:flow-monitors'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.flow_monitor is not None:
            for child_ref in self.flow_monitor:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_flow_monitor_oper as meta
        return meta._meta_table['FlowMonitors']['meta_info']


