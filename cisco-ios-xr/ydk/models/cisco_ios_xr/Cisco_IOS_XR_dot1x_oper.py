""" Cisco_IOS_XR_dot1x_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dot1x package operational data.

This module contains definitions
for the following management objects\:
  dot1x\: Dot1x operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Dot1x(Entity):
    """
    Dot1x operational data
    
    .. attribute:: statistics
    
    	Dot1x operational data
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics>`
    
    .. attribute:: nodes
    
    	Node\-specific Dot1x operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes>`
    
    .. attribute:: session
    
    	Dot1x operational data
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session>`
    
    

    """

    _prefix = 'dot1x-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dot1x, self).__init__()
        self._top_entity = None

        self.yang_name = "dot1x"
        self.yang_parent_name = "Cisco-IOS-XR-dot1x-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("statistics", ("statistics", Dot1x.Statistics)), ("nodes", ("nodes", Dot1x.Nodes)), ("session", ("session", Dot1x.Session))])
        self._leafs = OrderedDict()

        self.statistics = Dot1x.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"

        self.nodes = Dot1x.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"

        self.session = Dot1x.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._segment_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Dot1x, [], name, value)


    class Statistics(Entity):
        """
        Dot1x operational data
        
        .. attribute:: interface_statistics
        
        	Interfaces with Dot1x
        	**type**\:  :py:class:`InterfaceStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics>`
        
        

        """

        _prefix = 'dot1x-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1x.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-statistics", ("interface_statistics", Dot1x.Statistics.InterfaceStatistics))])
            self._leafs = OrderedDict()

            self.interface_statistics = Dot1x.Statistics.InterfaceStatistics()
            self.interface_statistics.parent = self
            self._children_name_map["interface_statistics"] = "interface-statistics"
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dot1x.Statistics, [], name, value)


        class InterfaceStatistics(Entity):
            """
            Interfaces with Dot1x
            
            .. attribute:: interface_statistic
            
            	Dot1x Data for that Interface
            	**type**\: list of  		 :py:class:`InterfaceStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic>`
            
            

            """

            _prefix = 'dot1x-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1x.Statistics.InterfaceStatistics, self).__init__()

                self.yang_name = "interface-statistics"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-statistic", ("interface_statistic", Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic))])
                self._leafs = OrderedDict()

                self.interface_statistic = YList(self)
                self._segment_path = lambda: "interface-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1x.Statistics.InterfaceStatistics, [], name, value)


            class InterfaceStatistic(Entity):
                """
                Dot1x Data for that Interface
                
                .. attribute:: name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: idb
                
                	Dot1x interface database Statistics
                	**type**\:  :py:class:`Idb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Idb>`
                
                .. attribute:: auth
                
                	Dot1x Authenticator Port Statistics
                	**type**\:  :py:class:`Auth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth>`
                
                .. attribute:: supp
                
                	Dot1x Supplicant Port Statistics
                	**type**\:  :py:class:`Supp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Supp>`
                
                .. attribute:: local_eap
                
                	Dot1x Local EAP Port Statistics
                	**type**\:  :py:class:`LocalEap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.LocalEap>`
                
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
                    super(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic, self).__init__()

                    self.yang_name = "interface-statistic"
                    self.yang_parent_name = "interface-statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("idb", ("idb", Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Idb)), ("auth", ("auth", Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth)), ("supp", ("supp", Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Supp)), ("local-eap", ("local_eap", Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.LocalEap))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('pae', (YLeaf(YType.str, 'pae'), ['str'])),
                    ])
                    self.name = None
                    self.interface_name = None
                    self.pae = None

                    self.idb = Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Idb()
                    self.idb.parent = self
                    self._children_name_map["idb"] = "idb"

                    self.auth = Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth()
                    self.auth.parent = self
                    self._children_name_map["auth"] = "auth"

                    self.supp = Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Supp()
                    self.supp.parent = self
                    self._children_name_map["supp"] = "supp"

                    self.local_eap = Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.LocalEap()
                    self.local_eap.parent = self
                    self._children_name_map["local_eap"] = "local-eap"
                    self._segment_path = lambda: "interface-statistic" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/statistics/interface-statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic, ['name', 'interface_name', 'pae'], name, value)


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
                        super(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Idb, self).__init__()

                        self.yang_name = "idb"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                            ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
                            ('no_rx_on_intf_down', (YLeaf(YType.uint32, 'no-rx-on-intf-down'), ['int'])),
                        ])
                        self.rx_total = None
                        self.tx_total = None
                        self.no_rx_on_intf_down = None
                        self._segment_path = lambda: "idb"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Idb, ['rx_total', 'tx_total', 'no_rx_on_intf_down'], name, value)


                class Auth(Entity):
                    """
                    Dot1x Authenticator Port Statistics
                    
                    .. attribute:: port_control
                    
                    	PortControl
                    	**type**\:  :py:class:`PortControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth.PortControl>`
                    
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
                    
                    .. attribute:: packet_drop_no_config_received
                    
                    	PacketDrop
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth, self).__init__()

                        self.yang_name = "auth"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("port-control", ("port_control", Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth.PortControl))])
                        self._leafs = OrderedDict([
                            ('rx_start', (YLeaf(YType.uint32, 'rx-start'), ['int'])),
                            ('rx_logoff', (YLeaf(YType.uint32, 'rx-logoff'), ['int'])),
                            ('rx_resp', (YLeaf(YType.uint32, 'rx-resp'), ['int'])),
                            ('rx_resp_id', (YLeaf(YType.uint32, 'rx-resp-id'), ['int'])),
                            ('rx_invalid', (YLeaf(YType.uint32, 'rx-invalid'), ['int'])),
                            ('rx_len_err', (YLeaf(YType.uint32, 'rx-len-err'), ['int'])),
                            ('rx_my_mac_err', (YLeaf(YType.uint32, 'rx-my-mac-err'), ['int'])),
                            ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                            ('tx_req', (YLeaf(YType.uint32, 'tx-req'), ['int'])),
                            ('tx_reqid', (YLeaf(YType.uint32, 'tx-reqid'), ['int'])),
                            ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
                            ('packet_drop_no_config_received', (YLeaf(YType.uint32, 'packet-drop-no-config-received'), ['int'])),
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
                        self.packet_drop_no_config_received = None

                        self.port_control = Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth.PortControl()
                        self.port_control.parent = self
                        self._children_name_map["port_control"] = "port-control"
                        self._segment_path = lambda: "auth"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth, ['rx_start', 'rx_logoff', 'rx_resp', 'rx_resp_id', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_req', 'tx_reqid', 'tx_total', 'packet_drop_no_config_received'], name, value)


                    class PortControl(Entity):
                        """
                        PortControl
                        
                        .. attribute:: enable_succ
                        
                        	EnableSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: enable_fail
                        
                        	EnableFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: add_client_succ
                        
                        	AddClientSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: add_client_fail
                        
                        	AddClientFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remove_client_succ
                        
                        	RemoveClientSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remove_client_fail
                        
                        	RemoveClientFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth.PortControl, self).__init__()

                            self.yang_name = "port-control"
                            self.yang_parent_name = "auth"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable_succ', (YLeaf(YType.uint32, 'enable-succ'), ['int'])),
                                ('enable_fail', (YLeaf(YType.uint32, 'enable-fail'), ['int'])),
                                ('add_client_succ', (YLeaf(YType.uint32, 'add-client-succ'), ['int'])),
                                ('add_client_fail', (YLeaf(YType.uint32, 'add-client-fail'), ['int'])),
                                ('remove_client_succ', (YLeaf(YType.uint32, 'remove-client-succ'), ['int'])),
                                ('remove_client_fail', (YLeaf(YType.uint32, 'remove-client-fail'), ['int'])),
                            ])
                            self.enable_succ = None
                            self.enable_fail = None
                            self.add_client_succ = None
                            self.add_client_fail = None
                            self.remove_client_succ = None
                            self.remove_client_fail = None
                            self._segment_path = lambda: "port-control"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Auth.PortControl, ['enable_succ', 'enable_fail', 'add_client_succ', 'add_client_fail', 'remove_client_succ', 'remove_client_fail'], name, value)


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
                        super(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Supp, self).__init__()

                        self.yang_name = "supp"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rx_req', (YLeaf(YType.uint32, 'rx-req'), ['int'])),
                            ('rx_invalid', (YLeaf(YType.uint32, 'rx-invalid'), ['int'])),
                            ('rx_len_err', (YLeaf(YType.uint32, 'rx-len-err'), ['int'])),
                            ('rx_my_mac_err', (YLeaf(YType.uint32, 'rx-my-mac-err'), ['int'])),
                            ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                            ('tx_start', (YLeaf(YType.uint32, 'tx-start'), ['int'])),
                            ('tx_logoff', (YLeaf(YType.uint32, 'tx-logoff'), ['int'])),
                            ('tx_resp', (YLeaf(YType.uint32, 'tx-resp'), ['int'])),
                            ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.Supp, ['rx_req', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_start', 'tx_logoff', 'tx_resp', 'tx_total'], name, value)


                class LocalEap(Entity):
                    """
                    Dot1x Local EAP Port Statistics
                    
                    .. attribute:: requests
                    
                    	Requests
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies
                    
                    	Replies
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: timeout
                    
                    	Timeout
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped_no_eap
                    
                    	DroppedNoEAP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dropped
                    
                    	Dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: success
                    
                    	Success
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed
                    
                    	Failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.LocalEap, self).__init__()

                        self.yang_name = "local-eap"
                        self.yang_parent_name = "interface-statistic"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('requests', (YLeaf(YType.uint32, 'requests'), ['int'])),
                            ('replies', (YLeaf(YType.uint32, 'replies'), ['int'])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                            ('dropped_no_eap', (YLeaf(YType.uint32, 'dropped-no-eap'), ['int'])),
                            ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                            ('success', (YLeaf(YType.uint32, 'success'), ['int'])),
                            ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                        ])
                        self.requests = None
                        self.replies = None
                        self.timeout = None
                        self.dropped_no_eap = None
                        self.dropped = None
                        self.success = None
                        self.failed = None
                        self._segment_path = lambda: "local-eap"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Statistics.InterfaceStatistics.InterfaceStatistic.LocalEap, ['requests', 'replies', 'timeout', 'dropped_no_eap', 'dropped', 'success', 'failed'], name, value)


    class Nodes(Entity):
        """
        Node\-specific Dot1x operational data
        
        .. attribute:: node
        
        	Dot1x operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node>`
        
        

        """

        _prefix = 'dot1x-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1x.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Dot1x.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dot1x.Nodes, [], name, value)


        class Node(Entity):
            """
            Dot1x operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: dot1x_defaults
            
            	Dot1x Default Values
            	**type**\:  :py:class:`Dot1xDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Dot1xDefaults>`
            
            .. attribute:: statistics
            
            	Dot1x Default Values
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'dot1x-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1x.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("dot1x-defaults", ("dot1x_defaults", Dot1x.Nodes.Node.Dot1xDefaults)), ("statistics", ("statistics", Dot1x.Nodes.Node.Statistics))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.dot1x_defaults = Dot1x.Nodes.Node.Dot1xDefaults()
                self.dot1x_defaults.parent = self
                self._children_name_map["dot1x_defaults"] = "dot1x-defaults"

                self.statistics = Dot1x.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1x.Nodes.Node, ['node_name'], name, value)


            class Dot1xDefaults(Entity):
                """
                Dot1x Default Values
                
                .. attribute:: auth_timers
                
                	Dot1x Authenticator default Timer values
                	**type**\:  :py:class:`AuthTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Dot1xDefaults.AuthTimers>`
                
                .. attribute:: supp_timers
                
                	Dot1x Supllicant default Timer values
                	**type**\:  :py:class:`SuppTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Dot1xDefaults.SuppTimers>`
                
                .. attribute:: version
                
                	Dot1x Protocol Version
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dot1x-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1x.Nodes.Node.Dot1xDefaults, self).__init__()

                    self.yang_name = "dot1x-defaults"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("auth-timers", ("auth_timers", Dot1x.Nodes.Node.Dot1xDefaults.AuthTimers)), ("supp-timers", ("supp_timers", Dot1x.Nodes.Node.Dot1xDefaults.SuppTimers))])
                    self._leafs = OrderedDict([
                        ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                    ])
                    self.version = None

                    self.auth_timers = Dot1x.Nodes.Node.Dot1xDefaults.AuthTimers()
                    self.auth_timers.parent = self
                    self._children_name_map["auth_timers"] = "auth-timers"

                    self.supp_timers = Dot1x.Nodes.Node.Dot1xDefaults.SuppTimers()
                    self.supp_timers.parent = self
                    self._children_name_map["supp_timers"] = "supp-timers"
                    self._segment_path = lambda: "dot1x-defaults"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1x.Nodes.Node.Dot1xDefaults, ['version'], name, value)


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
                        super(Dot1x.Nodes.Node.Dot1xDefaults.AuthTimers, self).__init__()

                        self.yang_name = "auth-timers"
                        self.yang_parent_name = "dot1x-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('quiet_period', (YLeaf(YType.uint32, 'quiet-period'), ['int'])),
                            ('tx_period', (YLeaf(YType.uint32, 'tx-period'), ['int'])),
                            ('max_reauth_req', (YLeaf(YType.uint32, 'max-reauth-req'), ['int'])),
                            ('supp_timeout', (YLeaf(YType.uint32, 'supp-timeout'), ['int'])),
                            ('max_req', (YLeaf(YType.uint32, 'max-req'), ['int'])),
                            ('reauth_period', (YLeaf(YType.uint32, 'reauth-period'), ['int'])),
                        ])
                        self.quiet_period = None
                        self.tx_period = None
                        self.max_reauth_req = None
                        self.supp_timeout = None
                        self.max_req = None
                        self.reauth_period = None
                        self._segment_path = lambda: "auth-timers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Nodes.Node.Dot1xDefaults.AuthTimers, ['quiet_period', 'tx_period', 'max_reauth_req', 'supp_timeout', 'max_req', 'reauth_period'], name, value)


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
                        super(Dot1x.Nodes.Node.Dot1xDefaults.SuppTimers, self).__init__()

                        self.yang_name = "supp-timers"
                        self.yang_parent_name = "dot1x-defaults"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('auth_period', (YLeaf(YType.uint32, 'auth-period'), ['int'])),
                            ('held_period', (YLeaf(YType.uint32, 'held-period'), ['int'])),
                            ('start_period', (YLeaf(YType.uint32, 'start-period'), ['int'])),
                            ('max_start', (YLeaf(YType.uint32, 'max-start'), ['int'])),
                        ])
                        self.auth_period = None
                        self.held_period = None
                        self.start_period = None
                        self.max_start = None
                        self._segment_path = lambda: "supp-timers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Nodes.Node.Dot1xDefaults.SuppTimers, ['auth_period', 'held_period', 'start_period', 'max_start'], name, value)


            class Statistics(Entity):
                """
                Dot1x Default Values
                
                .. attribute:: gl_stats
                
                	Global statistics
                	**type**\:  :py:class:`GlStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.GlStats>`
                
                .. attribute:: if_stats
                
                	dot1x interface statistics list
                	**type**\: list of  		 :py:class:`IfStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.IfStats>`
                
                

                """

                _prefix = 'dot1x-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dot1x.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("gl-stats", ("gl_stats", Dot1x.Nodes.Node.Statistics.GlStats)), ("if-stats", ("if_stats", Dot1x.Nodes.Node.Statistics.IfStats))])
                    self._leafs = OrderedDict()

                    self.gl_stats = Dot1x.Nodes.Node.Statistics.GlStats()
                    self.gl_stats.parent = self
                    self._children_name_map["gl_stats"] = "gl-stats"

                    self.if_stats = YList(self)
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1x.Nodes.Node.Statistics, [], name, value)


                class GlStats(Entity):
                    """
                    Global statistics
                    
                    .. attribute:: port_control
                    
                    	PortControl
                    	**type**\:  :py:class:`PortControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.GlStats.PortControl>`
                    
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
                    
                    .. attribute:: packet_drop_no_config_received
                    
                    	PacketDrop
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1x.Nodes.Node.Statistics.GlStats, self).__init__()

                        self.yang_name = "gl-stats"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("port-control", ("port_control", Dot1x.Nodes.Node.Statistics.GlStats.PortControl))])
                        self._leafs = OrderedDict([
                            ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
                            ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                            ('rx_no_idb', (YLeaf(YType.uint32, 'rx-no-idb'), ['int'])),
                            ('packet_drop_no_config_received', (YLeaf(YType.uint32, 'packet-drop-no-config-received'), ['int'])),
                        ])
                        self.tx_total = None
                        self.rx_total = None
                        self.rx_no_idb = None
                        self.packet_drop_no_config_received = None

                        self.port_control = Dot1x.Nodes.Node.Statistics.GlStats.PortControl()
                        self.port_control.parent = self
                        self._children_name_map["port_control"] = "port-control"
                        self._segment_path = lambda: "gl-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Nodes.Node.Statistics.GlStats, ['tx_total', 'rx_total', 'rx_no_idb', 'packet_drop_no_config_received'], name, value)


                    class PortControl(Entity):
                        """
                        PortControl
                        
                        .. attribute:: enable_succ
                        
                        	EnableSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: enable_fail
                        
                        	EnableFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disable_succ
                        
                        	DisableSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: disable_fail
                        
                        	DisableFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: add_client_succ
                        
                        	AddClientSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: add_client_fail
                        
                        	AddClientFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remove_client_succ
                        
                        	RemoveClientSucc
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remove_client_fail
                        
                        	RemoveClientFail
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1x.Nodes.Node.Statistics.GlStats.PortControl, self).__init__()

                            self.yang_name = "port-control"
                            self.yang_parent_name = "gl-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enable_succ', (YLeaf(YType.uint32, 'enable-succ'), ['int'])),
                                ('enable_fail', (YLeaf(YType.uint32, 'enable-fail'), ['int'])),
                                ('disable_succ', (YLeaf(YType.uint32, 'disable-succ'), ['int'])),
                                ('disable_fail', (YLeaf(YType.uint32, 'disable-fail'), ['int'])),
                                ('add_client_succ', (YLeaf(YType.uint32, 'add-client-succ'), ['int'])),
                                ('add_client_fail', (YLeaf(YType.uint32, 'add-client-fail'), ['int'])),
                                ('remove_client_succ', (YLeaf(YType.uint32, 'remove-client-succ'), ['int'])),
                                ('remove_client_fail', (YLeaf(YType.uint32, 'remove-client-fail'), ['int'])),
                            ])
                            self.enable_succ = None
                            self.enable_fail = None
                            self.disable_succ = None
                            self.disable_fail = None
                            self.add_client_succ = None
                            self.add_client_fail = None
                            self.remove_client_succ = None
                            self.remove_client_fail = None
                            self._segment_path = lambda: "port-control"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Nodes.Node.Statistics.GlStats.PortControl, ['enable_succ', 'enable_fail', 'disable_succ', 'disable_fail', 'add_client_succ', 'add_client_fail', 'remove_client_succ', 'remove_client_fail'], name, value)


                class IfStats(Entity):
                    """
                    dot1x interface statistics list
                    
                    .. attribute:: idb
                    
                    	Dot1x interface database Statistics
                    	**type**\:  :py:class:`Idb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.IfStats.Idb>`
                    
                    .. attribute:: auth
                    
                    	Dot1x Authenticator Port Statistics
                    	**type**\:  :py:class:`Auth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.IfStats.Auth>`
                    
                    .. attribute:: supp
                    
                    	Dot1x Supplicant Port Statistics
                    	**type**\:  :py:class:`Supp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.IfStats.Supp>`
                    
                    .. attribute:: local_eap
                    
                    	Dot1x Local EAP Port Statistics
                    	**type**\:  :py:class:`LocalEap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.IfStats.LocalEap>`
                    
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
                        super(Dot1x.Nodes.Node.Statistics.IfStats, self).__init__()

                        self.yang_name = "if-stats"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("idb", ("idb", Dot1x.Nodes.Node.Statistics.IfStats.Idb)), ("auth", ("auth", Dot1x.Nodes.Node.Statistics.IfStats.Auth)), ("supp", ("supp", Dot1x.Nodes.Node.Statistics.IfStats.Supp)), ("local-eap", ("local_eap", Dot1x.Nodes.Node.Statistics.IfStats.LocalEap))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('pae', (YLeaf(YType.str, 'pae'), ['str'])),
                        ])
                        self.interface_name = None
                        self.pae = None

                        self.idb = Dot1x.Nodes.Node.Statistics.IfStats.Idb()
                        self.idb.parent = self
                        self._children_name_map["idb"] = "idb"

                        self.auth = Dot1x.Nodes.Node.Statistics.IfStats.Auth()
                        self.auth.parent = self
                        self._children_name_map["auth"] = "auth"

                        self.supp = Dot1x.Nodes.Node.Statistics.IfStats.Supp()
                        self.supp.parent = self
                        self._children_name_map["supp"] = "supp"

                        self.local_eap = Dot1x.Nodes.Node.Statistics.IfStats.LocalEap()
                        self.local_eap.parent = self
                        self._children_name_map["local_eap"] = "local-eap"
                        self._segment_path = lambda: "if-stats"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Nodes.Node.Statistics.IfStats, ['interface_name', 'pae'], name, value)


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
                            super(Dot1x.Nodes.Node.Statistics.IfStats.Idb, self).__init__()

                            self.yang_name = "idb"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                                ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
                                ('no_rx_on_intf_down', (YLeaf(YType.uint32, 'no-rx-on-intf-down'), ['int'])),
                            ])
                            self.rx_total = None
                            self.tx_total = None
                            self.no_rx_on_intf_down = None
                            self._segment_path = lambda: "idb"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Nodes.Node.Statistics.IfStats.Idb, ['rx_total', 'tx_total', 'no_rx_on_intf_down'], name, value)


                    class Auth(Entity):
                        """
                        Dot1x Authenticator Port Statistics
                        
                        .. attribute:: port_control
                        
                        	PortControl
                        	**type**\:  :py:class:`PortControl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Nodes.Node.Statistics.IfStats.Auth.PortControl>`
                        
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
                        
                        .. attribute:: packet_drop_no_config_received
                        
                        	PacketDrop
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1x.Nodes.Node.Statistics.IfStats.Auth, self).__init__()

                            self.yang_name = "auth"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("port-control", ("port_control", Dot1x.Nodes.Node.Statistics.IfStats.Auth.PortControl))])
                            self._leafs = OrderedDict([
                                ('rx_start', (YLeaf(YType.uint32, 'rx-start'), ['int'])),
                                ('rx_logoff', (YLeaf(YType.uint32, 'rx-logoff'), ['int'])),
                                ('rx_resp', (YLeaf(YType.uint32, 'rx-resp'), ['int'])),
                                ('rx_resp_id', (YLeaf(YType.uint32, 'rx-resp-id'), ['int'])),
                                ('rx_invalid', (YLeaf(YType.uint32, 'rx-invalid'), ['int'])),
                                ('rx_len_err', (YLeaf(YType.uint32, 'rx-len-err'), ['int'])),
                                ('rx_my_mac_err', (YLeaf(YType.uint32, 'rx-my-mac-err'), ['int'])),
                                ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                                ('tx_req', (YLeaf(YType.uint32, 'tx-req'), ['int'])),
                                ('tx_reqid', (YLeaf(YType.uint32, 'tx-reqid'), ['int'])),
                                ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
                                ('packet_drop_no_config_received', (YLeaf(YType.uint32, 'packet-drop-no-config-received'), ['int'])),
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
                            self.packet_drop_no_config_received = None

                            self.port_control = Dot1x.Nodes.Node.Statistics.IfStats.Auth.PortControl()
                            self.port_control.parent = self
                            self._children_name_map["port_control"] = "port-control"
                            self._segment_path = lambda: "auth"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Nodes.Node.Statistics.IfStats.Auth, ['rx_start', 'rx_logoff', 'rx_resp', 'rx_resp_id', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_req', 'tx_reqid', 'tx_total', 'packet_drop_no_config_received'], name, value)


                        class PortControl(Entity):
                            """
                            PortControl
                            
                            .. attribute:: enable_succ
                            
                            	EnableSucc
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: enable_fail
                            
                            	EnableFail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: add_client_succ
                            
                            	AddClientSucc
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: add_client_fail
                            
                            	AddClientFail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remove_client_succ
                            
                            	RemoveClientSucc
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remove_client_fail
                            
                            	RemoveClientFail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'dot1x-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dot1x.Nodes.Node.Statistics.IfStats.Auth.PortControl, self).__init__()

                                self.yang_name = "port-control"
                                self.yang_parent_name = "auth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable_succ', (YLeaf(YType.uint32, 'enable-succ'), ['int'])),
                                    ('enable_fail', (YLeaf(YType.uint32, 'enable-fail'), ['int'])),
                                    ('add_client_succ', (YLeaf(YType.uint32, 'add-client-succ'), ['int'])),
                                    ('add_client_fail', (YLeaf(YType.uint32, 'add-client-fail'), ['int'])),
                                    ('remove_client_succ', (YLeaf(YType.uint32, 'remove-client-succ'), ['int'])),
                                    ('remove_client_fail', (YLeaf(YType.uint32, 'remove-client-fail'), ['int'])),
                                ])
                                self.enable_succ = None
                                self.enable_fail = None
                                self.add_client_succ = None
                                self.add_client_fail = None
                                self.remove_client_succ = None
                                self.remove_client_fail = None
                                self._segment_path = lambda: "port-control"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dot1x.Nodes.Node.Statistics.IfStats.Auth.PortControl, ['enable_succ', 'enable_fail', 'add_client_succ', 'add_client_fail', 'remove_client_succ', 'remove_client_fail'], name, value)


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
                            super(Dot1x.Nodes.Node.Statistics.IfStats.Supp, self).__init__()

                            self.yang_name = "supp"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rx_req', (YLeaf(YType.uint32, 'rx-req'), ['int'])),
                                ('rx_invalid', (YLeaf(YType.uint32, 'rx-invalid'), ['int'])),
                                ('rx_len_err', (YLeaf(YType.uint32, 'rx-len-err'), ['int'])),
                                ('rx_my_mac_err', (YLeaf(YType.uint32, 'rx-my-mac-err'), ['int'])),
                                ('rx_total', (YLeaf(YType.uint32, 'rx-total'), ['int'])),
                                ('tx_start', (YLeaf(YType.uint32, 'tx-start'), ['int'])),
                                ('tx_logoff', (YLeaf(YType.uint32, 'tx-logoff'), ['int'])),
                                ('tx_resp', (YLeaf(YType.uint32, 'tx-resp'), ['int'])),
                                ('tx_total', (YLeaf(YType.uint32, 'tx-total'), ['int'])),
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
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Nodes.Node.Statistics.IfStats.Supp, ['rx_req', 'rx_invalid', 'rx_len_err', 'rx_my_mac_err', 'rx_total', 'tx_start', 'tx_logoff', 'tx_resp', 'tx_total'], name, value)


                    class LocalEap(Entity):
                        """
                        Dot1x Local EAP Port Statistics
                        
                        .. attribute:: requests
                        
                        	Requests
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: replies
                        
                        	Replies
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timeout
                        
                        	Timeout
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_no_eap
                        
                        	DroppedNoEAP
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped
                        
                        	Dropped
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: success
                        
                        	Success
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed
                        
                        	Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1x.Nodes.Node.Statistics.IfStats.LocalEap, self).__init__()

                            self.yang_name = "local-eap"
                            self.yang_parent_name = "if-stats"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('requests', (YLeaf(YType.uint32, 'requests'), ['int'])),
                                ('replies', (YLeaf(YType.uint32, 'replies'), ['int'])),
                                ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                                ('dropped_no_eap', (YLeaf(YType.uint32, 'dropped-no-eap'), ['int'])),
                                ('dropped', (YLeaf(YType.uint32, 'dropped'), ['int'])),
                                ('success', (YLeaf(YType.uint32, 'success'), ['int'])),
                                ('failed', (YLeaf(YType.uint32, 'failed'), ['int'])),
                            ])
                            self.requests = None
                            self.replies = None
                            self.timeout = None
                            self.dropped_no_eap = None
                            self.dropped = None
                            self.success = None
                            self.failed = None
                            self._segment_path = lambda: "local-eap"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Nodes.Node.Statistics.IfStats.LocalEap, ['requests', 'replies', 'timeout', 'dropped_no_eap', 'dropped', 'success', 'failed'], name, value)


    class Session(Entity):
        """
        Dot1x operational data
        
        .. attribute:: interface_sessions
        
        	Interfaces with Dot1x
        	**type**\:  :py:class:`InterfaceSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions>`
        
        

        """

        _prefix = 'dot1x-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dot1x.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "dot1x"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface-sessions", ("interface_sessions", Dot1x.Session.InterfaceSessions))])
            self._leafs = OrderedDict()

            self.interface_sessions = Dot1x.Session.InterfaceSessions()
            self.interface_sessions.parent = self
            self._children_name_map["interface_sessions"] = "interface-sessions"
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dot1x.Session, [], name, value)


        class InterfaceSessions(Entity):
            """
            Interfaces with Dot1x
            
            .. attribute:: interface_session
            
            	Dot1x Data for that Interface
            	**type**\: list of  		 :py:class:`InterfaceSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession>`
            
            

            """

            _prefix = 'dot1x-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dot1x.Session.InterfaceSessions, self).__init__()

                self.yang_name = "interface-sessions"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interface-session", ("interface_session", Dot1x.Session.InterfaceSessions.InterfaceSession))])
                self._leafs = OrderedDict()

                self.interface_session = YList(self)
                self._segment_path = lambda: "interface-sessions"
                self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/session/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dot1x.Session.InterfaceSessions, [], name, value)


            class InterfaceSession(Entity):
                """
                Dot1x Data for that Interface
                
                .. attribute:: name  (key)
                
                	Interface Name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: intf_info
                
                	Dot1x interface Info
                	**type**\:  :py:class:`IntfInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo>`
                
                .. attribute:: mka_status_info
                
                	MKA session secure status
                	**type**\:  :py:class:`MkaStatusInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo>`
                
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
                    super(Dot1x.Session.InterfaceSessions.InterfaceSession, self).__init__()

                    self.yang_name = "interface-session"
                    self.yang_parent_name = "interface-sessions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("intf-info", ("intf_info", Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo)), ("mka-status-info", ("mka_status_info", Dot1x.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('interface_sname', (YLeaf(YType.str, 'interface-sname'), ['str'])),
                        ('if_handle', (YLeaf(YType.str, 'if-handle'), ['str'])),
                        ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                        ('ethertype', (YLeaf(YType.str, 'ethertype'), ['str'])),
                    ])
                    self.name = None
                    self.interface_name = None
                    self.interface_sname = None
                    self.if_handle = None
                    self.mac = None
                    self.ethertype = None

                    self.intf_info = Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo()
                    self.intf_info.parent = self
                    self._children_name_map["intf_info"] = "intf-info"

                    self.mka_status_info = Dot1x.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo()
                    self.mka_status_info.parent = self
                    self._children_name_map["mka_status_info"] = "mka-status-info"
                    self._segment_path = lambda: "interface-session" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-dot1x-oper:dot1x/session/interface-sessions/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession, ['name', 'interface_name', 'interface_sname', 'if_handle', 'mac', 'ethertype'], name, value)


                class IntfInfo(Entity):
                    """
                    Dot1x interface Info
                    
                    .. attribute:: auth_info
                    
                    	Dot1x Authenticator info
                    	**type**\:  :py:class:`AuthInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo>`
                    
                    .. attribute:: supp_info
                    
                    	Dot1x Supplicant info
                    	**type**\:  :py:class:`SuppInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo>`
                    
                    .. attribute:: pae
                    
                    	PAE type on interface
                    	**type**\: str
                    
                    .. attribute:: port_status
                    
                    	Dot1x Port Status
                    	**type**\: str
                    
                    .. attribute:: dot1x_profile
                    
                    	Dot1x Profile
                    	**type**\: str
                    
                    .. attribute:: l2_transport
                    
                    	L2 Transport Info
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'dot1x-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo, self).__init__()

                        self.yang_name = "intf-info"
                        self.yang_parent_name = "interface-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("auth-info", ("auth_info", Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo)), ("supp-info", ("supp_info", Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo))])
                        self._leafs = OrderedDict([
                            ('pae', (YLeaf(YType.str, 'pae'), ['str'])),
                            ('port_status', (YLeaf(YType.str, 'port-status'), ['str'])),
                            ('dot1x_profile', (YLeaf(YType.str, 'dot1x-profile'), ['str'])),
                            ('l2_transport', (YLeaf(YType.boolean, 'l2-transport'), ['bool'])),
                        ])
                        self.pae = None
                        self.port_status = None
                        self.dot1x_profile = None
                        self.l2_transport = None

                        self.auth_info = Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo()
                        self.auth_info.parent = self
                        self._children_name_map["auth_info"] = "auth-info"

                        self.supp_info = Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo()
                        self.supp_info.parent = self
                        self._children_name_map["supp_info"] = "supp-info"
                        self._segment_path = lambda: "intf-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo, ['pae', 'port_status', 'dot1x_profile', 'l2_transport'], name, value)


                    class AuthInfo(Entity):
                        """
                        Dot1x Authenticator info
                        
                        .. attribute:: port_control
                        
                        	Port Control Feature
                        	**type**\: str
                        
                        .. attribute:: reauth
                        
                        	Re\-Authentication enabled status
                        	**type**\: str
                        
                        .. attribute:: config_dependency
                        
                        	Configuration Dependency 
                        	**type**\: str
                        
                        .. attribute:: eap_profile
                        
                        	EAP profile
                        	**type**\: str
                        
                        .. attribute:: client
                        
                        	Authenticator client list
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client>`
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo, self).__init__()

                            self.yang_name = "auth-info"
                            self.yang_parent_name = "intf-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("client", ("client", Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client))])
                            self._leafs = OrderedDict([
                                ('port_control', (YLeaf(YType.str, 'port-control'), ['str'])),
                                ('reauth', (YLeaf(YType.str, 'reauth'), ['str'])),
                                ('config_dependency', (YLeaf(YType.str, 'config-dependency'), ['str'])),
                                ('eap_profile', (YLeaf(YType.str, 'eap-profile'), ['str'])),
                            ])
                            self.port_control = None
                            self.reauth = None
                            self.config_dependency = None
                            self.eap_profile = None

                            self.client = YList(self)
                            self._segment_path = lambda: "auth-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo, ['port_control', 'reauth', 'config_dependency', 'eap_profile'], name, value)


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
                            
                            .. attribute:: last_auth_server
                            
                            	Last Authenticated Server
                            	**type**\: str
                            
                            .. attribute:: port_control
                            
                            	Auth Client Port Control Status
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'dot1x-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "auth-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                    ('auth_sm_state', (YLeaf(YType.str, 'auth-sm-state'), ['str'])),
                                    ('auth_bend_sm_state', (YLeaf(YType.str, 'auth-bend-sm-state'), ['str'])),
                                    ('time_to_next_reauth', (YLeaf(YType.str, 'time-to-next-reauth'), ['str'])),
                                    ('last_auth_time', (YLeaf(YType.str, 'last-auth-time'), ['str'])),
                                    ('last_auth_server', (YLeaf(YType.str, 'last-auth-server'), ['str'])),
                                    ('port_control', (YLeaf(YType.str, 'port-control'), ['str'])),
                                ])
                                self.mac = None
                                self.auth_sm_state = None
                                self.auth_bend_sm_state = None
                                self.time_to_next_reauth = None
                                self.last_auth_time = None
                                self.last_auth_server = None
                                self.port_control = None
                                self._segment_path = lambda: "client"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.AuthInfo.Client, ['mac', 'auth_sm_state', 'auth_bend_sm_state', 'time_to_next_reauth', 'last_auth_time', 'last_auth_server', 'port_control'], name, value)


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
                        	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dot1x_oper.Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client>`
                        
                        

                        """

                        _prefix = 'dot1x-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo, self).__init__()

                            self.yang_name = "supp-info"
                            self.yang_parent_name = "intf-info"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("client", ("client", Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client))])
                            self._leafs = OrderedDict([
                                ('eap_profile', (YLeaf(YType.str, 'eap-profile'), ['str'])),
                                ('config_dependency', (YLeaf(YType.str, 'config-dependency'), ['str'])),
                            ])
                            self.eap_profile = None
                            self.config_dependency = None

                            self.client = YList(self)
                            self._segment_path = lambda: "supp-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo, ['eap_profile', 'config_dependency'], name, value)


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
                                super(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client, self).__init__()

                                self.yang_name = "client"
                                self.yang_parent_name = "supp-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mac', (YLeaf(YType.str, 'mac'), ['str'])),
                                    ('eap_method', (YLeaf(YType.str, 'eap-method'), ['str'])),
                                    ('last_auth_time', (YLeaf(YType.str, 'last-auth-time'), ['str'])),
                                    ('auth_sm_state', (YLeaf(YType.str, 'auth-sm-state'), ['str'])),
                                    ('auth_bend_sm_state', (YLeaf(YType.str, 'auth-bend-sm-state'), ['str'])),
                                ])
                                self.mac = None
                                self.eap_method = None
                                self.last_auth_time = None
                                self.auth_sm_state = None
                                self.auth_bend_sm_state = None
                                self._segment_path = lambda: "client"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession.IntfInfo.SuppInfo.Client, ['mac', 'eap_method', 'last_auth_time', 'auth_sm_state', 'auth_bend_sm_state'], name, value)


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
                        super(Dot1x.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo, self).__init__()

                        self.yang_name = "mka-status-info"
                        self.yang_parent_name = "interface-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tie_break_role', (YLeaf(YType.str, 'tie-break-role'), ['str'])),
                            ('eap_based_macsec', (YLeaf(YType.str, 'eap-based-macsec'), ['str'])),
                            ('mka_start_time', (YLeaf(YType.str, 'mka-start-time'), ['str'])),
                            ('mka_stop_time', (YLeaf(YType.str, 'mka-stop-time'), ['str'])),
                            ('mka_response_time', (YLeaf(YType.str, 'mka-response-time'), ['str'])),
                        ])
                        self.tie_break_role = None
                        self.eap_based_macsec = None
                        self.mka_start_time = None
                        self.mka_stop_time = None
                        self.mka_response_time = None
                        self._segment_path = lambda: "mka-status-info"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dot1x.Session.InterfaceSessions.InterfaceSession.MkaStatusInfo, ['tie_break_role', 'eap_based_macsec', 'mka_start_time', 'mka_stop_time', 'mka_response_time'], name, value)

    def clone_ptr(self):
        self._top_entity = Dot1x()
        return self._top_entity

