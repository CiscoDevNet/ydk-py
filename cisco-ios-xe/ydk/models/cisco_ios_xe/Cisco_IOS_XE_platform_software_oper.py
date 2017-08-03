""" Cisco_IOS_XE_platform_software_oper 

This module contains a collection of YANG definitions
for monitoring platform software in a Network Element

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BFru(Enum):
    """
    BFru

    FRU type

    .. data:: platform_fru_rp = 0

    .. data:: platform_fru_fp = 1

    .. data:: platform_fru_cc = 2

    .. data:: platform_fru_max = 3

    """

    platform_fru_rp = Enum.YLeaf(0, "platform-fru-rp")

    platform_fru_fp = Enum.YLeaf(1, "platform-fru-fp")

    platform_fru_cc = Enum.YLeaf(2, "platform-fru-cc")

    platform_fru_max = Enum.YLeaf(3, "platform-fru-max")



class CiscoPlatformSoftware(Entity):
    """
    Cisco platform software information
    
    .. attribute:: control_processes
    
    	Information about control processes
    	**type**\:   :py:class:`ControlProcesses <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses>`
    
    

    """

    _prefix = 'platform-sw-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(CiscoPlatformSoftware, self).__init__()
        self._top_entity = None

        self.yang_name = "cisco-platform-software"
        self.yang_parent_name = "Cisco-IOS-XE-platform-software-oper"

        self.control_processes = CiscoPlatformSoftware.ControlProcesses()
        self.control_processes.parent = self
        self._children_name_map["control_processes"] = "control-processes"
        self._children_yang_names.add("control-processes")


    class ControlProcesses(Entity):
        """
        Information about control processes
        
        .. attribute:: control_process
        
        	The list of control processes
        	**type**\: list of    :py:class:`ControlProcess <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess>`
        
        

        """

        _prefix = 'platform-sw-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(CiscoPlatformSoftware.ControlProcesses, self).__init__()

            self.yang_name = "control-processes"
            self.yang_parent_name = "cisco-platform-software"

            self.control_process = YList(self)

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
                        super(CiscoPlatformSoftware.ControlProcesses, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoPlatformSoftware.ControlProcesses, self).__setattr__(name, value)


        class ControlProcess(Entity):
            """
            The list of control processes
            
            .. attribute:: fru  <key>
            
            	Field replaceable unit
            	**type**\:   :py:class:`BFru <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.BFru>`
            
            .. attribute:: slotnum  <key>
            
            	Slot number
            	**type**\:  int
            
            	**range:** \-32768..32767
            
            .. attribute:: baynum  <key>
            
            	Bay number
            	**type**\:  int
            
            	**range:** \-32768..32767
            
            .. attribute:: chassisnum  <key>
            
            	Chassis number
            	**type**\:  int
            
            	**range:** \-32768..32767
            
            .. attribute:: control_process_status
            
            	Status of the control process
            	**type**\:  str
            
            .. attribute:: load_average_stats
            
            	Load average statictics
            	**type**\:   :py:class:`LoadAverageStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats>`
            
            .. attribute:: load_avg_minutes
            
            	Load average statistics calculated over a period of time
            	**type**\:   :py:class:`LoadAvgMinutes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes>`
            
            .. attribute:: memory_stats
            
            	Memory statistics
            	**type**\:   :py:class:`MemoryStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats>`
            
            .. attribute:: per_core_stats
            
            	Processor core statistics
            	**type**\:   :py:class:`PerCoreStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats>`
            
            .. attribute:: updated
            
            	Number of seconds since the data has been updated
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'platform-sw-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess, self).__init__()

                self.yang_name = "control-process"
                self.yang_parent_name = "control-processes"

                self.fru = YLeaf(YType.enumeration, "fru")

                self.slotnum = YLeaf(YType.int16, "slotnum")

                self.baynum = YLeaf(YType.int16, "baynum")

                self.chassisnum = YLeaf(YType.int16, "chassisnum")

                self.control_process_status = YLeaf(YType.str, "control-process-status")

                self.updated = YLeaf(YType.uint64, "updated")

                self.load_average_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats()
                self.load_average_stats.parent = self
                self._children_name_map["load_average_stats"] = "load-average-stats"
                self._children_yang_names.add("load-average-stats")

                self.load_avg_minutes = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes()
                self.load_avg_minutes.parent = self
                self._children_name_map["load_avg_minutes"] = "load-avg-minutes"
                self._children_yang_names.add("load-avg-minutes")

                self.memory_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats()
                self.memory_stats.parent = self
                self._children_name_map["memory_stats"] = "memory-stats"
                self._children_yang_names.add("memory-stats")

                self.per_core_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats()
                self.per_core_stats.parent = self
                self._children_name_map["per_core_stats"] = "per-core-stats"
                self._children_yang_names.add("per-core-stats")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("fru",
                                "slotnum",
                                "baynum",
                                "chassisnum",
                                "control_process_status",
                                "updated") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess, self).__setattr__(name, value)


            class LoadAverageStats(Entity):
                """
                Load average statictics
                
                .. attribute:: load_average_status
                
                	Load average status
                	**type**\:  str
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, self).__init__()

                    self.yang_name = "load-average-stats"
                    self.yang_parent_name = "control-process"

                    self.load_average_status = YLeaf(YType.str, "load-average-status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("load_average_status") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats, self).__setattr__(name, value)

                def has_data(self):
                    return self.load_average_status.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.load_average_status.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "load-average-stats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.load_average_status.is_set or self.load_average_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.load_average_status.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "load-average-status"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "load-average-status"):
                        self.load_average_status = value
                        self.load_average_status.value_namespace = name_space
                        self.load_average_status.value_namespace_prefix = name_space_prefix


            class LoadAvgMinutes(Entity):
                """
                Load average statistics calculated over a period of time
                
                .. attribute:: load_avg_minute
                
                	List of Load averages based on a time frame
                	**type**\: list of    :py:class:`LoadAvgMinute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute>`
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, self).__init__()

                    self.yang_name = "load-avg-minutes"
                    self.yang_parent_name = "control-process"

                    self.load_avg_minute = YList(self)

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
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes, self).__setattr__(name, value)


                class LoadAvgMinute(Entity):
                    """
                    List of Load averages based on a time frame
                    
                    .. attribute:: number  <key>
                    
                    	The number of minutes the average was calculated on
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: average
                    
                    	Calculated average
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: status
                    
                    	Load average statistics minute status
                    	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status>`
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, self).__init__()

                        self.yang_name = "load-avg-minute"
                        self.yang_parent_name = "load-avg-minutes"

                        self.number = YLeaf(YType.uint64, "number")

                        self.average = YLeaf(YType.str, "average")

                        self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status()
                        self.status.parent = self
                        self._children_name_map["status"] = "status"
                        self._children_yang_names.add("status")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("number",
                                        "average") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute, self).__setattr__(name, value)


                    class Status(Entity):
                        """
                        Load average statistics minute status
                        
                        .. attribute:: condition
                        
                        	Load average condition
                        	**type**\:  str
                        
                        .. attribute:: threshold_status
                        
                        	Load average status
                        	**type**\:  str
                        
                        .. attribute:: threshold_value
                        
                        	Load average threshold
                        	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        

                        """

                        _prefix = 'platform-sw-ios-xe-oper'
                        _revision = '2017-04-01'

                        def __init__(self):
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, self).__init__()

                            self.yang_name = "status"
                            self.yang_parent_name = "load-avg-minute"

                            self.condition = YLeaf(YType.str, "condition")

                            self.threshold_status = YLeaf(YType.str, "threshold-status")

                            self.threshold_value = YLeaf(YType.str, "threshold-value")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("condition",
                                            "threshold_status",
                                            "threshold_value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.condition.is_set or
                                self.threshold_status.is_set or
                                self.threshold_value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.condition.yfilter != YFilter.not_set or
                                self.threshold_status.yfilter != YFilter.not_set or
                                self.threshold_value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "status" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.condition.is_set or self.condition.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.condition.get_name_leafdata())
                            if (self.threshold_status.is_set or self.threshold_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_status.get_name_leafdata())
                            if (self.threshold_value.is_set or self.threshold_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.threshold_value.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "condition" or name == "threshold-status" or name == "threshold-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "condition"):
                                self.condition = value
                                self.condition.value_namespace = name_space
                                self.condition.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-status"):
                                self.threshold_status = value
                                self.threshold_status.value_namespace = name_space
                                self.threshold_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "threshold-value"):
                                self.threshold_value = value
                                self.threshold_value.value_namespace = name_space
                                self.threshold_value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.number.is_set or
                            self.average.is_set or
                            (self.status is not None and self.status.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.number.yfilter != YFilter.not_set or
                            self.average.yfilter != YFilter.not_set or
                            (self.status is not None and self.status.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "load-avg-minute" + "[number='" + self.number.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.number.get_name_leafdata())
                        if (self.average.is_set or self.average.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.average.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "status"):
                            if (self.status is None):
                                self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status()
                                self.status.parent = self
                                self._children_name_map["status"] = "status"
                            return self.status

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "status" or name == "number" or name == "average"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "number"):
                            self.number = value
                            self.number.value_namespace = name_space
                            self.number.value_namespace_prefix = name_space_prefix
                        if(value_path == "average"):
                            self.average = value
                            self.average.value_namespace = name_space
                            self.average.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.load_avg_minute:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.load_avg_minute:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "load-avg-minutes" + path_buffer

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

                    if (child_yang_name == "load-avg-minute"):
                        for c in self.load_avg_minute:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.load_avg_minute.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "load-avg-minute"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class MemoryStats(Entity):
                """
                Memory statistics
                
                .. attribute:: available_number
                
                	The amount of available memory in kb
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: available_percent
                
                	The percentage of available memory
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: committed_number
                
                	The amount of committed memory in kb
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: committed_percent
                
                	The percentage of committed memory
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: free_number
                
                	The amount of free memory in kb
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: free_percent
                
                	The percentage of free memory
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_status
                
                	The status of the memory
                	**type**\:  str
                
                .. attribute:: status
                
                	Memory status
                	**type**\:   :py:class:`Status <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status>`
                
                .. attribute:: total
                
                	The total amount of memory in kb
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: used_number
                
                	The amount of memory being used in kb
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: used_percent
                
                	The percentage of memory being used
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, self).__init__()

                    self.yang_name = "memory-stats"
                    self.yang_parent_name = "control-process"

                    self.available_number = YLeaf(YType.uint64, "available-number")

                    self.available_percent = YLeaf(YType.uint64, "available-percent")

                    self.committed_number = YLeaf(YType.uint64, "committed-number")

                    self.committed_percent = YLeaf(YType.uint8, "committed-percent")

                    self.free_number = YLeaf(YType.uint64, "free-number")

                    self.free_percent = YLeaf(YType.uint64, "free-percent")

                    self.memory_status = YLeaf(YType.str, "memory-status")

                    self.total = YLeaf(YType.uint64, "total")

                    self.used_number = YLeaf(YType.uint64, "used-number")

                    self.used_percent = YLeaf(YType.uint64, "used-percent")

                    self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status()
                    self.status.parent = self
                    self._children_name_map["status"] = "status"
                    self._children_yang_names.add("status")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("available_number",
                                    "available_percent",
                                    "committed_number",
                                    "committed_percent",
                                    "free_number",
                                    "free_percent",
                                    "memory_status",
                                    "total",
                                    "used_number",
                                    "used_percent") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats, self).__setattr__(name, value)


                class Status(Entity):
                    """
                    Memory status
                    
                    .. attribute:: critical_threshold_percent
                    
                    	Memory critical threshold value percent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: warning_threshold_percent
                    
                    	Memory warning threshold value percent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, self).__init__()

                        self.yang_name = "status"
                        self.yang_parent_name = "memory-stats"

                        self.critical_threshold_percent = YLeaf(YType.uint32, "critical-threshold-percent")

                        self.warning_threshold_percent = YLeaf(YType.uint32, "warning-threshold-percent")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("critical_threshold_percent",
                                        "warning_threshold_percent") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.critical_threshold_percent.is_set or
                            self.warning_threshold_percent.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.critical_threshold_percent.yfilter != YFilter.not_set or
                            self.warning_threshold_percent.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "status" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.critical_threshold_percent.is_set or self.critical_threshold_percent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.critical_threshold_percent.get_name_leafdata())
                        if (self.warning_threshold_percent.is_set or self.warning_threshold_percent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.warning_threshold_percent.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "critical-threshold-percent" or name == "warning-threshold-percent"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "critical-threshold-percent"):
                            self.critical_threshold_percent = value
                            self.critical_threshold_percent.value_namespace = name_space
                            self.critical_threshold_percent.value_namespace_prefix = name_space_prefix
                        if(value_path == "warning-threshold-percent"):
                            self.warning_threshold_percent = value
                            self.warning_threshold_percent.value_namespace = name_space
                            self.warning_threshold_percent.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.available_number.is_set or
                        self.available_percent.is_set or
                        self.committed_number.is_set or
                        self.committed_percent.is_set or
                        self.free_number.is_set or
                        self.free_percent.is_set or
                        self.memory_status.is_set or
                        self.total.is_set or
                        self.used_number.is_set or
                        self.used_percent.is_set or
                        (self.status is not None and self.status.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.available_number.yfilter != YFilter.not_set or
                        self.available_percent.yfilter != YFilter.not_set or
                        self.committed_number.yfilter != YFilter.not_set or
                        self.committed_percent.yfilter != YFilter.not_set or
                        self.free_number.yfilter != YFilter.not_set or
                        self.free_percent.yfilter != YFilter.not_set or
                        self.memory_status.yfilter != YFilter.not_set or
                        self.total.yfilter != YFilter.not_set or
                        self.used_number.yfilter != YFilter.not_set or
                        self.used_percent.yfilter != YFilter.not_set or
                        (self.status is not None and self.status.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "memory-stats" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.available_number.is_set or self.available_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.available_number.get_name_leafdata())
                    if (self.available_percent.is_set or self.available_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.available_percent.get_name_leafdata())
                    if (self.committed_number.is_set or self.committed_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.committed_number.get_name_leafdata())
                    if (self.committed_percent.is_set or self.committed_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.committed_percent.get_name_leafdata())
                    if (self.free_number.is_set or self.free_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_number.get_name_leafdata())
                    if (self.free_percent.is_set or self.free_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.free_percent.get_name_leafdata())
                    if (self.memory_status.is_set or self.memory_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_status.get_name_leafdata())
                    if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total.get_name_leafdata())
                    if (self.used_number.is_set or self.used_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.used_number.get_name_leafdata())
                    if (self.used_percent.is_set or self.used_percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.used_percent.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "status"):
                        if (self.status is None):
                            self.status = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats.Status()
                            self.status.parent = self
                            self._children_name_map["status"] = "status"
                        return self.status

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "status" or name == "available-number" or name == "available-percent" or name == "committed-number" or name == "committed-percent" or name == "free-number" or name == "free-percent" or name == "memory-status" or name == "total" or name == "used-number" or name == "used-percent"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "available-number"):
                        self.available_number = value
                        self.available_number.value_namespace = name_space
                        self.available_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "available-percent"):
                        self.available_percent = value
                        self.available_percent.value_namespace = name_space
                        self.available_percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "committed-number"):
                        self.committed_number = value
                        self.committed_number.value_namespace = name_space
                        self.committed_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "committed-percent"):
                        self.committed_percent = value
                        self.committed_percent.value_namespace = name_space
                        self.committed_percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "free-number"):
                        self.free_number = value
                        self.free_number.value_namespace = name_space
                        self.free_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "free-percent"):
                        self.free_percent = value
                        self.free_percent.value_namespace = name_space
                        self.free_percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "memory-status"):
                        self.memory_status = value
                        self.memory_status.value_namespace = name_space
                        self.memory_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "total"):
                        self.total = value
                        self.total.value_namespace = name_space
                        self.total.value_namespace_prefix = name_space_prefix
                    if(value_path == "used-number"):
                        self.used_number = value
                        self.used_number.value_namespace = name_space
                        self.used_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "used-percent"):
                        self.used_percent = value
                        self.used_percent.value_namespace = name_space
                        self.used_percent.value_namespace_prefix = name_space_prefix


            class PerCoreStats(Entity):
                """
                Processor core statistics
                
                .. attribute:: per_core_stat
                
                	List of processor cores
                	**type**\: list of    :py:class:`PerCoreStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper.CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat>`
                
                

                """

                _prefix = 'platform-sw-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, self).__init__()

                    self.yang_name = "per-core-stats"
                    self.yang_parent_name = "control-process"

                    self.per_core_stat = YList(self)

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
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats, self).__setattr__(name, value)


                class PerCoreStat(Entity):
                    """
                    List of processor cores
                    
                    .. attribute:: name  <key>
                    
                    	The identifier of the core
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: idle
                    
                    	Idle percentage
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: io_wait
                    
                    	IOWait percentage
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: irq
                    
                    	The percentage of utilization by irq
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: nice
                    
                    	Nice level
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: sirq
                    
                    	The percentage of utilization by sirq
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: system
                    
                    	CPU utilization in system mode
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    .. attribute:: user
                    
                    	CPU utilization in user mode
                    	**type**\:  :py:class:`Decimal64<ydk.types.Decimal64>`
                    
                    	**range:** \-92233720368547758.08..92233720368547758.07
                    
                    

                    """

                    _prefix = 'platform-sw-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, self).__init__()

                        self.yang_name = "per-core-stat"
                        self.yang_parent_name = "per-core-stats"

                        self.name = YLeaf(YType.uint32, "name")

                        self.idle = YLeaf(YType.str, "idle")

                        self.io_wait = YLeaf(YType.str, "io-wait")

                        self.irq = YLeaf(YType.str, "irq")

                        self.nice = YLeaf(YType.str, "nice")

                        self.sirq = YLeaf(YType.str, "sirq")

                        self.system = YLeaf(YType.str, "system")

                        self.user = YLeaf(YType.str, "user")

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
                                        "idle",
                                        "io_wait",
                                        "irq",
                                        "nice",
                                        "sirq",
                                        "system",
                                        "user") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.idle.is_set or
                            self.io_wait.is_set or
                            self.irq.is_set or
                            self.nice.is_set or
                            self.sirq.is_set or
                            self.system.is_set or
                            self.user.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.idle.yfilter != YFilter.not_set or
                            self.io_wait.yfilter != YFilter.not_set or
                            self.irq.yfilter != YFilter.not_set or
                            self.nice.yfilter != YFilter.not_set or
                            self.sirq.yfilter != YFilter.not_set or
                            self.system.yfilter != YFilter.not_set or
                            self.user.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "per-core-stat" + "[name='" + self.name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.idle.is_set or self.idle.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.idle.get_name_leafdata())
                        if (self.io_wait.is_set or self.io_wait.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.io_wait.get_name_leafdata())
                        if (self.irq.is_set or self.irq.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.irq.get_name_leafdata())
                        if (self.nice.is_set or self.nice.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nice.get_name_leafdata())
                        if (self.sirq.is_set or self.sirq.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sirq.get_name_leafdata())
                        if (self.system.is_set or self.system.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.system.get_name_leafdata())
                        if (self.user.is_set or self.user.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.user.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "name" or name == "idle" or name == "io-wait" or name == "irq" or name == "nice" or name == "sirq" or name == "system" or name == "user"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "idle"):
                            self.idle = value
                            self.idle.value_namespace = name_space
                            self.idle.value_namespace_prefix = name_space_prefix
                        if(value_path == "io-wait"):
                            self.io_wait = value
                            self.io_wait.value_namespace = name_space
                            self.io_wait.value_namespace_prefix = name_space_prefix
                        if(value_path == "irq"):
                            self.irq = value
                            self.irq.value_namespace = name_space
                            self.irq.value_namespace_prefix = name_space_prefix
                        if(value_path == "nice"):
                            self.nice = value
                            self.nice.value_namespace = name_space
                            self.nice.value_namespace_prefix = name_space_prefix
                        if(value_path == "sirq"):
                            self.sirq = value
                            self.sirq.value_namespace = name_space
                            self.sirq.value_namespace_prefix = name_space_prefix
                        if(value_path == "system"):
                            self.system = value
                            self.system.value_namespace = name_space
                            self.system.value_namespace_prefix = name_space_prefix
                        if(value_path == "user"):
                            self.user = value
                            self.user.value_namespace = name_space
                            self.user.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.per_core_stat:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.per_core_stat:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "per-core-stats" + path_buffer

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

                    if (child_yang_name == "per-core-stat"):
                        for c in self.per_core_stat:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.per_core_stat.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "per-core-stat"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.fru.is_set or
                    self.slotnum.is_set or
                    self.baynum.is_set or
                    self.chassisnum.is_set or
                    self.control_process_status.is_set or
                    self.updated.is_set or
                    (self.load_average_stats is not None and self.load_average_stats.has_data()) or
                    (self.load_avg_minutes is not None and self.load_avg_minutes.has_data()) or
                    (self.memory_stats is not None and self.memory_stats.has_data()) or
                    (self.per_core_stats is not None and self.per_core_stats.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.fru.yfilter != YFilter.not_set or
                    self.slotnum.yfilter != YFilter.not_set or
                    self.baynum.yfilter != YFilter.not_set or
                    self.chassisnum.yfilter != YFilter.not_set or
                    self.control_process_status.yfilter != YFilter.not_set or
                    self.updated.yfilter != YFilter.not_set or
                    (self.load_average_stats is not None and self.load_average_stats.has_operation()) or
                    (self.load_avg_minutes is not None and self.load_avg_minutes.has_operation()) or
                    (self.memory_stats is not None and self.memory_stats.has_operation()) or
                    (self.per_core_stats is not None and self.per_core_stats.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "control-process" + "[fru='" + self.fru.get() + "']" + "[slotnum='" + self.slotnum.get() + "']" + "[baynum='" + self.baynum.get() + "']" + "[chassisnum='" + self.chassisnum.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/control-processes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.fru.is_set or self.fru.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.fru.get_name_leafdata())
                if (self.slotnum.is_set or self.slotnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.slotnum.get_name_leafdata())
                if (self.baynum.is_set or self.baynum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.baynum.get_name_leafdata())
                if (self.chassisnum.is_set or self.chassisnum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chassisnum.get_name_leafdata())
                if (self.control_process_status.is_set or self.control_process_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.control_process_status.get_name_leafdata())
                if (self.updated.is_set or self.updated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.updated.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "load-average-stats"):
                    if (self.load_average_stats is None):
                        self.load_average_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAverageStats()
                        self.load_average_stats.parent = self
                        self._children_name_map["load_average_stats"] = "load-average-stats"
                    return self.load_average_stats

                if (child_yang_name == "load-avg-minutes"):
                    if (self.load_avg_minutes is None):
                        self.load_avg_minutes = CiscoPlatformSoftware.ControlProcesses.ControlProcess.LoadAvgMinutes()
                        self.load_avg_minutes.parent = self
                        self._children_name_map["load_avg_minutes"] = "load-avg-minutes"
                    return self.load_avg_minutes

                if (child_yang_name == "memory-stats"):
                    if (self.memory_stats is None):
                        self.memory_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.MemoryStats()
                        self.memory_stats.parent = self
                        self._children_name_map["memory_stats"] = "memory-stats"
                    return self.memory_stats

                if (child_yang_name == "per-core-stats"):
                    if (self.per_core_stats is None):
                        self.per_core_stats = CiscoPlatformSoftware.ControlProcesses.ControlProcess.PerCoreStats()
                        self.per_core_stats.parent = self
                        self._children_name_map["per_core_stats"] = "per-core-stats"
                    return self.per_core_stats

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "load-average-stats" or name == "load-avg-minutes" or name == "memory-stats" or name == "per-core-stats" or name == "fru" or name == "slotnum" or name == "baynum" or name == "chassisnum" or name == "control-process-status" or name == "updated"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "fru"):
                    self.fru = value
                    self.fru.value_namespace = name_space
                    self.fru.value_namespace_prefix = name_space_prefix
                if(value_path == "slotnum"):
                    self.slotnum = value
                    self.slotnum.value_namespace = name_space
                    self.slotnum.value_namespace_prefix = name_space_prefix
                if(value_path == "baynum"):
                    self.baynum = value
                    self.baynum.value_namespace = name_space
                    self.baynum.value_namespace_prefix = name_space_prefix
                if(value_path == "chassisnum"):
                    self.chassisnum = value
                    self.chassisnum.value_namespace = name_space
                    self.chassisnum.value_namespace_prefix = name_space_prefix
                if(value_path == "control-process-status"):
                    self.control_process_status = value
                    self.control_process_status.value_namespace = name_space
                    self.control_process_status.value_namespace_prefix = name_space_prefix
                if(value_path == "updated"):
                    self.updated = value
                    self.updated.value_namespace = name_space
                    self.updated.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.control_process:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.control_process:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "control-processes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-platform-software-oper:cisco-platform-software/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "control-process"):
                for c in self.control_process:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoPlatformSoftware.ControlProcesses.ControlProcess()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.control_process.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "control-process"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.control_processes is not None and self.control_processes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.control_processes is not None and self.control_processes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-platform-software-oper:cisco-platform-software" + path_buffer

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

        if (child_yang_name == "control-processes"):
            if (self.control_processes is None):
                self.control_processes = CiscoPlatformSoftware.ControlProcesses()
                self.control_processes.parent = self
                self._children_name_map["control_processes"] = "control-processes"
            return self.control_processes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "control-processes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoPlatformSoftware()
        return self._top_entity

