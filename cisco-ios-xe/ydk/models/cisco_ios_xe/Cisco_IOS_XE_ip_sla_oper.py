""" Cisco_IOS_XE_ip_sla_oper 

This module contains a collection of YANG definitions
for monitoring of IP SLA statistics of a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AccuracyType(Enum):
    """
    AccuracyType

    IP SLA accuracy type

    .. data:: accuracy_milliseconds = 0

    .. data:: accuracy_microseconds = 1

    """

    accuracy_milliseconds = Enum.YLeaf(0, "accuracy-milliseconds")

    accuracy_microseconds = Enum.YLeaf(1, "accuracy-microseconds")


class RttType(Enum):
    """
    RttType

    IP SLA RTT type

    .. data:: rtt_known = 0

    .. data:: rtt_unknown = 1

    .. data:: rtt_could_not_find = 2

    """

    rtt_known = Enum.YLeaf(0, "rtt-known")

    rtt_unknown = Enum.YLeaf(1, "rtt-unknown")

    rtt_could_not_find = Enum.YLeaf(2, "rtt-could-not-find")


class SlaOperType(Enum):
    """
    SlaOperType

    IP SLA operational type

    .. data:: oper_type_unknown = 0

    .. data:: oper_type_udp_echo = 1

    .. data:: oper_type_udp_jitter = 2

    .. data:: oper_type_icmp_jitter = 3

    .. data:: oper_type_ethernet_jitter = 4

    .. data:: oper_type_ethernet_echo = 5

    .. data:: oper_type_y1731_delay = 6

    .. data:: oper_type_y1731_loss = 7

    .. data:: oper_type_video = 8

    .. data:: oper_type_mcast = 9

    .. data:: oper_type_pong = 10

    .. data:: oper_type_path_jitter = 11

    """

    oper_type_unknown = Enum.YLeaf(0, "oper-type-unknown")

    oper_type_udp_echo = Enum.YLeaf(1, "oper-type-udp-echo")

    oper_type_udp_jitter = Enum.YLeaf(2, "oper-type-udp-jitter")

    oper_type_icmp_jitter = Enum.YLeaf(3, "oper-type-icmp-jitter")

    oper_type_ethernet_jitter = Enum.YLeaf(4, "oper-type-ethernet-jitter")

    oper_type_ethernet_echo = Enum.YLeaf(5, "oper-type-ethernet-echo")

    oper_type_y1731_delay = Enum.YLeaf(6, "oper-type-y1731-delay")

    oper_type_y1731_loss = Enum.YLeaf(7, "oper-type-y1731-loss")

    oper_type_video = Enum.YLeaf(8, "oper-type-video")

    oper_type_mcast = Enum.YLeaf(9, "oper-type-mcast")

    oper_type_pong = Enum.YLeaf(10, "oper-type-pong")

    oper_type_path_jitter = Enum.YLeaf(11, "oper-type-path-jitter")


class SlaReturnCode(Enum):
    """
    SlaReturnCode

    IP SLA return code

    .. data:: ret_code_unknown = 0

    .. data:: ret_code_ok = 1

    .. data:: ret_code_disconnected = 2

    .. data:: ret_code_busy = 3

    .. data:: ret_code_timeout = 4

    .. data:: ret_code_no_connection = 5

    .. data:: ret_code_internal_error = 6

    .. data:: ret_code_operation_failure = 7

    .. data:: ret_code_could_not_find = 8

    """

    ret_code_unknown = Enum.YLeaf(0, "ret-code-unknown")

    ret_code_ok = Enum.YLeaf(1, "ret-code-ok")

    ret_code_disconnected = Enum.YLeaf(2, "ret-code-disconnected")

    ret_code_busy = Enum.YLeaf(3, "ret-code-busy")

    ret_code_timeout = Enum.YLeaf(4, "ret-code-timeout")

    ret_code_no_connection = Enum.YLeaf(5, "ret-code-no-connection")

    ret_code_internal_error = Enum.YLeaf(6, "ret-code-internal-error")

    ret_code_operation_failure = Enum.YLeaf(7, "ret-code-operation-failure")

    ret_code_could_not_find = Enum.YLeaf(8, "ret-code-could-not-find")


class TtlType(Enum):
    """
    TtlType

    IP SLA time\-to\-live type

    .. data:: ttl_finite = 0

    .. data:: ttl_forever = 1

    """

    ttl_finite = Enum.YLeaf(0, "ttl-finite")

    ttl_forever = Enum.YLeaf(1, "ttl-forever")



class IpSlaStats(Entity):
    """
    Data nodes for All IP SLA Statistics
    
    .. attribute:: sla_oper_entry
    
    	The list of IP SLA operations with statistics info
    	**type**\: list of    :py:class:`SlaOperEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry>`
    
    

    """

    _prefix = 'ip-sla-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(IpSlaStats, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-sla-stats"
        self.yang_parent_name = "Cisco-IOS-XE-ip-sla-oper"

        self.sla_oper_entry = YList(self)

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
                    super(IpSlaStats, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(IpSlaStats, self).__setattr__(name, value)


    class SlaOperEntry(Entity):
        """
        The list of IP SLA operations with statistics info
        
        .. attribute:: oper_id  <key>
        
        	Entry unique identifier
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: failure_count
        
        	Failure count
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: latest_oper_start_time
        
        	Latest start time
        	**type**\:  str
        
        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
        
        .. attribute:: latest_return_code
        
        	Latest return code
        	**type**\:   :py:class:`SlaReturnCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.SlaReturnCode>`
        
        .. attribute:: measure_stats
        
        	Measured statistics
        	**type**\:   :py:class:`MeasureStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.MeasureStats>`
        
        .. attribute:: oper_type
        
        	Entry type
        	**type**\:   :py:class:`SlaOperType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.SlaOperType>`
        
        .. attribute:: rtt_info
        
        	RTT information
        	**type**\:   :py:class:`RttInfo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo>`
        
        .. attribute:: stats
        
        	Statistics
        	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats>`
        
        .. attribute:: success_count
        
        	Success count
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ip-sla-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(IpSlaStats.SlaOperEntry, self).__init__()

            self.yang_name = "sla-oper-entry"
            self.yang_parent_name = "ip-sla-stats"

            self.oper_id = YLeaf(YType.uint32, "oper-id")

            self.failure_count = YLeaf(YType.uint32, "failure-count")

            self.latest_oper_start_time = YLeaf(YType.str, "latest-oper-start-time")

            self.latest_return_code = YLeaf(YType.enumeration, "latest-return-code")

            self.oper_type = YLeaf(YType.enumeration, "oper-type")

            self.success_count = YLeaf(YType.uint32, "success-count")

            self.measure_stats = IpSlaStats.SlaOperEntry.MeasureStats()
            self.measure_stats.parent = self
            self._children_name_map["measure_stats"] = "measure-stats"
            self._children_yang_names.add("measure-stats")

            self.rtt_info = IpSlaStats.SlaOperEntry.RttInfo()
            self.rtt_info.parent = self
            self._children_name_map["rtt_info"] = "rtt-info"
            self._children_yang_names.add("rtt-info")

            self.stats = IpSlaStats.SlaOperEntry.Stats()
            self.stats.parent = self
            self._children_name_map["stats"] = "stats"
            self._children_yang_names.add("stats")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("oper_id",
                            "failure_count",
                            "latest_oper_start_time",
                            "latest_return_code",
                            "oper_type",
                            "success_count") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpSlaStats.SlaOperEntry, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpSlaStats.SlaOperEntry, self).__setattr__(name, value)


        class RttInfo(Entity):
            """
            RTT information
            
            .. attribute:: latest_rtt
            
            	The last Round Trip Time recorded for this SLA
            	**type**\:   :py:class:`LatestRtt <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo.LatestRtt>`
            
            .. attribute:: time_to_live
            
            	Time\-to\-live for the SLA operation
            	**type**\:   :py:class:`TimeToLive <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.RttInfo.TimeToLive>`
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(IpSlaStats.SlaOperEntry.RttInfo, self).__init__()

                self.yang_name = "rtt-info"
                self.yang_parent_name = "sla-oper-entry"

                self.latest_rtt = IpSlaStats.SlaOperEntry.RttInfo.LatestRtt()
                self.latest_rtt.parent = self
                self._children_name_map["latest_rtt"] = "latest-rtt"
                self._children_yang_names.add("latest-rtt")

                self.time_to_live = IpSlaStats.SlaOperEntry.RttInfo.TimeToLive()
                self.time_to_live.parent = self
                self._children_name_map["time_to_live"] = "time-to-live"
                self._children_yang_names.add("time-to-live")


            class LatestRtt(Entity):
                """
                The last Round Trip Time recorded for this SLA
                
                .. attribute:: could_not_find
                
                	Round trip time could not be determined
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rtt
                
                	Round trip time value
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: unknown
                
                	Round trip time is unknown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.RttInfo.LatestRtt, self).__init__()

                    self.yang_name = "latest-rtt"
                    self.yang_parent_name = "rtt-info"

                    self.could_not_find = YLeaf(YType.empty, "could-not-find")

                    self.rtt = YLeaf(YType.uint64, "rtt")

                    self.unknown = YLeaf(YType.empty, "unknown")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("could_not_find",
                                    "rtt",
                                    "unknown") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.RttInfo.LatestRtt, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.RttInfo.LatestRtt, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.could_not_find.is_set or
                        self.rtt.is_set or
                        self.unknown.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.could_not_find.yfilter != YFilter.not_set or
                        self.rtt.yfilter != YFilter.not_set or
                        self.unknown.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "latest-rtt" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.could_not_find.is_set or self.could_not_find.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.could_not_find.get_name_leafdata())
                    if (self.rtt.is_set or self.rtt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt.get_name_leafdata())
                    if (self.unknown.is_set or self.unknown.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "could-not-find" or name == "rtt" or name == "unknown"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "could-not-find"):
                        self.could_not_find = value
                        self.could_not_find.value_namespace = name_space
                        self.could_not_find.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt"):
                        self.rtt = value
                        self.rtt.value_namespace = name_space
                        self.rtt.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown"):
                        self.unknown = value
                        self.unknown.value_namespace = name_space
                        self.unknown.value_namespace_prefix = name_space_prefix


            class TimeToLive(Entity):
                """
                Time\-to\-live for the SLA operation
                
                .. attribute:: forever
                
                	Time to live unbound
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ttl
                
                	Time to live value
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.RttInfo.TimeToLive, self).__init__()

                    self.yang_name = "time-to-live"
                    self.yang_parent_name = "rtt-info"

                    self.forever = YLeaf(YType.empty, "forever")

                    self.ttl = YLeaf(YType.uint64, "ttl")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("forever",
                                    "ttl") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.RttInfo.TimeToLive, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.RttInfo.TimeToLive, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.forever.is_set or
                        self.ttl.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.forever.yfilter != YFilter.not_set or
                        self.ttl.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "time-to-live" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.forever.is_set or self.forever.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.forever.get_name_leafdata())
                    if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ttl.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "forever" or name == "ttl"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "forever"):
                        self.forever = value
                        self.forever.value_namespace = name_space
                        self.forever.value_namespace_prefix = name_space_prefix
                    if(value_path == "ttl"):
                        self.ttl = value
                        self.ttl.value_namespace = name_space
                        self.ttl.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.latest_rtt is not None and self.latest_rtt.has_data()) or
                    (self.time_to_live is not None and self.time_to_live.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.latest_rtt is not None and self.latest_rtt.has_operation()) or
                    (self.time_to_live is not None and self.time_to_live.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rtt-info" + path_buffer

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

                if (child_yang_name == "latest-rtt"):
                    if (self.latest_rtt is None):
                        self.latest_rtt = IpSlaStats.SlaOperEntry.RttInfo.LatestRtt()
                        self.latest_rtt.parent = self
                        self._children_name_map["latest_rtt"] = "latest-rtt"
                    return self.latest_rtt

                if (child_yang_name == "time-to-live"):
                    if (self.time_to_live is None):
                        self.time_to_live = IpSlaStats.SlaOperEntry.RttInfo.TimeToLive()
                        self.time_to_live.parent = self
                        self._children_name_map["time_to_live"] = "time-to-live"
                    return self.time_to_live

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "latest-rtt" or name == "time-to-live"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class MeasureStats(Entity):
            """
            Measured statistics
            
            .. attribute:: complete_count
            
            	Complete count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: init_count
            
            	Initial count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intv_start_time
            
            	Interval start time
            	**type**\:  str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: valid
            
            	Validity
            	**type**\:  bool
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(IpSlaStats.SlaOperEntry.MeasureStats, self).__init__()

                self.yang_name = "measure-stats"
                self.yang_parent_name = "sla-oper-entry"

                self.complete_count = YLeaf(YType.uint32, "complete-count")

                self.init_count = YLeaf(YType.uint32, "init-count")

                self.intv_start_time = YLeaf(YType.str, "intv-start-time")

                self.valid = YLeaf(YType.boolean, "valid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("complete_count",
                                "init_count",
                                "intv_start_time",
                                "valid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpSlaStats.SlaOperEntry.MeasureStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpSlaStats.SlaOperEntry.MeasureStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.complete_count.is_set or
                    self.init_count.is_set or
                    self.intv_start_time.is_set or
                    self.valid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.complete_count.yfilter != YFilter.not_set or
                    self.init_count.yfilter != YFilter.not_set or
                    self.intv_start_time.yfilter != YFilter.not_set or
                    self.valid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "measure-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.complete_count.is_set or self.complete_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.complete_count.get_name_leafdata())
                if (self.init_count.is_set or self.init_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.init_count.get_name_leafdata())
                if (self.intv_start_time.is_set or self.intv_start_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.intv_start_time.get_name_leafdata())
                if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.valid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "complete-count" or name == "init-count" or name == "intv-start-time" or name == "valid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "complete-count"):
                    self.complete_count = value
                    self.complete_count.value_namespace = name_space
                    self.complete_count.value_namespace_prefix = name_space_prefix
                if(value_path == "init-count"):
                    self.init_count = value
                    self.init_count.value_namespace = name_space
                    self.init_count.value_namespace_prefix = name_space_prefix
                if(value_path == "intv-start-time"):
                    self.intv_start_time = value
                    self.intv_start_time.value_namespace = name_space
                    self.intv_start_time.value_namespace_prefix = name_space_prefix
                if(value_path == "valid"):
                    self.valid = value
                    self.valid.value_namespace = name_space
                    self.valid.value_namespace_prefix = name_space_prefix


        class Stats(Entity):
            """
            Statistics
            
            .. attribute:: icmp_packet_loss
            
            	ICMP packet loss information
            	**type**\:   :py:class:`IcmpPacketLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss>`
            
            .. attribute:: jitter
            
            	Jitter information
            	**type**\:   :py:class:`Jitter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter>`
            
            .. attribute:: oneway_latency
            
            	Latency information
            	**type**\:   :py:class:`OnewayLatency <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency>`
            
            .. attribute:: over_threshold
            
            	Over threshold information
            	**type**\:   :py:class:`OverThreshold <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OverThreshold>`
            
            .. attribute:: packet_loss
            
            	Packet loss information
            	**type**\:   :py:class:`PacketLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss>`
            
            .. attribute:: rtt
            
            	RTT value
            	**type**\:   :py:class:`Rtt <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Rtt>`
            
            .. attribute:: voice_score
            
            	Voice score information
            	**type**\:   :py:class:`VoiceScore <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.VoiceScore>`
            
            

            """

            _prefix = 'ip-sla-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(IpSlaStats.SlaOperEntry.Stats, self).__init__()

                self.yang_name = "stats"
                self.yang_parent_name = "sla-oper-entry"

                self.icmp_packet_loss = IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss()
                self.icmp_packet_loss.parent = self
                self._children_name_map["icmp_packet_loss"] = "icmp-packet-loss"
                self._children_yang_names.add("icmp-packet-loss")

                self.jitter = IpSlaStats.SlaOperEntry.Stats.Jitter()
                self.jitter.parent = self
                self._children_name_map["jitter"] = "jitter"
                self._children_yang_names.add("jitter")

                self.oneway_latency = IpSlaStats.SlaOperEntry.Stats.OnewayLatency()
                self.oneway_latency.parent = self
                self._children_name_map["oneway_latency"] = "oneway-latency"
                self._children_yang_names.add("oneway-latency")

                self.over_threshold = IpSlaStats.SlaOperEntry.Stats.OverThreshold()
                self.over_threshold.parent = self
                self._children_name_map["over_threshold"] = "over-threshold"
                self._children_yang_names.add("over-threshold")

                self.packet_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss()
                self.packet_loss.parent = self
                self._children_name_map["packet_loss"] = "packet-loss"
                self._children_yang_names.add("packet-loss")

                self.rtt = IpSlaStats.SlaOperEntry.Stats.Rtt()
                self.rtt.parent = self
                self._children_name_map["rtt"] = "rtt"
                self._children_yang_names.add("rtt")

                self.voice_score = IpSlaStats.SlaOperEntry.Stats.VoiceScore()
                self.voice_score.parent = self
                self._children_name_map["voice_score"] = "voice-score"
                self._children_yang_names.add("voice-score")


            class Rtt(Entity):
                """
                RTT value
                
                .. attribute:: rtt_count
                
                	RTT count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sla_time_values
                
                	Timing information
                	**type**\:   :py:class:`SlaTimeValues <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.Rtt, self).__init__()

                    self.yang_name = "rtt"
                    self.yang_parent_name = "stats"

                    self.rtt_count = YLeaf(YType.uint32, "rtt-count")

                    self.sla_time_values = IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues()
                    self.sla_time_values.parent = self
                    self._children_name_map["sla_time_values"] = "sla-time-values"
                    self._children_yang_names.add("sla-time-values")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("rtt_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.Rtt, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.Rtt, self).__setattr__(name, value)


                class SlaTimeValues(Entity):
                    """
                    Timing information
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:   :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues, self).__init__()

                        self.yang_name = "sla-time-values"
                        self.yang_parent_name = "rtt"

                        self.accuracy = YLeaf(YType.enumeration, "accuracy")

                        self.avg = YLeaf(YType.uint32, "avg")

                        self.max = YLeaf(YType.uint32, "max")

                        self.min = YLeaf(YType.uint32, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accuracy",
                                        "avg",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accuracy.is_set or
                            self.avg.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accuracy.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sla-time-values" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accuracy.is_set or self.accuracy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accuracy.get_name_leafdata())
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accuracy" or name == "avg" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accuracy"):
                            self.accuracy = value
                            self.accuracy.value_namespace = name_space
                            self.accuracy.value_namespace_prefix = name_space_prefix
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.rtt_count.is_set or
                        (self.sla_time_values is not None and self.sla_time_values.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.rtt_count.yfilter != YFilter.not_set or
                        (self.sla_time_values is not None and self.sla_time_values.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "rtt" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.rtt_count.is_set or self.rtt_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "sla-time-values"):
                        if (self.sla_time_values is None):
                            self.sla_time_values = IpSlaStats.SlaOperEntry.Stats.Rtt.SlaTimeValues()
                            self.sla_time_values.parent = self
                            self._children_name_map["sla_time_values"] = "sla-time-values"
                        return self.sla_time_values

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "sla-time-values" or name == "rtt-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "rtt-count"):
                        self.rtt_count = value
                        self.rtt_count.value_namespace = name_space
                        self.rtt_count.value_namespace_prefix = name_space_prefix


            class OnewayLatency(Entity):
                """
                Latency information
                
                .. attribute:: ds
                
                	Destination to Source for the one\-way latency
                	**type**\:   :py:class:`Ds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds>`
                
                .. attribute:: sample_count
                
                	Sample count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd
                
                	Source to Destination for the one\-way latency
                	**type**\:   :py:class:`Sd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd>`
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency, self).__init__()

                    self.yang_name = "oneway-latency"
                    self.yang_parent_name = "stats"

                    self.sample_count = YLeaf(YType.uint32, "sample-count")

                    self.ds = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds()
                    self.ds.parent = self
                    self._children_name_map["ds"] = "ds"
                    self._children_yang_names.add("ds")

                    self.sd = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd()
                    self.sd.parent = self
                    self._children_name_map["sd"] = "sd"
                    self._children_yang_names.add("sd")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("sample_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency, self).__setattr__(name, value)


                class Sd(Entity):
                    """
                    Source to Destination for the one\-way latency
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:   :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd, self).__init__()

                        self.yang_name = "sd"
                        self.yang_parent_name = "oneway-latency"

                        self.accuracy = YLeaf(YType.enumeration, "accuracy")

                        self.avg = YLeaf(YType.uint32, "avg")

                        self.max = YLeaf(YType.uint32, "max")

                        self.min = YLeaf(YType.uint32, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accuracy",
                                        "avg",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accuracy.is_set or
                            self.avg.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accuracy.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sd" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accuracy.is_set or self.accuracy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accuracy.get_name_leafdata())
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accuracy" or name == "avg" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accuracy"):
                            self.accuracy = value
                            self.accuracy.value_namespace = name_space
                            self.accuracy.value_namespace_prefix = name_space_prefix
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class Ds(Entity):
                    """
                    Destination to Source for the one\-way latency
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:   :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds, self).__init__()

                        self.yang_name = "ds"
                        self.yang_parent_name = "oneway-latency"

                        self.accuracy = YLeaf(YType.enumeration, "accuracy")

                        self.avg = YLeaf(YType.uint32, "avg")

                        self.max = YLeaf(YType.uint32, "max")

                        self.min = YLeaf(YType.uint32, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accuracy",
                                        "avg",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accuracy.is_set or
                            self.avg.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accuracy.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ds" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accuracy.is_set or self.accuracy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accuracy.get_name_leafdata())
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accuracy" or name == "avg" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accuracy"):
                            self.accuracy = value
                            self.accuracy.value_namespace = name_space
                            self.accuracy.value_namespace_prefix = name_space_prefix
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.sample_count.is_set or
                        (self.ds is not None and self.ds.has_data()) or
                        (self.sd is not None and self.sd.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.sample_count.yfilter != YFilter.not_set or
                        (self.ds is not None and self.ds.has_operation()) or
                        (self.sd is not None and self.sd.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "oneway-latency" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.sample_count.is_set or self.sample_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sample_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ds"):
                        if (self.ds is None):
                            self.ds = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Ds()
                            self.ds.parent = self
                            self._children_name_map["ds"] = "ds"
                        return self.ds

                    if (child_yang_name == "sd"):
                        if (self.sd is None):
                            self.sd = IpSlaStats.SlaOperEntry.Stats.OnewayLatency.Sd()
                            self.sd.parent = self
                            self._children_name_map["sd"] = "sd"
                        return self.sd

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ds" or name == "sd" or name == "sample-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "sample-count"):
                        self.sample_count = value
                        self.sample_count.value_namespace = name_space
                        self.sample_count.value_namespace_prefix = name_space_prefix


            class Jitter(Entity):
                """
                Jitter information
                
                .. attribute:: ds
                
                	Destination to Source for the jitter
                	**type**\:   :py:class:`Ds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter.Ds>`
                
                .. attribute:: ds_sample_count
                
                	Sample count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd
                
                	Source to Destination for the jitter
                	**type**\:   :py:class:`Sd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.Jitter.Sd>`
                
                .. attribute:: sd_sample_count
                
                	Sample count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.Jitter, self).__init__()

                    self.yang_name = "jitter"
                    self.yang_parent_name = "stats"

                    self.ds_sample_count = YLeaf(YType.uint32, "ds-sample-count")

                    self.sd_sample_count = YLeaf(YType.uint32, "sd-sample-count")

                    self.ds = IpSlaStats.SlaOperEntry.Stats.Jitter.Ds()
                    self.ds.parent = self
                    self._children_name_map["ds"] = "ds"
                    self._children_yang_names.add("ds")

                    self.sd = IpSlaStats.SlaOperEntry.Stats.Jitter.Sd()
                    self.sd.parent = self
                    self._children_name_map["sd"] = "sd"
                    self._children_yang_names.add("sd")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("ds_sample_count",
                                    "sd_sample_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.Jitter, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.Jitter, self).__setattr__(name, value)


                class Sd(Entity):
                    """
                    Source to Destination for the jitter
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:   :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.Jitter.Sd, self).__init__()

                        self.yang_name = "sd"
                        self.yang_parent_name = "jitter"

                        self.accuracy = YLeaf(YType.enumeration, "accuracy")

                        self.avg = YLeaf(YType.uint32, "avg")

                        self.max = YLeaf(YType.uint32, "max")

                        self.min = YLeaf(YType.uint32, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accuracy",
                                        "avg",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.Jitter.Sd, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.Jitter.Sd, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accuracy.is_set or
                            self.avg.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accuracy.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sd" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accuracy.is_set or self.accuracy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accuracy.get_name_leafdata())
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accuracy" or name == "avg" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accuracy"):
                            self.accuracy = value
                            self.accuracy.value_namespace = name_space
                            self.accuracy.value_namespace_prefix = name_space_prefix
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix


                class Ds(Entity):
                    """
                    Destination to Source for the jitter
                    
                    .. attribute:: accuracy
                    
                    	Reading accuracy
                    	**type**\:   :py:class:`AccuracyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.AccuracyType>`
                    
                    .. attribute:: avg
                    
                    	Average value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max
                    
                    	Maximum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min
                    
                    	Minimum value reading
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.Jitter.Ds, self).__init__()

                        self.yang_name = "ds"
                        self.yang_parent_name = "jitter"

                        self.accuracy = YLeaf(YType.enumeration, "accuracy")

                        self.avg = YLeaf(YType.uint32, "avg")

                        self.max = YLeaf(YType.uint32, "max")

                        self.min = YLeaf(YType.uint32, "min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("accuracy",
                                        "avg",
                                        "max",
                                        "min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.Jitter.Ds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.Jitter.Ds, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.accuracy.is_set or
                            self.avg.is_set or
                            self.max.is_set or
                            self.min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.accuracy.yfilter != YFilter.not_set or
                            self.avg.yfilter != YFilter.not_set or
                            self.max.yfilter != YFilter.not_set or
                            self.min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ds" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.accuracy.is_set or self.accuracy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.accuracy.get_name_leafdata())
                        if (self.avg.is_set or self.avg.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.avg.get_name_leafdata())
                        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max.get_name_leafdata())
                        if (self.min.is_set or self.min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "accuracy" or name == "avg" or name == "max" or name == "min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "accuracy"):
                            self.accuracy = value
                            self.accuracy.value_namespace = name_space
                            self.accuracy.value_namespace_prefix = name_space_prefix
                        if(value_path == "avg"):
                            self.avg = value
                            self.avg.value_namespace = name_space
                            self.avg.value_namespace_prefix = name_space_prefix
                        if(value_path == "max"):
                            self.max = value
                            self.max.value_namespace = name_space
                            self.max.value_namespace_prefix = name_space_prefix
                        if(value_path == "min"):
                            self.min = value
                            self.min.value_namespace = name_space
                            self.min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.ds_sample_count.is_set or
                        self.sd_sample_count.is_set or
                        (self.ds is not None and self.ds.has_data()) or
                        (self.sd is not None and self.sd.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.ds_sample_count.yfilter != YFilter.not_set or
                        self.sd_sample_count.yfilter != YFilter.not_set or
                        (self.ds is not None and self.ds.has_operation()) or
                        (self.sd is not None and self.sd.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "jitter" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.ds_sample_count.is_set or self.ds_sample_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ds_sample_count.get_name_leafdata())
                    if (self.sd_sample_count.is_set or self.sd_sample_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sd_sample_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ds"):
                        if (self.ds is None):
                            self.ds = IpSlaStats.SlaOperEntry.Stats.Jitter.Ds()
                            self.ds.parent = self
                            self._children_name_map["ds"] = "ds"
                        return self.ds

                    if (child_yang_name == "sd"):
                        if (self.sd is None):
                            self.sd = IpSlaStats.SlaOperEntry.Stats.Jitter.Sd()
                            self.sd.parent = self
                            self._children_name_map["sd"] = "sd"
                        return self.sd

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ds" or name == "sd" or name == "ds-sample-count" or name == "sd-sample-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "ds-sample-count"):
                        self.ds_sample_count = value
                        self.ds_sample_count.value_namespace = name_space
                        self.ds_sample_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "sd-sample-count"):
                        self.sd_sample_count = value
                        self.sd_sample_count.value_namespace = name_space
                        self.sd_sample_count.value_namespace_prefix = name_space_prefix


            class OverThreshold(Entity):
                """
                Over threshold information
                
                .. attribute:: percent
                
                	Round Trip Time over threshold percentage (the percentage that the RTT was over the configured threshold)
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: rtt_count
                
                	Round Trip Time (RTT) over threshold count (the number of times that the RTT was over the configured threshold)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.OverThreshold, self).__init__()

                    self.yang_name = "over-threshold"
                    self.yang_parent_name = "stats"

                    self.percent = YLeaf(YType.uint8, "percent")

                    self.rtt_count = YLeaf(YType.uint32, "rtt-count")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("percent",
                                    "rtt_count") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.OverThreshold, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.OverThreshold, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.percent.is_set or
                        self.rtt_count.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.percent.yfilter != YFilter.not_set or
                        self.rtt_count.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "over-threshold" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.percent.is_set or self.percent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.percent.get_name_leafdata())
                    if (self.rtt_count.is_set or self.rtt_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rtt_count.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "percent" or name == "rtt-count"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "percent"):
                        self.percent = value
                        self.percent.value_namespace = name_space
                        self.percent.value_namespace_prefix = name_space_prefix
                    if(value_path == "rtt-count"):
                        self.rtt_count = value
                        self.rtt_count.value_namespace = name_space
                        self.rtt_count.value_namespace_prefix = name_space_prefix


            class PacketLoss(Entity):
                """
                Packet loss information
                
                .. attribute:: drops
                
                	Dropped packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ds_count
                
                	Number of packets lost from Destination to Source
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ds_loss
                
                	Destination to Source packet loss details
                	**type**\:   :py:class:`DsLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss>`
                
                .. attribute:: late_arrivals
                
                	Late arrival packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence
                
                	Out of sequence packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_count
                
                	Number of packets lost from Source to Destination
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sd_loss
                
                	Source to Destination packet loss details
                	**type**\:   :py:class:`SdLoss <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ip_sla_oper.IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss>`
                
                .. attribute:: skipped_packets
                
                	Skipped packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unprocessed_packets
                
                	Unprocessed packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.PacketLoss, self).__init__()

                    self.yang_name = "packet-loss"
                    self.yang_parent_name = "stats"

                    self.drops = YLeaf(YType.uint32, "drops")

                    self.ds_count = YLeaf(YType.uint32, "ds-count")

                    self.late_arrivals = YLeaf(YType.uint32, "late-arrivals")

                    self.out_of_sequence = YLeaf(YType.uint32, "out-of-sequence")

                    self.sd_count = YLeaf(YType.uint32, "sd-count")

                    self.skipped_packets = YLeaf(YType.uint32, "skipped-packets")

                    self.unprocessed_packets = YLeaf(YType.uint32, "unprocessed-packets")

                    self.ds_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss()
                    self.ds_loss.parent = self
                    self._children_name_map["ds_loss"] = "ds-loss"
                    self._children_yang_names.add("ds-loss")

                    self.sd_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss()
                    self.sd_loss.parent = self
                    self._children_name_map["sd_loss"] = "sd-loss"
                    self._children_yang_names.add("sd-loss")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("drops",
                                    "ds_count",
                                    "late_arrivals",
                                    "out_of_sequence",
                                    "sd_count",
                                    "skipped_packets",
                                    "unprocessed_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.PacketLoss, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.PacketLoss, self).__setattr__(name, value)


                class SdLoss(Entity):
                    """
                    Source to Destination packet loss details
                    
                    .. attribute:: inter_loss_period_len_max
                    
                    	Longest inter loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_min
                    
                    	Shortest inter loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_count
                    
                    	Loss period count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_max
                    
                    	Longest loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_min
                    
                    	Shortest loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss, self).__init__()

                        self.yang_name = "sd-loss"
                        self.yang_parent_name = "packet-loss"

                        self.inter_loss_period_len_max = YLeaf(YType.uint32, "inter-loss-period-len-max")

                        self.inter_loss_period_len_min = YLeaf(YType.uint32, "inter-loss-period-len-min")

                        self.loss_period_count = YLeaf(YType.uint32, "loss-period-count")

                        self.loss_period_len_max = YLeaf(YType.uint32, "loss-period-len-max")

                        self.loss_period_len_min = YLeaf(YType.uint32, "loss-period-len-min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("inter_loss_period_len_max",
                                        "inter_loss_period_len_min",
                                        "loss_period_count",
                                        "loss_period_len_max",
                                        "loss_period_len_min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.inter_loss_period_len_max.is_set or
                            self.inter_loss_period_len_min.is_set or
                            self.loss_period_count.is_set or
                            self.loss_period_len_max.is_set or
                            self.loss_period_len_min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.inter_loss_period_len_max.yfilter != YFilter.not_set or
                            self.inter_loss_period_len_min.yfilter != YFilter.not_set or
                            self.loss_period_count.yfilter != YFilter.not_set or
                            self.loss_period_len_max.yfilter != YFilter.not_set or
                            self.loss_period_len_min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sd-loss" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.inter_loss_period_len_max.is_set or self.inter_loss_period_len_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inter_loss_period_len_max.get_name_leafdata())
                        if (self.inter_loss_period_len_min.is_set or self.inter_loss_period_len_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inter_loss_period_len_min.get_name_leafdata())
                        if (self.loss_period_count.is_set or self.loss_period_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_period_count.get_name_leafdata())
                        if (self.loss_period_len_max.is_set or self.loss_period_len_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_period_len_max.get_name_leafdata())
                        if (self.loss_period_len_min.is_set or self.loss_period_len_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_period_len_min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "inter-loss-period-len-max" or name == "inter-loss-period-len-min" or name == "loss-period-count" or name == "loss-period-len-max" or name == "loss-period-len-min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "inter-loss-period-len-max"):
                            self.inter_loss_period_len_max = value
                            self.inter_loss_period_len_max.value_namespace = name_space
                            self.inter_loss_period_len_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "inter-loss-period-len-min"):
                            self.inter_loss_period_len_min = value
                            self.inter_loss_period_len_min.value_namespace = name_space
                            self.inter_loss_period_len_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-period-count"):
                            self.loss_period_count = value
                            self.loss_period_count.value_namespace = name_space
                            self.loss_period_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-period-len-max"):
                            self.loss_period_len_max = value
                            self.loss_period_len_max.value_namespace = name_space
                            self.loss_period_len_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-period-len-min"):
                            self.loss_period_len_min = value
                            self.loss_period_len_min.value_namespace = name_space
                            self.loss_period_len_min.value_namespace_prefix = name_space_prefix


                class DsLoss(Entity):
                    """
                    Destination to Source packet loss details
                    
                    .. attribute:: inter_loss_period_len_max
                    
                    	Longest inter loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inter_loss_period_len_min
                    
                    	Shortest inter loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_count
                    
                    	Loss period count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_max
                    
                    	Longest loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: loss_period_len_min
                    
                    	Shortest loss period length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-sla-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss, self).__init__()

                        self.yang_name = "ds-loss"
                        self.yang_parent_name = "packet-loss"

                        self.inter_loss_period_len_max = YLeaf(YType.uint32, "inter-loss-period-len-max")

                        self.inter_loss_period_len_min = YLeaf(YType.uint32, "inter-loss-period-len-min")

                        self.loss_period_count = YLeaf(YType.uint32, "loss-period-count")

                        self.loss_period_len_max = YLeaf(YType.uint32, "loss-period-len-max")

                        self.loss_period_len_min = YLeaf(YType.uint32, "loss-period-len-min")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("inter_loss_period_len_max",
                                        "inter_loss_period_len_min",
                                        "loss_period_count",
                                        "loss_period_len_max",
                                        "loss_period_len_min") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.inter_loss_period_len_max.is_set or
                            self.inter_loss_period_len_min.is_set or
                            self.loss_period_count.is_set or
                            self.loss_period_len_max.is_set or
                            self.loss_period_len_min.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.inter_loss_period_len_max.yfilter != YFilter.not_set or
                            self.inter_loss_period_len_min.yfilter != YFilter.not_set or
                            self.loss_period_count.yfilter != YFilter.not_set or
                            self.loss_period_len_max.yfilter != YFilter.not_set or
                            self.loss_period_len_min.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ds-loss" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.inter_loss_period_len_max.is_set or self.inter_loss_period_len_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inter_loss_period_len_max.get_name_leafdata())
                        if (self.inter_loss_period_len_min.is_set or self.inter_loss_period_len_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inter_loss_period_len_min.get_name_leafdata())
                        if (self.loss_period_count.is_set or self.loss_period_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_period_count.get_name_leafdata())
                        if (self.loss_period_len_max.is_set or self.loss_period_len_max.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_period_len_max.get_name_leafdata())
                        if (self.loss_period_len_min.is_set or self.loss_period_len_min.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.loss_period_len_min.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "inter-loss-period-len-max" or name == "inter-loss-period-len-min" or name == "loss-period-count" or name == "loss-period-len-max" or name == "loss-period-len-min"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "inter-loss-period-len-max"):
                            self.inter_loss_period_len_max = value
                            self.inter_loss_period_len_max.value_namespace = name_space
                            self.inter_loss_period_len_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "inter-loss-period-len-min"):
                            self.inter_loss_period_len_min = value
                            self.inter_loss_period_len_min.value_namespace = name_space
                            self.inter_loss_period_len_min.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-period-count"):
                            self.loss_period_count = value
                            self.loss_period_count.value_namespace = name_space
                            self.loss_period_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-period-len-max"):
                            self.loss_period_len_max = value
                            self.loss_period_len_max.value_namespace = name_space
                            self.loss_period_len_max.value_namespace_prefix = name_space_prefix
                        if(value_path == "loss-period-len-min"):
                            self.loss_period_len_min = value
                            self.loss_period_len_min.value_namespace = name_space
                            self.loss_period_len_min.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.drops.is_set or
                        self.ds_count.is_set or
                        self.late_arrivals.is_set or
                        self.out_of_sequence.is_set or
                        self.sd_count.is_set or
                        self.skipped_packets.is_set or
                        self.unprocessed_packets.is_set or
                        (self.ds_loss is not None and self.ds_loss.has_data()) or
                        (self.sd_loss is not None and self.sd_loss.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.drops.yfilter != YFilter.not_set or
                        self.ds_count.yfilter != YFilter.not_set or
                        self.late_arrivals.yfilter != YFilter.not_set or
                        self.out_of_sequence.yfilter != YFilter.not_set or
                        self.sd_count.yfilter != YFilter.not_set or
                        self.skipped_packets.yfilter != YFilter.not_set or
                        self.unprocessed_packets.yfilter != YFilter.not_set or
                        (self.ds_loss is not None and self.ds_loss.has_operation()) or
                        (self.sd_loss is not None and self.sd_loss.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "packet-loss" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.drops.is_set or self.drops.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.drops.get_name_leafdata())
                    if (self.ds_count.is_set or self.ds_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ds_count.get_name_leafdata())
                    if (self.late_arrivals.is_set or self.late_arrivals.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.late_arrivals.get_name_leafdata())
                    if (self.out_of_sequence.is_set or self.out_of_sequence.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_sequence.get_name_leafdata())
                    if (self.sd_count.is_set or self.sd_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sd_count.get_name_leafdata())
                    if (self.skipped_packets.is_set or self.skipped_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.skipped_packets.get_name_leafdata())
                    if (self.unprocessed_packets.is_set or self.unprocessed_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unprocessed_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ds-loss"):
                        if (self.ds_loss is None):
                            self.ds_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.DsLoss()
                            self.ds_loss.parent = self
                            self._children_name_map["ds_loss"] = "ds-loss"
                        return self.ds_loss

                    if (child_yang_name == "sd-loss"):
                        if (self.sd_loss is None):
                            self.sd_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss.SdLoss()
                            self.sd_loss.parent = self
                            self._children_name_map["sd_loss"] = "sd-loss"
                        return self.sd_loss

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ds-loss" or name == "sd-loss" or name == "drops" or name == "ds-count" or name == "late-arrivals" or name == "out-of-sequence" or name == "sd-count" or name == "skipped-packets" or name == "unprocessed-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "drops"):
                        self.drops = value
                        self.drops.value_namespace = name_space
                        self.drops.value_namespace_prefix = name_space_prefix
                    if(value_path == "ds-count"):
                        self.ds_count = value
                        self.ds_count.value_namespace = name_space
                        self.ds_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "late-arrivals"):
                        self.late_arrivals = value
                        self.late_arrivals.value_namespace = name_space
                        self.late_arrivals.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-sequence"):
                        self.out_of_sequence = value
                        self.out_of_sequence.value_namespace = name_space
                        self.out_of_sequence.value_namespace_prefix = name_space_prefix
                    if(value_path == "sd-count"):
                        self.sd_count = value
                        self.sd_count.value_namespace = name_space
                        self.sd_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "skipped-packets"):
                        self.skipped_packets = value
                        self.skipped_packets.value_namespace = name_space
                        self.skipped_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "unprocessed-packets"):
                        self.unprocessed_packets = value
                        self.unprocessed_packets.value_namespace = name_space
                        self.unprocessed_packets.value_namespace_prefix = name_space_prefix


            class IcmpPacketLoss(Entity):
                """
                ICMP packet loss information
                
                .. attribute:: inter_loss_period_len_max
                
                	Longest inter loss period length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: inter_loss_period_len_min
                
                	Shortest inter loss period length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: late_arrivals
                
                	Late arrival packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_count
                
                	Loss period count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_len_max
                
                	Longest loss period length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: loss_period_len_min
                
                	Shortest loss period length
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence
                
                	Out of sequence packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_both
                
                	Out of sequence packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_ds
                
                	Out of sequence packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_of_sequence_sd
                
                	Out of sequence packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packet_loss
                
                	Lost packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: skipped_packets
                
                	Skipped packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unprocessed_packets
                
                	Unprocessed packet count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss, self).__init__()

                    self.yang_name = "icmp-packet-loss"
                    self.yang_parent_name = "stats"

                    self.inter_loss_period_len_max = YLeaf(YType.uint32, "inter-loss-period-len-max")

                    self.inter_loss_period_len_min = YLeaf(YType.uint32, "inter-loss-period-len-min")

                    self.late_arrivals = YLeaf(YType.uint32, "late-arrivals")

                    self.loss_period_count = YLeaf(YType.uint32, "loss-period-count")

                    self.loss_period_len_max = YLeaf(YType.uint32, "loss-period-len-max")

                    self.loss_period_len_min = YLeaf(YType.uint32, "loss-period-len-min")

                    self.out_of_sequence = YLeaf(YType.uint32, "out-of-sequence")

                    self.out_of_sequence_both = YLeaf(YType.uint32, "out-of-sequence-both")

                    self.out_of_sequence_ds = YLeaf(YType.uint32, "out-of-sequence-ds")

                    self.out_of_sequence_sd = YLeaf(YType.uint32, "out-of-sequence-sd")

                    self.packet_loss = YLeaf(YType.uint32, "packet-loss")

                    self.skipped_packets = YLeaf(YType.uint32, "skipped-packets")

                    self.unprocessed_packets = YLeaf(YType.uint32, "unprocessed-packets")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("inter_loss_period_len_max",
                                    "inter_loss_period_len_min",
                                    "late_arrivals",
                                    "loss_period_count",
                                    "loss_period_len_max",
                                    "loss_period_len_min",
                                    "out_of_sequence",
                                    "out_of_sequence_both",
                                    "out_of_sequence_ds",
                                    "out_of_sequence_sd",
                                    "packet_loss",
                                    "skipped_packets",
                                    "unprocessed_packets") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.inter_loss_period_len_max.is_set or
                        self.inter_loss_period_len_min.is_set or
                        self.late_arrivals.is_set or
                        self.loss_period_count.is_set or
                        self.loss_period_len_max.is_set or
                        self.loss_period_len_min.is_set or
                        self.out_of_sequence.is_set or
                        self.out_of_sequence_both.is_set or
                        self.out_of_sequence_ds.is_set or
                        self.out_of_sequence_sd.is_set or
                        self.packet_loss.is_set or
                        self.skipped_packets.is_set or
                        self.unprocessed_packets.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.inter_loss_period_len_max.yfilter != YFilter.not_set or
                        self.inter_loss_period_len_min.yfilter != YFilter.not_set or
                        self.late_arrivals.yfilter != YFilter.not_set or
                        self.loss_period_count.yfilter != YFilter.not_set or
                        self.loss_period_len_max.yfilter != YFilter.not_set or
                        self.loss_period_len_min.yfilter != YFilter.not_set or
                        self.out_of_sequence.yfilter != YFilter.not_set or
                        self.out_of_sequence_both.yfilter != YFilter.not_set or
                        self.out_of_sequence_ds.yfilter != YFilter.not_set or
                        self.out_of_sequence_sd.yfilter != YFilter.not_set or
                        self.packet_loss.yfilter != YFilter.not_set or
                        self.skipped_packets.yfilter != YFilter.not_set or
                        self.unprocessed_packets.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "icmp-packet-loss" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.inter_loss_period_len_max.is_set or self.inter_loss_period_len_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.inter_loss_period_len_max.get_name_leafdata())
                    if (self.inter_loss_period_len_min.is_set or self.inter_loss_period_len_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.inter_loss_period_len_min.get_name_leafdata())
                    if (self.late_arrivals.is_set or self.late_arrivals.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.late_arrivals.get_name_leafdata())
                    if (self.loss_period_count.is_set or self.loss_period_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loss_period_count.get_name_leafdata())
                    if (self.loss_period_len_max.is_set or self.loss_period_len_max.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loss_period_len_max.get_name_leafdata())
                    if (self.loss_period_len_min.is_set or self.loss_period_len_min.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.loss_period_len_min.get_name_leafdata())
                    if (self.out_of_sequence.is_set or self.out_of_sequence.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_sequence.get_name_leafdata())
                    if (self.out_of_sequence_both.is_set or self.out_of_sequence_both.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_sequence_both.get_name_leafdata())
                    if (self.out_of_sequence_ds.is_set or self.out_of_sequence_ds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_sequence_ds.get_name_leafdata())
                    if (self.out_of_sequence_sd.is_set or self.out_of_sequence_sd.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_of_sequence_sd.get_name_leafdata())
                    if (self.packet_loss.is_set or self.packet_loss.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packet_loss.get_name_leafdata())
                    if (self.skipped_packets.is_set or self.skipped_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.skipped_packets.get_name_leafdata())
                    if (self.unprocessed_packets.is_set or self.unprocessed_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unprocessed_packets.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "inter-loss-period-len-max" or name == "inter-loss-period-len-min" or name == "late-arrivals" or name == "loss-period-count" or name == "loss-period-len-max" or name == "loss-period-len-min" or name == "out-of-sequence" or name == "out-of-sequence-both" or name == "out-of-sequence-ds" or name == "out-of-sequence-sd" or name == "packet-loss" or name == "skipped-packets" or name == "unprocessed-packets"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "inter-loss-period-len-max"):
                        self.inter_loss_period_len_max = value
                        self.inter_loss_period_len_max.value_namespace = name_space
                        self.inter_loss_period_len_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "inter-loss-period-len-min"):
                        self.inter_loss_period_len_min = value
                        self.inter_loss_period_len_min.value_namespace = name_space
                        self.inter_loss_period_len_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "late-arrivals"):
                        self.late_arrivals = value
                        self.late_arrivals.value_namespace = name_space
                        self.late_arrivals.value_namespace_prefix = name_space_prefix
                    if(value_path == "loss-period-count"):
                        self.loss_period_count = value
                        self.loss_period_count.value_namespace = name_space
                        self.loss_period_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "loss-period-len-max"):
                        self.loss_period_len_max = value
                        self.loss_period_len_max.value_namespace = name_space
                        self.loss_period_len_max.value_namespace_prefix = name_space_prefix
                    if(value_path == "loss-period-len-min"):
                        self.loss_period_len_min = value
                        self.loss_period_len_min.value_namespace = name_space
                        self.loss_period_len_min.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-sequence"):
                        self.out_of_sequence = value
                        self.out_of_sequence.value_namespace = name_space
                        self.out_of_sequence.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-sequence-both"):
                        self.out_of_sequence_both = value
                        self.out_of_sequence_both.value_namespace = name_space
                        self.out_of_sequence_both.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-sequence-ds"):
                        self.out_of_sequence_ds = value
                        self.out_of_sequence_ds.value_namespace = name_space
                        self.out_of_sequence_ds.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-of-sequence-sd"):
                        self.out_of_sequence_sd = value
                        self.out_of_sequence_sd.value_namespace = name_space
                        self.out_of_sequence_sd.value_namespace_prefix = name_space_prefix
                    if(value_path == "packet-loss"):
                        self.packet_loss = value
                        self.packet_loss.value_namespace = name_space
                        self.packet_loss.value_namespace_prefix = name_space_prefix
                    if(value_path == "skipped-packets"):
                        self.skipped_packets = value
                        self.skipped_packets.value_namespace = name_space
                        self.skipped_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "unprocessed-packets"):
                        self.unprocessed_packets = value
                        self.unprocessed_packets.value_namespace = name_space
                        self.unprocessed_packets.value_namespace_prefix = name_space_prefix


            class VoiceScore(Entity):
                """
                Voice score information
                
                .. attribute:: icpif
                
                	Calculated planning impairment factor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mos
                
                	Mean opinion score
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-sla-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(IpSlaStats.SlaOperEntry.Stats.VoiceScore, self).__init__()

                    self.yang_name = "voice-score"
                    self.yang_parent_name = "stats"

                    self.icpif = YLeaf(YType.uint32, "icpif")

                    self.mos = YLeaf(YType.uint32, "mos")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("icpif",
                                    "mos") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpSlaStats.SlaOperEntry.Stats.VoiceScore, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpSlaStats.SlaOperEntry.Stats.VoiceScore, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.icpif.is_set or
                        self.mos.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.icpif.yfilter != YFilter.not_set or
                        self.mos.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "voice-score" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.icpif.is_set or self.icpif.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.icpif.get_name_leafdata())
                    if (self.mos.is_set or self.mos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mos.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "icpif" or name == "mos"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "icpif"):
                        self.icpif = value
                        self.icpif.value_namespace = name_space
                        self.icpif.value_namespace_prefix = name_space_prefix
                    if(value_path == "mos"):
                        self.mos = value
                        self.mos.value_namespace = name_space
                        self.mos.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    (self.icmp_packet_loss is not None and self.icmp_packet_loss.has_data()) or
                    (self.jitter is not None and self.jitter.has_data()) or
                    (self.oneway_latency is not None and self.oneway_latency.has_data()) or
                    (self.over_threshold is not None and self.over_threshold.has_data()) or
                    (self.packet_loss is not None and self.packet_loss.has_data()) or
                    (self.rtt is not None and self.rtt.has_data()) or
                    (self.voice_score is not None and self.voice_score.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.icmp_packet_loss is not None and self.icmp_packet_loss.has_operation()) or
                    (self.jitter is not None and self.jitter.has_operation()) or
                    (self.oneway_latency is not None and self.oneway_latency.has_operation()) or
                    (self.over_threshold is not None and self.over_threshold.has_operation()) or
                    (self.packet_loss is not None and self.packet_loss.has_operation()) or
                    (self.rtt is not None and self.rtt.has_operation()) or
                    (self.voice_score is not None and self.voice_score.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "stats" + path_buffer

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

                if (child_yang_name == "icmp-packet-loss"):
                    if (self.icmp_packet_loss is None):
                        self.icmp_packet_loss = IpSlaStats.SlaOperEntry.Stats.IcmpPacketLoss()
                        self.icmp_packet_loss.parent = self
                        self._children_name_map["icmp_packet_loss"] = "icmp-packet-loss"
                    return self.icmp_packet_loss

                if (child_yang_name == "jitter"):
                    if (self.jitter is None):
                        self.jitter = IpSlaStats.SlaOperEntry.Stats.Jitter()
                        self.jitter.parent = self
                        self._children_name_map["jitter"] = "jitter"
                    return self.jitter

                if (child_yang_name == "oneway-latency"):
                    if (self.oneway_latency is None):
                        self.oneway_latency = IpSlaStats.SlaOperEntry.Stats.OnewayLatency()
                        self.oneway_latency.parent = self
                        self._children_name_map["oneway_latency"] = "oneway-latency"
                    return self.oneway_latency

                if (child_yang_name == "over-threshold"):
                    if (self.over_threshold is None):
                        self.over_threshold = IpSlaStats.SlaOperEntry.Stats.OverThreshold()
                        self.over_threshold.parent = self
                        self._children_name_map["over_threshold"] = "over-threshold"
                    return self.over_threshold

                if (child_yang_name == "packet-loss"):
                    if (self.packet_loss is None):
                        self.packet_loss = IpSlaStats.SlaOperEntry.Stats.PacketLoss()
                        self.packet_loss.parent = self
                        self._children_name_map["packet_loss"] = "packet-loss"
                    return self.packet_loss

                if (child_yang_name == "rtt"):
                    if (self.rtt is None):
                        self.rtt = IpSlaStats.SlaOperEntry.Stats.Rtt()
                        self.rtt.parent = self
                        self._children_name_map["rtt"] = "rtt"
                    return self.rtt

                if (child_yang_name == "voice-score"):
                    if (self.voice_score is None):
                        self.voice_score = IpSlaStats.SlaOperEntry.Stats.VoiceScore()
                        self.voice_score.parent = self
                        self._children_name_map["voice_score"] = "voice-score"
                    return self.voice_score

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "icmp-packet-loss" or name == "jitter" or name == "oneway-latency" or name == "over-threshold" or name == "packet-loss" or name == "rtt" or name == "voice-score"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.oper_id.is_set or
                self.failure_count.is_set or
                self.latest_oper_start_time.is_set or
                self.latest_return_code.is_set or
                self.oper_type.is_set or
                self.success_count.is_set or
                (self.measure_stats is not None and self.measure_stats.has_data()) or
                (self.rtt_info is not None and self.rtt_info.has_data()) or
                (self.stats is not None and self.stats.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.oper_id.yfilter != YFilter.not_set or
                self.failure_count.yfilter != YFilter.not_set or
                self.latest_oper_start_time.yfilter != YFilter.not_set or
                self.latest_return_code.yfilter != YFilter.not_set or
                self.oper_type.yfilter != YFilter.not_set or
                self.success_count.yfilter != YFilter.not_set or
                (self.measure_stats is not None and self.measure_stats.has_operation()) or
                (self.rtt_info is not None and self.rtt_info.has_operation()) or
                (self.stats is not None and self.stats.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sla-oper-entry" + "[oper-id='" + self.oper_id.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-ip-sla-oper:ip-sla-stats/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.oper_id.is_set or self.oper_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.oper_id.get_name_leafdata())
            if (self.failure_count.is_set or self.failure_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.failure_count.get_name_leafdata())
            if (self.latest_oper_start_time.is_set or self.latest_oper_start_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.latest_oper_start_time.get_name_leafdata())
            if (self.latest_return_code.is_set or self.latest_return_code.yfilter != YFilter.not_set):
                leaf_name_data.append(self.latest_return_code.get_name_leafdata())
            if (self.oper_type.is_set or self.oper_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.oper_type.get_name_leafdata())
            if (self.success_count.is_set or self.success_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.success_count.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "measure-stats"):
                if (self.measure_stats is None):
                    self.measure_stats = IpSlaStats.SlaOperEntry.MeasureStats()
                    self.measure_stats.parent = self
                    self._children_name_map["measure_stats"] = "measure-stats"
                return self.measure_stats

            if (child_yang_name == "rtt-info"):
                if (self.rtt_info is None):
                    self.rtt_info = IpSlaStats.SlaOperEntry.RttInfo()
                    self.rtt_info.parent = self
                    self._children_name_map["rtt_info"] = "rtt-info"
                return self.rtt_info

            if (child_yang_name == "stats"):
                if (self.stats is None):
                    self.stats = IpSlaStats.SlaOperEntry.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                return self.stats

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "measure-stats" or name == "rtt-info" or name == "stats" or name == "oper-id" or name == "failure-count" or name == "latest-oper-start-time" or name == "latest-return-code" or name == "oper-type" or name == "success-count"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "oper-id"):
                self.oper_id = value
                self.oper_id.value_namespace = name_space
                self.oper_id.value_namespace_prefix = name_space_prefix
            if(value_path == "failure-count"):
                self.failure_count = value
                self.failure_count.value_namespace = name_space
                self.failure_count.value_namespace_prefix = name_space_prefix
            if(value_path == "latest-oper-start-time"):
                self.latest_oper_start_time = value
                self.latest_oper_start_time.value_namespace = name_space
                self.latest_oper_start_time.value_namespace_prefix = name_space_prefix
            if(value_path == "latest-return-code"):
                self.latest_return_code = value
                self.latest_return_code.value_namespace = name_space
                self.latest_return_code.value_namespace_prefix = name_space_prefix
            if(value_path == "oper-type"):
                self.oper_type = value
                self.oper_type.value_namespace = name_space
                self.oper_type.value_namespace_prefix = name_space_prefix
            if(value_path == "success-count"):
                self.success_count = value
                self.success_count.value_namespace = name_space
                self.success_count.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.sla_oper_entry:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.sla_oper_entry:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-ip-sla-oper:ip-sla-stats" + path_buffer

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

        if (child_yang_name == "sla-oper-entry"):
            for c in self.sla_oper_entry:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = IpSlaStats.SlaOperEntry()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.sla_oper_entry.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "sla-oper-entry"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpSlaStats()
        return self._top_entity

