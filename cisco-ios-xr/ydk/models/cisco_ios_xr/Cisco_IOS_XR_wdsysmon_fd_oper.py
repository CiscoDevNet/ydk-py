""" Cisco_IOS_XR_wdsysmon_fd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wdsysmon\-fd package operational data.

This module contains definitions
for the following management objects\:
  system\-monitoring\: Processes operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SystemMonitoring(Entity):
    """
    Processes operational data
    
    .. attribute:: cpu_utilization
    
    	Processes CPU utilization information
    	**type**\: list of    :py:class:`CpuUtilization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper.SystemMonitoring.CpuUtilization>`
    
    

    """

    _prefix = 'wdsysmon-fd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SystemMonitoring, self).__init__()
        self._top_entity = None

        self.yang_name = "system-monitoring"
        self.yang_parent_name = "Cisco-IOS-XR-wdsysmon-fd-oper"

        self.cpu_utilization = YList(self)

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
                    super(SystemMonitoring, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(SystemMonitoring, self).__setattr__(name, value)


    class CpuUtilization(Entity):
        """
        Processes CPU utilization information
        
        .. attribute:: node_name  <key>
        
        	Node name
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: process_cpu
        
        	Per process CPU utilization
        	**type**\: list of    :py:class:`ProcessCpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wdsysmon_fd_oper.SystemMonitoring.CpuUtilization.ProcessCpu>`
        
        .. attribute:: total_cpu_fifteen_minute
        
        	Total CPU utilization in past 15 minute
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: total_cpu_five_minute
        
        	Total CPU utilization in past 5 minute
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: total_cpu_one_minute
        
        	Total CPU utilization in past 1 minute
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'wdsysmon-fd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SystemMonitoring.CpuUtilization, self).__init__()

            self.yang_name = "cpu-utilization"
            self.yang_parent_name = "system-monitoring"

            self.node_name = YLeaf(YType.str, "node-name")

            self.total_cpu_fifteen_minute = YLeaf(YType.uint32, "total-cpu-fifteen-minute")

            self.total_cpu_five_minute = YLeaf(YType.uint32, "total-cpu-five-minute")

            self.total_cpu_one_minute = YLeaf(YType.uint32, "total-cpu-one-minute")

            self.process_cpu = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("node_name",
                            "total_cpu_fifteen_minute",
                            "total_cpu_five_minute",
                            "total_cpu_one_minute") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SystemMonitoring.CpuUtilization, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SystemMonitoring.CpuUtilization, self).__setattr__(name, value)


        class ProcessCpu(Entity):
            """
            Per process CPU utilization
            
            .. attribute:: process_cpu_fifteen_minute
            
            	Process CPU utilization in percent for past 15 minute
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            .. attribute:: process_cpu_five_minute
            
            	Process CPU utilization in percent for past 5 minute
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            .. attribute:: process_cpu_one_minute
            
            	Process CPU utilization in percent for past 1 minute
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: percentage
            
            .. attribute:: process_id
            
            	Process ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: process_name
            
            	Process name
            	**type**\:  str
            
            

            """

            _prefix = 'wdsysmon-fd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SystemMonitoring.CpuUtilization.ProcessCpu, self).__init__()

                self.yang_name = "process-cpu"
                self.yang_parent_name = "cpu-utilization"

                self.process_cpu_fifteen_minute = YLeaf(YType.uint32, "process-cpu-fifteen-minute")

                self.process_cpu_five_minute = YLeaf(YType.uint32, "process-cpu-five-minute")

                self.process_cpu_one_minute = YLeaf(YType.uint32, "process-cpu-one-minute")

                self.process_id = YLeaf(YType.uint32, "process-id")

                self.process_name = YLeaf(YType.str, "process-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("process_cpu_fifteen_minute",
                                "process_cpu_five_minute",
                                "process_cpu_one_minute",
                                "process_id",
                                "process_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SystemMonitoring.CpuUtilization.ProcessCpu, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SystemMonitoring.CpuUtilization.ProcessCpu, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.process_cpu_fifteen_minute.is_set or
                    self.process_cpu_five_minute.is_set or
                    self.process_cpu_one_minute.is_set or
                    self.process_id.is_set or
                    self.process_name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.process_cpu_fifteen_minute.yfilter != YFilter.not_set or
                    self.process_cpu_five_minute.yfilter != YFilter.not_set or
                    self.process_cpu_one_minute.yfilter != YFilter.not_set or
                    self.process_id.yfilter != YFilter.not_set or
                    self.process_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "process-cpu" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.process_cpu_fifteen_minute.is_set or self.process_cpu_fifteen_minute.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.process_cpu_fifteen_minute.get_name_leafdata())
                if (self.process_cpu_five_minute.is_set or self.process_cpu_five_minute.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.process_cpu_five_minute.get_name_leafdata())
                if (self.process_cpu_one_minute.is_set or self.process_cpu_one_minute.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.process_cpu_one_minute.get_name_leafdata())
                if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.process_id.get_name_leafdata())
                if (self.process_name.is_set or self.process_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.process_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "process-cpu-fifteen-minute" or name == "process-cpu-five-minute" or name == "process-cpu-one-minute" or name == "process-id" or name == "process-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "process-cpu-fifteen-minute"):
                    self.process_cpu_fifteen_minute = value
                    self.process_cpu_fifteen_minute.value_namespace = name_space
                    self.process_cpu_fifteen_minute.value_namespace_prefix = name_space_prefix
                if(value_path == "process-cpu-five-minute"):
                    self.process_cpu_five_minute = value
                    self.process_cpu_five_minute.value_namespace = name_space
                    self.process_cpu_five_minute.value_namespace_prefix = name_space_prefix
                if(value_path == "process-cpu-one-minute"):
                    self.process_cpu_one_minute = value
                    self.process_cpu_one_minute.value_namespace = name_space
                    self.process_cpu_one_minute.value_namespace_prefix = name_space_prefix
                if(value_path == "process-id"):
                    self.process_id = value
                    self.process_id.value_namespace = name_space
                    self.process_id.value_namespace_prefix = name_space_prefix
                if(value_path == "process-name"):
                    self.process_name = value
                    self.process_name.value_namespace = name_space
                    self.process_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.process_cpu:
                if (c.has_data()):
                    return True
            return (
                self.node_name.is_set or
                self.total_cpu_fifteen_minute.is_set or
                self.total_cpu_five_minute.is_set or
                self.total_cpu_one_minute.is_set)

        def has_operation(self):
            for c in self.process_cpu:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.node_name.yfilter != YFilter.not_set or
                self.total_cpu_fifteen_minute.yfilter != YFilter.not_set or
                self.total_cpu_five_minute.yfilter != YFilter.not_set or
                self.total_cpu_one_minute.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpu-utilization" + "[node-name='" + self.node_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.node_name.get_name_leafdata())
            if (self.total_cpu_fifteen_minute.is_set or self.total_cpu_fifteen_minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.total_cpu_fifteen_minute.get_name_leafdata())
            if (self.total_cpu_five_minute.is_set or self.total_cpu_five_minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.total_cpu_five_minute.get_name_leafdata())
            if (self.total_cpu_one_minute.is_set or self.total_cpu_one_minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.total_cpu_one_minute.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "process-cpu"):
                for c in self.process_cpu:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SystemMonitoring.CpuUtilization.ProcessCpu()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.process_cpu.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "process-cpu" or name == "node-name" or name == "total-cpu-fifteen-minute" or name == "total-cpu-five-minute" or name == "total-cpu-one-minute"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "node-name"):
                self.node_name = value
                self.node_name.value_namespace = name_space
                self.node_name.value_namespace_prefix = name_space_prefix
            if(value_path == "total-cpu-fifteen-minute"):
                self.total_cpu_fifteen_minute = value
                self.total_cpu_fifteen_minute.value_namespace = name_space
                self.total_cpu_fifteen_minute.value_namespace_prefix = name_space_prefix
            if(value_path == "total-cpu-five-minute"):
                self.total_cpu_five_minute = value
                self.total_cpu_five_minute.value_namespace = name_space
                self.total_cpu_five_minute.value_namespace_prefix = name_space_prefix
            if(value_path == "total-cpu-one-minute"):
                self.total_cpu_one_minute = value
                self.total_cpu_one_minute.value_namespace = name_space
                self.total_cpu_one_minute.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.cpu_utilization:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.cpu_utilization:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-wdsysmon-fd-oper:system-monitoring" + path_buffer

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

        if (child_yang_name == "cpu-utilization"):
            for c in self.cpu_utilization:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = SystemMonitoring.CpuUtilization()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.cpu_utilization.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpu-utilization"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SystemMonitoring()
        return self._top_entity

