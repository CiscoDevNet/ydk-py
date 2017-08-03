""" Cisco_IOS_XR_ping_act 

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



class Ping(Entity):
    """
    Send echo messages
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output>`
    
    

    """

    _prefix = 'ping-act'
    _revision = '2016-09-28'

    def __init__(self):
        super(Ping, self).__init__()
        self._top_entity = None

        self.yang_name = "ping"
        self.yang_parent_name = "Cisco-IOS-XR-ping-act"

        self.input = Ping.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Ping.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: destination
        
        	
        	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Destination>`
        
        .. attribute:: ipv4
        
        	
        	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Ipv4>`
        
        .. attribute:: ipv6
        
        	
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Input.Ipv6>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Ping.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "ping"

            self.destination = Ping.Input.Destination()
            self.destination.parent = self
            self._children_name_map["destination"] = "destination"
            self._children_yang_names.add("destination")

            self.ipv6 = Ping.Input.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"
            self._children_yang_names.add("ipv6")

            self.ipv4 = YList(self)

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
                        super(Ping.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ping.Input, self).__setattr__(name, value)


        class Destination(Entity):
            """
            
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\:  int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: destination
            
            	Ping destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: do_not_frag
            
            	Do Not Fragment
            	**type**\:  bool
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of ping to link local address
            	**type**\:  str
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: priority
            
            	Priority of the packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\:  bool
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: type_of_service
            
            	Type of Service
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: validate
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Ping.Input.Destination, self).__init__()

                self.yang_name = "destination"
                self.yang_parent_name = "input"

                self.data_size = YLeaf(YType.uint64, "data-size")

                self.destination = YLeaf(YType.str, "destination")

                self.do_not_frag = YLeaf(YType.boolean, "do-not-frag")

                self.interval = YLeaf(YType.uint32, "interval")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.pattern = YLeaf(YType.str, "pattern")

                self.priority = YLeaf(YType.uint8, "priority")

                self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                self.source = YLeaf(YType.str, "source")

                self.sweep = YLeaf(YType.boolean, "sweep")

                self.timeout = YLeaf(YType.uint64, "timeout")

                self.type_of_service = YLeaf(YType.uint8, "type-of-service")

                self.validate = YLeaf(YType.boolean, "validate")

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
                    if name in ("data_size",
                                "destination",
                                "do_not_frag",
                                "interval",
                                "outgoing_interface",
                                "pattern",
                                "priority",
                                "repeat_count",
                                "source",
                                "sweep",
                                "timeout",
                                "type_of_service",
                                "validate",
                                "verbose",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ping.Input.Destination, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ping.Input.Destination, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.data_size.is_set or
                    self.destination.is_set or
                    self.do_not_frag.is_set or
                    self.interval.is_set or
                    self.outgoing_interface.is_set or
                    self.pattern.is_set or
                    self.priority.is_set or
                    self.repeat_count.is_set or
                    self.source.is_set or
                    self.sweep.is_set or
                    self.timeout.is_set or
                    self.type_of_service.is_set or
                    self.validate.is_set or
                    self.verbose.is_set or
                    self.vrf_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.data_size.yfilter != YFilter.not_set or
                    self.destination.yfilter != YFilter.not_set or
                    self.do_not_frag.yfilter != YFilter.not_set or
                    self.interval.yfilter != YFilter.not_set or
                    self.outgoing_interface.yfilter != YFilter.not_set or
                    self.pattern.yfilter != YFilter.not_set or
                    self.priority.yfilter != YFilter.not_set or
                    self.repeat_count.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set or
                    self.sweep.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.type_of_service.yfilter != YFilter.not_set or
                    self.validate.yfilter != YFilter.not_set or
                    self.verbose.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "destination" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ping-act:ping/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.data_size.is_set or self.data_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.data_size.get_name_leafdata())
                if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination.get_name_leafdata())
                if (self.do_not_frag.is_set or self.do_not_frag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.do_not_frag.get_name_leafdata())
                if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interval.get_name_leafdata())
                if (self.outgoing_interface.is_set or self.outgoing_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.outgoing_interface.get_name_leafdata())
                if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pattern.get_name_leafdata())
                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.priority.get_name_leafdata())
                if (self.repeat_count.is_set or self.repeat_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.repeat_count.get_name_leafdata())
                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source.get_name_leafdata())
                if (self.sweep.is_set or self.sweep.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sweep.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.type_of_service.is_set or self.type_of_service.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type_of_service.get_name_leafdata())
                if (self.validate.is_set or self.validate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.validate.get_name_leafdata())
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
                if(name == "data-size" or name == "destination" or name == "do-not-frag" or name == "interval" or name == "outgoing-interface" or name == "pattern" or name == "priority" or name == "repeat-count" or name == "source" or name == "sweep" or name == "timeout" or name == "type-of-service" or name == "validate" or name == "verbose" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "data-size"):
                    self.data_size = value
                    self.data_size.value_namespace = name_space
                    self.data_size.value_namespace_prefix = name_space_prefix
                if(value_path == "destination"):
                    self.destination = value
                    self.destination.value_namespace = name_space
                    self.destination.value_namespace_prefix = name_space_prefix
                if(value_path == "do-not-frag"):
                    self.do_not_frag = value
                    self.do_not_frag.value_namespace = name_space
                    self.do_not_frag.value_namespace_prefix = name_space_prefix
                if(value_path == "interval"):
                    self.interval = value
                    self.interval.value_namespace = name_space
                    self.interval.value_namespace_prefix = name_space_prefix
                if(value_path == "outgoing-interface"):
                    self.outgoing_interface = value
                    self.outgoing_interface.value_namespace = name_space
                    self.outgoing_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "pattern"):
                    self.pattern = value
                    self.pattern.value_namespace = name_space
                    self.pattern.value_namespace_prefix = name_space_prefix
                if(value_path == "priority"):
                    self.priority = value
                    self.priority.value_namespace = name_space
                    self.priority.value_namespace_prefix = name_space_prefix
                if(value_path == "repeat-count"):
                    self.repeat_count = value
                    self.repeat_count.value_namespace = name_space
                    self.repeat_count.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix
                if(value_path == "sweep"):
                    self.sweep = value
                    self.sweep.value_namespace = name_space
                    self.sweep.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "type-of-service"):
                    self.type_of_service = value
                    self.type_of_service.value_namespace = name_space
                    self.type_of_service.value_namespace_prefix = name_space_prefix
                if(value_path == "validate"):
                    self.validate = value
                    self.validate.value_namespace = name_space
                    self.validate.value_namespace_prefix = name_space_prefix
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
            
            
            .. attribute:: destination  <key>
            
            	Ping destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\:  int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: do_not_frag
            
            	Do Not Fragment
            	**type**\:  bool
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\:  bool
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: type_of_service
            
            	Type of Service
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: validate
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Ping.Input.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "input"

                self.destination = YLeaf(YType.str, "destination")

                self.data_size = YLeaf(YType.uint64, "data-size")

                self.do_not_frag = YLeaf(YType.boolean, "do-not-frag")

                self.interval = YLeaf(YType.uint32, "interval")

                self.pattern = YLeaf(YType.str, "pattern")

                self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                self.source = YLeaf(YType.str, "source")

                self.sweep = YLeaf(YType.boolean, "sweep")

                self.timeout = YLeaf(YType.uint64, "timeout")

                self.type_of_service = YLeaf(YType.uint8, "type-of-service")

                self.validate = YLeaf(YType.boolean, "validate")

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
                                "data_size",
                                "do_not_frag",
                                "interval",
                                "pattern",
                                "repeat_count",
                                "source",
                                "sweep",
                                "timeout",
                                "type_of_service",
                                "validate",
                                "verbose",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ping.Input.Ipv4, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ping.Input.Ipv4, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.destination.is_set or
                    self.data_size.is_set or
                    self.do_not_frag.is_set or
                    self.interval.is_set or
                    self.pattern.is_set or
                    self.repeat_count.is_set or
                    self.source.is_set or
                    self.sweep.is_set or
                    self.timeout.is_set or
                    self.type_of_service.is_set or
                    self.validate.is_set or
                    self.verbose.is_set or
                    self.vrf_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination.yfilter != YFilter.not_set or
                    self.data_size.yfilter != YFilter.not_set or
                    self.do_not_frag.yfilter != YFilter.not_set or
                    self.interval.yfilter != YFilter.not_set or
                    self.pattern.yfilter != YFilter.not_set or
                    self.repeat_count.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set or
                    self.sweep.yfilter != YFilter.not_set or
                    self.timeout.yfilter != YFilter.not_set or
                    self.type_of_service.yfilter != YFilter.not_set or
                    self.validate.yfilter != YFilter.not_set or
                    self.verbose.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4" + "[destination='" + self.destination.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ping-act:ping/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination.get_name_leafdata())
                if (self.data_size.is_set or self.data_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.data_size.get_name_leafdata())
                if (self.do_not_frag.is_set or self.do_not_frag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.do_not_frag.get_name_leafdata())
                if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interval.get_name_leafdata())
                if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pattern.get_name_leafdata())
                if (self.repeat_count.is_set or self.repeat_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.repeat_count.get_name_leafdata())
                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source.get_name_leafdata())
                if (self.sweep.is_set or self.sweep.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sweep.get_name_leafdata())
                if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeout.get_name_leafdata())
                if (self.type_of_service.is_set or self.type_of_service.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type_of_service.get_name_leafdata())
                if (self.validate.is_set or self.validate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.validate.get_name_leafdata())
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
                if(name == "destination" or name == "data-size" or name == "do-not-frag" or name == "interval" or name == "pattern" or name == "repeat-count" or name == "source" or name == "sweep" or name == "timeout" or name == "type-of-service" or name == "validate" or name == "verbose" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination"):
                    self.destination = value
                    self.destination.value_namespace = name_space
                    self.destination.value_namespace_prefix = name_space_prefix
                if(value_path == "data-size"):
                    self.data_size = value
                    self.data_size.value_namespace = name_space
                    self.data_size.value_namespace_prefix = name_space_prefix
                if(value_path == "do-not-frag"):
                    self.do_not_frag = value
                    self.do_not_frag.value_namespace = name_space
                    self.do_not_frag.value_namespace_prefix = name_space_prefix
                if(value_path == "interval"):
                    self.interval = value
                    self.interval.value_namespace = name_space
                    self.interval.value_namespace_prefix = name_space_prefix
                if(value_path == "pattern"):
                    self.pattern = value
                    self.pattern.value_namespace = name_space
                    self.pattern.value_namespace_prefix = name_space_prefix
                if(value_path == "repeat-count"):
                    self.repeat_count = value
                    self.repeat_count.value_namespace = name_space
                    self.repeat_count.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix
                if(value_path == "sweep"):
                    self.sweep = value
                    self.sweep.value_namespace = name_space
                    self.sweep.value_namespace_prefix = name_space_prefix
                if(value_path == "timeout"):
                    self.timeout = value
                    self.timeout.value_namespace = name_space
                    self.timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "type-of-service"):
                    self.type_of_service = value
                    self.type_of_service.value_namespace = name_space
                    self.type_of_service.value_namespace_prefix = name_space_prefix
                if(value_path == "validate"):
                    self.validate = value
                    self.validate.value_namespace = name_space
                    self.validate.value_namespace_prefix = name_space_prefix
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
            
            
            .. attribute:: data_size
            
            	Size of ping packet
            	**type**\:  int
            
            	**range:** 36..18024
            
            	**default value**\: 100
            
            .. attribute:: destination
            
            	Ping destination address or hostname
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: interval
            
            	Ping interval in milli seconds
            	**type**\:  int
            
            	**range:** 0..3600
            
            	**default value**\: 10
            
            .. attribute:: outgoing_interface
            
            	Outgoing interface, needed in case of ping to link local address
            	**type**\:  str
            
            .. attribute:: pattern
            
            	Pattern of payload data
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: priority
            
            	Priority of the packet
            	**type**\:  int
            
            	**range:** 0..15
            
            .. attribute:: repeat_count
            
            	Number of ping packets to be sent out
            	**type**\:  int
            
            	**range:** 1..64
            
            	**default value**\: 5
            
            .. attribute:: source
            
            	Source address or interface
            	**type**\:  str
            
            .. attribute:: sweep
            
            	Sweep is enabled
            	**type**\:  bool
            
            .. attribute:: timeout
            
            	Timeout in seconds
            	**type**\:  int
            
            	**range:** 0..36
            
            	**default value**\: 2
            
            .. attribute:: verbose
            
            	Validate return packet
            	**type**\:  bool
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Ping.Input.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "input"

                self.data_size = YLeaf(YType.uint64, "data-size")

                self.destination = YLeaf(YType.str, "destination")

                self.interval = YLeaf(YType.uint32, "interval")

                self.outgoing_interface = YLeaf(YType.str, "outgoing-interface")

                self.pattern = YLeaf(YType.str, "pattern")

                self.priority = YLeaf(YType.uint8, "priority")

                self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                self.source = YLeaf(YType.str, "source")

                self.sweep = YLeaf(YType.boolean, "sweep")

                self.timeout = YLeaf(YType.uint64, "timeout")

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
                    if name in ("data_size",
                                "destination",
                                "interval",
                                "outgoing_interface",
                                "pattern",
                                "priority",
                                "repeat_count",
                                "source",
                                "sweep",
                                "timeout",
                                "verbose",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ping.Input.Ipv6, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ping.Input.Ipv6, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.data_size.is_set or
                    self.destination.is_set or
                    self.interval.is_set or
                    self.outgoing_interface.is_set or
                    self.pattern.is_set or
                    self.priority.is_set or
                    self.repeat_count.is_set or
                    self.source.is_set or
                    self.sweep.is_set or
                    self.timeout.is_set or
                    self.verbose.is_set or
                    self.vrf_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.data_size.yfilter != YFilter.not_set or
                    self.destination.yfilter != YFilter.not_set or
                    self.interval.yfilter != YFilter.not_set or
                    self.outgoing_interface.yfilter != YFilter.not_set or
                    self.pattern.yfilter != YFilter.not_set or
                    self.priority.yfilter != YFilter.not_set or
                    self.repeat_count.yfilter != YFilter.not_set or
                    self.source.yfilter != YFilter.not_set or
                    self.sweep.yfilter != YFilter.not_set or
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
                    path_buffer = "Cisco-IOS-XR-ping-act:ping/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.data_size.is_set or self.data_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.data_size.get_name_leafdata())
                if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination.get_name_leafdata())
                if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interval.get_name_leafdata())
                if (self.outgoing_interface.is_set or self.outgoing_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.outgoing_interface.get_name_leafdata())
                if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pattern.get_name_leafdata())
                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.priority.get_name_leafdata())
                if (self.repeat_count.is_set or self.repeat_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.repeat_count.get_name_leafdata())
                if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source.get_name_leafdata())
                if (self.sweep.is_set or self.sweep.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sweep.get_name_leafdata())
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
                if(name == "data-size" or name == "destination" or name == "interval" or name == "outgoing-interface" or name == "pattern" or name == "priority" or name == "repeat-count" or name == "source" or name == "sweep" or name == "timeout" or name == "verbose" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "data-size"):
                    self.data_size = value
                    self.data_size.value_namespace = name_space
                    self.data_size.value_namespace_prefix = name_space_prefix
                if(value_path == "destination"):
                    self.destination = value
                    self.destination.value_namespace = name_space
                    self.destination.value_namespace_prefix = name_space_prefix
                if(value_path == "interval"):
                    self.interval = value
                    self.interval.value_namespace = name_space
                    self.interval.value_namespace_prefix = name_space_prefix
                if(value_path == "outgoing-interface"):
                    self.outgoing_interface = value
                    self.outgoing_interface.value_namespace = name_space
                    self.outgoing_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "pattern"):
                    self.pattern = value
                    self.pattern.value_namespace = name_space
                    self.pattern.value_namespace_prefix = name_space_prefix
                if(value_path == "priority"):
                    self.priority = value
                    self.priority.value_namespace = name_space
                    self.priority.value_namespace_prefix = name_space_prefix
                if(value_path == "repeat-count"):
                    self.repeat_count = value
                    self.repeat_count.value_namespace = name_space
                    self.repeat_count.value_namespace_prefix = name_space_prefix
                if(value_path == "source"):
                    self.source = value
                    self.source.value_namespace = name_space
                    self.source.value_namespace_prefix = name_space_prefix
                if(value_path == "sweep"):
                    self.sweep = value
                    self.sweep.value_namespace = name_space
                    self.sweep.value_namespace_prefix = name_space_prefix
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
            for c in self.ipv4:
                if (c.has_data()):
                    return True
            return (
                (self.destination is not None and self.destination.has_data()) or
                (self.ipv6 is not None and self.ipv6.has_data()))

        def has_operation(self):
            for c in self.ipv4:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                (self.destination is not None and self.destination.has_operation()) or
                (self.ipv6 is not None and self.ipv6.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ping-act:ping/%s" % self.get_segment_path()
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
                    self.destination = Ping.Input.Destination()
                    self.destination.parent = self
                    self._children_name_map["destination"] = "destination"
                return self.destination

            if (child_yang_name == "ipv4"):
                for c in self.ipv4:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ping.Input.Ipv4()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipv4.append(c)
                return c

            if (child_yang_name == "ipv6"):
                if (self.ipv6 is None):
                    self.ipv6 = Ping.Input.Ipv6()
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
        
        
        .. attribute:: ping_response
        
        	
        	**type**\:   :py:class:`PingResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse>`
        
        

        """

        _prefix = 'ping-act'
        _revision = '2016-09-28'

        def __init__(self):
            super(Ping.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "ping"

            self.ping_response = Ping.Output.PingResponse()
            self.ping_response.parent = self
            self._children_name_map["ping_response"] = "ping-response"
            self._children_yang_names.add("ping-response")


        class PingResponse(Entity):
            """
            
            
            .. attribute:: ipv4
            
            	
            	**type**\: list of    :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4>`
            
            .. attribute:: ipv6
            
            	
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6>`
            
            

            """

            _prefix = 'ping-act'
            _revision = '2016-09-28'

            def __init__(self):
                super(Ping.Output.PingResponse, self).__init__()

                self.yang_name = "ping-response"
                self.yang_parent_name = "output"

                self.ipv6 = Ping.Output.PingResponse.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._children_yang_names.add("ipv6")

                self.ipv4 = YList(self)

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
                            super(Ping.Output.PingResponse, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ping.Output.PingResponse, self).__setattr__(name, value)


            class Ipv4(Entity):
                """
                
                
                .. attribute:: destination  <key>
                
                	Ping destination address or hostname
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: data_size
                
                	Size of ping packet
                	**type**\:  int
                
                	**range:** 36..18024
                
                	**default value**\: 100
                
                .. attribute:: hits
                
                	Number of packets reach to destination and get reply back
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: interval
                
                	Ping interval in milli seconds
                	**type**\:  int
                
                	**range:** 0..3600
                
                	**default value**\: 10
                
                .. attribute:: pattern
                
                	Pattern of payload data
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: ping_error_response
                
                	Error response for each ping, in case of bulk ping
                	**type**\:  str
                
                .. attribute:: repeat_count
                
                	Number of ping packets to be sent out
                	**type**\:  int
                
                	**range:** 1..64
                
                	**default value**\: 5
                
                .. attribute:: replies
                
                	
                	**type**\:   :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies>`
                
                .. attribute:: rotate_pattern
                
                	Rotate Pattern is enabled
                	**type**\:  bool
                
                .. attribute:: rtt_avg
                
                	Average value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_max
                
                	Maximum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_min
                
                	Minimum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: success_rate
                
                	Successful rate of ping
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep
                
                	Sweep is enabled
                	**type**\:  bool
                
                .. attribute:: sweep_max
                
                	Maximum value of sweep size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep_min
                
                	Minimum value of sweep size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout
                
                	Timeout in seconds
                	**type**\:  int
                
                	**range:** 0..36
                
                	**default value**\: 2
                
                .. attribute:: total
                
                	Total number of packets sent out
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ping-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Ping.Output.PingResponse.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "ping-response"

                    self.destination = YLeaf(YType.str, "destination")

                    self.data_size = YLeaf(YType.uint64, "data-size")

                    self.hits = YLeaf(YType.uint64, "hits")

                    self.interval = YLeaf(YType.uint32, "interval")

                    self.pattern = YLeaf(YType.str, "pattern")

                    self.ping_error_response = YLeaf(YType.str, "ping-error-response")

                    self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                    self.rotate_pattern = YLeaf(YType.boolean, "rotate-pattern")

                    self.rtt_avg = YLeaf(YType.uint64, "rtt-avg")

                    self.rtt_max = YLeaf(YType.uint64, "rtt-max")

                    self.rtt_min = YLeaf(YType.uint64, "rtt-min")

                    self.success_rate = YLeaf(YType.uint64, "success-rate")

                    self.sweep = YLeaf(YType.boolean, "sweep")

                    self.sweep_max = YLeaf(YType.uint64, "sweep-max")

                    self.sweep_min = YLeaf(YType.uint32, "sweep-min")

                    self.timeout = YLeaf(YType.uint64, "timeout")

                    self.total = YLeaf(YType.uint64, "total")

                    self.replies = Ping.Output.PingResponse.Ipv4.Replies()
                    self.replies.parent = self
                    self._children_name_map["replies"] = "replies"
                    self._children_yang_names.add("replies")

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
                                    "data_size",
                                    "hits",
                                    "interval",
                                    "pattern",
                                    "ping_error_response",
                                    "repeat_count",
                                    "rotate_pattern",
                                    "rtt_avg",
                                    "rtt_max",
                                    "rtt_min",
                                    "success_rate",
                                    "sweep",
                                    "sweep_max",
                                    "sweep_min",
                                    "timeout",
                                    "total") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ping.Output.PingResponse.Ipv4, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ping.Output.PingResponse.Ipv4, self).__setattr__(name, value)


                class Replies(Entity):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of    :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Ping.Output.PingResponse.Ipv4.Replies, self).__init__()

                        self.yang_name = "replies"
                        self.yang_parent_name = "ipv4"

                        self.reply = YList(self)

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
                                    super(Ping.Output.PingResponse.Ipv4.Replies, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ping.Output.PingResponse.Ipv4.Replies, self).__setattr__(name, value)


                    class Reply(Entity):
                        """
                        
                        
                        .. attribute:: reply_index  <key>
                        
                        	Index of the reply list
                        	**type**\:  int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: broadcast_reply_addresses
                        
                        	
                        	**type**\:   :py:class:`BroadcastReplyAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses>`
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Ping.Output.PingResponse.Ipv4.Replies.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "replies"

                            self.reply_index = YLeaf(YType.uint64, "reply-index")

                            self.result = YLeaf(YType.str, "result")

                            self.broadcast_reply_addresses = Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses()
                            self.broadcast_reply_addresses.parent = self
                            self._children_name_map["broadcast_reply_addresses"] = "broadcast-reply-addresses"
                            self._children_yang_names.add("broadcast-reply-addresses")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("reply_index",
                                            "result") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ping.Output.PingResponse.Ipv4.Replies.Reply, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ping.Output.PingResponse.Ipv4.Replies.Reply, self).__setattr__(name, value)


                        class BroadcastReplyAddresses(Entity):
                            """
                            
                            
                            .. attribute:: broadcast_reply_address
                            
                            	
                            	**type**\: list of    :py:class:`BroadcastReplyAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress>`
                            
                            

                            """

                            _prefix = 'ping-act'
                            _revision = '2016-09-28'

                            def __init__(self):
                                super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, self).__init__()

                                self.yang_name = "broadcast-reply-addresses"
                                self.yang_parent_name = "reply"

                                self.broadcast_reply_address = YList(self)

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
                                            super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses, self).__setattr__(name, value)


                            class BroadcastReplyAddress(Entity):
                                """
                                
                                
                                .. attribute:: reply_address  <key>
                                
                                	Broadcast reply address
                                	**type**\:  str
                                
                                .. attribute:: result
                                
                                	Sign for each reply packet
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ping-act'
                                _revision = '2016-09-28'

                                def __init__(self):
                                    super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, self).__init__()

                                    self.yang_name = "broadcast-reply-address"
                                    self.yang_parent_name = "broadcast-reply-addresses"

                                    self.reply_address = YLeaf(YType.str, "reply-address")

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
                                        if name in ("reply_address",
                                                    "result") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.reply_address.is_set or
                                        self.result.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.reply_address.yfilter != YFilter.not_set or
                                        self.result.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "broadcast-reply-address" + "[reply-address='" + self.reply_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.reply_address.is_set or self.reply_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.reply_address.get_name_leafdata())
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
                                    if(name == "reply-address" or name == "result"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "reply-address"):
                                        self.reply_address = value
                                        self.reply_address.value_namespace = name_space
                                        self.reply_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "result"):
                                        self.result = value
                                        self.result.value_namespace = name_space
                                        self.result.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.broadcast_reply_address:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.broadcast_reply_address:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "broadcast-reply-addresses" + path_buffer

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

                                if (child_yang_name == "broadcast-reply-address"):
                                    for c in self.broadcast_reply_address:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses.BroadcastReplyAddress()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.broadcast_reply_address.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "broadcast-reply-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.reply_index.is_set or
                                self.result.is_set or
                                (self.broadcast_reply_addresses is not None and self.broadcast_reply_addresses.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.reply_index.yfilter != YFilter.not_set or
                                self.result.yfilter != YFilter.not_set or
                                (self.broadcast_reply_addresses is not None and self.broadcast_reply_addresses.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "reply" + "[reply-index='" + self.reply_index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.reply_index.is_set or self.reply_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reply_index.get_name_leafdata())
                            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.result.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "broadcast-reply-addresses"):
                                if (self.broadcast_reply_addresses is None):
                                    self.broadcast_reply_addresses = Ping.Output.PingResponse.Ipv4.Replies.Reply.BroadcastReplyAddresses()
                                    self.broadcast_reply_addresses.parent = self
                                    self._children_name_map["broadcast_reply_addresses"] = "broadcast-reply-addresses"
                                return self.broadcast_reply_addresses

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "broadcast-reply-addresses" or name == "reply-index" or name == "result"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "reply-index"):
                                self.reply_index = value
                                self.reply_index.value_namespace = name_space
                                self.reply_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "result"):
                                self.result = value
                                self.result.value_namespace = name_space
                                self.result.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.reply:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.reply:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "replies" + path_buffer

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

                        if (child_yang_name == "reply"):
                            for c in self.reply:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ping.Output.PingResponse.Ipv4.Replies.Reply()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.reply.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "reply"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.destination.is_set or
                        self.data_size.is_set or
                        self.hits.is_set or
                        self.interval.is_set or
                        self.pattern.is_set or
                        self.ping_error_response.is_set or
                        self.repeat_count.is_set or
                        self.rotate_pattern.is_set or
                        self.rtt_avg.is_set or
                        self.rtt_max.is_set or
                        self.rtt_min.is_set or
                        self.success_rate.is_set or
                        self.sweep.is_set or
                        self.sweep_max.is_set or
                        self.sweep_min.is_set or
                        self.timeout.is_set or
                        self.total.is_set or
                        (self.replies is not None and self.replies.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.destination.yfilter != YFilter.not_set or
                        self.data_size.yfilter != YFilter.not_set or
                        self.hits.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set or
                        self.pattern.yfilter != YFilter.not_set or
                        self.ping_error_response.yfilter != YFilter.not_set or
                        self.repeat_count.yfilter != YFilter.not_set or
                        self.rotate_pattern.yfilter != YFilter.not_set or
                        self.rtt_avg.yfilter != YFilter.not_set or
                        self.rtt_max.yfilter != YFilter.not_set or
                        self.rtt_min.yfilter != YFilter.not_set or
                        self.success_rate.yfilter != YFilter.not_set or
                        self.sweep.yfilter != YFilter.not_set or
                        self.sweep_max.yfilter != YFilter.not_set or
                        self.sweep_min.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set or
                        self.total.yfilter != YFilter.not_set or
                        (self.replies is not None and self.replies.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + "[destination='" + self.destination.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ping-act:ping/output/ping-response/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination.get_name_leafdata())
                    if (self.data_size.is_set or self.data_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.data_size.get_name_leafdata())
                    if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hits.get_name_leafdata())
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())
                    if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pattern.get_name_leafdata())
                    if (self.ping_error_response.is_set or self.ping_error_response.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ping_error_response.get_name_leafdata())
                    if (self.repeat_count.is_set or self.repeat_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.repeat_count.get_name_leafdata())
                    if (self.rotate_pattern.is_set or self.rotate_pattern.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rotate_pattern.get_name_leafdata())
                    if (self.rtt_avg.is_set or self.rtt_avg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_avg.get_name_leafdata())
                    if (self.rtt_max.is_set or self.rtt_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_max.get_name_leafdata())
                    if (self.rtt_min.is_set or self.rtt_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_min.get_name_leafdata())
                    if (self.success_rate.is_set or self.success_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.success_rate.get_name_leafdata())
                    if (self.sweep.is_set or self.sweep.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sweep.get_name_leafdata())
                    if (self.sweep_max.is_set or self.sweep_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sweep_max.get_name_leafdata())
                    if (self.sweep_min.is_set or self.sweep_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sweep_min.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())
                    if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "replies"):
                        if (self.replies is None):
                            self.replies = Ping.Output.PingResponse.Ipv4.Replies()
                            self.replies.parent = self
                            self._children_name_map["replies"] = "replies"
                        return self.replies

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "replies" or name == "destination" or name == "data-size" or name == "hits" or name == "interval" or name == "pattern" or name == "ping-error-response" or name == "repeat-count" or name == "rotate-pattern" or name == "rtt-avg" or name == "rtt-max" or name == "rtt-min" or name == "success-rate" or name == "sweep" or name == "sweep-max" or name == "sweep-min" or name == "timeout" or name == "total"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "destination"):
                        self.destination = value
                        self.destination.value_namespace = name_space
                        self.destination.value_namespace_prefix = name_space_prefix
                    if(value_path == "data-size"):
                        self.data_size = value
                        self.data_size.value_namespace = name_space
                        self.data_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "hits"):
                        self.hits = value
                        self.hits.value_namespace = name_space
                        self.hits.value_namespace_prefix = name_space_prefix
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "pattern"):
                        self.pattern = value
                        self.pattern.value_namespace = name_space
                        self.pattern.value_namespace_prefix = name_space_prefix
                    if(value_path == "ping-error-response"):
                        self.ping_error_response = value
                        self.ping_error_response.value_namespace = name_space
                        self.ping_error_response.value_namespace_prefix = name_space_prefix
                    if(value_path == "repeat-count"):
                        self.repeat_count = value
                        self.repeat_count.value_namespace = name_space
                        self.repeat_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "rotate-pattern"):
                        self.rotate_pattern = value
                        self.rotate_pattern.value_namespace = name_space
                        self.rotate_pattern.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-avg"):
                        self.rtt_avg = value
                        self.rtt_avg.value_namespace = name_space
                        self.rtt_avg.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-max"):
                        self.rtt_max = value
                        self.rtt_max.value_namespace = name_space
                        self.rtt_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-min"):
                        self.rtt_min = value
                        self.rtt_min.value_namespace = name_space
                        self.rtt_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "success-rate"):
                        self.success_rate = value
                        self.success_rate.value_namespace = name_space
                        self.success_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "sweep"):
                        self.sweep = value
                        self.sweep.value_namespace = name_space
                        self.sweep.value_namespace_prefix = name_space_prefix
                    if(value_path == "sweep-max"):
                        self.sweep_max = value
                        self.sweep_max.value_namespace = name_space
                        self.sweep_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "sweep-min"):
                        self.sweep_min = value
                        self.sweep_min.value_namespace = name_space
                        self.sweep_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "total"):
                        self.total = value
                        self.total.value_namespace = name_space
                        self.total.value_namespace_prefix = name_space_prefix


            class Ipv6(Entity):
                """
                
                
                .. attribute:: data_size
                
                	Size of ping packet
                	**type**\:  int
                
                	**range:** 36..18024
                
                	**default value**\: 100
                
                .. attribute:: destination
                
                	Ping destination address or hostname
                	**type**\:  str
                
                	**mandatory**\: True
                
                .. attribute:: hits
                
                	Number of packets reach to destination and get reply back
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: interval
                
                	Ping interval in milli seconds
                	**type**\:  int
                
                	**range:** 0..3600
                
                	**default value**\: 10
                
                .. attribute:: pattern
                
                	Pattern of payload data
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: repeat_count
                
                	Number of ping packets to be sent out
                	**type**\:  int
                
                	**range:** 1..64
                
                	**default value**\: 5
                
                .. attribute:: replies
                
                	
                	**type**\:   :py:class:`Replies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6.Replies>`
                
                .. attribute:: rotate_pattern
                
                	Rotate Pattern is enabled
                	**type**\:  bool
                
                .. attribute:: rtt_avg
                
                	Average value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_max
                
                	Maximum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rtt_min
                
                	Minimum value of Round Trip Time
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: success_rate
                
                	Successful rate of ping
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep
                
                	Sweep is enabled
                	**type**\:  bool
                
                .. attribute:: sweep_max
                
                	Maximum value of sweep size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: sweep_min
                
                	Minimum value of sweep size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout
                
                	Timeout in seconds
                	**type**\:  int
                
                	**range:** 0..36
                
                	**default value**\: 2
                
                .. attribute:: total
                
                	Total number of packets sent out
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ping-act'
                _revision = '2016-09-28'

                def __init__(self):
                    super(Ping.Output.PingResponse.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "ping-response"

                    self.data_size = YLeaf(YType.uint64, "data-size")

                    self.destination = YLeaf(YType.str, "destination")

                    self.hits = YLeaf(YType.uint64, "hits")

                    self.interval = YLeaf(YType.uint32, "interval")

                    self.pattern = YLeaf(YType.str, "pattern")

                    self.repeat_count = YLeaf(YType.uint64, "repeat-count")

                    self.rotate_pattern = YLeaf(YType.boolean, "rotate-pattern")

                    self.rtt_avg = YLeaf(YType.uint64, "rtt-avg")

                    self.rtt_max = YLeaf(YType.uint64, "rtt-max")

                    self.rtt_min = YLeaf(YType.uint64, "rtt-min")

                    self.success_rate = YLeaf(YType.uint64, "success-rate")

                    self.sweep = YLeaf(YType.boolean, "sweep")

                    self.sweep_max = YLeaf(YType.uint64, "sweep-max")

                    self.sweep_min = YLeaf(YType.uint32, "sweep-min")

                    self.timeout = YLeaf(YType.uint64, "timeout")

                    self.total = YLeaf(YType.uint64, "total")

                    self.replies = Ping.Output.PingResponse.Ipv6.Replies()
                    self.replies.parent = self
                    self._children_name_map["replies"] = "replies"
                    self._children_yang_names.add("replies")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("data_size",
                                    "destination",
                                    "hits",
                                    "interval",
                                    "pattern",
                                    "repeat_count",
                                    "rotate_pattern",
                                    "rtt_avg",
                                    "rtt_max",
                                    "rtt_min",
                                    "success_rate",
                                    "sweep",
                                    "sweep_max",
                                    "sweep_min",
                                    "timeout",
                                    "total") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ping.Output.PingResponse.Ipv6, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ping.Output.PingResponse.Ipv6, self).__setattr__(name, value)


                class Replies(Entity):
                    """
                    
                    
                    .. attribute:: reply
                    
                    	
                    	**type**\: list of    :py:class:`Reply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ping_act.Ping.Output.PingResponse.Ipv6.Replies.Reply>`
                    
                    

                    """

                    _prefix = 'ping-act'
                    _revision = '2016-09-28'

                    def __init__(self):
                        super(Ping.Output.PingResponse.Ipv6.Replies, self).__init__()

                        self.yang_name = "replies"
                        self.yang_parent_name = "ipv6"

                        self.reply = YList(self)

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
                                    super(Ping.Output.PingResponse.Ipv6.Replies, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ping.Output.PingResponse.Ipv6.Replies, self).__setattr__(name, value)


                    class Reply(Entity):
                        """
                        
                        
                        .. attribute:: reply_index  <key>
                        
                        	Index of the reply list
                        	**type**\:  int
                        
                        	**range:** 1..2147483647
                        
                        .. attribute:: result
                        
                        	Response for each packet
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ping-act'
                        _revision = '2016-09-28'

                        def __init__(self):
                            super(Ping.Output.PingResponse.Ipv6.Replies.Reply, self).__init__()

                            self.yang_name = "reply"
                            self.yang_parent_name = "replies"

                            self.reply_index = YLeaf(YType.uint64, "reply-index")

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
                                if name in ("reply_index",
                                            "result") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ping.Output.PingResponse.Ipv6.Replies.Reply, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ping.Output.PingResponse.Ipv6.Replies.Reply, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.reply_index.is_set or
                                self.result.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.reply_index.yfilter != YFilter.not_set or
                                self.result.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "reply" + "[reply-index='" + self.reply_index.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ping-act:ping/output/ping-response/ipv6/replies/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.reply_index.is_set or self.reply_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.reply_index.get_name_leafdata())
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
                            if(name == "reply-index" or name == "result"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "reply-index"):
                                self.reply_index = value
                                self.reply_index.value_namespace = name_space
                                self.reply_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "result"):
                                self.result = value
                                self.result.value_namespace = name_space
                                self.result.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.reply:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.reply:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "replies" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ping-act:ping/output/ping-response/ipv6/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "reply"):
                            for c in self.reply:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ping.Output.PingResponse.Ipv6.Replies.Reply()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.reply.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "reply"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.data_size.is_set or
                        self.destination.is_set or
                        self.hits.is_set or
                        self.interval.is_set or
                        self.pattern.is_set or
                        self.repeat_count.is_set or
                        self.rotate_pattern.is_set or
                        self.rtt_avg.is_set or
                        self.rtt_max.is_set or
                        self.rtt_min.is_set or
                        self.success_rate.is_set or
                        self.sweep.is_set or
                        self.sweep_max.is_set or
                        self.sweep_min.is_set or
                        self.timeout.is_set or
                        self.total.is_set or
                        (self.replies is not None and self.replies.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.data_size.yfilter != YFilter.not_set or
                        self.destination.yfilter != YFilter.not_set or
                        self.hits.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set or
                        self.pattern.yfilter != YFilter.not_set or
                        self.repeat_count.yfilter != YFilter.not_set or
                        self.rotate_pattern.yfilter != YFilter.not_set or
                        self.rtt_avg.yfilter != YFilter.not_set or
                        self.rtt_max.yfilter != YFilter.not_set or
                        self.rtt_min.yfilter != YFilter.not_set or
                        self.success_rate.yfilter != YFilter.not_set or
                        self.sweep.yfilter != YFilter.not_set or
                        self.sweep_max.yfilter != YFilter.not_set or
                        self.sweep_min.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set or
                        self.total.yfilter != YFilter.not_set or
                        (self.replies is not None and self.replies.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv6" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ping-act:ping/output/ping-response/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.data_size.is_set or self.data_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.data_size.get_name_leafdata())
                    if (self.destination.is_set or self.destination.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination.get_name_leafdata())
                    if (self.hits.is_set or self.hits.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hits.get_name_leafdata())
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())
                    if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pattern.get_name_leafdata())
                    if (self.repeat_count.is_set or self.repeat_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.repeat_count.get_name_leafdata())
                    if (self.rotate_pattern.is_set or self.rotate_pattern.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rotate_pattern.get_name_leafdata())
                    if (self.rtt_avg.is_set or self.rtt_avg.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_avg.get_name_leafdata())
                    if (self.rtt_max.is_set or self.rtt_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_max.get_name_leafdata())
                    if (self.rtt_min.is_set or self.rtt_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_min.get_name_leafdata())
                    if (self.success_rate.is_set or self.success_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.success_rate.get_name_leafdata())
                    if (self.sweep.is_set or self.sweep.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sweep.get_name_leafdata())
                    if (self.sweep_max.is_set or self.sweep_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sweep_max.get_name_leafdata())
                    if (self.sweep_min.is_set or self.sweep_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sweep_min.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())
                    if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "replies"):
                        if (self.replies is None):
                            self.replies = Ping.Output.PingResponse.Ipv6.Replies()
                            self.replies.parent = self
                            self._children_name_map["replies"] = "replies"
                        return self.replies

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "replies" or name == "data-size" or name == "destination" or name == "hits" or name == "interval" or name == "pattern" or name == "repeat-count" or name == "rotate-pattern" or name == "rtt-avg" or name == "rtt-max" or name == "rtt-min" or name == "success-rate" or name == "sweep" or name == "sweep-max" or name == "sweep-min" or name == "timeout" or name == "total"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "data-size"):
                        self.data_size = value
                        self.data_size.value_namespace = name_space
                        self.data_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination"):
                        self.destination = value
                        self.destination.value_namespace = name_space
                        self.destination.value_namespace_prefix = name_space_prefix
                    if(value_path == "hits"):
                        self.hits = value
                        self.hits.value_namespace = name_space
                        self.hits.value_namespace_prefix = name_space_prefix
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix
                    if(value_path == "pattern"):
                        self.pattern = value
                        self.pattern.value_namespace = name_space
                        self.pattern.value_namespace_prefix = name_space_prefix
                    if(value_path == "repeat-count"):
                        self.repeat_count = value
                        self.repeat_count.value_namespace = name_space
                        self.repeat_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "rotate-pattern"):
                        self.rotate_pattern = value
                        self.rotate_pattern.value_namespace = name_space
                        self.rotate_pattern.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-avg"):
                        self.rtt_avg = value
                        self.rtt_avg.value_namespace = name_space
                        self.rtt_avg.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-max"):
                        self.rtt_max = value
                        self.rtt_max.value_namespace = name_space
                        self.rtt_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-min"):
                        self.rtt_min = value
                        self.rtt_min.value_namespace = name_space
                        self.rtt_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "success-rate"):
                        self.success_rate = value
                        self.success_rate.value_namespace = name_space
                        self.success_rate.value_namespace_prefix = name_space_prefix
                    if(value_path == "sweep"):
                        self.sweep = value
                        self.sweep.value_namespace = name_space
                        self.sweep.value_namespace_prefix = name_space_prefix
                    if(value_path == "sweep-max"):
                        self.sweep_max = value
                        self.sweep_max.value_namespace = name_space
                        self.sweep_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "sweep-min"):
                        self.sweep_min = value
                        self.sweep_min.value_namespace = name_space
                        self.sweep_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "total"):
                        self.total = value
                        self.total.value_namespace = name_space
                        self.total.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.ipv4:
                    if (c.has_data()):
                        return True
                return (self.ipv6 is not None and self.ipv6.has_data())

            def has_operation(self):
                for c in self.ipv4:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ipv6 is not None and self.ipv6.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ping-response" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ping-act:ping/output/%s" % self.get_segment_path()
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
                    for c in self.ipv4:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Ping.Output.PingResponse.Ipv4()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.ipv4.append(c)
                    return c

                if (child_yang_name == "ipv6"):
                    if (self.ipv6 is None):
                        self.ipv6 = Ping.Output.PingResponse.Ipv6()
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
            return (self.ping_response is not None and self.ping_response.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.ping_response is not None and self.ping_response.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ping-act:ping/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ping-response"):
                if (self.ping_response is None):
                    self.ping_response = Ping.Output.PingResponse()
                    self.ping_response.parent = self
                    self._children_name_map["ping_response"] = "ping-response"
                return self.ping_response

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ping-response"):
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
        path_buffer = "Cisco-IOS-XR-ping-act:ping" + path_buffer

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
                self.input = Ping.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Ping.Output()
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
        self._top_entity = Ping()
        return self._top_entity

