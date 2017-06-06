""" Cisco_IOS_XR_subscriber_session_mon_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR subscriber\-session\-mon package operational data.

This module contains definitions
for the following management objects\:
  session\-mon\: Sessionmon

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class SessionMon(object):
    """
    Sessionmon
    
    .. attribute:: nodes
    
    	Subscriber Sessionmon list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes>`
    
    

    """

    _prefix = 'subscriber-session-mon-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = SessionMon.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Subscriber Sessionmon list of nodes
        
        .. attribute:: node
        
        	Subscriber sessionmon operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node>`
        
        

        """

        _prefix = 'subscriber-session-mon-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_id = None
                self.interface_all_statistics = SessionMon.Nodes.Node.InterfaceAllStatistics()
                self.interface_all_statistics.parent = self
                self.license_statistics = SessionMon.Nodes.Node.LicenseStatistics()
                self.license_statistics.parent = self
                self.session_mon_statistics = SessionMon.Nodes.Node.SessionMonStatistics()
                self.session_mon_statistics.parent = self


            class SessionMonStatistics(object):
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
                
                .. attribute:: total
                
                	total
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active_sessions = None
                    self.dhcp_ds = None
                    self.dhcpv4 = None
                    self.dhcpv6 = None
                    self.ippkt = None
                    self.peak_active_sessions = None
                    self.peak_standby_sessions = None
                    self.pppoe = None
                    self.pppoe_ds = None
                    self.standby_sessions = None
                    self.total = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-session-mon-oper:session-mon-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active_sessions is not None:
                        return True

                    if self.dhcp_ds is not None:
                        return True

                    if self.dhcpv4 is not None:
                        return True

                    if self.dhcpv6 is not None:
                        return True

                    if self.ippkt is not None:
                        return True

                    if self.peak_active_sessions is not None:
                        return True

                    if self.peak_standby_sessions is not None:
                        return True

                    if self.pppoe is not None:
                        return True

                    if self.pppoe_ds is not None:
                        return True

                    if self.standby_sessions is not None:
                        return True

                    if self.total is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                    return meta._meta_table['SessionMon.Nodes.Node.SessionMonStatistics']['meta_info']


            class InterfaceAllStatistics(object):
                """
                Statistics Table
                
                .. attribute:: interface_all_statistic
                
                	Statistics
                	**type**\: list of    :py:class:`InterfaceAllStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper.SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic>`
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_all_statistic = YList()
                    self.interface_all_statistic.parent = self
                    self.interface_all_statistic.name = 'interface_all_statistic'


                class InterfaceAllStatistic(object):
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
                    
                    .. attribute:: total
                    
                    	total
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'subscriber-session-mon-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.active_sessions = None
                        self.dhcp_ds = None
                        self.dhcpv4 = None
                        self.dhcpv6 = None
                        self.ippkt = None
                        self.peak_active_sessions = None
                        self.peak_standby_sessions = None
                        self.pppoe = None
                        self.pppoe_ds = None
                        self.standby_sessions = None
                        self.total = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-subscriber-session-mon-oper:interface-all-statistic[Cisco-IOS-XR-subscriber-session-mon-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.active_sessions is not None:
                            return True

                        if self.dhcp_ds is not None:
                            return True

                        if self.dhcpv4 is not None:
                            return True

                        if self.dhcpv6 is not None:
                            return True

                        if self.ippkt is not None:
                            return True

                        if self.peak_active_sessions is not None:
                            return True

                        if self.peak_standby_sessions is not None:
                            return True

                        if self.pppoe is not None:
                            return True

                        if self.pppoe_ds is not None:
                            return True

                        if self.standby_sessions is not None:
                            return True

                        if self.total is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                        return meta._meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-session-mon-oper:interface-all-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_all_statistic is not None:
                        for child_ref in self.interface_all_statistic:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                    return meta._meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics']['meta_info']


            class LicenseStatistics(object):
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
                
                .. attribute:: total
                
                	total
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'subscriber-session-mon-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.active_sessions = None
                    self.dhcp_ds = None
                    self.dhcpv4 = None
                    self.dhcpv6 = None
                    self.ippkt = None
                    self.peak_active_sessions = None
                    self.peak_standby_sessions = None
                    self.pppoe = None
                    self.pppoe_ds = None
                    self.standby_sessions = None
                    self.total = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-subscriber-session-mon-oper:license-statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.active_sessions is not None:
                        return True

                    if self.dhcp_ds is not None:
                        return True

                    if self.dhcpv4 is not None:
                        return True

                    if self.dhcpv6 is not None:
                        return True

                    if self.ippkt is not None:
                        return True

                    if self.peak_active_sessions is not None:
                        return True

                    if self.peak_standby_sessions is not None:
                        return True

                    if self.pppoe is not None:
                        return True

                    if self.pppoe_ds is not None:
                        return True

                    if self.standby_sessions is not None:
                        return True

                    if self.total is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                    return meta._meta_table['SessionMon.Nodes.Node.LicenseStatistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_id is None:
                    raise YPYModelError('Key property node_id is None')

                return '/Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/Cisco-IOS-XR-subscriber-session-mon-oper:nodes/Cisco-IOS-XR-subscriber-session-mon-oper:node[Cisco-IOS-XR-subscriber-session-mon-oper:node-id = ' + str(self.node_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_id is not None:
                    return True

                if self.interface_all_statistics is not None and self.interface_all_statistics._has_data():
                    return True

                if self.license_statistics is not None and self.license_statistics._has_data():
                    return True

                if self.session_mon_statistics is not None and self.session_mon_statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
                return meta._meta_table['SessionMon.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-subscriber-session-mon-oper:session-mon/Cisco-IOS-XR-subscriber-session-mon-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
            return meta._meta_table['SessionMon.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-subscriber-session-mon-oper:session-mon'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_subscriber_session_mon_oper as meta
        return meta._meta_table['SessionMon']['meta_info']


