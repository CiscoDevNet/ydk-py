""" Cisco_IOS_XR_dnx_port_mapper_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-port\-mapper package operational data.

This module contains definitions
for the following management objects\:
  oor\: Out of Resource Data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Oor(Entity):
    """
    Out of Resource Data
    
    .. attribute:: nodes
    
    	OOR data for available nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes>`
    
    

    """

    _prefix = 'dnx-port-mapper-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Oor, self).__init__()
        self._top_entity = None

        self.yang_name = "oor"
        self.yang_parent_name = "Cisco-IOS-XR-dnx-port-mapper-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Oor.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Oor.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-dnx-port-mapper-oper:oor"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Oor, [], name, value)


    class Nodes(Entity):
        """
        OOR data for available nodes
        
        .. attribute:: node
        
        	DPA operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-port-mapper-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Oor.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "oor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Oor.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-dnx-port-mapper-oper:oor/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Oor.Nodes, [], name, value)


        class Node(Entity):
            """
            DPA operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: summary
            
            	Summary
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.Summary>`
            
            .. attribute:: interface_names
            
            	OOR Interface Information
            	**type**\:  :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames>`
            
            

            """

            _prefix = 'dnx-port-mapper-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Oor.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("summary", ("summary", Oor.Nodes.Node.Summary)), ("interface-names", ("interface_names", Oor.Nodes.Node.InterfaceNames))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.summary = Oor.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.interface_names = Oor.Nodes.Node.InterfaceNames()
                self.interface_names.parent = self
                self._children_name_map["interface_names"] = "interface-names"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dnx-port-mapper-oper:oor/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Oor.Nodes.Node, ['node_name'], name, value)


            class Summary(Entity):
                """
                Summary
                
                .. attribute:: red
                
                	interfaces in red state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: green
                
                	interfaces in green state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: yel_low
                
                	interfaces in yellow state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Oor.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('red', (YLeaf(YType.uint32, 'red'), ['int'])),
                        ('green', (YLeaf(YType.uint32, 'green'), ['int'])),
                        ('yel_low', (YLeaf(YType.uint32, 'yel-low'), ['int'])),
                    ])
                    self.red = None
                    self.green = None
                    self.yel_low = None
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oor.Nodes.Node.Summary, ['red', 'green', 'yel_low'], name, value)


            class InterfaceNames(Entity):
                """
                OOR Interface Information
                
                .. attribute:: interface_name
                
                	OOR Data for particular interface
                	**type**\: list of  		 :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames.InterfaceName>`
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Oor.Nodes.Node.InterfaceNames, self).__init__()

                    self.yang_name = "interface-names"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-name", ("interface_name", Oor.Nodes.Node.InterfaceNames.InterfaceName))])
                    self._leafs = OrderedDict()

                    self.interface_name = YList(self)
                    self._segment_path = lambda: "interface-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Oor.Nodes.Node.InterfaceNames, [], name, value)


                class InterfaceName(Entity):
                    """
                    OOR Data for particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of the interface
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface
                    
                    	Interface details
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface>`
                    
                    

                    """

                    _prefix = 'dnx-port-mapper-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Oor.Nodes.Node.InterfaceNames.InterfaceName, self).__init__()

                        self.yang_name = "interface-name"
                        self.yang_parent_name = "interface-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("interface", ("interface", Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.interface = YList(self)
                        self._segment_path = lambda: "interface-name" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oor.Nodes.Node.InterfaceNames.InterfaceName, ['interface_name'], name, value)


                    class Interface(Entity):
                        """
                        Interface details
                        
                        .. attribute:: interface_name
                        
                        	Name of the interface
                        	**type**\: str
                        
                        .. attribute:: interface_status
                        
                        	The current state of the interface
                        	**type**\: str
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp
                        	**type**\: str
                        
                        .. attribute:: npu_id
                        
                        	Npuid of the interface
                        	**type**\: str
                        
                        .. attribute:: hardware_resource
                        
                        	Type of harware resoruce
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'dnx-port-mapper-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interface-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_status', (YLeaf(YType.str, 'interface-status'), ['str'])),
                                ('time_stamp', (YLeaf(YType.str, 'time-stamp'), ['str'])),
                                ('npu_id', (YLeaf(YType.str, 'npu-id'), ['str'])),
                                ('hardware_resource', (YLeaf(YType.str, 'hardware-resource'), ['str'])),
                            ])
                            self.interface_name = None
                            self.interface_status = None
                            self.time_stamp = None
                            self.npu_id = None
                            self.hardware_resource = None
                            self._segment_path = lambda: "interface"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, ['interface_name', 'interface_status', 'time_stamp', 'npu_id', 'hardware_resource'], name, value)

    def clone_ptr(self):
        self._top_entity = Oor()
        return self._top_entity

