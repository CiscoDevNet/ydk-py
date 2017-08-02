""" Cisco_IOS_XE_memory_oper 

This module contains a collection of YANG definitions for
monitoring memory in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MemoryStatistics(Entity):
    """
    Data nodes for All Memory Pool Statistics.
    
    .. attribute:: memory_statistic
    
    	The list of software memory pools in the system
    	**type**\: list of    :py:class:`MemoryStatistic <ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper.MemoryStatistics.MemoryStatistic>`
    
    

    """

    _prefix = 'memory-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(MemoryStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-statistics"
        self.yang_parent_name = "Cisco-IOS-XE-memory-oper"

        self.memory_statistic = YList(self)

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
                    super(MemoryStatistics, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MemoryStatistics, self).__setattr__(name, value)


    class MemoryStatistic(Entity):
        """
        The list of software memory pools in the system.
        
        .. attribute:: name  <key>
        
        	The name of the memory pool
        	**type**\:  str
        
        .. attribute:: free_memory
        
        	Total free memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: highest_usage
        
        	Historical highest memory usage (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: lowest_usage
        
        	Historical lowest memory usage (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: total_memory
        
        	Total memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        .. attribute:: used_memory
        
        	Total used memory in the pool (bytes)
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        	**units**\: bytes
        
        

        """

        _prefix = 'memory-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(MemoryStatistics.MemoryStatistic, self).__init__()

            self.yang_name = "memory-statistic"
            self.yang_parent_name = "memory-statistics"

            self.name = YLeaf(YType.str, "name")

            self.free_memory = YLeaf(YType.uint64, "free-memory")

            self.highest_usage = YLeaf(YType.uint64, "highest-usage")

            self.lowest_usage = YLeaf(YType.uint64, "lowest-usage")

            self.total_memory = YLeaf(YType.uint64, "total-memory")

            self.used_memory = YLeaf(YType.uint64, "used-memory")

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
                            "free_memory",
                            "highest_usage",
                            "lowest_usage",
                            "total_memory",
                            "used_memory") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MemoryStatistics.MemoryStatistic, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MemoryStatistics.MemoryStatistic, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.name.is_set or
                self.free_memory.is_set or
                self.highest_usage.is_set or
                self.lowest_usage.is_set or
                self.total_memory.is_set or
                self.used_memory.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.free_memory.yfilter != YFilter.not_set or
                self.highest_usage.yfilter != YFilter.not_set or
                self.lowest_usage.yfilter != YFilter.not_set or
                self.total_memory.yfilter != YFilter.not_set or
                self.used_memory.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "memory-statistic" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-memory-oper:memory-statistics/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.free_memory.is_set or self.free_memory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.free_memory.get_name_leafdata())
            if (self.highest_usage.is_set or self.highest_usage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.highest_usage.get_name_leafdata())
            if (self.lowest_usage.is_set or self.lowest_usage.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lowest_usage.get_name_leafdata())
            if (self.total_memory.is_set or self.total_memory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.total_memory.get_name_leafdata())
            if (self.used_memory.is_set or self.used_memory.yfilter != YFilter.not_set):
                leaf_name_data.append(self.used_memory.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "name" or name == "free-memory" or name == "highest-usage" or name == "lowest-usage" or name == "total-memory" or name == "used-memory"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "free-memory"):
                self.free_memory = value
                self.free_memory.value_namespace = name_space
                self.free_memory.value_namespace_prefix = name_space_prefix
            if(value_path == "highest-usage"):
                self.highest_usage = value
                self.highest_usage.value_namespace = name_space
                self.highest_usage.value_namespace_prefix = name_space_prefix
            if(value_path == "lowest-usage"):
                self.lowest_usage = value
                self.lowest_usage.value_namespace = name_space
                self.lowest_usage.value_namespace_prefix = name_space_prefix
            if(value_path == "total-memory"):
                self.total_memory = value
                self.total_memory.value_namespace = name_space
                self.total_memory.value_namespace_prefix = name_space_prefix
            if(value_path == "used-memory"):
                self.used_memory = value
                self.used_memory.value_namespace = name_space
                self.used_memory.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.memory_statistic:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.memory_statistic:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-memory-oper:memory-statistics" + path_buffer

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

        if (child_yang_name == "memory-statistic"):
            for c in self.memory_statistic:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = MemoryStatistics.MemoryStatistic()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.memory_statistic.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "memory-statistic"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MemoryStatistics()
        return self._top_entity

