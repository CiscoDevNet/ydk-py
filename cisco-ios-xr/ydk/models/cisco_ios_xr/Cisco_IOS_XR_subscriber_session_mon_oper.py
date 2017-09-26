""" Cisco_IOS_XR_subscriber_session_mon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-session\-mon package operational data.

This module contains definitions
for the following management objects\:
  session\-mon\: Sessionmon

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", SessionMon.Nodes)}
        self._child_list_classes = {}

        self.nodes = SessionMon.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", SessionMon.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SessionMon.Nodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interface-all-statistics" : ("interface_all_statistics", SessionMon.Nodes.Node.InterfaceAllStatistics), "license-statistics" : ("license_statistics", SessionMon.Nodes.Node.LicenseStatistics), "session-mon-statistics" : ("session_mon_statistics", SessionMon.Nodes.Node.SessionMonStatistics)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "node" + "[node-id='" + self.node_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SessionMon.Nodes.Node, ['node_id'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-all-statistic" : ("interface_all_statistic", SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic)}

                    self.interface_all_statistic = YList(self)
                    self._segment_path = lambda: "interface-all-statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionMon.Nodes.Node.InterfaceAllStatistics, [], name, value)


                class InterfaceAllStatistic(Entity):
                    """
                    Statistics
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "interface-all-statistic" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic, ['interface_name', 'active_sessions', 'dhcp_ds', 'dhcpv4', 'dhcpv6', 'ippkt', 'peak_active_sessions', 'peak_standby_sessions', 'peak_start_time', 'pppoe', 'pppoe_ds', 'standby_sessions', 'timeout_value', 'total'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "license-statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionMon.Nodes.Node.LicenseStatistics, ['active_sessions', 'dhcp_ds', 'dhcpv4', 'dhcpv6', 'ippkt', 'peak_active_sessions', 'peak_standby_sessions', 'peak_start_time', 'pppoe', 'pppoe_ds', 'standby_sessions', 'timeout_value', 'total'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "session-mon-statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionMon.Nodes.Node.SessionMonStatistics, ['active_sessions', 'dhcp_ds', 'dhcpv4', 'dhcpv6', 'ippkt', 'peak_active_sessions', 'peak_standby_sessions', 'peak_start_time', 'pppoe', 'pppoe_ds', 'standby_sessions', 'timeout_value', 'total'], name, value)

    def clone_ptr(self):
        self._top_entity = SessionMon()
        return self._top_entity

