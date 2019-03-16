""" Cisco_IOS_XR_asr9k_sc_invmgr_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-invmgr package operational data.

This module contains definitions
for the following management objects\:
  inventory\: Logical Router Inventory operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InvAdminState(Enum):
    """
    InvAdminState (Enum Class)

    Inv admin state

    .. data:: admin_state_invalid = 0

    	admin state invalid

    .. data:: admin_up = 1

    	admin up

    .. data:: admin_down = 2

    	admin down

    """

    admin_state_invalid = Enum.YLeaf(0, "admin-state-invalid")

    admin_up = Enum.YLeaf(1, "admin-up")

    admin_down = Enum.YLeaf(2, "admin-down")


class InvCardState(Enum):
    """
    InvCardState (Enum Class)

    Inv card state

    .. data:: inv_card_not_present = 0

    	inv card not present

    .. data:: inv_card_present = 1

    	inv card present

    .. data:: inv_card_reset = 2

    	inv card reset

    .. data:: inv_card_booting = 3

    	inv card booting

    .. data:: inv_card_mbi_booting = 4

    	inv card mbi booting

    .. data:: inv_card_running_mbi = 5

    	inv card running mbi

    .. data:: inv_card_running_ena = 6

    	inv card running ena

    .. data:: inv_card_bring_down = 7

    	inv card bring down

    .. data:: inv_card_ena_failure = 8

    	inv card ena failure

    .. data:: inv_card_f_diag_run = 9

    	inv card f diag run

    .. data:: inv_card_f_diag_failure = 10

    	inv card f diag failure

    .. data:: inv_card_powered = 11

    	inv card powered

    .. data:: inv_card_unpowered = 12

    	inv card unpowered

    .. data:: inv_card_mdr = 13

    	inv card mdr

    .. data:: inv_card_mdr_running_mbi = 14

    	inv card mdr running mbi

    .. data:: inv_card_main_t_mode = 15

    	inv card main t mode

    .. data:: inv_card_admin_down = 16

    	inv card admin down

    .. data:: inv_card_no_mon = 17

    	inv card no mon

    .. data:: inv_card_unknown = 18

    	inv card unknown

    .. data:: inv_card_failed = 19

    	inv card failed

    .. data:: inv_card_ok = 20

    	inv card ok

    .. data:: inv_card_missing = 21

    	inv card missing

    .. data:: inv_card_field_diag_downloading = 22

    	inv card field diag downloading

    .. data:: inv_card_field_diag_unmonitor = 23

    	inv card field diag unmonitor

    .. data:: inv_card_fabric_field_diag_unmonitor = 24

    	inv card fabric field diag unmonitor

    .. data:: inv_card_field_diag_rp_launching = 25

    	inv card field diag rp launching

    .. data:: inv_card_field_diag_running = 26

    	inv card field diag running

    .. data:: inv_card_field_diag_pass = 27

    	inv card field diag pass

    .. data:: inv_card_field_diag_fail = 28

    	inv card field diag fail

    .. data:: inv_card_field_diag_timeout = 29

    	inv card field diag timeout

    .. data:: inv_card_disabled = 30

    	inv card disabled

    .. data:: inv_card_spa_booting = 31

    	inv card spa booting

    .. data:: inv_card_not_allowed_online = 32

    	inv card not allowed online

    .. data:: inv_card_stopped = 33

    	inv card stopped

    .. data:: inv_card_incompatible_fw_ver = 34

    	inv card incompatible fw ver

    .. data:: inv_card_fpd_hold = 35

    	inv card fpd hold

    .. data:: inv_card_node_prep = 36

    	inv card node prep

    .. data:: inv_card_updating_fpd = 37

    	inv card updating fpd

    .. data:: inv_card_num_states = 38

    	inv card num states

    """

    inv_card_not_present = Enum.YLeaf(0, "inv-card-not-present")

    inv_card_present = Enum.YLeaf(1, "inv-card-present")

    inv_card_reset = Enum.YLeaf(2, "inv-card-reset")

    inv_card_booting = Enum.YLeaf(3, "inv-card-booting")

    inv_card_mbi_booting = Enum.YLeaf(4, "inv-card-mbi-booting")

    inv_card_running_mbi = Enum.YLeaf(5, "inv-card-running-mbi")

    inv_card_running_ena = Enum.YLeaf(6, "inv-card-running-ena")

    inv_card_bring_down = Enum.YLeaf(7, "inv-card-bring-down")

    inv_card_ena_failure = Enum.YLeaf(8, "inv-card-ena-failure")

    inv_card_f_diag_run = Enum.YLeaf(9, "inv-card-f-diag-run")

    inv_card_f_diag_failure = Enum.YLeaf(10, "inv-card-f-diag-failure")

    inv_card_powered = Enum.YLeaf(11, "inv-card-powered")

    inv_card_unpowered = Enum.YLeaf(12, "inv-card-unpowered")

    inv_card_mdr = Enum.YLeaf(13, "inv-card-mdr")

    inv_card_mdr_running_mbi = Enum.YLeaf(14, "inv-card-mdr-running-mbi")

    inv_card_main_t_mode = Enum.YLeaf(15, "inv-card-main-t-mode")

    inv_card_admin_down = Enum.YLeaf(16, "inv-card-admin-down")

    inv_card_no_mon = Enum.YLeaf(17, "inv-card-no-mon")

    inv_card_unknown = Enum.YLeaf(18, "inv-card-unknown")

    inv_card_failed = Enum.YLeaf(19, "inv-card-failed")

    inv_card_ok = Enum.YLeaf(20, "inv-card-ok")

    inv_card_missing = Enum.YLeaf(21, "inv-card-missing")

    inv_card_field_diag_downloading = Enum.YLeaf(22, "inv-card-field-diag-downloading")

    inv_card_field_diag_unmonitor = Enum.YLeaf(23, "inv-card-field-diag-unmonitor")

    inv_card_fabric_field_diag_unmonitor = Enum.YLeaf(24, "inv-card-fabric-field-diag-unmonitor")

    inv_card_field_diag_rp_launching = Enum.YLeaf(25, "inv-card-field-diag-rp-launching")

    inv_card_field_diag_running = Enum.YLeaf(26, "inv-card-field-diag-running")

    inv_card_field_diag_pass = Enum.YLeaf(27, "inv-card-field-diag-pass")

    inv_card_field_diag_fail = Enum.YLeaf(28, "inv-card-field-diag-fail")

    inv_card_field_diag_timeout = Enum.YLeaf(29, "inv-card-field-diag-timeout")

    inv_card_disabled = Enum.YLeaf(30, "inv-card-disabled")

    inv_card_spa_booting = Enum.YLeaf(31, "inv-card-spa-booting")

    inv_card_not_allowed_online = Enum.YLeaf(32, "inv-card-not-allowed-online")

    inv_card_stopped = Enum.YLeaf(33, "inv-card-stopped")

    inv_card_incompatible_fw_ver = Enum.YLeaf(34, "inv-card-incompatible-fw-ver")

    inv_card_fpd_hold = Enum.YLeaf(35, "inv-card-fpd-hold")

    inv_card_node_prep = Enum.YLeaf(36, "inv-card-node-prep")

    inv_card_updating_fpd = Enum.YLeaf(37, "inv-card-updating-fpd")

    inv_card_num_states = Enum.YLeaf(38, "inv-card-num-states")


class InvMonitorState(Enum):
    """
    InvMonitorState (Enum Class)

    Inv monitor state

    .. data:: unmonitored = 0

    	unmonitored

    .. data:: monitored = 1

    	monitored

    """

    unmonitored = Enum.YLeaf(0, "unmonitored")

    monitored = Enum.YLeaf(1, "monitored")


class InvPowerAdminState(Enum):
    """
    InvPowerAdminState (Enum Class)

    Inv power admin state

    .. data:: admin_power_invalid = 0

    	admin power invalid

    .. data:: admin_on = 2

    	admin on

    .. data:: admin_off = 3

    	admin off

    """

    admin_power_invalid = Enum.YLeaf(0, "admin-power-invalid")

    admin_on = Enum.YLeaf(2, "admin-on")

    admin_off = Enum.YLeaf(3, "admin-off")


class InvResetReason(Enum):
    """
    InvResetReason (Enum Class)

    Inv reset reason

    .. data:: module_reset_reason_unknown = 0

    	module reset reason unknown

    .. data:: module_reset_reason_powerup = 1

    	module reset reason powerup

    .. data:: module_reset_reason_user_shutdown = 2

    	module reset reason user shutdown

    .. data:: module_reset_reason_user_reload = 3

    	module reset reason user reload

    .. data:: module_reset_reason_auto_reload = 4

    	module reset reason auto reload

    .. data:: module_reset_reason_environment = 5

    	module reset reason environment

    .. data:: module_reset_reason_user_unpower = 6

    	module reset reason user unpower

    """

    module_reset_reason_unknown = Enum.YLeaf(0, "module-reset-reason-unknown")

    module_reset_reason_powerup = Enum.YLeaf(1, "module-reset-reason-powerup")

    module_reset_reason_user_shutdown = Enum.YLeaf(2, "module-reset-reason-user-shutdown")

    module_reset_reason_user_reload = Enum.YLeaf(3, "module-reset-reason-user-reload")

    module_reset_reason_auto_reload = Enum.YLeaf(4, "module-reset-reason-auto-reload")

    module_reset_reason_environment = Enum.YLeaf(5, "module-reset-reason-environment")

    module_reset_reason_user_unpower = Enum.YLeaf(6, "module-reset-reason-user-unpower")



class Inventory(Entity):
    """
    Logical Router Inventory operational data
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks>`
    
    	**config**\: False
    
    

    """

    _prefix = 'asr9k-sc-invmgr-oper'
    _revision = '2018-06-28'

    def __init__(self):
        super(Inventory, self).__init__()
        self._top_entity = None

        self.yang_name = "inventory"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-invmgr-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("racks", ("racks", Inventory.Racks))])
        self._leafs = OrderedDict()

        self.racks = Inventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-oper:inventory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Inventory, [], name, value)


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack number
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack>`
        
        	**config**\: False
        
        

        """

        _prefix = 'asr9k-sc-invmgr-oper'
        _revision = '2018-06-28'

        def __init__(self):
            super(Inventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", Inventory.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-oper:inventory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Racks, [], name, value)


        class Rack(Entity):
            """
            Rack number
            
            .. attribute:: number  (key)
            
            	Rack number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: slots
            
            	Slot table contains all slots in the rack
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots>`
            
            	**config**\: False
            
            

            """

            _prefix = 'asr9k-sc-invmgr-oper'
            _revision = '2018-06-28'

            def __init__(self):
                super(Inventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['number']
                self._child_classes = OrderedDict([("slots", ("slots", Inventory.Racks.Rack.Slots))])
                self._leafs = OrderedDict([
                    ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                ])
                self.number = None

                self.slots = Inventory.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._segment_path = lambda: "rack" + "[number='" + str(self.number) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-oper:inventory/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Inventory.Racks.Rack, ['number'], name, value)


            class Slots(Entity):
                """
                Slot table contains all slots in the rack
                
                .. attribute:: slot
                
                	Slot number
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot>`
                
                	**config**\: False
                
                

                """

                _prefix = 'asr9k-sc-invmgr-oper'
                _revision = '2018-06-28'

                def __init__(self):
                    super(Inventory.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot", ("slot", Inventory.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Inventory.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Slot number
                    
                    .. attribute:: number  (key)
                    
                    	Slot number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: cards
                    
                    	Card table contains all cards in the slot
                    	**type**\:  :py:class:`Cards <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards>`
                    
                    	**config**\: False
                    
                    .. attribute:: basic_attributes
                    
                    	Attributes
                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-oper'
                    _revision = '2018-06-28'

                    def __init__(self):
                        super(Inventory.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['number']
                        self._child_classes = OrderedDict([("cards", ("cards", Inventory.Racks.Rack.Slots.Slot.Cards)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.BasicAttributes))])
                        self._leafs = OrderedDict([
                            ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                        ])
                        self.number = None

                        self.cards = Inventory.Racks.Rack.Slots.Slot.Cards()
                        self.cards.parent = self
                        self._children_name_map["cards"] = "cards"

                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.BasicAttributes()
                        self.basic_attributes.parent = self
                        self._children_name_map["basic_attributes"] = "basic-attributes"
                        self._segment_path = lambda: "slot" + "[number='" + str(self.number) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot, ['number'], name, value)


                    class Cards(Entity):
                        """
                        Card table contains all cards in the slot
                        
                        .. attribute:: card
                        
                        	Card number
                        	**type**\: list of  		 :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-oper'
                        _revision = '2018-06-28'

                        def __init__(self):
                            super(Inventory.Racks.Rack.Slots.Slot.Cards, self).__init__()

                            self.yang_name = "cards"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("card", ("card", Inventory.Racks.Rack.Slots.Slot.Cards.Card))])
                            self._leafs = OrderedDict()

                            self.card = YList(self)
                            self._segment_path = lambda: "cards"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards, [], name, value)


                        class Card(Entity):
                            """
                            Card number
                            
                            .. attribute:: number  (key)
                            
                            	card number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: sub_slots
                            
                            	SubSlotTable contains all subslots in a Slot
                            	**type**\:  :py:class:`SubSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots>`
                            
                            	**config**\: False
                            
                            .. attribute:: hw_components
                            
                            	HWComponent table contains all HW modules within the card 
                            	**type**\:  :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents>`
                            
                            	**config**\: False
                            
                            .. attribute:: sensors
                            
                            	ModuleSensorTable contains all sensors in a Module
                            	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors>`
                            
                            	**config**\: False
                            
                            .. attribute:: port_slots
                            
                            	PortSlotTable contains all optics ports in a SPA/PLIM
                            	**type**\:  :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots>`
                            
                            	**config**\: False
                            
                            .. attribute:: basic_attributes
                            
                            	Attributes
                            	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-oper'
                            _revision = '2018-06-28'

                            def __init__(self):
                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card, self).__init__()

                                self.yang_name = "card"
                                self.yang_parent_name = "cards"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['number']
                                self._child_classes = OrderedDict([("sub-slots", ("sub_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots)), ("hw-components", ("hw_components", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents)), ("sensors", ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors)), ("port-slots", ("port_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes))])
                                self._leafs = OrderedDict([
                                    ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                ])
                                self.number = None

                                self.sub_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots()
                                self.sub_slots.parent = self
                                self._children_name_map["sub_slots"] = "sub-slots"

                                self.hw_components = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents()
                                self.hw_components.parent = self
                                self._children_name_map["hw_components"] = "hw-components"

                                self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors()
                                self.sensors.parent = self
                                self._children_name_map["sensors"] = "sensors"

                                self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots()
                                self.port_slots.parent = self
                                self._children_name_map["port_slots"] = "port-slots"

                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes()
                                self.basic_attributes.parent = self
                                self._children_name_map["basic_attributes"] = "basic-attributes"
                                self._segment_path = lambda: "card" + "[number='" + str(self.number) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card, ['number'], name, value)


                            class SubSlots(Entity):
                                """
                                SubSlotTable contains all subslots in a
                                Slot
                                
                                .. attribute:: sub_slot
                                
                                	SubSlot number
                                	**type**\: list of  		 :py:class:`SubSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, self).__init__()

                                    self.yang_name = "sub-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sub-slot", ("sub_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot))])
                                    self._leafs = OrderedDict()

                                    self.sub_slot = YList(self)
                                    self._segment_path = lambda: "sub-slots"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, [], name, value)


                                class SubSlot(Entity):
                                    """
                                    SubSlot number
                                    
                                    .. attribute:: number  (key)
                                    
                                    	subslot number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module
                                    
                                    	Module string
                                    	**type**\:  :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2018-06-28'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, self).__init__()

                                        self.yang_name = "sub-slot"
                                        self.yang_parent_name = "sub-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_classes = OrderedDict([("module", ("module", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes))])
                                        self._leafs = OrderedDict([
                                            ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                        ])
                                        self.number = None

                                        self.module = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module()
                                        self.module.parent = self
                                        self._children_name_map["module"] = "module"

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._segment_path = lambda: "sub-slot" + "[number='" + str(self.number) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, ['number'], name, value)


                                    class Module(Entity):
                                        """
                                        Module string
                                        
                                        .. attribute:: sensors
                                        
                                        	ModuleSensorTable contains all sensors in a Module
                                        	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: port_slots
                                        
                                        	PortSlotTable contains all optics ports in a SPA/PLIM
                                        	**type**\:  :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module, self).__init__()

                                            self.yang_name = "module"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensors", ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors)), ("port-slots", ("port_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes))])
                                            self._leafs = OrderedDict()

                                            self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors()
                                            self.sensors.parent = self
                                            self._children_name_map["sensors"] = "sensors"

                                            self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots()
                                            self.port_slots.parent = self
                                            self._children_name_map["port_slots"] = "port-slots"

                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes()
                                            self.basic_attributes.parent = self
                                            self._children_name_map["basic_attributes"] = "basic-attributes"
                                            self._segment_path = lambda: "module"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module, [], name, value)


                                        class Sensors(Entity):
                                            """
                                            ModuleSensorTable contains all sensors in a
                                            Module.
                                            
                                            .. attribute:: sensor
                                            
                                            	Sensor number in the Module
                                            	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, self).__init__()

                                                self.yang_name = "sensors"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("sensor", ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor))])
                                                self._leafs = OrderedDict()

                                                self.sensor = YList(self)
                                                self._segment_path = lambda: "sensors"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, [], name, value)


                                            class Sensor(Entity):
                                                """
                                                Sensor number in the Module
                                                
                                                .. attribute:: number  (key)
                                                
                                                	sensor number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: basic_attributes
                                                
                                                	Attributes
                                                	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, self).__init__()

                                                    self.yang_name = "sensor"
                                                    self.yang_parent_name = "sensors"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['number']
                                                    self._child_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes))])
                                                    self._leafs = OrderedDict([
                                                        ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                                    ])
                                                    self.number = None

                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self._children_name_map["basic_attributes"] = "basic-attributes"
                                                    self._segment_path = lambda: "sensor" + "[number='" + str(self.number) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, ['number'], name, value)


                                                class BasicAttributes(Entity):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Inventory information
                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) inventory information
                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes, self).__init__()

                                                        self.yang_name = "basic-attributes"
                                                        self.yang_parent_name = "sensor"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo))])
                                                        self._leafs = OrderedDict()

                                                        self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self._children_name_map["basic_info"] = "basic-info"

                                                        self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo()
                                                        self.fru_info.parent = self
                                                        self._children_name_map["fru_info"] = "fru-info"
                                                        self._segment_path = lambda: "basic-attributes"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes, [], name, value)


                                                    class BasicInfo(Entity):
                                                        """
                                                        Inventory information
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms       what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: chip_hardware_revision
                                                        
                                                        	chip module hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: manufacturer_name
                                                        
                                                        	manufacturer's name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: asset_id_str
                                                        
                                                        	asset Identification string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: asset_identification
                                                        
                                                        	asset Identification
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: manufacturer_asset_tags
                                                        
                                                        	Manufacture Asset Tags
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: composite_class_code
                                                        
                                                        	Major&minor class of the entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: memory_size
                                                        
                                                        	Size of memory associated with       the entity where applicable
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: environmental_monitor_path
                                                        
                                                        	sysdb name of sensor in the envmon EDM
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: alias
                                                        
                                                        	useful for storing an entity alias 
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: group_flag
                                                        
                                                        	indicates if this entity is group       or not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: new_deviation_number
                                                        
                                                        	integer value for New Deviation Number 0x88
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: physical_layer_interface_module_type
                                                        
                                                        	integer value for plim type if     applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unrecognized_fru
                                                        
                                                        	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: redundancystate
                                                        
                                                        	integer value for Redundancy State if applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: ceport
                                                        
                                                        	1 if ce port found, 0 if not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: xr_scoped
                                                        
                                                        	1 if xr scoped, 0 if not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unique_id
                                                        
                                                        	Unique id for an entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                                ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                                ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                                ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                                ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                                ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                                ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                                ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                                ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                                ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                                ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                                ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                                ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                                ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                                ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                                ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                                    class FruInfo(Entity):
                                                        """
                                                        Field Replaceable Unit (FRU) inventory
                                                        information
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	Time operational state is   last changed
                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_up_time
                                                        
                                                        	Module up time
                                                        	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_administrative_state
                                                        
                                                        	Administrative    state
                                                        	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_power_administrative_state
                                                        
                                                        	Power administrative state
                                                        	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_operational_state
                                                        
                                                        	Operation state
                                                        	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_monitor_state
                                                        
                                                        	Monitor state
                                                        	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_reset_reason
                                                        
                                                        	Reset reason
                                                        	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime))])
                                                            self._leafs = OrderedDict([
                                                                ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                                ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                                ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                                ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                                ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                            ])
                                                            self.module_administrative_state = None
                                                            self.module_power_administrative_state = None
                                                            self.module_operational_state = None
                                                            self.module_monitor_state = None
                                                            self.module_reset_reason = None

                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                            self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime()
                                                            self.module_up_time.parent = self
                                                            self._children_name_map["module_up_time"] = "module-up-time"
                                                            self._segment_path = lambda: "fru-info"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                        class LastOperationalStateChange(Entity):
                                                            """
                                                            Time operational state is   last changed
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2018-06-28'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "last-operational-state-change"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                                        class ModuleUpTime(Entity):
                                                            """
                                                            Module up time
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2018-06-28'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                                self.yang_name = "module-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "module-up-time"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                                        class PortSlots(Entity):
                                            """
                                            PortSlotTable contains all optics ports in a
                                            SPA/PLIM.
                                            
                                            .. attribute:: port_slot
                                            
                                            	PortSlot number in the SPA/PLIM
                                            	**type**\: list of  		 :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, self).__init__()

                                                self.yang_name = "port-slots"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("port-slot", ("port_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot))])
                                                self._leafs = OrderedDict()

                                                self.port_slot = YList(self)
                                                self._segment_path = lambda: "port-slots"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, [], name, value)


                                            class PortSlot(Entity):
                                                """
                                                PortSlot number in the SPA/PLIM
                                                
                                                .. attribute:: number  (key)
                                                
                                                	portslot number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: port
                                                
                                                	Port string
                                                	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: basic_attributes
                                                
                                                	Attributes
                                                	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, self).__init__()

                                                    self.yang_name = "port-slot"
                                                    self.yang_parent_name = "port-slots"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['number']
                                                    self._child_classes = OrderedDict([("port", ("port", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes))])
                                                    self._leafs = OrderedDict([
                                                        ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                                    ])
                                                    self.number = None

                                                    self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port()
                                                    self.port.parent = self
                                                    self._children_name_map["port"] = "port"

                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self._children_name_map["basic_attributes"] = "basic-attributes"
                                                    self._segment_path = lambda: "port-slot" + "[number='" + str(self.number) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, ['number'], name, value)


                                                class Port(Entity):
                                                    """
                                                    Port string
                                                    
                                                    .. attribute:: basic_attributes
                                                    
                                                    	Attributes
                                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port, self).__init__()

                                                        self.yang_name = "port"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes))])
                                                        self._leafs = OrderedDict()

                                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes()
                                                        self.basic_attributes.parent = self
                                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                                        self._segment_path = lambda: "port"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port, [], name, value)


                                                    class BasicAttributes(Entity):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Inventory information
                                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) inventory information
                                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes, self).__init__()

                                                            self.yang_name = "basic-attributes"
                                                            self.yang_parent_name = "port"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo))])
                                                            self._leafs = OrderedDict()

                                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self._children_name_map["basic_info"] = "basic-info"

                                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo()
                                                            self.fru_info.parent = self
                                                            self._children_name_map["fru_info"] = "fru-info"
                                                            self._segment_path = lambda: "basic-attributes"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes, [], name, value)


                                                        class BasicInfo(Entity):
                                                            """
                                                            Inventory information
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms       what the entity in question does
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: chip_hardware_revision
                                                            
                                                            	chip module hw revision string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: manufacturer_name
                                                            
                                                            	manufacturer's name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: asset_id_str
                                                            
                                                            	asset Identification string
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: asset_identification
                                                            
                                                            	asset Identification
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\: bool
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: manufacturer_asset_tags
                                                            
                                                            	Manufacture Asset Tags
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: composite_class_code
                                                            
                                                            	Major&minor class of the entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: memory_size
                                                            
                                                            	Size of memory associated with       the entity where applicable
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: environmental_monitor_path
                                                            
                                                            	sysdb name of sensor in the envmon EDM
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: alias
                                                            
                                                            	useful for storing an entity alias 
                                                            	**type**\: str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: group_flag
                                                            
                                                            	indicates if this entity is group       or not
                                                            	**type**\: bool
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: new_deviation_number
                                                            
                                                            	integer value for New Deviation Number 0x88
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: physical_layer_interface_module_type
                                                            
                                                            	integer value for plim type if     applicable to this entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: unrecognized_fru
                                                            
                                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                            	**type**\: bool
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: redundancystate
                                                            
                                                            	integer value for Redundancy State if applicable to this entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: ceport
                                                            
                                                            	1 if ce port found, 0 if not
                                                            	**type**\: bool
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: xr_scoped
                                                            
                                                            	1 if xr scoped, 0 if not
                                                            	**type**\: bool
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: unique_id
                                                            
                                                            	Unique id for an entity
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2018-06-28'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, self).__init__()

                                                                self.yang_name = "basic-info"
                                                                self.yang_parent_name = "basic-attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                    ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                    ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                    ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                                    ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                    ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                                    ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                                    ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                                    ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                                    ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                                    ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                                    ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                                    ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                                    ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                                    ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                                    ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                                    ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                                    ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                                        class FruInfo(Entity):
                                                            """
                                                            Field Replaceable Unit (FRU) inventory
                                                            information
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	Time operational state is   last changed
                                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: module_up_time
                                                            
                                                            	Module up time
                                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime>`
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: module_administrative_state
                                                            
                                                            	Administrative    state
                                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: module_power_administrative_state
                                                            
                                                            	Power administrative state
                                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: module_operational_state
                                                            
                                                            	Operation state
                                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: module_monitor_state
                                                            
                                                            	Monitor state
                                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                                            
                                                            	**config**\: False
                                                            
                                                            .. attribute:: module_reset_reason
                                                            
                                                            	Reset reason
                                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                                            
                                                            	**config**\: False
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2018-06-28'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, self).__init__()

                                                                self.yang_name = "fru-info"
                                                                self.yang_parent_name = "basic-attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime))])
                                                                self._leafs = OrderedDict([
                                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                                ])
                                                                self.module_administrative_state = None
                                                                self.module_power_administrative_state = None
                                                                self.module_operational_state = None
                                                                self.module_monitor_state = None
                                                                self.module_reset_reason = None

                                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                                self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime()
                                                                self.module_up_time.parent = self
                                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                                self._segment_path = lambda: "fru-info"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                            class LastOperationalStateChange(Entity):
                                                                """
                                                                Time operational state is   last changed
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**config**\: False
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**config**\: False
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                                _revision = '2018-06-28'

                                                                def __init__(self):
                                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                    self.yang_name = "last-operational-state-change"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "last-operational-state-change"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                                            class ModuleUpTime(Entity):
                                                                """
                                                                Module up time
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**config**\: False
                                                                
                                                                	**units**\: second
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\: int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**config**\: False
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                

                                                                """

                                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                                _revision = '2018-06-28'

                                                                def __init__(self):
                                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                                    self.yang_name = "module-up-time"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self.ylist_key_names = []
                                                                    self._child_classes = OrderedDict([])
                                                                    self._leafs = OrderedDict([
                                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                    ])
                                                                    self.time_in_seconds = None
                                                                    self.time_in_nano_seconds = None
                                                                    self._segment_path = lambda: "module-up-time"
                                                                    self._is_frozen = True

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)






                                                class BasicAttributes(Entity):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Inventory information
                                                    	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) inventory information
                                                    	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes, self).__init__()

                                                        self.yang_name = "basic-attributes"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo))])
                                                        self._leafs = OrderedDict()

                                                        self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self._children_name_map["basic_info"] = "basic-info"

                                                        self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo()
                                                        self.fru_info.parent = self
                                                        self._children_name_map["fru_info"] = "fru-info"
                                                        self._segment_path = lambda: "basic-attributes"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes, [], name, value)


                                                    class BasicInfo(Entity):
                                                        """
                                                        Inventory information
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms       what the entity in question does
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: chip_hardware_revision
                                                        
                                                        	chip module hw revision string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: manufacturer_name
                                                        
                                                        	manufacturer's name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: asset_id_str
                                                        
                                                        	asset Identification string
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: asset_identification
                                                        
                                                        	asset Identification
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: manufacturer_asset_tags
                                                        
                                                        	Manufacture Asset Tags
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: composite_class_code
                                                        
                                                        	Major&minor class of the entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: memory_size
                                                        
                                                        	Size of memory associated with       the entity where applicable
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: environmental_monitor_path
                                                        
                                                        	sysdb name of sensor in the envmon EDM
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: alias
                                                        
                                                        	useful for storing an entity alias 
                                                        	**type**\: str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: group_flag
                                                        
                                                        	indicates if this entity is group       or not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: new_deviation_number
                                                        
                                                        	integer value for New Deviation Number 0x88
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: physical_layer_interface_module_type
                                                        
                                                        	integer value for plim type if     applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unrecognized_fru
                                                        
                                                        	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: redundancystate
                                                        
                                                        	integer value for Redundancy State if applicable to this entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: ceport
                                                        
                                                        	1 if ce port found, 0 if not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: xr_scoped
                                                        
                                                        	1 if xr scoped, 0 if not
                                                        	**type**\: bool
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: unique_id
                                                        
                                                        	Unique id for an entity
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                                ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                                ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                                ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                                ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                                ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                                ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                                ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                                ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                                ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                                ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                                ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                                ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                                ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                                ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                                ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                                ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                                ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                                ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                                ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                                ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                                ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                                ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                                ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                                ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                                    class FruInfo(Entity):
                                                        """
                                                        Field Replaceable Unit (FRU) inventory
                                                        information
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	Time operational state is   last changed
                                                        	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_up_time
                                                        
                                                        	Module up time
                                                        	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_administrative_state
                                                        
                                                        	Administrative    state
                                                        	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_power_administrative_state
                                                        
                                                        	Power administrative state
                                                        	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_operational_state
                                                        
                                                        	Operation state
                                                        	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_monitor_state
                                                        
                                                        	Monitor state
                                                        	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                                        
                                                        	**config**\: False
                                                        
                                                        .. attribute:: module_reset_reason
                                                        
                                                        	Reset reason
                                                        	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                                        
                                                        	**config**\: False
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime))])
                                                            self._leafs = OrderedDict([
                                                                ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                                ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                                ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                                ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                                ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                            ])
                                                            self.module_administrative_state = None
                                                            self.module_power_administrative_state = None
                                                            self.module_operational_state = None
                                                            self.module_monitor_state = None
                                                            self.module_reset_reason = None

                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                            self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime()
                                                            self.module_up_time.parent = self
                                                            self._children_name_map["module_up_time"] = "module-up-time"
                                                            self._segment_path = lambda: "fru-info"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                        class LastOperationalStateChange(Entity):
                                                            """
                                                            Time operational state is   last changed
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2018-06-28'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "last-operational-state-change"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                                        class ModuleUpTime(Entity):
                                                            """
                                                            Module up time
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: second
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\: int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**config**\: False
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-oper'
                                                            _revision = '2018-06-28'

                                                            def __init__(self):
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                                self.yang_name = "module-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self.ylist_key_names = []
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                    ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                                ])
                                                                self.time_in_seconds = None
                                                                self.time_in_nano_seconds = None
                                                                self._segment_path = lambda: "module-up-time"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                                        class BasicAttributes(Entity):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Inventory information
                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes, self).__init__()

                                                self.yang_name = "basic-attributes"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo))])
                                                self._leafs = OrderedDict()

                                                self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self._children_name_map["basic_info"] = "basic-info"

                                                self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo()
                                                self.fru_info.parent = self
                                                self._children_name_map["fru_info"] = "fru-info"
                                                self._segment_path = lambda: "basic-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes, [], name, value)


                                            class BasicInfo(Entity):
                                                """
                                                Inventory information
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms       what the entity in question does
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: chip_hardware_revision
                                                
                                                	chip module hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: manufacturer_name
                                                
                                                	manufacturer's name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: asset_id_str
                                                
                                                	asset Identification string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: asset_identification
                                                
                                                	asset Identification
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: manufacturer_asset_tags
                                                
                                                	Manufacture Asset Tags
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: composite_class_code
                                                
                                                	Major&minor class of the entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: memory_size
                                                
                                                	Size of memory associated with       the entity where applicable
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: environmental_monitor_path
                                                
                                                	sysdb name of sensor in the envmon EDM
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: alias
                                                
                                                	useful for storing an entity alias 
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: group_flag
                                                
                                                	indicates if this entity is group       or not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: new_deviation_number
                                                
                                                	integer value for New Deviation Number 0x88
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: physical_layer_interface_module_type
                                                
                                                	integer value for plim type if     applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unrecognized_fru
                                                
                                                	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: redundancystate
                                                
                                                	integer value for Redundancy State if applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ceport
                                                
                                                	1 if ce port found, 0 if not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: xr_scoped
                                                
                                                	1 if xr scoped, 0 if not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unique_id
                                                
                                                	Unique id for an entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                        ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                        ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                        ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                        ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                        ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                        ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                        ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                        ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                        ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                        ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                        ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                        ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                        ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                        ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                        ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                        ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                        ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                        ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                        ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                        ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                        ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                        ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                            class FruInfo(Entity):
                                                """
                                                Field Replaceable Unit (FRU) inventory
                                                information
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	Time operational state is   last changed
                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_up_time
                                                
                                                	Module up time
                                                	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.ModuleUpTime>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_administrative_state
                                                
                                                	Administrative    state
                                                	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_power_administrative_state
                                                
                                                	Power administrative state
                                                	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_operational_state
                                                
                                                	Operation state
                                                	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_monitor_state
                                                
                                                	Monitor state
                                                	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_reset_reason
                                                
                                                	Reset reason
                                                	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.ModuleUpTime))])
                                                    self._leafs = OrderedDict([
                                                        ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                        ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                        ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                        ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                        ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                    ])
                                                    self.module_administrative_state = None
                                                    self.module_power_administrative_state = None
                                                    self.module_operational_state = None
                                                    self.module_monitor_state = None
                                                    self.module_reset_reason = None

                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                    self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.ModuleUpTime()
                                                    self.module_up_time.parent = self
                                                    self._children_name_map["module_up_time"] = "module-up-time"
                                                    self._segment_path = lambda: "fru-info"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                class LastOperationalStateChange(Entity):
                                                    """
                                                    Time operational state is   last changed
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "last-operational-state-change"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                                class ModuleUpTime(Entity):
                                                    """
                                                    Module up time
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                        self.yang_name = "module-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "module-up-time"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)






                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "basic-attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                    ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                    ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                    ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                    ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                    ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                    ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                    ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                    ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                    ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                    ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                    ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                    ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                    ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                    ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.ModuleUpTime>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                            class HwComponents(Entity):
                                """
                                HWComponent table contains all HW modules
                                within the card 
                                
                                .. attribute:: hw_component
                                
                                	HWComponent number
                                	**type**\: list of  		 :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, self).__init__()

                                    self.yang_name = "hw-components"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("hw-component", ("hw_component", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent))])
                                    self._leafs = OrderedDict()

                                    self.hw_component = YList(self)
                                    self._segment_path = lambda: "hw-components"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, [], name, value)


                                class HwComponent(Entity):
                                    """
                                    HWComponent number
                                    
                                    .. attribute:: number  (key)
                                    
                                    	node number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sensors
                                    
                                    	ModuleSensorTable contains all sensors in a Module
                                    	**type**\:  :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2018-06-28'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, self).__init__()

                                        self.yang_name = "hw-component"
                                        self.yang_parent_name = "hw-components"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_classes = OrderedDict([("sensors", ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes))])
                                        self._leafs = OrderedDict([
                                            ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                        ])
                                        self.number = None

                                        self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors()
                                        self.sensors.parent = self
                                        self._children_name_map["sensors"] = "sensors"

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._segment_path = lambda: "hw-component" + "[number='" + str(self.number) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, ['number'], name, value)


                                    class Sensors(Entity):
                                        """
                                        ModuleSensorTable contains all sensors in a
                                        Module.
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number in the Module
                                        	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, self).__init__()

                                            self.yang_name = "sensors"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("sensor", ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor))])
                                            self._leafs = OrderedDict()

                                            self.sensor = YList(self)
                                            self._segment_path = lambda: "sensors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, [], name, value)


                                        class Sensor(Entity):
                                            """
                                            Sensor number in the Module
                                            
                                            .. attribute:: number  (key)
                                            
                                            	sensor number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: basic_attributes
                                            
                                            	Attributes
                                            	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                self.yang_name = "sensor"
                                                self.yang_parent_name = "sensors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['number']
                                                self._child_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes))])
                                                self._leafs = OrderedDict([
                                                    ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                                ])
                                                self.number = None

                                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes()
                                                self.basic_attributes.parent = self
                                                self._children_name_map["basic_attributes"] = "basic-attributes"
                                                self._segment_path = lambda: "sensor" + "[number='" + str(self.number) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, ['number'], name, value)


                                            class BasicAttributes(Entity):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Inventory information
                                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) inventory information
                                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes, self).__init__()

                                                    self.yang_name = "basic-attributes"
                                                    self.yang_parent_name = "sensor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo))])
                                                    self._leafs = OrderedDict()

                                                    self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self._children_name_map["basic_info"] = "basic-info"

                                                    self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo()
                                                    self.fru_info.parent = self
                                                    self._children_name_map["fru_info"] = "fru-info"
                                                    self._segment_path = lambda: "basic-attributes"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes, [], name, value)


                                                class BasicInfo(Entity):
                                                    """
                                                    Inventory information
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms       what the entity in question does
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: chip_hardware_revision
                                                    
                                                    	chip module hw revision string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: manufacturer_name
                                                    
                                                    	manufacturer's name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asset_id_str
                                                    
                                                    	asset Identification string
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: asset_identification
                                                    
                                                    	asset Identification
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: manufacturer_asset_tags
                                                    
                                                    	Manufacture Asset Tags
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: composite_class_code
                                                    
                                                    	Major&minor class of the entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: memory_size
                                                    
                                                    	Size of memory associated with       the entity where applicable
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: environmental_monitor_path
                                                    
                                                    	sysdb name of sensor in the envmon EDM
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: alias
                                                    
                                                    	useful for storing an entity alias 
                                                    	**type**\: str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: group_flag
                                                    
                                                    	indicates if this entity is group       or not
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: new_deviation_number
                                                    
                                                    	integer value for New Deviation Number 0x88
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: physical_layer_interface_module_type
                                                    
                                                    	integer value for plim type if     applicable to this entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: unrecognized_fru
                                                    
                                                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: redundancystate
                                                    
                                                    	integer value for Redundancy State if applicable to this entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: ceport
                                                    
                                                    	1 if ce port found, 0 if not
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: xr_scoped
                                                    
                                                    	1 if xr scoped, 0 if not
                                                    	**type**\: bool
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: unique_id
                                                    
                                                    	Unique id for an entity
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "basic-attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                            ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                            ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                            ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                            ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                            ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                            ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                            ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                            ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                            ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                            ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                            ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                            ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                            ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                            ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                            ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                            ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                            ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                                class FruInfo(Entity):
                                                    """
                                                    Field Replaceable Unit (FRU) inventory
                                                    information
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	Time operational state is   last changed
                                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: module_up_time
                                                    
                                                    	Module up time
                                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: module_administrative_state
                                                    
                                                    	Administrative    state
                                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: module_power_administrative_state
                                                    
                                                    	Power administrative state
                                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: module_operational_state
                                                    
                                                    	Operation state
                                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: module_monitor_state
                                                    
                                                    	Monitor state
                                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                                    
                                                    	**config**\: False
                                                    
                                                    .. attribute:: module_reset_reason
                                                    
                                                    	Reset reason
                                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                                    
                                                    	**config**\: False
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "basic-attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime))])
                                                        self._leafs = OrderedDict([
                                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                        ])
                                                        self.module_administrative_state = None
                                                        self.module_power_administrative_state = None
                                                        self.module_operational_state = None
                                                        self.module_monitor_state = None
                                                        self.module_reset_reason = None

                                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                        self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime()
                                                        self.module_up_time.parent = self
                                                        self._children_name_map["module_up_time"] = "module-up-time"
                                                        self._segment_path = lambda: "fru-info"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                    class LastOperationalStateChange(Entity):
                                                        """
                                                        Time operational state is   last changed
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "last-operational-state-change"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                                    class ModuleUpTime(Entity):
                                                        """
                                                        Module up time
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        	**units**\: second
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\: int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**config**\: False
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-oper'
                                                        _revision = '2018-06-28'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                            self.yang_name = "module-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                            ])
                                                            self.time_in_seconds = None
                                                            self.time_in_nano_seconds = None
                                                            self._segment_path = lambda: "module-up-time"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "basic-attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                    ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                    ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                    ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                    ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                    ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                    ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                    ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                    ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                    ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                    ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                    ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                    ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                    ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                    ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.ModuleUpTime>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                            class Sensors(Entity):
                                """
                                ModuleSensorTable contains all sensors in a
                                Module.
                                
                                .. attribute:: sensor
                                
                                	Sensor number in the Module
                                	**type**\: list of  		 :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, self).__init__()

                                    self.yang_name = "sensors"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sensor", ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor))])
                                    self._leafs = OrderedDict()

                                    self.sensor = YList(self)
                                    self._segment_path = lambda: "sensors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, [], name, value)


                                class Sensor(Entity):
                                    """
                                    Sensor number in the Module
                                    
                                    .. attribute:: number  (key)
                                    
                                    	sensor number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2018-06-28'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, self).__init__()

                                        self.yang_name = "sensor"
                                        self.yang_parent_name = "sensors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes))])
                                        self._leafs = OrderedDict([
                                            ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                        ])
                                        self.number = None

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._segment_path = lambda: "sensor" + "[number='" + str(self.number) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, ['number'], name, value)


                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "sensor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "basic-attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                    ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                    ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                    ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                    ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                    ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                    ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                    ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                    ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                    ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                    ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                    ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                    ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                    ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                    ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                            class PortSlots(Entity):
                                """
                                PortSlotTable contains all optics ports in a
                                SPA/PLIM.
                                
                                .. attribute:: port_slot
                                
                                	PortSlot number in the SPA/PLIM
                                	**type**\: list of  		 :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, self).__init__()

                                    self.yang_name = "port-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("port-slot", ("port_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot))])
                                    self._leafs = OrderedDict()

                                    self.port_slot = YList(self)
                                    self._segment_path = lambda: "port-slots"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, [], name, value)


                                class PortSlot(Entity):
                                    """
                                    PortSlot number in the SPA/PLIM
                                    
                                    .. attribute:: number  (key)
                                    
                                    	portslot number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port
                                    
                                    	Port string
                                    	**type**\:  :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2018-06-28'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, self).__init__()

                                        self.yang_name = "port-slot"
                                        self.yang_parent_name = "port-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['number']
                                        self._child_classes = OrderedDict([("port", ("port", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port)), ("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes))])
                                        self._leafs = OrderedDict([
                                            ('number', (YLeaf(YType.uint32, 'number'), ['int'])),
                                        ])
                                        self.number = None

                                        self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port()
                                        self.port.parent = self
                                        self._children_name_map["port"] = "port"

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._segment_path = lambda: "port-slot" + "[number='" + str(self.number) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, ['number'], name, value)


                                    class Port(Entity):
                                        """
                                        Port string
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:  :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port, self).__init__()

                                            self.yang_name = "port"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-attributes", ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes))])
                                            self._leafs = OrderedDict()

                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes()
                                            self.basic_attributes.parent = self
                                            self._children_name_map["basic_attributes"] = "basic-attributes"
                                            self._segment_path = lambda: "port"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port, [], name, value)


                                        class BasicAttributes(Entity):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Inventory information
                                            	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes, self).__init__()

                                                self.yang_name = "basic-attributes"
                                                self.yang_parent_name = "port"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo))])
                                                self._leafs = OrderedDict()

                                                self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self._children_name_map["basic_info"] = "basic-info"

                                                self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo()
                                                self.fru_info.parent = self
                                                self._children_name_map["fru_info"] = "fru-info"
                                                self._segment_path = lambda: "basic-attributes"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes, [], name, value)


                                            class BasicInfo(Entity):
                                                """
                                                Inventory information
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms       what the entity in question does
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: chip_hardware_revision
                                                
                                                	chip module hw revision string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: manufacturer_name
                                                
                                                	manufacturer's name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: asset_id_str
                                                
                                                	asset Identification string
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: asset_identification
                                                
                                                	asset Identification
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: manufacturer_asset_tags
                                                
                                                	Manufacture Asset Tags
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: composite_class_code
                                                
                                                	Major&minor class of the entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: memory_size
                                                
                                                	Size of memory associated with       the entity where applicable
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: environmental_monitor_path
                                                
                                                	sysdb name of sensor in the envmon EDM
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: alias
                                                
                                                	useful for storing an entity alias 
                                                	**type**\: str
                                                
                                                	**length:** 0..255
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: group_flag
                                                
                                                	indicates if this entity is group       or not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: new_deviation_number
                                                
                                                	integer value for New Deviation Number 0x88
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: physical_layer_interface_module_type
                                                
                                                	integer value for plim type if     applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unrecognized_fru
                                                
                                                	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: redundancystate
                                                
                                                	integer value for Redundancy State if applicable to this entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: ceport
                                                
                                                	1 if ce port found, 0 if not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: xr_scoped
                                                
                                                	1 if xr scoped, 0 if not
                                                	**type**\: bool
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: unique_id
                                                
                                                	Unique id for an entity
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                        ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                        ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                        ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                        ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                        ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                        ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                        ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                        ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                        ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                        ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                        ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                        ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                        ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                        ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                        ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                        ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                        ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                        ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                        ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                        ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                        ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                        ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                        ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                            class FruInfo(Entity):
                                                """
                                                Field Replaceable Unit (FRU) inventory
                                                information
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	Time operational state is   last changed
                                                	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_up_time
                                                
                                                	Module up time
                                                	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_administrative_state
                                                
                                                	Administrative    state
                                                	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_power_administrative_state
                                                
                                                	Power administrative state
                                                	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_operational_state
                                                
                                                	Operation state
                                                	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_monitor_state
                                                
                                                	Monitor state
                                                	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                                
                                                	**config**\: False
                                                
                                                .. attribute:: module_reset_reason
                                                
                                                	Reset reason
                                                	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                                
                                                	**config**\: False
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime))])
                                                    self._leafs = OrderedDict([
                                                        ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                        ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                        ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                        ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                        ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                    ])
                                                    self.module_administrative_state = None
                                                    self.module_power_administrative_state = None
                                                    self.module_operational_state = None
                                                    self.module_monitor_state = None
                                                    self.module_reset_reason = None

                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                    self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime()
                                                    self.module_up_time.parent = self
                                                    self._children_name_map["module_up_time"] = "module-up-time"
                                                    self._segment_path = lambda: "fru-info"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                                class LastOperationalStateChange(Entity):
                                                    """
                                                    Time operational state is   last changed
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "last-operational-state-change"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                                class ModuleUpTime(Entity):
                                                    """
                                                    Module up time
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: second
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\: int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**config**\: False
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-oper'
                                                    _revision = '2018-06-28'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                        self.yang_name = "module-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                            ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                        ])
                                                        self.time_in_seconds = None
                                                        self.time_in_nano_seconds = None
                                                        self._segment_path = lambda: "module-up-time"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)






                                    class BasicAttributes(Entity):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo>`
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo>`
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo))])
                                            self._leafs = OrderedDict()

                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self._children_name_map["basic_info"] = "basic-info"

                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self
                                            self._children_name_map["fru_info"] = "fru-info"
                                            self._segment_path = lambda: "basic-attributes"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes, [], name, value)


                                        class BasicInfo(Entity):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\: str
                                            
                                            	**length:** 0..255
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if applicable to this entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\: bool
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\: int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                                    ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                                    ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                                    ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                                    ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                                    ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                                    ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                                    ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                                    ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                                    ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                                    ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                                    ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                                    ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                                    ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                                    ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                                    ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                                    ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                                    ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                        class FruInfo(Entity):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	Time operational state is   last changed
                                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_up_time
                                            
                                            	Module up time
                                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_administrative_state
                                            
                                            	Administrative    state
                                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_power_administrative_state
                                            
                                            	Power administrative state
                                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_operational_state
                                            
                                            	Operation state
                                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_monitor_state
                                            
                                            	Monitor state
                                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                            
                                            	**config**\: False
                                            
                                            .. attribute:: module_reset_reason
                                            
                                            	Reset reason
                                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                            
                                            	**config**\: False
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-oper'
                                            _revision = '2018-06-28'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime))])
                                                self._leafs = OrderedDict([
                                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                                ])
                                                self.module_administrative_state = None
                                                self.module_power_administrative_state = None
                                                self.module_operational_state = None
                                                self.module_monitor_state = None
                                                self.module_reset_reason = None

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                                self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime()
                                                self.module_up_time.parent = self
                                                self._children_name_map["module_up_time"] = "module-up-time"
                                                self._segment_path = lambda: "fru-info"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                            class LastOperationalStateChange(Entity):
                                                """
                                                Time operational state is   last changed
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "last-operational-state-change"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                            class ModuleUpTime(Entity):
                                                """
                                                Module up time
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: second
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\: int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**config**\: False
                                                
                                                	**units**\: nanosecond
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-oper'
                                                _revision = '2018-06-28'

                                                def __init__(self):
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                                    self.yang_name = "module-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                                    ])
                                                    self.time_in_seconds = None
                                                    self.time_in_nano_seconds = None
                                                    self._segment_path = lambda: "module-up-time"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                            class BasicAttributes(Entity):
                                """
                                Attributes
                                
                                .. attribute:: basic_info
                                
                                	Inventory information
                                	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo>`
                                
                                	**config**\: False
                                
                                .. attribute:: fru_info
                                
                                	Field Replaceable Unit (FRU) inventory information
                                	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes, self).__init__()

                                    self.yang_name = "basic-attributes"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo))])
                                    self._leafs = OrderedDict()

                                    self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo()
                                    self.basic_info.parent = self
                                    self._children_name_map["basic_info"] = "basic-info"

                                    self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo()
                                    self.fru_info.parent = self
                                    self._children_name_map["fru_info"] = "fru-info"
                                    self._segment_path = lambda: "basic-attributes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes, [], name, value)


                                class BasicInfo(Entity):
                                    """
                                    Inventory information
                                    
                                    .. attribute:: description
                                    
                                    	describes in user\-readable terms       what the entity in question does
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: vendor_type
                                    
                                    	maps to the vendor OID string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: name
                                    
                                    	name string for the entity
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	hw revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: firmware_revision
                                    
                                    	firmware revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: software_revision
                                    
                                    	software revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: chip_hardware_revision
                                    
                                    	chip module hw revision string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: serial_number
                                    
                                    	serial number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: manufacturer_name
                                    
                                    	manufacturer's name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: model_name
                                    
                                    	model name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: asset_id_str
                                    
                                    	asset Identification string
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: asset_identification
                                    
                                    	asset Identification
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_field_replaceable_unit
                                    
                                    	1 if Field Replaceable Unit 0, if not
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: manufacturer_asset_tags
                                    
                                    	Manufacture Asset Tags
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: composite_class_code
                                    
                                    	Major&minor class of the entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: memory_size
                                    
                                    	Size of memory associated with       the entity where applicable
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: environmental_monitor_path
                                    
                                    	sysdb name of sensor in the envmon EDM
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: alias
                                    
                                    	useful for storing an entity alias 
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: group_flag
                                    
                                    	indicates if this entity is group       or not
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: new_deviation_number
                                    
                                    	integer value for New Deviation Number 0x88
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: physical_layer_interface_module_type
                                    
                                    	integer value for plim type if     applicable to this entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: unrecognized_fru
                                    
                                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: redundancystate
                                    
                                    	integer value for Redundancy State if applicable to this entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: ceport
                                    
                                    	1 if ce port found, 0 if not
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: xr_scoped
                                    
                                    	1 if xr scoped, 0 if not
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: unique_id
                                    
                                    	Unique id for an entity
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2018-06-28'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo, self).__init__()

                                        self.yang_name = "basic-info"
                                        self.yang_parent_name = "basic-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                            ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                            ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                            ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                            ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                            ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                            ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                            ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                            ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                            ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                            ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                            ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                            ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                            ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                            ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                            ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                            ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                            ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                            ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                            ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                            ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                            ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                            ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                                class FruInfo(Entity):
                                    """
                                    Field Replaceable Unit (FRU) inventory
                                    information
                                    
                                    .. attribute:: last_operational_state_change
                                    
                                    	Time operational state is   last changed
                                    	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module_up_time
                                    
                                    	Module up time
                                    	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.ModuleUpTime>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module_administrative_state
                                    
                                    	Administrative    state
                                    	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module_power_administrative_state
                                    
                                    	Power administrative state
                                    	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module_operational_state
                                    
                                    	Operation state
                                    	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module_monitor_state
                                    
                                    	Monitor state
                                    	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: module_reset_reason
                                    
                                    	Reset reason
                                    	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-oper'
                                    _revision = '2018-06-28'

                                    def __init__(self):
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo, self).__init__()

                                        self.yang_name = "fru-info"
                                        self.yang_parent_name = "basic-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.ModuleUpTime))])
                                        self._leafs = OrderedDict([
                                            ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                            ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                            ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                            ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                            ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                        ])
                                        self.module_administrative_state = None
                                        self.module_power_administrative_state = None
                                        self.module_operational_state = None
                                        self.module_monitor_state = None
                                        self.module_reset_reason = None

                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange()
                                        self.last_operational_state_change.parent = self
                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                        self.module_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.ModuleUpTime()
                                        self.module_up_time.parent = self
                                        self._children_name_map["module_up_time"] = "module-up-time"
                                        self._segment_path = lambda: "fru-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                                    class LastOperationalStateChange(Entity):
                                        """
                                        Time operational state is   last changed
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        	**units**\: nanosecond
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                            self.yang_name = "last-operational-state-change"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                            ])
                                            self.time_in_seconds = None
                                            self.time_in_nano_seconds = None
                                            self._segment_path = lambda: "last-operational-state-change"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                                    class ModuleUpTime(Entity):
                                        """
                                        Module up time
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        	**units**\: second
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\: int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**config**\: False
                                        
                                        	**units**\: nanosecond
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-oper'
                                        _revision = '2018-06-28'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                            self.yang_name = "module-up-time"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                                ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                            ])
                                            self.time_in_seconds = None
                                            self.time_in_nano_seconds = None
                                            self._segment_path = lambda: "module-up-time"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)







                    class BasicAttributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:  :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo>`
                        
                        	**config**\: False
                        
                        .. attribute:: fru_info
                        
                        	Field Replaceable Unit (FRU) inventory information
                        	**type**\:  :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-oper'
                        _revision = '2018-06-28'

                        def __init__(self):
                            super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes, self).__init__()

                            self.yang_name = "basic-attributes"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("basic-info", ("basic_info", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo)), ("fru-info", ("fru_info", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo))])
                            self._leafs = OrderedDict()

                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"

                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo()
                            self.fru_info.parent = self
                            self._children_name_map["fru_info"] = "fru-info"
                            self._segment_path = lambda: "basic-attributes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes, [], name, value)


                        class BasicInfo(Entity):
                            """
                            Inventory information
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms       what the entity in question does
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: chip_hardware_revision
                            
                            	chip module hw revision string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: manufacturer_name
                            
                            	manufacturer's name
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: asset_id_str
                            
                            	asset Identification string
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: asset_identification
                            
                            	asset Identification
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: manufacturer_asset_tags
                            
                            	Manufacture Asset Tags
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: composite_class_code
                            
                            	Major&minor class of the entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: memory_size
                            
                            	Size of memory associated with       the entity where applicable
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: environmental_monitor_path
                            
                            	sysdb name of sensor in the envmon EDM
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: alias
                            
                            	useful for storing an entity alias 
                            	**type**\: str
                            
                            	**length:** 0..255
                            
                            	**config**\: False
                            
                            .. attribute:: group_flag
                            
                            	indicates if this entity is group       or not
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: new_deviation_number
                            
                            	integer value for New Deviation Number 0x88
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: physical_layer_interface_module_type
                            
                            	integer value for plim type if     applicable to this entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: unrecognized_fru
                            
                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: redundancystate
                            
                            	integer value for Redundancy State if applicable to this entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            .. attribute:: ceport
                            
                            	1 if ce port found, 0 if not
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: xr_scoped
                            
                            	1 if xr scoped, 0 if not
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: unique_id
                            
                            	Unique id for an entity
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-oper'
                            _revision = '2018-06-28'

                            def __init__(self):
                                super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                    ('vendor_type', (YLeaf(YType.str, 'vendor-type'), ['str'])),
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('hardware_revision', (YLeaf(YType.str, 'hardware-revision'), ['str'])),
                                    ('firmware_revision', (YLeaf(YType.str, 'firmware-revision'), ['str'])),
                                    ('software_revision', (YLeaf(YType.str, 'software-revision'), ['str'])),
                                    ('chip_hardware_revision', (YLeaf(YType.str, 'chip-hardware-revision'), ['str'])),
                                    ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                    ('manufacturer_name', (YLeaf(YType.str, 'manufacturer-name'), ['str'])),
                                    ('model_name', (YLeaf(YType.str, 'model-name'), ['str'])),
                                    ('asset_id_str', (YLeaf(YType.str, 'asset-id-str'), ['str'])),
                                    ('asset_identification', (YLeaf(YType.int32, 'asset-identification'), ['int'])),
                                    ('is_field_replaceable_unit', (YLeaf(YType.boolean, 'is-field-replaceable-unit'), ['bool'])),
                                    ('manufacturer_asset_tags', (YLeaf(YType.int32, 'manufacturer-asset-tags'), ['int'])),
                                    ('composite_class_code', (YLeaf(YType.int32, 'composite-class-code'), ['int'])),
                                    ('memory_size', (YLeaf(YType.int32, 'memory-size'), ['int'])),
                                    ('environmental_monitor_path', (YLeaf(YType.str, 'environmental-monitor-path'), ['str'])),
                                    ('alias', (YLeaf(YType.str, 'alias'), ['str'])),
                                    ('group_flag', (YLeaf(YType.boolean, 'group-flag'), ['bool'])),
                                    ('new_deviation_number', (YLeaf(YType.int32, 'new-deviation-number'), ['int'])),
                                    ('physical_layer_interface_module_type', (YLeaf(YType.int32, 'physical-layer-interface-module-type'), ['int'])),
                                    ('unrecognized_fru', (YLeaf(YType.boolean, 'unrecognized-fru'), ['bool'])),
                                    ('redundancystate', (YLeaf(YType.int32, 'redundancystate'), ['int'])),
                                    ('ceport', (YLeaf(YType.boolean, 'ceport'), ['bool'])),
                                    ('xr_scoped', (YLeaf(YType.boolean, 'xr-scoped'), ['bool'])),
                                    ('unique_id', (YLeaf(YType.int32, 'unique-id'), ['int'])),
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
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo, [u'description', u'vendor_type', u'name', u'hardware_revision', u'firmware_revision', u'software_revision', u'chip_hardware_revision', u'serial_number', u'manufacturer_name', u'model_name', u'asset_id_str', u'asset_identification', u'is_field_replaceable_unit', u'manufacturer_asset_tags', u'composite_class_code', u'memory_size', u'environmental_monitor_path', u'alias', u'group_flag', u'new_deviation_number', u'physical_layer_interface_module_type', u'unrecognized_fru', u'redundancystate', u'ceport', u'xr_scoped', u'unique_id'], name, value)



                        class FruInfo(Entity):
                            """
                            Field Replaceable Unit (FRU) inventory
                            information
                            
                            .. attribute:: last_operational_state_change
                            
                            	Time operational state is   last changed
                            	**type**\:  :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                            
                            	**config**\: False
                            
                            .. attribute:: module_up_time
                            
                            	Module up time
                            	**type**\:  :py:class:`ModuleUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.ModuleUpTime>`
                            
                            	**config**\: False
                            
                            .. attribute:: module_administrative_state
                            
                            	Administrative    state
                            	**type**\:  :py:class:`InvAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvAdminState>`
                            
                            	**config**\: False
                            
                            .. attribute:: module_power_administrative_state
                            
                            	Power administrative state
                            	**type**\:  :py:class:`InvPowerAdminState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvPowerAdminState>`
                            
                            	**config**\: False
                            
                            .. attribute:: module_operational_state
                            
                            	Operation state
                            	**type**\:  :py:class:`InvCardState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvCardState>`
                            
                            	**config**\: False
                            
                            .. attribute:: module_monitor_state
                            
                            	Monitor state
                            	**type**\:  :py:class:`InvMonitorState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvMonitorState>`
                            
                            	**config**\: False
                            
                            .. attribute:: module_reset_reason
                            
                            	Reset reason
                            	**type**\:  :py:class:`InvResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper.InvResetReason>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-oper'
                            _revision = '2018-06-28'

                            def __init__(self):
                                super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo, self).__init__()

                                self.yang_name = "fru-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("last-operational-state-change", ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange)), ("module-up-time", ("module_up_time", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.ModuleUpTime))])
                                self._leafs = OrderedDict([
                                    ('module_administrative_state', (YLeaf(YType.enumeration, 'module-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvAdminState', '')])),
                                    ('module_power_administrative_state', (YLeaf(YType.enumeration, 'module-power-administrative-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvPowerAdminState', '')])),
                                    ('module_operational_state', (YLeaf(YType.enumeration, 'module-operational-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvCardState', '')])),
                                    ('module_monitor_state', (YLeaf(YType.enumeration, 'module-monitor-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvMonitorState', '')])),
                                    ('module_reset_reason', (YLeaf(YType.enumeration, 'module-reset-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_oper', 'InvResetReason', '')])),
                                ])
                                self.module_administrative_state = None
                                self.module_power_administrative_state = None
                                self.module_operational_state = None
                                self.module_monitor_state = None
                                self.module_reset_reason = None

                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                self.last_operational_state_change.parent = self
                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"

                                self.module_up_time = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.ModuleUpTime()
                                self.module_up_time.parent = self
                                self._children_name_map["module_up_time"] = "module-up-time"
                                self._segment_path = lambda: "fru-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo, [u'module_administrative_state', u'module_power_administrative_state', u'module_operational_state', u'module_monitor_state', u'module_reset_reason'], name, value)


                            class LastOperationalStateChange(Entity):
                                """
                                Time operational state is   last changed
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                	**units**\: nanosecond
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                    self.yang_name = "last-operational-state-change"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                    ])
                                    self.time_in_seconds = None
                                    self.time_in_nano_seconds = None
                                    self._segment_path = lambda: "last-operational-state-change"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)



                            class ModuleUpTime(Entity):
                                """
                                Module up time
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                	**units**\: second
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\: int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**config**\: False
                                
                                	**units**\: nanosecond
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-oper'
                                _revision = '2018-06-28'

                                def __init__(self):
                                    super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.ModuleUpTime, self).__init__()

                                    self.yang_name = "module-up-time"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time_in_seconds', (YLeaf(YType.int32, 'time-in-seconds'), ['int'])),
                                        ('time_in_nano_seconds', (YLeaf(YType.int32, 'time-in-nano-seconds'), ['int'])),
                                    ])
                                    self.time_in_seconds = None
                                    self.time_in_nano_seconds = None
                                    self._segment_path = lambda: "module-up-time"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.ModuleUpTime, [u'time_in_seconds', u'time_in_nano_seconds'], name, value)








    def clone_ptr(self):
        self._top_entity = Inventory()
        return self._top_entity



