""" Cisco_IOS_XR_subscriber_session_mon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-session\-mon package operational data.

This module contains definitions
for the following management objects\:
  session\-mon\: Sessionmon

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SessionMon(Entity):
    """
    Sessionmon
    
    .. attribute:: nodes
    
    	Subscriber Sessionmon list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes>`
    
    

    """

    _prefix = 'subscriber-session-mon-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SessionMon, self).__init__()
        self._top_entity = None

        self.yang_name = "session-mon"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-session-mon-oper"

        self.nodes = SessionMon.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Subscriber Sessionmon list of nodes
        
        .. attribute:: node
        
        	Subscriber sessionmon operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-session-mon-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SessionMon.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "session-mon"

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
                        super(SessionMon.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SessionMon.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Subscriber sessionmon operational data for a
            particular node
            
            .. attribute:: node_id  <key>
            
            	Nodeid location 
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_all_statistics
            
            	Statistics Table
            	**type**\:   :py:class:`InterfaceAllStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.InterfaceAllStatistics>`
            
            .. attribute:: license_statistics
            
            	Smart license
            	**type**\:   :py:class:`LicenseStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.LicenseStatistics>`
            
            .. attribute:: session_mon_statistics
            
            	Session Mon Statistics
            	**type**\:   :py:class:`SessionMonStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.SessionMonStatistics>`
            
            

            """

            _prefix = 'subscriber-session-mon-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SessionMon.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_id = YLeaf(YType.str, "node-id")

                self.interface_all_statistics = SessionMon.Nodes.Node.InterfaceAllStatistics()
                self.interface_all_statistics.parent = self
                self._children_name_map["interface_all_statistics"] = "interface-all-statistics"
                self._children_yang_names.add("interface-all-statistics")

                self.license_statistics = SessionMon.Nodes.Node.LicenseStatistics()
                self.license_statistics.parent = self
                self._children_name_map["license_statistics"] = "license-statistics"
                self._children_yang_names.add("license-statistics")

                self.session_mon_statistics = SessionMon.Nodes.Node.SessionMonStatistics()
                self.session_mon_statistics.parent = self
                self._children_name_map["session_mon_statistics"] = "session-mon-statistics"
                self._children_yang_names.add("session-mon-statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SessionMon.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SessionMon.Nodes.Node, self).__setattr__(name, value)


            class SessionMonStatistics(Entity):
                """
                Session Mon Statistics
                
                .. attribute:: active_sessions
                
                	active sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcp_ds
                
                	dhcp ds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcpv4
                
                	dhcpv4
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcpv6
                
                	dhcpv6
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ippkt
                
                	ippkt
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_active_sessions
                
                	peak active sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_standby_sessions
                
                	peak standby sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_start_time
                
                	peak start time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pppoe
                
                	pppoe
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pppoe_ds
                
                	pppoe ds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_sessions
                
                	standby sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_value
                
                	timeout value
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total
                
                	total
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionMon.Nodes.Node.SessionMonStatistics, self).__init__()

                    self.yang_name = "session-mon-statistics"
                    self.yang_parent_name = "node"

                    self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                    self.dhcp_ds = YLeaf(YType.uint32, "dhcp-ds")

                    self.dhcpv4 = YLeaf(YType.uint32, "dhcpv4")

                    self.dhcpv6 = YLeaf(YType.uint32, "dhcpv6")

                    self.ippkt = YLeaf(YType.uint32, "ippkt")

                    self.peak_active_sessions = YLeaf(YType.uint32, "peak-active-sessions")

                    self.peak_standby_sessions = YLeaf(YType.uint32, "peak-standby-sessions")

                    self.peak_start_time = YLeaf(YType.uint32, "peak-start-time")

                    self.pppoe = YLeaf(YType.uint32, "pppoe")

                    self.pppoe_ds = YLeaf(YType.uint32, "pppoe-ds")

                    self.standby_sessions = YLeaf(YType.uint32, "standby-sessions")

                    self.timeout_value = YLeaf(YType.uint32, "timeout-value")

                    self.total = YLeaf(YType.uint32, "total")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_sessions",
                                    "dhcp_ds",
                                    "dhcpv4",
                                    "dhcpv6",
                                    "ippkt",
                                    "peak_active_sessions",
                                    "peak_standby_sessions",
                                    "peak_start_time",
                                    "pppoe",
                                    "pppoe_ds",
                                    "standby_sessions",
                                    "timeout_value",
                                    "total") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SessionMon.Nodes.Node.SessionMonStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionMon.Nodes.Node.SessionMonStatistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_sessions.is_set or
                        self.dhcp_ds.is_set or
                        self.dhcpv4.is_set or
                        self.dhcpv6.is_set or
                        self.ippkt.is_set or
                        self.peak_active_sessions.is_set or
                        self.peak_standby_sessions.is_set or
                        self.peak_start_time.is_set or
                        self.pppoe.is_set or
                        self.pppoe_ds.is_set or
                        self.standby_sessions.is_set or
                        self.timeout_value.is_set or
                        self.total.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_sessions.yfilter != YFilter.not_set or
                        self.dhcp_ds.yfilter != YFilter.not_set or
                        self.dhcpv4.yfilter != YFilter.not_set or
                        self.dhcpv6.yfilter != YFilter.not_set or
                        self.ippkt.yfilter != YFilter.not_set or
                        self.peak_active_sessions.yfilter != YFilter.not_set or
                        self.peak_standby_sessions.yfilter != YFilter.not_set or
                        self.peak_start_time.yfilter != YFilter.not_set or
                        self.pppoe.yfilter != YFilter.not_set or
                        self.pppoe_ds.yfilter != YFilter.not_set or
                        self.standby_sessions.yfilter != YFilter.not_set or
                        self.timeout_value.yfilter != YFilter.not_set or
                        self.total.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session-mon-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_sessions.is_set or self.active_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_sessions.get_name_leafdata())
                    if (self.dhcp_ds.is_set or self.dhcp_ds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcp_ds.get_name_leafdata())
                    if (self.dhcpv4.is_set or self.dhcpv4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcpv4.get_name_leafdata())
                    if (self.dhcpv6.is_set or self.dhcpv6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcpv6.get_name_leafdata())
                    if (self.ippkt.is_set or self.ippkt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ippkt.get_name_leafdata())
                    if (self.peak_active_sessions.is_set or self.peak_active_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_active_sessions.get_name_leafdata())
                    if (self.peak_standby_sessions.is_set or self.peak_standby_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_standby_sessions.get_name_leafdata())
                    if (self.peak_start_time.is_set or self.peak_start_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_start_time.get_name_leafdata())
                    if (self.pppoe.is_set or self.pppoe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pppoe.get_name_leafdata())
                    if (self.pppoe_ds.is_set or self.pppoe_ds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pppoe_ds.get_name_leafdata())
                    if (self.standby_sessions.is_set or self.standby_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_sessions.get_name_leafdata())
                    if (self.timeout_value.is_set or self.timeout_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout_value.get_name_leafdata())
                    if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-sessions" or name == "dhcp-ds" or name == "dhcpv4" or name == "dhcpv6" or name == "ippkt" or name == "peak-active-sessions" or name == "peak-standby-sessions" or name == "peak-start-time" or name == "pppoe" or name == "pppoe-ds" or name == "standby-sessions" or name == "timeout-value" or name == "total"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-sessions"):
                        self.active_sessions = value
                        self.active_sessions.value_namespace = name_space
                        self.active_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcp-ds"):
                        self.dhcp_ds = value
                        self.dhcp_ds.value_namespace = name_space
                        self.dhcp_ds.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcpv4"):
                        self.dhcpv4 = value
                        self.dhcpv4.value_namespace = name_space
                        self.dhcpv4.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcpv6"):
                        self.dhcpv6 = value
                        self.dhcpv6.value_namespace = name_space
                        self.dhcpv6.value_namespace_prefix = name_space_prefix
                    if(value_path == "ippkt"):
                        self.ippkt = value
                        self.ippkt.value_namespace = name_space
                        self.ippkt.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-active-sessions"):
                        self.peak_active_sessions = value
                        self.peak_active_sessions.value_namespace = name_space
                        self.peak_active_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-standby-sessions"):
                        self.peak_standby_sessions = value
                        self.peak_standby_sessions.value_namespace = name_space
                        self.peak_standby_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-start-time"):
                        self.peak_start_time = value
                        self.peak_start_time.value_namespace = name_space
                        self.peak_start_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "pppoe"):
                        self.pppoe = value
                        self.pppoe.value_namespace = name_space
                        self.pppoe.value_namespace_prefix = name_space_prefix
                    if(value_path == "pppoe-ds"):
                        self.pppoe_ds = value
                        self.pppoe_ds.value_namespace = name_space
                        self.pppoe_ds.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-sessions"):
                        self.standby_sessions = value
                        self.standby_sessions.value_namespace = name_space
                        self.standby_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout-value"):
                        self.timeout_value = value
                        self.timeout_value.value_namespace = name_space
                        self.timeout_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "total"):
                        self.total = value
                        self.total.value_namespace = name_space
                        self.total.value_namespace_prefix = name_space_prefix


            class InterfaceAllStatistics(Entity):
                """
                Statistics Table
                
                .. attribute:: interface_all_statistic
                
                	Statistics
                	**type**\: list of    :py:class:`InterfaceAllStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic>`
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionMon.Nodes.Node.InterfaceAllStatistics, self).__init__()

                    self.yang_name = "interface-all-statistics"
                    self.yang_parent_name = "node"

                    self.interface_all_statistic = YList(self)

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
                                super(SessionMon.Nodes.Node.InterfaceAllStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionMon.Nodes.Node.InterfaceAllStatistics, self).__setattr__(name, value)


                class InterfaceAllStatistic(Entity):
                    """
                    Statistics
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: active_sessions
                    
                    	active sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dhcp_ds
                    
                    	dhcp ds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dhcpv4
                    
                    	dhcpv4
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dhcpv6
                    
                    	dhcpv6
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ippkt
                    
                    	ippkt
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peak_active_sessions
                    
                    	peak active sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peak_standby_sessions
                    
                    	peak standby sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peak_start_time
                    
                    	peak start time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pppoe
                    
                    	pppoe
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pppoe_ds
                    
                    	pppoe ds
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: standby_sessions
                    
                    	standby sessions
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: timeout_value
                    
                    	timeout value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total
                    
                    	total
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic, self).__init__()

                        self.yang_name = "interface-all-statistic"
                        self.yang_parent_name = "interface-all-statistics"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                        self.dhcp_ds = YLeaf(YType.uint32, "dhcp-ds")

                        self.dhcpv4 = YLeaf(YType.uint32, "dhcpv4")

                        self.dhcpv6 = YLeaf(YType.uint32, "dhcpv6")

                        self.ippkt = YLeaf(YType.uint32, "ippkt")

                        self.peak_active_sessions = YLeaf(YType.uint32, "peak-active-sessions")

                        self.peak_standby_sessions = YLeaf(YType.uint32, "peak-standby-sessions")

                        self.peak_start_time = YLeaf(YType.uint32, "peak-start-time")

                        self.pppoe = YLeaf(YType.uint32, "pppoe")

                        self.pppoe_ds = YLeaf(YType.uint32, "pppoe-ds")

                        self.standby_sessions = YLeaf(YType.uint32, "standby-sessions")

                        self.timeout_value = YLeaf(YType.uint32, "timeout-value")

                        self.total = YLeaf(YType.uint32, "total")

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
                                        "active_sessions",
                                        "dhcp_ds",
                                        "dhcpv4",
                                        "dhcpv6",
                                        "ippkt",
                                        "peak_active_sessions",
                                        "peak_standby_sessions",
                                        "peak_start_time",
                                        "pppoe",
                                        "pppoe_ds",
                                        "standby_sessions",
                                        "timeout_value",
                                        "total") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.active_sessions.is_set or
                            self.dhcp_ds.is_set or
                            self.dhcpv4.is_set or
                            self.dhcpv6.is_set or
                            self.ippkt.is_set or
                            self.peak_active_sessions.is_set or
                            self.peak_standby_sessions.is_set or
                            self.peak_start_time.is_set or
                            self.pppoe.is_set or
                            self.pppoe_ds.is_set or
                            self.standby_sessions.is_set or
                            self.timeout_value.is_set or
                            self.total.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.active_sessions.yfilter != YFilter.not_set or
                            self.dhcp_ds.yfilter != YFilter.not_set or
                            self.dhcpv4.yfilter != YFilter.not_set or
                            self.dhcpv6.yfilter != YFilter.not_set or
                            self.ippkt.yfilter != YFilter.not_set or
                            self.peak_active_sessions.yfilter != YFilter.not_set or
                            self.peak_standby_sessions.yfilter != YFilter.not_set or
                            self.peak_start_time.yfilter != YFilter.not_set or
                            self.pppoe.yfilter != YFilter.not_set or
                            self.pppoe_ds.yfilter != YFilter.not_set or
                            self.standby_sessions.yfilter != YFilter.not_set or
                            self.timeout_value.yfilter != YFilter.not_set or
                            self.total.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-all-statistic" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

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
                        if (self.active_sessions.is_set or self.active_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active_sessions.get_name_leafdata())
                        if (self.dhcp_ds.is_set or self.dhcp_ds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dhcp_ds.get_name_leafdata())
                        if (self.dhcpv4.is_set or self.dhcpv4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dhcpv4.get_name_leafdata())
                        if (self.dhcpv6.is_set or self.dhcpv6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dhcpv6.get_name_leafdata())
                        if (self.ippkt.is_set or self.ippkt.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ippkt.get_name_leafdata())
                        if (self.peak_active_sessions.is_set or self.peak_active_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_active_sessions.get_name_leafdata())
                        if (self.peak_standby_sessions.is_set or self.peak_standby_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_standby_sessions.get_name_leafdata())
                        if (self.peak_start_time.is_set or self.peak_start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peak_start_time.get_name_leafdata())
                        if (self.pppoe.is_set or self.pppoe.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pppoe.get_name_leafdata())
                        if (self.pppoe_ds.is_set or self.pppoe_ds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pppoe_ds.get_name_leafdata())
                        if (self.standby_sessions.is_set or self.standby_sessions.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.standby_sessions.get_name_leafdata())
                        if (self.timeout_value.is_set or self.timeout_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout_value.get_name_leafdata())
                        if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-name" or name == "active-sessions" or name == "dhcp-ds" or name == "dhcpv4" or name == "dhcpv6" or name == "ippkt" or name == "peak-active-sessions" or name == "peak-standby-sessions" or name == "peak-start-time" or name == "pppoe" or name == "pppoe-ds" or name == "standby-sessions" or name == "timeout-value" or name == "total"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "active-sessions"):
                            self.active_sessions = value
                            self.active_sessions.value_namespace = name_space
                            self.active_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "dhcp-ds"):
                            self.dhcp_ds = value
                            self.dhcp_ds.value_namespace = name_space
                            self.dhcp_ds.value_namespace_prefix = name_space_prefix
                        if(value_path == "dhcpv4"):
                            self.dhcpv4 = value
                            self.dhcpv4.value_namespace = name_space
                            self.dhcpv4.value_namespace_prefix = name_space_prefix
                        if(value_path == "dhcpv6"):
                            self.dhcpv6 = value
                            self.dhcpv6.value_namespace = name_space
                            self.dhcpv6.value_namespace_prefix = name_space_prefix
                        if(value_path == "ippkt"):
                            self.ippkt = value
                            self.ippkt.value_namespace = name_space
                            self.ippkt.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-active-sessions"):
                            self.peak_active_sessions = value
                            self.peak_active_sessions.value_namespace = name_space
                            self.peak_active_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-standby-sessions"):
                            self.peak_standby_sessions = value
                            self.peak_standby_sessions.value_namespace = name_space
                            self.peak_standby_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "peak-start-time"):
                            self.peak_start_time = value
                            self.peak_start_time.value_namespace = name_space
                            self.peak_start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "pppoe"):
                            self.pppoe = value
                            self.pppoe.value_namespace = name_space
                            self.pppoe.value_namespace_prefix = name_space_prefix
                        if(value_path == "pppoe-ds"):
                            self.pppoe_ds = value
                            self.pppoe_ds.value_namespace = name_space
                            self.pppoe_ds.value_namespace_prefix = name_space_prefix
                        if(value_path == "standby-sessions"):
                            self.standby_sessions = value
                            self.standby_sessions.value_namespace = name_space
                            self.standby_sessions.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout-value"):
                            self.timeout_value = value
                            self.timeout_value.value_namespace = name_space
                            self.timeout_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "total"):
                            self.total = value
                            self.total.value_namespace = name_space
                            self.total.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_all_statistic:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_all_statistic:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-all-statistics" + path_buffer

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

                    if (child_yang_name == "interface-all-statistic"):
                        for c in self.interface_all_statistic:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_all_statistic.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-all-statistic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class LicenseStatistics(Entity):
                """
                Smart license
                
                .. attribute:: active_sessions
                
                	active sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcp_ds
                
                	dhcp ds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcpv4
                
                	dhcpv4
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dhcpv6
                
                	dhcpv6
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: ippkt
                
                	ippkt
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_active_sessions
                
                	peak active sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_standby_sessions
                
                	peak standby sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peak_start_time
                
                	peak start time
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pppoe
                
                	pppoe
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pppoe_ds
                
                	pppoe ds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: standby_sessions
                
                	standby sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_value
                
                	timeout value
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total
                
                	total
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SessionMon.Nodes.Node.LicenseStatistics, self).__init__()

                    self.yang_name = "license-statistics"
                    self.yang_parent_name = "node"

                    self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                    self.dhcp_ds = YLeaf(YType.uint32, "dhcp-ds")

                    self.dhcpv4 = YLeaf(YType.uint32, "dhcpv4")

                    self.dhcpv6 = YLeaf(YType.uint32, "dhcpv6")

                    self.ippkt = YLeaf(YType.uint32, "ippkt")

                    self.peak_active_sessions = YLeaf(YType.uint32, "peak-active-sessions")

                    self.peak_standby_sessions = YLeaf(YType.uint32, "peak-standby-sessions")

                    self.peak_start_time = YLeaf(YType.uint32, "peak-start-time")

                    self.pppoe = YLeaf(YType.uint32, "pppoe")

                    self.pppoe_ds = YLeaf(YType.uint32, "pppoe-ds")

                    self.standby_sessions = YLeaf(YType.uint32, "standby-sessions")

                    self.timeout_value = YLeaf(YType.uint32, "timeout-value")

                    self.total = YLeaf(YType.uint32, "total")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active_sessions",
                                    "dhcp_ds",
                                    "dhcpv4",
                                    "dhcpv6",
                                    "ippkt",
                                    "peak_active_sessions",
                                    "peak_standby_sessions",
                                    "peak_start_time",
                                    "pppoe",
                                    "pppoe_ds",
                                    "standby_sessions",
                                    "timeout_value",
                                    "total") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SessionMon.Nodes.Node.LicenseStatistics, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SessionMon.Nodes.Node.LicenseStatistics, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active_sessions.is_set or
                        self.dhcp_ds.is_set or
                        self.dhcpv4.is_set or
                        self.dhcpv6.is_set or
                        self.ippkt.is_set or
                        self.peak_active_sessions.is_set or
                        self.peak_standby_sessions.is_set or
                        self.peak_start_time.is_set or
                        self.pppoe.is_set or
                        self.pppoe_ds.is_set or
                        self.standby_sessions.is_set or
                        self.timeout_value.is_set or
                        self.total.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active_sessions.yfilter != YFilter.not_set or
                        self.dhcp_ds.yfilter != YFilter.not_set or
                        self.dhcpv4.yfilter != YFilter.not_set or
                        self.dhcpv6.yfilter != YFilter.not_set or
                        self.ippkt.yfilter != YFilter.not_set or
                        self.peak_active_sessions.yfilter != YFilter.not_set or
                        self.peak_standby_sessions.yfilter != YFilter.not_set or
                        self.peak_start_time.yfilter != YFilter.not_set or
                        self.pppoe.yfilter != YFilter.not_set or
                        self.pppoe_ds.yfilter != YFilter.not_set or
                        self.standby_sessions.yfilter != YFilter.not_set or
                        self.timeout_value.yfilter != YFilter.not_set or
                        self.total.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "license-statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active_sessions.is_set or self.active_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active_sessions.get_name_leafdata())
                    if (self.dhcp_ds.is_set or self.dhcp_ds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcp_ds.get_name_leafdata())
                    if (self.dhcpv4.is_set or self.dhcpv4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcpv4.get_name_leafdata())
                    if (self.dhcpv6.is_set or self.dhcpv6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dhcpv6.get_name_leafdata())
                    if (self.ippkt.is_set or self.ippkt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ippkt.get_name_leafdata())
                    if (self.peak_active_sessions.is_set or self.peak_active_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_active_sessions.get_name_leafdata())
                    if (self.peak_standby_sessions.is_set or self.peak_standby_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_standby_sessions.get_name_leafdata())
                    if (self.peak_start_time.is_set or self.peak_start_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peak_start_time.get_name_leafdata())
                    if (self.pppoe.is_set or self.pppoe.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pppoe.get_name_leafdata())
                    if (self.pppoe_ds.is_set or self.pppoe_ds.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pppoe_ds.get_name_leafdata())
                    if (self.standby_sessions.is_set or self.standby_sessions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby_sessions.get_name_leafdata())
                    if (self.timeout_value.is_set or self.timeout_value.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout_value.get_name_leafdata())
                    if (self.total.is_set or self.total.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active-sessions" or name == "dhcp-ds" or name == "dhcpv4" or name == "dhcpv6" or name == "ippkt" or name == "peak-active-sessions" or name == "peak-standby-sessions" or name == "peak-start-time" or name == "pppoe" or name == "pppoe-ds" or name == "standby-sessions" or name == "timeout-value" or name == "total"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active-sessions"):
                        self.active_sessions = value
                        self.active_sessions.value_namespace = name_space
                        self.active_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcp-ds"):
                        self.dhcp_ds = value
                        self.dhcp_ds.value_namespace = name_space
                        self.dhcp_ds.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcpv4"):
                        self.dhcpv4 = value
                        self.dhcpv4.value_namespace = name_space
                        self.dhcpv4.value_namespace_prefix = name_space_prefix
                    if(value_path == "dhcpv6"):
                        self.dhcpv6 = value
                        self.dhcpv6.value_namespace = name_space
                        self.dhcpv6.value_namespace_prefix = name_space_prefix
                    if(value_path == "ippkt"):
                        self.ippkt = value
                        self.ippkt.value_namespace = name_space
                        self.ippkt.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-active-sessions"):
                        self.peak_active_sessions = value
                        self.peak_active_sessions.value_namespace = name_space
                        self.peak_active_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-standby-sessions"):
                        self.peak_standby_sessions = value
                        self.peak_standby_sessions.value_namespace = name_space
                        self.peak_standby_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "peak-start-time"):
                        self.peak_start_time = value
                        self.peak_start_time.value_namespace = name_space
                        self.peak_start_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "pppoe"):
                        self.pppoe = value
                        self.pppoe.value_namespace = name_space
                        self.pppoe.value_namespace_prefix = name_space_prefix
                    if(value_path == "pppoe-ds"):
                        self.pppoe_ds = value
                        self.pppoe_ds.value_namespace = name_space
                        self.pppoe_ds.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby-sessions"):
                        self.standby_sessions = value
                        self.standby_sessions.value_namespace = name_space
                        self.standby_sessions.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout-value"):
                        self.timeout_value = value
                        self.timeout_value.value_namespace = name_space
                        self.timeout_value.value_namespace_prefix = name_space_prefix
                    if(value_path == "total"):
                        self.total = value
                        self.total.value_namespace = name_space
                        self.total.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_id.is_set or
                    (self.interface_all_statistics is not None and self.interface_all_statistics.has_data()) or
                    (self.license_statistics is not None and self.license_statistics.has_data()) or
                    (self.session_mon_statistics is not None and self.session_mon_statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_id.yfilter != YFilter.not_set or
                    (self.interface_all_statistics is not None and self.interface_all_statistics.has_operation()) or
                    (self.license_statistics is not None and self.license_statistics.has_operation()) or
                    (self.session_mon_statistics is not None and self.session_mon_statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-all-statistics"):
                    if (self.interface_all_statistics is None):
                        self.interface_all_statistics = SessionMon.Nodes.Node.InterfaceAllStatistics()
                        self.interface_all_statistics.parent = self
                        self._children_name_map["interface_all_statistics"] = "interface-all-statistics"
                    return self.interface_all_statistics

                if (child_yang_name == "license-statistics"):
                    if (self.license_statistics is None):
                        self.license_statistics = SessionMon.Nodes.Node.LicenseStatistics()
                        self.license_statistics.parent = self
                        self._children_name_map["license_statistics"] = "license-statistics"
                    return self.license_statistics

                if (child_yang_name == "session-mon-statistics"):
                    if (self.session_mon_statistics is None):
                        self.session_mon_statistics = SessionMon.Nodes.Node.SessionMonStatistics()
                        self.session_mon_statistics.parent = self
                        self._children_name_map["session_mon_statistics"] = "session-mon-statistics"
                    return self.session_mon_statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-all-statistics" or name == "license-statistics" or name == "session-mon-statistics" or name == "node-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-id"):
                    self.node_id = value
                    self.node_id.value_namespace = name_space
                    self.node_id.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/%s" % self.get_segment_path()
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
                c = SessionMon.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon" + path_buffer

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
                self.nodes = SessionMon.Nodes()
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
        self._top_entity = SessionMon()
        return self._top_entity

