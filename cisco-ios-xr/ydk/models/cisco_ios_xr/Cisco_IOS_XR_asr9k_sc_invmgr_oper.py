""" Cisco_IOS_XR_asr9k_sc_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  inventory\: Logical Router Inventory operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CardResetReason(Enum):
    """
    CardResetReason (Enum Class)

    Card reset reason

    .. data:: reset_unknown = 1

    	reset unknown

    .. data:: power_up = 2

    	power up

    .. data:: parity_error = 3

    	parity error

    .. data:: clear_config_reset = 4

    	clear config reset

    .. data:: manual_reset = 5

    	manual reset

    .. data:: watch_dog_timeout_reset = 6

    	watch dog timeout reset

    .. data:: resource_overflow_reset = 7

    	resource overflow reset

    .. data:: missing_task_reset = 8

    	missing task reset

    .. data:: low_voltage_reset = 9

    	low voltage reset

    .. data:: controller_reset = 10

    	controller reset

    .. data:: system_reset = 11

    	system reset

    .. data:: switchover_reset = 12

    	switchover reset

    .. data:: upgrade_reset = 13

    	upgrade reset

    .. data:: downgrade_reset = 14

    	downgrade reset

    .. data:: cache_error_reset = 15

    	cache error reset

    .. data:: device_driver_reset = 16

    	device driver reset

    .. data:: software_exception_reset = 17

    	software exception reset

    .. data:: restore_config_reset = 18

    	restore config reset

    .. data:: abort_rev_reset = 19

    	abort rev reset

    .. data:: burn_boot_reset = 20

    	burn boot reset

    .. data:: standby_cd_healthier_reset = 21

    	standby cd healthier reset

    .. data:: non_native_config_clear_reset = 22

    	non native config clear reset

    .. data:: memory_protection_error_reset = 23

    	memory protection error reset

    .. data:: card_reset_reason_max = 24

    	card reset reason max

    """

    reset_unknown = Enum.YLeaf(1, "reset-unknown")

    power_up = Enum.YLeaf(2, "power-up")

    parity_error = Enum.YLeaf(3, "parity-error")

    clear_config_reset = Enum.YLeaf(4, "clear-config-reset")

    manual_reset = Enum.YLeaf(5, "manual-reset")

    watch_dog_timeout_reset = Enum.YLeaf(6, "watch-dog-timeout-reset")

    resource_overflow_reset = Enum.YLeaf(7, "resource-overflow-reset")

    missing_task_reset = Enum.YLeaf(8, "missing-task-reset")

    low_voltage_reset = Enum.YLeaf(9, "low-voltage-reset")

    controller_reset = Enum.YLeaf(10, "controller-reset")

    system_reset = Enum.YLeaf(11, "system-reset")

    switchover_reset = Enum.YLeaf(12, "switchover-reset")

    upgrade_reset = Enum.YLeaf(13, "upgrade-reset")

    downgrade_reset = Enum.YLeaf(14, "downgrade-reset")

    cache_error_reset = Enum.YLeaf(15, "cache-error-reset")

    device_driver_reset = Enum.YLeaf(16, "device-driver-reset")

    software_exception_reset = Enum.YLeaf(17, "software-exception-reset")

    restore_config_reset = Enum.YLeaf(18, "restore-config-reset")

    abort_rev_reset = Enum.YLeaf(19, "abort-rev-reset")

    burn_boot_reset = Enum.YLeaf(20, "burn-boot-reset")

    standby_cd_healthier_reset = Enum.YLeaf(21, "standby-cd-healthier-reset")

    non_native_config_clear_reset = Enum.YLeaf(22, "non-native-config-clear-reset")

    memory_protection_error_reset = Enum.YLeaf(23, "memory-protection-error-reset")

    card_reset_reason_max = Enum.YLeaf(24, "card-reset-reason-max")



class Inventory(Entity):
    """
    Logical Router Inventory operational data
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-invmgr-oper'
    _revision = '2017-01-04'

    def __init__(self):
        super(Inventory, self).__init__()
        self._top_entity = None

        self.yang_name = "inventory"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-invmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("racks", ("racks", Inventory.Racks))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.racks = Inventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-oper:inventory"


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack number
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-invmgr-oper'
        _revision = '2017-01-04'

        def __init__(self):
            super(Inventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rack", ("rack", Inventory.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-oper:inventory/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Racks, [], name, value)


        class Rack(Entity):
            """
            Rack number
            
            .. attribute:: number  (key)
            
            	Rack number
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: slots
            
            	Slot table contains all slots in the rack
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'asr9k-sc-invmgr-oper'
            _revision = '2017-01-04'

            def __init__(self):
                super(Inventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['number']
                self._child_container_classes = OrderedDict([("slots", ("slots", Inventory.Racks.Rack.Slots))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('number', YLeaf(YType.int32, 'number')),
                ])
                self.number = None

                self.slots = Inventory.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")
                self._segment_path = lambda: "rack" + "[number='" + str(self.number) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-oper:inventory/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Inventory.Racks.Rack, ['number'], name, value)


            class Slots(Entity):
                """
                Slot table contains all slots in the rack
                
                .. attribute:: slot
                
                	Slot number
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    super(Inventory.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("slot", ("slot", Inventory.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"

                def __setattr__(self, name, value):
                    self._perform_setattr(Inventory.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Slot number
                    
                    .. attribute:: number  (key)
                    
                    	Slot number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: cards
                    
                    	Card table contains all cards in the slot
                    	**type**\:  :py:class:`Cards <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards>`
                    
                    .. attribute:: basic_attributes
                    
                    	Attributes
                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-oper'
                    _revision = '2017-01-04'

                    def __init__(self):
                        super(Inventory.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_container_classes = OrderedDict([("cards", ("cards", Inventory.Racks.Rack.Slots.Slot.Cards)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.BasicAttributes))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('number', YLeaf(YType.int32, 'number')),
                        ])
                        self.number = None

                        self.cards = Inventory.Racks.Rack.Slots.Slot.Cards()
                        self.cards.parent = self
                        self._children_name_map["cards"] = "cards"
                        self._children_yang_names.add("cards")

                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.BasicAttributes()
                        self.basic_attributes.parent = self
                        self._children_name_map["basic_attributes"] = "basic-attributes"
                        self._children_yang_names.add("basic-attributes")
                        self._segment_path = lambda: "slot" + "[number='" + str(self.number) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot, ['number'], name, value)


                    class Cards(Entity):
                        """
                        Card table contains all cards in the slot
                        
                        .. attribute:: card
                        
                        	Card number
                        	**type**\: list of  		 :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            super(Inventory.Racks.Rack.Slots.Slot.Cards, self).__init__()

                            self.yang_name = "cards"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("card", ("card", Inventory.Racks.Rack.Slots.Slot.Cards.Card))])
                            self._leafs = OrderedDict()

                            self.card = YList(self)
                            self._segment_path = lambda: "cards"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards, [], name, value)


                        class Card(Entity):
                            """
                            Card number
                            
                            .. attribute:: number  (key)
                            
                            	card number
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: sub_slots
                            
                            	SubSlotTable contains all subslots in a Slot
                            	**type**\:  :py:class:`SubSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots>`
                            
                            .. attribute:: hw_components
                            
                            	HWComponent table contains all HW modules within the card 
                            	**type**\:  :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents>`
                            
                            .. attribute:: sensors
                            
                            	ModuleSensorTable contains all sensors in a Module
                            	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors>`
                            
                            .. attribute:: port_slots
                            
                            	PortSlotTable contains all optics ports in a SPA/PLIM
                            	**type**\:  :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots>`
                            
                            .. attribute:: basic_attributes
                            
                            	Attributes
                            	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card, self).__init__()

                                self.yang_name = "card"
                                self.yang_parent_name = "cards"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['number']
                                self._child_container_classes = OrderedDict([("sub-slots", ("sub_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots)), ("hw-components", ("hw_components", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents)), ("sensors", ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors)), ("port-slots", ("port_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('number', YLeaf(YType.int32, 'number')),
                                ])
                                self.number = None

                                self.sub_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots()
                                self.sub_slots.parent = self
                                self._children_name_map["sub_slots"] = "sub-slots"
                                self._children_yang_names.add("sub-slots")

                                self.hw_components = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents()
                                self.hw_components.parent = self
                                self._children_name_map["hw_components"] = "hw-components"
                                self._children_yang_names.add("hw-components")

                                self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors()
                                self.sensors.parent = self
                                self._children_name_map["sensors"] = "sensors"
                                self._children_yang_names.add("sensors")

                                self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots()
                                self.port_slots.parent = self
                                self._children_name_map["port_slots"] = "port-slots"
                                self._children_yang_names.add("port-slots")

                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes()
                                self.basic_attributes.parent = self
                                self._children_name_map["basic_attributes"] = "basic-attributes"
                                self._children_yang_names.add("basic-attributes")
                                self._segment_path = lambda: "card" + "[number='" + str(self.number) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card, ['number'], name, value)


                            class SubSlots(Entity):
                                """
                                SubSlotTable contains all subslots in a
                                Slot
                                
                                .. attribute:: sub_slot
                                
                                	SubSlot number
                                	**type**\: list of  		 :py:class:`SubSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, self).__init__()

                                    self.yang_name = "sub-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("sub-slot", ("sub_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot))])
                                    self._leafs = OrderedDict()

                                    self.sub_slot = YList(self)
                                    self._segment_path = lambda: "sub-slots"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, [], name, value)


                                class SubSlot(Entity):
                                    """
                                    SubSlot number
                                    
                                    .. attribute:: number  (key)
                                    
                                    	subslot number
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: module
                                    
                                    	Module string
                                    	**type**\:  :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module>`
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, self).__init__()

                                        self.yang_name = "sub-slot"
                                        self.yang_parent_name = "sub-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_container_classes = OrderedDict([("module", ("module", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('number', YLeaf(YType.int32, 'number')),
                                        ])
                                        self.number = None

                                        self.module = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module()
                                        self.module.parent = self
                                        self._children_name_map["module"] = "module"
                                        self._children_yang_names.add("module")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")
                                        self._segment_path = lambda: "sub-slot" + "[number='" + str(self.number) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, ['number'], name, value)


                                    class Module(Entity):
                                        """
                                        Module string
                                        
                                        .. attribute:: sensors
                                        
                                        	ModuleSensorTable contains all sensors in a Module
                                        	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors>`
                                        
                                        .. attribute:: port_slots
                                        
                                        	PortSlotTable contains all optics ports in a SPA/PLIM
                                        	**type**\:  :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots>`
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module, self).__init__()

                                            self.yang_name = "module"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("sensors", ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors)), ("port-slots", ("port_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors()
                                            self.sensors.parent = self
                                            self._children_name_map["sensors"] = "sensors"
                                            self._children_yang_names.add("sensors")

                                            self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots()
                                            self.port_slots.parent = self
                                            self._children_name_map["port_slots"] = "port-slots"
                                            self._children_yang_names.add("port-slots")

                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes()
                                            self.basic_attributes.parent = self
                                            self._children_name_map["basic_attributes"] = "basic-attributes"
                                            self._children_yang_names.add("basic-attributes")
                                            self._segment_path = lambda: "module"


                                        class Sensors(Entity):
                                            """
                                            ModuleSensorTable contains all sensors in a
                                            Module.
                                            
                                            .. attribute:: sensor
                                            
                                            	Sensor number in the Module
                                            	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, self).__init__()

                                                self.yang_name = "sensors"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([("sensor", ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor))])
                                                self._leafs = OrderedDict()

                                                self.sensor = YList(self)
                                                self._segment_path = lambda: "sensors"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, [], name, value)


                                            class Sensor(Entity):
                                                """
                                                Sensor number in the Module
                                                
                                                .. attribute:: number  (key)
                                                
                                                	sensor number
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: basic_attributes
                                                
                                                	Attributes
                                                	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, self).__init__()

                                                    self.yang_name = "sensor"
                                                    self.yang_parent_name = "sensors"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['number']
                                                    self._child_container_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes))])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('number', YLeaf(YType.int32, 'number')),
                                                    ])
                                                    self.number = None

                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self._children_name_map["basic_attributes"] = "basic-attributes"
                                                    self._children_yang_names.add("basic-attributes")
                                                    self._segment_path = lambda: "sensor" + "[number='" + str(self.number) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, ['number'], name, value)


                                                class BasicAttributes(Entity):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Inventory information
                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) inventory information
                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes, self).__init__()

                                                        self.yang_name = "basic-attributes"
                                                        self.yang_parent_name = "sensor"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo))])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict()

                                                        self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self._children_name_map["basic_info"] = "basic-info"
                                                        self._children_yang_names.add("basic-info")

                                                        self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo()
                                                        self.fru_info.parent = self
                                                        self._children_name_map["fru_info"] = "fru-info"
                                                        self._children_yang_names.add("fru-info")
                                                        self._segment_path = lambda: "basic-attributes"


                                                    class BasicInfo(Entity):
                                                        """
                                                        Inventory information
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms       what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: chip_hardware_revision
                                                        
                                                        	chip module hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: manufacturer_name
                                                        
                                                        	manufacturer's name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_id_str
                                                        
                                                        	asset Identification string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_identification
                                                        
                                                        	asset Identification
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: manufacturer_asset_tags
                                                        
                                                        	Manufacture Asset Tags
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: composite_class_code
                                                        
                                                        	Major&minor class of the entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: memory_size
                                                        
                                                        	Size of memory associated with       the entity where applicable
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: environmental_monitor_path
                                                        
                                                        	sysdb name of sensor in the envmon EDM
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: alias
                                                        
                                                        	useful for storing an entity alias 
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: group_flag
                                                        
                                                        	indicates if this entity is group       or not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: new_deviation_number
                                                        
                                                        	integer value for New Deviation Number 0x88
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: physical_layer_interface_module_type
                                                        
                                                        	integer value for plim type if     applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: unrecognized_fru
                                                        
                                                        	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: redundancystate
                                                        
                                                        	integer value for Redundancy State if     applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: ceport
                                                        
                                                        	1 if ce port found, 0 if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: xr_scoped
                                                        
                                                        	1 if xr scoped, 0 if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: unique_id
                                                        
                                                        	Unique id for an entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('description', YLeaf(YType.str, 'description')),
                                                                ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                                ('name', YLeaf(YType.str, 'name')),
                                                                ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                                ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                                ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                                ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                                ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                                ('model_name', YLeaf(YType.str, 'model-name')),
                                                                ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                                ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                                ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                                ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                                ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                                ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                                ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                                ('alias', YLeaf(YType.str, 'alias')),
                                                                ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                                ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                                ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                                ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                                ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                                ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                                ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                                ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                            ])
                                                            self.description = None
                                                            self.vendor_type = None
                                                            self.name = None
                                                            self.hardware_revision = None
                                                            self.firmware_revision = None
                                                            self.software_revision = None
                                                            self.chip_hardware_revision = None
                                                            self.serial_number = None
                                                            self.manufacturer_name = None
                                                            self.model_name = None
                                                            self.asset_id_str = None
                                                            self.asset_identification = None
                                                            self.is_field_replaceable_unit = None
                                                            self.manufacturer_asset_tags = None
                                                            self.composite_class_code = None
                                                            self.memory_size = None
                                                            self.environmental_monitor_path = None
                                                            self.alias = None
                                                            self.group_flag = None
                                                            self.new_deviation_number = None
                                                            self.physical_layer_interface_module_type = None
                                                            self.unrecognized_fru = None
                                                            self.redundancystate = None
                                                            self.ceport = None
                                                            self.xr_scoped = None
                                                            self.unique_id = None
                                                            self._segment_path = lambda: "basic-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                                    class FruInfo(Entity):
                                                        """
                                                        Field Replaceable Unit (FRU) inventory
                                                        information
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	last card oper change state
                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: card_up_time
                                                        
                                                        	card up time
                                                        	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime>`
                                                        
                                                        .. attribute:: card_administrative_state
                                                        
                                                        	card admin state\: shutdown or not
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_administrative_state
                                                        
                                                        	power admin state\: up or down
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_operational_state
                                                        
                                                        	card operation state
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_monitor_state
                                                        
                                                        	card is monitored by a manager or left unmonitored
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_reset_reason
                                                        
                                                        	card reset reason enum
                                                        	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                                        
                                                        .. attribute:: power_current_measurement
                                                        
                                                        	power current\: not implemented
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_operational_state
                                                        
                                                        	Power operation state
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime))])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                                ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                                ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                                ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                                ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                                ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                                ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                            ])
                                                            self.card_administrative_state = None
                                                            self.power_administrative_state = None
                                                            self.card_operational_state = None
                                                            self.card_monitor_state = None
                                                            self.card_reset_reason = None
                                                            self.power_current_measurement = None
                                                            self.power_operational_state = None

                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                            self._children_yang_names.add("last-operational-state-change")

                                                            self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                            self.card_up_time.parent = self
                                                            self._children_name_map["card_up_time"] = "card-up-time"
                                                            self._children_yang_names.add("card-up-time")
                                                            self._segment_path = lambda: "fru-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                                        class LastOperationalStateChange(Entity):
                                                            """
                                                            last card oper change state
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_container_classes = OrderedDict([])
                                                                self._child_list_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                    ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "last-operational-state-change"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                        class CardUpTime(Entity):
                                                            """
                                                            card up time
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                                self.yang_name = "card-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_container_classes = OrderedDict([])
                                                                self._child_list_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                    ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "card-up-time"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                        class PortSlots(Entity):
                                            """
                                            PortSlotTable contains all optics ports in a
                                            SPA/PLIM.
                                            
                                            .. attribute:: port_slot
                                            
                                            	PortSlot number in the SPA/PLIM
                                            	**type**\: list of  		 :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, self).__init__()

                                                self.yang_name = "port-slots"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([("port-slot", ("port_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot))])
                                                self._leafs = OrderedDict()

                                                self.port_slot = YList(self)
                                                self._segment_path = lambda: "port-slots"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, [], name, value)


                                            class PortSlot(Entity):
                                                """
                                                PortSlot number in the SPA/PLIM
                                                
                                                .. attribute:: number  (key)
                                                
                                                	portslot number
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: port
                                                
                                                	Port string
                                                	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port>`
                                                
                                                .. attribute:: basic_attributes
                                                
                                                	Attributes
                                                	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, self).__init__()

                                                    self.yang_name = "port-slot"
                                                    self.yang_parent_name = "port-slots"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['number']
                                                    self._child_container_classes = OrderedDict([("port", ("port", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes))])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('number', YLeaf(YType.int32, 'number')),
                                                    ])
                                                    self.number = None

                                                    self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port()
                                                    self.port.parent = self
                                                    self._children_name_map["port"] = "port"
                                                    self._children_yang_names.add("port")

                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self._children_name_map["basic_attributes"] = "basic-attributes"
                                                    self._children_yang_names.add("basic-attributes")
                                                    self._segment_path = lambda: "port-slot" + "[number='" + str(self.number) + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, ['number'], name, value)


                                                class Port(Entity):
                                                    """
                                                    Port string
                                                    
                                                    .. attribute:: basic_attributes
                                                    
                                                    	Attributes
                                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port, self).__init__()

                                                        self.yang_name = "port"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes))])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict()

                                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes()
                                                        self.basic_attributes.parent = self
                                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                                        self._children_yang_names.add("basic-attributes")
                                                        self._segment_path = lambda: "port"


                                                    class BasicAttributes(Entity):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Inventory information
                                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) inventory information
                                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes, self).__init__()

                                                            self.yang_name = "basic-attributes"
                                                            self.yang_parent_name = "port"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo))])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict()

                                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self._children_name_map["basic_info"] = "basic-info"
                                                            self._children_yang_names.add("basic-info")

                                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo()
                                                            self.fru_info.parent = self
                                                            self._children_name_map["fru_info"] = "fru-info"
                                                            self._children_yang_names.add("fru-info")
                                                            self._segment_path = lambda: "basic-attributes"


                                                        class BasicInfo(Entity):
                                                            """
                                                            Inventory information
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms       what the entity in question does
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: chip_hardware_revision
                                                            
                                                            	chip module hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: manufacturer_name
                                                            
                                                            	manufacturer's name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: asset_id_str
                                                            
                                                            	asset Identification string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: asset_identification
                                                            
                                                            	asset Identification
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\: bool
                                                            
                                                            .. attribute:: manufacturer_asset_tags
                                                            
                                                            	Manufacture Asset Tags
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: composite_class_code
                                                            
                                                            	Major&minor class of the entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: memory_size
                                                            
                                                            	Size of memory associated with       the entity where applicable
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: environmental_monitor_path
                                                            
                                                            	sysdb name of sensor in the envmon EDM
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: alias
                                                            
                                                            	useful for storing an entity alias 
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: group_flag
                                                            
                                                            	indicates if this entity is group       or not
                                                            	**type**\: bool
                                                            
                                                            .. attribute:: new_deviation_number
                                                            
                                                            	integer value for New Deviation Number 0x88
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: physical_layer_interface_module_type
                                                            
                                                            	integer value for plim type if     applicable to this entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: unrecognized_fru
                                                            
                                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                            	**type**\: bool
                                                            
                                                            .. attribute:: redundancystate
                                                            
                                                            	integer value for Redundancy State if     applicable to this entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: ceport
                                                            
                                                            	1 if ce port found, 0 if not
                                                            	**type**\: bool
                                                            
                                                            .. attribute:: xr_scoped
                                                            
                                                            	1 if xr scoped, 0 if not
                                                            	**type**\: bool
                                                            
                                                            .. attribute:: unique_id
                                                            
                                                            	Unique id for an entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, self).__init__()

                                                                self.yang_name = "basic-info"
                                                                self.yang_parent_name = "basic-attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_container_classes = OrderedDict([])
                                                                self._child_list_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('description', YLeaf(YType.str, 'description')),
                                                                    ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                                    ('name', YLeaf(YType.str, 'name')),
                                                                    ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                                    ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                                    ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                                    ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                                    ('model_name', YLeaf(YType.str, 'model-name')),
                                                                    ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                                    ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                                    ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                                    ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                                    ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                                    ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                                    ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                                    ('alias', YLeaf(YType.str, 'alias')),
                                                                    ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                                    ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                                    ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                                    ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                                    ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                                    ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                                    ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                                    ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                                ])
                                                                self.description = None
                                                                self.vendor_type = None
                                                                self.name = None
                                                                self.hardware_revision = None
                                                                self.firmware_revision = None
                                                                self.software_revision = None
                                                                self.chip_hardware_revision = None
                                                                self.serial_number = None
                                                                self.manufacturer_name = None
                                                                self.model_name = None
                                                                self.asset_id_str = None
                                                                self.asset_identification = None
                                                                self.is_field_replaceable_unit = None
                                                                self.manufacturer_asset_tags = None
                                                                self.composite_class_code = None
                                                                self.memory_size = None
                                                                self.environmental_monitor_path = None
                                                                self.alias = None
                                                                self.group_flag = None
                                                                self.new_deviation_number = None
                                                                self.physical_layer_interface_module_type = None
                                                                self.unrecognized_fru = None
                                                                self.redundancystate = None
                                                                self.ceport = None
                                                                self.xr_scoped = None
                                                                self.unique_id = None
                                                                self._segment_path = lambda: "basic-info"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                                        class FruInfo(Entity):
                                                            """
                                                            Field Replaceable Unit (FRU) inventory
                                                            information
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	last card oper change state
                                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            .. attribute:: card_up_time
                                                            
                                                            	card up time
                                                            	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime>`
                                                            
                                                            .. attribute:: card_administrative_state
                                                            
                                                            	card admin state\: shutdown or not
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: power_administrative_state
                                                            
                                                            	power admin state\: up or down
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: card_operational_state
                                                            
                                                            	card operation state
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: card_monitor_state
                                                            
                                                            	card is monitored by a manager or left unmonitored
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: card_reset_reason
                                                            
                                                            	card reset reason enum
                                                            	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                                            
                                                            .. attribute:: power_current_measurement
                                                            
                                                            	power current\: not implemented
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: power_operational_state
                                                            
                                                            	Power operation state
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, self).__init__()

                                                                self.yang_name = "fru-info"
                                                                self.yang_parent_name = "basic-attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime))])
                                                                self._child_list_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                                    ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                                    ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                                    ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                                    ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                                    ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                                    ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                                ])
                                                                self.card_administrative_state = None
                                                                self.power_administrative_state = None
                                                                self.card_operational_state = None
                                                                self.card_monitor_state = None
                                                                self.card_reset_reason = None
                                                                self.power_current_measurement = None
                                                                self.power_operational_state = None

                                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                                self._children_yang_names.add("last-operational-state-change")

                                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime()
                                                                self.card_up_time.parent = self
                                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                                self._children_yang_names.add("card-up-time")
                                                                self._segment_path = lambda: "fru-info"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                                            class LastOperationalStateChange(Entity):
                                                                """
                                                                last card oper change state
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                                _revision = '2017-01-04'

                                                                def __init__(self):
                                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                    self.yang_name = "last-operational-state-change"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_container_classes = OrderedDict([])
                                                                    self._child_list_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "last-operational-state-change"

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                            class CardUpTime(Entity):
                                                                """
                                                                card up time
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                                _revision = '2017-01-04'

                                                                def __init__(self):
                                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                                    self.yang_name = "card-up-time"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_container_classes = OrderedDict([])
                                                                    self._child_list_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "card-up-time"

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                class BasicAttributes(Entity):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Inventory information
                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) inventory information
                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes, self).__init__()

                                                        self.yang_name = "basic-attributes"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo))])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict()

                                                        self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self._children_name_map["basic_info"] = "basic-info"
                                                        self._children_yang_names.add("basic-info")

                                                        self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo()
                                                        self.fru_info.parent = self
                                                        self._children_name_map["fru_info"] = "fru-info"
                                                        self._children_yang_names.add("fru-info")
                                                        self._segment_path = lambda: "basic-attributes"


                                                    class BasicInfo(Entity):
                                                        """
                                                        Inventory information
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms       what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: chip_hardware_revision
                                                        
                                                        	chip module hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: manufacturer_name
                                                        
                                                        	manufacturer's name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_id_str
                                                        
                                                        	asset Identification string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_identification
                                                        
                                                        	asset Identification
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: manufacturer_asset_tags
                                                        
                                                        	Manufacture Asset Tags
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: composite_class_code
                                                        
                                                        	Major&minor class of the entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: memory_size
                                                        
                                                        	Size of memory associated with       the entity where applicable
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: environmental_monitor_path
                                                        
                                                        	sysdb name of sensor in the envmon EDM
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: alias
                                                        
                                                        	useful for storing an entity alias 
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: group_flag
                                                        
                                                        	indicates if this entity is group       or not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: new_deviation_number
                                                        
                                                        	integer value for New Deviation Number 0x88
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: physical_layer_interface_module_type
                                                        
                                                        	integer value for plim type if     applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: unrecognized_fru
                                                        
                                                        	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: redundancystate
                                                        
                                                        	integer value for Redundancy State if     applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: ceport
                                                        
                                                        	1 if ce port found, 0 if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: xr_scoped
                                                        
                                                        	1 if xr scoped, 0 if not
                                                        	**type**\: bool
                                                        
                                                        .. attribute:: unique_id
                                                        
                                                        	Unique id for an entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('description', YLeaf(YType.str, 'description')),
                                                                ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                                ('name', YLeaf(YType.str, 'name')),
                                                                ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                                ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                                ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                                ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                                ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                                ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                                ('model_name', YLeaf(YType.str, 'model-name')),
                                                                ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                                ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                                ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                                ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                                ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                                ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                                ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                                ('alias', YLeaf(YType.str, 'alias')),
                                                                ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                                ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                                ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                                ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                                ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                                ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                                ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                                ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                            ])
                                                            self.description = None
                                                            self.vendor_type = None
                                                            self.name = None
                                                            self.hardware_revision = None
                                                            self.firmware_revision = None
                                                            self.software_revision = None
                                                            self.chip_hardware_revision = None
                                                            self.serial_number = None
                                                            self.manufacturer_name = None
                                                            self.model_name = None
                                                            self.asset_id_str = None
                                                            self.asset_identification = None
                                                            self.is_field_replaceable_unit = None
                                                            self.manufacturer_asset_tags = None
                                                            self.composite_class_code = None
                                                            self.memory_size = None
                                                            self.environmental_monitor_path = None
                                                            self.alias = None
                                                            self.group_flag = None
                                                            self.new_deviation_number = None
                                                            self.physical_layer_interface_module_type = None
                                                            self.unrecognized_fru = None
                                                            self.redundancystate = None
                                                            self.ceport = None
                                                            self.xr_scoped = None
                                                            self.unique_id = None
                                                            self._segment_path = lambda: "basic-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                                    class FruInfo(Entity):
                                                        """
                                                        Field Replaceable Unit (FRU) inventory
                                                        information
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	last card oper change state
                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: card_up_time
                                                        
                                                        	card up time
                                                        	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime>`
                                                        
                                                        .. attribute:: card_administrative_state
                                                        
                                                        	card admin state\: shutdown or not
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_administrative_state
                                                        
                                                        	power admin state\: up or down
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_operational_state
                                                        
                                                        	card operation state
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_monitor_state
                                                        
                                                        	card is monitored by a manager or left unmonitored
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_reset_reason
                                                        
                                                        	card reset reason enum
                                                        	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                                        
                                                        .. attribute:: power_current_measurement
                                                        
                                                        	power current\: not implemented
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_operational_state
                                                        
                                                        	Power operation state
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime))])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                                ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                                ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                                ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                                ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                                ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                                ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                            ])
                                                            self.card_administrative_state = None
                                                            self.power_administrative_state = None
                                                            self.card_operational_state = None
                                                            self.card_monitor_state = None
                                                            self.card_reset_reason = None
                                                            self.power_current_measurement = None
                                                            self.power_operational_state = None

                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                            self._children_yang_names.add("last-operational-state-change")

                                                            self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime()
                                                            self.card_up_time.parent = self
                                                            self._children_name_map["card_up_time"] = "card-up-time"
                                                            self._children_yang_names.add("card-up-time")
                                                            self._segment_path = lambda: "fru-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                                        class LastOperationalStateChange(Entity):
                                                            """
                                                            last card oper change state
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_container_classes = OrderedDict([])
                                                                self._child_list_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                    ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "last-operational-state-change"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                        class CardUpTime(Entity):
                                                            """
                                                            card up time
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                                self.yang_name = "card-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_container_classes = OrderedDict([])
                                                                self._child_list_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                    ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "card-up-time"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                        class BasicAttributes(Entity):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Inventory information
                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes, self).__init__()

                                                self.yang_name = "basic-attributes"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict()

                                                self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self._children_name_map["basic_info"] = "basic-info"
                                                self._children_yang_names.add("basic-info")

                                                self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo()
                                                self.fru_info.parent = self
                                                self._children_name_map["fru_info"] = "fru-info"
                                                self._children_yang_names.add("fru-info")
                                                self._segment_path = lambda: "basic-attributes"


                                            class BasicInfo(Entity):
                                                """
                                                Inventory information
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms       what the entity in question does
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: chip_hardware_revision
                                                
                                                	chip module hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: manufacturer_name
                                                
                                                	manufacturer's name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_id_str
                                                
                                                	asset Identification string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_identification
                                                
                                                	asset Identification
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                .. attribute:: manufacturer_asset_tags
                                                
                                                	Manufacture Asset Tags
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: composite_class_code
                                                
                                                	Major&minor class of the entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: memory_size
                                                
                                                	Size of memory associated with       the entity where applicable
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: environmental_monitor_path
                                                
                                                	sysdb name of sensor in the envmon EDM
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: alias
                                                
                                                	useful for storing an entity alias 
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: group_flag
                                                
                                                	indicates if this entity is group       or not
                                                	**type**\: bool
                                                
                                                .. attribute:: new_deviation_number
                                                
                                                	integer value for New Deviation Number 0x88
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: physical_layer_interface_module_type
                                                
                                                	integer value for plim type if     applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: unrecognized_fru
                                                
                                                	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                	**type**\: bool
                                                
                                                .. attribute:: redundancystate
                                                
                                                	integer value for Redundancy State if     applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: ceport
                                                
                                                	1 if ce port found, 0 if not
                                                	**type**\: bool
                                                
                                                .. attribute:: xr_scoped
                                                
                                                	1 if xr scoped, 0 if not
                                                	**type**\: bool
                                                
                                                .. attribute:: unique_id
                                                
                                                	Unique id for an entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('description', YLeaf(YType.str, 'description')),
                                                        ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                        ('name', YLeaf(YType.str, 'name')),
                                                        ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                        ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                        ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                        ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                        ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                        ('model_name', YLeaf(YType.str, 'model-name')),
                                                        ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                        ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                        ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                        ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                        ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                        ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                        ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                        ('alias', YLeaf(YType.str, 'alias')),
                                                        ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                        ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                        ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                        ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                        ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                        ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                        ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                        ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                    ])
                                                    self.description = None
                                                    self.vendor_type = None
                                                    self.name = None
                                                    self.hardware_revision = None
                                                    self.firmware_revision = None
                                                    self.software_revision = None
                                                    self.chip_hardware_revision = None
                                                    self.serial_number = None
                                                    self.manufacturer_name = None
                                                    self.model_name = None
                                                    self.asset_id_str = None
                                                    self.asset_identification = None
                                                    self.is_field_replaceable_unit = None
                                                    self.manufacturer_asset_tags = None
                                                    self.composite_class_code = None
                                                    self.memory_size = None
                                                    self.environmental_monitor_path = None
                                                    self.alias = None
                                                    self.group_flag = None
                                                    self.new_deviation_number = None
                                                    self.physical_layer_interface_module_type = None
                                                    self.unrecognized_fru = None
                                                    self.redundancystate = None
                                                    self.ceport = None
                                                    self.xr_scoped = None
                                                    self.unique_id = None
                                                    self._segment_path = lambda: "basic-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                            class FruInfo(Entity):
                                                """
                                                Field Replaceable Unit (FRU) inventory
                                                information
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	last card oper change state
                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: card_up_time
                                                
                                                	card up time
                                                	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime>`
                                                
                                                .. attribute:: card_administrative_state
                                                
                                                	card admin state\: shutdown or not
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_administrative_state
                                                
                                                	power admin state\: up or down
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_operational_state
                                                
                                                	card operation state
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_monitor_state
                                                
                                                	card is monitored by a manager or left unmonitored
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_reset_reason
                                                
                                                	card reset reason enum
                                                	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                                
                                                .. attribute:: power_current_measurement
                                                
                                                	power current\: not implemented
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_operational_state
                                                
                                                	Power operation state
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime))])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                        ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                        ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                        ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                        ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                        ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                        ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                    ])
                                                    self.card_administrative_state = None
                                                    self.power_administrative_state = None
                                                    self.card_operational_state = None
                                                    self.card_monitor_state = None
                                                    self.card_reset_reason = None
                                                    self.power_current_measurement = None
                                                    self.power_operational_state = None

                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                    self._children_yang_names.add("last-operational-state-change")

                                                    self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime()
                                                    self.card_up_time.parent = self
                                                    self._children_name_map["card_up_time"] = "card-up-time"
                                                    self._children_yang_names.add("card-up-time")
                                                    self._segment_path = lambda: "fru-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                                class LastOperationalStateChange(Entity):
                                                    """
                                                    last card oper change state
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                            ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "last-operational-state-change"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                class CardUpTime(Entity):
                                                    """
                                                    card up time
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                        self.yang_name = "card-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                            ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "card-up-time"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"
                                            self._children_yang_names.add("basic-info")

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._children_yang_names.add("fru-info")
                                            self._segment_path = lambda: "basic-attributes"


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', YLeaf(YType.str, 'description')),
                                                    ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                    ('name', YLeaf(YType.str, 'name')),
                                                    ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                    ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                    ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                    ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                    ('model_name', YLeaf(YType.str, 'model-name')),
                                                    ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                    ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                    ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                    ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                    ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                    ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                    ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                    ('alias', YLeaf(YType.str, 'alias')),
                                                    ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                    ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                    ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                    ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                    ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                    ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                    ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                    ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                ])
                                                self.description = None
                                                self.vendor_type = None
                                                self.name = None
                                                self.hardware_revision = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.chip_hardware_revision = None
                                                self.serial_number = None
                                                self.manufacturer_name = None
                                                self.model_name = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.composite_class_code = None
                                                self.memory_size = None
                                                self.environmental_monitor_path = None
                                                self.alias = None
                                                self.group_flag = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.unrecognized_fru = None
                                                self.redundancystate = None
                                                self.ceport = None
                                                self.xr_scoped = None
                                                self.unique_id = None
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                    ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                    ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                    ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                    ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                    ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                    ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                ])
                                                self.card_administrative_state = None
                                                self.power_administrative_state = None
                                                self.card_operational_state = None
                                                self.card_monitor_state = None
                                                self.card_reset_reason = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                            class CardUpTime(Entity):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                            class HwComponents(Entity):
                                """
                                HWComponent table contains all HW modules
                                within the card 
                                
                                .. attribute:: hw_component
                                
                                	HWComponent number
                                	**type**\: list of  		 :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, self).__init__()

                                    self.yang_name = "hw-components"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("hw-component", ("hw_component", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent))])
                                    self._leafs = OrderedDict()

                                    self.hw_component = YList(self)
                                    self._segment_path = lambda: "hw-components"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, [], name, value)


                                class HwComponent(Entity):
                                    """
                                    HWComponent number
                                    
                                    .. attribute:: number  (key)
                                    
                                    	node number
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: sensors
                                    
                                    	ModuleSensorTable contains all sensors in a Module
                                    	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors>`
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, self).__init__()

                                        self.yang_name = "hw-component"
                                        self.yang_parent_name = "hw-components"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_container_classes = OrderedDict([("sensors", ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('number', YLeaf(YType.int32, 'number')),
                                        ])
                                        self.number = None

                                        self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors()
                                        self.sensors.parent = self
                                        self._children_name_map["sensors"] = "sensors"
                                        self._children_yang_names.add("sensors")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")
                                        self._segment_path = lambda: "hw-component" + "[number='" + str(self.number) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, ['number'], name, value)


                                    class Sensors(Entity):
                                        """
                                        ModuleSensorTable contains all sensors in a
                                        Module.
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number in the Module
                                        	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, self).__init__()

                                            self.yang_name = "sensors"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("sensor", ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor))])
                                            self._leafs = OrderedDict()

                                            self.sensor = YList(self)
                                            self._segment_path = lambda: "sensors"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, [], name, value)


                                        class Sensor(Entity):
                                            """
                                            Sensor number in the Module
                                            
                                            .. attribute:: number  (key)
                                            
                                            	sensor number
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: basic_attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                self.yang_name = "sensor"
                                                self.yang_parent_name = "sensors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['number']
                                                self._child_container_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('number', YLeaf(YType.int32, 'number')),
                                                ])
                                                self.number = None

                                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes()
                                                self.basic_attributes.parent = self
                                                self._children_name_map["basic_attributes"] = "basic-attributes"
                                                self._children_yang_names.add("basic-attributes")
                                                self._segment_path = lambda: "sensor" + "[number='" + str(self.number) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, ['number'], name, value)


                                            class BasicAttributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Inventory information
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) inventory information
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes, self).__init__()

                                                    self.yang_name = "basic-attributes"
                                                    self.yang_parent_name = "sensor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo))])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"
                                                    self._children_yang_names.add("basic-info")

                                                    self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._children_yang_names.add("fru-info")
                                                    self._segment_path = lambda: "basic-attributes"


                                                class BasicInfo(Entity):
                                                    """
                                                    Inventory information
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms       what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: chip_hardware_revision
                                                    
                                                    	chip module hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: manufacturer_name
                                                    
                                                    	manufacturer's name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: asset_id_str
                                                    
                                                    	asset Identification string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: asset_identification
                                                    
                                                    	asset Identification
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: manufacturer_asset_tags
                                                    
                                                    	Manufacture Asset Tags
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: composite_class_code
                                                    
                                                    	Major&minor class of the entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: memory_size
                                                    
                                                    	Size of memory associated with       the entity where applicable
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: environmental_monitor_path
                                                    
                                                    	sysdb name of sensor in the envmon EDM
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: alias
                                                    
                                                    	useful for storing an entity alias 
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: group_flag
                                                    
                                                    	indicates if this entity is group       or not
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: new_deviation_number
                                                    
                                                    	integer value for New Deviation Number 0x88
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: physical_layer_interface_module_type
                                                    
                                                    	integer value for plim type if     applicable to this entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: unrecognized_fru
                                                    
                                                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: redundancystate
                                                    
                                                    	integer value for Redundancy State if     applicable to this entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: ceport
                                                    
                                                    	1 if ce port found, 0 if not
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: xr_scoped
                                                    
                                                    	1 if xr scoped, 0 if not
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: unique_id
                                                    
                                                    	Unique id for an entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "basic-attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('description', YLeaf(YType.str, 'description')),
                                                            ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                            ('name', YLeaf(YType.str, 'name')),
                                                            ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                            ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                            ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                            ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                            ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                            ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                            ('model_name', YLeaf(YType.str, 'model-name')),
                                                            ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                            ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                            ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                            ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                            ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                            ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                            ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                            ('alias', YLeaf(YType.str, 'alias')),
                                                            ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                            ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                            ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                            ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                            ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                            ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                            ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                            ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                        ])
                                                        self.description = None
                                                        self.vendor_type = None
                                                        self.name = None
                                                        self.hardware_revision = None
                                                        self.firmware_revision = None
                                                        self.software_revision = None
                                                        self.chip_hardware_revision = None
                                                        self.serial_number = None
                                                        self.manufacturer_name = None
                                                        self.model_name = None
                                                        self.asset_id_str = None
                                                        self.asset_identification = None
                                                        self.is_field_replaceable_unit = None
                                                        self.manufacturer_asset_tags = None
                                                        self.composite_class_code = None
                                                        self.memory_size = None
                                                        self.environmental_monitor_path = None
                                                        self.alias = None
                                                        self.group_flag = None
                                                        self.new_deviation_number = None
                                                        self.physical_layer_interface_module_type = None
                                                        self.unrecognized_fru = None
                                                        self.redundancystate = None
                                                        self.ceport = None
                                                        self.xr_scoped = None
                                                        self.unique_id = None
                                                        self._segment_path = lambda: "basic-info"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) inventory
                                                    information
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	last card oper change state
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: card_up_time
                                                    
                                                    	card up time
                                                    	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime>`
                                                    
                                                    .. attribute:: card_administrative_state
                                                    
                                                    	card admin state\: shutdown or not
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: power_administrative_state
                                                    
                                                    	power admin state\: up or down
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: card_operational_state
                                                    
                                                    	card operation state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: card_monitor_state
                                                    
                                                    	card is monitored by a manager or left unmonitored
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: card_reset_reason
                                                    
                                                    	card reset reason enum
                                                    	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                                    
                                                    .. attribute:: power_current_measurement
                                                    
                                                    	power current\: not implemented
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: power_operational_state
                                                    
                                                    	Power operation state
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "basic-attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime))])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                            ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                            ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                            ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                            ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                            ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                            ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                        ])
                                                        self.card_administrative_state = None
                                                        self.power_administrative_state = None
                                                        self.card_operational_state = None
                                                        self.card_monitor_state = None
                                                        self.card_reset_reason = None
                                                        self.power_current_measurement = None
                                                        self.power_operational_state = None

                                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                        self._children_yang_names.add("last-operational-state-change")

                                                        self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                        self.card_up_time.parent = self
                                                        self._children_name_map["card_up_time"] = "card-up-time"
                                                        self._children_yang_names.add("card-up-time")
                                                        self._segment_path = lambda: "fru-info"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        last card oper change state
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                    class CardUpTime(Entity):
                                                        """
                                                        card up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                            self.yang_name = "card-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                                ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "card-up-time"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"
                                            self._children_yang_names.add("basic-info")

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._children_yang_names.add("fru-info")
                                            self._segment_path = lambda: "basic-attributes"


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', YLeaf(YType.str, 'description')),
                                                    ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                    ('name', YLeaf(YType.str, 'name')),
                                                    ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                    ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                    ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                    ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                    ('model_name', YLeaf(YType.str, 'model-name')),
                                                    ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                    ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                    ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                    ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                    ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                    ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                    ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                    ('alias', YLeaf(YType.str, 'alias')),
                                                    ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                    ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                    ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                    ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                    ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                    ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                    ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                    ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                ])
                                                self.description = None
                                                self.vendor_type = None
                                                self.name = None
                                                self.hardware_revision = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.chip_hardware_revision = None
                                                self.serial_number = None
                                                self.manufacturer_name = None
                                                self.model_name = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.composite_class_code = None
                                                self.memory_size = None
                                                self.environmental_monitor_path = None
                                                self.alias = None
                                                self.group_flag = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.unrecognized_fru = None
                                                self.redundancystate = None
                                                self.ceport = None
                                                self.xr_scoped = None
                                                self.unique_id = None
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                    ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                    ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                    ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                    ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                    ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                    ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                ])
                                                self.card_administrative_state = None
                                                self.power_administrative_state = None
                                                self.card_operational_state = None
                                                self.card_monitor_state = None
                                                self.card_reset_reason = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                            class CardUpTime(Entity):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                            class Sensors(Entity):
                                """
                                ModuleSensorTable contains all sensors in a
                                Module.
                                
                                .. attribute:: sensor
                                
                                	Sensor number in the Module
                                	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, self).__init__()

                                    self.yang_name = "sensors"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("sensor", ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor))])
                                    self._leafs = OrderedDict()

                                    self.sensor = YList(self)
                                    self._segment_path = lambda: "sensors"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, [], name, value)


                                class Sensor(Entity):
                                    """
                                    Sensor number in the Module
                                    
                                    .. attribute:: number  (key)
                                    
                                    	sensor number
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, self).__init__()

                                        self.yang_name = "sensor"
                                        self.yang_parent_name = "sensors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_container_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('number', YLeaf(YType.int32, 'number')),
                                        ])
                                        self.number = None

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")
                                        self._segment_path = lambda: "sensor" + "[number='" + str(self.number) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, ['number'], name, value)


                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "sensor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"
                                            self._children_yang_names.add("basic-info")

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._children_yang_names.add("fru-info")
                                            self._segment_path = lambda: "basic-attributes"


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', YLeaf(YType.str, 'description')),
                                                    ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                    ('name', YLeaf(YType.str, 'name')),
                                                    ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                    ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                    ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                    ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                    ('model_name', YLeaf(YType.str, 'model-name')),
                                                    ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                    ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                    ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                    ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                    ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                    ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                    ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                    ('alias', YLeaf(YType.str, 'alias')),
                                                    ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                    ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                    ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                    ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                    ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                    ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                    ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                    ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                ])
                                                self.description = None
                                                self.vendor_type = None
                                                self.name = None
                                                self.hardware_revision = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.chip_hardware_revision = None
                                                self.serial_number = None
                                                self.manufacturer_name = None
                                                self.model_name = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.composite_class_code = None
                                                self.memory_size = None
                                                self.environmental_monitor_path = None
                                                self.alias = None
                                                self.group_flag = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.unrecognized_fru = None
                                                self.redundancystate = None
                                                self.ceport = None
                                                self.xr_scoped = None
                                                self.unique_id = None
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                    ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                    ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                    ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                    ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                    ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                    ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                ])
                                                self.card_administrative_state = None
                                                self.power_administrative_state = None
                                                self.card_operational_state = None
                                                self.card_monitor_state = None
                                                self.card_reset_reason = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                            class CardUpTime(Entity):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                            class PortSlots(Entity):
                                """
                                PortSlotTable contains all optics ports in a
                                SPA/PLIM.
                                
                                .. attribute:: port_slot
                                
                                	PortSlot number in the SPA/PLIM
                                	**type**\: list of  		 :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, self).__init__()

                                    self.yang_name = "port-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("port-slot", ("port_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot))])
                                    self._leafs = OrderedDict()

                                    self.port_slot = YList(self)
                                    self._segment_path = lambda: "port-slots"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, [], name, value)


                                class PortSlot(Entity):
                                    """
                                    PortSlot number in the SPA/PLIM
                                    
                                    .. attribute:: number  (key)
                                    
                                    	portslot number
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: port
                                    
                                    	Port string
                                    	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port>`
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, self).__init__()

                                        self.yang_name = "port-slot"
                                        self.yang_parent_name = "port-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_container_classes = OrderedDict([("port", ("port", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('number', YLeaf(YType.int32, 'number')),
                                        ])
                                        self.number = None

                                        self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port()
                                        self.port.parent = self
                                        self._children_name_map["port"] = "port"
                                        self._children_yang_names.add("port")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")
                                        self._segment_path = lambda: "port-slot" + "[number='" + str(self.number) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, ['number'], name, value)


                                    class Port(Entity):
                                        """
                                        Port string
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port, self).__init__()

                                            self.yang_name = "port"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes()
                                            self.basic_attributes.parent = self
                                            self._children_name_map["basic_attributes"] = "basic-attributes"
                                            self._children_yang_names.add("basic-attributes")
                                            self._segment_path = lambda: "port"


                                        class BasicAttributes(Entity):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Inventory information
                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes, self).__init__()

                                                self.yang_name = "basic-attributes"
                                                self.yang_parent_name = "port"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict()

                                                self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self._children_name_map["basic_info"] = "basic-info"
                                                self._children_yang_names.add("basic-info")

                                                self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo()
                                                self.fru_info.parent = self
                                                self._children_name_map["fru_info"] = "fru-info"
                                                self._children_yang_names.add("fru-info")
                                                self._segment_path = lambda: "basic-attributes"


                                            class BasicInfo(Entity):
                                                """
                                                Inventory information
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms       what the entity in question does
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: chip_hardware_revision
                                                
                                                	chip module hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: manufacturer_name
                                                
                                                	manufacturer's name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_id_str
                                                
                                                	asset Identification string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_identification
                                                
                                                	asset Identification
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                .. attribute:: manufacturer_asset_tags
                                                
                                                	Manufacture Asset Tags
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: composite_class_code
                                                
                                                	Major&minor class of the entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: memory_size
                                                
                                                	Size of memory associated with       the entity where applicable
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: environmental_monitor_path
                                                
                                                	sysdb name of sensor in the envmon EDM
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: alias
                                                
                                                	useful for storing an entity alias 
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: group_flag
                                                
                                                	indicates if this entity is group       or not
                                                	**type**\: bool
                                                
                                                .. attribute:: new_deviation_number
                                                
                                                	integer value for New Deviation Number 0x88
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: physical_layer_interface_module_type
                                                
                                                	integer value for plim type if     applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: unrecognized_fru
                                                
                                                	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                	**type**\: bool
                                                
                                                .. attribute:: redundancystate
                                                
                                                	integer value for Redundancy State if     applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: ceport
                                                
                                                	1 if ce port found, 0 if not
                                                	**type**\: bool
                                                
                                                .. attribute:: xr_scoped
                                                
                                                	1 if xr scoped, 0 if not
                                                	**type**\: bool
                                                
                                                .. attribute:: unique_id
                                                
                                                	Unique id for an entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('description', YLeaf(YType.str, 'description')),
                                                        ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                        ('name', YLeaf(YType.str, 'name')),
                                                        ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                        ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                        ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                        ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                        ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                        ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                        ('model_name', YLeaf(YType.str, 'model-name')),
                                                        ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                        ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                        ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                        ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                        ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                        ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                        ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                        ('alias', YLeaf(YType.str, 'alias')),
                                                        ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                        ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                        ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                        ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                        ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                        ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                        ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                        ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                    ])
                                                    self.description = None
                                                    self.vendor_type = None
                                                    self.name = None
                                                    self.hardware_revision = None
                                                    self.firmware_revision = None
                                                    self.software_revision = None
                                                    self.chip_hardware_revision = None
                                                    self.serial_number = None
                                                    self.manufacturer_name = None
                                                    self.model_name = None
                                                    self.asset_id_str = None
                                                    self.asset_identification = None
                                                    self.is_field_replaceable_unit = None
                                                    self.manufacturer_asset_tags = None
                                                    self.composite_class_code = None
                                                    self.memory_size = None
                                                    self.environmental_monitor_path = None
                                                    self.alias = None
                                                    self.group_flag = None
                                                    self.new_deviation_number = None
                                                    self.physical_layer_interface_module_type = None
                                                    self.unrecognized_fru = None
                                                    self.redundancystate = None
                                                    self.ceport = None
                                                    self.xr_scoped = None
                                                    self.unique_id = None
                                                    self._segment_path = lambda: "basic-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                            class FruInfo(Entity):
                                                """
                                                Field Replaceable Unit (FRU) inventory
                                                information
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	last card oper change state
                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: card_up_time
                                                
                                                	card up time
                                                	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime>`
                                                
                                                .. attribute:: card_administrative_state
                                                
                                                	card admin state\: shutdown or not
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_administrative_state
                                                
                                                	power admin state\: up or down
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_operational_state
                                                
                                                	card operation state
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_monitor_state
                                                
                                                	card is monitored by a manager or left unmonitored
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_reset_reason
                                                
                                                	card reset reason enum
                                                	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                                
                                                .. attribute:: power_current_measurement
                                                
                                                	power current\: not implemented
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_operational_state
                                                
                                                	Power operation state
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime))])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                        ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                        ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                        ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                        ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                        ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                        ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                    ])
                                                    self.card_administrative_state = None
                                                    self.power_administrative_state = None
                                                    self.card_operational_state = None
                                                    self.card_monitor_state = None
                                                    self.card_reset_reason = None
                                                    self.power_current_measurement = None
                                                    self.power_operational_state = None

                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                    self._children_yang_names.add("last-operational-state-change")

                                                    self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime()
                                                    self.card_up_time.parent = self
                                                    self._children_name_map["card_up_time"] = "card-up-time"
                                                    self._children_yang_names.add("card-up-time")
                                                    self._segment_path = lambda: "fru-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                                class LastOperationalStateChange(Entity):
                                                    """
                                                    last card oper change state
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                            ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "last-operational-state-change"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                                class CardUpTime(Entity):
                                                    """
                                                    card up time
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                        self.yang_name = "card-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_container_classes = OrderedDict([])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                            ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "card-up-time"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"
                                            self._children_yang_names.add("basic-info")

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._children_yang_names.add("fru-info")
                                            self._segment_path = lambda: "basic-attributes"


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', YLeaf(YType.str, 'description')),
                                                    ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                                    ('name', YLeaf(YType.str, 'name')),
                                                    ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                                    ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                                    ('software_revision', YLeaf(YType.str, 'software-revision')),
                                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                                    ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                                    ('model_name', YLeaf(YType.str, 'model-name')),
                                                    ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                                    ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                                    ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                                    ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                                    ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                                    ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                                    ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                                    ('alias', YLeaf(YType.str, 'alias')),
                                                    ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                                    ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                                    ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                                    ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                                    ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                                    ('ceport', YLeaf(YType.boolean, 'ceport')),
                                                    ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                                    ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                                ])
                                                self.description = None
                                                self.vendor_type = None
                                                self.name = None
                                                self.hardware_revision = None
                                                self.firmware_revision = None
                                                self.software_revision = None
                                                self.chip_hardware_revision = None
                                                self.serial_number = None
                                                self.manufacturer_name = None
                                                self.model_name = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.composite_class_code = None
                                                self.memory_size = None
                                                self.environmental_monitor_path = None
                                                self.alias = None
                                                self.group_flag = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.unrecognized_fru = None
                                                self.redundancystate = None
                                                self.ceport = None
                                                self.xr_scoped = None
                                                self.unique_id = None
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                                    ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                                    ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                                    ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                                    ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                                    ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                                    ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                                ])
                                                self.card_administrative_state = None
                                                self.power_administrative_state = None
                                                self.card_operational_state = None
                                                self.card_monitor_state = None
                                                self.card_reset_reason = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                            class CardUpTime(Entity):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                            class BasicAttributes(Entity):
                                """
                                Attributes
                                
                                .. attribute:: basic_info
                                
                                	Inventory information
                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo>`
                                
                                .. attribute:: fru_info
                                
                                	Field Replaceable Unit (FRU) inventory information
                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes, self).__init__()

                                    self.yang_name = "basic-attributes"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo()
                                    self.basic_info.parent = self
                                    self._children_name_map["basic_info"] = "basic-info"
                                    self._children_yang_names.add("basic-info")

                                    self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo()
                                    self.fru_info.parent = self
                                    self._children_name_map["fru_info"] = "fru-info"
                                    self._children_yang_names.add("fru-info")
                                    self._segment_path = lambda: "basic-attributes"


                                class BasicInfo(Entity):
                                    """
                                    Inventory information
                                    
                                    .. attribute:: description
                                    
                                    	describes in user\-readable terms       what the entity in question does
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: vendor_type
                                    
                                    	maps to the vendor OID string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: name
                                    
                                    	name string for the entity
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	hw revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: firmware_revision
                                    
                                    	firmware revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: software_revision
                                    
                                    	software revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: chip_hardware_revision
                                    
                                    	chip module hw revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: serial_number
                                    
                                    	serial number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: manufacturer_name
                                    
                                    	manufacturer's name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: model_name
                                    
                                    	model name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_id_str
                                    
                                    	asset Identification string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_identification
                                    
                                    	asset Identification
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: is_field_replaceable_unit
                                    
                                    	1 if Field Replaceable Unit 0, if not
                                    	**type**\: bool
                                    
                                    .. attribute:: manufacturer_asset_tags
                                    
                                    	Manufacture Asset Tags
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: composite_class_code
                                    
                                    	Major&minor class of the entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: memory_size
                                    
                                    	Size of memory associated with       the entity where applicable
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: environmental_monitor_path
                                    
                                    	sysdb name of sensor in the envmon EDM
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: alias
                                    
                                    	useful for storing an entity alias 
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: group_flag
                                    
                                    	indicates if this entity is group       or not
                                    	**type**\: bool
                                    
                                    .. attribute:: new_deviation_number
                                    
                                    	integer value for New Deviation Number 0x88
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: physical_layer_interface_module_type
                                    
                                    	integer value for plim type if     applicable to this entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: unrecognized_fru
                                    
                                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                                    	**type**\: bool
                                    
                                    .. attribute:: redundancystate
                                    
                                    	integer value for Redundancy State if     applicable to this entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: ceport
                                    
                                    	1 if ce port found, 0 if not
                                    	**type**\: bool
                                    
                                    .. attribute:: xr_scoped
                                    
                                    	1 if xr scoped, 0 if not
                                    	**type**\: bool
                                    
                                    .. attribute:: unique_id
                                    
                                    	Unique id for an entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo, self).__init__()

                                        self.yang_name = "basic-info"
                                        self.yang_parent_name = "basic-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('description', YLeaf(YType.str, 'description')),
                                            ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                            ('name', YLeaf(YType.str, 'name')),
                                            ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                            ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                            ('software_revision', YLeaf(YType.str, 'software-revision')),
                                            ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                            ('serial_number', YLeaf(YType.str, 'serial-number')),
                                            ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                            ('model_name', YLeaf(YType.str, 'model-name')),
                                            ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                            ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                            ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                            ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                            ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                            ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                            ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                            ('alias', YLeaf(YType.str, 'alias')),
                                            ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                            ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                            ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                            ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                            ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                            ('ceport', YLeaf(YType.boolean, 'ceport')),
                                            ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                            ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                        ])
                                        self.description = None
                                        self.vendor_type = None
                                        self.name = None
                                        self.hardware_revision = None
                                        self.firmware_revision = None
                                        self.software_revision = None
                                        self.chip_hardware_revision = None
                                        self.serial_number = None
                                        self.manufacturer_name = None
                                        self.model_name = None
                                        self.asset_id_str = None
                                        self.asset_identification = None
                                        self.is_field_replaceable_unit = None
                                        self.manufacturer_asset_tags = None
                                        self.composite_class_code = None
                                        self.memory_size = None
                                        self.environmental_monitor_path = None
                                        self.alias = None
                                        self.group_flag = None
                                        self.new_deviation_number = None
                                        self.physical_layer_interface_module_type = None
                                        self.unrecognized_fru = None
                                        self.redundancystate = None
                                        self.ceport = None
                                        self.xr_scoped = None
                                        self.unique_id = None
                                        self._segment_path = lambda: "basic-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                                class FruInfo(Entity):
                                    """
                                    Field Replaceable Unit (FRU) inventory
                                    information
                                    
                                    .. attribute:: last_operational_state_change
                                    
                                    	last card oper change state
                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                    
                                    .. attribute:: card_up_time
                                    
                                    	card up time
                                    	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime>`
                                    
                                    .. attribute:: card_administrative_state
                                    
                                    	card admin state\: shutdown or not
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: power_administrative_state
                                    
                                    	power admin state\: up or down
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_operational_state
                                    
                                    	card operation state
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_monitor_state
                                    
                                    	card is monitored by a manager or left unmonitored
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_reset_reason
                                    
                                    	card reset reason enum
                                    	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                                    
                                    .. attribute:: power_current_measurement
                                    
                                    	power current\: not implemented
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: power_operational_state
                                    
                                    	Power operation state
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo, self).__init__()

                                        self.yang_name = "fru-info"
                                        self.yang_parent_name = "basic-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                            ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                            ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                            ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                            ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                            ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                            ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                        ])
                                        self.card_administrative_state = None
                                        self.power_administrative_state = None
                                        self.card_operational_state = None
                                        self.card_monitor_state = None
                                        self.card_reset_reason = None
                                        self.power_current_measurement = None
                                        self.power_operational_state = None

                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange()
                                        self.last_operational_state_change.parent = self
                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                        self._children_yang_names.add("last-operational-state-change")

                                        self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime()
                                        self.card_up_time.parent = self
                                        self._children_name_map["card_up_time"] = "card-up-time"
                                        self._children_yang_names.add("card-up-time")
                                        self._segment_path = lambda: "fru-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                                    class LastOperationalStateChange(Entity):
                                        """
                                        last card oper change state
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: nanosecond
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                            self.yang_name = "last-operational-state-change"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                            ])
                                            self.time_in_seconds = None
                                            self.time_in_nano_seconds = None
                                            self._segment_path = lambda: "last-operational-state-change"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                                    class CardUpTime(Entity):
                                        """
                                        card up time
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: nanosecond
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                            self.yang_name = "card-up-time"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                                ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                            ])
                                            self.time_in_seconds = None
                                            self.time_in_nano_seconds = None
                                            self._segment_path = lambda: "card-up-time"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                    class BasicAttributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo>`
                        
                        .. attribute:: fru_info
                        
                        	Field Replaceable Unit (FRU) inventory information
                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes, self).__init__()

                            self.yang_name = "basic-attributes"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"
                            self._children_yang_names.add("basic-info")

                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo()
                            self.fru_info.parent = self
                            self._children_name_map["fru_info"] = "fru-info"
                            self._children_yang_names.add("fru-info")
                            self._segment_path = lambda: "basic-attributes"


                        class BasicInfo(Entity):
                            """
                            Inventory information
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms       what the entity in question does
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: chip_hardware_revision
                            
                            	chip module hw revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: manufacturer_name
                            
                            	manufacturer's name
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_id_str
                            
                            	asset Identification string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_identification
                            
                            	asset Identification
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\: bool
                            
                            .. attribute:: manufacturer_asset_tags
                            
                            	Manufacture Asset Tags
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: composite_class_code
                            
                            	Major&minor class of the entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: memory_size
                            
                            	Size of memory associated with       the entity where applicable
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: environmental_monitor_path
                            
                            	sysdb name of sensor in the envmon EDM
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: alias
                            
                            	useful for storing an entity alias 
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            .. attribute:: group_flag
                            
                            	indicates if this entity is group       or not
                            	**type**\: bool
                            
                            .. attribute:: new_deviation_number
                            
                            	integer value for New Deviation Number 0x88
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: physical_layer_interface_module_type
                            
                            	integer value for plim type if     applicable to this entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: unrecognized_fru
                            
                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                            	**type**\: bool
                            
                            .. attribute:: redundancystate
                            
                            	integer value for Redundancy State if     applicable to this entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ceport
                            
                            	1 if ce port found, 0 if not
                            	**type**\: bool
                            
                            .. attribute:: xr_scoped
                            
                            	1 if xr scoped, 0 if not
                            	**type**\: bool
                            
                            .. attribute:: unique_id
                            
                            	Unique id for an entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('description', YLeaf(YType.str, 'description')),
                                    ('vendor_type', YLeaf(YType.str, 'vendor-type')),
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('hardware_revision', YLeaf(YType.str, 'hardware-revision')),
                                    ('firmware_revision', YLeaf(YType.str, 'firmware-revision')),
                                    ('software_revision', YLeaf(YType.str, 'software-revision')),
                                    ('chip_hardware_revision', YLeaf(YType.str, 'chip-hardware-revision')),
                                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                                    ('manufacturer_name', YLeaf(YType.str, 'manufacturer-name')),
                                    ('model_name', YLeaf(YType.str, 'model-name')),
                                    ('asset_id_str', YLeaf(YType.str, 'asset-id-str')),
                                    ('asset_identification', YLeaf(YType.int32, 'asset-identification')),
                                    ('is_field_replaceable_unit', YLeaf(YType.boolean, 'is-field-replaceable-unit')),
                                    ('manufacturer_asset_tags', YLeaf(YType.int32, 'manufacturer-asset-tags')),
                                    ('composite_class_code', YLeaf(YType.int32, 'composite-class-code')),
                                    ('memory_size', YLeaf(YType.int32, 'memory-size')),
                                    ('environmental_monitor_path', YLeaf(YType.str, 'environmental-monitor-path')),
                                    ('alias', YLeaf(YType.str, 'alias')),
                                    ('group_flag', YLeaf(YType.boolean, 'group-flag')),
                                    ('new_deviation_number', YLeaf(YType.int32, 'new-deviation-number')),
                                    ('physical_layer_interface_module_type', YLeaf(YType.int32, 'physical-layer-interface-module-type')),
                                    ('unrecognized_fru', YLeaf(YType.boolean, 'unrecognized-fru')),
                                    ('redundancystate', YLeaf(YType.int32, 'redundancystate')),
                                    ('ceport', YLeaf(YType.boolean, 'ceport')),
                                    ('xr_scoped', YLeaf(YType.boolean, 'xr-scoped')),
                                    ('unique_id', YLeaf(YType.int32, 'unique-id')),
                                ])
                                self.description = None
                                self.vendor_type = None
                                self.name = None
                                self.hardware_revision = None
                                self.firmware_revision = None
                                self.software_revision = None
                                self.chip_hardware_revision = None
                                self.serial_number = None
                                self.manufacturer_name = None
                                self.model_name = None
                                self.asset_id_str = None
                                self.asset_identification = None
                                self.is_field_replaceable_unit = None
                                self.manufacturer_asset_tags = None
                                self.composite_class_code = None
                                self.memory_size = None
                                self.environmental_monitor_path = None
                                self.alias = None
                                self.group_flag = None
                                self.new_deviation_number = None
                                self.physical_layer_interface_module_type = None
                                self.unrecognized_fru = None
                                self.redundancystate = None
                                self.ceport = None
                                self.xr_scoped = None
                                self.unique_id = None
                                self._segment_path = lambda: "basic-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo, ['description', 'vendor_type', 'name', 'hardware_revision', 'firmware_revision', 'software_revision', 'chip_hardware_revision', 'serial_number', 'manufacturer_name', 'model_name', 'asset_id_str', 'asset_identification', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'composite_class_code', 'memory_size', 'environmental_monitor_path', 'alias', 'group_flag', 'new_deviation_number', 'physical_layer_interface_module_type', 'unrecognized_fru', 'redundancystate', 'ceport', 'xr_scoped', 'unique_id'], name, value)


                        class FruInfo(Entity):
                            """
                            Field Replaceable Unit (FRU) inventory
                            information
                            
                            .. attribute:: last_operational_state_change
                            
                            	last card oper change state
                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                            
                            .. attribute:: card_up_time
                            
                            	card up time
                            	**type**\:  :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime>`
                            
                            .. attribute:: card_administrative_state
                            
                            	card admin state\: shutdown or not
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: power_administrative_state
                            
                            	power admin state\: up or down
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_operational_state
                            
                            	card operation state
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_monitor_state
                            
                            	card is monitored by a manager or left unmonitored
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_reset_reason
                            
                            	card reset reason enum
                            	**type**\:  :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.CardResetReason>`
                            
                            .. attribute:: power_current_measurement
                            
                            	power current\: not implemented
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: power_operational_state
                            
                            	Power operation state
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo, self).__init__()

                                self.yang_name = "fru-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("card-up-time", ("card_up_time", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('card_administrative_state', YLeaf(YType.int32, 'card-administrative-state')),
                                    ('power_administrative_state', YLeaf(YType.int32, 'power-administrative-state')),
                                    ('card_operational_state', YLeaf(YType.int32, 'card-operational-state')),
                                    ('card_monitor_state', YLeaf(YType.int32, 'card-monitor-state')),
                                    ('card_reset_reason', YLeaf(YType.enumeration, 'card-reset-reason')),
                                    ('power_current_measurement', YLeaf(YType.int32, 'power-current-measurement')),
                                    ('power_operational_state', YLeaf(YType.int32, 'power-operational-state')),
                                ])
                                self.card_administrative_state = None
                                self.power_administrative_state = None
                                self.card_operational_state = None
                                self.card_monitor_state = None
                                self.card_reset_reason = None
                                self.power_current_measurement = None
                                self.power_operational_state = None

                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                self.last_operational_state_change.parent = self
                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                self._children_yang_names.add("last-operational-state-change")

                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime()
                                self.card_up_time.parent = self
                                self._children_name_map["card_up_time"] = "card-up-time"
                                self._children_yang_names.add("card-up-time")
                                self._segment_path = lambda: "fru-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo, ['card_administrative_state', 'power_administrative_state', 'card_operational_state', 'card_monitor_state', 'card_reset_reason', 'power_current_measurement', 'power_operational_state'], name, value)


                            class LastOperationalStateChange(Entity):
                                """
                                last card oper change state
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: second
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: nanosecond
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                    self.yang_name = "last-operational-state-change"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                    ])
                                    self.time_in_seconds = None
                                    self.time_in_nano_seconds = None
                                    self._segment_path = lambda: "last-operational-state-change"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_seconds', 'time_in_nano_seconds'], name, value)


                            class CardUpTime(Entity):
                                """
                                card up time
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: second
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: nanosecond
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                    self.yang_name = "card-up-time"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_in_seconds', YLeaf(YType.int32, 'time-in-seconds')),
                                        ('time_in_nano_seconds', YLeaf(YType.int32, 'time-in-nano-seconds')),
                                    ])
                                    self.time_in_seconds = None
                                    self.time_in_nano_seconds = None
                                    self._segment_path = lambda: "card-up-time"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime, ['time_in_seconds', 'time_in_nano_seconds'], name, value)

    def clone_ptr(self):
        self._top_entity = Inventory()
        return self._top_entity

