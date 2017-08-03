""" Cisco_IOS_XE_flow_monitor_oper 

This module contains a collection of YANG definitions
for Flexible NetFlow Operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FlowMonitors(Entity):
    """
    All of the flow monitors
    
    .. attribute:: flow_monitor
    
    	List of Flow monitors
    	**type**\: list of    :py:class:`FlowMonitor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor>`
    
    

    """

    _prefix = 'flow-monitor-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(FlowMonitors, self).__init__()
        self._top_entity = None

        self.yang_name = "flow-monitors"
        self.yang_parent_name = "Cisco-IOS-XE-flow-monitor-oper"

        self.flow_monitor = YList(self)

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
                    super(FlowMonitors, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(FlowMonitors, self).__setattr__(name, value)


    class FlowMonitor(Entity):
        """
        List of Flow monitors
        
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
        _revision = '2017-04-01'

        def __init__(self):
            super(FlowMonitors.FlowMonitor, self).__init__()

            self.yang_name = "flow-monitor"
            self.yang_parent_name = "flow-monitors"

            self.name = YLeaf(YType.str, "name")

            self.time_collected = YLeaf(YType.uint64, "time-collected")

            self.flows = FlowMonitors.FlowMonitor.Flows()
            self.flows.parent = self
            self._children_name_map["flows"] = "flows"
            self._children_yang_names.add("flows")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name",
                            "time_collected") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(FlowMonitors.FlowMonitor, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FlowMonitors.FlowMonitor, self).__setattr__(name, value)


        class Flows(Entity):
            """
            All the flows for this flow monitor
            
            .. attribute:: flow
            
            	List of flows
            	**type**\: list of    :py:class:`Flow <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows.Flow>`
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(FlowMonitors.FlowMonitor.Flows, self).__init__()

                self.yang_name = "flows"
                self.yang_parent_name = "flow-monitor"

                self.flow = YList(self)

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
                            super(FlowMonitors.FlowMonitor.Flows, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FlowMonitors.FlowMonitor.Flows, self).__setattr__(name, value)


            class Flow(Entity):
                """
                List of flows
                
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
                
                	VRF ID input
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: source_port  <key>
                
                	Source port number
                	**type**\:  int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: destination_port  <key>
                
                	Destination port number
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
                _revision = '2017-04-01'

                def __init__(self):
                    super(FlowMonitors.FlowMonitor.Flows.Flow, self).__init__()

                    self.yang_name = "flow"
                    self.yang_parent_name = "flows"

                    self.source_address = YLeaf(YType.str, "source-address")

                    self.destination_address = YLeaf(YType.str, "destination-address")

                    self.interface_input = YLeaf(YType.str, "interface-input")

                    self.is_multicast = YLeaf(YType.str, "is-multicast")

                    self.vrf_id_input = YLeaf(YType.int64, "vrf-id-input")

                    self.source_port = YLeaf(YType.int64, "source-port")

                    self.destination_port = YLeaf(YType.int64, "destination-port")

                    self.ip_tos = YLeaf(YType.str, "ip-tos")

                    self.ip_protocol = YLeaf(YType.int64, "ip-protocol")

                    self.bytes = YLeaf(YType.int64, "bytes")

                    self.interface_output = YLeaf(YType.str, "interface-output")

                    self.packets = YLeaf(YType.int64, "packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("source_address",
                                    "destination_address",
                                    "interface_input",
                                    "is_multicast",
                                    "vrf_id_input",
                                    "source_port",
                                    "destination_port",
                                    "ip_tos",
                                    "ip_protocol",
                                    "bytes",
                                    "interface_output",
                                    "packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(FlowMonitors.FlowMonitor.Flows.Flow, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(FlowMonitors.FlowMonitor.Flows.Flow, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.source_address.is_set or
                        self.destination_address.is_set or
                        self.interface_input.is_set or
                        self.is_multicast.is_set or
                        self.vrf_id_input.is_set or
                        self.source_port.is_set or
                        self.destination_port.is_set or
                        self.ip_tos.is_set or
                        self.ip_protocol.is_set or
                        self.bytes.is_set or
                        self.interface_output.is_set or
                        self.packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.source_address.yfilter != YFilter.not_set or
                        self.destination_address.yfilter != YFilter.not_set or
                        self.interface_input.yfilter != YFilter.not_set or
                        self.is_multicast.yfilter != YFilter.not_set or
                        self.vrf_id_input.yfilter != YFilter.not_set or
                        self.source_port.yfilter != YFilter.not_set or
                        self.destination_port.yfilter != YFilter.not_set or
                        self.ip_tos.yfilter != YFilter.not_set or
                        self.ip_protocol.yfilter != YFilter.not_set or
                        self.bytes.yfilter != YFilter.not_set or
                        self.interface_output.yfilter != YFilter.not_set or
                        self.packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "flow" + "[source-address='" + self.source_address.get() + "']" + "[destination-address='" + self.destination_address.get() + "']" + "[interface-input='" + self.interface_input.get() + "']" + "[is-multicast='" + self.is_multicast.get() + "']" + "[vrf-id-input='" + self.vrf_id_input.get() + "']" + "[source-port='" + self.source_port.get() + "']" + "[destination-port='" + self.destination_port.get() + "']" + "[ip-tos='" + self.ip_tos.get() + "']" + "[ip-protocol='" + self.ip_protocol.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_address.get_name_leafdata())
                    if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_address.get_name_leafdata())
                    if (self.interface_input.is_set or self.interface_input.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_input.get_name_leafdata())
                    if (self.is_multicast.is_set or self.is_multicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_multicast.get_name_leafdata())
                    if (self.vrf_id_input.is_set or self.vrf_id_input.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_id_input.get_name_leafdata())
                    if (self.source_port.is_set or self.source_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_port.get_name_leafdata())
                    if (self.destination_port.is_set or self.destination_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_port.get_name_leafdata())
                    if (self.ip_tos.is_set or self.ip_tos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_tos.get_name_leafdata())
                    if (self.ip_protocol.is_set or self.ip_protocol.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_protocol.get_name_leafdata())
                    if (self.bytes.is_set or self.bytes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes.get_name_leafdata())
                    if (self.interface_output.is_set or self.interface_output.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_output.get_name_leafdata())
                    if (self.packets.is_set or self.packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "source-address" or name == "destination-address" or name == "interface-input" or name == "is-multicast" or name == "vrf-id-input" or name == "source-port" or name == "destination-port" or name == "ip-tos" or name == "ip-protocol" or name == "bytes" or name == "interface-output" or name == "packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "source-address"):
                        self.source_address = value
                        self.source_address.value_namespace = name_space
                        self.source_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-address"):
                        self.destination_address = value
                        self.destination_address.value_namespace = name_space
                        self.destination_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-input"):
                        self.interface_input = value
                        self.interface_input.value_namespace = name_space
                        self.interface_input.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-multicast"):
                        self.is_multicast = value
                        self.is_multicast.value_namespace = name_space
                        self.is_multicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-id-input"):
                        self.vrf_id_input = value
                        self.vrf_id_input.value_namespace = name_space
                        self.vrf_id_input.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-port"):
                        self.source_port = value
                        self.source_port.value_namespace = name_space
                        self.source_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-port"):
                        self.destination_port = value
                        self.destination_port.value_namespace = name_space
                        self.destination_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-tos"):
                        self.ip_tos = value
                        self.ip_tos.value_namespace = name_space
                        self.ip_tos.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-protocol"):
                        self.ip_protocol = value
                        self.ip_protocol.value_namespace = name_space
                        self.ip_protocol.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes"):
                        self.bytes = value
                        self.bytes.value_namespace = name_space
                        self.bytes.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-output"):
                        self.interface_output = value
                        self.interface_output.value_namespace = name_space
                        self.interface_output.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets"):
                        self.packets = value
                        self.packets.value_namespace = name_space
                        self.packets.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.flow:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.flow:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "flows" + path_buffer

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

                if (child_yang_name == "flow"):
                    for c in self.flow:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = FlowMonitors.FlowMonitor.Flows.Flow()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.flow.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "flow"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.name.is_set or
                self.time_collected.is_set or
                (self.flows is not None and self.flows.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.time_collected.yfilter != YFilter.not_set or
                (self.flows is not None and self.flows.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "flow-monitor" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-flow-monitor-oper:flow-monitors/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.time_collected.is_set or self.time_collected.yfilter != YFilter.not_set):
                leaf_name_data.append(self.time_collected.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "flows"):
                if (self.flows is None):
                    self.flows = FlowMonitors.FlowMonitor.Flows()
                    self.flows.parent = self
                    self._children_name_map["flows"] = "flows"
                return self.flows

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "flows" or name == "name" or name == "time-collected"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "time-collected"):
                self.time_collected = value
                self.time_collected.value_namespace = name_space
                self.time_collected.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.flow_monitor:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.flow_monitor:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-flow-monitor-oper:flow-monitors" + path_buffer

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

        if (child_yang_name == "flow-monitor"):
            for c in self.flow_monitor:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = FlowMonitors.FlowMonitor()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.flow_monitor.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "flow-monitor"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = FlowMonitors()
        return self._top_entity

