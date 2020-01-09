""" Cisco_IOS_XR_pppoe_ea_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR pppoe\-ea package operational data.

This module contains definitions
for the following management objects\:
  pppoe\-ea\: PPPoE Ea data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PppoeEa(_Entity_):
    """
    PPPoE Ea data
    
    .. attribute:: nodes
    
    	PPPOE\_EA list of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'pppoe-ea-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(PppoeEa, self).__init__()
        self._top_entity = None

        self.yang_name = "pppoe-ea"
        self.yang_parent_name = "Cisco-IOS-XR-pppoe-ea-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PppoeEa.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PppoeEa.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PppoeEa, [], name, value)


    class Nodes(_Entity_):
        """
        PPPOE\_EA list of nodes
        
        .. attribute:: node
        
        	PPPOE\-EA operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'pppoe-ea-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(PppoeEa.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "pppoe-ea"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PppoeEa.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PppoeEa.Nodes, [], name, value)


        class Node(_Entity_):
            """
            PPPOE\-EA operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: parent_interface_ids
            
            	PPPoE parent interface info
            	**type**\:  :py:class:`ParentInterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds>`
            
            	**config**\: False
            
            .. attribute:: interface_ids
            
            	PPPoE interface info
            	**type**\:  :py:class:`InterfaceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds>`
            
            	**config**\: False
            
            

            """

            _prefix = 'pppoe-ea-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(PppoeEa.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("parent-interface-ids", ("parent_interface_ids", PppoeEa.Nodes.Node.ParentInterfaceIds)), ("interface-ids", ("interface_ids", PppoeEa.Nodes.Node.InterfaceIds))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.parent_interface_ids = PppoeEa.Nodes.Node.ParentInterfaceIds()
                self.parent_interface_ids.parent = self
                self._children_name_map["parent_interface_ids"] = "parent-interface-ids"

                self.interface_ids = PppoeEa.Nodes.Node.InterfaceIds()
                self.interface_ids.parent = self
                self._children_name_map["interface_ids"] = "interface-ids"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-pppoe-ea-oper:pppoe-ea/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PppoeEa.Nodes.Node, ['node_name'], name, value)


            class ParentInterfaceIds(_Entity_):
                """
                PPPoE parent interface info
                
                .. attribute:: parent_interface_id
                
                	PPPoE parent interface info
                	**type**\: list of  		 :py:class:`ParentInterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PppoeEa.Nodes.Node.ParentInterfaceIds, self).__init__()

                    self.yang_name = "parent-interface-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("parent-interface-id", ("parent_interface_id", PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId))])
                    self._leafs = OrderedDict()

                    self.parent_interface_id = YList(self)
                    self._segment_path = lambda: "parent-interface-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeEa.Nodes.Node.ParentInterfaceIds, [], name, value)


                class ParentInterfaceId(_Entity_):
                    """
                    PPPoE parent interface info
                    
                    .. attribute:: parent_interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:  :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, self).__init__()

                        self.yang_name = "parent-interface-id"
                        self.yang_parent_name = "parent-interface-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['parent_interface_name']
                        self._child_classes = OrderedDict([("srgv-mac", ("srgv_mac", PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac))])
                        self._leafs = OrderedDict([
                            ('parent_interface_name', (YLeaf(YType.str, 'parent-interface-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('is_in_sync', (YLeaf(YType.boolean, 'is-in-sync'), ['bool'])),
                        ])
                        self.parent_interface_name = None
                        self.interface = None
                        self.is_in_sync = None

                        self.srgv_mac = PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self._children_name_map["srgv_mac"] = "srgv-mac"
                        self._segment_path = lambda: "parent-interface-id" + "[parent-interface-name='" + str(self.parent_interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId, ['parent_interface_name', 'interface', 'is_in_sync'], name, value)


                    class SrgvMac(_Entity_):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, self).__init__()

                            self.yang_name = "srgv-mac"
                            self.yang_parent_name = "parent-interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "srgv-mac"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId.SrgvMac']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                        return meta._meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds.ParentInterfaceId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                    return meta._meta_table['PppoeEa.Nodes.Node.ParentInterfaceIds']['meta_info']


            class InterfaceIds(_Entity_):
                """
                PPPoE interface info
                
                .. attribute:: interface_id
                
                	PPPoE interface info
                	**type**\: list of  		 :py:class:`InterfaceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId>`
                
                	**config**\: False
                
                

                """

                _prefix = 'pppoe-ea-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(PppoeEa.Nodes.Node.InterfaceIds, self).__init__()

                    self.yang_name = "interface-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-id", ("interface_id", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId))])
                    self._leafs = OrderedDict()

                    self.interface_id = YList(self)
                    self._segment_path = lambda: "interface-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds, [], name, value)


                class InterfaceId(_Entity_):
                    """
                    PPPoE interface info
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: peer_mac
                    
                    	Peer Mac\-address
                    	**type**\:  :py:class:`PeerMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac>`
                    
                    	**config**\: False
                    
                    .. attribute:: local_mac
                    
                    	Local Mac\-address
                    	**type**\:  :py:class:`LocalMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac>`
                    
                    	**config**\: False
                    
                    .. attribute:: srgv_mac
                    
                    	SRG VMac\-address
                    	**type**\:  :py:class:`SrgvMac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_pppoe_ea_oper.PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac>`
                    
                    	**config**\: False
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: parent_interface
                    
                    	Parent Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    .. attribute:: is_priority_set
                    
                    	Is Priority Set
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    	**config**\: False
                    
                    .. attribute:: is_in_sync
                    
                    	Is in sync
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: is_platform_created
                    
                    	Is Platform created
                    	**type**\: bool
                    
                    	**config**\: False
                    
                    .. attribute:: vlanid
                    
                    	VLAN Ids
                    	**type**\: list of int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'pppoe-ea-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, self).__init__()

                        self.yang_name = "interface-id"
                        self.yang_parent_name = "interface-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("peer-mac", ("peer_mac", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac)), ("local-mac", ("local_mac", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac)), ("srgv-mac", ("srgv_mac", PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('session_id', (YLeaf(YType.uint16, 'session-id'), ['int'])),
                            ('parent_interface', (YLeaf(YType.str, 'parent-interface'), ['str'])),
                            ('is_priority_set', (YLeaf(YType.boolean, 'is-priority-set'), ['bool'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                            ('is_in_sync', (YLeaf(YType.boolean, 'is-in-sync'), ['bool'])),
                            ('is_platform_created', (YLeaf(YType.boolean, 'is-platform-created'), ['bool'])),
                            ('vlanid', (YLeafList(YType.uint16, 'vlanid'), ['int'])),
                        ])
                        self.interface_name = None
                        self.interface = None
                        self.session_id = None
                        self.parent_interface = None
                        self.is_priority_set = None
                        self.priority = None
                        self.is_in_sync = None
                        self.is_platform_created = None
                        self.vlanid = []

                        self.peer_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac()
                        self.peer_mac.parent = self
                        self._children_name_map["peer_mac"] = "peer-mac"

                        self.local_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac()
                        self.local_mac.parent = self
                        self._children_name_map["local_mac"] = "local-mac"

                        self.srgv_mac = PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac()
                        self.srgv_mac.parent = self
                        self._children_name_map["srgv_mac"] = "srgv-mac"
                        self._segment_path = lambda: "interface-id" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId, ['interface_name', 'interface', 'session_id', 'parent_interface', 'is_priority_set', 'priority', 'is_in_sync', 'is_platform_created', 'vlanid'], name, value)


                    class PeerMac(_Entity_):
                        """
                        Peer Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, self).__init__()

                            self.yang_name = "peer-mac"
                            self.yang_parent_name = "interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "peer-mac"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.PeerMac']['meta_info']


                    class LocalMac(_Entity_):
                        """
                        Local Mac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, self).__init__()

                            self.yang_name = "local-mac"
                            self.yang_parent_name = "interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "local-mac"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.LocalMac']['meta_info']


                    class SrgvMac(_Entity_):
                        """
                        SRG VMac\-address
                        
                        .. attribute:: macaddr
                        
                        	macaddr
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'pppoe-ea-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, self).__init__()

                            self.yang_name = "srgv-mac"
                            self.yang_parent_name = "interface-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('macaddr', (YLeaf(YType.str, 'macaddr'), ['str'])),
                            ])
                            self.macaddr = None
                            self._segment_path = lambda: "srgv-mac"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac, ['macaddr'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                            return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId.SrgvMac']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                        return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds.InterfaceId']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                    return meta._meta_table['PppoeEa.Nodes.Node.InterfaceIds']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
                return meta._meta_table['PppoeEa.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
            return meta._meta_table['PppoeEa.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = PppoeEa()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_pppoe_ea_oper as meta
        return meta._meta_table['PppoeEa']['meta_info']


