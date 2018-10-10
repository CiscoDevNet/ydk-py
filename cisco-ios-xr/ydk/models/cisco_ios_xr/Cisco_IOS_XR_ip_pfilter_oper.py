""" Cisco_IOS_XR_ip_pfilter_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-pfilter package operational data.

This module contains definitions
for the following management objects\:
  pfilter\-ma\: Root class of PfilterMa Oper schema

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PfilterMa(Entity):
    """
    Root class of PfilterMa Oper schema
    
    .. attribute:: nodes
    
    	Node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes>`
    
    

    """

    _prefix = 'ip-pfilter-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PfilterMa, self).__init__()
        self._top_entity = None

        self.yang_name = "pfilter-ma"
        self.yang_parent_name = "Cisco-IOS-XR-ip-pfilter-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PfilterMa.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PfilterMa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PfilterMa, [], name, value)


    class Nodes(Entity):
        """
        Node\-specific operational data
        
        .. attribute:: node
        
        	PfilterMa operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node>`
        
        

        """

        _prefix = 'ip-pfilter-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PfilterMa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pfilter-ma"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PfilterMa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PfilterMa.Nodes, [], name, value)


        class Node(Entity):
            """
            PfilterMa operational data for a particular
            node
            
            .. attribute:: node_name  (key)
            
            	The node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process
            
            	Operational data for pfilter
            	**type**\:  :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process>`
            
            

            """

            _prefix = 'ip-pfilter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PfilterMa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("process", ("process", PfilterMa.Nodes.Node.Process))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.process = PfilterMa.Nodes.Node.Process()
                self.process.parent = self
                self._children_name_map["process"] = "process"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-pfilter-oper:pfilter-ma/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PfilterMa.Nodes.Node, ['node_name'], name, value)


            class Process(Entity):
                """
                Operational data for pfilter
                
                .. attribute:: ipv6
                
                	Operational data for pfilter
                	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6>`
                
                .. attribute:: ipv4
                
                	Operational data for pfilter
                	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4>`
                
                

                """

                _prefix = 'ip-pfilter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PfilterMa.Nodes.Node.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv6", ("ipv6", PfilterMa.Nodes.Node.Process.Ipv6)), ("ipv4", ("ipv4", PfilterMa.Nodes.Node.Process.Ipv4))])
                    self._leafs = OrderedDict()

                    self.ipv6 = PfilterMa.Nodes.Node.Process.Ipv6()
                    self.ipv6.parent = self
                    self._children_name_map["ipv6"] = "ipv6"

                    self.ipv4 = PfilterMa.Nodes.Node.Process.Ipv4()
                    self.ipv4.parent = self
                    self._children_name_map["ipv4"] = "ipv4"
                    self._segment_path = lambda: "process"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PfilterMa.Nodes.Node.Process, [], name, value)


                class Ipv6(Entity):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: acl_info_table
                    
                    	Operational data for pfilter
                    	**type**\:  :py:class:`AclInfoTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PfilterMa.Nodes.Node.Process.Ipv6, self).__init__()

                        self.yang_name = "ipv6"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("acl-info-table", ("acl_info_table", PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable))])
                        self._leafs = OrderedDict()

                        self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable()
                        self.acl_info_table.parent = self
                        self._children_name_map["acl_info_table"] = "acl-info-table"
                        self._segment_path = lambda: "ipv6"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv6, [], name, value)


                    class AclInfoTable(Entity):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface_infos
                        
                        	Operational data for pfilter
                        	**type**\:  :py:class:`InterfaceInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable, self).__init__()

                            self.yang_name = "acl-info-table"
                            self.yang_parent_name = "ipv6"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-infos", ("interface_infos", PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos))])
                            self._leafs = OrderedDict()

                            self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos()
                            self.interface_infos.parent = self
                            self._children_name_map["interface_infos"] = "interface-infos"
                            self._segment_path = lambda: "acl-info-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable, [], name, value)


                        class InterfaceInfos(Entity):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_info
                            
                            	Operational data for pfilter in bag
                            	**type**\: list of  		 :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo>`
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos, self).__init__()

                                self.yang_name = "interface-infos"
                                self.yang_parent_name = "acl-info-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("interface-info", ("interface_info", PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo))])
                                self._leafs = OrderedDict()

                                self.interface_info = YList(self)
                                self._segment_path = lambda: "interface-infos"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos, [], name, value)


                            class InterfaceInfo(Entity):
                                """
                                Operational data for pfilter in bag
                                
                                .. attribute:: interface_name  (key)
                                
                                	Name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: acl_info
                                
                                	acl information
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ip-pfilter-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__init__()

                                    self.yang_name = "interface-info"
                                    self.yang_parent_name = "interface-infos"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('acl_info', (YLeaf(YType.str, 'acl-info'), ['str'])),
                                    ])
                                    self.interface_name = None
                                    self.acl_info = None
                                    self._segment_path = lambda: "interface-info" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo, ['interface_name', u'acl_info'], name, value)


                class Ipv4(Entity):
                    """
                    Operational data for pfilter
                    
                    .. attribute:: acl_info_table
                    
                    	Operational data for pfilter
                    	**type**\:  :py:class:`AclInfoTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable>`
                    
                    

                    """

                    _prefix = 'ip-pfilter-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PfilterMa.Nodes.Node.Process.Ipv4, self).__init__()

                        self.yang_name = "ipv4"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("acl-info-table", ("acl_info_table", PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable))])
                        self._leafs = OrderedDict()

                        self.acl_info_table = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable()
                        self.acl_info_table.parent = self
                        self._children_name_map["acl_info_table"] = "acl-info-table"
                        self._segment_path = lambda: "ipv4"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv4, [], name, value)


                    class AclInfoTable(Entity):
                        """
                        Operational data for pfilter
                        
                        .. attribute:: interface_infos
                        
                        	Operational data for pfilter
                        	**type**\:  :py:class:`InterfaceInfos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos>`
                        
                        

                        """

                        _prefix = 'ip-pfilter-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable, self).__init__()

                            self.yang_name = "acl-info-table"
                            self.yang_parent_name = "ipv4"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-infos", ("interface_infos", PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos))])
                            self._leafs = OrderedDict()

                            self.interface_infos = PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos()
                            self.interface_infos.parent = self
                            self._children_name_map["interface_infos"] = "interface-infos"
                            self._segment_path = lambda: "acl-info-table"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable, [], name, value)


                        class InterfaceInfos(Entity):
                            """
                            Operational data for pfilter
                            
                            .. attribute:: interface_info
                            
                            	Operational data for pfilter in bag
                            	**type**\: list of  		 :py:class:`InterfaceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper.PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo>`
                            
                            

                            """

                            _prefix = 'ip-pfilter-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos, self).__init__()

                                self.yang_name = "interface-infos"
                                self.yang_parent_name = "acl-info-table"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("interface-info", ("interface_info", PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo))])
                                self._leafs = OrderedDict()

                                self.interface_info = YList(self)
                                self._segment_path = lambda: "interface-infos"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos, [], name, value)


                            class InterfaceInfo(Entity):
                                """
                                Operational data for pfilter in bag
                                
                                .. attribute:: interface_name  (key)
                                
                                	Name of the interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: acl_info
                                
                                	acl information
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ip-pfilter-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo, self).__init__()

                                    self.yang_name = "interface-info"
                                    self.yang_parent_name = "interface-infos"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('acl_info', (YLeaf(YType.str, 'acl-info'), ['str'])),
                                    ])
                                    self.interface_name = None
                                    self.acl_info = None
                                    self._segment_path = lambda: "interface-info" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo, ['interface_name', u'acl_info'], name, value)

    def clone_ptr(self):
        self._top_entity = PfilterMa()
        return self._top_entity

