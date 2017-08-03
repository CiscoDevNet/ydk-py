""" Cisco_IOS_XR_infra_alarm_logger_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-alarm\-logger package operational data.

This module contains definitions
for the following management objects\:
  alarm\-logger\: Alarm Logger operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AlAlarmBistate(Enum):
    """
    AlAlarmBistate

    Al alarm bistate

    .. data:: not_available = 0

    	not available

    .. data:: active = 1

    	active

    .. data:: clear = 2

    	clear

    """

    not_available = Enum.YLeaf(0, "not-available")

    active = Enum.YLeaf(1, "active")

    clear = Enum.YLeaf(2, "clear")


class AlAlarmSeverity(Enum):
    """
    AlAlarmSeverity

    Al alarm severity

    .. data:: unknown = -1

    	unknown

    .. data:: emergency = 0

    	emergency

    .. data:: alert = 1

    	alert

    .. data:: critical = 2

    	critical

    .. data:: error = 3

    	error

    .. data:: warning = 4

    	warning

    .. data:: notice = 5

    	notice

    .. data:: informational = 6

    	informational

    .. data:: debugging = 7

    	debugging

    """

    unknown = Enum.YLeaf(-1, "unknown")

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    informational = Enum.YLeaf(6, "informational")

    debugging = Enum.YLeaf(7, "debugging")



class AlarmLogger(Entity):
    """
    Alarm Logger operational data
    
    .. attribute:: alarms
    
    	Table that contains the database of logged alarms
    	**type**\:   :py:class:`Alarms <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.Alarms>`
    
    .. attribute:: buffer_status
    
    	Describes buffer utilization and parameters configured
    	**type**\:   :py:class:`BufferStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.BufferStatus>`
    
    

    """

    _prefix = 'infra-alarm-logger-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(AlarmLogger, self).__init__()
        self._top_entity = None

        self.yang_name = "alarm-logger"
        self.yang_parent_name = "Cisco-IOS-XR-infra-alarm-logger-oper"

        self.alarms = AlarmLogger.Alarms()
        self.alarms.parent = self
        self._children_name_map["alarms"] = "alarms"
        self._children_yang_names.add("alarms")

        self.buffer_status = AlarmLogger.BufferStatus()
        self.buffer_status.parent = self
        self._children_name_map["buffer_status"] = "buffer-status"
        self._children_yang_names.add("buffer-status")


    class BufferStatus(Entity):
        """
        Describes buffer utilization and parameters
        configured
        
        .. attribute:: capacity_threshold
        
        	Percentage of the buffer utilization which, when exceeded, triggers the  generation of a notification for the clients of the XML agent
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: percentage
        
        .. attribute:: log_buffer_size
        
        	Current Logging Buffer Size (Bytes)
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: byte
        
        .. attribute:: max_log_buffer_size
        
        	Maximum Logging Buffer Size (Bytes) 
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: byte
        
        .. attribute:: record_count
        
        	Number of Records in the Buffer
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: severity_filter
        
        	Severity Filter
        	**type**\:   :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmSeverity>`
        
        

        """

        _prefix = 'infra-alarm-logger-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(AlarmLogger.BufferStatus, self).__init__()

            self.yang_name = "buffer-status"
            self.yang_parent_name = "alarm-logger"

            self.capacity_threshold = YLeaf(YType.uint32, "capacity-threshold")

            self.log_buffer_size = YLeaf(YType.uint32, "log-buffer-size")

            self.max_log_buffer_size = YLeaf(YType.uint32, "max-log-buffer-size")

            self.record_count = YLeaf(YType.uint32, "record-count")

            self.severity_filter = YLeaf(YType.enumeration, "severity-filter")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("capacity_threshold",
                            "log_buffer_size",
                            "max_log_buffer_size",
                            "record_count",
                            "severity_filter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(AlarmLogger.BufferStatus, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AlarmLogger.BufferStatus, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.capacity_threshold.is_set or
                self.log_buffer_size.is_set or
                self.max_log_buffer_size.is_set or
                self.record_count.is_set or
                self.severity_filter.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.capacity_threshold.yfilter != YFilter.not_set or
                self.log_buffer_size.yfilter != YFilter.not_set or
                self.max_log_buffer_size.yfilter != YFilter.not_set or
                self.record_count.yfilter != YFilter.not_set or
                self.severity_filter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "buffer-status" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.capacity_threshold.is_set or self.capacity_threshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.capacity_threshold.get_name_leafdata())
            if (self.log_buffer_size.is_set or self.log_buffer_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.log_buffer_size.get_name_leafdata())
            if (self.max_log_buffer_size.is_set or self.max_log_buffer_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_log_buffer_size.get_name_leafdata())
            if (self.record_count.is_set or self.record_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.record_count.get_name_leafdata())
            if (self.severity_filter.is_set or self.severity_filter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.severity_filter.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "capacity-threshold" or name == "log-buffer-size" or name == "max-log-buffer-size" or name == "record-count" or name == "severity-filter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "capacity-threshold"):
                self.capacity_threshold = value
                self.capacity_threshold.value_namespace = name_space
                self.capacity_threshold.value_namespace_prefix = name_space_prefix
            if(value_path == "log-buffer-size"):
                self.log_buffer_size = value
                self.log_buffer_size.value_namespace = name_space
                self.log_buffer_size.value_namespace_prefix = name_space_prefix
            if(value_path == "max-log-buffer-size"):
                self.max_log_buffer_size = value
                self.max_log_buffer_size.value_namespace = name_space
                self.max_log_buffer_size.value_namespace_prefix = name_space_prefix
            if(value_path == "record-count"):
                self.record_count = value
                self.record_count.value_namespace = name_space
                self.record_count.value_namespace_prefix = name_space_prefix
            if(value_path == "severity-filter"):
                self.severity_filter = value
                self.severity_filter.value_namespace = name_space
                self.severity_filter.value_namespace_prefix = name_space_prefix


    class Alarms(Entity):
        """
        Table that contains the database of logged
        alarms
        
        .. attribute:: alarm
        
        	One of the logged alarms
        	**type**\: list of    :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlarmLogger.Alarms.Alarm>`
        
        

        """

        _prefix = 'infra-alarm-logger-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(AlarmLogger.Alarms, self).__init__()

            self.yang_name = "alarms"
            self.yang_parent_name = "alarm-logger"

            self.alarm = YList(self)

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
                        super(AlarmLogger.Alarms, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(AlarmLogger.Alarms, self).__setattr__(name, value)


        class Alarm(Entity):
            """
            One of the logged alarms
            
            .. attribute:: event_id  <key>
            
            	Event ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: additional_text
            
            	Full text of the Alarm
            	**type**\:  str
            
            .. attribute:: category
            
            	Category of the alarm
            	**type**\:  str
            
            .. attribute:: code
            
            	Alarm code which further qualifies the alarm within a message group
            	**type**\:  str
            
            .. attribute:: correlation_id
            
            	Correlation Identifier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: group
            
            	Group of messages to which this alarm belongs to
            	**type**\:  str
            
            .. attribute:: is_admin
            
            	Indicates the event id admin\-level
            	**type**\:  bool
            
            .. attribute:: severity
            
            	Severity of the alarm
            	**type**\:   :py:class:`AlAlarmSeverity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmSeverity>`
            
            .. attribute:: source_id
            
            	Source Identifier(Location).Indicates the node in which the alarm was generated
            	**type**\:  str
            
            .. attribute:: state
            
            	State of the alarm (bistate alarms only)
            	**type**\:   :py:class:`AlAlarmBistate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_oper.AlAlarmBistate>`
            
            .. attribute:: timestamp
            
            	Time when the alarm was generated. It is expressed in number of milliseconds since 00\:00 \:00 UTC, January 1, 1970
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: millisecond
            
            

            """

            _prefix = 'infra-alarm-logger-oper'
            _revision = '2015-01-07'

            def __init__(self):
                super(AlarmLogger.Alarms.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "alarms"

                self.event_id = YLeaf(YType.int32, "event-id")

                self.additional_text = YLeaf(YType.str, "additional-text")

                self.category = YLeaf(YType.str, "category")

                self.code = YLeaf(YType.str, "code")

                self.correlation_id = YLeaf(YType.uint32, "correlation-id")

                self.group = YLeaf(YType.str, "group")

                self.is_admin = YLeaf(YType.boolean, "is-admin")

                self.severity = YLeaf(YType.enumeration, "severity")

                self.source_id = YLeaf(YType.str, "source-id")

                self.state = YLeaf(YType.enumeration, "state")

                self.timestamp = YLeaf(YType.uint64, "timestamp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("event_id",
                                "additional_text",
                                "category",
                                "code",
                                "correlation_id",
                                "group",
                                "is_admin",
                                "severity",
                                "source_id",
                                "state",
                                "timestamp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(AlarmLogger.Alarms.Alarm, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(AlarmLogger.Alarms.Alarm, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.event_id.is_set or
                    self.additional_text.is_set or
                    self.category.is_set or
                    self.code.is_set or
                    self.correlation_id.is_set or
                    self.group.is_set or
                    self.is_admin.is_set or
                    self.severity.is_set or
                    self.source_id.is_set or
                    self.state.is_set or
                    self.timestamp.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.event_id.yfilter != YFilter.not_set or
                    self.additional_text.yfilter != YFilter.not_set or
                    self.category.yfilter != YFilter.not_set or
                    self.code.yfilter != YFilter.not_set or
                    self.correlation_id.yfilter != YFilter.not_set or
                    self.group.yfilter != YFilter.not_set or
                    self.is_admin.yfilter != YFilter.not_set or
                    self.severity.yfilter != YFilter.not_set or
                    self.source_id.yfilter != YFilter.not_set or
                    self.state.yfilter != YFilter.not_set or
                    self.timestamp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "alarm" + "[event-id='" + self.event_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/alarms/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.event_id.is_set or self.event_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.event_id.get_name_leafdata())
                if (self.additional_text.is_set or self.additional_text.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.additional_text.get_name_leafdata())
                if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.category.get_name_leafdata())
                if (self.code.is_set or self.code.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.code.get_name_leafdata())
                if (self.correlation_id.is_set or self.correlation_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.correlation_id.get_name_leafdata())
                if (self.group.is_set or self.group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.group.get_name_leafdata())
                if (self.is_admin.is_set or self.is_admin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_admin.get_name_leafdata())
                if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.severity.get_name_leafdata())
                if (self.source_id.is_set or self.source_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_id.get_name_leafdata())
                if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.state.get_name_leafdata())
                if (self.timestamp.is_set or self.timestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timestamp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "event-id" or name == "additional-text" or name == "category" or name == "code" or name == "correlation-id" or name == "group" or name == "is-admin" or name == "severity" or name == "source-id" or name == "state" or name == "timestamp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "event-id"):
                    self.event_id = value
                    self.event_id.value_namespace = name_space
                    self.event_id.value_namespace_prefix = name_space_prefix
                if(value_path == "additional-text"):
                    self.additional_text = value
                    self.additional_text.value_namespace = name_space
                    self.additional_text.value_namespace_prefix = name_space_prefix
                if(value_path == "category"):
                    self.category = value
                    self.category.value_namespace = name_space
                    self.category.value_namespace_prefix = name_space_prefix
                if(value_path == "code"):
                    self.code = value
                    self.code.value_namespace = name_space
                    self.code.value_namespace_prefix = name_space_prefix
                if(value_path == "correlation-id"):
                    self.correlation_id = value
                    self.correlation_id.value_namespace = name_space
                    self.correlation_id.value_namespace_prefix = name_space_prefix
                if(value_path == "group"):
                    self.group = value
                    self.group.value_namespace = name_space
                    self.group.value_namespace_prefix = name_space_prefix
                if(value_path == "is-admin"):
                    self.is_admin = value
                    self.is_admin.value_namespace = name_space
                    self.is_admin.value_namespace_prefix = name_space_prefix
                if(value_path == "severity"):
                    self.severity = value
                    self.severity.value_namespace = name_space
                    self.severity.value_namespace_prefix = name_space_prefix
                if(value_path == "source-id"):
                    self.source_id = value
                    self.source_id.value_namespace = name_space
                    self.source_id.value_namespace_prefix = name_space_prefix
                if(value_path == "state"):
                    self.state = value
                    self.state.value_namespace = name_space
                    self.state.value_namespace_prefix = name_space_prefix
                if(value_path == "timestamp"):
                    self.timestamp = value
                    self.timestamp.value_namespace = name_space
                    self.timestamp.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.alarm:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.alarm:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "alarms" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "alarm"):
                for c in self.alarm:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = AlarmLogger.Alarms.Alarm()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.alarm.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "alarm"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.alarms is not None and self.alarms.has_data()) or
            (self.buffer_status is not None and self.buffer_status.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.alarms is not None and self.alarms.has_operation()) or
            (self.buffer_status is not None and self.buffer_status.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-alarm-logger-oper:alarm-logger" + path_buffer

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

        if (child_yang_name == "alarms"):
            if (self.alarms is None):
                self.alarms = AlarmLogger.Alarms()
                self.alarms.parent = self
                self._children_name_map["alarms"] = "alarms"
            return self.alarms

        if (child_yang_name == "buffer-status"):
            if (self.buffer_status is None):
                self.buffer_status = AlarmLogger.BufferStatus()
                self.buffer_status.parent = self
                self._children_name_map["buffer_status"] = "buffer-status"
            return self.buffer_status

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "alarms" or name == "buffer-status"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = AlarmLogger()
        return self._top_entity

