""" Cisco_IOS_XR_fretta_grid_svr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-grid\-svr package operational data.

This module contains definitions
for the following management objects\:
  grid\: GRID operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Grid(Entity):
    """
    GRID operational data
    
    .. attribute:: nodes
    
    	Table of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes>`
    
    

    """

    _prefix = 'fretta-grid-svr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Grid, self).__init__()
        self._top_entity = None

        self.yang_name = "grid"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-grid-svr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Grid.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Grid.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-grid-svr-oper:grid"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Grid, [], name, value)


    class Nodes(Entity):
        """
        Table of nodes
        
        .. attribute:: node
        
        	Operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node>`
        
        

        """

        _prefix = 'fretta-grid-svr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Grid.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "grid"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Grid.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-grid-svr-oper:grid/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Grid.Nodes, [], name, value)


        class Node(Entity):
            """
            Operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: client_xr
            
            	GRID Client Table
            	**type**\:  :py:class:`ClientXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr>`
            
            .. attribute:: clients
            
            	GRID Client Consistency Check
            	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients>`
            
            

            """

            _prefix = 'fretta-grid-svr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Grid.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("client-xr", ("client_xr", Grid.Nodes.Node.ClientXr)), ("clients", ("clients", Grid.Nodes.Node.Clients))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.client_xr = Grid.Nodes.Node.ClientXr()
                self.client_xr.parent = self
                self._children_name_map["client_xr"] = "client-xr"

                self.clients = Grid.Nodes.Node.Clients()
                self.clients.parent = self
                self._children_name_map["clients"] = "clients"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-grid-svr-oper:grid/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Grid.Nodes.Node, ['node_name'], name, value)


            class ClientXr(Entity):
                """
                GRID Client Table
                
                .. attribute:: client
                
                	GRID Client Database
                	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr.Client>`
                
                

                """

                _prefix = 'fretta-grid-svr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Grid.Nodes.Node.ClientXr, self).__init__()

                    self.yang_name = "client-xr"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client", ("client", Grid.Nodes.Node.ClientXr.Client))])
                    self._leafs = OrderedDict()

                    self.client = YList(self)
                    self._segment_path = lambda: "client-xr"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Grid.Nodes.Node.ClientXr, [], name, value)


                class Client(Entity):
                    """
                    GRID Client Database
                    
                    .. attribute:: client_name  (key)
                    
                    	Client name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_data
                    
                    	Client information
                    	**type**\: list of  		 :py:class:`ClientData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.ClientXr.Client.ClientData>`
                    
                    

                    """

                    _prefix = 'fretta-grid-svr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Grid.Nodes.Node.ClientXr.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "client-xr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['client_name']
                        self._child_classes = OrderedDict([("client-data", ("client_data", Grid.Nodes.Node.ClientXr.Client.ClientData))])
                        self._leafs = OrderedDict([
                            ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                        ])
                        self.client_name = None

                        self.client_data = YList(self)
                        self._segment_path = lambda: "client" + "[client-name='" + str(self.client_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Grid.Nodes.Node.ClientXr.Client, ['client_name'], name, value)


                    class ClientData(Entity):
                        """
                        Client information
                        
                        .. attribute:: res_id
                        
                        	Resource ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-grid-svr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Grid.Nodes.Node.ClientXr.Client.ClientData, self).__init__()

                            self.yang_name = "client-data"
                            self.yang_parent_name = "client"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('res_id', (YLeaf(YType.uint32, 'res-id'), ['int'])),
                            ])
                            self.res_id = None
                            self._segment_path = lambda: "client-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Grid.Nodes.Node.ClientXr.Client.ClientData, ['res_id'], name, value)


            class Clients(Entity):
                """
                GRID Client Consistency Check
                
                .. attribute:: client
                
                	GRID Client Consistency Check
                	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients.Client>`
                
                

                """

                _prefix = 'fretta-grid-svr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Grid.Nodes.Node.Clients, self).__init__()

                    self.yang_name = "clients"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("client", ("client", Grid.Nodes.Node.Clients.Client))])
                    self._leafs = OrderedDict()

                    self.client = YList(self)
                    self._segment_path = lambda: "clients"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Grid.Nodes.Node.Clients, [], name, value)


                class Client(Entity):
                    """
                    GRID Client Consistency Check
                    
                    .. attribute:: client_name  (key)
                    
                    	Client name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: client_data
                    
                    	Client information
                    	**type**\: list of  		 :py:class:`ClientData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper.Grid.Nodes.Node.Clients.Client.ClientData>`
                    
                    

                    """

                    _prefix = 'fretta-grid-svr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Grid.Nodes.Node.Clients.Client, self).__init__()

                        self.yang_name = "client"
                        self.yang_parent_name = "clients"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['client_name']
                        self._child_classes = OrderedDict([("client-data", ("client_data", Grid.Nodes.Node.Clients.Client.ClientData))])
                        self._leafs = OrderedDict([
                            ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                        ])
                        self.client_name = None

                        self.client_data = YList(self)
                        self._segment_path = lambda: "client" + "[client-name='" + str(self.client_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Grid.Nodes.Node.Clients.Client, ['client_name'], name, value)


                    class ClientData(Entity):
                        """
                        Client information
                        
                        .. attribute:: res_id
                        
                        	Resource ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'fretta-grid-svr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Grid.Nodes.Node.Clients.Client.ClientData, self).__init__()

                            self.yang_name = "client-data"
                            self.yang_parent_name = "client"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('res_id', (YLeaf(YType.uint32, 'res-id'), ['int'])),
                            ])
                            self.res_id = None
                            self._segment_path = lambda: "client-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Grid.Nodes.Node.Clients.Client.ClientData, ['res_id'], name, value)

    def clone_ptr(self):
        self._top_entity = Grid()
        return self._top_entity

