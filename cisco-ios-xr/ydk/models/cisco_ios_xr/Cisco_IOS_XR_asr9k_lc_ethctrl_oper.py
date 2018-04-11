""" Cisco_IOS_XR_asr9k_lc_ethctrl_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-ethctrl package operational data.

This module contains definitions
for the following management objects\:
  mlan\: Management LAN Operational data space

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Mlan(Entity):
    """
    Management LAN Operational data space
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes>`
    
    

    """

    _prefix = 'asr9k-lc-ethctrl-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Mlan, self).__init__()
        self._top_entity = None

        self.yang_name = "mlan"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-lc-ethctrl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Mlan.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Mlan.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan"


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Number
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node>`
        
        

        """

        _prefix = 'asr9k-lc-ethctrl-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Mlan.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mlan"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Mlan.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Mlan.Nodes, [], name, value)


        class Node(Entity):
            """
            Number
            
            .. attribute:: node  (key)
            
            	node number
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: port_status_numbers
            
            	Table of port status
            	**type**\:  :py:class:`PortStatusNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers>`
            
            .. attribute:: switch_status_table
            
            	Table of switch status
            	**type**\:  :py:class:`SwitchStatusTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable>`
            
            .. attribute:: port_counters_numbers
            
            	Table of port counters
            	**type**\:  :py:class:`PortCountersNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers>`
            
            .. attribute:: atu_entry_numbers
            
            	Table of switch ATU
            	**type**\:  :py:class:`AtuEntryNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers>`
            
            

            """

            _prefix = 'asr9k-lc-ethctrl-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Mlan.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_container_classes = OrderedDict([("port-status-numbers", ("port_status_numbers", Mlan.Nodes.Node.PortStatusNumbers)), ("switch-status-table", ("switch_status_table", Mlan.Nodes.Node.SwitchStatusTable)), ("port-counters-numbers", ("port_counters_numbers", Mlan.Nodes.Node.PortCountersNumbers)), ("atu-entry-numbers", ("atu_entry_numbers", Mlan.Nodes.Node.AtuEntryNumbers))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node', YLeaf(YType.str, 'node')),
                ])
                self.node = None

                self.port_status_numbers = Mlan.Nodes.Node.PortStatusNumbers()
                self.port_status_numbers.parent = self
                self._children_name_map["port_status_numbers"] = "port-status-numbers"
                self._children_yang_names.add("port-status-numbers")

                self.switch_status_table = Mlan.Nodes.Node.SwitchStatusTable()
                self.switch_status_table.parent = self
                self._children_name_map["switch_status_table"] = "switch-status-table"
                self._children_yang_names.add("switch-status-table")

                self.port_counters_numbers = Mlan.Nodes.Node.PortCountersNumbers()
                self.port_counters_numbers.parent = self
                self._children_name_map["port_counters_numbers"] = "port-counters-numbers"
                self._children_yang_names.add("port-counters-numbers")

                self.atu_entry_numbers = Mlan.Nodes.Node.AtuEntryNumbers()
                self.atu_entry_numbers.parent = self
                self._children_name_map["atu_entry_numbers"] = "atu-entry-numbers"
                self._children_yang_names.add("atu-entry-numbers")
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-lc-ethctrl-oper:mlan/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Mlan.Nodes.Node, ['node'], name, value)


            class PortStatusNumbers(Entity):
                """
                Table of port status
                
                .. attribute:: port_status_number
                
                	Number
                	**type**\: list of  		 :py:class:`PortStatusNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.PortStatusNumbers, self).__init__()

                    self.yang_name = "port-status-numbers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("port-status-number", ("port_status_number", Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber))])
                    self._leafs = OrderedDict()

                    self.port_status_number = YList(self)
                    self._segment_path = lambda: "port-status-numbers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers, [], name, value)


                class PortStatusNumber(Entity):
                    """
                    Number
                    
                    .. attribute:: number  (key)
                    
                    	port number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: port_status
                    
                    	mlan port status info
                    	**type**\:  :py:class:`PortStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber, self).__init__()

                        self.yang_name = "port-status-number"
                        self.yang_parent_name = "port-status-numbers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_container_classes = OrderedDict([("port-status", ("port_status", Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('number', YLeaf(YType.int32, 'number')),
                        ])
                        self.number = None

                        self.port_status = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus()
                        self.port_status.parent = self
                        self._children_name_map["port_status"] = "port-status"
                        self._children_yang_names.add("port-status")
                        self._segment_path = lambda: "port-status-number" + "[number='" + str(self.number) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber, ['number'], name, value)


                    class PortStatus(Entity):
                        """
                        mlan port status info
                        
                        .. attribute:: config
                        
                        	Configuration Data
                        	**type**\:  :py:class:`Config <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config>`
                        
                        .. attribute:: phy
                        
                        	PHY Registers
                        	**type**\:  :py:class:`Phy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy>`
                        
                        .. attribute:: serdes
                        
                        	SERDES Registers
                        	**type**\:  :py:class:`Serdes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes>`
                        
                        .. attribute:: mac
                        
                        	MAC Registers
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac>`
                        
                        .. attribute:: port_num
                        
                        	Port Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: phy_valid
                        
                        	PHY data valid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: serdes_valid
                        
                        	SERDES data valid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_valid
                        
                        	MAC data valid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus, self).__init__()

                            self.yang_name = "port-status"
                            self.yang_parent_name = "port-status-number"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("config", ("config", Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config)), ("phy", ("phy", Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy)), ("serdes", ("serdes", Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes)), ("mac", ("mac", Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('port_num', YLeaf(YType.uint32, 'port-num')),
                                ('phy_valid', YLeaf(YType.uint32, 'phy-valid')),
                                ('serdes_valid', YLeaf(YType.uint32, 'serdes-valid')),
                                ('mac_valid', YLeaf(YType.uint32, 'mac-valid')),
                            ])
                            self.port_num = None
                            self.phy_valid = None
                            self.serdes_valid = None
                            self.mac_valid = None

                            self.config = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config()
                            self.config.parent = self
                            self._children_name_map["config"] = "config"
                            self._children_yang_names.add("config")

                            self.phy = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy()
                            self.phy.parent = self
                            self._children_name_map["phy"] = "phy"
                            self._children_yang_names.add("phy")

                            self.serdes = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes()
                            self.serdes.parent = self
                            self._children_name_map["serdes"] = "serdes"
                            self._children_yang_names.add("serdes")

                            self.mac = Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")
                            self._segment_path = lambda: "port-status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus, ['port_num', 'phy_valid', 'serdes_valid', 'mac_valid'], name, value)


                        class Config(Entity):
                            """
                            Configuration Data
                            
                            .. attribute:: speed
                            
                            	speed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: duplex
                            
                            	duplex
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: pause
                            
                            	pauseEn
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: my_pause
                            
                            	myPause
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: loopback
                            
                            	loopback
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config, self).__init__()

                                self.yang_name = "config"
                                self.yang_parent_name = "port-status"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('speed', YLeaf(YType.uint32, 'speed')),
                                    ('duplex', YLeaf(YType.uint32, 'duplex')),
                                    ('pause', YLeaf(YType.uint16, 'pause')),
                                    ('my_pause', YLeaf(YType.uint16, 'my-pause')),
                                    ('loopback', YLeaf(YType.uint32, 'loopback')),
                                ])
                                self.speed = None
                                self.duplex = None
                                self.pause = None
                                self.my_pause = None
                                self.loopback = None
                                self._segment_path = lambda: "config"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config, ['speed', 'duplex', 'pause', 'my_pause', 'loopback'], name, value)


                        class Phy(Entity):
                            """
                            PHY Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\: list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy, self).__init__()

                                self.yang_name = "phy"
                                self.yang_parent_name = "port-status"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reg', YLeafList(YType.uint16, 'reg')),
                                ])
                                self.reg = []
                                self._segment_path = lambda: "phy"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy, ['reg'], name, value)


                        class Serdes(Entity):
                            """
                            SERDES Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\: list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes, self).__init__()

                                self.yang_name = "serdes"
                                self.yang_parent_name = "port-status"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reg', YLeafList(YType.uint16, 'reg')),
                                ])
                                self.reg = []
                                self._segment_path = lambda: "serdes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes, ['reg'], name, value)


                        class Mac(Entity):
                            """
                            MAC Registers
                            
                            .. attribute:: reg
                            
                            	reg
                            	**type**\: list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "port-status"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('reg', YLeafList(YType.uint16, 'reg')),
                                ])
                                self.reg = []
                                self._segment_path = lambda: "mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac, ['reg'], name, value)


            class SwitchStatusTable(Entity):
                """
                Table of switch status
                
                .. attribute:: switch_status
                
                	mlan switch status info
                	**type**\:  :py:class:`SwitchStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.SwitchStatusTable, self).__init__()

                    self.yang_name = "switch-status-table"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("switch-status", ("switch_status", Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.switch_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus()
                    self.switch_status.parent = self
                    self._children_name_map["switch_status"] = "switch-status"
                    self._children_yang_names.add("switch-status")
                    self._segment_path = lambda: "switch-status-table"


                class SwitchStatus(Entity):
                    """
                    mlan switch status info
                    
                    .. attribute:: sw_reg_1
                    
                    	Switch Global Registers
                    	**type**\:  :py:class:`SwReg1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1>`
                    
                    .. attribute:: sw_reg_2
                    
                    	Switch Global Registers
                    	**type**\:  :py:class:`SwReg2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2>`
                    
                    .. attribute:: sw_status
                    
                    	Switch Status Data
                    	**type**\:  :py:class:`SwStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus>`
                    
                    .. attribute:: rate_limit
                    
                    	CPU Interface Rate Limit
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus, self).__init__()

                        self.yang_name = "switch-status"
                        self.yang_parent_name = "switch-status-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("sw-reg-1", ("sw_reg_1", Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1)), ("sw-reg-2", ("sw_reg_2", Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2)), ("sw-status", ("sw_status", Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rate_limit', YLeaf(YType.int32, 'rate-limit')),
                        ])
                        self.rate_limit = None

                        self.sw_reg_1 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1()
                        self.sw_reg_1.parent = self
                        self._children_name_map["sw_reg_1"] = "sw-reg-1"
                        self._children_yang_names.add("sw-reg-1")

                        self.sw_reg_2 = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2()
                        self.sw_reg_2.parent = self
                        self._children_name_map["sw_reg_2"] = "sw-reg-2"
                        self._children_yang_names.add("sw-reg-2")

                        self.sw_status = Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus()
                        self.sw_status.parent = self
                        self._children_name_map["sw_status"] = "sw-status"
                        self._children_yang_names.add("sw-status")
                        self._segment_path = lambda: "switch-status"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus, ['rate_limit'], name, value)


                    class SwReg1(Entity):
                        """
                        Switch Global Registers
                        
                        .. attribute:: reg
                        
                        	reg
                        	**type**\: list of int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1, self).__init__()

                            self.yang_name = "sw-reg-1"
                            self.yang_parent_name = "switch-status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reg', YLeafList(YType.uint16, 'reg')),
                            ])
                            self.reg = []
                            self._segment_path = lambda: "sw-reg-1"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1, ['reg'], name, value)


                    class SwReg2(Entity):
                        """
                        Switch Global Registers
                        
                        .. attribute:: reg
                        
                        	reg
                        	**type**\: list of int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2, self).__init__()

                            self.yang_name = "sw-reg-2"
                            self.yang_parent_name = "switch-status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reg', YLeafList(YType.uint16, 'reg')),
                            ])
                            self.reg = []
                            self._segment_path = lambda: "sw-reg-2"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2, ['reg'], name, value)


                    class SwStatus(Entity):
                        """
                        Switch Status Data
                        
                        .. attribute:: ppu
                        
                        	ppu
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mtu
                        
                        	mtu
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac
                        
                        	mac
                        	**type**\: str
                        
                        	**length:** 0..6
                        
                        .. attribute:: cpu_port
                        
                        	cpu port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: cpu_mac
                        
                        	cpu mac
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: initialized
                        
                        	initialized
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: restarted
                        
                        	restarted
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus, self).__init__()

                            self.yang_name = "sw-status"
                            self.yang_parent_name = "switch-status"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ppu', YLeaf(YType.uint32, 'ppu')),
                                ('mtu', YLeaf(YType.uint32, 'mtu')),
                                ('mac', YLeaf(YType.str, 'mac')),
                                ('cpu_port', YLeaf(YType.uint16, 'cpu-port')),
                                ('cpu_mac', YLeaf(YType.uint16, 'cpu-mac')),
                                ('initialized', YLeaf(YType.uint16, 'initialized')),
                                ('restarted', YLeaf(YType.uint16, 'restarted')),
                            ])
                            self.ppu = None
                            self.mtu = None
                            self.mac = None
                            self.cpu_port = None
                            self.cpu_mac = None
                            self.initialized = None
                            self.restarted = None
                            self._segment_path = lambda: "sw-status"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus, ['ppu', 'mtu', 'mac', 'cpu_port', 'cpu_mac', 'initialized', 'restarted'], name, value)


            class PortCountersNumbers(Entity):
                """
                Table of port counters
                
                .. attribute:: port_counters_number
                
                	Number
                	**type**\: list of  		 :py:class:`PortCountersNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.PortCountersNumbers, self).__init__()

                    self.yang_name = "port-counters-numbers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("port-counters-number", ("port_counters_number", Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber))])
                    self._leafs = OrderedDict()

                    self.port_counters_number = YList(self)
                    self._segment_path = lambda: "port-counters-numbers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mlan.Nodes.Node.PortCountersNumbers, [], name, value)


                class PortCountersNumber(Entity):
                    """
                    Number
                    
                    .. attribute:: number  (key)
                    
                    	port number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: port_counters
                    
                    	mlan port counters info
                    	**type**\:  :py:class:`PortCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber, self).__init__()

                        self.yang_name = "port-counters-number"
                        self.yang_parent_name = "port-counters-numbers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_container_classes = OrderedDict([("port-counters", ("port_counters", Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('number', YLeaf(YType.int32, 'number')),
                        ])
                        self.number = None

                        self.port_counters = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters()
                        self.port_counters.parent = self
                        self._children_name_map["port_counters"] = "port-counters"
                        self._children_yang_names.add("port-counters")
                        self._segment_path = lambda: "port-counters-number" + "[number='" + str(self.number) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber, ['number'], name, value)


                    class PortCounters(Entity):
                        """
                        mlan port counters info
                        
                        .. attribute:: mlan_stats
                        
                        	Switch Port Statistics
                        	**type**\:  :py:class:`MlanStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats>`
                        
                        .. attribute:: port_num
                        
                        	Port Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters, self).__init__()

                            self.yang_name = "port-counters"
                            self.yang_parent_name = "port-counters-number"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("mlan-stats", ("mlan_stats", Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('port_num', YLeaf(YType.uint32, 'port-num')),
                            ])
                            self.port_num = None

                            self.mlan_stats = Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats()
                            self.mlan_stats.parent = self
                            self._children_name_map["mlan_stats"] = "mlan-stats"
                            self._children_yang_names.add("mlan-stats")
                            self._segment_path = lambda: "port-counters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters, ['port_num'], name, value)


                        class MlanStats(Entity):
                            """
                            Switch Port Statistics
                            
                            .. attribute:: in_good_octets_hi
                            
                            	inGoodOctets hi
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_good_octets
                            
                            	inGoodOctets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_bad_octets
                            
                            	inBadOctets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_unicast_pkt
                            
                            	inUnicastPkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_bcast_pkt
                            
                            	inBcastPkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_mcast_pkt
                            
                            	inMcastPkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_pause_pkt
                            
                            	inPausePkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_undersize_pkt
                            
                            	inUndersizePkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_fragments
                            
                            	inFragments
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_oversize
                            
                            	inOversize
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_jabber
                            
                            	inJabber
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_rx_err
                            
                            	inRxErr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_fcs_err
                            
                            	inFcsErr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_octets_hi
                            
                            	outOctets hi
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_octets
                            
                            	outOctets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_unicast_pkt
                            
                            	outUnicastPkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_bcast_pkt
                            
                            	outBcastPkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_mcast_pkt
                            
                            	outMcastPkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_pause_pkt
                            
                            	outPausePkt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: excessive
                            
                            	excessive
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: collisions
                            
                            	collisions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: deferred
                            
                            	deferred
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: single
                            
                            	single
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: multiple
                            
                            	multiple
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_fcs_err
                            
                            	outFcsErr
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: late
                            
                            	late
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_64_octets
                            
                            	rx tx 64 Octets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_65_127_octets
                            
                            	rx tx 65 127 Octets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_128_255_octets
                            
                            	rx tx 128 255 Octets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_256_511_octets
                            
                            	rx tx 256 511 Octets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_512_1023_octets
                            
                            	rx tx 512 1023 Octets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: rx_tx_1024_max_octets
                            
                            	rx tx 1024 Max Octets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_discards
                            
                            	inDiscards
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_filtered
                            
                            	inFiltered
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_filtered
                            
                            	outFiltered
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats, self).__init__()

                                self.yang_name = "mlan-stats"
                                self.yang_parent_name = "port-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('in_good_octets_hi', YLeaf(YType.uint32, 'in-good-octets-hi')),
                                    ('in_good_octets', YLeaf(YType.uint32, 'in-good-octets')),
                                    ('in_bad_octets', YLeaf(YType.uint32, 'in-bad-octets')),
                                    ('in_unicast_pkt', YLeaf(YType.uint32, 'in-unicast-pkt')),
                                    ('in_bcast_pkt', YLeaf(YType.uint32, 'in-bcast-pkt')),
                                    ('in_mcast_pkt', YLeaf(YType.uint32, 'in-mcast-pkt')),
                                    ('in_pause_pkt', YLeaf(YType.uint32, 'in-pause-pkt')),
                                    ('in_undersize_pkt', YLeaf(YType.uint32, 'in-undersize-pkt')),
                                    ('in_fragments', YLeaf(YType.uint32, 'in-fragments')),
                                    ('in_oversize', YLeaf(YType.uint32, 'in-oversize')),
                                    ('in_jabber', YLeaf(YType.uint32, 'in-jabber')),
                                    ('in_rx_err', YLeaf(YType.uint32, 'in-rx-err')),
                                    ('in_fcs_err', YLeaf(YType.uint32, 'in-fcs-err')),
                                    ('out_octets_hi', YLeaf(YType.uint32, 'out-octets-hi')),
                                    ('out_octets', YLeaf(YType.uint32, 'out-octets')),
                                    ('out_unicast_pkt', YLeaf(YType.uint32, 'out-unicast-pkt')),
                                    ('out_bcast_pkt', YLeaf(YType.uint32, 'out-bcast-pkt')),
                                    ('out_mcast_pkt', YLeaf(YType.uint32, 'out-mcast-pkt')),
                                    ('out_pause_pkt', YLeaf(YType.uint32, 'out-pause-pkt')),
                                    ('excessive', YLeaf(YType.uint32, 'excessive')),
                                    ('collisions', YLeaf(YType.uint32, 'collisions')),
                                    ('deferred', YLeaf(YType.uint32, 'deferred')),
                                    ('single', YLeaf(YType.uint32, 'single')),
                                    ('multiple', YLeaf(YType.uint32, 'multiple')),
                                    ('out_fcs_err', YLeaf(YType.uint32, 'out-fcs-err')),
                                    ('late', YLeaf(YType.uint32, 'late')),
                                    ('rx_tx_64_octets', YLeaf(YType.uint32, 'rx-tx-64-octets')),
                                    ('rx_tx_65_127_octets', YLeaf(YType.uint32, 'rx-tx-65-127-octets')),
                                    ('rx_tx_128_255_octets', YLeaf(YType.uint32, 'rx-tx-128-255-octets')),
                                    ('rx_tx_256_511_octets', YLeaf(YType.uint32, 'rx-tx-256-511-octets')),
                                    ('rx_tx_512_1023_octets', YLeaf(YType.uint32, 'rx-tx-512-1023-octets')),
                                    ('rx_tx_1024_max_octets', YLeaf(YType.uint32, 'rx-tx-1024-max-octets')),
                                    ('in_discards', YLeaf(YType.uint32, 'in-discards')),
                                    ('in_filtered', YLeaf(YType.uint32, 'in-filtered')),
                                    ('out_filtered', YLeaf(YType.uint32, 'out-filtered')),
                                ])
                                self.in_good_octets_hi = None
                                self.in_good_octets = None
                                self.in_bad_octets = None
                                self.in_unicast_pkt = None
                                self.in_bcast_pkt = None
                                self.in_mcast_pkt = None
                                self.in_pause_pkt = None
                                self.in_undersize_pkt = None
                                self.in_fragments = None
                                self.in_oversize = None
                                self.in_jabber = None
                                self.in_rx_err = None
                                self.in_fcs_err = None
                                self.out_octets_hi = None
                                self.out_octets = None
                                self.out_unicast_pkt = None
                                self.out_bcast_pkt = None
                                self.out_mcast_pkt = None
                                self.out_pause_pkt = None
                                self.excessive = None
                                self.collisions = None
                                self.deferred = None
                                self.single = None
                                self.multiple = None
                                self.out_fcs_err = None
                                self.late = None
                                self.rx_tx_64_octets = None
                                self.rx_tx_65_127_octets = None
                                self.rx_tx_128_255_octets = None
                                self.rx_tx_256_511_octets = None
                                self.rx_tx_512_1023_octets = None
                                self.rx_tx_1024_max_octets = None
                                self.in_discards = None
                                self.in_filtered = None
                                self.out_filtered = None
                                self._segment_path = lambda: "mlan-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats, ['in_good_octets_hi', 'in_good_octets', 'in_bad_octets', 'in_unicast_pkt', 'in_bcast_pkt', 'in_mcast_pkt', 'in_pause_pkt', 'in_undersize_pkt', 'in_fragments', 'in_oversize', 'in_jabber', 'in_rx_err', 'in_fcs_err', 'out_octets_hi', 'out_octets', 'out_unicast_pkt', 'out_bcast_pkt', 'out_mcast_pkt', 'out_pause_pkt', 'excessive', 'collisions', 'deferred', 'single', 'multiple', 'out_fcs_err', 'late', 'rx_tx_64_octets', 'rx_tx_65_127_octets', 'rx_tx_128_255_octets', 'rx_tx_256_511_octets', 'rx_tx_512_1023_octets', 'rx_tx_1024_max_octets', 'in_discards', 'in_filtered', 'out_filtered'], name, value)


            class AtuEntryNumbers(Entity):
                """
                Table of switch ATU
                
                .. attribute:: atu_entry_number
                
                	Entry number
                	**type**\: list of  		 :py:class:`AtuEntryNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber>`
                
                

                """

                _prefix = 'asr9k-lc-ethctrl-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Mlan.Nodes.Node.AtuEntryNumbers, self).__init__()

                    self.yang_name = "atu-entry-numbers"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("atu-entry-number", ("atu_entry_number", Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber))])
                    self._leafs = OrderedDict()

                    self.atu_entry_number = YList(self)
                    self._segment_path = lambda: "atu-entry-numbers"

                def __setattr__(self, name, value):
                    self._perform_setattr(Mlan.Nodes.Node.AtuEntryNumbers, [], name, value)


                class AtuEntryNumber(Entity):
                    """
                    Entry number
                    
                    .. attribute:: entry  (key)
                    
                    	entry number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: switch_counters
                    
                    	mlan switch counters info
                    	**type**\:  :py:class:`SwitchCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters>`
                    
                    

                    """

                    _prefix = 'asr9k-lc-ethctrl-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber, self).__init__()

                        self.yang_name = "atu-entry-number"
                        self.yang_parent_name = "atu-entry-numbers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['entry']
                        self._child_container_classes = OrderedDict([("switch-counters", ("switch_counters", Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.int32, 'entry')),
                        ])
                        self.entry = None

                        self.switch_counters = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters()
                        self.switch_counters.parent = self
                        self._children_name_map["switch_counters"] = "switch-counters"
                        self._children_yang_names.add("switch-counters")
                        self._segment_path = lambda: "atu-entry-number" + "[entry='" + str(self.entry) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber, ['entry'], name, value)


                    class SwitchCounters(Entity):
                        """
                        mlan switch counters info
                        
                        .. attribute:: atu
                        
                        	Switch ATU Data
                        	**type**\:  :py:class:`Atu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper.Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu>`
                        
                        .. attribute:: entry_num
                        
                        	Index of ATU Entry
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-lc-ethctrl-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters, self).__init__()

                            self.yang_name = "switch-counters"
                            self.yang_parent_name = "atu-entry-number"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("atu", ("atu", Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry_num', YLeaf(YType.uint32, 'entry-num')),
                            ])
                            self.entry_num = None

                            self.atu = Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu()
                            self.atu.parent = self
                            self._children_name_map["atu"] = "atu"
                            self._children_yang_names.add("atu")
                            self._segment_path = lambda: "switch-counters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters, ['entry_num'], name, value)


                        class Atu(Entity):
                            """
                            Switch ATU Data
                            
                            .. attribute:: db_num
                            
                            	dbNum
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: priority
                            
                            	priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: trunk
                            
                            	trunk
                            	**type**\: bool
                            
                            .. attribute:: dpv
                            
                            	dpv
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: es
                            
                            	es
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: macaddr
                            
                            	macaddr
                            	**type**\: list of int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-lc-ethctrl-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu, self).__init__()

                                self.yang_name = "atu"
                                self.yang_parent_name = "switch-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('db_num', YLeaf(YType.uint16, 'db-num')),
                                    ('priority', YLeaf(YType.uint8, 'priority')),
                                    ('trunk', YLeaf(YType.boolean, 'trunk')),
                                    ('dpv', YLeaf(YType.uint8, 'dpv')),
                                    ('es', YLeaf(YType.uint8, 'es')),
                                    ('macaddr', YLeafList(YType.uint16, 'macaddr')),
                                ])
                                self.db_num = None
                                self.priority = None
                                self.trunk = None
                                self.dpv = None
                                self.es = None
                                self.macaddr = []
                                self._segment_path = lambda: "atu"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu, ['db_num', 'priority', 'trunk', 'dpv', 'es', 'macaddr'], name, value)

    def clone_ptr(self):
        self._top_entity = Mlan()
        return self._top_entity

