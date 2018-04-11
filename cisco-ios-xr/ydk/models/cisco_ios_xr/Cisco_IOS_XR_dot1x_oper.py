""" Cisco_IOS_XR_dot1x_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dot1x package operational data.

This module contains definitions
for the following management objects\:
  dot1x\: Dot1x operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Dot1X(Entity):
    """
    Dot1x operational data
    
    .. attribute:: statistics
    
    	Dot1x operational data
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Statistics>`
    
    .. attribute:: nodes
    
    	Node\-specific Dot1x operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes>`
    
    .. attribute:: session
    
    	Dot1x operational data
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session>`
    
    

    """

    _prefix = 'dot1x-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dot1X, self).__init__()
        self._top_entity = None

        self.yang_name = "dot1x"
        self.yang_parent_name = "Cisco-IOS-XR-dot1x-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("statistics", ("statistics", Dot1X.Statistics)), ("nodes", ("nodes", Dot1X.Nodes)), ("session", ("session", Dot1X.Session))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.statistics = Dot1X.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"
        self._children_yang_names.add("statistics")

        self.nodes = Dot1X.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.session = Dot1X.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")
        self._segment_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x"


    class Statistics(Entity):
        """
        Dot1x operational data
        
        .. attribute:: interface_statistics
        
        	Interfaces with Dot1x
        	**type**\:  :py:class:`InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Statistics.InterfaceStatistics>`
        
        

        """

        _prefix = 'dot1x-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1X.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("interface-statistics", ("interface_statistics", Dot1X.Statistics.InterfaceStatistics))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.interface_statistics = Dot1X.Statistics.InterfaceStatistics()
            self.interface_statistics.parent = self
            self._children_name_map["interface_statistics"] = "interface-statistics"
            self._children_yang_names.add("interface-statistics")
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/%s" % self._segment_path()


        class InterfaceStatistics(Entity):
            """
            Interfaces with Dot1x
            
            .. attribute:: interface_statistic
            
            	Dot1x Data for that Interface
            	**type**\: list of  		 :py:class:`InterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic>`
            
            

            """

            _prefix = 'dot1x-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1X.Statistics.InterfaceStatistics, self).__init__()

                self.yang_name = "interface-statistics"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface-statistic", ("interface_statistic", Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic))])
                self._leafs = OrderedDict()

                self.interface_statistic = YList(self)
                self._segment_path = lambda: "interface-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/statistics/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1X.Statistics.InterfaceStatistics, [], name, value)


            class InterfaceStatistic(Entity):
                """
                Dot1x Data for that Interface
                
                .. attribute:: name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: idb
                
                	Dot1x interface database Statistics
                	**type**\:  :py:class:`Idb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Idb>`
                
                .. attribute:: auth
                
                	Dot1x Authenticator Port Statistics
                	**type**\:  :py:class:`Auth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Auth>`
                
                .. attribute:: supp
                
                	Dot1x Supplicant Port Statistics
                	**type**\:  :py:class:`Supp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Supp>`
                
                .. attribute:: interface_name
                
                	Interface Display name 
                	**type**\: str
                
                .. attribute:: pae
                
                	PAE type on interface
                	**type**\: str
                
                

                """

                _prefix = 'dot1x-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic, self).__init__()

                    self.yang_name = "interface-statistic"
                    self.yang_parent_name = "interface-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("idb", ("idb", Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Idb)), ("auth", ("auth", Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Auth)), ("supp", ("supp", Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Supp))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('pae', YLeaf(YType.str, 'pae')),
                    ])
                    self.name = None
                    self.interface_name = None
                    self.pae = None

                    self.idb = Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Idb()
                    self.idb.parent = self
                    self._children_name_map["idb"] = "idb"
                    self._children_yang_names.add("idb")

                    self.auth = Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Auth()
                    self.auth.parent = self
                    self._children_name_map["auth"] = "auth"
                    self._children_yang_names.add("auth")

                    self.supp = Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Supp()
                    self.supp.parent = self
                    self._children_name_map["supp"] = "supp"
                    self._children_yang_names.add("supp")
                    self._segment_path = lambda: "interface-statistic" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/statistics/interface-statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic, ['name', 'interface_name', 'pae'], name, value)


                class Idb(Entity):
                    """
                    Dot1x interface database Statistics
                    
                    .. attribute:: rx_total
                    
                    	RxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_total
                    
                    	TxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_rx_on_intf_down
                    
                    	NoRxOnIntfDown
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Idb, self).__init__()

                        self.yang_name = "idb"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                            ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                            ('no_rx_on_intf_down', YLeaf(YType.uint32, 'no-rx-on-intf-down')),
                        ])
                        self.rx_total = None
                        self.tx_total = None
                        self.no_rx_on_intf_down = None
                        self._segment_path = lambda: "idb"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Idb, ['rx_total', 'tx_total', 'no_rx_on_intf_down'], name, value)


                class Auth(Entity):
                    """
                    Dot1x Authenticator Port Statistics
                    
                    .. attribute:: rx_start
                    
                    	RxStart
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_logoff
                    
                    	RxLogoff
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_resp
                    
                    	RxResp
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_resp_id
                    
                    	RxRespID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_invalid
                    
                    	RxInvalid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_len_err
                    
                    	RxLenErr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_my_mac_err
                    
                    	RxMyMacErr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_total
                    
                    	RxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_req
                    
                    	TxReq
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_reqid
                    
                    	TxReqID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_total
                    
                    	TxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Auth, self).__init__()

                        self.yang_name = "auth"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rx_start', YLeaf(YType.uint32, 'rx-start')),
                            ('rx_logoff', YLeaf(YType.uint32, 'rx-logoff')),
                            ('rx_resp', YLeaf(YType.uint32, 'rx-resp')),
                            ('rx_resp_id', YLeaf(YType.uint32, 'rx-resp-id')),
                            ('rx_invalid', YLeaf(YType.uint32, 'rx-invalid')),
                            ('rx_len_err', YLeaf(YType.uint32, 'rx-len-err')),
                            ('rx_my_mac_err', YLeaf(YType.uint32, 'rx-my-mac-err')),
                            ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                            ('tx_req', YLeaf(YType.uint32, 'tx-req')),
                            ('tx_reqid', YLeaf(YType.uint32, 'tx-reqid')),
                            ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                        ])
                        self.rx_start = None
                        self.rx_logoff = None
                        self.rx_resp = None
                        self.rx_resp_id = None
                        self.rx_invalid = None
                        self.rx_len_err = None
                        self.rx_my_mac_err = None
                        self.rx_total = None
                        self.tx_req = None
                        self.tx_reqid = None
                        self.tx_total = None
                        self._segment_path = lambda: "auth"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Auth, ['rx_start', 'rx_logoff', 'rx_resp', 'rx_resp_id', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_req', 'tx_reqid', 'tx_total'], name, value)


                class Supp(Entity):
                    """
                    Dot1x Supplicant Port Statistics
                    
                    .. attribute:: rx_req
                    
                    	RxReq
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_invalid
                    
                    	RxInvalid
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_len_err
                    
                    	RxLenErr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_my_mac_err
                    
                    	RxMyMacErr
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_total
                    
                    	RxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_start
                    
                    	TxStart
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_logoff
                    
                    	TxLogoff
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_resp
                    
                    	TxResp
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tx_total
                    
                    	TxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Supp, self).__init__()

                        self.yang_name = "supp"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rx_req', YLeaf(YType.uint32, 'rx-req')),
                            ('rx_invalid', YLeaf(YType.uint32, 'rx-invalid')),
                            ('rx_len_err', YLeaf(YType.uint32, 'rx-len-err')),
                            ('rx_my_mac_err', YLeaf(YType.uint32, 'rx-my-mac-err')),
                            ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                            ('tx_start', YLeaf(YType.uint32, 'tx-start')),
                            ('tx_logoff', YLeaf(YType.uint32, 'tx-logoff')),
                            ('tx_resp', YLeaf(YType.uint32, 'tx-resp')),
                            ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                        ])
                        self.rx_req = None
                        self.rx_invalid = None
                        self.rx_len_err = None
                        self.rx_my_mac_err = None
                        self.rx_total = None
                        self.tx_start = None
                        self.tx_logoff = None
                        self.tx_resp = None
                        self.tx_total = None
                        self._segment_path = lambda: "supp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Statistics.InterfaceStatistics.InterfaceStatistic.Supp, ['rx_req', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_start', 'tx_logoff', 'tx_resp', 'tx_total'], name, value)


    class Nodes(Entity):
        """
        Node\-specific Dot1x operational data
        
        .. attribute:: node
        
        	Dot1x operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node>`
        
        

        """

        _prefix = 'dot1x-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1X.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Dot1X.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Dot1X.Nodes, [], name, value)


        class Node(Entity):
            """
            Dot1x operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: dot1x_defaults
            
            	Dot1x Default Values
            	**type**\:  :py:class:`Dot1XDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Dot1XDefaults>`
            
            .. attribute:: statistics
            
            	Dot1x Default Values
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'dot1x-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1X.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("dot1x-defaults", ("dot1x_defaults", Dot1X.Nodes.Node.Dot1XDefaults)), ("statistics", ("statistics", Dot1X.Nodes.Node.Statistics))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.dot1x_defaults = Dot1X.Nodes.Node.Dot1XDefaults()
                self.dot1x_defaults.parent = self
                self._children_name_map["dot1x_defaults"] = "dot1x-defaults"
                self._children_yang_names.add("dot1x-defaults")

                self.statistics = Dot1X.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1X.Nodes.Node, ['node_name'], name, value)


            class Dot1XDefaults(Entity):
                """
                Dot1x Default Values
                
                .. attribute:: auth_timers
                
                	Dot1x Authenticator default Timer values
                	**type**\:  :py:class:`AuthTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Dot1XDefaults.AuthTimers>`
                
                .. attribute:: supp_timers
                
                	Dot1x Supllicant default Timer values
                	**type**\:  :py:class:`SuppTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Dot1XDefaults.SuppTimers>`
                
                .. attribute:: version
                
                	Dot1x Protocol Version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dot1x-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1X.Nodes.Node.Dot1XDefaults, self).__init__()

                    self.yang_name = "dot1x-defaults"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("auth-timers", ("auth_timers", Dot1X.Nodes.Node.Dot1XDefaults.AuthTimers)), ("supp-timers", ("supp_timers", Dot1X.Nodes.Node.Dot1XDefaults.SuppTimers))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('version', YLeaf(YType.uint32, 'version')),
                    ])
                    self.version = None

                    self.auth_timers = Dot1X.Nodes.Node.Dot1XDefaults.AuthTimers()
                    self.auth_timers.parent = self
                    self._children_name_map["auth_timers"] = "auth-timers"
                    self._children_yang_names.add("auth-timers")

                    self.supp_timers = Dot1X.Nodes.Node.Dot1XDefaults.SuppTimers()
                    self.supp_timers.parent = self
                    self._children_name_map["supp_timers"] = "supp-timers"
                    self._children_yang_names.add("supp-timers")
                    self._segment_path = lambda: "dot1x-defaults"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1X.Nodes.Node.Dot1XDefaults, ['version'], name, value)


                class AuthTimers(Entity):
                    """
                    Dot1x Authenticator default Timer values
                    
                    .. attribute:: quiet_period
                    
                    	in Seconds, authenticator remains quiet (in the HELD state) following a failed authentication exchange before trying to reauthenticate the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: tx_period
                    
                    	in Seconds, Timeout for supplicant reply, authenticator\-to\-supplicant retransmission time for EAP\-request\-ID packets (assuming that no response is received) from the client
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: max_reauth_req
                    
                    	Max No. of Reauthentication Attempts (or) retransmits an EAP\-request\-ID frame to the client before restarting the authentication process
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: supp_timeout
                    
                    	in Seconds, Timeout for supplicant reply, authenticator\-to\-supplicant retransmission time for all EAP messages except for EAP Request ID packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: max_req
                    
                    	Max No. of EAP\-Req (except for EAP\-Request\-ID) retransmits (authenticator\-to\-supplicant) before sending EAP\-Failure
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reauth_period
                    
                    	in Seconds,  after which an automatic reauthentication should be initiated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Nodes.Node.Dot1XDefaults.AuthTimers, self).__init__()

                        self.yang_name = "auth-timers"
                        self.yang_parent_name = "dot1x-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('quiet_period', YLeaf(YType.uint32, 'quiet-period')),
                            ('tx_period', YLeaf(YType.uint32, 'tx-period')),
                            ('max_reauth_req', YLeaf(YType.uint32, 'max-reauth-req')),
                            ('supp_timeout', YLeaf(YType.uint32, 'supp-timeout')),
                            ('max_req', YLeaf(YType.uint32, 'max-req')),
                            ('reauth_period', YLeaf(YType.uint32, 'reauth-period')),
                        ])
                        self.quiet_period = None
                        self.tx_period = None
                        self.max_reauth_req = None
                        self.supp_timeout = None
                        self.max_req = None
                        self.reauth_period = None
                        self._segment_path = lambda: "auth-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Nodes.Node.Dot1XDefaults.AuthTimers, ['quiet_period', 'tx_period', 'max_reauth_req', 'supp_timeout', 'max_req', 'reauth_period'], name, value)


                class SuppTimers(Entity):
                    """
                    Dot1x Supllicant default Timer values
                    
                    .. attribute:: auth_period
                    
                    	in Seconds, supplicant waits for a response from an authenticator except for EAPOL\-START before timing out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: held_period
                    
                    	in Seconds, supplicant will stay in the HELD state (that is, the length of time it will wait before trying to send the credentials again after a failed attempt)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: start_period
                    
                    	Configures the interval, in seconds, between two successive EAPOL\-Start frames when they are being retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: max_start
                    
                    	Max No. of EAPOL\-Start frames supplicant can send to the authenticator
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Nodes.Node.Dot1XDefaults.SuppTimers, self).__init__()

                        self.yang_name = "supp-timers"
                        self.yang_parent_name = "dot1x-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('auth_period', YLeaf(YType.uint32, 'auth-period')),
                            ('held_period', YLeaf(YType.uint32, 'held-period')),
                            ('start_period', YLeaf(YType.uint32, 'start-period')),
                            ('max_start', YLeaf(YType.uint32, 'max-start')),
                        ])
                        self.auth_period = None
                        self.held_period = None
                        self.start_period = None
                        self.max_start = None
                        self._segment_path = lambda: "supp-timers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Nodes.Node.Dot1XDefaults.SuppTimers, ['auth_period', 'held_period', 'start_period', 'max_start'], name, value)


            class Statistics(Entity):
                """
                Dot1x Default Values
                
                .. attribute:: gl_stats
                
                	Global statistics
                	**type**\:  :py:class:`GlStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Statistics.GlStats>`
                
                .. attribute:: if_stats
                
                	dot1x interface statistics list
                	**type**\: list of  		 :py:class:`IfStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Statistics.IfStats>`
                
                

                """

                _prefix = 'dot1x-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1X.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("gl-stats", ("gl_stats", Dot1X.Nodes.Node.Statistics.GlStats))])
                    self._child_list_classes = OrderedDict([("if-stats", ("if_stats", Dot1X.Nodes.Node.Statistics.IfStats))])
                    self._leafs = OrderedDict()

                    self.gl_stats = Dot1X.Nodes.Node.Statistics.GlStats()
                    self.gl_stats.parent = self
                    self._children_name_map["gl_stats"] = "gl-stats"
                    self._children_yang_names.add("gl-stats")

                    self.if_stats = YList(self)
                    self._segment_path = lambda: "statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1X.Nodes.Node.Statistics, [], name, value)


                class GlStats(Entity):
                    """
                    Global statistics
                    
                    .. attribute:: tx_total
                    
                    	TxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_total
                    
                    	RxTotal
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rx_no_idb
                    
                    	RxNoIDB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Nodes.Node.Statistics.GlStats, self).__init__()

                        self.yang_name = "gl-stats"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                            ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                            ('rx_no_idb', YLeaf(YType.uint32, 'rx-no-idb')),
                        ])
                        self.tx_total = None
                        self.rx_total = None
                        self.rx_no_idb = None
                        self._segment_path = lambda: "gl-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Nodes.Node.Statistics.GlStats, ['tx_total', 'rx_total', 'rx_no_idb'], name, value)


                class IfStats(Entity):
                    """
                    dot1x interface statistics list
                    
                    .. attribute:: idb
                    
                    	Dot1x interface database Statistics
                    	**type**\:  :py:class:`Idb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Statistics.IfStats.Idb>`
                    
                    .. attribute:: auth
                    
                    	Dot1x Authenticator Port Statistics
                    	**type**\:  :py:class:`Auth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Statistics.IfStats.Auth>`
                    
                    .. attribute:: supp
                    
                    	Dot1x Supplicant Port Statistics
                    	**type**\:  :py:class:`Supp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Nodes.Node.Statistics.IfStats.Supp>`
                    
                    .. attribute:: interface_name
                    
                    	Interface Display name 
                    	**type**\: str
                    
                    .. attribute:: pae
                    
                    	PAE type on interface
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Nodes.Node.Statistics.IfStats, self).__init__()

                        self.yang_name = "if-stats"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("idb", ("idb", Dot1X.Nodes.Node.Statistics.IfStats.Idb)), ("auth", ("auth", Dot1X.Nodes.Node.Statistics.IfStats.Auth)), ("supp", ("supp", Dot1X.Nodes.Node.Statistics.IfStats.Supp))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('pae', YLeaf(YType.str, 'pae')),
                        ])
                        self.interface_name = None
                        self.pae = None

                        self.idb = Dot1X.Nodes.Node.Statistics.IfStats.Idb()
                        self.idb.parent = self
                        self._children_name_map["idb"] = "idb"
                        self._children_yang_names.add("idb")

                        self.auth = Dot1X.Nodes.Node.Statistics.IfStats.Auth()
                        self.auth.parent = self
                        self._children_name_map["auth"] = "auth"
                        self._children_yang_names.add("auth")

                        self.supp = Dot1X.Nodes.Node.Statistics.IfStats.Supp()
                        self.supp.parent = self
                        self._children_name_map["supp"] = "supp"
                        self._children_yang_names.add("supp")
                        self._segment_path = lambda: "if-stats"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Nodes.Node.Statistics.IfStats, ['interface_name', 'pae'], name, value)


                    class Idb(Entity):
                        """
                        Dot1x interface database Statistics
                        
                        .. attribute:: rx_total
                        
                        	RxTotal
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_total
                        
                        	TxTotal
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_rx_on_intf_down
                        
                        	NoRxOnIntfDown
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1X.Nodes.Node.Statistics.IfStats.Idb, self).__init__()

                            self.yang_name = "idb"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                                ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                                ('no_rx_on_intf_down', YLeaf(YType.uint32, 'no-rx-on-intf-down')),
                            ])
                            self.rx_total = None
                            self.tx_total = None
                            self.no_rx_on_intf_down = None
                            self._segment_path = lambda: "idb"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1X.Nodes.Node.Statistics.IfStats.Idb, ['rx_total', 'tx_total', 'no_rx_on_intf_down'], name, value)


                    class Auth(Entity):
                        """
                        Dot1x Authenticator Port Statistics
                        
                        .. attribute:: rx_start
                        
                        	RxStart
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_logoff
                        
                        	RxLogoff
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_resp
                        
                        	RxResp
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_resp_id
                        
                        	RxRespID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_invalid
                        
                        	RxInvalid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_len_err
                        
                        	RxLenErr
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_my_mac_err
                        
                        	RxMyMacErr
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_total
                        
                        	RxTotal
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_req
                        
                        	TxReq
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_reqid
                        
                        	TxReqID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_total
                        
                        	TxTotal
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1X.Nodes.Node.Statistics.IfStats.Auth, self).__init__()

                            self.yang_name = "auth"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rx_start', YLeaf(YType.uint32, 'rx-start')),
                                ('rx_logoff', YLeaf(YType.uint32, 'rx-logoff')),
                                ('rx_resp', YLeaf(YType.uint32, 'rx-resp')),
                                ('rx_resp_id', YLeaf(YType.uint32, 'rx-resp-id')),
                                ('rx_invalid', YLeaf(YType.uint32, 'rx-invalid')),
                                ('rx_len_err', YLeaf(YType.uint32, 'rx-len-err')),
                                ('rx_my_mac_err', YLeaf(YType.uint32, 'rx-my-mac-err')),
                                ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                                ('tx_req', YLeaf(YType.uint32, 'tx-req')),
                                ('tx_reqid', YLeaf(YType.uint32, 'tx-reqid')),
                                ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                            ])
                            self.rx_start = None
                            self.rx_logoff = None
                            self.rx_resp = None
                            self.rx_resp_id = None
                            self.rx_invalid = None
                            self.rx_len_err = None
                            self.rx_my_mac_err = None
                            self.rx_total = None
                            self.tx_req = None
                            self.tx_reqid = None
                            self.tx_total = None
                            self._segment_path = lambda: "auth"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1X.Nodes.Node.Statistics.IfStats.Auth, ['rx_start', 'rx_logoff', 'rx_resp', 'rx_resp_id', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_req', 'tx_reqid', 'tx_total'], name, value)


                    class Supp(Entity):
                        """
                        Dot1x Supplicant Port Statistics
                        
                        .. attribute:: rx_req
                        
                        	RxReq
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_invalid
                        
                        	RxInvalid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_len_err
                        
                        	RxLenErr
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_my_mac_err
                        
                        	RxMyMacErr
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rx_total
                        
                        	RxTotal
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_start
                        
                        	TxStart
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_logoff
                        
                        	TxLogoff
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_resp
                        
                        	TxResp
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tx_total
                        
                        	TxTotal
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1X.Nodes.Node.Statistics.IfStats.Supp, self).__init__()

                            self.yang_name = "supp"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rx_req', YLeaf(YType.uint32, 'rx-req')),
                                ('rx_invalid', YLeaf(YType.uint32, 'rx-invalid')),
                                ('rx_len_err', YLeaf(YType.uint32, 'rx-len-err')),
                                ('rx_my_mac_err', YLeaf(YType.uint32, 'rx-my-mac-err')),
                                ('rx_total', YLeaf(YType.uint32, 'rx-total')),
                                ('tx_start', YLeaf(YType.uint32, 'tx-start')),
                                ('tx_logoff', YLeaf(YType.uint32, 'tx-logoff')),
                                ('tx_resp', YLeaf(YType.uint32, 'tx-resp')),
                                ('tx_total', YLeaf(YType.uint32, 'tx-total')),
                            ])
                            self.rx_req = None
                            self.rx_invalid = None
                            self.rx_len_err = None
                            self.rx_my_mac_err = None
                            self.rx_total = None
                            self.tx_start = None
                            self.tx_logoff = None
                            self.tx_resp = None
                            self.tx_total = None
                            self._segment_path = lambda: "supp"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1X.Nodes.Node.Statistics.IfStats.Supp, ['rx_req', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_start', 'tx_logoff', 'tx_resp', 'tx_total'], name, value)


    class Session(Entity):
        """
        Dot1x operational data
        
        .. attribute:: interface_sessions
        
        	Interfaces with Dot1x
        	**type**\:  :py:class:`InterfaceSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions>`
        
        

        """

        _prefix = 'dot1x-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1X.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("interface-sessions", ("interface_sessions", Dot1X.Session.InterfaceSessions))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.interface_sessions = Dot1X.Session.InterfaceSessions()
            self.interface_sessions.parent = self
            self._children_name_map["interface_sessions"] = "interface-sessions"
            self._children_yang_names.add("interface-sessions")
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/%s" % self._segment_path()


        class InterfaceSessions(Entity):
            """
            Interfaces with Dot1x
            
            .. attribute:: interface_session
            
            	Dot1x Data for that Interface
            	**type**\: list of  		 :py:class:`InterfaceSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession>`
            
            

            """

            _prefix = 'dot1x-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1X.Session.InterfaceSessions, self).__init__()

                self.yang_name = "interface-sessions"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("interface-session", ("interface_session", Dot1X.Session.InterfaceSessions.InterfaceSession))])
                self._leafs = OrderedDict()

                self.interface_session = YList(self)
                self._segment_path = lambda: "interface-sessions"
                self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/session/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1X.Session.InterfaceSessions, [], name, value)


            class InterfaceSession(Entity):
                """
                Dot1x Data for that Interface
                
                .. attribute:: name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: intf_info
                
                	Dot1x interface Info
                	**type**\:  :py:class:`IntfInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo>`
                
                .. attribute:: mka_status_info
                
                	MKA session secure status
                	**type**\:  :py:class:`MkaStatusInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo>`
                
                .. attribute:: interface_name
                
                	Interface Display name 
                	**type**\: str
                
                .. attribute:: interface_sname
                
                	Interface Display short\_name 
                	**type**\: str
                
                .. attribute:: if_handle
                
                	Interface handle
                	**type**\: str
                
                .. attribute:: mac
                
                	formatted MAC Address
                	**type**\: str
                
                .. attribute:: ethertype
                
                	EAPOL Ethertype
                	**type**\: str
                
                

                """

                _prefix = 'dot1x-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1X.Session.InterfaceSessions.InterfaceSession, self).__init__()

                    self.yang_name = "interface-session"
                    self.yang_parent_name = "interface-sessions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([("intf-info", ("intf_info", Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo)), ("mka-status-info", ("mka_status_info", Dot1X.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('interface_sname', YLeaf(YType.str, 'interface-sname')),
                        ('if_handle', YLeaf(YType.str, 'if-handle')),
                        ('mac', YLeaf(YType.str, 'mac')),
                        ('ethertype', YLeaf(YType.str, 'ethertype')),
                    ])
                    self.name = None
                    self.interface_name = None
                    self.interface_sname = None
                    self.if_handle = None
                    self.mac = None
                    self.ethertype = None

                    self.intf_info = Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo()
                    self.intf_info.parent = self
                    self._children_name_map["intf_info"] = "intf-info"
                    self._children_yang_names.add("intf-info")

                    self.mka_status_info = Dot1X.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo()
                    self.mka_status_info.parent = self
                    self._children_name_map["mka_status_info"] = "mka-status-info"
                    self._children_yang_names.add("mka-status-info")
                    self._segment_path = lambda: "interface-session" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/session/interface-sessions/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession, ['name', 'interface_name', 'interface_sname', 'if_handle', 'mac', 'ethertype'], name, value)


                class IntfInfo(Entity):
                    """
                    Dot1x interface Info
                    
                    .. attribute:: auth_info
                    
                    	Dot1x Authenticator info
                    	**type**\:  :py:class:`AuthInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo>`
                    
                    .. attribute:: supp_info
                    
                    	Dot1x Supplicant info
                    	**type**\:  :py:class:`SuppInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo>`
                    
                    .. attribute:: pae
                    
                    	PAE type on interface
                    	**type**\: str
                    
                    .. attribute:: port_status
                    
                    	Dot1x Port Status
                    	**type**\: str
                    
                    .. attribute:: dot1x_profile
                    
                    	Dot1x Profile
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo, self).__init__()

                        self.yang_name = "intf-info"
                        self.yang_parent_name = "interface-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("auth-info", ("auth_info", Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo)), ("supp-info", ("supp_info", Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pae', YLeaf(YType.str, 'pae')),
                            ('port_status', YLeaf(YType.str, 'port-status')),
                            ('dot1x_profile', YLeaf(YType.str, 'dot1x-profile')),
                        ])
                        self.pae = None
                        self.port_status = None
                        self.dot1x_profile = None

                        self.auth_info = Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo()
                        self.auth_info.parent = self
                        self._children_name_map["auth_info"] = "auth-info"
                        self._children_yang_names.add("auth-info")

                        self.supp_info = Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo()
                        self.supp_info.parent = self
                        self._children_name_map["supp_info"] = "supp-info"
                        self._children_yang_names.add("supp-info")
                        self._segment_path = lambda: "intf-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo, ['pae', 'port_status', 'dot1x_profile'], name, value)


                    class AuthInfo(Entity):
                        """
                        Dot1x Authenticator info
                        
                        .. attribute:: reauth
                        
                        	Re\-Authentication enabled status
                        	**type**\: str
                        
                        .. attribute:: config_dependency
                        
                        	Configuration Dependency 
                        	**type**\: str
                        
                        .. attribute:: client
                        
                        	Authenticator client list
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client>`
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo, self).__init__()

                            self.yang_name = "auth-info"
                            self.yang_parent_name = "intf-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("client", ("client", Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client))])
                            self._leafs = OrderedDict([
                                ('reauth', YLeaf(YType.str, 'reauth')),
                                ('config_dependency', YLeaf(YType.str, 'config-dependency')),
                            ])
                            self.reauth = None
                            self.config_dependency = None

                            self.client = YList(self)
                            self._segment_path = lambda: "auth-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo, ['reauth', 'config_dependency'], name, value)


                        class Client(Entity):
                            """
                            Authenticator client list
                            
                            .. attribute:: mac
                            
                            	formatted MAC Address
                            	**type**\: str
                            
                            .. attribute:: auth_sm_state
                            
                            	Auth SM State
                            	**type**\: str
                            
                            .. attribute:: auth_bend_sm_state
                            
                            	Auth back end SM State
                            	**type**\: str
                            
                            .. attribute:: time_to_next_reauth
                            
                            	remaining time for next reauthentication
                            	**type**\: str
                            
                            .. attribute:: last_auth_time
                            
                            	Last Authenticated Timestamp (formatted)
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'dot1x-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "auth-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mac', YLeaf(YType.str, 'mac')),
                                    ('auth_sm_state', YLeaf(YType.str, 'auth-sm-state')),
                                    ('auth_bend_sm_state', YLeaf(YType.str, 'auth-bend-sm-state')),
                                    ('time_to_next_reauth', YLeaf(YType.str, 'time-to-next-reauth')),
                                    ('last_auth_time', YLeaf(YType.str, 'last-auth-time')),
                                ])
                                self.mac = None
                                self.auth_sm_state = None
                                self.auth_bend_sm_state = None
                                self.time_to_next_reauth = None
                                self.last_auth_time = None
                                self._segment_path = lambda: "client"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client, ['mac', 'auth_sm_state', 'auth_bend_sm_state', 'time_to_next_reauth', 'last_auth_time'], name, value)


                    class SuppInfo(Entity):
                        """
                        Dot1x Supplicant info
                        
                        .. attribute:: eap_profile
                        
                        	EAP profile
                        	**type**\: str
                        
                        .. attribute:: config_dependency
                        
                        	Configuration Dependency 
                        	**type**\: str
                        
                        .. attribute:: client
                        
                        	Supp Client info
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client>`
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo, self).__init__()

                            self.yang_name = "supp-info"
                            self.yang_parent_name = "intf-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("client", ("client", Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client))])
                            self._leafs = OrderedDict([
                                ('eap_profile', YLeaf(YType.str, 'eap-profile')),
                                ('config_dependency', YLeaf(YType.str, 'config-dependency')),
                            ])
                            self.eap_profile = None
                            self.config_dependency = None

                            self.client = YList(self)
                            self._segment_path = lambda: "supp-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo, ['eap_profile', 'config_dependency'], name, value)


                        class Client(Entity):
                            """
                            Supp Client info
                            
                            .. attribute:: mac
                            
                            	formatted MAC Address
                            	**type**\: str
                            
                            .. attribute:: eap_method
                            
                            	EAP Method
                            	**type**\: str
                            
                            .. attribute:: last_auth_time
                            
                            	Last Authenticated Timestamp (formatted)
                            	**type**\: str
                            
                            .. attribute:: auth_sm_state
                            
                            	supp SM State
                            	**type**\: str
                            
                            .. attribute:: auth_bend_sm_state
                            
                            	supp back end SM State
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'dot1x-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "supp-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mac', YLeaf(YType.str, 'mac')),
                                    ('eap_method', YLeaf(YType.str, 'eap-method')),
                                    ('last_auth_time', YLeaf(YType.str, 'last-auth-time')),
                                    ('auth_sm_state', YLeaf(YType.str, 'auth-sm-state')),
                                    ('auth_bend_sm_state', YLeaf(YType.str, 'auth-bend-sm-state')),
                                ])
                                self.mac = None
                                self.eap_method = None
                                self.last_auth_time = None
                                self.auth_sm_state = None
                                self.auth_bend_sm_state = None
                                self._segment_path = lambda: "client"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client, ['mac', 'eap_method', 'last_auth_time', 'auth_sm_state', 'auth_bend_sm_state'], name, value)


                class MkaStatusInfo(Entity):
                    """
                    MKA session secure status
                    
                    .. attribute:: tie_break_role
                    
                    	Dot1x Tie breaker role chosen for mka when PAE type is BOTH
                    	**type**\: str
                    
                    .. attribute:: eap_based_macsec
                    
                    	EAP Mode status for MKA
                    	**type**\: str
                    
                    .. attribute:: mka_start_time
                    
                    	Time stamp when Dot1x posting a message to  MKA to start session
                    	**type**\: str
                    
                    .. attribute:: mka_stop_time
                    
                    	Time stamp when Dot1x posting a message to  MKA to stop session
                    	**type**\: str
                    
                    .. attribute:: mka_response_time
                    
                    	Time Stamp of MKA acknowledgement to Dot1x
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1X.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo, self).__init__()

                        self.yang_name = "mka-status-info"
                        self.yang_parent_name = "interface-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tie_break_role', YLeaf(YType.str, 'tie-break-role')),
                            ('eap_based_macsec', YLeaf(YType.str, 'eap-based-macsec')),
                            ('mka_start_time', YLeaf(YType.str, 'mka-start-time')),
                            ('mka_stop_time', YLeaf(YType.str, 'mka-stop-time')),
                            ('mka_response_time', YLeaf(YType.str, 'mka-response-time')),
                        ])
                        self.tie_break_role = None
                        self.eap_based_macsec = None
                        self.mka_start_time = None
                        self.mka_stop_time = None
                        self.mka_response_time = None
                        self._segment_path = lambda: "mka-status-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1X.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo, ['tie_break_role', 'eap_based_macsec', 'mka_start_time', 'mka_stop_time', 'mka_response_time'], name, value)

    def clone_ptr(self):
        self._top_entity = Dot1X()
        return self._top_entity

