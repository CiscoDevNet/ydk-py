""" Cisco_IOS_XR_wd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wd package operational data.

This module contains definitions
for the following management objects\:
  watchdog\: Watchdog information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MemoryState(Enum):
    """
    MemoryState

    Memory state options

    .. data:: unknown = 0

    	Memory state unknown

    .. data:: normal = 1

    	Memory state normal

    .. data:: minor = 2

    	Memory state minor

    .. data:: severe = 3

    	Memory state severe

    .. data:: critical = 4

    	Memory state critical

    """

    unknown = Enum.YLeaf(0, "unknown")

    normal = Enum.YLeaf(1, "normal")

    minor = Enum.YLeaf(2, "minor")

    severe = Enum.YLeaf(3, "severe")

    critical = Enum.YLeaf(4, "critical")


class OverloadCtrlNotif(Enum):
    """
    OverloadCtrlNotif

    Overload control notification

    .. data:: disabled = 0

    	Diabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")



class Watchdog(Entity):
    """
    Watchdog information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes>`
    
    

    """

    _prefix = 'wd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Watchdog, self).__init__()
        self._top_entity = None

        self.yang_name = "watchdog"
        self.yang_parent_name = "Cisco-IOS-XR-wd-oper"

        self.nodes = Watchdog.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node>`
        
        

        """

        _prefix = 'wd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Watchdog.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "watchdog"

            self.node = YList(self)

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
                        super(Watchdog.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Watchdog.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node ID
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: memory_state
            
            	Memory state
            	**type**\:   :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.MemoryState>`
            
            .. attribute:: overload_state
            
            	Display overload control state
            	**type**\:   :py:class:`OverloadState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState>`
            
            .. attribute:: threshold_memory
            
            	Threshold memory
            	**type**\:   :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory>`
            
            

            """

            _prefix = 'wd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Watchdog.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.memory_state = Watchdog.Nodes.Node.MemoryState()
                self.memory_state.parent = self
                self._children_name_map["memory_state"] = "memory-state"
                self._children_yang_names.add("memory-state")

                self.overload_state = Watchdog.Nodes.Node.OverloadState()
                self.overload_state.parent = self
                self._children_name_map["overload_state"] = "overload-state"
                self._children_yang_names.add("overload-state")

                self.threshold_memory = Watchdog.Nodes.Node.ThresholdMemory()
                self.threshold_memory.parent = self
                self._children_name_map["threshold_memory"] = "threshold-memory"
                self._children_yang_names.add("threshold-memory")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Watchdog.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Watchdog.Nodes.Node, self).__setattr__(name, value)


            class ThresholdMemory(Entity):
                """
                Threshold memory
                
                .. attribute:: configured
                
                	Memory configured by user
                	**type**\:   :py:class:`Configured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Configured>`
                
                .. attribute:: default
                
                	System default memory
                	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default>`
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Watchdog.Nodes.Node.ThresholdMemory, self).__init__()

                    self.yang_name = "threshold-memory"
                    self.yang_parent_name = "node"

                    self.configured = Watchdog.Nodes.Node.ThresholdMemory.Configured()
                    self.configured.parent = self
                    self._children_name_map["configured"] = "configured"
                    self._children_yang_names.add("configured")

                    self.default = Watchdog.Nodes.Node.ThresholdMemory.Default()
                    self.default.parent = self
                    self._children_name_map["default"] = "default"
                    self._children_yang_names.add("default")


                class Default(Entity):
                    """
                    System default memory
                    
                    .. attribute:: configured_memory
                    
                    	Configured memory
                    	**type**\:   :py:class:`ConfiguredMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory>`
                    
                    .. attribute:: memory
                    
                    	Memory Information
                    	**type**\:   :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.ThresholdMemory.Default.Memory>`
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Watchdog.Nodes.Node.ThresholdMemory.Default, self).__init__()

                        self.yang_name = "default"
                        self.yang_parent_name = "threshold-memory"

                        self.configured_memory = Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory()
                        self.configured_memory.parent = self
                        self._children_name_map["configured_memory"] = "configured-memory"
                        self._children_yang_names.add("configured-memory")

                        self.memory = Watchdog.Nodes.Node.ThresholdMemory.Default.Memory()
                        self.memory.parent = self
                        self._children_name_map["memory"] = "memory"
                        self._children_yang_names.add("memory")


                    class ConfiguredMemory(Entity):
                        """
                        Configured memory
                        
                        .. attribute:: critical
                        
                        	Critical memory in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: minor
                        
                        	Minor memory threshold in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: severe
                        
                        	Severe memory threshold in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'wd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory, self).__init__()

                            self.yang_name = "configured-memory"
                            self.yang_parent_name = "default"

                            self.critical = YLeaf(YType.uint64, "critical")

                            self.minor = YLeaf(YType.uint32, "minor")

                            self.severe = YLeaf(YType.uint32, "severe")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("critical",
                                            "minor",
                                            "severe") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.critical.is_set or
                                self.minor.is_set or
                                self.severe.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.critical.yfilter != YFilter.not_set or
                                self.minor.yfilter != YFilter.not_set or
                                self.severe.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "configured-memory" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.critical.get_name_leafdata())
                            if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.minor.get_name_leafdata())
                            if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.severe.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "critical" or name == "minor" or name == "severe"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "critical"):
                                self.critical = value
                                self.critical.value_namespace = name_space
                                self.critical.value_namespace_prefix = name_space_prefix
                            if(value_path == "minor"):
                                self.minor = value
                                self.minor.value_namespace = name_space
                                self.minor.value_namespace_prefix = name_space_prefix
                            if(value_path == "severe"):
                                self.severe = value
                                self.severe.value_namespace = name_space
                                self.severe.value_namespace_prefix = name_space_prefix


                    class Memory(Entity):
                        """
                        Memory Information
                        
                        .. attribute:: free_memory
                        
                        	Free memory in bytes
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: byte
                        
                        .. attribute:: memory_state
                        
                        	State of memory
                        	**type**\:   :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.MemoryState>`
                        
                        .. attribute:: physical_memory
                        
                        	Physical memory in bytes
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        

                        """

                        _prefix = 'wd-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Watchdog.Nodes.Node.ThresholdMemory.Default.Memory, self).__init__()

                            self.yang_name = "memory"
                            self.yang_parent_name = "default"

                            self.free_memory = YLeaf(YType.uint64, "free-memory")

                            self.memory_state = YLeaf(YType.enumeration, "memory-state")

                            self.physical_memory = YLeaf(YType.uint32, "physical-memory")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("free_memory",
                                            "memory_state",
                                            "physical_memory") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Watchdog.Nodes.Node.ThresholdMemory.Default.Memory, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Watchdog.Nodes.Node.ThresholdMemory.Default.Memory, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.free_memory.is_set or
                                self.memory_state.is_set or
                                self.physical_memory.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.free_memory.yfilter != YFilter.not_set or
                                self.memory_state.yfilter != YFilter.not_set or
                                self.physical_memory.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "memory" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.free_memory.is_set or self.free_memory.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.free_memory.get_name_leafdata())
                            if (self.memory_state.is_set or self.memory_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.memory_state.get_name_leafdata())
                            if (self.physical_memory.is_set or self.physical_memory.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.physical_memory.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "free-memory" or name == "memory-state" or name == "physical-memory"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "free-memory"):
                                self.free_memory = value
                                self.free_memory.value_namespace = name_space
                                self.free_memory.value_namespace_prefix = name_space_prefix
                            if(value_path == "memory-state"):
                                self.memory_state = value
                                self.memory_state.value_namespace = name_space
                                self.memory_state.value_namespace_prefix = name_space_prefix
                            if(value_path == "physical-memory"):
                                self.physical_memory = value
                                self.physical_memory.value_namespace = name_space
                                self.physical_memory.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.configured_memory is not None and self.configured_memory.has_data()) or
                            (self.memory is not None and self.memory.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.configured_memory is not None and self.configured_memory.has_operation()) or
                            (self.memory is not None and self.memory.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "default" + path_buffer

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

                        if (child_yang_name == "configured-memory"):
                            if (self.configured_memory is None):
                                self.configured_memory = Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory()
                                self.configured_memory.parent = self
                                self._children_name_map["configured_memory"] = "configured-memory"
                            return self.configured_memory

                        if (child_yang_name == "memory"):
                            if (self.memory is None):
                                self.memory = Watchdog.Nodes.Node.ThresholdMemory.Default.Memory()
                                self.memory.parent = self
                                self._children_name_map["memory"] = "memory"
                            return self.memory

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "configured-memory" or name == "memory"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Configured(Entity):
                    """
                    Memory configured by user
                    
                    .. attribute:: critical
                    
                    	Critical memory in bytes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    	**units**\: byte
                    
                    .. attribute:: minor
                    
                    	Minor memory threshold in bytes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: severe
                    
                    	Severe memory threshold in bytes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Watchdog.Nodes.Node.ThresholdMemory.Configured, self).__init__()

                        self.yang_name = "configured"
                        self.yang_parent_name = "threshold-memory"

                        self.critical = YLeaf(YType.uint64, "critical")

                        self.minor = YLeaf(YType.uint32, "minor")

                        self.severe = YLeaf(YType.uint32, "severe")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("critical",
                                        "minor",
                                        "severe") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Watchdog.Nodes.Node.ThresholdMemory.Configured, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Watchdog.Nodes.Node.ThresholdMemory.Configured, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.critical.is_set or
                            self.minor.is_set or
                            self.severe.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.critical.yfilter != YFilter.not_set or
                            self.minor.yfilter != YFilter.not_set or
                            self.severe.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "configured" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.critical.get_name_leafdata())
                        if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minor.get_name_leafdata())
                        if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.severe.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "critical" or name == "minor" or name == "severe"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "critical"):
                            self.critical = value
                            self.critical.value_namespace = name_space
                            self.critical.value_namespace_prefix = name_space_prefix
                        if(value_path == "minor"):
                            self.minor = value
                            self.minor.value_namespace = name_space
                            self.minor.value_namespace_prefix = name_space_prefix
                        if(value_path == "severe"):
                            self.severe = value
                            self.severe.value_namespace = name_space
                            self.severe.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.configured is not None and self.configured.has_data()) or
                        (self.default is not None and self.default.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.configured is not None and self.configured.has_operation()) or
                        (self.default is not None and self.default.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "threshold-memory" + path_buffer

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

                    if (child_yang_name == "configured"):
                        if (self.configured is None):
                            self.configured = Watchdog.Nodes.Node.ThresholdMemory.Configured()
                            self.configured.parent = self
                            self._children_name_map["configured"] = "configured"
                        return self.configured

                    if (child_yang_name == "default"):
                        if (self.default is None):
                            self.default = Watchdog.Nodes.Node.ThresholdMemory.Default()
                            self.default.parent = self
                            self._children_name_map["default"] = "default"
                        return self.default

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "configured" or name == "default"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class MemoryState(Entity):
                """
                Memory state
                
                .. attribute:: free_memory
                
                	Free memory in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: memory_state
                
                	State of memory
                	**type**\:   :py:class:`MemoryState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.MemoryState>`
                
                .. attribute:: physical_memory
                
                	Physical memory in bytes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Watchdog.Nodes.Node.MemoryState, self).__init__()

                    self.yang_name = "memory-state"
                    self.yang_parent_name = "node"

                    self.free_memory = YLeaf(YType.uint64, "free-memory")

                    self.memory_state = YLeaf(YType.enumeration, "memory-state")

                    self.physical_memory = YLeaf(YType.uint32, "physical-memory")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("free_memory",
                                    "memory_state",
                                    "physical_memory") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Watchdog.Nodes.Node.MemoryState, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Watchdog.Nodes.Node.MemoryState, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.free_memory.is_set or
                        self.memory_state.is_set or
                        self.physical_memory.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.free_memory.yfilter != YFilter.not_set or
                        self.memory_state.yfilter != YFilter.not_set or
                        self.physical_memory.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.free_memory.is_set or self.free_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_memory.get_name_leafdata())
                    if (self.memory_state.is_set or self.memory_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_state.get_name_leafdata())
                    if (self.physical_memory.is_set or self.physical_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.physical_memory.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "free-memory" or name == "memory-state" or name == "physical-memory"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "free-memory"):
                        self.free_memory = value
                        self.free_memory.value_namespace = name_space
                        self.free_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "memory-state"):
                        self.memory_state = value
                        self.memory_state.value_namespace = name_space
                        self.memory_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "physical-memory"):
                        self.physical_memory = value
                        self.physical_memory.value_namespace = name_space
                        self.physical_memory.value_namespace_prefix = name_space_prefix


            class OverloadState(Entity):
                """
                Display overload control state
                
                .. attribute:: configured_wdsysmon_throttle
                
                	Configured resmon throttle
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_throttle
                
                	Current throttle information
                	**type**\:   :py:class:`CurrentThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState.CurrentThrottle>`
                
                .. attribute:: default_wdsysmon_throttle
                
                	Default resmon throttle
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_throttle
                
                	Last throttle information
                	**type**\: list of    :py:class:`LastThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.Watchdog.Nodes.Node.OverloadState.LastThrottle>`
                
                .. attribute:: overload_control_notification
                
                	State of overload control notification
                	**type**\:   :py:class:`OverloadCtrlNotif <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper.OverloadCtrlNotif>`
                
                

                """

                _prefix = 'wd-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Watchdog.Nodes.Node.OverloadState, self).__init__()

                    self.yang_name = "overload-state"
                    self.yang_parent_name = "node"

                    self.configured_wdsysmon_throttle = YLeaf(YType.uint32, "configured-wdsysmon-throttle")

                    self.default_wdsysmon_throttle = YLeaf(YType.uint32, "default-wdsysmon-throttle")

                    self.overload_control_notification = YLeaf(YType.enumeration, "overload-control-notification")

                    self.current_throttle = Watchdog.Nodes.Node.OverloadState.CurrentThrottle()
                    self.current_throttle.parent = self
                    self._children_name_map["current_throttle"] = "current-throttle"
                    self._children_yang_names.add("current-throttle")

                    self.last_throttle = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("configured_wdsysmon_throttle",
                                    "default_wdsysmon_throttle",
                                    "overload_control_notification") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Watchdog.Nodes.Node.OverloadState, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Watchdog.Nodes.Node.OverloadState, self).__setattr__(name, value)


                class CurrentThrottle(Entity):
                    """
                    Current throttle information
                    
                    .. attribute:: start_time
                    
                    	Current throttle start time in format  \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\:  str
                    
                    	**length:** 0..25
                    
                    .. attribute:: throttle_duration
                    
                    	Current throttle duration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Watchdog.Nodes.Node.OverloadState.CurrentThrottle, self).__init__()

                        self.yang_name = "current-throttle"
                        self.yang_parent_name = "overload-state"

                        self.start_time = YLeaf(YType.str, "start-time")

                        self.throttle_duration = YLeaf(YType.uint32, "throttle-duration")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("start_time",
                                        "throttle_duration") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Watchdog.Nodes.Node.OverloadState.CurrentThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Watchdog.Nodes.Node.OverloadState.CurrentThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.start_time.is_set or
                            self.throttle_duration.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.start_time.yfilter != YFilter.not_set or
                            self.throttle_duration.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "current-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_time.get_name_leafdata())
                        if (self.throttle_duration.is_set or self.throttle_duration.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle_duration.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "start-time" or name == "throttle-duration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "start-time"):
                            self.start_time = value
                            self.start_time.value_namespace = name_space
                            self.start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle-duration"):
                            self.throttle_duration = value
                            self.throttle_duration.value_namespace = name_space
                            self.throttle_duration.value_namespace_prefix = name_space_prefix


                class LastThrottle(Entity):
                    """
                    Last throttle information
                    
                    .. attribute:: start_time
                    
                    	Last throttle start time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\:  str
                    
                    	**length:** 0..25
                    
                    .. attribute:: stop_time
                    
                    	Last throttle stop time in format \:day\-of\-week month date\-of\-month HH\:MM\:SS year eg\: Thu Feb 1 18\:32\:14 2011
                    	**type**\:  str
                    
                    	**length:** 0..25
                    
                    .. attribute:: throttle_duration
                    
                    	Last throttle duration in seconds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'wd-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Watchdog.Nodes.Node.OverloadState.LastThrottle, self).__init__()

                        self.yang_name = "last-throttle"
                        self.yang_parent_name = "overload-state"

                        self.start_time = YLeaf(YType.str, "start-time")

                        self.stop_time = YLeaf(YType.str, "stop-time")

                        self.throttle_duration = YLeaf(YType.uint32, "throttle-duration")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("start_time",
                                        "stop_time",
                                        "throttle_duration") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Watchdog.Nodes.Node.OverloadState.LastThrottle, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Watchdog.Nodes.Node.OverloadState.LastThrottle, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.start_time.is_set or
                            self.stop_time.is_set or
                            self.throttle_duration.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.start_time.yfilter != YFilter.not_set or
                            self.stop_time.yfilter != YFilter.not_set or
                            self.throttle_duration.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "last-throttle" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_time.get_name_leafdata())
                        if (self.stop_time.is_set or self.stop_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stop_time.get_name_leafdata())
                        if (self.throttle_duration.is_set or self.throttle_duration.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.throttle_duration.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "start-time" or name == "stop-time" or name == "throttle-duration"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "start-time"):
                            self.start_time = value
                            self.start_time.value_namespace = name_space
                            self.start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "stop-time"):
                            self.stop_time = value
                            self.stop_time.value_namespace = name_space
                            self.stop_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "throttle-duration"):
                            self.throttle_duration = value
                            self.throttle_duration.value_namespace = name_space
                            self.throttle_duration.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.last_throttle:
                        if (c.has_data()):
                            return True
                    return (
                        self.configured_wdsysmon_throttle.is_set or
                        self.default_wdsysmon_throttle.is_set or
                        self.overload_control_notification.is_set or
                        (self.current_throttle is not None and self.current_throttle.has_data()))

                def has_operation(self):
                    for c in self.last_throttle:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.configured_wdsysmon_throttle.yfilter != YFilter.not_set or
                        self.default_wdsysmon_throttle.yfilter != YFilter.not_set or
                        self.overload_control_notification.yfilter != YFilter.not_set or
                        (self.current_throttle is not None and self.current_throttle.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "overload-state" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.configured_wdsysmon_throttle.is_set or self.configured_wdsysmon_throttle.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.configured_wdsysmon_throttle.get_name_leafdata())
                    if (self.default_wdsysmon_throttle.is_set or self.default_wdsysmon_throttle.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_wdsysmon_throttle.get_name_leafdata())
                    if (self.overload_control_notification.is_set or self.overload_control_notification.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.overload_control_notification.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "current-throttle"):
                        if (self.current_throttle is None):
                            self.current_throttle = Watchdog.Nodes.Node.OverloadState.CurrentThrottle()
                            self.current_throttle.parent = self
                            self._children_name_map["current_throttle"] = "current-throttle"
                        return self.current_throttle

                    if (child_yang_name == "last-throttle"):
                        for c in self.last_throttle:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Watchdog.Nodes.Node.OverloadState.LastThrottle()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.last_throttle.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "current-throttle" or name == "last-throttle" or name == "configured-wdsysmon-throttle" or name == "default-wdsysmon-throttle" or name == "overload-control-notification"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "configured-wdsysmon-throttle"):
                        self.configured_wdsysmon_throttle = value
                        self.configured_wdsysmon_throttle.value_namespace = name_space
                        self.configured_wdsysmon_throttle.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-wdsysmon-throttle"):
                        self.default_wdsysmon_throttle = value
                        self.default_wdsysmon_throttle.value_namespace = name_space
                        self.default_wdsysmon_throttle.value_namespace_prefix = name_space_prefix
                    if(value_path == "overload-control-notification"):
                        self.overload_control_notification = value
                        self.overload_control_notification.value_namespace = name_space
                        self.overload_control_notification.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.memory_state is not None and self.memory_state.has_data()) or
                    (self.overload_state is not None and self.overload_state.has_data()) or
                    (self.threshold_memory is not None and self.threshold_memory.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.memory_state is not None and self.memory_state.has_operation()) or
                    (self.overload_state is not None and self.overload_state.has_operation()) or
                    (self.threshold_memory is not None and self.threshold_memory.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-wd-oper:watchdog/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "memory-state"):
                    if (self.memory_state is None):
                        self.memory_state = Watchdog.Nodes.Node.MemoryState()
                        self.memory_state.parent = self
                        self._children_name_map["memory_state"] = "memory-state"
                    return self.memory_state

                if (child_yang_name == "overload-state"):
                    if (self.overload_state is None):
                        self.overload_state = Watchdog.Nodes.Node.OverloadState()
                        self.overload_state.parent = self
                        self._children_name_map["overload_state"] = "overload-state"
                    return self.overload_state

                if (child_yang_name == "threshold-memory"):
                    if (self.threshold_memory is None):
                        self.threshold_memory = Watchdog.Nodes.Node.ThresholdMemory()
                        self.threshold_memory.parent = self
                        self._children_name_map["threshold_memory"] = "threshold-memory"
                    return self.threshold_memory

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "memory-state" or name == "overload-state" or name == "threshold-memory" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-wd-oper:watchdog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Watchdog.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-wd-oper:watchdog" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Watchdog.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity

