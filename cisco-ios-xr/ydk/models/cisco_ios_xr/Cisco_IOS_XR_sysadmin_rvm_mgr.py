""" Cisco_IOS_XR_sysadmin_rvm_mgr 

This module contains a collection of YANG
definitions for Cisco IOS\-XR SysAdmin configuration.

Copyright(c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FlagtypeTd(Enum):
    """
    FlagtypeTd (Enum Class)

    .. data:: clear = 0

    .. data:: set = 1

    """

    clear = Enum.YLeaf(0, "clear")

    set = Enum.YLeaf(1, "set")


class NodetypeTd(Enum):
    """
    NodetypeTd (Enum Class)

    .. data:: sysadmin = 1

    .. data:: service = 2

    """

    sysadmin = Enum.YLeaf(1, "sysadmin")

    service = Enum.YLeaf(2, "service")



class RVM(Entity):
    """
    RVM Manager Info
    
    .. attribute:: all_locations
    
    	
    	**type**\: list of  		 :py:class:`AllLocations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations>`
    
    

    """

    _prefix = 'rvmmh'
    _revision = '2017-04-12'

    def __init__(self):
        super(RVM, self).__init__()
        self._top_entity = None

        self.yang_name = "RVM"
        self.yang_parent_name = "Cisco-IOS-XR-sysadmin-rvm-mgr"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all-locations", ("all_locations", RVM.AllLocations))])
        self._leafs = OrderedDict()

        self.all_locations = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-sysadmin-rvm-mgr:RVM"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RVM, [], name, value)


    class AllLocations(Entity):
        """
        
        
        .. attribute:: location  (key)
        
        	
        	**type**\: str
        
        .. attribute:: objects
        
        	RVM Manager Info
        	**type**\:  :py:class:`Objects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations.Objects>`
        
        .. attribute:: node
        
        	RVM Manager Node Info
        	**type**\:  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations.Node>`
        
        .. attribute:: card
        
        	RVM Manager Card Info
        	**type**\:  :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations.Card>`
        
        

        """

        _prefix = 'rvmmh'
        _revision = '2017-04-12'

        def __init__(self):
            super(RVM.AllLocations, self).__init__()

            self.yang_name = "all-locations"
            self.yang_parent_name = "RVM"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['location']
            self._child_classes = OrderedDict([("objects", ("objects", RVM.AllLocations.Objects)), ("node", ("node", RVM.AllLocations.Node)), ("card", ("card", RVM.AllLocations.Card))])
            self._leafs = OrderedDict([
                ('location', (YLeaf(YType.str, 'location'), ['str'])),
            ])
            self.location = None

            self.objects = RVM.AllLocations.Objects()
            self.objects.parent = self
            self._children_name_map["objects"] = "objects"

            self.node = RVM.AllLocations.Node()
            self.node.parent = self
            self._children_name_map["node"] = "node"

            self.card = RVM.AllLocations.Card()
            self.card.parent = self
            self._children_name_map["card"] = "card"
            self._segment_path = lambda: "all-locations" + "[location='" + str(self.location) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-sysadmin-rvm-mgr:RVM/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RVM.AllLocations, ['location'], name, value)


        class Objects(Entity):
            """
            RVM Manager Info
            
            .. attribute:: all_objs
            
            	
            	**type**\: list of  		 :py:class:`AllObjs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations.Objects.AllObjs>`
            
            

            """

            _prefix = 'rvmmh'
            _revision = '2017-04-12'

            def __init__(self):
                super(RVM.AllLocations.Objects, self).__init__()

                self.yang_name = "objects"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("all-objs", ("all_objs", RVM.AllLocations.Objects.AllObjs))])
                self._leafs = OrderedDict()

                self.all_objs = YList(self)
                self._segment_path = lambda: "objects"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RVM.AllLocations.Objects, [], name, value)


            class AllObjs(Entity):
                """
                
                
                .. attribute:: index  (key)
                
                	Index into obj\_db array
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_allocated
                
                	Number of allocated nodes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_freed
                
                	Number of freed nodes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: num_objects
                
                	Number of current object nodes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'rvmmh'
                _revision = '2017-04-12'

                def __init__(self):
                    super(RVM.AllLocations.Objects.AllObjs, self).__init__()

                    self.yang_name = "all-objs"
                    self.yang_parent_name = "objects"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['index']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ('num_allocated', (YLeaf(YType.uint32, 'num_allocated'), ['int'])),
                        ('num_freed', (YLeaf(YType.uint32, 'num_freed'), ['int'])),
                        ('num_objects', (YLeaf(YType.uint32, 'num_objects'), ['int'])),
                    ])
                    self.index = None
                    self.num_allocated = None
                    self.num_freed = None
                    self.num_objects = None
                    self._segment_path = lambda: "all-objs" + "[index='" + str(self.index) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RVM.AllLocations.Objects.AllObjs, ['index', 'num_allocated', 'num_freed', 'num_objects'], name, value)


        class Node(Entity):
            """
            RVM Manager Node Info
            
            .. attribute:: all_nodes
            
            	
            	**type**\: list of  		 :py:class:`AllNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations.Node.AllNodes>`
            
            

            """

            _prefix = 'rvmmh'
            _revision = '2017-04-12'

            def __init__(self):
                super(RVM.AllLocations.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("all-nodes", ("all_nodes", RVM.AllLocations.Node.AllNodes))])
                self._leafs = OrderedDict()

                self.all_nodes = YList(self)
                self._segment_path = lambda: "node"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RVM.AllLocations.Node, [], name, value)


            class AllNodes(Entity):
                """
                
                
                .. attribute:: ipv4_addr  (key)
                
                	IP address of the node
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ipv4_addr_str
                
                	IP address of the node in string format
                	**type**\: str
                
                .. attribute:: node_info
                
                	Node type state and flag
                	**type**\: str
                
                .. attribute:: node_hb_info
                
                	Node heartbeat related info
                	**type**\: str
                
                .. attribute:: node_card_info
                
                	Card info the node belongs to
                	**type**\: str
                
                

                """

                _prefix = 'rvmmh'
                _revision = '2017-04-12'

                def __init__(self):
                    super(RVM.AllLocations.Node.AllNodes, self).__init__()

                    self.yang_name = "all-nodes"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['ipv4_addr']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ipv4_addr', (YLeaf(YType.uint32, 'ipv4_addr'), ['int'])),
                        ('ipv4_addr_str', (YLeaf(YType.str, 'ipv4_addr_str'), ['str'])),
                        ('node_info', (YLeaf(YType.str, 'node_info'), ['str'])),
                        ('node_hb_info', (YLeaf(YType.str, 'node_hb_info'), ['str'])),
                        ('node_card_info', (YLeaf(YType.str, 'node_card_info'), ['str'])),
                    ])
                    self.ipv4_addr = None
                    self.ipv4_addr_str = None
                    self.node_info = None
                    self.node_hb_info = None
                    self.node_card_info = None
                    self._segment_path = lambda: "all-nodes" + "[ipv4_addr='" + str(self.ipv4_addr) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RVM.AllLocations.Node.AllNodes, ['ipv4_addr', 'ipv4_addr_str', 'node_info', 'node_hb_info', 'node_card_info'], name, value)


        class Card(Entity):
            """
            RVM Manager Card Info
            
            .. attribute:: all_cards
            
            	
            	**type**\: list of  		 :py:class:`AllCards <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sysadmin_rvm_mgr.RVM.AllLocations.Card.AllCards>`
            
            

            """

            _prefix = 'rvmmh'
            _revision = '2017-04-12'

            def __init__(self):
                super(RVM.AllLocations.Card, self).__init__()

                self.yang_name = "card"
                self.yang_parent_name = "all-locations"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("all-cards", ("all_cards", RVM.AllLocations.Card.AllCards))])
                self._leafs = OrderedDict()

                self.all_cards = YList(self)
                self._segment_path = lambda: "card"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RVM.AllLocations.Card, [], name, value)


            class AllCards(Entity):
                """
                
                
                .. attribute:: serial_num  (key)
                
                	Serial number of the card
                	**type**\: str
                
                .. attribute:: card_flag
                
                	Card flags
                	**type**\: str
                
                .. attribute:: card_info
                
                	Card rack and slot num
                	**type**\: str
                
                .. attribute:: sysadmin_nodes
                
                	Sysadmin nodes on this card
                	**type**\: str
                
                .. attribute:: xr_nodes
                
                	XR nodes on this card
                	**type**\: str
                
                

                """

                _prefix = 'rvmmh'
                _revision = '2017-04-12'

                def __init__(self):
                    super(RVM.AllLocations.Card.AllCards, self).__init__()

                    self.yang_name = "all-cards"
                    self.yang_parent_name = "card"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['serial_num']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('serial_num', (YLeaf(YType.str, 'serial_num'), ['str'])),
                        ('card_flag', (YLeaf(YType.str, 'card_flag'), ['str'])),
                        ('card_info', (YLeaf(YType.str, 'card_info'), ['str'])),
                        ('sysadmin_nodes', (YLeaf(YType.str, 'sysadmin_nodes'), ['str'])),
                        ('xr_nodes', (YLeaf(YType.str, 'xr_nodes'), ['str'])),
                    ])
                    self.serial_num = None
                    self.card_flag = None
                    self.card_info = None
                    self.sysadmin_nodes = None
                    self.xr_nodes = None
                    self._segment_path = lambda: "all-cards" + "[serial_num='" + str(self.serial_num) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RVM.AllLocations.Card.AllCards, ['serial_num', 'card_flag', 'card_info', 'sysadmin_nodes', 'xr_nodes'], name, value)

    def clone_ptr(self):
        self._top_entity = RVM()
        return self._top_entity

