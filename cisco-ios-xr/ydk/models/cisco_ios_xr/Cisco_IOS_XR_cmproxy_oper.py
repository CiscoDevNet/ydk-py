""" Cisco_IOS_XR_cmproxy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cmproxy package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\-vm\: Platform VM information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SdrInventoryVm(Entity):
    """
    Platform VM information
    
    .. attribute:: nodes
    
    	Node directory
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes>`
    
    

    """

    _prefix = 'cmproxy-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SdrInventoryVm, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-inventory-vm"
        self.yang_parent_name = "Cisco-IOS-XR-cmproxy-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", SdrInventoryVm.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = SdrInventoryVm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SdrInventoryVm, [], name, value)


    class Nodes(Entity):
        """
        Node directory
        
        .. attribute:: node
        
        	Node name
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node>`
        
        

        """

        _prefix = 'cmproxy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SdrInventoryVm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "sdr-inventory-vm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SdrInventoryVm.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrInventoryVm.Nodes, [], name, value)


        class Node(Entity):
            """
            Node name
            
            .. attribute:: name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: node_entries
            
            	VM Information
            	**type**\:  :py:class:`NodeEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries>`
            
            

            """

            _prefix = 'cmproxy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SdrInventoryVm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("node-entries", ("node_entries", SdrInventoryVm.Nodes.Node.NodeEntries))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.node_entries = SdrInventoryVm.Nodes.Node.NodeEntries()
                self.node_entries.parent = self
                self._children_name_map["node_entries"] = "node-entries"
                self._segment_path = lambda: "node" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrInventoryVm.Nodes.Node, ['name'], name, value)


            class NodeEntries(Entity):
                """
                VM Information
                
                .. attribute:: node_entry
                
                	VM information for a node
                	**type**\: list of  		 :py:class:`NodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry>`
                
                

                """

                _prefix = 'cmproxy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SdrInventoryVm.Nodes.Node.NodeEntries, self).__init__()

                    self.yang_name = "node-entries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-entry", ("node_entry", SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry))])
                    self._leafs = OrderedDict()

                    self.node_entry = YList(self)
                    self._segment_path = lambda: "node-entries"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrInventoryVm.Nodes.Node.NodeEntries, [], name, value)


                class NodeEntry(Entity):
                    """
                    VM information for a node
                    
                    .. attribute:: name  (key)
                    
                    	Node name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: valid
                    
                    	valid flag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: card_type_string
                    
                    	card type string
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: nodeid
                    
                    	node ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: node_name
                    
                    	node name string
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: partner_id
                    
                    	partner node id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_name
                    
                    	partner name string
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: red_state
                    
                    	redundancy state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: red_state_string
                    
                    	redundancy state string
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_sw_state
                    
                    	current software state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_sw_state_string
                    
                    	current software state string
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: prev_sw_state
                    
                    	previous software state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prev_sw_state_string
                    
                    	previous software state string
                    	**type**\: str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_ip
                    
                    	node IP address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_ipv4_string
                    
                    	node IPv4 address string
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    

                    """

                    _prefix = 'cmproxy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, self).__init__()

                        self.yang_name = "node-entry"
                        self.yang_parent_name = "node-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('valid', (YLeaf(YType.uint32, 'valid'), ['int'])),
                            ('card_type', (YLeaf(YType.uint32, 'card-type'), ['int'])),
                            ('card_type_string', (YLeaf(YType.str, 'card-type-string'), ['str'])),
                            ('nodeid', (YLeaf(YType.int32, 'nodeid'), ['int'])),
                            ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                            ('partner_id', (YLeaf(YType.int32, 'partner-id'), ['int'])),
                            ('partner_name', (YLeaf(YType.str, 'partner-name'), ['str'])),
                            ('red_state', (YLeaf(YType.uint32, 'red-state'), ['int'])),
                            ('red_state_string', (YLeaf(YType.str, 'red-state-string'), ['str'])),
                            ('node_sw_state', (YLeaf(YType.uint32, 'node-sw-state'), ['int'])),
                            ('node_sw_state_string', (YLeaf(YType.str, 'node-sw-state-string'), ['str'])),
                            ('prev_sw_state', (YLeaf(YType.uint32, 'prev-sw-state'), ['int'])),
                            ('prev_sw_state_string', (YLeaf(YType.str, 'prev-sw-state-string'), ['str'])),
                            ('node_ip', (YLeaf(YType.uint32, 'node-ip'), ['int'])),
                            ('node_ipv4_string', (YLeaf(YType.str, 'node-ipv4-string'), ['str'])),
                        ])
                        self.name = None
                        self.valid = None
                        self.card_type = None
                        self.card_type_string = None
                        self.nodeid = None
                        self.node_name = None
                        self.partner_id = None
                        self.partner_name = None
                        self.red_state = None
                        self.red_state_string = None
                        self.node_sw_state = None
                        self.node_sw_state_string = None
                        self.prev_sw_state = None
                        self.prev_sw_state_string = None
                        self.node_ip = None
                        self.node_ipv4_string = None
                        self._segment_path = lambda: "node-entry" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, ['name', 'valid', 'card_type', 'card_type_string', 'nodeid', 'node_name', 'partner_id', 'partner_name', 'red_state', 'red_state_string', 'node_sw_state', 'node_sw_state_string', 'prev_sw_state', 'prev_sw_state_string', 'node_ip', 'node_ipv4_string'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrInventoryVm()
        return self._top_entity

