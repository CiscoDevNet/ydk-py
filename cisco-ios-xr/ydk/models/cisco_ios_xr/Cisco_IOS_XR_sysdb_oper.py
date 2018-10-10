""" Cisco_IOS_XR_sysdb_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sysdb package operational data.

This module contains definitions
for the following management objects\:
  sysdb\-connections\: Sysdb health on client connections
  sysdb\: sysdb

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class SysdbConnections(Entity):
    """
    Sysdb health on client connections
    
    .. attribute:: nodes
    
    	Node operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper.SysdbConnections.Nodes>`
    
    

    """

    _prefix = 'sysdb-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SysdbConnections, self).__init__()
        self._top_entity = None

        self.yang_name = "sysdb-connections"
        self.yang_parent_name = "Cisco-IOS-XR-sysdb-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", SysdbConnections.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = SysdbConnections.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-sysdb-oper:sysdb-connections"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SysdbConnections, [], name, value)


    class Nodes(Entity):
        """
        Node operational data
        
        .. attribute:: node
        
        	Per\-node Sysdb health on connection
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysdb_oper.SysdbConnections.Nodes.Node>`
        
        

        """

        _prefix = 'sysdb-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SysdbConnections.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "sysdb-connections"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SysdbConnections.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysdb-oper:sysdb-connections/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SysdbConnections.Nodes, [], name, value)


        class Node(Entity):
            """
            Per\-node Sysdb health on connection
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: connections
            
            	Per\-node Sysdb Client Connections
            	**type**\: str
            
            

            """

            _prefix = 'sysdb-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SysdbConnections.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ('connections', (YLeaf(YType.str, 'connections'), ['str'])),
                ])
                self.node_name = None
                self.connections = None
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sysdb-oper:sysdb-connections/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SysdbConnections.Nodes.Node, ['node_name', 'connections'], name, value)

    def clone_ptr(self):
        self._top_entity = SysdbConnections()
        return self._top_entity

class Sysdb(Entity):
    """
    sysdb
    
    .. attribute:: configuration_space
    
    	Sysdb health for configuration space
    	**type**\: str
    
    .. attribute:: memory
    
    	Sysdb health on memory consumption
    	**type**\: str
    
    .. attribute:: ipc_space
    
    	Sysdb health for operational space
    	**type**\: str
    
    .. attribute:: cpu
    
    	Sysdb health on cpu consumption
    	**type**\: str
    
    

    """

    _prefix = 'sysdb-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Sysdb, self).__init__()
        self._top_entity = None

        self.yang_name = "sysdb"
        self.yang_parent_name = "Cisco-IOS-XR-sysdb-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('configuration_space', (YLeaf(YType.str, 'configuration-space'), ['str'])),
            ('memory', (YLeaf(YType.str, 'memory'), ['str'])),
            ('ipc_space', (YLeaf(YType.str, 'ipc-space'), ['str'])),
            ('cpu', (YLeaf(YType.str, 'cpu'), ['str'])),
        ])
        self.configuration_space = None
        self.memory = None
        self.ipc_space = None
        self.cpu = None
        self._segment_path = lambda: "Cisco-IOS-XR-sysdb-oper:sysdb"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Sysdb, ['configuration_space', 'memory', 'ipc_space', 'cpu'], name, value)

    def clone_ptr(self):
        self._top_entity = Sysdb()
        return self._top_entity

