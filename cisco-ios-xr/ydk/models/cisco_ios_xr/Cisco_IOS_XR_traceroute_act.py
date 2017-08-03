""" Cisco_IOS_XR_traceroute_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ping action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Traceroute(Entity):
    """
    Trace route to destination
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output>`
    
    

    """

    _prefix = 'traceroute-act'
    _revision = '2016-09-28'

    def __init__(self):
        super(Traceroute, self).__init__()
        self._top_entity = None

        self.yang_name = "traceroute"
        self.yang_parent_name = "Cisco-IOS-XR-traceroute-act"

        self.input = Traceroute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Traceroute.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Input.Ipv6>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Traceroute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "traceroute"

            self.destination = Traceroute.Input.Destination()
            self.destination.parent = self
            self._children_name_map["destination"] = "destination"
            self._children_yang_names.add("destination")

            self.ipv4 = Traceroute.Input.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._children_yang_names.add("ipv4")

            self.ipv6 = Traceroute.Input.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")


        class Destination(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\:  str
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"

                self.destination = YLeaf(YType.str, "destination")

                self.max_ttl = YLeaf(YType.uint16, "max-ttl")

                self.min_ttl = YLeaf(YType.uint16, "min-ttl")

                self.numeric = YLeaf(YType.boolean, "numeric")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.port = YLeaf(YType.uint32, "port")

                self.priority = YLeaf(YType.uint16, "priority")

                self.probe = YLeaf(YType.uint16, "probe")

                self.source = YLeaf(YType.str, "source")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("destination",
                                "max_ttl",
                                "min_ttl",
                                "numeric",
                                "outgoing_interface",
                                "port",
                                "priority",
                                "probe",
                                "source",
                                "timeout",
                                "verbose",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Traceroute.Input.Destination, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Traceroute.Input.Destination, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.destination.is_set or
                    self.max_ttl.is_set or
                    self.min_ttl.is_set or
                    self.numeric.is_set or
                    self.outgoing_interface.is_set or
                    self.port.is_set or
                    self.priority.is_set or
                    self.probe.is_set or
                    self.source.is_set or
                    self.timeout.is_set or
                    self.verbose.is_set or
                    self.vrf_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination.yfilter != YFilter.not_set or
                    self.max_ttl.yfilter != YFilter.not_set or
                    self.min_ttl.yfilter != YFilter.not_set or
                    self.numeric.yfilter != YFilter.not_set or
                    self.outgoing_interface.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.priority.yfilter != YFilter.not_set or
                    self.probe.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.verbose.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "destination" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination.get_name_leafdata())
                if (self.max_ttl.is_set or self.max_ttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_ttl.get_name_leafdata())
                if (self.min_ttl.is_set or self.min_ttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.min_ttl.get_name_leafdata())
                if (self.numeric.is_set or self.numeric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.numeric.get_name_leafdata())
                if (self.outgoing_interface.is_set or self.outgoing_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.outgoing_interface.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.priority.get_name_leafdata())
                if (self.probe.is_set or self.probe.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.probe.get_name_leafdata())
                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.verbose.is_set or self.verbose.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.verbose.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination" or name == "max-ttl" or name == "min-ttl" or name == "numeric" or name == "outgoing-interface" or name == "port" or name == "priority" or name == "probe" or name == "source" or name == "timeout" or name == "verbose" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination"):
                    self.destination = value
                    self.destination.value_namespace = name_space
                    self.destination.value_namespace_prefix = name_space_prefix
                if(value_path == "max-ttl"):
                    self.max_ttl = value
                    self.max_ttl.value_namespace = name_space
                    self.max_ttl.value_namespace_prefix = name_space_prefix
                if(value_path == "min-ttl"):
                    self.min_ttl = value
                    self.min_ttl.value_namespace = name_space
                    self.min_ttl.value_namespace_prefix = name_space_prefix
                if(value_path == "numeric"):
                    self.numeric = value
                    self.numeric.value_namespace = name_space
                    self.numeric.value_namespace_prefix = name_space_prefix
                if(value_path == "outgoing-interface"):
                    self.outgoing_interface = value
                    self.outgoing_interface.value_namespace = name_space
                    self.outgoing_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "priority"):
                    self.priority = value
                    self.priority.value_namespace = name_space
                    self.priority.value_namespace_prefix = name_space_prefix
                if(value_path == "probe"):
                    self.probe = value
                    self.probe.value_namespace = name_space
                    self.probe.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "verbose"):
                    self.verbose = value
                    self.verbose.value_namespace = name_space
                    self.verbose.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix


        class Ipv4(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"

                self.destination = YLeaf(YType.str, "destination")

                self.max_ttl = YLeaf(YType.uint16, "max-ttl")

                self.min_ttl = YLeaf(YType.uint16, "min-ttl")

                self.numeric = YLeaf(YType.boolean, "numeric")

                self.port = YLeaf(YType.uint32, "port")

                self.probe = YLeaf(YType.uint16, "probe")

                self.source = YLeaf(YType.str, "source")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("destination",
                                "max_ttl",
                                "min_ttl",
                                "numeric",
                                "port",
                                "probe",
                                "source",
                                "timeout",
                                "verbose",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Traceroute.Input.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Traceroute.Input.Ipv4, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.destination.is_set or
                    self.max_ttl.is_set or
                    self.min_ttl.is_set or
                    self.numeric.is_set or
                    self.port.is_set or
                    self.probe.is_set or
                    self.source.is_set or
                    self.timeout.is_set or
                    self.verbose.is_set or
                    self.vrf_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination.yfilter != YFilter.not_set or
                    self.max_ttl.yfilter != YFilter.not_set or
                    self.min_ttl.yfilter != YFilter.not_set or
                    self.numeric.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.probe.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.verbose.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination.get_name_leafdata())
                if (self.max_ttl.is_set or self.max_ttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_ttl.get_name_leafdata())
                if (self.min_ttl.is_set or self.min_ttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.min_ttl.get_name_leafdata())
                if (self.numeric.is_set or self.numeric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.numeric.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.probe.is_set or self.probe.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.probe.get_name_leafdata())
                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.verbose.is_set or self.verbose.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.verbose.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination" or name == "max-ttl" or name == "min-ttl" or name == "numeric" or name == "port" or name == "probe" or name == "source" or name == "timeout" or name == "verbose" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination"):
                    self.destination = value
                    self.destination.value_namespace = name_space
                    self.destination.value_namespace_prefix = name_space_prefix
                if(value_path == "max-ttl"):
                    self.max_ttl = value
                    self.max_ttl.value_namespace = name_space
                    self.max_ttl.value_namespace_prefix = name_space_prefix
                if(value_path == "min-ttl"):
                    self.min_ttl = value
                    self.min_ttl.value_namespace = name_space
                    self.min_ttl.value_namespace_prefix = name_space_prefix
                if(value_path == "numeric"):
                    self.numeric = value
                    self.numeric.value_namespace = name_space
                    self.numeric.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "probe"):
                    self.probe = value
                    self.probe.value_namespace = name_space
                    self.probe.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "verbose"):
                    self.verbose = value
                    self.verbose.value_namespace = name_space
                    self.verbose.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix


        class Ipv6(Entity):
            """
            
            
            .. attribute:: destination
            
            	Destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: max_ttl
            
            	maximum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 30
            
            .. attribute:: min_ttl
            
            	minimum time to live
            	**type**\:  int
            
            	**range:** 0..255
            
            	**default value**\: 1
            
            .. attribute:: numeric
            
            	Numeric display only
            	**type**\:  bool
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of traceroute to link local address
            	**type**\:  str
            
            .. attribute:: port
            
            	Port numbe
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: priority
            
            	Priority of hte packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: probe
            
            	Probe count
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 3
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 3
            
            .. attribute:: verbose
            
            	verbose output
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"

                self.destination = YLeaf(YType.str, "destination")

                self.max_ttl = YLeaf(YType.uint16, "max-ttl")

                self.min_ttl = YLeaf(YType.uint16, "min-ttl")

                self.numeric = YLeaf(YType.boolean, "numeric")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.port = YLeaf(YType.uint32, "port")

                self.priority = YLeaf(YType.uint16, "priority")

                self.probe = YLeaf(YType.uint16, "probe")

                self.source = YLeaf(YType.str, "source")

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.verbose = YLeaf(YType.boolean, "verbose")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("destination",
                                "max_ttl",
                                "min_ttl",
                                "numeric",
                                "outgoing_interface",
                                "port",
                                "priority",
                                "probe",
                                "source",
                                "timeout",
                                "verbose",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Traceroute.Input.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Traceroute.Input.Ipv6, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.destination.is_set or
                    self.max_ttl.is_set or
                    self.min_ttl.is_set or
                    self.numeric.is_set or
                    self.outgoing_interface.is_set or
                    self.port.is_set or
                    self.priority.is_set or
                    self.probe.is_set or
                    self.source.is_set or
                    self.timeout.is_set or
                    self.verbose.is_set or
                    self.vrf_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination.yfilter != YFilter.not_set or
                    self.max_ttl.yfilter != YFilter.not_set or
                    self.min_ttl.yfilter != YFilter.not_set or
                    self.numeric.yfilter != YFilter.not_set or
                    self.outgoing_interface.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set or
                    self.priority.yfilter != YFilter.not_set or
                    self.probe.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.verbose.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination.get_name_leafdata())
                if (self.max_ttl.is_set or self.max_ttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_ttl.get_name_leafdata())
                if (self.min_ttl.is_set or self.min_ttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.min_ttl.get_name_leafdata())
                if (self.numeric.is_set or self.numeric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.numeric.get_name_leafdata())
                if (self.outgoing_interface.is_set or self.outgoing_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.outgoing_interface.get_name_leafdata())
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())
                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.priority.get_name_leafdata())
                if (self.probe.is_set or self.probe.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.probe.get_name_leafdata())
                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.verbose.is_set or self.verbose.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.verbose.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination" or name == "max-ttl" or name == "min-ttl" or name == "numeric" or name == "outgoing-interface" or name == "port" or name == "priority" or name == "probe" or name == "source" or name == "timeout" or name == "verbose" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination"):
                    self.destination = value
                    self.destination.value_namespace = name_space
                    self.destination.value_namespace_prefix = name_space_prefix
                if(value_path == "max-ttl"):
                    self.max_ttl = value
                    self.max_ttl.value_namespace = name_space
                    self.max_ttl.value_namespace_prefix = name_space_prefix
                if(value_path == "min-ttl"):
                    self.min_ttl = value
                    self.min_ttl.value_namespace = name_space
                    self.min_ttl.value_namespace_prefix = name_space_prefix
                if(value_path == "numeric"):
                    self.numeric = value
                    self.numeric.value_namespace = name_space
                    self.numeric.value_namespace_prefix = name_space_prefix
                if(value_path == "outgoing-interface"):
                    self.outgoing_interface = value
                    self.outgoing_interface.value_namespace = name_space
                    self.outgoing_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix
                if(value_path == "priority"):
                    self.priority = value
                    self.priority.value_namespace = name_space
                    self.priority.value_namespace_prefix = name_space_prefix
                if(value_path == "probe"):
                    self.probe = value
                    self.probe.value_namespace = name_space
                    self.probe.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "verbose"):
                    self.verbose = value
                    self.verbose.value_namespace = name_space
                    self.verbose.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.destination is not None and self.destination.has_data()) or
                (self.ipv4 is not None and self.ipv4.has_data()) or
                (self.ipv6 is not None and self.ipv6.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.destination is not None and self.destination.has_operation()) or
                (self.ipv4 is not None and self.ipv4.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self.get_segment_path()
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
                if (self.destination is None):
                    self.destination = Traceroute.Input.Destination()
                    self.destination.parent = self
                    self._children_name_map["destination"] = "destination"
                return self.destination

            if (child_yang_name == "ipv4"):
                if (self.ipv4 is None):
                    self.ipv4 = Traceroute.Input.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                return self.ipv4

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Traceroute.Input.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"
                return self.ipv6

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "destination" or name == "ipv4" or name == "ipv6"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Output(Entity):
        """
        
        
        .. attribute:: traceroute_response
        
        	
        	**type**\:   :py:class:`TracerouteResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse>`
        
        

        """

        _prefix = 'traceroute-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Traceroute.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "traceroute"

            self.traceroute_response = Traceroute.Output.TracerouteResponse()
            self.traceroute_response.parent = self
            self._children_name_map["traceroute_response"] = "traceroute-response"
            self._children_yang_names.add("traceroute-response")


        class TracerouteResponse(Entity):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6>`
            
            

            """

            _prefix = 'traceroute-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Traceroute.Output.TracerouteResponse, self).__init__()

                self.yang_name = "traceroute-response"
                self.yang_parent_name = "output"

                self.ipv4 = Traceroute.Output.TracerouteResponse.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.ipv6 = Traceroute.Output.TracerouteResponse.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")


            class Ipv4(Entity):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\:  str
                
                .. attribute:: hops
                
                	
                	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\:  str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Traceroute.Output.TracerouteResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "traceroute-response"

                    self.destination = YLeaf(YType.str, "destination")

                    self.verbose_output = YLeaf(YType.str, "verbose-output")

                    self.hops = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination",
                                    "verbose_output") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Traceroute.Output.TracerouteResponse.Ipv4, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Traceroute.Output.TracerouteResponse.Ipv4, self).__setattr__(name, value)


                class Hops(Entity):
                    """
                    
                    
                    .. attribute:: hop_index  <key>
                    
                    	Index of the hop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hop_address
                    
                    	Address of the hop
                    	**type**\:  str
                    
                    .. attribute:: hop_hostname
                    
                    	Hostname of the hop
                    	**type**\:  str
                    
                    .. attribute:: probes
                    
                    	
                    	**type**\: list of    :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Traceroute.Output.TracerouteResponse.Ipv4.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "ipv4"

                        self.hop_index = YLeaf(YType.uint32, "hop-index")

                        self.hop_address = YLeaf(YType.str, "hop-address")

                        self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                        self.probes = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("hop_index",
                                        "hop_address",
                                        "hop_hostname") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Traceroute.Output.TracerouteResponse.Ipv4.Hops, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Traceroute.Output.TracerouteResponse.Ipv4.Hops, self).__setattr__(name, value)


                    class Probes(Entity):
                        """
                        
                        
                        .. attribute:: probe_index  <key>
                        
                        	Index of the probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delta_time
                        
                        	Delta time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\:  str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\:  str
                        
                        .. attribute:: result
                        
                        	Response for each probe
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes, self).__init__()

                            self.yang_name = "probes"
                            self.yang_parent_name = "hops"

                            self.probe_index = YLeaf(YType.uint32, "probe-index")

                            self.delta_time = YLeaf(YType.uint32, "delta-time")

                            self.hop_address = YLeaf(YType.str, "hop-address")

                            self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                            self.result = YLeaf(YType.str, "result")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("probe_index",
                                            "delta_time",
                                            "hop_address",
                                            "hop_hostname",
                                            "result") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.probe_index.is_set or
                                self.delta_time.is_set or
                                self.hop_address.is_set or
                                self.hop_hostname.is_set or
                                self.result.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.probe_index.yfilter != YFilter.not_set or
                                self.delta_time.yfilter != YFilter.not_set or
                                self.hop_address.yfilter != YFilter.not_set or
                                self.hop_hostname.yfilter != YFilter.not_set or
                                self.result.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "probes" + "[probe-index='" + self.probe_index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.probe_index.is_set or self.probe_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_index.get_name_leafdata())
                            if (self.delta_time.is_set or self.delta_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delta_time.get_name_leafdata())
                            if (self.hop_address.is_set or self.hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_address.get_name_leafdata())
                            if (self.hop_hostname.is_set or self.hop_hostname.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_hostname.get_name_leafdata())
                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.result.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "probe-index" or name == "delta-time" or name == "hop-address" or name == "hop-hostname" or name == "result"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "probe-index"):
                                self.probe_index = value
                                self.probe_index.value_namespace = name_space
                                self.probe_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "delta-time"):
                                self.delta_time = value
                                self.delta_time.value_namespace = name_space
                                self.delta_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-address"):
                                self.hop_address = value
                                self.hop_address.value_namespace = name_space
                                self.hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-hostname"):
                                self.hop_hostname = value
                                self.hop_hostname.value_namespace = name_space
                                self.hop_hostname.value_namespace_prefix = name_space_prefix
                            if(value_path == "result"):
                                self.result = value
                                self.result.value_namespace = name_space
                                self.result.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.probes:
                            if (c.has_data()):
                                return True
                        return (
                            self.hop_index.is_set or
                            self.hop_address.is_set or
                            self.hop_hostname.is_set)

                    def has_operation(self):
                        for c in self.probes:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.hop_index.yfilter != YFilter.not_set or
                            self.hop_address.yfilter != YFilter.not_set or
                            self.hop_hostname.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hops" + "[hop-index='" + self.hop_index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv4/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.hop_index.is_set or self.hop_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_index.get_name_leafdata())
                        if (self.hop_address.is_set or self.hop_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_address.get_name_leafdata())
                        if (self.hop_hostname.is_set or self.hop_hostname.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_hostname.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "probes"):
                            for c in self.probes:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Traceroute.Output.TracerouteResponse.Ipv4.Hops.Probes()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.probes.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "probes" or name == "hop-index" or name == "hop-address" or name == "hop-hostname"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "hop-index"):
                            self.hop_index = value
                            self.hop_index.value_namespace = name_space
                            self.hop_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "hop-address"):
                            self.hop_address = value
                            self.hop_address.value_namespace = name_space
                            self.hop_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "hop-hostname"):
                            self.hop_hostname = value
                            self.hop_hostname.value_namespace = name_space
                            self.hop_hostname.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.hops:
                        if (c.has_data()):
                            return True
                    return (
                        self.destination.is_set or
                        self.verbose_output.is_set)

                def has_operation(self):
                    for c in self.hops:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination.yfilter != YFilter.not_set or
                        self.verbose_output.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination.get_name_leafdata())
                    if (self.verbose_output.is_set or self.verbose_output.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.verbose_output.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "hops"):
                        for c in self.hops:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Traceroute.Output.TracerouteResponse.Ipv4.Hops()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.hops.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hops" or name == "destination" or name == "verbose-output"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination"):
                        self.destination = value
                        self.destination.value_namespace = name_space
                        self.destination.value_namespace_prefix = name_space_prefix
                    if(value_path == "verbose-output"):
                        self.verbose_output = value
                        self.verbose_output.value_namespace = name_space
                        self.verbose_output.value_namespace_prefix = name_space_prefix


            class Ipv6(Entity):
                """
                
                
                .. attribute:: destination
                
                	Destination address or hostname
                	**type**\:  str
                
                .. attribute:: hops
                
                	
                	**type**\: list of    :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops>`
                
                .. attribute:: verbose_output
                
                	Verbose output
                	**type**\:  str
                
                

                """

                _prefix = 'traceroute-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Traceroute.Output.TracerouteResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "traceroute-response"

                    self.destination = YLeaf(YType.str, "destination")

                    self.verbose_output = YLeaf(YType.str, "verbose-output")

                    self.hops = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("destination",
                                    "verbose_output") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Traceroute.Output.TracerouteResponse.Ipv6, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Traceroute.Output.TracerouteResponse.Ipv6, self).__setattr__(name, value)


                class Hops(Entity):
                    """
                    
                    
                    .. attribute:: hop_index  <key>
                    
                    	Index of the hop
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hop_address
                    
                    	Address of the hop
                    	**type**\:  str
                    
                    .. attribute:: hop_hostname
                    
                    	Hostname of the hop
                    	**type**\:  str
                    
                    .. attribute:: probes
                    
                    	
                    	**type**\: list of    :py:class:`Probes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traceroute_act.Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes>`
                    
                    

                    """

                    _prefix = 'traceroute-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Traceroute.Output.TracerouteResponse.Ipv6.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "ipv6"

                        self.hop_index = YLeaf(YType.uint32, "hop-index")

                        self.hop_address = YLeaf(YType.str, "hop-address")

                        self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                        self.probes = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("hop_index",
                                        "hop_address",
                                        "hop_hostname") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Traceroute.Output.TracerouteResponse.Ipv6.Hops, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Traceroute.Output.TracerouteResponse.Ipv6.Hops, self).__setattr__(name, value)


                    class Probes(Entity):
                        """
                        
                        
                        .. attribute:: probe_index  <key>
                        
                        	Index of the probe
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delta_time
                        
                        	Delta time in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: hop_address
                        
                        	Address of the hop
                        	**type**\:  str
                        
                        .. attribute:: hop_hostname
                        
                        	Hostname of the hop
                        	**type**\:  str
                        
                        .. attribute:: result
                        
                        	Response for each probe
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'traceroute-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes, self).__init__()

                            self.yang_name = "probes"
                            self.yang_parent_name = "hops"

                            self.probe_index = YLeaf(YType.uint32, "probe-index")

                            self.delta_time = YLeaf(YType.uint32, "delta-time")

                            self.hop_address = YLeaf(YType.str, "hop-address")

                            self.hop_hostname = YLeaf(YType.str, "hop-hostname")

                            self.result = YLeaf(YType.str, "result")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("probe_index",
                                            "delta_time",
                                            "hop_address",
                                            "hop_hostname",
                                            "result") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.probe_index.is_set or
                                self.delta_time.is_set or
                                self.hop_address.is_set or
                                self.hop_hostname.is_set or
                                self.result.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.probe_index.yfilter != YFilter.not_set or
                                self.delta_time.yfilter != YFilter.not_set or
                                self.hop_address.yfilter != YFilter.not_set or
                                self.hop_hostname.yfilter != YFilter.not_set or
                                self.result.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "probes" + "[probe-index='" + self.probe_index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.probe_index.is_set or self.probe_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.probe_index.get_name_leafdata())
                            if (self.delta_time.is_set or self.delta_time.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.delta_time.get_name_leafdata())
                            if (self.hop_address.is_set or self.hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_address.get_name_leafdata())
                            if (self.hop_hostname.is_set or self.hop_hostname.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_hostname.get_name_leafdata())
                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.result.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "probe-index" or name == "delta-time" or name == "hop-address" or name == "hop-hostname" or name == "result"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "probe-index"):
                                self.probe_index = value
                                self.probe_index.value_namespace = name_space
                                self.probe_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "delta-time"):
                                self.delta_time = value
                                self.delta_time.value_namespace = name_space
                                self.delta_time.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-address"):
                                self.hop_address = value
                                self.hop_address.value_namespace = name_space
                                self.hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-hostname"):
                                self.hop_hostname = value
                                self.hop_hostname.value_namespace = name_space
                                self.hop_hostname.value_namespace_prefix = name_space_prefix
                            if(value_path == "result"):
                                self.result = value
                                self.result.value_namespace = name_space
                                self.result.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.probes:
                            if (c.has_data()):
                                return True
                        return (
                            self.hop_index.is_set or
                            self.hop_address.is_set or
                            self.hop_hostname.is_set)

                    def has_operation(self):
                        for c in self.probes:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.hop_index.yfilter != YFilter.not_set or
                            self.hop_address.yfilter != YFilter.not_set or
                            self.hop_hostname.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hops" + "[hop-index='" + self.hop_index.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/ipv6/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.hop_index.is_set or self.hop_index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_index.get_name_leafdata())
                        if (self.hop_address.is_set or self.hop_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_address.get_name_leafdata())
                        if (self.hop_hostname.is_set or self.hop_hostname.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.hop_hostname.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "probes"):
                            for c in self.probes:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Traceroute.Output.TracerouteResponse.Ipv6.Hops.Probes()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.probes.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "probes" or name == "hop-index" or name == "hop-address" or name == "hop-hostname"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "hop-index"):
                            self.hop_index = value
                            self.hop_index.value_namespace = name_space
                            self.hop_index.value_namespace_prefix = name_space_prefix
                        if(value_path == "hop-address"):
                            self.hop_address = value
                            self.hop_address.value_namespace = name_space
                            self.hop_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "hop-hostname"):
                            self.hop_hostname = value
                            self.hop_hostname.value_namespace = name_space
                            self.hop_hostname.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.hops:
                        if (c.has_data()):
                            return True
                    return (
                        self.destination.is_set or
                        self.verbose_output.is_set)

                def has_operation(self):
                    for c in self.hops:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination.yfilter != YFilter.not_set or
                        self.verbose_output.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/output/traceroute-response/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination.get_name_leafdata())
                    if (self.verbose_output.is_set or self.verbose_output.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.verbose_output.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "hops"):
                        for c in self.hops:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Traceroute.Output.TracerouteResponse.Ipv6.Hops()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.hops.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hops" or name == "destination" or name == "verbose-output"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination"):
                        self.destination = value
                        self.destination.value_namespace = name_space
                        self.destination.value_namespace_prefix = name_space_prefix
                    if(value_path == "verbose-output"):
                        self.verbose_output = value
                        self.verbose_output.value_namespace = name_space
                        self.verbose_output.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.ipv6 is not None and self.ipv6.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.ipv6 is not None and self.ipv6.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "traceroute-response" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/output/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = Traceroute.Output.TracerouteResponse.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Traceroute.Output.TracerouteResponse.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                    return self.ipv6

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4" or name == "ipv6"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.traceroute_response is not None and self.traceroute_response.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.traceroute_response is not None and self.traceroute_response.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "traceroute-response"):
                if (self.traceroute_response is None):
                    self.traceroute_response = Traceroute.Output.TracerouteResponse()
                    self.traceroute_response.parent = self
                    self._children_name_map["traceroute_response"] = "traceroute-response"
                return self.traceroute_response

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "traceroute-response"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-traceroute-act:traceroute" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = Traceroute.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Traceroute.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Traceroute()
        return self._top_entity

