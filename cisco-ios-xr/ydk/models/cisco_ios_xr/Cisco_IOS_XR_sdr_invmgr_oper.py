""" Cisco_IOS_XR_sdr_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\: SDR information

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




class SdrInventory(_Entity_):
    """
    SDR information
    
    .. attribute:: racks
    
    	RackTable
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks>`
    
    	**config**\: False
    
    .. attribute:: memory
    
    	Memory
    	**type**\:  :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Memory>`
    
    	**config**\: False
    
    

    """

    _prefix = 'sdr-invmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(SdrInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sdr-invmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("racks", ("racks", SdrInventory.Racks)), ("memory", ("memory", SdrInventory.Memory))])
        self._leafs = OrderedDict()

        self.racks = SdrInventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"

        self.memory = SdrInventory.Memory()
        self.memory.parent = self
        self._children_name_map["memory"] = "memory"
        self._segment_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SdrInventory, [], name, value)


    class Racks(_Entity_):
        """
        RackTable
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack>`
        
        	**config**\: False
        
        

        """

        _prefix = 'sdr-invmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SdrInventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "sdr-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", SdrInventory.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrInventory.Racks, [], name, value)


        class Rack(_Entity_):
            """
            Rack name
            
            .. attribute:: name  (key)
            
            	Rack name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: slot
            
            	Slot name
            	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot>`
            
            	**config**\: False
            
            

            """

            _prefix = 'sdr-invmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SdrInventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("slot", ("slot", SdrInventory.Racks.Rack.Slot))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.slot = YList(self)
                self._segment_path = lambda: "rack" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrInventory.Racks.Rack, ['name'], name, value)


            class Slot(_Entity_):
                """
                Slot name
                
                .. attribute:: name  (key)
                
                	Slot name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: card
                
                	Card
                	**type**\: list of  		 :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sdr-invmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SdrInventory.Racks.Rack.Slot, self).__init__()

                    self.yang_name = "slot"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("card", ("card", SdrInventory.Racks.Rack.Slot.Card))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.card = YList(self)
                    self._segment_path = lambda: "slot" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrInventory.Racks.Rack.Slot, ['name'], name, value)


                class Card(_Entity_):
                    """
                    Card
                    
                    .. attribute:: name  (key)
                    
                    	Card
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: attributes
                    
                    	Attributes
                    	**type**\:  :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card.Attributes>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sdr-invmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SdrInventory.Racks.Rack.Slot.Card, self).__init__()

                        self.yang_name = "card"
                        self.yang_parent_name = "slot"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("attributes", ("attributes", SdrInventory.Racks.Rack.Slot.Card.Attributes))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None

                        self.attributes = SdrInventory.Racks.Rack.Slot.Card.Attributes()
                        self.attributes.parent = self
                        self._children_name_map["attributes"] = "attributes"
                        self._segment_path = lambda: "card" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrInventory.Racks.Rack.Slot.Card, ['name'], name, value)


                    class Attributes(_Entity_):
                        """
                        Attributes
                        
                        .. attribute:: config_state_string
                        
                        	Config State String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: power
                        
                        	Power
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: config_state
                        
                        	ConfigState
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state
                        
                        	CardState
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: vm_state
                        
                        	VM State information
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_admin_state
                        
                        	Card Admin State
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_type
                        
                        	CardType
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_type_string
                        
                        	Card Type String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: node_name_string
                        
                        	Node Name String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: card_valid
                        
                        	Card Valid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: pi_slot_number
                        
                        	Pi Slot Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: shutdown
                        
                        	Shutdown
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: ctype
                        
                        	CType
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state_string
                        
                        	Card State String
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: monitor
                        
                        	Monitor
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'sdr-invmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SdrInventory.Racks.Rack.Slot.Card.Attributes, self).__init__()

                            self.yang_name = "attributes"
                            self.yang_parent_name = "card"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('config_state_string', (YLeaf(YType.str, 'config-state-string'), ['str'])),
                                ('power', (YLeaf(YType.uint32, 'power'), ['int'])),
                                ('config_state', (YLeaf(YType.uint32, 'config-state'), ['int'])),
                                ('card_state', (YLeaf(YType.uint32, 'card-state'), ['int'])),
                                ('vm_state', (YLeaf(YType.uint32, 'vm-state'), ['int'])),
                                ('card_admin_state', (YLeaf(YType.uint32, 'card-admin-state'), ['int'])),
                                ('card_type', (YLeaf(YType.uint32, 'card-type'), ['int'])),
                                ('card_type_string', (YLeaf(YType.str, 'card-type-string'), ['str'])),
                                ('node_name_string', (YLeaf(YType.str, 'node-name-string'), ['str'])),
                                ('card_valid', (YLeaf(YType.uint32, 'card-valid'), ['int'])),
                                ('pi_slot_number', (YLeaf(YType.uint32, 'pi-slot-number'), ['int'])),
                                ('shutdown', (YLeaf(YType.uint32, 'shutdown'), ['int'])),
                                ('ctype', (YLeaf(YType.uint32, 'ctype'), ['int'])),
                                ('card_state_string', (YLeaf(YType.str, 'card-state-string'), ['str'])),
                                ('monitor', (YLeaf(YType.uint32, 'monitor'), ['int'])),
                            ])
                            self.config_state_string = None
                            self.power = None
                            self.config_state = None
                            self.card_state = None
                            self.vm_state = None
                            self.card_admin_state = None
                            self.card_type = None
                            self.card_type_string = None
                            self.node_name_string = None
                            self.card_valid = None
                            self.pi_slot_number = None
                            self.shutdown = None
                            self.ctype = None
                            self.card_state_string = None
                            self.monitor = None
                            self._segment_path = lambda: "attributes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SdrInventory.Racks.Rack.Slot.Card.Attributes, ['config_state_string', 'power', 'config_state', 'card_state', 'vm_state', 'card_admin_state', 'card_type', 'card_type_string', 'node_name_string', 'card_valid', 'pi_slot_number', 'shutdown', 'ctype', 'card_state_string', 'monitor'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                            return meta._meta_table['SdrInventory.Racks.Rack.Slot.Card.Attributes']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                        return meta._meta_table['SdrInventory.Racks.Rack.Slot.Card']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                    return meta._meta_table['SdrInventory.Racks.Rack.Slot']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                return meta._meta_table['SdrInventory.Racks.Rack']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
            return meta._meta_table['SdrInventory.Racks']['meta_info']


    class Memory(_Entity_):
        """
        Memory
        
        .. attribute:: racks
        
        	RackTable
        	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Memory.Racks>`
        
        	**config**\: False
        
        

        """

        _prefix = 'sdr-invmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(SdrInventory.Memory, self).__init__()

            self.yang_name = "memory"
            self.yang_parent_name = "sdr-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("racks", ("racks", SdrInventory.Memory.Racks))])
            self._leafs = OrderedDict()

            self.racks = SdrInventory.Memory.Racks()
            self.racks.parent = self
            self._children_name_map["racks"] = "racks"
            self._segment_path = lambda: "memory"
            self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SdrInventory.Memory, [], name, value)


        class Racks(_Entity_):
            """
            RackTable
            
            .. attribute:: rack
            
            	Rack name
            	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Memory.Racks.Rack>`
            
            	**config**\: False
            
            

            """

            _prefix = 'sdr-invmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(SdrInventory.Memory.Racks, self).__init__()

                self.yang_name = "racks"
                self.yang_parent_name = "memory"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rack", ("rack", SdrInventory.Memory.Racks.Rack))])
                self._leafs = OrderedDict()

                self.rack = YList(self)
                self._segment_path = lambda: "racks"
                self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/memory/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SdrInventory.Memory.Racks, [], name, value)


            class Rack(_Entity_):
                """
                Rack name
                
                .. attribute:: name  (key)
                
                	Rack name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                	**config**\: False
                
                .. attribute:: node_ids
                
                	NodeIDTable
                	**type**\:  :py:class:`NodeIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Memory.Racks.Rack.NodeIds>`
                
                	**config**\: False
                
                

                """

                _prefix = 'sdr-invmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(SdrInventory.Memory.Racks.Rack, self).__init__()

                    self.yang_name = "rack"
                    self.yang_parent_name = "racks"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("node-ids", ("node_ids", SdrInventory.Memory.Racks.Rack.NodeIds))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None

                    self.node_ids = SdrInventory.Memory.Racks.Rack.NodeIds()
                    self.node_ids.parent = self
                    self._children_name_map["node_ids"] = "node-ids"
                    self._segment_path = lambda: "rack" + "[name='" + str(self.name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/memory/racks/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrInventory.Memory.Racks.Rack, ['name'], name, value)


                class NodeIds(_Entity_):
                    """
                    NodeIDTable
                    
                    .. attribute:: node_id
                    
                    	Inventory Admin Mempool Data  Bag
                    	**type**\: list of  		 :py:class:`NodeId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Memory.Racks.Rack.NodeIds.NodeId>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'sdr-invmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(SdrInventory.Memory.Racks.Rack.NodeIds, self).__init__()

                        self.yang_name = "node-ids"
                        self.yang_parent_name = "rack"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node-id", ("node_id", SdrInventory.Memory.Racks.Rack.NodeIds.NodeId))])
                        self._leafs = OrderedDict()

                        self.node_id = YList(self)
                        self._segment_path = lambda: "node-ids"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrInventory.Memory.Racks.Rack.NodeIds, [], name, value)


                    class NodeId(_Entity_):
                        """
                        Inventory Admin Mempool Data  Bag
                        
                        .. attribute:: name  (key)
                        
                        	nodeid
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        	**config**\: False
                        
                        .. attribute:: total_memory
                        
                        	Total Memory
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: available_memory
                        
                        	Avaialble Memory
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'sdr-invmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(SdrInventory.Memory.Racks.Rack.NodeIds.NodeId, self).__init__()

                            self.yang_name = "node-id"
                            self.yang_parent_name = "node-ids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('total_memory', (YLeaf(YType.uint32, 'total-memory'), ['int'])),
                                ('available_memory', (YLeaf(YType.uint32, 'available-memory'), ['int'])),
                            ])
                            self.name = None
                            self.total_memory = None
                            self.available_memory = None
                            self._segment_path = lambda: "node-id" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SdrInventory.Memory.Racks.Rack.NodeIds.NodeId, ['name', 'total_memory', 'available_memory'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                            return meta._meta_table['SdrInventory.Memory.Racks.Rack.NodeIds.NodeId']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                        return meta._meta_table['SdrInventory.Memory.Racks.Rack.NodeIds']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                    return meta._meta_table['SdrInventory.Memory.Racks.Rack']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
                return meta._meta_table['SdrInventory.Memory.Racks']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
            return meta._meta_table['SdrInventory.Memory']['meta_info']

    def clone_ptr(self):
        self._top_entity = SdrInventory()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_oper as meta
        return meta._meta_table['SdrInventory']['meta_info']


