""" Cisco_IOS_XR_pppoe_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pppoe\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppoe\-ea\: PPPoE Ea data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PppoeEa(Entity):
    """
    PPPoE Ea data
    
    .. attribute:: nodes
    
    	PPPOE\_EA list of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes>`
    
    

    """

    _prefix = 'pppoe-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PppoeEa, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe-ea"
        self.yang_parent_name = "Cisco-IOS-XR-pppoe-ea-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", PppoeEa.Nodes)}
        self._child_list_classes = {}

        self.nodes = PppoeEa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea"


    class Nodes(Entity):
        """
        PPPOE\_EA list of nodes
        
        .. attribute:: node
        
        	PPPOE\-EA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node>`
        
        

        """

        _prefix = 'pppoe-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PppoeEa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppoe-ea"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", PppoeEa.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PppoeEa.Nodes, [], name, value)


        class Node(Entity):
            """
            PPPOE\-EA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_ids
            
            	PPPoE interface info
            	**type**\:   :py:class:`InterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds>`
            
            .. attribute:: parent_interface_ids
            
            	PPPoE parent interface info
            	**type**\:   :py:class:`ParentInterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds>`
            
            

            """

            _prefix = 'pppoe-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PppoeEa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interface-ids" : ("interface_ids", PppoeEa.Nodes.Node.InterfaceIds), "parent-interface-ids" : ("parent_interface_ids", PppoeEa.Nodes.Node.ParentInterfaceIds)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_ids = PppoeEa.Nodes.Node.InterfaceIds()
                self.interface_ids.parent = self
                self._children_name_map["interface_ids"] = "interface-ids"
                self._children_yang_names.add("interface-ids")

                self.parent_interface_ids = PppoeEa.Nodes.Node.ParentInterfaceIds()
                self.parent_interface_ids.parent = self
                self._children_name_map["parent_interface_ids"] = "parent-interface-ids"
                self._children_yang_names.add("parent-interface-ids")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PppoeEa.Nodes.Node, ['node_name'], name, value)


            class InterfaceIds(Entity):
                """
                PPPoE interface info
                
                .. attribute:: interface_id
                
                	PPPoE interface info
                	**type**\: list of    :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId>`
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeEa.Nodes.Node.InterfaceIds, self).__init__()

                    self.yang_name = "interface-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface-id" : ("interface_id", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId)}

                    self.interface_id = YList(self)
                    self._segment_path = lambda: "interface-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds, [], name, value)


                class InterfaceId(Entity):
                    """
                    PPPoE interface info
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\:  bool
                    
                    .. attribute:: is_platform_created
                    
                    	Is Platform created
                    	**type**\:  bool
                    
                    .. attribute:: is_priority_set
                    
                    	Is Priority Set
                    	**type**\:  bool
                    
                    .. attribute:: local_mac
                    
                    	Local Mac\-address
                    	**type**\:   :py:class:`LocalMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac>`
                    
                    .. attribute:: parent_interface
                    
                    	Parent Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: peer_mac
                    
                    	Peer Mac\-address
                    	**type**\:   :py:class:`PeerMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac>`
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:   :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac>`
                    
                    .. attribute:: vlanid
                    
                    	VLAN Ids
                    	**type**\:  list of int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, self).__init__()

                        self.yang_name = "interface-id"
                        self.yang_parent_name = "interface-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"local-mac" : ("local_mac", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac), "peer-mac" : ("peer_mac", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac), "srgv-mac" : ("srgv_mac", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_in_sync = YLeaf(YType.boolean, "is-in-sync")

                        self.is_platform_created = YLeaf(YType.boolean, "is-platform-created")

                        self.is_priority_set = YLeaf(YType.boolean, "is-priority-set")

                        self.parent_interface = YLeaf(YType.str, "parent-interface")

                        self.priority = YLeaf(YType.uint8, "priority")

                        self.session_id = YLeaf(YType.uint16, "session-id")

                        self.vlanid = YLeafList(YType.uint16, "vlanid")

                        self.local_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac()
                        self.local_mac.parent = self
                        self._children_name_map["local_mac"] = "local-mac"
                        self._children_yang_names.add("local-mac")

                        self.peer_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac()
                        self.peer_mac.parent = self
                        self._children_name_map["peer_mac"] = "peer-mac"
                        self._children_yang_names.add("peer-mac")

                        self.srgv_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self._children_name_map["srgv_mac"] = "srgv-mac"
                        self._children_yang_names.add("srgv-mac")
                        self._segment_path = lambda: "interface-id" + "[interface-name='" + self.interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, ['interface_name', 'interface', 'is_in_sync', 'is_platform_created', 'is_priority_set', 'parent_interface', 'priority', 'session_id', 'vlanid'], name, value)


                    class LocalMac(Entity):
                        """
                        Local Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, self).__init__()

                            self.yang_name = "local-mac"
                            self.yang_parent_name = "interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "local-mac"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, ['macaddr'], name, value)


                    class PeerMac(Entity):
                        """
                        Peer Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, self).__init__()

                            self.yang_name = "peer-mac"
                            self.yang_parent_name = "interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "peer-mac"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, ['macaddr'], name, value)


                    class SrgvMac(Entity):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, self).__init__()

                            self.yang_name = "srgv-mac"
                            self.yang_parent_name = "interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "srgv-mac"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, ['macaddr'], name, value)


            class ParentInterfaceIds(Entity):
                """
                PPPoE parent interface info
                
                .. attribute:: parent_interface_id
                
                	PPPoE parent interface info
                	**type**\: list of    :py:class:`ParentInterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId>`
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PppoeEa.Nodes.Node.ParentInterfaceIds, self).__init__()

                    self.yang_name = "parent-interface-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"parent-interface-id" : ("parent_interface_id", PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId)}

                    self.parent_interface_id = YList(self)
                    self._segment_path = lambda: "parent-interface-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeEa.Nodes.Node.ParentInterfaceIds, [], name, value)


                class ParentInterfaceId(Entity):
                    """
                    PPPoE parent interface info
                    
                    .. attribute:: parent_interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\:  bool
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:   :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac>`
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, self).__init__()

                        self.yang_name = "parent-interface-id"
                        self.yang_parent_name = "parent-interface-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"srgv-mac" : ("srgv_mac", PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac)}
                        self._child_list_classes = {}

                        self.parent_interface_name = YLeaf(YType.str, "parent-interface-name")

                        self.interface = YLeaf(YType.str, "interface")

                        self.is_in_sync = YLeaf(YType.boolean, "is-in-sync")

                        self.srgv_mac = PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self._children_name_map["srgv_mac"] = "srgv-mac"
                        self._children_yang_names.add("srgv-mac")
                        self._segment_path = lambda: "parent-interface-id" + "[parent-interface-name='" + self.parent_interface_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, ['parent_interface_name', 'interface', 'is_in_sync'], name, value)


                    class SrgvMac(Entity):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, self).__init__()

                            self.yang_name = "srgv-mac"
                            self.yang_parent_name = "parent-interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.macaddr = YLeaf(YType.str, "macaddr")
                            self._segment_path = lambda: "srgv-mac"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, ['macaddr'], name, value)

    def clone_ptr(self):
        self._top_entity = PppoeEa()
        return self._top_entity

