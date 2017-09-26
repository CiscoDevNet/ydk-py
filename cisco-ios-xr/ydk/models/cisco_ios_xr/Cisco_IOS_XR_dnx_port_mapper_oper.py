""" Cisco_IOS_XR_dnx_port_mapper_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-port\-mapper package operational data.

This module contains definitions
for the following management objects\:
  oor\: Out of Resource Data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Oor(Entity):
    """
    Out of Resource Data
    
    .. attribute:: nodes
    
    	OOR data for available nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes>`
    
    

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
        self._child_container_classes = {"nodes" : ("nodes", Oor.Nodes)}
        self._child_list_classes = {}

        self.nodes = Oor.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-dnx-port-mapper-oper:oor"


    class Nodes(Entity):
        """
        OOR data for available nodes
        
        .. attribute:: node
        
        	DPA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-port-mapper-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Oor.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "oor"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", Oor.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-dnx-port-mapper-oper:oor/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Oor.Nodes, [], name, value)


        class Node(Entity):
            """
            DPA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_names
            
            	OOR Interface Information
            	**type**\:   :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames>`
            
            .. attribute:: summary
            
            	Summary
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'dnx-port-mapper-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Oor.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interface-names" : ("interface_names", Oor.Nodes.Node.InterfaceNames), "summary" : ("summary", Oor.Nodes.Node.Summary)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_names = Oor.Nodes.Node.InterfaceNames()
                self.interface_names.parent = self
                self._children_name_map["interface_names"] = "interface-names"
                self._children_yang_names.add("interface-names")

                self.summary = Oor.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-dnx-port-mapper-oper:oor/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Oor.Nodes.Node, ['node_name'], name, value)


            class InterfaceNames(Entity):
                """
                OOR Interface Information
                
                .. attribute:: interface_name
                
                	OOR Data for particular interface
                	**type**\: list of    :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames.InterfaceName>`
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Oor.Nodes.Node.InterfaceNames, self).__init__()

                    self.yang_name = "interface-names"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-name" : ("interface_name", Oor.Nodes.Node.InterfaceNames.InterfaceName)}

                    self.interface_name = YList(self)
                    self._segment_path = lambda: "interface-names"

                def __setattr__(self, name, value):
                    self._perform_setattr(Oor.Nodes.Node.InterfaceNames, [], name, value)


                class InterfaceName(Entity):
                    """
                    OOR Data for particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface
                    
                    	Interface details
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface>`
                    
                    

                    """

                    _prefix = 'dnx-port-mapper-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Oor.Nodes.Node.InterfaceNames.InterfaceName, self).__init__()

                        self.yang_name = "interface-name"
                        self.yang_parent_name = "interface-names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface" : ("interface", Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface)}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface = YList(self)
                        self._segment_path = lambda: "interface-name" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Oor.Nodes.Node.InterfaceNames.InterfaceName, ['interface_name'], name, value)


                    class Interface(Entity):
                        """
                        Interface details
                        
                        .. attribute:: hardware_resource
                        
                        	Type of harware resoruce
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	Name of the interface
                        	**type**\:  str
                        
                        .. attribute:: interface_status
                        
                        	The current state of the interface
                        	**type**\:  str
                        
                        .. attribute:: npu_id
                        
                        	Npuid of the interface
                        	**type**\:  str
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'dnx-port-mapper-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interface-name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.hardware_resource = YLeaf(YType.str, "hardware-resource")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_status = YLeaf(YType.str, "interface-status")

                            self.npu_id = YLeaf(YType.str, "npu-id")

                            self.time_stamp = YLeaf(YType.str, "time-stamp")
                            self._segment_path = lambda: "interface"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, ['hardware_resource', 'interface_name', 'interface_status', 'npu_id', 'time_stamp'], name, value)


            class Summary(Entity):
                """
                Summary
                
                .. attribute:: green
                
                	interfaces in green state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: red
                
                	interfaces in red state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: yel_low
                
                	interfaces in yellow state
                	**type**\:  int
                
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
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.green = YLeaf(YType.uint32, "green")

                    self.red = YLeaf(YType.uint32, "red")

                    self.yel_low = YLeaf(YType.uint32, "yel-low")
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Oor.Nodes.Node.Summary, ['green', 'red', 'yel_low'], name, value)

    def clone_ptr(self):
        self._top_entity = Oor()
        return self._top_entity

