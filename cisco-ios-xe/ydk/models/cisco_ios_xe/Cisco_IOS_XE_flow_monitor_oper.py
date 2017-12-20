""" Cisco_IOS_XE_flow_monitor_oper 

This module contains a collection of YANG definitions
for Flexible NetFlow Operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FlowMonitors(Entity):
    """
    All of the flow monitors
    
    .. attribute:: flow_monitor
    
    	List of Flow monitors
    	**type**\: list of  		 :py:class:`FlowMonitor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor>`
    
    

    """

    _prefix = 'flow-monitor-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(FlowMonitors, self).__init__()
        self._top_entity = None

        self.yang_name = "flow-monitors"
        self.yang_parent_name = "Cisco-IOS-XE-flow-monitor-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"flow-monitor" : ("flow_monitor", FlowMonitors.FlowMonitor)}

        self.flow_monitor = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors"

    def __setattr__(self, name, value):
        self._perform_setattr(FlowMonitors, [], name, value)


    class FlowMonitor(Entity):
        """
        List of Flow monitors
        
        .. attribute:: name  <key>
        
        	Name of the flow monitor
        	**type**\: str
        
        .. attribute:: time_collected
        
        	Time the flow monitor data was collected in seconds
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flows
        
        	All the flows for this flow monitor
        	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows>`
        
        

        """

        _prefix = 'flow-monitor-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(FlowMonitors.FlowMonitor, self).__init__()

            self.yang_name = "flow-monitor"
            self.yang_parent_name = "flow-monitors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"flows" : ("flows", FlowMonitors.FlowMonitor.Flows)}
            self._child_list_classes = {}

            self.name = YLeaf(YType.str, "name")

            self.time_collected = YLeaf(YType.uint64, "time-collected")

            self.flows = FlowMonitors.FlowMonitor.Flows()
            self.flows.parent = self
            self._children_name_map["flows"] = "flows"
            self._children_yang_names.add("flows")
            self._segment_path = lambda: "flow-monitor" + "[name='" + self.name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FlowMonitors.FlowMonitor, ['name', 'time_collected'], name, value)


        class Flows(Entity):
            """
            All the flows for this flow monitor
            
            .. attribute:: flow
            
            	List of flows
            	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows.Flow>`
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(FlowMonitors.FlowMonitor.Flows, self).__init__()

                self.yang_name = "flows"
                self.yang_parent_name = "flow-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"flow" : ("flow", FlowMonitors.FlowMonitor.Flows.Flow)}

                self.flow = YList(self)
                self._segment_path = lambda: "flows"

            def __setattr__(self, name, value):
                self._perform_setattr(FlowMonitors.FlowMonitor.Flows, [], name, value)


            class Flow(Entity):
                """
                List of flows
                
                .. attribute:: source_address  <key>
                
                	Source address of the flow
                	**type**\: str
                
                .. attribute:: destination_address  <key>
                
                	Destination address of the flow
                	**type**\: str
                
                .. attribute:: interface_input  <key>
                
                	Input interface of the flow
                	**type**\: str
                
                .. attribute:: is_multicast  <key>
                
                	Multicast flow
                	**type**\: str
                
                .. attribute:: vrf_id_input  <key>
                
                	VRF ID input
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: source_port  <key>
                
                	Source port number
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: destination_port  <key>
                
                	Destination port number
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: ip_tos  <key>
                
                	ip\-tos value
                	**type**\: str
                
                .. attribute:: ip_protocol  <key>
                
                	IP protocol number
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: interface_output
                
                	Output interface of the flow
                	**type**\: str
                
                .. attribute:: bytes
                
                	Number of bytes passed through
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: packets
                
                	Number of packets passed through
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                

                """

                _prefix = 'flow-monitor-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(FlowMonitors.FlowMonitor.Flows.Flow, self).__init__()

                    self.yang_name = "flow"
                    self.yang_parent_name = "flows"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.interface_input = YLeaf(YType.str, "interface-input")

                    self.is_multicast = YLeaf(YType.str, "is-multicast")

                    self.vrf_id_input = YLeaf(YType.int64, "vrf-id-input")

                    self.source_port = YLeaf(YType.int64, "source-port")

                    self.destination_port = YLeaf(YType.int64, "destination-port")

                    self.ip_tos = YLeaf(YType.str, "ip-tos")

                    self.ip_protocol = YLeaf(YType.int64, "ip-protocol")

                    self.interface_output = YLeaf(YType.str, "interface-output")

                    self.bytes = YLeaf(YType.int64, "bytes")

                    self.packets = YLeaf(YType.int64, "packets")
                    self._segment_path = lambda: "flow" + "[source-address='" + self.source_address.get() + "']" + "[destination-address='" + self.destination_address.get() + "']" + "[interface-input='" + self.interface_input.get() + "']" + "[is-multicast='" + self.is_multicast.get() + "']" + "[vrf-id-input='" + self.vrf_id_input.get() + "']" + "[source-port='" + self.source_port.get() + "']" + "[destination-port='" + self.destination_port.get() + "']" + "[ip-tos='" + self.ip_tos.get() + "']" + "[ip-protocol='" + self.ip_protocol.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowMonitors.FlowMonitor.Flows.Flow, ['source_address', 'destination_address', 'interface_input', 'is_multicast', 'vrf_id_input', 'source_port', 'destination_port', 'ip_tos', 'ip_protocol', 'interface_output', 'bytes', 'packets'], name, value)

    def clone_ptr(self):
        self._top_entity = FlowMonitors()
        return self._top_entity

