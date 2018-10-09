""" Cisco_IOS_XR_mpls_io_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-io package operational data.

This module contains definitions
for the following management objects\:
  mpls\-ea\: MPLS IO EA operational data
  mpls\-ma\: mpls ma

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class MplsEa(Entity):
    """
    MPLS IO EA operational data
    
    .. attribute:: nodes
    
    	NODE container class for MPLS IO EA operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsEa.Nodes>`
    
    

    """

    _prefix = 'mpls-io-oper'
    _revision = '2017-05-18'

    def __init__(self):
        super(MplsEa, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-ea"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-io-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", MplsEa.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = MplsEa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-io-oper:mpls-ea"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsEa, [], name, value)


    class Nodes(Entity):
        """
        NODE container class for MPLS IO EA operational
        data
        
        .. attribute:: node
        
        	Per node MPLS IO EA operational data
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsEa.Nodes.Node>`
        
        

        """

        _prefix = 'mpls-io-oper'
        _revision = '2017-05-18'

        def __init__(self):
            super(MplsEa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mpls-ea"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", MplsEa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-io-oper:mpls-ea/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsEa.Nodes, [], name, value)


        class Node(Entity):
            """
            Per node MPLS IO EA operational data
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	MPLS IO EA Interfaces information 
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsEa.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'mpls-io-oper'
            _revision = '2017-05-18'

            def __init__(self):
                super(MplsEa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("interfaces", ("interfaces", MplsEa.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.interfaces = MplsEa.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-io-oper:mpls-ea/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsEa.Nodes.Node, ['node_name'], name, value)


            class Interfaces(Entity):
                """
                MPLS IO EA Interfaces information 
                
                .. attribute:: interface
                
                	MPLS IO EA NODE Interface data 
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsEa.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'mpls-io-oper'
                _revision = '2017-05-18'

                def __init__(self):
                    super(MplsEa.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", MplsEa.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsEa.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    MPLS IO EA NODE Interface data 
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mtu
                    
                    	MTU for fragmentation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bkp_label_stack_depth
                    
                    	Bkp Label Stack Depth
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: srte_label_stack_depth
                    
                    	Srte Label Stack Depth
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pri_label_stack_depth
                    
                    	Pri Label Stack Depth
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'mpls-io-oper'
                    _revision = '2017-05-18'

                    def __init__(self):
                        super(MplsEa.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                            ('bkp_label_stack_depth', (YLeaf(YType.uint8, 'bkp-label-stack-depth'), ['int'])),
                            ('srte_label_stack_depth', (YLeaf(YType.uint8, 'srte-label-stack-depth'), ['int'])),
                            ('pri_label_stack_depth', (YLeaf(YType.uint8, 'pri-label-stack-depth'), ['int'])),
                        ])
                        self.interface_name = None
                        self.mtu = None
                        self.bkp_label_stack_depth = None
                        self.srte_label_stack_depth = None
                        self.pri_label_stack_depth = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsEa.Nodes.Node.Interfaces.Interface, ['interface_name', 'mtu', 'bkp_label_stack_depth', 'srte_label_stack_depth', 'pri_label_stack_depth'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsEa()
        return self._top_entity

class MplsMa(Entity):
    """
    mpls ma
    
    .. attribute:: nodes
    
    	NODE container class for MPLS IO MA operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsMa.Nodes>`
    
    

    """

    _prefix = 'mpls-io-oper'
    _revision = '2017-05-18'

    def __init__(self):
        super(MplsMa, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-ma"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-io-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", MplsMa.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = MplsMa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-io-oper:mpls-ma"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsMa, [], name, value)


    class Nodes(Entity):
        """
        NODE container class for MPLS IO MA operational
        data
        
        .. attribute:: node
        
        	Per node MPLS IO MA operational data
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsMa.Nodes.Node>`
        
        

        """

        _prefix = 'mpls-io-oper'
        _revision = '2017-05-18'

        def __init__(self):
            super(MplsMa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "mpls-ma"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", MplsMa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-io-oper:mpls-ma/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsMa.Nodes, [], name, value)


        class Node(Entity):
            """
            Per node MPLS IO MA operational data
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interfaces
            
            	MPLS IO MA Interfaces information 
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsMa.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'mpls-io-oper'
            _revision = '2017-05-18'

            def __init__(self):
                super(MplsMa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("interfaces", ("interfaces", MplsMa.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.interfaces = MplsMa.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-io-oper:mpls-ma/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsMa.Nodes.Node, ['node_name'], name, value)


            class Interfaces(Entity):
                """
                MPLS IO MA Interfaces information 
                
                .. attribute:: interface
                
                	MPLS IO MA NODE Interface data 
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_io_oper.MplsMa.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'mpls-io-oper'
                _revision = '2017-05-18'

                def __init__(self):
                    super(MplsMa.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", MplsMa.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsMa.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    MPLS IO MA NODE Interface data 
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: mtu
                    
                    	MTU for fragmentation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bkp_label_stack_depth
                    
                    	Bkp Label Stack Depth
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: srte_label_stack_depth
                    
                    	Srte Label Stack Depth
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: pri_label_stack_depth
                    
                    	Pri Label Stack Depth
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'mpls-io-oper'
                    _revision = '2017-05-18'

                    def __init__(self):
                        super(MplsMa.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                            ('bkp_label_stack_depth', (YLeaf(YType.uint8, 'bkp-label-stack-depth'), ['int'])),
                            ('srte_label_stack_depth', (YLeaf(YType.uint8, 'srte-label-stack-depth'), ['int'])),
                            ('pri_label_stack_depth', (YLeaf(YType.uint8, 'pri-label-stack-depth'), ['int'])),
                        ])
                        self.interface_name = None
                        self.mtu = None
                        self.bkp_label_stack_depth = None
                        self.srte_label_stack_depth = None
                        self.pri_label_stack_depth = None
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsMa.Nodes.Node.Interfaces.Interface, ['interface_name', 'mtu', 'bkp_label_stack_depth', 'srte_label_stack_depth', 'pri_label_stack_depth'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsMa()
        return self._top_entity

