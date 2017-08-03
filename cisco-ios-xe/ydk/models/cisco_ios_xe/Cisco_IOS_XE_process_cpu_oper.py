""" Cisco_IOS_XE_process_cpu_oper 

This module contains a collection of YANG definitions for
monitoring CPU usage of processes in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CpuUsage(Entity):
    """
    CPU Utilization data
    
    .. attribute:: cpu_utilization
    
    	Data nodes for Total CPU Utilization Statistics
    	**type**\:   :py:class:`CpuUtilization <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization>`
    
    

    """

    _prefix = 'process-cpu-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(CpuUsage, self).__init__()
        self._top_entity = None

        self.yang_name = "cpu-usage"
        self.yang_parent_name = "Cisco-IOS-XE-process-cpu-oper"

        self.cpu_utilization = CpuUsage.CpuUtilization()
        self.cpu_utilization.parent = self
        self._children_name_map["cpu_utilization"] = "cpu-utilization"
        self._children_yang_names.add("cpu-utilization")


    class CpuUtilization(Entity):
        """
        Data nodes for Total CPU Utilization Statistics.
        
        .. attribute:: cpu_usage_processes
        
        	Data nodes for System wide Process CPU usage Statistics
        	**type**\:   :py:class:`CpuUsageProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization.CpuUsageProcesses>`
        
        .. attribute:: five_minutes
        
        	Busy percentage in last five minutes
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: five_seconds
        
        	Busy percentage in last 5\-seconds
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: five_seconds_intr
        
        	Interrupt busy percentage in last 5\-seconds
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        .. attribute:: one_minute
        
        	Busy percentage in last one minute
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: percent
        
        

        """

        _prefix = 'process-cpu-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(CpuUsage.CpuUtilization, self).__init__()

            self.yang_name = "cpu-utilization"
            self.yang_parent_name = "cpu-usage"

            self.five_minutes = YLeaf(YType.uint8, "five-minutes")

            self.five_seconds = YLeaf(YType.uint8, "five-seconds")

            self.five_seconds_intr = YLeaf(YType.uint8, "five-seconds-intr")

            self.one_minute = YLeaf(YType.uint8, "one-minute")

            self.cpu_usage_processes = CpuUsage.CpuUtilization.CpuUsageProcesses()
            self.cpu_usage_processes.parent = self
            self._children_name_map["cpu_usage_processes"] = "cpu-usage-processes"
            self._children_yang_names.add("cpu-usage-processes")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("five_minutes",
                            "five_seconds",
                            "five_seconds_intr",
                            "one_minute") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CpuUsage.CpuUtilization, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CpuUsage.CpuUtilization, self).__setattr__(name, value)


        class CpuUsageProcesses(Entity):
            """
            Data nodes for System wide Process CPU usage Statistics.
            
            .. attribute:: cpu_usage_process
            
            	The list of software processes on the device
            	**type**\: list of    :py:class:`CpuUsageProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper.CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess>`
            
            

            """

            _prefix = 'process-cpu-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(CpuUsage.CpuUtilization.CpuUsageProcesses, self).__init__()

                self.yang_name = "cpu-usage-processes"
                self.yang_parent_name = "cpu-utilization"

                self.cpu_usage_process = YList(self)

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
                            super(CpuUsage.CpuUtilization.CpuUsageProcesses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CpuUsage.CpuUtilization.CpuUsageProcesses, self).__setattr__(name, value)


            class CpuUsageProcess(Entity):
                """
                The list of software processes on the device.
                
                .. attribute:: pid  <key>
                
                	Process\-ID of the process
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name  <key>
                
                	The name of the process
                	**type**\:  str
                
                .. attribute:: avg_run_time
                
                	Average Run\-time of this process (uSec)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: micro-seconds
                
                .. attribute:: five_minutes
                
                	Busy percentage in last five minutes
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: five_seconds
                
                	Busy percentage in last 5\-seconds
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: invocation_count
                
                	Total number of invocations
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: one_minute
                
                	Busy percentage in last one minute
                	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                
                	**range:** \-92233720368547758.08..92233720368547758.07
                
                	**units**\: percent
                
                .. attribute:: total_run_time
                
                	Total Run\-time of this process (mSec)
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: milli-seconds
                
                .. attribute:: tty
                
                	TTY bound to by the process
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'process-cpu-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess, self).__init__()

                    self.yang_name = "cpu-usage-process"
                    self.yang_parent_name = "cpu-usage-processes"

                    self.pid = YLeaf(YType.uint32, "pid")

                    self.name = YLeaf(YType.str, "name")

                    self.avg_run_time = YLeaf(YType.uint64, "avg-run-time")

                    self.five_minutes = YLeaf(YType.str, "five-minutes")

                    self.five_seconds = YLeaf(YType.str, "five-seconds")

                    self.invocation_count = YLeaf(YType.uint32, "invocation-count")

                    self.one_minute = YLeaf(YType.str, "one-minute")

                    self.total_run_time = YLeaf(YType.uint64, "total-run-time")

                    self.tty = YLeaf(YType.uint16, "tty")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("pid",
                                    "name",
                                    "avg_run_time",
                                    "five_minutes",
                                    "five_seconds",
                                    "invocation_count",
                                    "one_minute",
                                    "total_run_time",
                                    "tty") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.pid.is_set or
                        self.name.is_set or
                        self.avg_run_time.is_set or
                        self.five_minutes.is_set or
                        self.five_seconds.is_set or
                        self.invocation_count.is_set or
                        self.one_minute.is_set or
                        self.total_run_time.is_set or
                        self.tty.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.pid.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.avg_run_time.yfilter != YFilter.not_set or
                        self.five_minutes.yfilter != YFilter.not_set or
                        self.five_seconds.yfilter != YFilter.not_set or
                        self.invocation_count.yfilter != YFilter.not_set or
                        self.one_minute.yfilter != YFilter.not_set or
                        self.total_run_time.yfilter != YFilter.not_set or
                        self.tty.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "cpu-usage-process" + "[pid='" + self.pid.get() + "']" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/cpu-usage-processes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pid.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.avg_run_time.is_set or self.avg_run_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.avg_run_time.get_name_leafdata())
                    if (self.five_minutes.is_set or self.five_minutes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.five_minutes.get_name_leafdata())
                    if (self.five_seconds.is_set or self.five_seconds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.five_seconds.get_name_leafdata())
                    if (self.invocation_count.is_set or self.invocation_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.invocation_count.get_name_leafdata())
                    if (self.one_minute.is_set or self.one_minute.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.one_minute.get_name_leafdata())
                    if (self.total_run_time.is_set or self.total_run_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_run_time.get_name_leafdata())
                    if (self.tty.is_set or self.tty.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tty.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pid" or name == "name" or name == "avg-run-time" or name == "five-minutes" or name == "five-seconds" or name == "invocation-count" or name == "one-minute" or name == "total-run-time" or name == "tty"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "pid"):
                        self.pid = value
                        self.pid.value_namespace = name_space
                        self.pid.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "avg-run-time"):
                        self.avg_run_time = value
                        self.avg_run_time.value_namespace = name_space
                        self.avg_run_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "five-minutes"):
                        self.five_minutes = value
                        self.five_minutes.value_namespace = name_space
                        self.five_minutes.value_namespace_prefix = name_space_prefix
                    if(value_path == "five-seconds"):
                        self.five_seconds = value
                        self.five_seconds.value_namespace = name_space
                        self.five_seconds.value_namespace_prefix = name_space_prefix
                    if(value_path == "invocation-count"):
                        self.invocation_count = value
                        self.invocation_count.value_namespace = name_space
                        self.invocation_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "one-minute"):
                        self.one_minute = value
                        self.one_minute.value_namespace = name_space
                        self.one_minute.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-run-time"):
                        self.total_run_time = value
                        self.total_run_time.value_namespace = name_space
                        self.total_run_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "tty"):
                        self.tty = value
                        self.tty.value_namespace = name_space
                        self.tty.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.cpu_usage_process:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.cpu_usage_process:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpu-usage-processes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-process-cpu-oper:cpu-usage/cpu-utilization/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "cpu-usage-process"):
                    for c in self.cpu_usage_process:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.cpu_usage_process.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpu-usage-process"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.five_minutes.is_set or
                self.five_seconds.is_set or
                self.five_seconds_intr.is_set or
                self.one_minute.is_set or
                (self.cpu_usage_processes is not None and self.cpu_usage_processes.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.five_minutes.yfilter != YFilter.not_set or
                self.five_seconds.yfilter != YFilter.not_set or
                self.five_seconds_intr.yfilter != YFilter.not_set or
                self.one_minute.yfilter != YFilter.not_set or
                (self.cpu_usage_processes is not None and self.cpu_usage_processes.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpu-utilization" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-process-cpu-oper:cpu-usage/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.five_minutes.is_set or self.five_minutes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.five_minutes.get_name_leafdata())
            if (self.five_seconds.is_set or self.five_seconds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.five_seconds.get_name_leafdata())
            if (self.five_seconds_intr.is_set or self.five_seconds_intr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.five_seconds_intr.get_name_leafdata())
            if (self.one_minute.is_set or self.one_minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.one_minute.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpu-usage-processes"):
                if (self.cpu_usage_processes is None):
                    self.cpu_usage_processes = CpuUsage.CpuUtilization.CpuUsageProcesses()
                    self.cpu_usage_processes.parent = self
                    self._children_name_map["cpu_usage_processes"] = "cpu-usage-processes"
                return self.cpu_usage_processes

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpu-usage-processes" or name == "five-minutes" or name == "five-seconds" or name == "five-seconds-intr" or name == "one-minute"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "five-minutes"):
                self.five_minutes = value
                self.five_minutes.value_namespace = name_space
                self.five_minutes.value_namespace_prefix = name_space_prefix
            if(value_path == "five-seconds"):
                self.five_seconds = value
                self.five_seconds.value_namespace = name_space
                self.five_seconds.value_namespace_prefix = name_space_prefix
            if(value_path == "five-seconds-intr"):
                self.five_seconds_intr = value
                self.five_seconds_intr.value_namespace = name_space
                self.five_seconds_intr.value_namespace_prefix = name_space_prefix
            if(value_path == "one-minute"):
                self.one_minute = value
                self.one_minute.value_namespace = name_space
                self.one_minute.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.cpu_utilization is not None and self.cpu_utilization.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpu_utilization is not None and self.cpu_utilization.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-process-cpu-oper:cpu-usage" + path_buffer

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
            if (self.cpu_utilization is None):
                self.cpu_utilization = CpuUsage.CpuUtilization()
                self.cpu_utilization.parent = self
                self._children_name_map["cpu_utilization"] = "cpu-utilization"
            return self.cpu_utilization

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpu-utilization"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CpuUsage()
        return self._top_entity

