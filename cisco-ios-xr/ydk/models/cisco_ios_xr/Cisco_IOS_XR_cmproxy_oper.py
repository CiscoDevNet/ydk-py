""" Cisco_IOS_XR_cmproxy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cmproxy package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\-vm\: Platform VM information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SdrInventoryVm(Entity):
    """
    Platform VM information
    
    .. attribute:: nodes
    
    	Node directory
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes>`
    
    

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
        self._child_container_classes = {"nodes" : ("nodes", SdrInventoryVm.Nodes)}
        self._child_list_classes = {}

        self.nodes = SdrInventoryVm.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm"


    class Nodes(Entity):
        """
        Node directory
        
        .. attribute:: node
        
        	Node name
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node>`
        
        

        """

        _prefix = 'cmproxy-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SdrInventoryVm.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "sdr-inventory-vm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", SdrInventoryVm.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SdrInventoryVm.Nodes, [], name, value)


        class Node(Entity):
            """
            Node name
            
            .. attribute:: name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: node_entries
            
            	VM Information
            	**type**\:   :py:class:`NodeEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries>`
            
            

            """

            _prefix = 'cmproxy-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SdrInventoryVm.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"node-entries" : ("node_entries", SdrInventoryVm.Nodes.Node.NodeEntries)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.node_entries = SdrInventoryVm.Nodes.Node.NodeEntries()
                self.node_entries.parent = self
                self._children_name_map["node_entries"] = "node-entries"
                self._children_yang_names.add("node-entries")
                self._segment_path = lambda: "node" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-cmproxy-oper:sdr-inventory-vm/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SdrInventoryVm.Nodes.Node, ['name'], name, value)


            class NodeEntries(Entity):
                """
                VM Information
                
                .. attribute:: node_entry
                
                	VM information for a node
                	**type**\: list of    :py:class:`NodeEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cmproxy_oper.SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry>`
                
                

                """

                _prefix = 'cmproxy-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SdrInventoryVm.Nodes.Node.NodeEntries, self).__init__()

                    self.yang_name = "node-entries"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"node-entry" : ("node_entry", SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry)}

                    self.node_entry = YList(self)
                    self._segment_path = lambda: "node-entries"

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrInventoryVm.Nodes.Node.NodeEntries, [], name, value)


                class NodeEntry(Entity):
                    """
                    VM information for a node
                    
                    .. attribute:: name  <key>
                    
                    	Node name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: card_type
                    
                    	card type
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: card_type_string
                    
                    	card type string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_ip
                    
                    	node IP address
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_ipv4_string
                    
                    	node IPv4 address string
                    	**type**\:  str
                    
                    	**length:** 0..16
                    
                    .. attribute:: node_name
                    
                    	node name string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: node_sw_state
                    
                    	current software state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: node_sw_state_string
                    
                    	current software state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: nodeid
                    
                    	node ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_id
                    
                    	partner node id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: partner_name
                    
                    	partner name string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: prev_sw_state
                    
                    	previous software state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: prev_sw_state_string
                    
                    	previous software state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: red_state
                    
                    	redundancy state
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: red_state_string
                    
                    	redundancy state string
                    	**type**\:  str
                    
                    	**length:** 0..32
                    
                    .. attribute:: valid
                    
                    	valid flag
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'cmproxy-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, self).__init__()

                        self.yang_name = "node-entry"
                        self.yang_parent_name = "node-entries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.card_type = YLeaf(YType.uint32, "card-type")

                        self.card_type_string = YLeaf(YType.str, "card-type-string")

                        self.node_ip = YLeaf(YType.uint32, "node-ip")

                        self.node_ipv4_string = YLeaf(YType.str, "node-ipv4-string")

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.node_sw_state = YLeaf(YType.uint32, "node-sw-state")

                        self.node_sw_state_string = YLeaf(YType.str, "node-sw-state-string")

                        self.nodeid = YLeaf(YType.int32, "nodeid")

                        self.partner_id = YLeaf(YType.int32, "partner-id")

                        self.partner_name = YLeaf(YType.str, "partner-name")

                        self.prev_sw_state = YLeaf(YType.uint32, "prev-sw-state")

                        self.prev_sw_state_string = YLeaf(YType.str, "prev-sw-state-string")

                        self.red_state = YLeaf(YType.uint32, "red-state")

                        self.red_state_string = YLeaf(YType.str, "red-state-string")

                        self.valid = YLeaf(YType.uint32, "valid")
                        self._segment_path = lambda: "node-entry" + "[name='" + self.name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrInventoryVm.Nodes.Node.NodeEntries.NodeEntry, ['name', 'card_type', 'card_type_string', 'node_ip', 'node_ipv4_string', 'node_name', 'node_sw_state', 'node_sw_state_string', 'nodeid', 'partner_id', 'partner_name', 'prev_sw_state', 'prev_sw_state_string', 'red_state', 'red_state_string', 'valid'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrInventoryVm()
        return self._top_entity

