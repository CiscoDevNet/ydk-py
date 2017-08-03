""" Cisco_IOS_XR_infra_tc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package operational data.

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


class TcOperAfName(Enum):
    """
    TcOperAfName

    Tc oper af name

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")



class TrafficCollector(Entity):
    """
    Global Traffic Collector configuration commands
    
    .. attribute:: afs
    
    	Address Family specific operational data
    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs>`
    
    .. attribute:: external_interfaces
    
    	External Interface
    	**type**\:   :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: summary
    
    	Traffic Collector summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary>`
    
    .. attribute:: vrf_table
    
    	VRF specific operational data
    	**type**\:   :py:class:`VrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable>`
    
    

    """

    _prefix = 'infra-tc-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(TrafficCollector, self).__init__()
        self._top_entity = None

        self.yang_name = "traffic-collector"
        self.yang_parent_name = "Cisco-IOS-XR-infra-tc-oper"

        self.afs = TrafficCollector.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"
        self._children_yang_names.add("afs")

        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self._children_name_map["external_interfaces"] = "external-interfaces"
        self._children_yang_names.add("external-interfaces")

        self.summary = TrafficCollector.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.vrf_table = TrafficCollector.VrfTable()
        self.vrf_table.parent = self
        self._children_name_map["vrf_table"] = "vrf-table"
        self._children_yang_names.add("vrf-table")


    class ExternalInterfaces(Entity):
        """
        External Interface
        
        .. attribute:: external_interface
        
        	External Interface 
        	**type**\: list of    :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-oper'
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
            External Interface 
            
            .. attribute:: interface_name  <key>
            
            	The Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name_xr
            
            	Interface name in Display format
            	**type**\:  str
            
            .. attribute:: is_interface_enabled
            
            	Flag to indicate interface enabled or not
            	**type**\:  bool
            
            .. attribute:: vrfid
            
            	Interface VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__init__()

                self.yang_name = "external-interface"
                self.yang_parent_name = "external-interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                self.is_interface_enabled = YLeaf(YType.boolean, "is-interface-enabled")

                self.vrfid = YLeaf(YType.uint32, "vrfid")

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
                                "interface_handle",
                                "interface_name_xr",
                                "is_interface_enabled",
                                "vrfid") and name in self.__dict__:
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
                    self.interface_handle.is_set or
                    self.interface_name_xr.is_set or
                    self.is_interface_enabled.is_set or
                    self.vrfid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.interface_handle.yfilter != YFilter.not_set or
                    self.interface_name_xr.yfilter != YFilter.not_set or
                    self.is_interface_enabled.yfilter != YFilter.not_set or
                    self.vrfid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "external-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/external-interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_handle.get_name_leafdata())
                if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                if (self.is_interface_enabled.is_set or self.is_interface_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_interface_enabled.get_name_leafdata())
                if (self.vrfid.is_set or self.vrfid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrfid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name" or name == "interface-handle" or name == "interface-name-xr" or name == "is-interface-enabled" or name == "vrfid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-handle"):
                    self.interface_handle = value
                    self.interface_handle.value_namespace = name_space
                    self.interface_handle.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name-xr"):
                    self.interface_name_xr = value
                    self.interface_name_xr.value_namespace = name_space
                    self.interface_name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "is-interface-enabled"):
                    self.is_interface_enabled = value
                    self.is_interface_enabled.value_namespace = name_space
                    self.is_interface_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "vrfid"):
                    self.vrfid = value
                    self.vrfid.value_namespace = name_space
                    self.vrfid.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self.get_segment_path()
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


    class Summary(Entity):
        """
        Traffic Collector summary
        
        .. attribute:: checkpoint_message_statistic
        
        	Statistics per message type for Chkpt
        	**type**\: list of    :py:class:`CheckpointMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CheckpointMessageStatistic>`
        
        .. attribute:: collection_interval
        
        	Statistic collection interval in minutes
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: minute
        
        .. attribute:: collection_message_statistic
        
        	Statistics per message type for STAT collector
        	**type**\: list of    :py:class:`CollectionMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CollectionMessageStatistic>`
        
        .. attribute:: collection_timer_is_running
        
        	TRUE if collection timer is running
        	**type**\:  bool
        
        .. attribute:: database_statistics_external_interface
        
        	Database statistics for External Interface
        	**type**\:   :py:class:`DatabaseStatisticsExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.DatabaseStatisticsExternalInterface>`
        
        .. attribute:: history_size
        
        	Statistics history size
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: timeout_interval
        
        	Statistic history timeout interval in hours
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**units**\: hour
        
        .. attribute:: timeout_timer_is_running
        
        	TRUE if history timeout timer is running
        	**type**\:  bool
        
        .. attribute:: vrf_statistic
        
        	VRF table statistics
        	**type**\: list of    :py:class:`VrfStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "traffic-collector"

            self.collection_interval = YLeaf(YType.uint8, "collection-interval")

            self.collection_timer_is_running = YLeaf(YType.boolean, "collection-timer-is-running")

            self.history_size = YLeaf(YType.uint8, "history-size")

            self.timeout_interval = YLeaf(YType.uint16, "timeout-interval")

            self.timeout_timer_is_running = YLeaf(YType.boolean, "timeout-timer-is-running")

            self.database_statistics_external_interface = TrafficCollector.Summary.DatabaseStatisticsExternalInterface()
            self.database_statistics_external_interface.parent = self
            self._children_name_map["database_statistics_external_interface"] = "database-statistics-external-interface"
            self._children_yang_names.add("database-statistics-external-interface")

            self.checkpoint_message_statistic = YList(self)
            self.collection_message_statistic = YList(self)
            self.vrf_statistic = YList(self)

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
                            "collection_timer_is_running",
                            "history_size",
                            "timeout_interval",
                            "timeout_timer_is_running") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(TrafficCollector.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrafficCollector.Summary, self).__setattr__(name, value)


        class DatabaseStatisticsExternalInterface(Entity):
            """
            Database statistics for External Interface
            
            .. attribute:: number_of_add_o_perations
            
            	Number of add operations
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_delete_o_perations
            
            	Number of delete operations
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_entries
            
            	Number of DB entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_stale_entries
            
            	Number of stale  entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, self).__init__()

                self.yang_name = "database-statistics-external-interface"
                self.yang_parent_name = "summary"

                self.number_of_add_o_perations = YLeaf(YType.uint64, "number-of-add-o-perations")

                self.number_of_delete_o_perations = YLeaf(YType.uint64, "number-of-delete-o-perations")

                self.number_of_entries = YLeaf(YType.uint32, "number-of-entries")

                self.number_of_stale_entries = YLeaf(YType.uint32, "number-of-stale-entries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("number_of_add_o_perations",
                                "number_of_delete_o_perations",
                                "number_of_entries",
                                "number_of_stale_entries") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.number_of_add_o_perations.is_set or
                    self.number_of_delete_o_perations.is_set or
                    self.number_of_entries.is_set or
                    self.number_of_stale_entries.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.number_of_add_o_perations.yfilter != YFilter.not_set or
                    self.number_of_delete_o_perations.yfilter != YFilter.not_set or
                    self.number_of_entries.yfilter != YFilter.not_set or
                    self.number_of_stale_entries.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "database-statistics-external-interface" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.number_of_add_o_perations.is_set or self.number_of_add_o_perations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_add_o_perations.get_name_leafdata())
                if (self.number_of_delete_o_perations.is_set or self.number_of_delete_o_perations.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_delete_o_perations.get_name_leafdata())
                if (self.number_of_entries.is_set or self.number_of_entries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_entries.get_name_leafdata())
                if (self.number_of_stale_entries.is_set or self.number_of_stale_entries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number_of_stale_entries.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "number-of-add-o-perations" or name == "number-of-delete-o-perations" or name == "number-of-entries" or name == "number-of-stale-entries"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "number-of-add-o-perations"):
                    self.number_of_add_o_perations = value
                    self.number_of_add_o_perations.value_namespace = name_space
                    self.number_of_add_o_perations.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-delete-o-perations"):
                    self.number_of_delete_o_perations = value
                    self.number_of_delete_o_perations.value_namespace = name_space
                    self.number_of_delete_o_perations.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-entries"):
                    self.number_of_entries = value
                    self.number_of_entries.value_namespace = name_space
                    self.number_of_entries.value_namespace_prefix = name_space_prefix
                if(value_path == "number-of-stale-entries"):
                    self.number_of_stale_entries = value
                    self.number_of_stale_entries.value_namespace = name_space
                    self.number_of_stale_entries.value_namespace_prefix = name_space_prefix


        class VrfStatistic(Entity):
            """
            VRF table statistics
            
            .. attribute:: database_statistics_ipv4
            
            	Database statistics for IPv4 table
            	**type**\:   :py:class:`DatabaseStatisticsIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4>`
            
            .. attribute:: database_statistics_tunnel
            
            	Database statistics for Tunnel table
            	**type**\:   :py:class:`DatabaseStatisticsTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.VrfStatistic, self).__init__()

                self.yang_name = "vrf-statistic"
                self.yang_parent_name = "summary"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.database_statistics_ipv4 = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4()
                self.database_statistics_ipv4.parent = self
                self._children_name_map["database_statistics_ipv4"] = "database-statistics-ipv4"
                self._children_yang_names.add("database-statistics-ipv4")

                self.database_statistics_tunnel = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel()
                self.database_statistics_tunnel.parent = self
                self._children_name_map["database_statistics_tunnel"] = "database-statistics-tunnel"
                self._children_yang_names.add("database-statistics-tunnel")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrafficCollector.Summary.VrfStatistic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrafficCollector.Summary.VrfStatistic, self).__setattr__(name, value)


            class DatabaseStatisticsIpv4(Entity):
                """
                Database statistics for IPv4 table
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, self).__init__()

                    self.yang_name = "database-statistics-ipv4"
                    self.yang_parent_name = "vrf-statistic"

                    self.number_of_add_o_perations = YLeaf(YType.uint64, "number-of-add-o-perations")

                    self.number_of_delete_o_perations = YLeaf(YType.uint64, "number-of-delete-o-perations")

                    self.number_of_entries = YLeaf(YType.uint32, "number-of-entries")

                    self.number_of_stale_entries = YLeaf(YType.uint32, "number-of-stale-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("number_of_add_o_perations",
                                    "number_of_delete_o_perations",
                                    "number_of_entries",
                                    "number_of_stale_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.number_of_add_o_perations.is_set or
                        self.number_of_delete_o_perations.is_set or
                        self.number_of_entries.is_set or
                        self.number_of_stale_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.number_of_add_o_perations.yfilter != YFilter.not_set or
                        self.number_of_delete_o_perations.yfilter != YFilter.not_set or
                        self.number_of_entries.yfilter != YFilter.not_set or
                        self.number_of_stale_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "database-statistics-ipv4" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/vrf-statistic/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.number_of_add_o_perations.is_set or self.number_of_add_o_perations.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_add_o_perations.get_name_leafdata())
                    if (self.number_of_delete_o_perations.is_set or self.number_of_delete_o_perations.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_delete_o_perations.get_name_leafdata())
                    if (self.number_of_entries.is_set or self.number_of_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_entries.get_name_leafdata())
                    if (self.number_of_stale_entries.is_set or self.number_of_stale_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_stale_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "number-of-add-o-perations" or name == "number-of-delete-o-perations" or name == "number-of-entries" or name == "number-of-stale-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "number-of-add-o-perations"):
                        self.number_of_add_o_perations = value
                        self.number_of_add_o_perations.value_namespace = name_space
                        self.number_of_add_o_perations.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-delete-o-perations"):
                        self.number_of_delete_o_perations = value
                        self.number_of_delete_o_perations.value_namespace = name_space
                        self.number_of_delete_o_perations.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-entries"):
                        self.number_of_entries = value
                        self.number_of_entries.value_namespace = name_space
                        self.number_of_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-stale-entries"):
                        self.number_of_stale_entries = value
                        self.number_of_stale_entries.value_namespace = name_space
                        self.number_of_stale_entries.value_namespace_prefix = name_space_prefix


            class DatabaseStatisticsTunnel(Entity):
                """
                Database statistics for Tunnel table
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, self).__init__()

                    self.yang_name = "database-statistics-tunnel"
                    self.yang_parent_name = "vrf-statistic"

                    self.number_of_add_o_perations = YLeaf(YType.uint64, "number-of-add-o-perations")

                    self.number_of_delete_o_perations = YLeaf(YType.uint64, "number-of-delete-o-perations")

                    self.number_of_entries = YLeaf(YType.uint32, "number-of-entries")

                    self.number_of_stale_entries = YLeaf(YType.uint32, "number-of-stale-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("number_of_add_o_perations",
                                    "number_of_delete_o_perations",
                                    "number_of_entries",
                                    "number_of_stale_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.number_of_add_o_perations.is_set or
                        self.number_of_delete_o_perations.is_set or
                        self.number_of_entries.is_set or
                        self.number_of_stale_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.number_of_add_o_perations.yfilter != YFilter.not_set or
                        self.number_of_delete_o_perations.yfilter != YFilter.not_set or
                        self.number_of_entries.yfilter != YFilter.not_set or
                        self.number_of_stale_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "database-statistics-tunnel" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/vrf-statistic/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.number_of_add_o_perations.is_set or self.number_of_add_o_perations.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_add_o_perations.get_name_leafdata())
                    if (self.number_of_delete_o_perations.is_set or self.number_of_delete_o_perations.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_delete_o_perations.get_name_leafdata())
                    if (self.number_of_entries.is_set or self.number_of_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_entries.get_name_leafdata())
                    if (self.number_of_stale_entries.is_set or self.number_of_stale_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.number_of_stale_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "number-of-add-o-perations" or name == "number-of-delete-o-perations" or name == "number-of-entries" or name == "number-of-stale-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "number-of-add-o-perations"):
                        self.number_of_add_o_perations = value
                        self.number_of_add_o_perations.value_namespace = name_space
                        self.number_of_add_o_perations.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-delete-o-perations"):
                        self.number_of_delete_o_perations = value
                        self.number_of_delete_o_perations.value_namespace = name_space
                        self.number_of_delete_o_perations.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-entries"):
                        self.number_of_entries = value
                        self.number_of_entries.value_namespace = name_space
                        self.number_of_entries.value_namespace_prefix = name_space_prefix
                    if(value_path == "number-of-stale-entries"):
                        self.number_of_stale_entries = value
                        self.number_of_stale_entries.value_namespace = name_space
                        self.number_of_stale_entries.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.database_statistics_ipv4 is not None and self.database_statistics_ipv4.has_data()) or
                    (self.database_statistics_tunnel is not None and self.database_statistics_tunnel.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.database_statistics_ipv4 is not None and self.database_statistics_ipv4.has_operation()) or
                    (self.database_statistics_tunnel is not None and self.database_statistics_tunnel.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf-statistic" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "database-statistics-ipv4"):
                    if (self.database_statistics_ipv4 is None):
                        self.database_statistics_ipv4 = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4()
                        self.database_statistics_ipv4.parent = self
                        self._children_name_map["database_statistics_ipv4"] = "database-statistics-ipv4"
                    return self.database_statistics_ipv4

                if (child_yang_name == "database-statistics-tunnel"):
                    if (self.database_statistics_tunnel is None):
                        self.database_statistics_tunnel = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel()
                        self.database_statistics_tunnel.parent = self
                        self._children_name_map["database_statistics_tunnel"] = "database-statistics-tunnel"
                    return self.database_statistics_tunnel

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "database-statistics-ipv4" or name == "database-statistics-tunnel" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix


        class CollectionMessageStatistic(Entity):
            """
            Statistics per message type for STAT collector
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.CollectionMessageStatistic, self).__init__()

                self.yang_name = "collection-message-statistic"
                self.yang_parent_name = "summary"

                self.byte_received = YLeaf(YType.uint64, "byte-received")

                self.byte_sent = YLeaf(YType.uint64, "byte-sent")

                self.maimum_latency_timestamp = YLeaf(YType.uint64, "maimum-latency-timestamp")

                self.maximum_roundtrip_latency = YLeaf(YType.uint32, "maximum-roundtrip-latency")

                self.packet_received = YLeaf(YType.uint64, "packet-received")

                self.packet_sent = YLeaf(YType.uint64, "packet-sent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("byte_received",
                                "byte_sent",
                                "maimum_latency_timestamp",
                                "maximum_roundtrip_latency",
                                "packet_received",
                                "packet_sent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrafficCollector.Summary.CollectionMessageStatistic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrafficCollector.Summary.CollectionMessageStatistic, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.byte_received.is_set or
                    self.byte_sent.is_set or
                    self.maimum_latency_timestamp.is_set or
                    self.maximum_roundtrip_latency.is_set or
                    self.packet_received.is_set or
                    self.packet_sent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.byte_received.yfilter != YFilter.not_set or
                    self.byte_sent.yfilter != YFilter.not_set or
                    self.maimum_latency_timestamp.yfilter != YFilter.not_set or
                    self.maximum_roundtrip_latency.yfilter != YFilter.not_set or
                    self.packet_received.yfilter != YFilter.not_set or
                    self.packet_sent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "collection-message-statistic" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.byte_received.is_set or self.byte_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.byte_received.get_name_leafdata())
                if (self.byte_sent.is_set or self.byte_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.byte_sent.get_name_leafdata())
                if (self.maimum_latency_timestamp.is_set or self.maimum_latency_timestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maimum_latency_timestamp.get_name_leafdata())
                if (self.maximum_roundtrip_latency.is_set or self.maximum_roundtrip_latency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_roundtrip_latency.get_name_leafdata())
                if (self.packet_received.is_set or self.packet_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.packet_received.get_name_leafdata())
                if (self.packet_sent.is_set or self.packet_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.packet_sent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "byte-received" or name == "byte-sent" or name == "maimum-latency-timestamp" or name == "maximum-roundtrip-latency" or name == "packet-received" or name == "packet-sent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "byte-received"):
                    self.byte_received = value
                    self.byte_received.value_namespace = name_space
                    self.byte_received.value_namespace_prefix = name_space_prefix
                if(value_path == "byte-sent"):
                    self.byte_sent = value
                    self.byte_sent.value_namespace = name_space
                    self.byte_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "maimum-latency-timestamp"):
                    self.maimum_latency_timestamp = value
                    self.maimum_latency_timestamp.value_namespace = name_space
                    self.maimum_latency_timestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-roundtrip-latency"):
                    self.maximum_roundtrip_latency = value
                    self.maximum_roundtrip_latency.value_namespace = name_space
                    self.maximum_roundtrip_latency.value_namespace_prefix = name_space_prefix
                if(value_path == "packet-received"):
                    self.packet_received = value
                    self.packet_received.value_namespace = name_space
                    self.packet_received.value_namespace_prefix = name_space_prefix
                if(value_path == "packet-sent"):
                    self.packet_sent = value
                    self.packet_sent.value_namespace = name_space
                    self.packet_sent.value_namespace_prefix = name_space_prefix


        class CheckpointMessageStatistic(Entity):
            """
            Statistics per message type for Chkpt
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.CheckpointMessageStatistic, self).__init__()

                self.yang_name = "checkpoint-message-statistic"
                self.yang_parent_name = "summary"

                self.byte_received = YLeaf(YType.uint64, "byte-received")

                self.byte_sent = YLeaf(YType.uint64, "byte-sent")

                self.maimum_latency_timestamp = YLeaf(YType.uint64, "maimum-latency-timestamp")

                self.maximum_roundtrip_latency = YLeaf(YType.uint32, "maximum-roundtrip-latency")

                self.packet_received = YLeaf(YType.uint64, "packet-received")

                self.packet_sent = YLeaf(YType.uint64, "packet-sent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("byte_received",
                                "byte_sent",
                                "maimum_latency_timestamp",
                                "maximum_roundtrip_latency",
                                "packet_received",
                                "packet_sent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrafficCollector.Summary.CheckpointMessageStatistic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrafficCollector.Summary.CheckpointMessageStatistic, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.byte_received.is_set or
                    self.byte_sent.is_set or
                    self.maimum_latency_timestamp.is_set or
                    self.maximum_roundtrip_latency.is_set or
                    self.packet_received.is_set or
                    self.packet_sent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.byte_received.yfilter != YFilter.not_set or
                    self.byte_sent.yfilter != YFilter.not_set or
                    self.maimum_latency_timestamp.yfilter != YFilter.not_set or
                    self.maximum_roundtrip_latency.yfilter != YFilter.not_set or
                    self.packet_received.yfilter != YFilter.not_set or
                    self.packet_sent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "checkpoint-message-statistic" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.byte_received.is_set or self.byte_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.byte_received.get_name_leafdata())
                if (self.byte_sent.is_set or self.byte_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.byte_sent.get_name_leafdata())
                if (self.maimum_latency_timestamp.is_set or self.maimum_latency_timestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maimum_latency_timestamp.get_name_leafdata())
                if (self.maximum_roundtrip_latency.is_set or self.maximum_roundtrip_latency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.maximum_roundtrip_latency.get_name_leafdata())
                if (self.packet_received.is_set or self.packet_received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.packet_received.get_name_leafdata())
                if (self.packet_sent.is_set or self.packet_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.packet_sent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "byte-received" or name == "byte-sent" or name == "maimum-latency-timestamp" or name == "maximum-roundtrip-latency" or name == "packet-received" or name == "packet-sent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "byte-received"):
                    self.byte_received = value
                    self.byte_received.value_namespace = name_space
                    self.byte_received.value_namespace_prefix = name_space_prefix
                if(value_path == "byte-sent"):
                    self.byte_sent = value
                    self.byte_sent.value_namespace = name_space
                    self.byte_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "maimum-latency-timestamp"):
                    self.maimum_latency_timestamp = value
                    self.maimum_latency_timestamp.value_namespace = name_space
                    self.maimum_latency_timestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "maximum-roundtrip-latency"):
                    self.maximum_roundtrip_latency = value
                    self.maximum_roundtrip_latency.value_namespace = name_space
                    self.maximum_roundtrip_latency.value_namespace_prefix = name_space_prefix
                if(value_path == "packet-received"):
                    self.packet_received = value
                    self.packet_received.value_namespace = name_space
                    self.packet_received.value_namespace_prefix = name_space_prefix
                if(value_path == "packet-sent"):
                    self.packet_sent = value
                    self.packet_sent.value_namespace = name_space
                    self.packet_sent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.checkpoint_message_statistic:
                if (c.has_data()):
                    return True
            for c in self.collection_message_statistic:
                if (c.has_data()):
                    return True
            for c in self.vrf_statistic:
                if (c.has_data()):
                    return True
            return (
                self.collection_interval.is_set or
                self.collection_timer_is_running.is_set or
                self.history_size.is_set or
                self.timeout_interval.is_set or
                self.timeout_timer_is_running.is_set or
                (self.database_statistics_external_interface is not None and self.database_statistics_external_interface.has_data()))

        def has_operation(self):
            for c in self.checkpoint_message_statistic:
                if (c.has_operation()):
                    return True
            for c in self.collection_message_statistic:
                if (c.has_operation()):
                    return True
            for c in self.vrf_statistic:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.collection_interval.yfilter != YFilter.not_set or
                self.collection_timer_is_running.yfilter != YFilter.not_set or
                self.history_size.yfilter != YFilter.not_set or
                self.timeout_interval.yfilter != YFilter.not_set or
                self.timeout_timer_is_running.yfilter != YFilter.not_set or
                (self.database_statistics_external_interface is not None and self.database_statistics_external_interface.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.collection_interval.is_set or self.collection_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.collection_interval.get_name_leafdata())
            if (self.collection_timer_is_running.is_set or self.collection_timer_is_running.yfilter != YFilter.not_set):
                leaf_name_data.append(self.collection_timer_is_running.get_name_leafdata())
            if (self.history_size.is_set or self.history_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.history_size.get_name_leafdata())
            if (self.timeout_interval.is_set or self.timeout_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout_interval.get_name_leafdata())
            if (self.timeout_timer_is_running.is_set or self.timeout_timer_is_running.yfilter != YFilter.not_set):
                leaf_name_data.append(self.timeout_timer_is_running.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "checkpoint-message-statistic"):
                for c in self.checkpoint_message_statistic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrafficCollector.Summary.CheckpointMessageStatistic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.checkpoint_message_statistic.append(c)
                return c

            if (child_yang_name == "collection-message-statistic"):
                for c in self.collection_message_statistic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrafficCollector.Summary.CollectionMessageStatistic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.collection_message_statistic.append(c)
                return c

            if (child_yang_name == "database-statistics-external-interface"):
                if (self.database_statistics_external_interface is None):
                    self.database_statistics_external_interface = TrafficCollector.Summary.DatabaseStatisticsExternalInterface()
                    self.database_statistics_external_interface.parent = self
                    self._children_name_map["database_statistics_external_interface"] = "database-statistics-external-interface"
                return self.database_statistics_external_interface

            if (child_yang_name == "vrf-statistic"):
                for c in self.vrf_statistic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrafficCollector.Summary.VrfStatistic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf_statistic.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "checkpoint-message-statistic" or name == "collection-message-statistic" or name == "database-statistics-external-interface" or name == "vrf-statistic" or name == "collection-interval" or name == "collection-timer-is-running" or name == "history-size" or name == "timeout-interval" or name == "timeout-timer-is-running"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "collection-interval"):
                self.collection_interval = value
                self.collection_interval.value_namespace = name_space
                self.collection_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "collection-timer-is-running"):
                self.collection_timer_is_running = value
                self.collection_timer_is_running.value_namespace = name_space
                self.collection_timer_is_running.value_namespace_prefix = name_space_prefix
            if(value_path == "history-size"):
                self.history_size = value
                self.history_size.value_namespace = name_space
                self.history_size.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout-interval"):
                self.timeout_interval = value
                self.timeout_interval.value_namespace = name_space
                self.timeout_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "timeout-timer-is-running"):
                self.timeout_timer_is_running = value
                self.timeout_timer_is_running.value_namespace = name_space
                self.timeout_timer_is_running.value_namespace_prefix = name_space_prefix


    class VrfTable(Entity):
        """
        VRF specific operational data
        
        .. attribute:: default_vrf
        
        	DefaultVRF specific operational data
        	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.VrfTable, self).__init__()

            self.yang_name = "vrf-table"
            self.yang_parent_name = "traffic-collector"

            self.default_vrf = TrafficCollector.VrfTable.DefaultVrf()
            self.default_vrf.parent = self
            self._children_name_map["default_vrf"] = "default-vrf"
            self._children_yang_names.add("default-vrf")


        class DefaultVrf(Entity):
            """
            DefaultVRF specific operational data
            
            .. attribute:: afs
            
            	Address Family specific operational data
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.VrfTable.DefaultVrf, self).__init__()

                self.yang_name = "default-vrf"
                self.yang_parent_name = "vrf-table"

                self.afs = TrafficCollector.VrfTable.DefaultVrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._children_yang_names.add("afs")


            class Afs(Entity):
                """
                Address Family specific operational data
                
                .. attribute:: af
                
                	Operational data for given Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.VrfTable.DefaultVrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "default-vrf"

                    self.af = YList(self)

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
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(TrafficCollector.VrfTable.DefaultVrf.Afs, self).__setattr__(name, value)


                class Af(Entity):
                    """
                    Operational data for given Address Family
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`TcOperAfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfName>`
                    
                    .. attribute:: counters
                    
                    	Show Counters
                    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.counters = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, self).__setattr__(name, value)


                    class Counters(Entity):
                        """
                        Show Counters
                        
                        .. attribute:: prefixes
                        
                        	Prefix Database
                        	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes>`
                        
                        .. attribute:: tunnels
                        
                        	Tunnels
                        	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "af"

                            self.prefixes = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes()
                            self.prefixes.parent = self
                            self._children_name_map["prefixes"] = "prefixes"
                            self._children_yang_names.add("prefixes")

                            self.tunnels = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels()
                            self.tunnels.parent = self
                            self._children_name_map["tunnels"] = "tunnels"
                            self._children_yang_names.add("tunnels")


                        class Prefixes(Entity):
                            """
                            Prefix Database
                            
                            .. attribute:: prefix
                            
                            	Show Prefix Counter
                            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, self).__init__()

                                self.yang_name = "prefixes"
                                self.yang_parent_name = "counters"

                                self.prefix = YList(self)

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
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, self).__setattr__(name, value)


                            class Prefix(Entity):
                                """
                                Show Prefix Counter
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                                
                                .. attribute:: ipaddr
                                
                                	IP Address
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: is_active
                                
                                	Prefix is Active and collecting new Statistics
                                	**type**\:  bool
                                
                                .. attribute:: label
                                
                                	Local Label
                                	**type**\:  int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: label_xr
                                
                                	Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mask
                                
                                	Prefix Mask
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: prefix
                                
                                	Prefix Address (V4 or V6 Format)
                                	**type**\:  str
                                
                                .. attribute:: traffic_matrix_counter_statistics
                                
                                	Traffic Matrix (TM) counter statistics
                                	**type**\:   :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "prefixes"

                                    self.ipaddr = YLeaf(YType.str, "ipaddr")

                                    self.is_active = YLeaf(YType.boolean, "is-active")

                                    self.label = YLeaf(YType.uint32, "label")

                                    self.label_xr = YLeaf(YType.uint32, "label-xr")

                                    self.mask = YLeaf(YType.str, "mask")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                    self._children_yang_names.add("base-counter-statistics")

                                    self.traffic_matrix_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                                    self.traffic_matrix_counter_statistics.parent = self
                                    self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                                    self._children_yang_names.add("traffic-matrix-counter-statistics")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ipaddr",
                                                    "is_active",
                                                    "label",
                                                    "label_xr",
                                                    "mask",
                                                    "prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, self).__setattr__(name, value)


                                class BaseCounterStatistics(Entity):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__init__()

                                        self.yang_name = "base-counter-statistics"
                                        self.yang_parent_name = "prefix"

                                        self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                        self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                        self.count_history = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("transmit_bytes_per_second_switched",
                                                        "transmit_packets_per_second_switched") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__setattr__(name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "base-counter-statistics"

                                            self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                            self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                            self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("event_end_timestamp",
                                                            "event_start_timestamp",
                                                            "is_valid",
                                                            "transmit_number_of_bytes_switched",
                                                            "transmit_number_of_packets_switched") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.event_end_timestamp.is_set or
                                                self.event_start_timestamp.is_set or
                                                self.is_valid.is_set or
                                                self.transmit_number_of_bytes_switched.is_set or
                                                self.transmit_number_of_packets_switched.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.event_end_timestamp.yfilter != YFilter.not_set or
                                                self.event_start_timestamp.yfilter != YFilter.not_set or
                                                self.is_valid.yfilter != YFilter.not_set or
                                                self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set or
                                                self.transmit_number_of_packets_switched.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "count-history" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.event_end_timestamp.is_set or self.event_end_timestamp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.event_end_timestamp.get_name_leafdata())
                                            if (self.event_start_timestamp.is_set or self.event_start_timestamp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.event_start_timestamp.get_name_leafdata())
                                            if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.is_valid.get_name_leafdata())
                                            if (self.transmit_number_of_bytes_switched.is_set or self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_number_of_bytes_switched.get_name_leafdata())
                                            if (self.transmit_number_of_packets_switched.is_set or self.transmit_number_of_packets_switched.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_number_of_packets_switched.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "event-end-timestamp" or name == "event-start-timestamp" or name == "is-valid" or name == "transmit-number-of-bytes-switched" or name == "transmit-number-of-packets-switched"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "event-end-timestamp"):
                                                self.event_end_timestamp = value
                                                self.event_end_timestamp.value_namespace = name_space
                                                self.event_end_timestamp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "event-start-timestamp"):
                                                self.event_start_timestamp = value
                                                self.event_start_timestamp.value_namespace = name_space
                                                self.event_start_timestamp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "is-valid"):
                                                self.is_valid = value
                                                self.is_valid.value_namespace = name_space
                                                self.is_valid.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-number-of-bytes-switched"):
                                                self.transmit_number_of_bytes_switched = value
                                                self.transmit_number_of_bytes_switched.value_namespace = name_space
                                                self.transmit_number_of_bytes_switched.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-number-of-packets-switched"):
                                                self.transmit_number_of_packets_switched = value
                                                self.transmit_number_of_packets_switched.value_namespace = name_space
                                                self.transmit_number_of_packets_switched.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.count_history:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.transmit_bytes_per_second_switched.is_set or
                                            self.transmit_packets_per_second_switched.is_set)

                                    def has_operation(self):
                                        for c in self.count_history:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set or
                                            self.transmit_packets_per_second_switched.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "base-counter-statistics" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.transmit_bytes_per_second_switched.is_set or self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transmit_bytes_per_second_switched.get_name_leafdata())
                                        if (self.transmit_packets_per_second_switched.is_set or self.transmit_packets_per_second_switched.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transmit_packets_per_second_switched.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "count-history"):
                                            for c in self.count_history:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.count_history.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "count-history" or name == "transmit-bytes-per-second-switched" or name == "transmit-packets-per-second-switched"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "transmit-bytes-per-second-switched"):
                                            self.transmit_bytes_per_second_switched = value
                                            self.transmit_bytes_per_second_switched.value_namespace = name_space
                                            self.transmit_bytes_per_second_switched.value_namespace_prefix = name_space_prefix
                                        if(value_path == "transmit-packets-per-second-switched"):
                                            self.transmit_packets_per_second_switched = value
                                            self.transmit_packets_per_second_switched.value_namespace = name_space
                                            self.transmit_packets_per_second_switched.value_namespace_prefix = name_space_prefix


                                class TrafficMatrixCounterStatistics(Entity):
                                    """
                                    Traffic Matrix (TM) counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__init__()

                                        self.yang_name = "traffic-matrix-counter-statistics"
                                        self.yang_parent_name = "prefix"

                                        self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                        self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                        self.count_history = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("transmit_bytes_per_second_switched",
                                                        "transmit_packets_per_second_switched") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__setattr__(name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "traffic-matrix-counter-statistics"

                                            self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                            self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                            self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("event_end_timestamp",
                                                            "event_start_timestamp",
                                                            "is_valid",
                                                            "transmit_number_of_bytes_switched",
                                                            "transmit_number_of_packets_switched") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.event_end_timestamp.is_set or
                                                self.event_start_timestamp.is_set or
                                                self.is_valid.is_set or
                                                self.transmit_number_of_bytes_switched.is_set or
                                                self.transmit_number_of_packets_switched.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.event_end_timestamp.yfilter != YFilter.not_set or
                                                self.event_start_timestamp.yfilter != YFilter.not_set or
                                                self.is_valid.yfilter != YFilter.not_set or
                                                self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set or
                                                self.transmit_number_of_packets_switched.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "count-history" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.event_end_timestamp.is_set or self.event_end_timestamp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.event_end_timestamp.get_name_leafdata())
                                            if (self.event_start_timestamp.is_set or self.event_start_timestamp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.event_start_timestamp.get_name_leafdata())
                                            if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.is_valid.get_name_leafdata())
                                            if (self.transmit_number_of_bytes_switched.is_set or self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_number_of_bytes_switched.get_name_leafdata())
                                            if (self.transmit_number_of_packets_switched.is_set or self.transmit_number_of_packets_switched.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_number_of_packets_switched.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "event-end-timestamp" or name == "event-start-timestamp" or name == "is-valid" or name == "transmit-number-of-bytes-switched" or name == "transmit-number-of-packets-switched"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "event-end-timestamp"):
                                                self.event_end_timestamp = value
                                                self.event_end_timestamp.value_namespace = name_space
                                                self.event_end_timestamp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "event-start-timestamp"):
                                                self.event_start_timestamp = value
                                                self.event_start_timestamp.value_namespace = name_space
                                                self.event_start_timestamp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "is-valid"):
                                                self.is_valid = value
                                                self.is_valid.value_namespace = name_space
                                                self.is_valid.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-number-of-bytes-switched"):
                                                self.transmit_number_of_bytes_switched = value
                                                self.transmit_number_of_bytes_switched.value_namespace = name_space
                                                self.transmit_number_of_bytes_switched.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-number-of-packets-switched"):
                                                self.transmit_number_of_packets_switched = value
                                                self.transmit_number_of_packets_switched.value_namespace = name_space
                                                self.transmit_number_of_packets_switched.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.count_history:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.transmit_bytes_per_second_switched.is_set or
                                            self.transmit_packets_per_second_switched.is_set)

                                    def has_operation(self):
                                        for c in self.count_history:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set or
                                            self.transmit_packets_per_second_switched.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "traffic-matrix-counter-statistics" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.transmit_bytes_per_second_switched.is_set or self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transmit_bytes_per_second_switched.get_name_leafdata())
                                        if (self.transmit_packets_per_second_switched.is_set or self.transmit_packets_per_second_switched.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transmit_packets_per_second_switched.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "count-history"):
                                            for c in self.count_history:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.count_history.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "count-history" or name == "transmit-bytes-per-second-switched" or name == "transmit-packets-per-second-switched"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "transmit-bytes-per-second-switched"):
                                            self.transmit_bytes_per_second_switched = value
                                            self.transmit_bytes_per_second_switched.value_namespace = name_space
                                            self.transmit_bytes_per_second_switched.value_namespace_prefix = name_space_prefix
                                        if(value_path == "transmit-packets-per-second-switched"):
                                            self.transmit_packets_per_second_switched = value
                                            self.transmit_packets_per_second_switched.value_namespace = name_space
                                            self.transmit_packets_per_second_switched.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.ipaddr.is_set or
                                        self.is_active.is_set or
                                        self.label.is_set or
                                        self.label_xr.is_set or
                                        self.mask.is_set or
                                        self.prefix.is_set or
                                        (self.base_counter_statistics is not None and self.base_counter_statistics.has_data()) or
                                        (self.traffic_matrix_counter_statistics is not None and self.traffic_matrix_counter_statistics.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ipaddr.yfilter != YFilter.not_set or
                                        self.is_active.yfilter != YFilter.not_set or
                                        self.label.yfilter != YFilter.not_set or
                                        self.label_xr.yfilter != YFilter.not_set or
                                        self.mask.yfilter != YFilter.not_set or
                                        self.prefix.yfilter != YFilter.not_set or
                                        (self.base_counter_statistics is not None and self.base_counter_statistics.has_operation()) or
                                        (self.traffic_matrix_counter_statistics is not None and self.traffic_matrix_counter_statistics.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "prefix" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ipaddr.is_set or self.ipaddr.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipaddr.get_name_leafdata())
                                    if (self.is_active.is_set or self.is_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_active.get_name_leafdata())
                                    if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label.get_name_leafdata())
                                    if (self.label_xr.is_set or self.label_xr.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label_xr.get_name_leafdata())
                                    if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mask.get_name_leafdata())
                                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "base-counter-statistics"):
                                        if (self.base_counter_statistics is None):
                                            self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                                            self.base_counter_statistics.parent = self
                                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                        return self.base_counter_statistics

                                    if (child_yang_name == "traffic-matrix-counter-statistics"):
                                        if (self.traffic_matrix_counter_statistics is None):
                                            self.traffic_matrix_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                                            self.traffic_matrix_counter_statistics.parent = self
                                            self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                                        return self.traffic_matrix_counter_statistics

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "base-counter-statistics" or name == "traffic-matrix-counter-statistics" or name == "ipaddr" or name == "is-active" or name == "label" or name == "label-xr" or name == "mask" or name == "prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ipaddr"):
                                        self.ipaddr = value
                                        self.ipaddr.value_namespace = name_space
                                        self.ipaddr.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-active"):
                                        self.is_active = value
                                        self.is_active.value_namespace = name_space
                                        self.is_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "label"):
                                        self.label = value
                                        self.label.value_namespace = name_space
                                        self.label.value_namespace_prefix = name_space_prefix
                                    if(value_path == "label-xr"):
                                        self.label_xr = value
                                        self.label_xr.value_namespace = name_space
                                        self.label_xr.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mask"):
                                        self.mask = value
                                        self.mask.value_namespace = name_space
                                        self.mask.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix"):
                                        self.prefix = value
                                        self.prefix.value_namespace = name_space
                                        self.prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.prefix:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.prefix:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefixes" + path_buffer

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

                                if (child_yang_name == "prefix"):
                                    for c in self.prefix:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.prefix.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "prefix"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Tunnels(Entity):
                            """
                            Tunnels
                            
                            .. attribute:: tunnel
                            
                            	Tunnel information
                            	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, self).__init__()

                                self.yang_name = "tunnels"
                                self.yang_parent_name = "counters"

                                self.tunnel = YList(self)

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
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, self).__setattr__(name, value)


                            class Tunnel(Entity):
                                """
                                Tunnel information
                                
                                .. attribute:: interface_name  <key>
                                
                                	The Interface Name
                                	**type**\:  str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                                
                                .. attribute:: interface_handle
                                
                                	Interface handle
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name_xr
                                
                                	Interface name in Display format
                                	**type**\:  str
                                
                                .. attribute:: is_active
                                
                                	Interface is Active and collecting new Statistics
                                	**type**\:  bool
                                
                                .. attribute:: vrfid
                                
                                	Interface VRF ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, self).__init__()

                                    self.yang_name = "tunnel"
                                    self.yang_parent_name = "tunnels"

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                                    self.is_active = YLeaf(YType.boolean, "is-active")

                                    self.vrfid = YLeaf(YType.uint32, "vrfid")

                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                    self._children_yang_names.add("base-counter-statistics")

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
                                                    "interface_handle",
                                                    "interface_name_xr",
                                                    "is_active",
                                                    "vrfid") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, self).__setattr__(name, value)


                                class BaseCounterStatistics(Entity):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__init__()

                                        self.yang_name = "base-counter-statistics"
                                        self.yang_parent_name = "tunnel"

                                        self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                        self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                        self.count_history = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("transmit_bytes_per_second_switched",
                                                        "transmit_packets_per_second_switched") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__setattr__(name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "base-counter-statistics"

                                            self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                            self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                            self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("event_end_timestamp",
                                                            "event_start_timestamp",
                                                            "is_valid",
                                                            "transmit_number_of_bytes_switched",
                                                            "transmit_number_of_packets_switched") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.event_end_timestamp.is_set or
                                                self.event_start_timestamp.is_set or
                                                self.is_valid.is_set or
                                                self.transmit_number_of_bytes_switched.is_set or
                                                self.transmit_number_of_packets_switched.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.event_end_timestamp.yfilter != YFilter.not_set or
                                                self.event_start_timestamp.yfilter != YFilter.not_set or
                                                self.is_valid.yfilter != YFilter.not_set or
                                                self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set or
                                                self.transmit_number_of_packets_switched.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "count-history" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.event_end_timestamp.is_set or self.event_end_timestamp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.event_end_timestamp.get_name_leafdata())
                                            if (self.event_start_timestamp.is_set or self.event_start_timestamp.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.event_start_timestamp.get_name_leafdata())
                                            if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.is_valid.get_name_leafdata())
                                            if (self.transmit_number_of_bytes_switched.is_set or self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_number_of_bytes_switched.get_name_leafdata())
                                            if (self.transmit_number_of_packets_switched.is_set or self.transmit_number_of_packets_switched.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.transmit_number_of_packets_switched.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "event-end-timestamp" or name == "event-start-timestamp" or name == "is-valid" or name == "transmit-number-of-bytes-switched" or name == "transmit-number-of-packets-switched"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "event-end-timestamp"):
                                                self.event_end_timestamp = value
                                                self.event_end_timestamp.value_namespace = name_space
                                                self.event_end_timestamp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "event-start-timestamp"):
                                                self.event_start_timestamp = value
                                                self.event_start_timestamp.value_namespace = name_space
                                                self.event_start_timestamp.value_namespace_prefix = name_space_prefix
                                            if(value_path == "is-valid"):
                                                self.is_valid = value
                                                self.is_valid.value_namespace = name_space
                                                self.is_valid.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-number-of-bytes-switched"):
                                                self.transmit_number_of_bytes_switched = value
                                                self.transmit_number_of_bytes_switched.value_namespace = name_space
                                                self.transmit_number_of_bytes_switched.value_namespace_prefix = name_space_prefix
                                            if(value_path == "transmit-number-of-packets-switched"):
                                                self.transmit_number_of_packets_switched = value
                                                self.transmit_number_of_packets_switched.value_namespace = name_space
                                                self.transmit_number_of_packets_switched.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.count_history:
                                            if (c.has_data()):
                                                return True
                                        return (
                                            self.transmit_bytes_per_second_switched.is_set or
                                            self.transmit_packets_per_second_switched.is_set)

                                    def has_operation(self):
                                        for c in self.count_history:
                                            if (c.has_operation()):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set or
                                            self.transmit_packets_per_second_switched.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "base-counter-statistics" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.transmit_bytes_per_second_switched.is_set or self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transmit_bytes_per_second_switched.get_name_leafdata())
                                        if (self.transmit_packets_per_second_switched.is_set or self.transmit_packets_per_second_switched.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.transmit_packets_per_second_switched.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "count-history"):
                                            for c in self.count_history:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.count_history.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "count-history" or name == "transmit-bytes-per-second-switched" or name == "transmit-packets-per-second-switched"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "transmit-bytes-per-second-switched"):
                                            self.transmit_bytes_per_second_switched = value
                                            self.transmit_bytes_per_second_switched.value_namespace = name_space
                                            self.transmit_bytes_per_second_switched.value_namespace_prefix = name_space_prefix
                                        if(value_path == "transmit-packets-per-second-switched"):
                                            self.transmit_packets_per_second_switched = value
                                            self.transmit_packets_per_second_switched.value_namespace = name_space
                                            self.transmit_packets_per_second_switched.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.interface_name.is_set or
                                        self.interface_handle.is_set or
                                        self.interface_name_xr.is_set or
                                        self.is_active.is_set or
                                        self.vrfid.is_set or
                                        (self.base_counter_statistics is not None and self.base_counter_statistics.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.interface_handle.yfilter != YFilter.not_set or
                                        self.interface_name_xr.yfilter != YFilter.not_set or
                                        self.is_active.yfilter != YFilter.not_set or
                                        self.vrfid.yfilter != YFilter.not_set or
                                        (self.base_counter_statistics is not None and self.base_counter_statistics.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "tunnel" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_handle.get_name_leafdata())
                                    if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                                    if (self.is_active.is_set or self.is_active.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_active.get_name_leafdata())
                                    if (self.vrfid.is_set or self.vrfid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrfid.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "base-counter-statistics"):
                                        if (self.base_counter_statistics is None):
                                            self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                                            self.base_counter_statistics.parent = self
                                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                        return self.base_counter_statistics

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "base-counter-statistics" or name == "interface-name" or name == "interface-handle" or name == "interface-name-xr" or name == "is-active" or name == "vrfid"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-handle"):
                                        self.interface_handle = value
                                        self.interface_handle.value_namespace = name_space
                                        self.interface_handle.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name-xr"):
                                        self.interface_name_xr = value
                                        self.interface_name_xr.value_namespace = name_space
                                        self.interface_name_xr.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-active"):
                                        self.is_active = value
                                        self.is_active.value_namespace = name_space
                                        self.is_active.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrfid"):
                                        self.vrfid = value
                                        self.vrfid.value_namespace = name_space
                                        self.vrfid.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.tunnel:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.tunnel:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "tunnels" + path_buffer

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

                                if (child_yang_name == "tunnel"):
                                    for c in self.tunnel:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.tunnel.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "tunnel"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                (self.prefixes is not None and self.prefixes.has_data()) or
                                (self.tunnels is not None and self.tunnels.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.prefixes is not None and self.prefixes.has_operation()) or
                                (self.tunnels is not None and self.tunnels.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "counters" + path_buffer

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

                            if (child_yang_name == "prefixes"):
                                if (self.prefixes is None):
                                    self.prefixes = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes()
                                    self.prefixes.parent = self
                                    self._children_name_map["prefixes"] = "prefixes"
                                return self.prefixes

                            if (child_yang_name == "tunnels"):
                                if (self.tunnels is None):
                                    self.tunnels = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels()
                                    self.tunnels.parent = self
                                    self._children_name_map["tunnels"] = "tunnels"
                                return self.tunnels

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prefixes" or name == "tunnels"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.af_name.is_set or
                            (self.counters is not None and self.counters.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            (self.counters is not None and self.counters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/default-vrf/afs/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "counters"):
                            if (self.counters is None):
                                self.counters = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters()
                                self.counters.parent = self
                                self._children_name_map["counters"] = "counters"
                            return self.counters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "counters" or name == "af-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.af:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.af:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "afs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/default-vrf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "af"):
                        for c in self.af:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = TrafficCollector.VrfTable.DefaultVrf.Afs.Af()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.af.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "af"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.afs is not None and self.afs.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.afs is not None and self.afs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default-vrf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "afs"):
                    if (self.afs is None):
                        self.afs = TrafficCollector.VrfTable.DefaultVrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                    return self.afs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "afs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.default_vrf is not None and self.default_vrf.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.default_vrf is not None and self.default_vrf.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrf-table" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "default-vrf"):
                if (self.default_vrf is None):
                    self.default_vrf = TrafficCollector.VrfTable.DefaultVrf()
                    self.default_vrf.parent = self
                    self._children_name_map["default_vrf"] = "default-vrf"
                return self.default_vrf

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "default-vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Afs(Entity):
        """
        Address Family specific operational data
        
        .. attribute:: af
        
        	Operational data for given Address Family
        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "traffic-collector"

            self.af = YList(self)

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
                        super(TrafficCollector.Afs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TrafficCollector.Afs, self).__setattr__(name, value)


        class Af(Entity):
            """
            Operational data for given Address Family
            
            .. attribute:: af_name  <key>
            
            	Address Family name
            	**type**\:   :py:class:`TcOperAfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfName>`
            
            .. attribute:: counters
            
            	Show Counters
            	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"

                self.af_name = YLeaf(YType.enumeration, "af-name")

                self.counters = TrafficCollector.Afs.Af.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"
                self._children_yang_names.add("counters")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("af_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TrafficCollector.Afs.Af, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TrafficCollector.Afs.Af, self).__setattr__(name, value)


            class Counters(Entity):
                """
                Show Counters
                
                .. attribute:: prefixes
                
                	Prefix Database
                	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes>`
                
                .. attribute:: tunnels
                
                	Tunnels
                	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Afs.Af.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "af"

                    self.prefixes = TrafficCollector.Afs.Af.Counters.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"
                    self._children_yang_names.add("prefixes")

                    self.tunnels = TrafficCollector.Afs.Af.Counters.Tunnels()
                    self.tunnels.parent = self
                    self._children_name_map["tunnels"] = "tunnels"
                    self._children_yang_names.add("tunnels")


                class Prefixes(Entity):
                    """
                    Prefix Database
                    
                    .. attribute:: prefix
                    
                    	Show Prefix Counter
                    	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.Afs.Af.Counters.Prefixes, self).__init__()

                        self.yang_name = "prefixes"
                        self.yang_parent_name = "counters"

                        self.prefix = YList(self)

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
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TrafficCollector.Afs.Af.Counters.Prefixes, self).__setattr__(name, value)


                    class Prefix(Entity):
                        """
                        Show Prefix Counter
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                        
                        .. attribute:: ipaddr
                        
                        	IP Address
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: is_active
                        
                        	Prefix is Active and collecting new Statistics
                        	**type**\:  bool
                        
                        .. attribute:: label
                        
                        	Local Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_xr
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask
                        
                        	Prefix Mask
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: prefix
                        
                        	Prefix Address (V4 or V6 Format)
                        	**type**\:  str
                        
                        .. attribute:: traffic_matrix_counter_statistics
                        
                        	Traffic Matrix (TM) counter statistics
                        	**type**\:   :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "prefixes"

                            self.ipaddr = YLeaf(YType.str, "ipaddr")

                            self.is_active = YLeaf(YType.boolean, "is-active")

                            self.label = YLeaf(YType.uint32, "label")

                            self.label_xr = YLeaf(YType.uint32, "label-xr")

                            self.mask = YLeaf(YType.str, "mask")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                            self._children_yang_names.add("base-counter-statistics")

                            self.traffic_matrix_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                            self.traffic_matrix_counter_statistics.parent = self
                            self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                            self._children_yang_names.add("traffic-matrix-counter-statistics")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipaddr",
                                            "is_active",
                                            "label",
                                            "label_xr",
                                            "mask",
                                            "prefix") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, self).__setattr__(name, value)


                        class BaseCounterStatistics(Entity):
                            """
                            Base counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__init__()

                                self.yang_name = "base-counter-statistics"
                                self.yang_parent_name = "prefix"

                                self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                self.count_history = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("transmit_bytes_per_second_switched",
                                                "transmit_packets_per_second_switched") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__setattr__(name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "base-counter-statistics"

                                    self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                    self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                    self.is_valid = YLeaf(YType.boolean, "is-valid")

                                    self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                    self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("event_end_timestamp",
                                                    "event_start_timestamp",
                                                    "is_valid",
                                                    "transmit_number_of_bytes_switched",
                                                    "transmit_number_of_packets_switched") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.event_end_timestamp.is_set or
                                        self.event_start_timestamp.is_set or
                                        self.is_valid.is_set or
                                        self.transmit_number_of_bytes_switched.is_set or
                                        self.transmit_number_of_packets_switched.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.event_end_timestamp.yfilter != YFilter.not_set or
                                        self.event_start_timestamp.yfilter != YFilter.not_set or
                                        self.is_valid.yfilter != YFilter.not_set or
                                        self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set or
                                        self.transmit_number_of_packets_switched.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "count-history" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.event_end_timestamp.is_set or self.event_end_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.event_end_timestamp.get_name_leafdata())
                                    if (self.event_start_timestamp.is_set or self.event_start_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.event_start_timestamp.get_name_leafdata())
                                    if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_valid.get_name_leafdata())
                                    if (self.transmit_number_of_bytes_switched.is_set or self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.transmit_number_of_bytes_switched.get_name_leafdata())
                                    if (self.transmit_number_of_packets_switched.is_set or self.transmit_number_of_packets_switched.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.transmit_number_of_packets_switched.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "event-end-timestamp" or name == "event-start-timestamp" or name == "is-valid" or name == "transmit-number-of-bytes-switched" or name == "transmit-number-of-packets-switched"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "event-end-timestamp"):
                                        self.event_end_timestamp = value
                                        self.event_end_timestamp.value_namespace = name_space
                                        self.event_end_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "event-start-timestamp"):
                                        self.event_start_timestamp = value
                                        self.event_start_timestamp.value_namespace = name_space
                                        self.event_start_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-valid"):
                                        self.is_valid = value
                                        self.is_valid.value_namespace = name_space
                                        self.is_valid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "transmit-number-of-bytes-switched"):
                                        self.transmit_number_of_bytes_switched = value
                                        self.transmit_number_of_bytes_switched.value_namespace = name_space
                                        self.transmit_number_of_bytes_switched.value_namespace_prefix = name_space_prefix
                                    if(value_path == "transmit-number-of-packets-switched"):
                                        self.transmit_number_of_packets_switched = value
                                        self.transmit_number_of_packets_switched.value_namespace = name_space
                                        self.transmit_number_of_packets_switched.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.count_history:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.transmit_bytes_per_second_switched.is_set or
                                    self.transmit_packets_per_second_switched.is_set)

                            def has_operation(self):
                                for c in self.count_history:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set or
                                    self.transmit_packets_per_second_switched.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "base-counter-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.transmit_bytes_per_second_switched.is_set or self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_bytes_per_second_switched.get_name_leafdata())
                                if (self.transmit_packets_per_second_switched.is_set or self.transmit_packets_per_second_switched.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_packets_per_second_switched.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "count-history"):
                                    for c in self.count_history:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.count_history.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "count-history" or name == "transmit-bytes-per-second-switched" or name == "transmit-packets-per-second-switched"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "transmit-bytes-per-second-switched"):
                                    self.transmit_bytes_per_second_switched = value
                                    self.transmit_bytes_per_second_switched.value_namespace = name_space
                                    self.transmit_bytes_per_second_switched.value_namespace_prefix = name_space_prefix
                                if(value_path == "transmit-packets-per-second-switched"):
                                    self.transmit_packets_per_second_switched = value
                                    self.transmit_packets_per_second_switched.value_namespace = name_space
                                    self.transmit_packets_per_second_switched.value_namespace_prefix = name_space_prefix


                        class TrafficMatrixCounterStatistics(Entity):
                            """
                            Traffic Matrix (TM) counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__init__()

                                self.yang_name = "traffic-matrix-counter-statistics"
                                self.yang_parent_name = "prefix"

                                self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                self.count_history = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("transmit_bytes_per_second_switched",
                                                "transmit_packets_per_second_switched") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__setattr__(name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "traffic-matrix-counter-statistics"

                                    self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                    self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                    self.is_valid = YLeaf(YType.boolean, "is-valid")

                                    self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                    self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("event_end_timestamp",
                                                    "event_start_timestamp",
                                                    "is_valid",
                                                    "transmit_number_of_bytes_switched",
                                                    "transmit_number_of_packets_switched") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.event_end_timestamp.is_set or
                                        self.event_start_timestamp.is_set or
                                        self.is_valid.is_set or
                                        self.transmit_number_of_bytes_switched.is_set or
                                        self.transmit_number_of_packets_switched.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.event_end_timestamp.yfilter != YFilter.not_set or
                                        self.event_start_timestamp.yfilter != YFilter.not_set or
                                        self.is_valid.yfilter != YFilter.not_set or
                                        self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set or
                                        self.transmit_number_of_packets_switched.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "count-history" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.event_end_timestamp.is_set or self.event_end_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.event_end_timestamp.get_name_leafdata())
                                    if (self.event_start_timestamp.is_set or self.event_start_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.event_start_timestamp.get_name_leafdata())
                                    if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_valid.get_name_leafdata())
                                    if (self.transmit_number_of_bytes_switched.is_set or self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.transmit_number_of_bytes_switched.get_name_leafdata())
                                    if (self.transmit_number_of_packets_switched.is_set or self.transmit_number_of_packets_switched.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.transmit_number_of_packets_switched.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "event-end-timestamp" or name == "event-start-timestamp" or name == "is-valid" or name == "transmit-number-of-bytes-switched" or name == "transmit-number-of-packets-switched"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "event-end-timestamp"):
                                        self.event_end_timestamp = value
                                        self.event_end_timestamp.value_namespace = name_space
                                        self.event_end_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "event-start-timestamp"):
                                        self.event_start_timestamp = value
                                        self.event_start_timestamp.value_namespace = name_space
                                        self.event_start_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-valid"):
                                        self.is_valid = value
                                        self.is_valid.value_namespace = name_space
                                        self.is_valid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "transmit-number-of-bytes-switched"):
                                        self.transmit_number_of_bytes_switched = value
                                        self.transmit_number_of_bytes_switched.value_namespace = name_space
                                        self.transmit_number_of_bytes_switched.value_namespace_prefix = name_space_prefix
                                    if(value_path == "transmit-number-of-packets-switched"):
                                        self.transmit_number_of_packets_switched = value
                                        self.transmit_number_of_packets_switched.value_namespace = name_space
                                        self.transmit_number_of_packets_switched.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.count_history:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.transmit_bytes_per_second_switched.is_set or
                                    self.transmit_packets_per_second_switched.is_set)

                            def has_operation(self):
                                for c in self.count_history:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set or
                                    self.transmit_packets_per_second_switched.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "traffic-matrix-counter-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.transmit_bytes_per_second_switched.is_set or self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_bytes_per_second_switched.get_name_leafdata())
                                if (self.transmit_packets_per_second_switched.is_set or self.transmit_packets_per_second_switched.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_packets_per_second_switched.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "count-history"):
                                    for c in self.count_history:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.count_history.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "count-history" or name == "transmit-bytes-per-second-switched" or name == "transmit-packets-per-second-switched"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "transmit-bytes-per-second-switched"):
                                    self.transmit_bytes_per_second_switched = value
                                    self.transmit_bytes_per_second_switched.value_namespace = name_space
                                    self.transmit_bytes_per_second_switched.value_namespace_prefix = name_space_prefix
                                if(value_path == "transmit-packets-per-second-switched"):
                                    self.transmit_packets_per_second_switched = value
                                    self.transmit_packets_per_second_switched.value_namespace = name_space
                                    self.transmit_packets_per_second_switched.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.ipaddr.is_set or
                                self.is_active.is_set or
                                self.label.is_set or
                                self.label_xr.is_set or
                                self.mask.is_set or
                                self.prefix.is_set or
                                (self.base_counter_statistics is not None and self.base_counter_statistics.has_data()) or
                                (self.traffic_matrix_counter_statistics is not None and self.traffic_matrix_counter_statistics.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipaddr.yfilter != YFilter.not_set or
                                self.is_active.yfilter != YFilter.not_set or
                                self.label.yfilter != YFilter.not_set or
                                self.label_xr.yfilter != YFilter.not_set or
                                self.mask.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                (self.base_counter_statistics is not None and self.base_counter_statistics.has_operation()) or
                                (self.traffic_matrix_counter_statistics is not None and self.traffic_matrix_counter_statistics.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prefix" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipaddr.is_set or self.ipaddr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipaddr.get_name_leafdata())
                            if (self.is_active.is_set or self.is_active.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_active.get_name_leafdata())
                            if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label.get_name_leafdata())
                            if (self.label_xr.is_set or self.label_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_xr.get_name_leafdata())
                            if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mask.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "base-counter-statistics"):
                                if (self.base_counter_statistics is None):
                                    self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                return self.base_counter_statistics

                            if (child_yang_name == "traffic-matrix-counter-statistics"):
                                if (self.traffic_matrix_counter_statistics is None):
                                    self.traffic_matrix_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                                    self.traffic_matrix_counter_statistics.parent = self
                                    self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                                return self.traffic_matrix_counter_statistics

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "base-counter-statistics" or name == "traffic-matrix-counter-statistics" or name == "ipaddr" or name == "is-active" or name == "label" or name == "label-xr" or name == "mask" or name == "prefix"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipaddr"):
                                self.ipaddr = value
                                self.ipaddr.value_namespace = name_space
                                self.ipaddr.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-active"):
                                self.is_active = value
                                self.is_active.value_namespace = name_space
                                self.is_active.value_namespace_prefix = name_space_prefix
                            if(value_path == "label"):
                                self.label = value
                                self.label.value_namespace = name_space
                                self.label.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-xr"):
                                self.label_xr = value
                                self.label_xr.value_namespace = name_space
                                self.label_xr.value_namespace_prefix = name_space_prefix
                            if(value_path == "mask"):
                                self.mask = value
                                self.mask.value_namespace = name_space
                                self.mask.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.prefix:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.prefix:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prefixes" + path_buffer

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

                        if (child_yang_name == "prefix"):
                            for c in self.prefix:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.prefix.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "prefix"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Tunnels(Entity):
                    """
                    Tunnels
                    
                    .. attribute:: tunnel
                    
                    	Tunnel information
                    	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.Afs.Af.Counters.Tunnels, self).__init__()

                        self.yang_name = "tunnels"
                        self.yang_parent_name = "counters"

                        self.tunnel = YList(self)

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
                                    super(TrafficCollector.Afs.Af.Counters.Tunnels, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(TrafficCollector.Afs.Af.Counters.Tunnels, self).__setattr__(name, value)


                    class Tunnel(Entity):
                        """
                        Tunnel information
                        
                        .. attribute:: interface_name  <key>
                        
                        	The Interface Name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface name in Display format
                        	**type**\:  str
                        
                        .. attribute:: is_active
                        
                        	Interface is Active and collecting new Statistics
                        	**type**\:  bool
                        
                        .. attribute:: vrfid
                        
                        	Interface VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, self).__init__()

                            self.yang_name = "tunnel"
                            self.yang_parent_name = "tunnels"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                            self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                            self.is_active = YLeaf(YType.boolean, "is-active")

                            self.vrfid = YLeaf(YType.uint32, "vrfid")

                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                            self._children_yang_names.add("base-counter-statistics")

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
                                            "interface_handle",
                                            "interface_name_xr",
                                            "is_active",
                                            "vrfid") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, self).__setattr__(name, value)


                        class BaseCounterStatistics(Entity):
                            """
                            Base counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__init__()

                                self.yang_name = "base-counter-statistics"
                                self.yang_parent_name = "tunnel"

                                self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                self.count_history = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("transmit_bytes_per_second_switched",
                                                "transmit_packets_per_second_switched") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__setattr__(name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "base-counter-statistics"

                                    self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                    self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                    self.is_valid = YLeaf(YType.boolean, "is-valid")

                                    self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                    self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("event_end_timestamp",
                                                    "event_start_timestamp",
                                                    "is_valid",
                                                    "transmit_number_of_bytes_switched",
                                                    "transmit_number_of_packets_switched") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.event_end_timestamp.is_set or
                                        self.event_start_timestamp.is_set or
                                        self.is_valid.is_set or
                                        self.transmit_number_of_bytes_switched.is_set or
                                        self.transmit_number_of_packets_switched.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.event_end_timestamp.yfilter != YFilter.not_set or
                                        self.event_start_timestamp.yfilter != YFilter.not_set or
                                        self.is_valid.yfilter != YFilter.not_set or
                                        self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set or
                                        self.transmit_number_of_packets_switched.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "count-history" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.event_end_timestamp.is_set or self.event_end_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.event_end_timestamp.get_name_leafdata())
                                    if (self.event_start_timestamp.is_set or self.event_start_timestamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.event_start_timestamp.get_name_leafdata())
                                    if (self.is_valid.is_set or self.is_valid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.is_valid.get_name_leafdata())
                                    if (self.transmit_number_of_bytes_switched.is_set or self.transmit_number_of_bytes_switched.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.transmit_number_of_bytes_switched.get_name_leafdata())
                                    if (self.transmit_number_of_packets_switched.is_set or self.transmit_number_of_packets_switched.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.transmit_number_of_packets_switched.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "event-end-timestamp" or name == "event-start-timestamp" or name == "is-valid" or name == "transmit-number-of-bytes-switched" or name == "transmit-number-of-packets-switched"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "event-end-timestamp"):
                                        self.event_end_timestamp = value
                                        self.event_end_timestamp.value_namespace = name_space
                                        self.event_end_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "event-start-timestamp"):
                                        self.event_start_timestamp = value
                                        self.event_start_timestamp.value_namespace = name_space
                                        self.event_start_timestamp.value_namespace_prefix = name_space_prefix
                                    if(value_path == "is-valid"):
                                        self.is_valid = value
                                        self.is_valid.value_namespace = name_space
                                        self.is_valid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "transmit-number-of-bytes-switched"):
                                        self.transmit_number_of_bytes_switched = value
                                        self.transmit_number_of_bytes_switched.value_namespace = name_space
                                        self.transmit_number_of_bytes_switched.value_namespace_prefix = name_space_prefix
                                    if(value_path == "transmit-number-of-packets-switched"):
                                        self.transmit_number_of_packets_switched = value
                                        self.transmit_number_of_packets_switched.value_namespace = name_space
                                        self.transmit_number_of_packets_switched.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.count_history:
                                    if (c.has_data()):
                                        return True
                                return (
                                    self.transmit_bytes_per_second_switched.is_set or
                                    self.transmit_packets_per_second_switched.is_set)

                            def has_operation(self):
                                for c in self.count_history:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set or
                                    self.transmit_packets_per_second_switched.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "base-counter-statistics" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.transmit_bytes_per_second_switched.is_set or self.transmit_bytes_per_second_switched.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_bytes_per_second_switched.get_name_leafdata())
                                if (self.transmit_packets_per_second_switched.is_set or self.transmit_packets_per_second_switched.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.transmit_packets_per_second_switched.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "count-history"):
                                    for c in self.count_history:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.count_history.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "count-history" or name == "transmit-bytes-per-second-switched" or name == "transmit-packets-per-second-switched"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "transmit-bytes-per-second-switched"):
                                    self.transmit_bytes_per_second_switched = value
                                    self.transmit_bytes_per_second_switched.value_namespace = name_space
                                    self.transmit_bytes_per_second_switched.value_namespace_prefix = name_space_prefix
                                if(value_path == "transmit-packets-per-second-switched"):
                                    self.transmit_packets_per_second_switched = value
                                    self.transmit_packets_per_second_switched.value_namespace = name_space
                                    self.transmit_packets_per_second_switched.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.interface_handle.is_set or
                                self.interface_name_xr.is_set or
                                self.is_active.is_set or
                                self.vrfid.is_set or
                                (self.base_counter_statistics is not None and self.base_counter_statistics.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.interface_handle.yfilter != YFilter.not_set or
                                self.interface_name_xr.yfilter != YFilter.not_set or
                                self.is_active.yfilter != YFilter.not_set or
                                self.vrfid.yfilter != YFilter.not_set or
                                (self.base_counter_statistics is not None and self.base_counter_statistics.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tunnel" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.interface_handle.is_set or self.interface_handle.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_handle.get_name_leafdata())
                            if (self.interface_name_xr.is_set or self.interface_name_xr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name_xr.get_name_leafdata())
                            if (self.is_active.is_set or self.is_active.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_active.get_name_leafdata())
                            if (self.vrfid.is_set or self.vrfid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrfid.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "base-counter-statistics"):
                                if (self.base_counter_statistics is None):
                                    self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                return self.base_counter_statistics

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "base-counter-statistics" or name == "interface-name" or name == "interface-handle" or name == "interface-name-xr" or name == "is-active" or name == "vrfid"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-handle"):
                                self.interface_handle = value
                                self.interface_handle.value_namespace = name_space
                                self.interface_handle.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name-xr"):
                                self.interface_name_xr = value
                                self.interface_name_xr.value_namespace = name_space
                                self.interface_name_xr.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-active"):
                                self.is_active = value
                                self.is_active.value_namespace = name_space
                                self.is_active.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrfid"):
                                self.vrfid = value
                                self.vrfid.value_namespace = name_space
                                self.vrfid.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.tunnel:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.tunnel:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tunnels" + path_buffer

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

                        if (child_yang_name == "tunnel"):
                            for c in self.tunnel:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.tunnel.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tunnel"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.prefixes is not None and self.prefixes.has_data()) or
                        (self.tunnels is not None and self.tunnels.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.prefixes is not None and self.prefixes.has_operation()) or
                        (self.tunnels is not None and self.tunnels.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "counters" + path_buffer

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

                    if (child_yang_name == "prefixes"):
                        if (self.prefixes is None):
                            self.prefixes = TrafficCollector.Afs.Af.Counters.Prefixes()
                            self.prefixes.parent = self
                            self._children_name_map["prefixes"] = "prefixes"
                        return self.prefixes

                    if (child_yang_name == "tunnels"):
                        if (self.tunnels is None):
                            self.tunnels = TrafficCollector.Afs.Af.Counters.Tunnels()
                            self.tunnels.parent = self
                            self._children_name_map["tunnels"] = "tunnels"
                        return self.tunnels

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefixes" or name == "tunnels"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.af_name.is_set or
                    (self.counters is not None and self.counters.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.af_name.yfilter != YFilter.not_set or
                    (self.counters is not None and self.counters.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/afs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.af_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "counters"):
                    if (self.counters is None):
                        self.counters = TrafficCollector.Afs.Af.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                    return self.counters

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "counters" or name == "af-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "af-name"):
                    self.af_name = value
                    self.af_name.value_namespace = name_space
                    self.af_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.af:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.af:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "afs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "af"):
                for c in self.af:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TrafficCollector.Afs.Af()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.af.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "af"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.afs is not None and self.afs.has_data()) or
            (self.external_interfaces is not None and self.external_interfaces.has_data()) or
            (self.summary is not None and self.summary.has_data()) or
            (self.vrf_table is not None and self.vrf_table.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.afs is not None and self.afs.has_operation()) or
            (self.external_interfaces is not None and self.external_interfaces.has_operation()) or
            (self.summary is not None and self.summary.has_operation()) or
            (self.vrf_table is not None and self.vrf_table.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-tc-oper:traffic-collector" + path_buffer

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

        if (child_yang_name == "afs"):
            if (self.afs is None):
                self.afs = TrafficCollector.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
            return self.afs

        if (child_yang_name == "external-interfaces"):
            if (self.external_interfaces is None):
                self.external_interfaces = TrafficCollector.ExternalInterfaces()
                self.external_interfaces.parent = self
                self._children_name_map["external_interfaces"] = "external-interfaces"
            return self.external_interfaces

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = TrafficCollector.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        if (child_yang_name == "vrf-table"):
            if (self.vrf_table is None):
                self.vrf_table = TrafficCollector.VrfTable()
                self.vrf_table.parent = self
                self._children_name_map["vrf_table"] = "vrf-table"
            return self.vrf_table

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "afs" or name == "external-interfaces" or name == "summary" or name == "vrf-table"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TrafficCollector()
        return self._top_entity

