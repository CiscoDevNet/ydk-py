""" Cisco_IOS_XR_infra_tc_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package configuration.

This module contains definitions
for the following management objects\:
  traffic\-collector\: Global Traffic Collector configuration
    commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CollectIonInterval(Enum):
    """
    CollectIonInterval

    Collect ion interval

    .. data:: Y_1_minute = 1

    	Interval1minute

    .. data:: Y_2_minutes = 2

    	Interval2minutes

    .. data:: Y_3_minutes = 3

    	Interval3minutes

    .. data:: Y_4_minutes = 4

    	Interval4minutes

    .. data:: Y_5_minutes = 5

    	Interval5minutes

    .. data:: Y_6_minutes = 6

    	Interval6minutes

    .. data:: Y_10_minutes = 10

    	Interval10minutes

    .. data:: Y_12_minutes = 12

    	Interval12minutes

    .. data:: Y_15_minutes = 15

    	Interval15inutes

    .. data:: Y_20_minutes = 20

    	Interval20minutes

    .. data:: Y_30_minutes = 30

    	Interval30minutes

    .. data:: Y_60_minutes = 60

    	Interval60minutes

    """

    Y_1_minute = Enum.YLeaf(1, "1-minute")

    Y_2_minutes = Enum.YLeaf(2, "2-minutes")

    Y_3_minutes = Enum.YLeaf(3, "3-minutes")

    Y_4_minutes = Enum.YLeaf(4, "4-minutes")

    Y_5_minutes = Enum.YLeaf(5, "5-minutes")

    Y_6_minutes = Enum.YLeaf(6, "6-minutes")

    Y_10_minutes = Enum.YLeaf(10, "10-minutes")

    Y_12_minutes = Enum.YLeaf(12, "12-minutes")

    Y_15_minutes = Enum.YLeaf(15, "15-minutes")

    Y_20_minutes = Enum.YLeaf(20, "20-minutes")

    Y_30_minutes = Enum.YLeaf(30, "30-minutes")

    Y_60_minutes = Enum.YLeaf(60, "60-minutes")


class HistorySize(Enum):
    """
    HistorySize

    History size

    .. data:: max = 10

    	Max history

    """

    max = Enum.YLeaf(10, "max")


class HistoryTimeout(Enum):
    """
    HistoryTimeout

    History timeout

    .. data:: max = 720

    	Max timeout

    """

    max = Enum.YLeaf(720, "max")



class TrafficCollector(Entity):
    """
    Global Traffic Collector configuration commands
    
    .. attribute:: enable_traffic_collector
    
    	Enable traffic collector
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: external_interfaces
    
    	Configure external interfaces
    	**type**\:   :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: statistics
    
    	Configure statistics related parameters
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.Statistics>`
    
    

    """

    _prefix = 'infra-tc-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(TrafficCollector, self).__init__()
        self._top_entity = None

        self.yang_name = "traffic-collector"
        self.yang_parent_name = "Cisco-IOS-XR-infra-tc-cfg"

        self.enable_traffic_collector = YLeaf(YType.empty, "enable-traffic-collector")

        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self._children_name_map["external_interfaces"] = "external-interfaces"
        self._children_yang_names.add("external-interfaces")

        self.statistics = TrafficCollector.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable_traffic_collector") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(TrafficCollector, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(TrafficCollector, self).__setattr__(name, value)


    class ExternalInterfaces(Entity):
        """
        Configure external interfaces
        
        .. attribute:: external_interface
        
        	Configure an external internface
        	**type**\: list of    :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.ExternalInterfaces, self).__init__()

            self.yang_name = "external-interfaces"
            self.yang_parent_name = "traffic-collector"

            self.external_interface = YList(self)

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
                        super(TrafficCollector.ExternalInterfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrafficCollector.ExternalInterfaces, self).__setattr__(name, value)


        class ExternalInterface(Entity):
            """
            Configure an external internface
            
            .. attribute:: interface_name  <key>
            
            	Name of interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: enable
            
            	Enable traffic collector on this interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-tc-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__init__()

                self.yang_name = "external-interface"
                self.yang_parent_name = "external-interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.enable = YLeaf(YType.empty, "enable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.enable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "external-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-cfg:traffic-collector/external-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.external_interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.external_interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "external-interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-tc-cfg:traffic-collector/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "external-interface"):
                for c in self.external_interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrafficCollector.ExternalInterfaces.ExternalInterface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.external_interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "external-interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Statistics(Entity):
        """
        Configure statistics related parameters
        
        .. attribute:: collection_interval
        
        	Configure statistics collection interval
        	**type**\:   :py:class:`CollectIonInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.CollectIonInterval>`
        
        .. attribute:: enable_traffic_collector_statistics
        
        	Enable traffic collector statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: history_size
        
        	Configure statistics history size
        	**type**\: one of the below types:
        
        	**type**\:   :py:class:`HistorySize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.HistorySize>`
        
        
        ----
        	**type**\:  int
        
        	**range:** 1..10
        
        
        ----
        .. attribute:: history_timeout
        
        	Configure statistics history timeout interval
        	**type**\: one of the below types:
        
        	**type**\:   :py:class:`HistoryTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_cfg.HistoryTimeout>`
        
        
        ----
        	**type**\:  int
        
        	**range:** 0..720
        
        
        ----
        

        """

        _prefix = 'infra-tc-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "traffic-collector"

            self.collection_interval = YLeaf(YType.enumeration, "collection-interval")

            self.enable_traffic_collector_statistics = YLeaf(YType.empty, "enable-traffic-collector-statistics")

            self.history_size = YLeaf(YType.str, "history-size")

            self.history_timeout = YLeaf(YType.str, "history-timeout")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("collection_interval",
                            "enable_traffic_collector_statistics",
                            "history_size",
                            "history_timeout") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(TrafficCollector.Statistics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrafficCollector.Statistics, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.collection_interval.is_set or
                self.enable_traffic_collector_statistics.is_set or
                self.history_size.is_set or
                self.history_timeout.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.collection_interval.yfilter != YFilter.not_set or
                self.enable_traffic_collector_statistics.yfilter != YFilter.not_set or
                self.history_size.yfilter != YFilter.not_set or
                self.history_timeout.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "statistics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-tc-cfg:traffic-collector/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.collection_interval.is_set or self.collection_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.collection_interval.get_name_leafdata())
            if (self.enable_traffic_collector_statistics.is_set or self.enable_traffic_collector_statistics.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable_traffic_collector_statistics.get_name_leafdata())
            if (self.history_size.is_set or self.history_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.history_size.get_name_leafdata())
            if (self.history_timeout.is_set or self.history_timeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.history_timeout.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "collection-interval" or name == "enable-traffic-collector-statistics" or name == "history-size" or name == "history-timeout"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "collection-interval"):
                self.collection_interval = value
                self.collection_interval.value_namespace = name_space
                self.collection_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "enable-traffic-collector-statistics"):
                self.enable_traffic_collector_statistics = value
                self.enable_traffic_collector_statistics.value_namespace = name_space
                self.enable_traffic_collector_statistics.value_namespace_prefix = name_space_prefix
            if(value_path == "history-size"):
                self.history_size = value
                self.history_size.value_namespace = name_space
                self.history_size.value_namespace_prefix = name_space_prefix
            if(value_path == "history-timeout"):
                self.history_timeout = value
                self.history_timeout.value_namespace = name_space
                self.history_timeout.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.enable_traffic_collector.is_set or
            (self.external_interfaces is not None and self.external_interfaces.has_data()) or
            (self.statistics is not None and self.statistics.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable_traffic_collector.yfilter != YFilter.not_set or
            (self.external_interfaces is not None and self.external_interfaces.has_operation()) or
            (self.statistics is not None and self.statistics.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-tc-cfg:traffic-collector" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable_traffic_collector.is_set or self.enable_traffic_collector.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable_traffic_collector.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "external-interfaces"):
            if (self.external_interfaces is None):
                self.external_interfaces = TrafficCollector.ExternalInterfaces()
                self.external_interfaces.parent = self
                self._children_name_map["external_interfaces"] = "external-interfaces"
            return self.external_interfaces

        if (child_yang_name == "statistics"):
            if (self.statistics is None):
                self.statistics = TrafficCollector.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
            return self.statistics

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "external-interfaces" or name == "statistics" or name == "enable-traffic-collector"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable-traffic-collector"):
            self.enable_traffic_collector = value
            self.enable_traffic_collector.value_namespace = name_space
            self.enable_traffic_collector.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = TrafficCollector()
        return self._top_entity

