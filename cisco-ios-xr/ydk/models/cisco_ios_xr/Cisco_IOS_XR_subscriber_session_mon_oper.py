""" Cisco_IOS_XR_subscriber_session_mon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-session\-mon package operational data.

This module contains definitions
for the following management objects\:
  session\-mon\: Sessionmon

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SessionMon(_Entity_):
    """
    Sessionmon
    
    .. attribute:: nodes
    
    	Subscriber Sessionmon list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'subscriber-session-mon-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SessionMon, self).__init__()
        self._top_entity = None

        self.yang_name = "session-mon"
        self.yang_parent_name = "Cisco-IOS-XR-subscriber-session-mon-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", SessionMon.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = SessionMon.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SessionMon, [], name, value)


    class Nodes(_Entity_):
        """
        Subscriber Sessionmon list of nodes
        
        .. attribute:: node
        
        	Subscriber sessionmon operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'subscriber-session-mon-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SessionMon.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "session-mon"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SessionMon.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SessionMon.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Subscriber sessionmon operational data for a
            particular node
            
            .. attribute:: node_id  (key)
            
            	Nodeid location 
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: session_mon_statistics
            
            	Session Mon Statistics
            	**type**\:  :py:class:`SessionMonStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.SessionMonStatistics>`
            
            	**config**\: False
            
            .. attribute:: interface_all_statistics
            
            	Statistics Table
            	**type**\:  :py:class:`InterfaceAllStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.InterfaceAllStatistics>`
            
            	**config**\: False
            
            .. attribute:: license_statistics
            
            	Smart license
            	**type**\:  :py:class:`LicenseStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.LicenseStatistics>`
            
            	**config**\: False
            
            

            """

            _prefix = 'subscriber-session-mon-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SessionMon.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_id']
                self._child_classes = OrderedDict([("session-mon-statistics", ("session_mon_statistics", SessionMon.Nodes.Node.SessionMonStatistics)), ("interface-all-statistics", ("interface_all_statistics", SessionMon.Nodes.Node.InterfaceAllStatistics)), ("license-statistics", ("license_statistics", SessionMon.Nodes.Node.LicenseStatistics))])
                self._leafs = OrderedDict([
                    ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                ])
                self.node_id = None

                self.session_mon_statistics = SessionMon.Nodes.Node.SessionMonStatistics()
                self.session_mon_statistics.parent = self
                self._children_name_map["session_mon_statistics"] = "session-mon-statistics"

                self.interface_all_statistics = SessionMon.Nodes.Node.InterfaceAllStatistics()
                self.interface_all_statistics.parent = self
                self._children_name_map["interface_all_statistics"] = "interface-all-statistics"

                self.license_statistics = SessionMon.Nodes.Node.LicenseStatistics()
                self.license_statistics.parent = self
                self._children_name_map["license_statistics"] = "license-statistics"
                self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SessionMon.Nodes.Node, ['node_id'], name, value)


            class SessionMonStatistics(_Entity_):
                """
                Session Mon Statistics
                
                .. attribute:: total
                
                	total
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: pppoe
                
                	pppoe
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: pppoe_ds
                
                	pppoe ds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcpv4
                
                	dhcpv4
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcpv6
                
                	dhcpv6
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcp_ds
                
                	dhcp ds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ippkt
                
                	ippkt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: active_sessions
                
                	active sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_sessions
                
                	standby sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peak_active_sessions
                
                	peak active sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peak_standby_sessions
                
                	peak standby sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peak_start_time
                
                	peak start time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: timeout_value
                
                	timeout value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SessionMon.Nodes.Node.SessionMonStatistics, self).__init__()

                    self.yang_name = "session-mon-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                        ('pppoe', (YLeaf(YType.uint32, 'pppoe'), ['int'])),
                        ('pppoe_ds', (YLeaf(YType.uint32, 'pppoe-ds'), ['int'])),
                        ('dhcpv4', (YLeaf(YType.uint32, 'dhcpv4'), ['int'])),
                        ('dhcpv6', (YLeaf(YType.uint32, 'dhcpv6'), ['int'])),
                        ('dhcp_ds', (YLeaf(YType.uint32, 'dhcp-ds'), ['int'])),
                        ('ippkt', (YLeaf(YType.uint32, 'ippkt'), ['int'])),
                        ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                        ('standby_sessions', (YLeaf(YType.uint32, 'standby-sessions'), ['int'])),
                        ('peak_active_sessions', (YLeaf(YType.uint32, 'peak-active-sessions'), ['int'])),
                        ('peak_standby_sessions', (YLeaf(YType.uint32, 'peak-standby-sessions'), ['int'])),
                        ('peak_start_time', (YLeaf(YType.uint32, 'peak-start-time'), ['int'])),
                        ('timeout_value', (YLeaf(YType.uint32, 'timeout-value'), ['int'])),
                    ])
                    self.total = None
                    self.pppoe = None
                    self.pppoe_ds = None
                    self.dhcpv4 = None
                    self.dhcpv6 = None
                    self.dhcp_ds = None
                    self.ippkt = None
                    self.active_sessions = None
                    self.standby_sessions = None
                    self.peak_active_sessions = None
                    self.peak_standby_sessions = None
                    self.peak_start_time = None
                    self.timeout_value = None
                    self._segment_path = lambda: "session-mon-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionMon.Nodes.Node.SessionMonStatistics, ['total', 'pppoe', 'pppoe_ds', 'dhcpv4', 'dhcpv6', 'dhcp_ds', 'ippkt', 'active_sessions', 'standby_sessions', 'peak_active_sessions', 'peak_standby_sessions', 'peak_start_time', 'timeout_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                    return meta._meta_table['SessionMon.Nodes.Node.SessionMonStatistics']['meta_info']


            class InterfaceAllStatistics(_Entity_):
                """
                Statistics Table
                
                .. attribute:: interface_all_statistic
                
                	Statistics
                	**type**\: list of  		 :py:class:`InterfaceAllStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic>`
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SessionMon.Nodes.Node.InterfaceAllStatistics, self).__init__()

                    self.yang_name = "interface-all-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-all-statistic", ("interface_all_statistic", SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic))])
                    self._leafs = OrderedDict()

                    self.interface_all_statistic = YList(self)
                    self._segment_path = lambda: "interface-all-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionMon.Nodes.Node.InterfaceAllStatistics, [], name, value)


                class InterfaceAllStatistic(_Entity_):
                    """
                    Statistics
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: total
                    
                    	total
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pppoe
                    
                    	pppoe
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pppoe_ds
                    
                    	pppoe ds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dhcpv4
                    
                    	dhcpv4
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dhcpv6
                    
                    	dhcpv6
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: dhcp_ds
                    
                    	dhcp ds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ippkt
                    
                    	ippkt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: active_sessions
                    
                    	active sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: standby_sessions
                    
                    	standby sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peak_active_sessions
                    
                    	peak active sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peak_standby_sessions
                    
                    	peak standby sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: peak_start_time
                    
                    	peak start time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: timeout_value
                    
                    	timeout value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic, self).__init__()

                        self.yang_name = "interface-all-statistic"
                        self.yang_parent_name = "interface-all-statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                            ('pppoe', (YLeaf(YType.uint32, 'pppoe'), ['int'])),
                            ('pppoe_ds', (YLeaf(YType.uint32, 'pppoe-ds'), ['int'])),
                            ('dhcpv4', (YLeaf(YType.uint32, 'dhcpv4'), ['int'])),
                            ('dhcpv6', (YLeaf(YType.uint32, 'dhcpv6'), ['int'])),
                            ('dhcp_ds', (YLeaf(YType.uint32, 'dhcp-ds'), ['int'])),
                            ('ippkt', (YLeaf(YType.uint32, 'ippkt'), ['int'])),
                            ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                            ('standby_sessions', (YLeaf(YType.uint32, 'standby-sessions'), ['int'])),
                            ('peak_active_sessions', (YLeaf(YType.uint32, 'peak-active-sessions'), ['int'])),
                            ('peak_standby_sessions', (YLeaf(YType.uint32, 'peak-standby-sessions'), ['int'])),
                            ('peak_start_time', (YLeaf(YType.uint32, 'peak-start-time'), ['int'])),
                            ('timeout_value', (YLeaf(YType.uint32, 'timeout-value'), ['int'])),
                        ])
                        self.interface_name = None
                        self.total = None
                        self.pppoe = None
                        self.pppoe_ds = None
                        self.dhcpv4 = None
                        self.dhcpv6 = None
                        self.dhcp_ds = None
                        self.ippkt = None
                        self.active_sessions = None
                        self.standby_sessions = None
                        self.peak_active_sessions = None
                        self.peak_standby_sessions = None
                        self.peak_start_time = None
                        self.timeout_value = None
                        self._segment_path = lambda: "interface-all-statistic" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic, ['interface_name', 'total', 'pppoe', 'pppoe_ds', 'dhcpv4', 'dhcpv6', 'dhcp_ds', 'ippkt', 'active_sessions', 'standby_sessions', 'peak_active_sessions', 'peak_standby_sessions', 'peak_start_time', 'timeout_value'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                        return meta._meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                    return meta._meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics']['meta_info']


            class LicenseStatistics(_Entity_):
                """
                Smart license
                
                .. attribute:: total
                
                	total
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: pppoe
                
                	pppoe
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: pppoe_ds
                
                	pppoe ds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcpv4
                
                	dhcpv4
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcpv6
                
                	dhcpv6
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: dhcp_ds
                
                	dhcp ds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: ippkt
                
                	ippkt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: active_sessions
                
                	active sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: standby_sessions
                
                	standby sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peak_active_sessions
                
                	peak active sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peak_standby_sessions
                
                	peak standby sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: peak_start_time
                
                	peak start time
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: timeout_value
                
                	timeout value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SessionMon.Nodes.Node.LicenseStatistics, self).__init__()

                    self.yang_name = "license-statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total', (YLeaf(YType.uint32, 'total'), ['int'])),
                        ('pppoe', (YLeaf(YType.uint32, 'pppoe'), ['int'])),
                        ('pppoe_ds', (YLeaf(YType.uint32, 'pppoe-ds'), ['int'])),
                        ('dhcpv4', (YLeaf(YType.uint32, 'dhcpv4'), ['int'])),
                        ('dhcpv6', (YLeaf(YType.uint32, 'dhcpv6'), ['int'])),
                        ('dhcp_ds', (YLeaf(YType.uint32, 'dhcp-ds'), ['int'])),
                        ('ippkt', (YLeaf(YType.uint32, 'ippkt'), ['int'])),
                        ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                        ('standby_sessions', (YLeaf(YType.uint32, 'standby-sessions'), ['int'])),
                        ('peak_active_sessions', (YLeaf(YType.uint32, 'peak-active-sessions'), ['int'])),
                        ('peak_standby_sessions', (YLeaf(YType.uint32, 'peak-standby-sessions'), ['int'])),
                        ('peak_start_time', (YLeaf(YType.uint32, 'peak-start-time'), ['int'])),
                        ('timeout_value', (YLeaf(YType.uint32, 'timeout-value'), ['int'])),
                    ])
                    self.total = None
                    self.pppoe = None
                    self.pppoe_ds = None
                    self.dhcpv4 = None
                    self.dhcpv6 = None
                    self.dhcp_ds = None
                    self.ippkt = None
                    self.active_sessions = None
                    self.standby_sessions = None
                    self.peak_active_sessions = None
                    self.peak_standby_sessions = None
                    self.peak_start_time = None
                    self.timeout_value = None
                    self._segment_path = lambda: "license-statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SessionMon.Nodes.Node.LicenseStatistics, ['total', 'pppoe', 'pppoe_ds', 'dhcpv4', 'dhcpv6', 'dhcp_ds', 'ippkt', 'active_sessions', 'standby_sessions', 'peak_active_sessions', 'peak_standby_sessions', 'peak_start_time', 'timeout_value'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                    return meta._meta_table['SessionMon.Nodes.Node.LicenseStatistics']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                return meta._meta_table['SessionMon.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
            return meta._meta_table['SessionMon.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = SessionMon()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
        return meta._meta_table['SessionMon']['meta_info']


