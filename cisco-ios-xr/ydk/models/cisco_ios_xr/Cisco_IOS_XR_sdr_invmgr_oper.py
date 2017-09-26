""" Cisco_IOS_XR_sdr_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  sdr\-inventory\: SDR information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class SdrInventory(Entity):
    """
    SDR information
    
    .. attribute:: racks
    
    	RackTable
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks>`
    
    

    """

    _prefix = 'sdr-invmgr-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SdrInventory, self).__init__()
        self._top_entity = None

        self.yang_name = "sdr-inventory"
        self.yang_parent_name = "Cisco-IOS-XR-sdr-invmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"racks" : ("racks", SdrInventory.Racks)}
        self._child_list_classes = {}

        self.racks = SdrInventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory"


    class Racks(Entity):
        """
        RackTable
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack>`
        
        

        """

        _prefix = 'sdr-invmgr-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SdrInventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "sdr-inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rack" : ("rack", SdrInventory.Racks.Rack)}

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SdrInventory.Racks, [], name, value)


        class Rack(Entity):
            """
            Rack name
            
            .. attribute:: name  <key>
            
            	Rack name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: slot
            
            	Slot name
            	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot>`
            
            

            """

            _prefix = 'sdr-invmgr-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SdrInventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"slot" : ("slot", SdrInventory.Racks.Rack.Slot)}

                self.name = YLeaf(YType.str, "name")

                self.slot = YList(self)
                self._segment_path = lambda: "rack" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-oper:sdr-inventory/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SdrInventory.Racks.Rack, ['name'], name, value)


            class Slot(Entity):
                """
                Slot name
                
                .. attribute:: name  <key>
                
                	Slot name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: card
                
                	Card
                	**type**\: list of    :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card>`
                
                

                """

                _prefix = 'sdr-invmgr-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SdrInventory.Racks.Rack.Slot, self).__init__()

                    self.yang_name = "slot"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"card" : ("card", SdrInventory.Racks.Rack.Slot.Card)}

                    self.name = YLeaf(YType.str, "name")

                    self.card = YList(self)
                    self._segment_path = lambda: "slot" + "[name='" + self.name.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(SdrInventory.Racks.Rack.Slot, ['name'], name, value)


                class Card(Entity):
                    """
                    Card
                    
                    .. attribute:: name  <key>
                    
                    	Card
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: attributes
                    
                    	Attributes
                    	**type**\:   :py:class:`Attributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_oper.SdrInventory.Racks.Rack.Slot.Card.Attributes>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SdrInventory.Racks.Rack.Slot.Card, self).__init__()

                        self.yang_name = "card"
                        self.yang_parent_name = "slot"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"attributes" : ("attributes", SdrInventory.Racks.Rack.Slot.Card.Attributes)}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.attributes = SdrInventory.Racks.Rack.Slot.Card.Attributes()
                        self.attributes.parent = self
                        self._children_name_map["attributes"] = "attributes"
                        self._children_yang_names.add("attributes")
                        self._segment_path = lambda: "card" + "[name='" + self.name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SdrInventory.Racks.Rack.Slot.Card, ['name'], name, value)


                    class Attributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: card_admin_state
                        
                        	Card Admin State
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state
                        
                        	CardState
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_state_string
                        
                        	Card State String
                        	**type**\:  str
                        
                        .. attribute:: card_type
                        
                        	CardType
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: card_type_string
                        
                        	Card Type String
                        	**type**\:  str
                        
                        .. attribute:: config_state
                        
                        	ConfigState
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: config_state_string
                        
                        	Config State String
                        	**type**\:  str
                        
                        .. attribute:: ctype
                        
                        	CType
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: monitor
                        
                        	Monitor
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: node_name_string
                        
                        	Node Name String
                        	**type**\:  str
                        
                        .. attribute:: pi_slot_number
                        
                        	Pi Slot Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: power
                        
                        	Power
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: shutdown
                        
                        	Shutdown
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: vm_state
                        
                        	VM State information
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'sdr-invmgr-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SdrInventory.Racks.Rack.Slot.Card.Attributes, self).__init__()

                            self.yang_name = "attributes"
                            self.yang_parent_name = "card"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.card_admin_state = YLeaf(YType.uint32, "card-admin-state")

                            self.card_state = YLeaf(YType.uint32, "card-state")

                            self.card_state_string = YLeaf(YType.str, "card-state-string")

                            self.card_type = YLeaf(YType.uint32, "card-type")

                            self.card_type_string = YLeaf(YType.str, "card-type-string")

                            self.config_state = YLeaf(YType.uint32, "config-state")

                            self.config_state_string = YLeaf(YType.str, "config-state-string")

                            self.ctype = YLeaf(YType.uint32, "ctype")

                            self.monitor = YLeaf(YType.uint32, "monitor")

                            self.node_name_string = YLeaf(YType.str, "node-name-string")

                            self.pi_slot_number = YLeaf(YType.uint32, "pi-slot-number")

                            self.power = YLeaf(YType.uint32, "power")

                            self.shutdown = YLeaf(YType.uint32, "shutdown")

                            self.vm_state = YLeaf(YType.uint32, "vm-state")
                            self._segment_path = lambda: "attributes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SdrInventory.Racks.Rack.Slot.Card.Attributes, ['card_admin_state', 'card_state', 'card_state_string', 'card_type', 'card_type_string', 'config_state', 'config_state_string', 'ctype', 'monitor', 'node_name_string', 'pi_slot_number', 'power', 'shutdown', 'vm_state'], name, value)

    def clone_ptr(self):
        self._top_entity = SdrInventory()
        return self._top_entity

