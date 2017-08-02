""" Cisco_IOS_XR_nto_misc_shmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR nto\-misc\-shmem package operational data.

This module contains definitions
for the following management objects\:
  memory\-summary\: Memory summary information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MemorySummary(Entity):
    """
    Memory summary information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper.MemorySummary.Nodes>`
    
    

    """

    _prefix = 'nto-misc-shmem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MemorySummary, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-summary"
        self.yang_parent_name = "Cisco-IOS-XR-nto-misc-shmem-oper"

        self.nodes = MemorySummary.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Name of nodes
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper.MemorySummary.Nodes.Node>`
        
        

        """

        _prefix = 'nto-misc-shmem-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MemorySummary.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "memory-summary"

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
                        super(MemorySummary.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MemorySummary.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Name of nodes
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: detail
            
            	Detail Memory summary information for a specific node
            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper.MemorySummary.Nodes.Node.Detail>`
            
            .. attribute:: summary
            
            	Memory summary information for a specific node
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper.MemorySummary.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'nto-misc-shmem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MemorySummary.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.detail = MemorySummary.Nodes.Node.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._children_yang_names.add("detail")

                self.summary = MemorySummary.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

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
                            super(MemorySummary.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MemorySummary.Nodes.Node, self).__setattr__(name, value)


            class Summary(Entity):
                """
                Memory summary information for a specific node
                
                .. attribute:: boot_ram_size
                
                	Boot RAM size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: flash_system
                
                	Flash System size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_application_memory
                
                	Application memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_physical_memory
                
                	Physical memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: image_memory
                
                	Image memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: io_memory
                
                	IO memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: page_size
                
                	Page size in bytes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: ram_memory
                
                	Physical memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: reserved_memory
                
                	Reserved memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: system_ram_memory
                
                	Application memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'nto-misc-shmem-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MemorySummary.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"

                    self.boot_ram_size = YLeaf(YType.uint64, "boot-ram-size")

                    self.flash_system = YLeaf(YType.uint64, "flash-system")

                    self.free_application_memory = YLeaf(YType.uint64, "free-application-memory")

                    self.free_physical_memory = YLeaf(YType.uint64, "free-physical-memory")

                    self.image_memory = YLeaf(YType.uint64, "image-memory")

                    self.io_memory = YLeaf(YType.uint64, "io-memory")

                    self.page_size = YLeaf(YType.uint32, "page-size")

                    self.ram_memory = YLeaf(YType.uint64, "ram-memory")

                    self.reserved_memory = YLeaf(YType.uint64, "reserved-memory")

                    self.system_ram_memory = YLeaf(YType.uint64, "system-ram-memory")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("boot_ram_size",
                                    "flash_system",
                                    "free_application_memory",
                                    "free_physical_memory",
                                    "image_memory",
                                    "io_memory",
                                    "page_size",
                                    "ram_memory",
                                    "reserved_memory",
                                    "system_ram_memory") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MemorySummary.Nodes.Node.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MemorySummary.Nodes.Node.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.boot_ram_size.is_set or
                        self.flash_system.is_set or
                        self.free_application_memory.is_set or
                        self.free_physical_memory.is_set or
                        self.image_memory.is_set or
                        self.io_memory.is_set or
                        self.page_size.is_set or
                        self.ram_memory.is_set or
                        self.reserved_memory.is_set or
                        self.system_ram_memory.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.boot_ram_size.yfilter != YFilter.not_set or
                        self.flash_system.yfilter != YFilter.not_set or
                        self.free_application_memory.yfilter != YFilter.not_set or
                        self.free_physical_memory.yfilter != YFilter.not_set or
                        self.image_memory.yfilter != YFilter.not_set or
                        self.io_memory.yfilter != YFilter.not_set or
                        self.page_size.yfilter != YFilter.not_set or
                        self.ram_memory.yfilter != YFilter.not_set or
                        self.reserved_memory.yfilter != YFilter.not_set or
                        self.system_ram_memory.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.boot_ram_size.is_set or self.boot_ram_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.boot_ram_size.get_name_leafdata())
                    if (self.flash_system.is_set or self.flash_system.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flash_system.get_name_leafdata())
                    if (self.free_application_memory.is_set or self.free_application_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_application_memory.get_name_leafdata())
                    if (self.free_physical_memory.is_set or self.free_physical_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_physical_memory.get_name_leafdata())
                    if (self.image_memory.is_set or self.image_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.image_memory.get_name_leafdata())
                    if (self.io_memory.is_set or self.io_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.io_memory.get_name_leafdata())
                    if (self.page_size.is_set or self.page_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.page_size.get_name_leafdata())
                    if (self.ram_memory.is_set or self.ram_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ram_memory.get_name_leafdata())
                    if (self.reserved_memory.is_set or self.reserved_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reserved_memory.get_name_leafdata())
                    if (self.system_ram_memory.is_set or self.system_ram_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_ram_memory.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "boot-ram-size" or name == "flash-system" or name == "free-application-memory" or name == "free-physical-memory" or name == "image-memory" or name == "io-memory" or name == "page-size" or name == "ram-memory" or name == "reserved-memory" or name == "system-ram-memory"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "boot-ram-size"):
                        self.boot_ram_size = value
                        self.boot_ram_size.value_namespace = name_space
                        self.boot_ram_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "flash-system"):
                        self.flash_system = value
                        self.flash_system.value_namespace = name_space
                        self.flash_system.value_namespace_prefix = name_space_prefix
                    if(value_path == "free-application-memory"):
                        self.free_application_memory = value
                        self.free_application_memory.value_namespace = name_space
                        self.free_application_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "free-physical-memory"):
                        self.free_physical_memory = value
                        self.free_physical_memory.value_namespace = name_space
                        self.free_physical_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "image-memory"):
                        self.image_memory = value
                        self.image_memory.value_namespace = name_space
                        self.image_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "io-memory"):
                        self.io_memory = value
                        self.io_memory.value_namespace = name_space
                        self.io_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "page-size"):
                        self.page_size = value
                        self.page_size.value_namespace = name_space
                        self.page_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "ram-memory"):
                        self.ram_memory = value
                        self.ram_memory.value_namespace = name_space
                        self.ram_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "reserved-memory"):
                        self.reserved_memory = value
                        self.reserved_memory.value_namespace = name_space
                        self.reserved_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-ram-memory"):
                        self.system_ram_memory = value
                        self.system_ram_memory.value_namespace = name_space
                        self.system_ram_memory.value_namespace_prefix = name_space_prefix


            class Detail(Entity):
                """
                Detail Memory summary information for a
                specific node
                
                .. attribute:: allocated_memory
                
                	Allocated Memory Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: boot_ram_size
                
                	Boot RAM size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: flash_system
                
                	Flash System size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_application_memory
                
                	Application memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_physical_memory
                
                	Physical memory available in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: image_memory
                
                	Image memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: io_memory
                
                	IO memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: page_size
                
                	Page size in bytes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: private_physical_memory
                
                	Private Physical memory in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: program_data
                
                	Program Data Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_stack
                
                	Program Stack Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_text
                
                	Program Text Size
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ram_memory
                
                	Physical memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: reserved_memory
                
                	Reserved memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: shared_window
                
                	Available Shared windows
                	**type**\: list of    :py:class:`SharedWindow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper.MemorySummary.Nodes.Node.Detail.SharedWindow>`
                
                .. attribute:: system_ram_memory
                
                	Application memory size in bytes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: total_shared_window
                
                	Total Shared window
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'nto-misc-shmem-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MemorySummary.Nodes.Node.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "node"

                    self.allocated_memory = YLeaf(YType.uint64, "allocated-memory")

                    self.boot_ram_size = YLeaf(YType.uint64, "boot-ram-size")

                    self.flash_system = YLeaf(YType.uint64, "flash-system")

                    self.free_application_memory = YLeaf(YType.uint64, "free-application-memory")

                    self.free_physical_memory = YLeaf(YType.uint64, "free-physical-memory")

                    self.image_memory = YLeaf(YType.uint64, "image-memory")

                    self.io_memory = YLeaf(YType.uint64, "io-memory")

                    self.page_size = YLeaf(YType.uint32, "page-size")

                    self.private_physical_memory = YLeaf(YType.uint64, "private-physical-memory")

                    self.program_data = YLeaf(YType.uint64, "program-data")

                    self.program_stack = YLeaf(YType.uint64, "program-stack")

                    self.program_text = YLeaf(YType.uint64, "program-text")

                    self.ram_memory = YLeaf(YType.uint64, "ram-memory")

                    self.reserved_memory = YLeaf(YType.uint64, "reserved-memory")

                    self.system_ram_memory = YLeaf(YType.uint64, "system-ram-memory")

                    self.total_shared_window = YLeaf(YType.uint64, "total-shared-window")

                    self.shared_window = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("allocated_memory",
                                    "boot_ram_size",
                                    "flash_system",
                                    "free_application_memory",
                                    "free_physical_memory",
                                    "image_memory",
                                    "io_memory",
                                    "page_size",
                                    "private_physical_memory",
                                    "program_data",
                                    "program_stack",
                                    "program_text",
                                    "ram_memory",
                                    "reserved_memory",
                                    "system_ram_memory",
                                    "total_shared_window") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MemorySummary.Nodes.Node.Detail, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MemorySummary.Nodes.Node.Detail, self).__setattr__(name, value)


                class SharedWindow(Entity):
                    """
                    Available Shared windows
                    
                    .. attribute:: shared_window
                    
                    	Name of shared window
                    	**type**\:  str
                    
                    .. attribute:: window_size
                    
                    	Size of shared window
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'nto-misc-shmem-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MemorySummary.Nodes.Node.Detail.SharedWindow, self).__init__()

                        self.yang_name = "shared-window"
                        self.yang_parent_name = "detail"

                        self.shared_window = YLeaf(YType.str, "shared-window")

                        self.window_size = YLeaf(YType.uint64, "window-size")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("shared_window",
                                        "window_size") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MemorySummary.Nodes.Node.Detail.SharedWindow, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MemorySummary.Nodes.Node.Detail.SharedWindow, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.shared_window.is_set or
                            self.window_size.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.shared_window.yfilter != YFilter.not_set or
                            self.window_size.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "shared-window" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.shared_window.is_set or self.shared_window.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shared_window.get_name_leafdata())
                        if (self.window_size.is_set or self.window_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.window_size.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "shared-window" or name == "window-size"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "shared-window"):
                            self.shared_window = value
                            self.shared_window.value_namespace = name_space
                            self.shared_window.value_namespace_prefix = name_space_prefix
                        if(value_path == "window-size"):
                            self.window_size = value
                            self.window_size.value_namespace = name_space
                            self.window_size.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.shared_window:
                        if (c.has_data()):
                            return True
                    return (
                        self.allocated_memory.is_set or
                        self.boot_ram_size.is_set or
                        self.flash_system.is_set or
                        self.free_application_memory.is_set or
                        self.free_physical_memory.is_set or
                        self.image_memory.is_set or
                        self.io_memory.is_set or
                        self.page_size.is_set or
                        self.private_physical_memory.is_set or
                        self.program_data.is_set or
                        self.program_stack.is_set or
                        self.program_text.is_set or
                        self.ram_memory.is_set or
                        self.reserved_memory.is_set or
                        self.system_ram_memory.is_set or
                        self.total_shared_window.is_set)

                def has_operation(self):
                    for c in self.shared_window:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.allocated_memory.yfilter != YFilter.not_set or
                        self.boot_ram_size.yfilter != YFilter.not_set or
                        self.flash_system.yfilter != YFilter.not_set or
                        self.free_application_memory.yfilter != YFilter.not_set or
                        self.free_physical_memory.yfilter != YFilter.not_set or
                        self.image_memory.yfilter != YFilter.not_set or
                        self.io_memory.yfilter != YFilter.not_set or
                        self.page_size.yfilter != YFilter.not_set or
                        self.private_physical_memory.yfilter != YFilter.not_set or
                        self.program_data.yfilter != YFilter.not_set or
                        self.program_stack.yfilter != YFilter.not_set or
                        self.program_text.yfilter != YFilter.not_set or
                        self.ram_memory.yfilter != YFilter.not_set or
                        self.reserved_memory.yfilter != YFilter.not_set or
                        self.system_ram_memory.yfilter != YFilter.not_set or
                        self.total_shared_window.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "detail" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.allocated_memory.is_set or self.allocated_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.allocated_memory.get_name_leafdata())
                    if (self.boot_ram_size.is_set or self.boot_ram_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.boot_ram_size.get_name_leafdata())
                    if (self.flash_system.is_set or self.flash_system.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.flash_system.get_name_leafdata())
                    if (self.free_application_memory.is_set or self.free_application_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_application_memory.get_name_leafdata())
                    if (self.free_physical_memory.is_set or self.free_physical_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_physical_memory.get_name_leafdata())
                    if (self.image_memory.is_set or self.image_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.image_memory.get_name_leafdata())
                    if (self.io_memory.is_set or self.io_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.io_memory.get_name_leafdata())
                    if (self.page_size.is_set or self.page_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.page_size.get_name_leafdata())
                    if (self.private_physical_memory.is_set or self.private_physical_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.private_physical_memory.get_name_leafdata())
                    if (self.program_data.is_set or self.program_data.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.program_data.get_name_leafdata())
                    if (self.program_stack.is_set or self.program_stack.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.program_stack.get_name_leafdata())
                    if (self.program_text.is_set or self.program_text.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.program_text.get_name_leafdata())
                    if (self.ram_memory.is_set or self.ram_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ram_memory.get_name_leafdata())
                    if (self.reserved_memory.is_set or self.reserved_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reserved_memory.get_name_leafdata())
                    if (self.system_ram_memory.is_set or self.system_ram_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.system_ram_memory.get_name_leafdata())
                    if (self.total_shared_window.is_set or self.total_shared_window.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_shared_window.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "shared-window"):
                        for c in self.shared_window:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MemorySummary.Nodes.Node.Detail.SharedWindow()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.shared_window.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "shared-window" or name == "allocated-memory" or name == "boot-ram-size" or name == "flash-system" or name == "free-application-memory" or name == "free-physical-memory" or name == "image-memory" or name == "io-memory" or name == "page-size" or name == "private-physical-memory" or name == "program-data" or name == "program-stack" or name == "program-text" or name == "ram-memory" or name == "reserved-memory" or name == "system-ram-memory" or name == "total-shared-window"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "allocated-memory"):
                        self.allocated_memory = value
                        self.allocated_memory.value_namespace = name_space
                        self.allocated_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "boot-ram-size"):
                        self.boot_ram_size = value
                        self.boot_ram_size.value_namespace = name_space
                        self.boot_ram_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "flash-system"):
                        self.flash_system = value
                        self.flash_system.value_namespace = name_space
                        self.flash_system.value_namespace_prefix = name_space_prefix
                    if(value_path == "free-application-memory"):
                        self.free_application_memory = value
                        self.free_application_memory.value_namespace = name_space
                        self.free_application_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "free-physical-memory"):
                        self.free_physical_memory = value
                        self.free_physical_memory.value_namespace = name_space
                        self.free_physical_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "image-memory"):
                        self.image_memory = value
                        self.image_memory.value_namespace = name_space
                        self.image_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "io-memory"):
                        self.io_memory = value
                        self.io_memory.value_namespace = name_space
                        self.io_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "page-size"):
                        self.page_size = value
                        self.page_size.value_namespace = name_space
                        self.page_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "private-physical-memory"):
                        self.private_physical_memory = value
                        self.private_physical_memory.value_namespace = name_space
                        self.private_physical_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "program-data"):
                        self.program_data = value
                        self.program_data.value_namespace = name_space
                        self.program_data.value_namespace_prefix = name_space_prefix
                    if(value_path == "program-stack"):
                        self.program_stack = value
                        self.program_stack.value_namespace = name_space
                        self.program_stack.value_namespace_prefix = name_space_prefix
                    if(value_path == "program-text"):
                        self.program_text = value
                        self.program_text.value_namespace = name_space
                        self.program_text.value_namespace_prefix = name_space_prefix
                    if(value_path == "ram-memory"):
                        self.ram_memory = value
                        self.ram_memory.value_namespace = name_space
                        self.ram_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "reserved-memory"):
                        self.reserved_memory = value
                        self.reserved_memory.value_namespace = name_space
                        self.reserved_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "system-ram-memory"):
                        self.system_ram_memory = value
                        self.system_ram_memory.value_namespace = name_space
                        self.system_ram_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-shared-window"):
                        self.total_shared_window = value
                        self.total_shared_window.value_namespace = name_space
                        self.total_shared_window.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.detail is not None and self.detail.has_data()) or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.detail is not None and self.detail.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-nto-misc-shmem-oper:memory-summary/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "detail"):
                    if (self.detail is None):
                        self.detail = MemorySummary.Nodes.Node.Detail()
                        self.detail.parent = self
                        self._children_name_map["detail"] = "detail"
                    return self.detail

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = MemorySummary.Nodes.Node.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "detail" or name == "summary" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-nto-misc-shmem-oper:memory-summary/%s" % self.get_segment_path()
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
                c = MemorySummary.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-nto-misc-shmem-oper:memory-summary" + path_buffer

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
                self.nodes = MemorySummary.Nodes()
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
        self._top_entity = MemorySummary()
        return self._top_entity

